# -*- coding: utf-8 -*-
"""`EP-026·HU-010` · Pruebas de la copia diaria: CP-001 a CP-003 de la fase A.

Con `TransactionTestCase`: la copia lee la base por otra conexión, y desde ella
no se ve lo que una prueba deja sin confirmar.
"""
import datetime
import gzip
import os
import shutil
import tempfile

from django.contrib.sessions.backends.db import SessionStore
from django.db import connection
from django.test import TransactionTestCase

from core.proyectos.models import Proyecto

from . import copia


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class LaCopiaDiaria(TransactionTestCase):
    serialized_rollback = True

    def setUp(self):
        self.destino = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.destino, True)
        raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, raiz, True)
        Proyecto.objects.create(nombre="con ’comillas’ y\nsalto", ruta=raiz)
        sesion = SessionStore()
        sesion["algo"] = "dato"
        sesion.create()

    def test_cp001_la_copia_del_dia_una_sola_vez(self):
        hoy = datetime.date(2026, 10, 6)
        ruta = copia.copiar(self.destino, _ajustes(), hoy=hoy)
        self.assertEqual("cimiento-2026-10-06.sql.gz", os.path.basename(ruta))
        with gzip.open(ruta, "rt", encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("CREATE TABLE `proyectos_proyecto`", texto)
        self.assertIn("CREATE TABLE `historia_cambio`", texto)
        self.assertTrue(copia.hay_de_hoy(self.destino, hoy))

    def test_cp002_se_guardan_las_ultimas_7(self):
        for dia in range(1, 9):
            with open(os.path.join(self.destino, "cimiento-2026-09-%02d.sql.gz" % dia), "w") as f:
                f.write("--\n")
        copia.copiar(self.destino, _ajustes(), hoy=datetime.date(2026, 10, 6))
        quedan = copia.copias(self.destino)
        self.assertEqual(7, len(quedan))
        self.assertEqual("cimiento-2026-10-06.sql.gz", quedan[0])
        self.assertNotIn("cimiento-2026-09-02.sql.gz", quedan)

    def test_cp003_sin_sesiones_y_se_restaura(self):
        ruta = copia.copiar(self.destino, _ajustes(), hoy=datetime.date(2026, 10, 6))
        with gzip.open(ruta, "rt", encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("CREATE TABLE `django_session`", texto)
        self.assertNotIn("INSERT INTO `django_session`", texto)
        cuenta = copia.probar(ruta, _ajustes())
        self.assertEqual(1, cuenta["proyectos_proyecto"])
        self.assertEqual(0, cuenta["django_session"])
        self.assertIn("historia_cambio", cuenta)
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES LIKE %s", [_ajustes()["NAME"] + "_prueba_copia"])
            self.assertEqual((), cursor.fetchall())

    def test_el_estado_dice_si_la_ultima_fallo(self):
        copia.guardar_estado(self.destino, {"fecha": "2026-10-05", "bien": False, "error": "sin base"})
        self.assertFalse(copia.estado(self.destino)["bien"])
