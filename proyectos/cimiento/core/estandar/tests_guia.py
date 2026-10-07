# -*- coding: utf-8 -*-
"""`EP-028·HU-002` · La guía de diseño de pantallas: CP-001 y CP-002 de la fase A.

Lee el estándar aprobado de la base real, sin escribir nada.
"""
import os

from django.test import SimpleTestCase

from core.comun import Proyecto as Carpeta

from .en_base import fuente

GUIA = "base/17-guia-de-pantallas.md"
CAPITULO = "base/17-interfaz.md"

# Las 14 secciones del encargo `prompts/prompt-guia-estilo.md`.
SECCIONES = ["Fundamentos visuales", "Jerarquía visual", "Componentes", "Navegación", "Formularios",
             "Tablas y presentación de información", "Estados del sistema", "Lenguaje de interfaz",
             "Accesibilidad", "Pantallas de distintos tamaños", "Patrones de interacción",
             "Reutilización y consistencia", "Documentación", "Cómo crece esta guía"]


def _leer(rel):
    raiz = Carpeta.estandar()
    return fuente(raiz).leer(os.path.join(raiz, *rel.split("/")))


class LaGuia(SimpleTestCase):

    def test_cp001_trae_las_14_secciones_y_el_capitulo_la_enlaza(self):
        guia = _leer(GUIA)
        for n, titulo in enumerate(SECCIONES, 1):
            self.assertIn("## %d. %s" % (n, titulo), guia)
        self.assertIn("(17-guia-de-pantallas.md)", _leer(CAPITULO))

    def test_cp002_cada_seccion_de_construccion_dice_como_con_tabler(self):
        guia = _leer(GUIA)
        partes = guia.split("\n## ")[1:]
        self.assertEqual(14, len(partes))
        for parte in partes:
            self.assertIn("**Qué se exige", parte, parte[:40])
        # La 14 dice cómo crece la guía: no construye nada, no lleva «cómo con Tabler».
        for parte in partes[:13]:
            self.assertIn("**Cómo con Tabler.**", parte, parte[:40])
