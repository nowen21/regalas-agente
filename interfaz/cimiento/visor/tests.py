# -*- coding: utf-8 -*-
"""Las pruebas de humo del visor: que las pantallas respondan.

No prueban el contenido (los archivos reales cambian a diario): prueban que
cada vista carga sin reventar, que es lo que se rompe cuando una
reestructuración mueve algo de sitio.
"""
from django.test import TestCase


class Pantallas(TestCase):

    def test_inicio_responde(self):
        self.assertEqual(200, self.client.get("/").status_code)

    def test_memoria_responde(self):
        self.assertEqual(200, self.client.get("/memoria/").status_code)
