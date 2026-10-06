# -*- coding: utf-8 -*-
"""`EP-025·HU-026`, fase B: la ayuda de «Gasto» describe la pantalla nueva."""
from django.template.loader import render_to_string
from django.test import SimpleTestCase


class LaAyudaDeGasto(SimpleTestCase):
    """CP-001."""

    def test_nombra_la_franja_las_pestanas_y_el_boton(self):
        texto = render_to_string("ayuda/secciones/gasto.html")
        for parte in ("franja", "Resumen", "Dónde se gasta", "Contexto", "Ahorro", "Actividad", "↻ Actualizar"):
            self.assertIn(parte, texto)
        self.assertNotIn("10 segundos", texto)

    def test_dice_que_se_actualiza_sola(self):
        """`EP-025·HU-027`, fase B · CP-001."""
        texto = render_to_string("ayuda/secciones/gasto.html")
        self.assertIn("lo nuevo aparece solo", texto)
        self.assertIn("se actualiza sola", texto)
