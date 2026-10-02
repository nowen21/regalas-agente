# -*- coding: utf-8 -*-
"""`EP-023 · HU-001 · CA-06` · Un análisis aprobado trae sus cuatro partes.

Los casos del CP-005 de la fase `A`: el análisis aprobado completo pasa; al que
le falta una sección se le nombra; el abierto todavía no se juzga, porque se
está llenando.
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import analisis   # noqa: E402

SECCIONES = {
    "Cimiento": "### Cimiento: las reglas que aplican y las que chocan\n\nAlgo.\n",
    "El proyecto": "### El proyecto: lo que existe, lo que funciona y lo que falta\n\nAlgo.\n",
    "Lo aprendido": "### Lo aprendido: señales, lecciones y análisis anteriores\n\nAlgo.\n",
    "El entorno": "### El entorno: normas, herramientas y proyectos que heredan\n\nAlgo.\n",
}


def documento(aprobado=True, sin=None):
    marca = "> **Aprobado** por el usuario el 2026-10-01, en el turno 9.\n\n" if aprobado else ""
    partes = "".join(t for n, t in SECCIONES.items() if n != sin)
    return f"# Análisis 1: algo\n\n{marca}## Lo que aportó cada parte\n\n{partes}"


class UnAnalisisAprobadoTraeSusCuatroPartes(unittest.TestCase):

    def escribir(self, raiz, texto, nombre="analisis-1.md"):
        carpeta = os.path.join(raiz, "documentacion", "pendiente")
        os.makedirs(carpeta, exist_ok=True)
        with open(os.path.join(carpeta, nombre), "w", encoding="utf-8") as f:
            f.write(texto)

    def test_el_aprobado_completo_pasa(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento())
            self.assertEqual(analisis.revisar(raiz), [])

    def test_al_aprobado_sin_lo_aprendido_se_le_nombra(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="Lo aprendido"))
            fallas = analisis.revisar(raiz)
            self.assertEqual(len(fallas), 1)
            self.assertIn("«Lo aprendido»", fallas[0])

    def test_al_aprobado_sin_el_entorno_se_le_nombra(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="El entorno"))
            fallas = analisis.revisar(raiz)
            self.assertEqual(len(fallas), 1)
            self.assertIn("«El entorno»", fallas[0])

    def test_el_abierto_incompleto_todavia_no_se_juzga(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(aprobado=False, sin="Cimiento"))
            self.assertEqual(analisis.revisar(raiz), [])

    def test_solo_mira_los_analisis_numerados(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="Cimiento"), nombre="base-cierre.md")
            self.assertEqual(analisis.revisar(raiz), [])

    def test_la_falla_llega_a_validar(self):
        with tempfile.TemporaryDirectory() as raiz:
            self.escribir(raiz, documento(sin="El proyecto"))
            hallazgos = analisis.validar(raiz)
            self.assertEqual(len(hallazgos), 1)


if __name__ == "__main__":
    unittest.main()
