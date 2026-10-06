# -*- coding: utf-8 -*-
"""`EP-025·HU-025`, fase B: lo guardado se vuelve a tapar.

La clave se arma al correr y no se repite al fallar (señal S-315).
"""
import io
import shutil
import tempfile

from django.core.management import call_command
from django.test import TestCase

from core.consumo.models import LineaDeSesion
from core.enganches.enmascarar import MARCA
from core.proyectos.models import Proyecto


def clave_anthropic():
    return "sk-" + "ant-" + "api03-" + "q7Rb2LmX9vTz4KpW8nHc3YdF6gJs"


class LoGuardadoSeVuelveATapar(TestCase):
    """CP-001 y CP-002."""

    def setUp(self):
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        # Como quedó guardada antes de que el tapado conociera la forma.
        self.con_clave = LineaDeSesion.objects.create(
            proyecto=proyecto, archivo="c/s.jsonl", huella="a" * 40, posicion=0,
            texto='{"content": "la clave es %s"}' % clave_anthropic())
        self.sin_clave = LineaDeSesion.objects.create(
            proyecto=proyecto, archivo="c/s.jsonl", huella="b" * 40, posicion=50, texto='{"content": "nada"}')

    def correr(self):
        salida = io.StringIO()
        call_command("retapar_lineas", stdout=salida)
        return salida.getvalue()

    def test_la_clave_que_quedo_en_claro_se_tapa(self):
        self.assertIn("1 con claves", self.correr())
        self.con_clave.refresh_from_db()
        self.assertFalse(clave_anthropic() in self.con_clave.texto, "la clave sigue en claro")
        self.assertIn(MARCA, self.con_clave.texto)
        self.assertEqual(1, self.con_clave.tapadas)
        self.sin_clave.refresh_from_db()
        self.assertEqual('{"content": "nada"}', self.sin_clave.texto)

    def test_correrla_otra_vez_no_cambia_nada(self):
        self.correr()
        self.assertIn("0 con claves", self.correr())
        self.con_clave.refresh_from_db()
        self.assertEqual("a" * 40, self.con_clave.huella)
