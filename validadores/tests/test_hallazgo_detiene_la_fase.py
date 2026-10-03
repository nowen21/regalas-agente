# -*- coding: utf-8 -*-
"""`EP-023 · HU-004 · fase A · CP-002` · Un hallazgo detiene la fase, y ni ella ni su HU cierran.

Mientras el análisis que abrió el hallazgo siga sin aprobar, la fase que sale
del pendiente no puede decir «Cumple» ni su HU «Terminada».
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import fases                # noqa: E402
from comun import FALLA     # noqa: E402

EPICA = "documentacion/epicas/EP-009-algo"
HU = EPICA + "/HU-001-una-cosa"
FASE = HU + "/A-EP-009-HU-001-la-fase"
PENDIENTE = EPICA + "/pendientes/110-algo-falla"
MARCA = "> **Aprobado** por el usuario el 2026-10-02, en el turno 3.\n\n"


class UnHallazgoDetieneLaFase(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.escribir(PENDIENTE + "/pendiente.md", "# Pendiente: algo\n")
        self.escribir(PENDIENTE + "/analisis-1.md", "# Análisis 1\n\n" + MARCA)
        self.escribir(FASE + "/plan_trabajo.md",
                      "# Plan\n\n**ORIGEN**: sale del [análisis 1](../../pendientes/110-algo-falla/analisis-1.md).\n")
        self.escribir(FASE + "/estado-fase.md", "# Estado\n\n| Campo | Valor |\n|---|---|\n| **Concepto** | Cumple |\n")
        self.escribir(HU + "/HU-001-una-cosa.md", "# HU-001\n\n| Campo | Valor |\n|---|---|\n| **Estado** | Terminada |\n")

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, relativa, texto):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def detenidas(self):
        return [h.mensaje for h in fases.detenidas_por_un_hallazgo(self.raiz) if h.severidad == FALLA]

    def test_sin_hallazgo_cierra(self):
        self.assertEqual([], self.detenidas())

    def test_con_el_analisis_del_hallazgo_abierto_no_cierran(self):
        self.escribir(PENDIENTE + "/analisis-2.md", "# Análisis 2: lo que falló\n")
        fallas = self.detenidas()
        self.assertEqual(2, len(fallas))
        self.assertTrue(any("la fase dice «Cumple»" in f and "analisis-2.md" in f for f in fallas))
        self.assertTrue(any("la HU dice «Terminada»" in f for f in fallas))

    def test_aprobado_el_analisis_del_hallazgo_vuelve_a_cerrar(self):
        self.escribir(PENDIENTE + "/analisis-2.md", "# Análisis 2: lo que falló\n\n" + MARCA)
        self.assertEqual([], self.detenidas())

    def test_la_fase_en_curso_no_falla(self):
        self.escribir(PENDIENTE + "/analisis-2.md", "# Análisis 2: lo que falló\n")
        self.escribir(FASE + "/estado-fase.md", "# Estado\n\n| Campo | Valor |\n|---|---|\n| **Concepto** | Sin ejecutar |\n")
        self.escribir(HU + "/HU-001-una-cosa.md", "# HU-001\n\n| Campo | Valor |\n|---|---|\n| **Estado** | Lista |\n")
        self.assertEqual([], self.detenidas())


if __name__ == "__main__":
    unittest.main()
