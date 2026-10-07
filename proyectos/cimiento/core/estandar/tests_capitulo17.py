# -*- coding: utf-8 -*-
"""`EP-028·HU-001` · El capítulo 17 rige para todo proyecto con pantallas: CP-001 y CP-002.

El texto del capítulo se lee del estándar aprobado en la base real, sin escribir.
"""
import os
import tempfile

from django.db import connection
from django.test import SimpleTestCase, TransactionTestCase

from core.comun import Proyecto as Carpeta
from core.enganches.configuracion import ConfiguracionDelProyecto
from core.herramientas.recuperar import RecuperadorDeReglas
from core.proyectos.ajustes import AJUSTES, CAPITULOS_OPT_IN

from .en_base import fuente

CAPITULO = "base/17-interfaz.md"


def _capitulo():
    raiz = Carpeta.estandar()
    return fuente(raiz).leer(os.path.join(raiz, *CAPITULO.split("/")))


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class ElCapituloRigeSiempre(TransactionTestCase):
    """CP-001."""

    serialized_rollback = True

    def test_cp001_sin_opt_in_ni_ajuste_y_un_claude_md_viejo_no_lo_apaga(self):
        self.assertNotIn("opt-in", _capitulo().splitlines()[0])
        self.assertNotIn("17", CAPITULOS_OPT_IN)
        self.assertNotIn("opt_in_17", AJUSTES)
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        with open(os.path.join(carpeta.name, "CLAUDE.md"), "w", encoding="utf-8") as f:
            f.write("- **Patrón opt-in `17` (interfaz / UI):** no\n- **Patrón opt-in `15` (registros inmutables):** no\n")
        apagados = RecuperadorDeReglas.opt_in_apagados(
            carpeta.name, configuracion=ConfiguracionDelProyecto(carpeta.name, ajustes=_ajustes()))
        self.assertNotIn("17", apagados)
        self.assertIn("15", apagados)


class LaPantallaOrientaSola(SimpleTestCase):
    """CP-002."""

    def test_cp002_i7_existe_con_su_checklist_e_i5_pide_la_plantilla_instalada(self):
        texto = _capitulo()
        i7 = texto[texto.index("## I7 · La pantalla orienta sola"):]
        self.assertIn("### Checklist", i7)
        i5 = texto[texto.index("## I5"):texto.index("## I6")]
        self.assertIn("plantilla de interfaz instalada", i5)
