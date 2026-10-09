# -*- coding: utf-8 -*-
"""`EP-029·HU-006` · El visor viejo salió del estándar: CP-001 de la fase A.

Lee el repositorio real: lo que se comprueba es justamente que ya no está.
"""
import os

from django.test import SimpleTestCase

from core.pruebas.lenguaje import DJANGO, reconocer

CIMIENTO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ESTANDAR = os.path.dirname(os.path.dirname(CIMIENTO))


class ElVisorViejoSalio(SimpleTestCase):
    """CP-001."""

    def test_la_carpeta_no_existe(self):
        self.assertFalse(os.path.exists(os.path.join(ESTANDAR, "interfaz")))

    def test_nada_vivo_la_nombra(self):
        for rel in (".claude/settings.json", "anatomia/componentes-del-agente.md", "anatomia/mapa-del-sitio.md"):
            with open(os.path.join(ESTANDAR, *rel.split("/")), encoding="utf-8") as f:
                self.assertNotIn("interfaz/", f.read(), rel)

    def test_el_estandar_es_un_solo_programa_cimiento(self):
        lenguaje = reconocer(ESTANDAR)
        self.assertEqual(DJANGO, lenguaje.nombre)
        self.assertEqual(os.path.normcase(CIMIENTO), os.path.normcase(os.path.abspath(lenguaje.carpeta)))
