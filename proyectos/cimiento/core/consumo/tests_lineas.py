# -*- coding: utf-8 -*-
"""`EP-025·HU-025`: cada línea del `.jsonl` queda en la base, sin claves y una sola vez.

La clave de prueba se arma al correr: escrita entera en el archivo, el control de
secretos la detendría antes de llegar al repositorio.
"""
import io
import os
import shutil
import tempfile

from django.core.management import call_command
from django.test import TestCase

from core.consumo.guardar import GuardadoDeConsumo
from core.consumo.models import AvanceDeLectura, LineaDeSesion, Llamada
from core.consumo.tests import SESION, escribir_jsonl, llamada, muestra
from core.enganches.enmascarar import MARCA
from core.proyectos.models import Proyecto


def clave_de_prueba():
    # Una forma que el `Enmascarador` reconoce; las de Anthropic no las conoce
    # todavía (hallazgo anotado en el resumen de la sesión del 2026-10-05).
    return "gh" + "p_" + "q7Rb2LmX9vTz4KpW8nHc3YdF6gJs1AeU"


def linea_con_clave():
    return {"type": "user", "sessionId": SESION, "timestamp": "2026-10-05T10:00:02Z", "isMeta": True,
            "message": {"role": "user", "content": "la clave es " + clave_de_prueba()}}


class LasLineasQuedanEnLaBase(TestCase):
    """CP-001, CP-002 y CP-003."""

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        os.makedirs(os.path.join(self.base, self.proyecto.carpeta_claude))
        self.jsonl = os.path.join(self.base, self.proyecto.carpeta_claude, SESION + ".jsonl")
        escribir_jsonl(self.jsonl, muestra() + [linea_con_clave()])
        self.guardado = GuardadoDeConsumo(self.proyecto, self.base)

    def lineas_del_archivo(self):
        with open(self.jsonl, encoding="utf-8") as f:
            return [l for l in f.read().split("\n") if l.strip()]

    def test_cada_linea_queda_con_la_clave_tapada(self):
        nuevo = self.guardado.leer_archivo(self.jsonl)
        self.assertEqual(len(self.lineas_del_archivo()), nuevo["lineas"])
        self.assertEqual(len(self.lineas_del_archivo()), LineaDeSesion.objects.count())
        textos = " ".join(LineaDeSesion.objects.values_list("texto", flat=True))
        self.assertNotIn(clave_de_prueba(), textos)
        self.assertIn(MARCA, textos)
        self.assertEqual(1, LineaDeSesion.objects.filter(tapadas__gt=0).count())
        self.assertEqual(2, Llamada.objects.count())
        fila = LineaDeSesion.objects.order_by("posicion").first()
        self.assertEqual((self.proyecto.carpeta_claude + "/" + SESION + ".jsonl", 0), (fila.archivo, fila.posicion))

    def test_la_ultima_linea_sin_salto_espera(self):
        escribir_jsonl(self.jsonl, [], crudo_al_final='{"type": "assistant"')
        self.guardado.leer_archivo(self.jsonl)
        self.assertEqual(len(self.lineas_del_archivo()) - 1, LineaDeSesion.objects.count())

    def test_leer_otra_vez_no_duplica(self):
        self.guardado.leer_archivo(self.jsonl)
        antes = (LineaDeSesion.objects.count(), Llamada.objects.count())
        AvanceDeLectura.objects.update(posicion=0, tamano=0, modificado=0)
        self.guardado.leer_archivo(self.jsonl)
        self.assertEqual(antes, (LineaDeSesion.objects.count(), Llamada.objects.count()))

    def test_desde_cero_trae_lo_que_ya_estaba_sin_duplicar(self):
        self.guardado.leer_archivo(self.jsonl)
        LineaDeSesion.objects.all().delete()           # como antes de esta HU: conteos sin líneas
        call_command("leer_consumo", "--desde-cero", stdout=io.StringIO())
        # La orden lee de la carpeta de Claude Code de verdad; aquí se usa la de prueba.
        AvanceDeLectura.objects.update(posicion=0, tamano=0, modificado=0)
        self.guardado.leer_archivo(self.jsonl)
        self.assertEqual(len(self.lineas_del_archivo()), LineaDeSesion.objects.count())
        self.assertEqual(2, Llamada.objects.count())

    def test_un_archivo_reescrito_conserva_las_dos_versiones(self):
        self.guardado.leer_archivo(self.jsonl)
        antes = LineaDeSesion.objects.count()
        with open(self.jsonl, "w", encoding="utf-8"):
            pass
        escribir_jsonl(self.jsonl, [llamada("m-9")])
        self.guardado.leer_archivo(self.jsonl)
        self.assertEqual(antes + 1, LineaDeSesion.objects.count())
