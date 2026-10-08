# -*- coding: utf-8 -*-
"""`EP-027·HU-006` · Pruebas de la fase C: el agente del proyecto recibe sus reglas de la base."""
import os
import tempfile

from django.db import connection
from django.test import TransactionTestCase

from core.estandar.models import Regla
from core.proyectos.models import Proyecto

from .autorizado import REGLAS_PROYECTO, Autorizaciones
from .reglas_del_proyecto import ReglasDelProyecto


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class ConUnProyecto(TransactionTestCase):
    serialized_rollback = True

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.ruta = os.path.abspath(carpeta.name)
        self.proyecto = Proyecto.objects.create(nombre="Finca", ruta=self.ruta)

    def con_reglas(self):
        Regla.objects.create(proyecto=self.proyecto, codigo="P1", titulo="Todo monto se guarda en centavos",
                             exigencia="Centavos.", grupo="Base de datos", orden=0)
        Regla.objects.create(proyecto=self.proyecto, codigo="P2", titulo="Cada finca tiene su carpeta",
                             exigencia="Carpeta.", orden=1,
                             autoriza_escribir="**Autoriza escribir:** `documentacion/fincas/**`")


class ElIndiceLlegaAlAbrir(ConUnProyecto):
    """CP-001."""

    def test_con_reglas_en_la_base(self):
        self.con_reglas()
        texto = ReglasDelProyecto(self.ruta, ajustes=_ajustes()).contexto()
        self.assertIn("REGLAS PROPIAS DEL PROYECTO", texto)
        self.assertIn("P1 · Todo monto se guarda en centavos (Base de datos)", texto)
        self.assertIn("P2 · Cada finca tiene su carpeta", texto)
        self.assertIn("ver_regla --proyecto", texto)

    def test_con_tope_cabe(self):
        self.con_reglas()
        entero = ReglasDelProyecto(self.ruta, ajustes=_ajustes()).contexto()
        corto = ReglasDelProyecto(self.ruta, ajustes=_ajustes()).contexto(tope=len(entero) - 1)
        self.assertLessEqual(len(corto), len(entero) - 1)
        self.assertRegex(corto, r"Se listan \d de 2")

    def test_sin_reglas_en_la_base_nada(self):
        self.assertEqual("", ReglasDelProyecto(self.ruta, ajustes=_ajustes()).contexto())


class ElFrenoDejaLoQueAutorizan(ConUnProyecto):
    """CP-002."""

    def test_desde_la_base(self):
        self.con_reglas()
        autorizadas = Autorizaciones(ajustes=_ajustes()).del_proyecto(self.ruta)
        self.assertEqual([("P2", ["documentacion/fincas/**"])], autorizadas)

    def test_sin_reglas_en_la_base_lee_el_archivo(self):
        archivo = os.path.join(self.ruta, REGLAS_PROYECTO)
        os.makedirs(os.path.dirname(archivo))
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("### P9 · Escribe actas\n\n**Autoriza escribir:** `actas/*.md`\n")
        self.assertEqual([("P9", ["actas/*.md"])], Autorizaciones(ajustes=_ajustes()).del_proyecto(self.ruta))
