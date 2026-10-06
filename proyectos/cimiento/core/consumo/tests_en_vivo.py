# -*- coding: utf-8 -*-
"""`EP-025·HU-027`: la pantalla se entera en el momento de lo que guarda el vigilante."""
import os
import shutil
import socket
import tempfile
import threading
import time
from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import SimpleTestCase, TestCase

from core.consumo import avisos as modulo_avisos
from core.consumo import vigilante as modulo_vigilante
from core.consumo.avisos import Avisos, avisar_a_cimiento, eventos
from core.consumo.tests import SESION, escribir_jsonl, muestra
from core.consumo.vigilante import VigilanteDeConsumo
from core.cuentas.permisos import CONSULTA
from core.proyectos.models import Proyecto


class ElAvisoDespiertaSinReloj(SimpleTestCase):
    """CP-001."""

    def test_el_que_espera_despierta_con_el_aviso(self):
        visto = Avisos.numero()
        despierto = []
        hilo = threading.Thread(target=lambda: despierto.append(Avisos.esperar(visto)), daemon=True)
        hilo.start()
        Avisos.avisar()
        hilo.join(5)
        self.assertEqual([visto + 1], despierto)

    def test_el_flujo_trae_un_evento_por_aviso(self):
        flujo = eventos()
        self.assertTrue(next(flujo).startswith(":"))
        siguiente = []
        hilo = threading.Thread(target=lambda: siguiente.append(next(flujo)), daemon=True)
        hilo.start()
        Avisos.avisar()
        hilo.join(5)
        self.assertTrue(siguiente and siguiente[0].startswith("event: gasto\n"))

    def test_no_hay_relojes(self):
        plantilla = os.path.join(os.path.dirname(modulo_avisos.__file__), "templates", "consumo", "tablero.html")
        for ruta in (modulo_avisos.__file__, modulo_vigilante.__file__, plantilla):
            with open(ruta, encoding="utf-8") as f:
                fuente = f.read()
            for reloj in ("sleep(", "every ", "setInterval"):
                self.assertNotIn(reloj, fuente, "%s en %s" % (reloj, os.path.basename(ruta)))


class ElVigilanteAvisa(TestCase):
    """CP-002."""

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        os.makedirs(os.path.join(self.base, proyecto.carpeta_claude))
        self.jsonl = os.path.join(self.base, proyecto.carpeta_claude, SESION + ".jsonl")
        self.vigilante = VigilanteDeConsumo(self.base)
        self.vigilante.leer_proyectos()

    def test_avisa_solo_cuando_guardo_algo(self):
        escribir_jsonl(self.jsonl, muestra())
        with mock.patch("core.consumo.vigilante.avisar_a_cimiento") as avisar:
            self.assertTrue(self.vigilante.avisar(self.jsonl))
            self.assertFalse(self.vigilante.avisar(self.jsonl))
        self.assertEqual(1, avisar.call_count)

    def test_con_cimiento_apagado_no_falla_y_no_se_demora(self):
        libre = socket.socket()
        libre.bind(("127.0.0.1", 0))
        puerto = libre.getsockname()[1]
        libre.close()
        inicio = time.monotonic()
        self.assertFalse(avisar_a_cimiento("http://127.0.0.1:%d/gasto/aviso/" % puerto))
        self.assertLess(time.monotonic() - inicio, 2.5)


class LasRutas(TestCase):
    """CP-003 y CP-004."""

    def entrar(self):
        cuenta = get_user_model().objects.create_user("consulta")
        cuenta.groups.add(Group.objects.get(name=CONSULTA))
        self.client.force_login(cuenta)

    def test_la_pantalla_escucha_los_eventos(self):
        self.entrar()
        respuesta = self.client.get("/gasto/")
        self.assertContains(respuesta, 'new EventSource("/gasto/eventos/")')
        self.assertContains(respuesta, 'addEventListener("gasto"')

    def test_los_eventos_piden_cuenta(self):
        self.assertEqual(302, self.client.get("/gasto/eventos/").status_code)
        self.entrar()
        respuesta = self.client.get("/gasto/eventos/")
        self.assertEqual(200, respuesta.status_code)
        self.assertEqual("text/event-stream", respuesta["Content-Type"])
        respuesta.close()

    def test_el_aviso_desde_esta_maquina_sin_cuenta(self):
        antes = Avisos.numero()
        self.assertEqual(204, self.client.post("/gasto/aviso/", REMOTE_ADDR="127.0.0.1").status_code)
        self.assertEqual(antes + 1, Avisos.numero())

    def test_el_aviso_desde_otra_maquina_o_por_get_se_rechaza(self):
        antes = Avisos.numero()
        self.assertEqual(403, self.client.post("/gasto/aviso/", REMOTE_ADDR="10.0.0.5").status_code)
        self.assertEqual(405, self.client.get("/gasto/aviso/", REMOTE_ADDR="127.0.0.1").status_code)
        self.assertEqual(antes, Avisos.numero())
