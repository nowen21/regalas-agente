# -*- coding: utf-8 -*-
"""`EP-027·HU-006` · CP-001 de la fase D: el validador del catálogo lee la tabla."""
import os
import tempfile

from django.db import connection
from django.test import TransactionTestCase

from core.estandar.models import Regla
from core.proyectos.models import Proyecto

from .metareglas import CatalogoDelProyecto


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class ElCatalogoLeeLaTabla(TransactionTestCase):
    serialized_rollback = True

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.ruta = os.path.abspath(carpeta.name)
        self.proyecto = Proyecto.objects.create(nombre="Finca", ruta=self.ruta)

    def validar(self):
        return CatalogoDelProyecto(self.ruta, ajustes=_ajustes()).validar()

    def test_con_reglas_en_la_tabla(self):
        Regla.objects.create(proyecto=self.proyecto, codigo="P1", titulo="Centavos", orden=0,
                             exigencia="Todo monto en centavos.\\n\\n**Respaldo:** concreta `03·D1`.".replace("\\n", "\n"))
        Regla.objects.create(proyecto=self.proyecto, codigo="P2", titulo="Sin respaldo", orden=1,
                             exigencia="Algo sin respaldo.")
        hallazgos = self.validar()
        self.assertEqual(1, len(hallazgos))
        self.assertIn("P2", hallazgos[0].mensaje)
        self.assertIn("Respaldo", hallazgos[0].mensaje)

    def test_sin_reglas_en_la_tabla_ni_archivo(self):
        hallazgos = self.validar()
        self.assertEqual(1, len(hallazgos))
        self.assertIn("no tiene", hallazgos[0].mensaje)
