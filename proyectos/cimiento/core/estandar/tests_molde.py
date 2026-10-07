# -*- coding: utf-8 -*-
"""`EP-027·HU-007` · El molde habla de casillas: CP-001 y CP-002 de la fase A.

Lee el estándar aprobado de la base real, sin escribir nada: lo que se prueba
es el texto que el usuario aprobó en «Estándar» → «Propuestas».
"""
import os

from django.test import SimpleTestCase

from core.comun import Proyecto as Carpeta

from .en_base import fuente

CAPITULO = "base/20-meta-reglas/"
M5 = CAPITULO + "reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md"
M9 = CAPITULO + "reglas/M9-toda-regla-declara-si-es-validable.md"
DEL_MOLDE = [M9, CAPITULO + "base.md", CAPITULO + "checklist.md", CAPITULO + "estructura-regla.md"]


def _leer(rel):
    raiz = Carpeta.estandar()
    return fuente(raiz).leer(os.path.join(raiz, *rel.split("/")))


class ElMoldeHablaDeCasillas(SimpleTestCase):

    def test_cp001_m5_dice_casillas_y_su_checklist_esta_al_dia(self):
        texto = _leer(M5)
        self.assertIn("cada parte en su casilla", texto)
        self.assertIn("se arma desde esas casillas", texto)
        self.assertIn("**2026-10-07**", texto)

    def test_cp002_validable_es_una_casilla_con_tres_valores(self):
        for rel in DEL_MOLDE:
            self.assertNotIn("reglas-validables.md", _leer(rel), rel)
        texto = _leer(M9)
        for valor in ("*no*", "*sí, falta el programa*", "*sí*"):
            self.assertIn(valor, texto)
