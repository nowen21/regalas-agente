# -*- coding: utf-8 -*-
"""El análisis aprobado se cierra cuando terminan las HU de su plan, y solo esas.

La columna «Pasó a» de una fila hecha «de una y sin fase» nombra archivos, y
sus rutas traen HU de otras épicas. Antes se juntaban con la primera épica de
la celda y daban una HU que no existe (`EP-023 HU-012`): el análisis del
pendiente 110 no se cerraba nunca y no dejaba abrir otro (sesión del
2026-10-04, «Corrija»).
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import analisis_en_curso as curso   # noqa: E402


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


class ElPlanLeeBienSusHU(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.analisis = os.path.join(self.raiz, "analisis-1.md")

    def tearDown(self):
        self.tmp.cleanup()

    def hu(self, epica, hu, estado):
        nombre = "HU-%03d-algo" % hu
        _escribir(os.path.join(self.raiz, "documentacion", "epicas", "EP-%03d-algo" % epica,
                               nombre, nombre + ".md"),
                  "| **Estado** | %s |\n" % estado)

    def plan(self, celda):
        _escribir(self.analisis, "## Lo que se tiene que hacer\n\n"
                                 "| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
                                 "| 1 | algo | 1 | %s |\n" % celda)
        return curso._plan_pendiente(self.raiz, self.analisis)

    def test_lo_hecho_de_una_no_espera_ninguna_hu(self):
        celda = ("Este análisis, de una y sin fase: `documentacion/epicas/EP-023-x/HU-007-y/a.md`, "
                 "`documentacion/epicas/EP-004-z/HU-012-w/b.md`, hecho el 2026-10-04")
        self.assertEqual(self.plan(celda), [])

    def test_cada_hu_va_con_su_propia_epica(self):
        self.hu(23, 7, "Terminada")
        self.hu(4, 12, "En curso")
        self.assertEqual(self.plan("EP-023, HU-007; EP-004, HU-012"), ["EP-004 HU-012"])

    def test_la_hu_enlazada_cuenta_una_vez(self):
        self.hu(23, 1, "En curso")
        celda = "EP-023, [HU-001](../../HU-001-algo/HU-001-algo.md)"
        self.assertEqual(self.plan(celda), ["EP-023 HU-001"])

    def test_terminada_la_hu_el_plan_se_cumple(self):
        self.hu(23, 1, "Terminada")
        self.assertEqual(self.plan("EP-023, HU 1"), [])


if __name__ == "__main__":
    unittest.main()
