# -*- coding: utf-8 -*-
"""`EP-029·HU-004` · Sin copia local: CP-001 (la ayuda) y CP-002 de la fase A.

El paso 1 de CP-001, que guardar ya no escribe la copia, lo prueban
`tests_configuracion.py` y `tests_opt_in.py`.
"""
import os
import tempfile

from django.test import SimpleTestCase

from core.ayuda.textos import CAMPOS, PANTALLAS
from core.herramientas.instalar import Instalador

AYUDA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ayuda")


class LaAyudaNoNombraLaCopia(SimpleTestCase):
    """CP-001, paso 2."""

    def test_ni_los_textos_ni_el_manual(self):
        self.assertNotIn("configuracion.md", str(CAMPOS) + str(PANTALLAS))
        carpeta = os.path.join(AYUDA, "templates", "ayuda", "secciones")
        for nombre in os.listdir(carpeta):
            with open(os.path.join(carpeta, nombre), encoding="utf-8") as f:
                self.assertNotIn("configuracion.md", f.read(), nombre)


class VolverAInstalarBorraLaCopiaVieja(SimpleTestCase):
    """CP-002."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.ruta = tmp.name
        self.copia = os.path.join(self.ruta, ".agente", "configuracion.md")

    def test_la_borra(self):
        os.makedirs(os.path.dirname(self.copia))
        with open(self.copia, "w", encoding="utf-8") as f:
            f.write("# Configuración de «uno»\n")
        pasos = Instalador.quitar_copia_de_configuracion(self.ruta, aplicar=True)
        self.assertFalse(os.path.exists(self.copia))
        self.assertEqual(1, len(pasos))
        self.assertIn("configuracion.md", pasos[0])

    def test_sin_copia_no_hace_nada(self):
        self.assertEqual([], Instalador.quitar_copia_de_configuracion(self.ruta, aplicar=True))
