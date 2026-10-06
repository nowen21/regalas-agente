# -*- coding: utf-8 -*-
"""`EP-025·HU-015`: lo que corre sin tokens y los candidatos a automatizar."""
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone as tz
from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import SimpleTestCase, TestCase

from core.consumo.guardar import GuardadoDeConsumo
from core.consumo.lector import LectorDeClaudeCode, orden_de
from core.consumo.models import EjecucionDeEnganche, GastoDeArchivo, GastoDeEnganche, GastoDeHerramienta, Pedido
from core.consumo.tablero import GastoDelPeriodo
from core.consumo.tests import SESION, escribir_jsonl, llamada, muestra
from core.cuentas.permisos import CONSULTA
from core.proyectos.models import Proyecto

AHORA = datetime(2026, 10, 5, 12, 0, tzinfo=tz.utc)
HOY = datetime(2026, 10, 5, 10, 0, tzinfo=tz.utc)


def comando(identificador, orden):
    return {"type": "tool_use", "id": identificador, "name": "Bash", "input": {"command": orden}}


def resultado(identificador, texto):
    return {"type": "user", "sessionId": SESION, "timestamp": "2026-10-05T10:00:03Z",
            "message": {"content": [{"type": "tool_result", "tool_use_id": identificador, "content": texto}]}}


class LaOrdenDeUnComando(SimpleTestCase):
    """CP-002, paso 1."""

    def test_solo_el_programa_y_su_orden(self):
        self.assertEqual("git status", orden_de("git status --short"))
        self.assertEqual("python manage.py", orden_de('cd "/c/x" && .venv/Scripts/python.exe manage.py test core'))
        self.assertEqual("python -m unittest", orden_de("python -m unittest core.algo"))
        self.assertEqual("python validar.py", orden_de("python validadores/validar.py fases"))
        self.assertEqual("curl", orden_de("curl https://ejemplo.invalid/clave?x=1"))
        self.assertEqual("echo", orden_de('echo "un texto largo con datos"'))
        self.assertEqual("", orden_de(""))


class LoQueCorreSinTokens(TestCase):
    """CP-001."""

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        os.makedirs(os.path.join(self.base, self.proyecto.carpeta_claude))
        self.jsonl = os.path.join(self.base, self.proyecto.carpeta_claude, SESION + ".jsonl")
        mudo = {"type": "attachment", "sessionId": SESION, "uuid": "u-9", "timestamp": "2026-10-05T10:00:05Z",
                "attachment": {"type": "hook_success", "hookName": "Stop", "hookEvent": "Stop",
                               "command": "Sumando el consumo...", "stdout": ""}}
        escribir_jsonl(self.jsonl, muestra() + [llamada("m-5", contenido=[comando("b-1", "git status --short")]),
                                                resultado("b-1", "x" * 35), mudo])

    def leer(self):
        GuardadoDeConsumo(self.proyecto, self.base).leer_archivo(self.jsonl)

    def test_cada_corrida_queda_guardada_sin_duplicar(self):
        self.assertEqual(3, len(LectorDeClaudeCode(self.jsonl).leer().ejecuciones))
        self.leer()
        self.leer()
        self.assertEqual(3, EjecucionDeEnganche.objects.count())
        self.assertEqual("git status", GastoDeHerramienta.objects.get(identificador="b-1").orden)

    def test_la_seccion_trae_tambien_el_que_no_agrega(self):
        self.leer()
        filas = {f["nombre"]: f for f in GastoDelPeriodo(ahora=AHORA).sin_tokens()}
        self.assertEqual(0, filas["Sumando el consumo..."]["tokens"])
        self.assertEqual(1, filas["Sumando el consumo..."]["veces"])
        self.assertGreater(filas["Revisando las reglas..."]["tokens"], 0)


class CandidatosAAutomatizar(TestCase):
    """CP-002, pasos 2 a 5."""

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=carpeta.name)
        comun = {"proyecto": self.proyecto, "sesion": "s-1", "fecha": HOY}
        for n in range(3):
            GastoDeArchivo.objects.create(identificador="a-%d" % n, ruta="C:/p/grande.md", caracteres=3500, **comun)
            GastoDeHerramienta.objects.create(identificador="h-%d" % n, nombre="Bash", orden="git status",
                                              caracteres=350, **comun)
        for n in range(2):
            GastoDeArchivo.objects.create(identificador="b-%d" % n, ruta="C:/p/chico.md", caracteres=3500, **comun)
            Pedido.objects.create(proyecto=self.proyecto, sesion="s-1", identificador="p-%d" % n, fecha=HOY)
            GastoDeEnganche.objects.create(identificador="e-%d" % n, nombre="Las reglas", evento="UserPromptSubmit",
                                           caracteres=7000, **comun)
        GastoDeEnganche.objects.create(identificador="e-x", nombre="Una vez", evento="UserPromptSubmit",
                                       caracteres=7000, **comun)

    def test_lo_que_se_repite_con_lo_que_se_ahorraria(self):
        candidatos = {(c["tipo"], c["nombre"]): c for c in GastoDelPeriodo(ahora=AHORA).candidatos()}
        # Tres lecturas de 1.000 tokens: se ahorrarían las dos que sobran.
        self.assertEqual(2000, candidatos[("Archivo leído", "C:/p/grande.md")]["ahorro"])
        self.assertNotIn(("Archivo leído", "C:/p/chico.md"), candidatos)
        self.assertEqual(4000, candidatos[("Enganche en cada mensaje", "Las reglas")]["ahorro"])
        self.assertNotIn(("Enganche en cada mensaje", "Una vez"), candidatos)
        self.assertEqual(3, candidatos[("Comando repetido", "git status")]["veces"])

    def test_la_pagina_trae_las_dos_secciones(self):
        cuenta = get_user_model().objects.create_user("consulta")
        cuenta.groups.add(Group.objects.get(name=CONSULTA))
        self.client.force_login(cuenta)
        with mock.patch("core.consumo.tablero.timezone.now", return_value=AHORA):
            # `EP-025·HU-026` · Las dos secciones van en la pestaña Ahorro.
            respuesta = self.client.get("/gasto/pestana/ahorro/")
        self.assertContains(respuesta, "No gasta tokens")
        self.assertContains(respuesta, "Gasta y se puede automatizar")
        self.assertContains(respuesta, "git status")
        self.assertNotContains(respuesta, json.dumps("git status --short"))
