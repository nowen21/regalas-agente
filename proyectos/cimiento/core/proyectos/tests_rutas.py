# -*- coding: utf-8 -*-
"""`EP-025·HU-014 · CP-001`: las rutas de los avisos salen como diga el ajuste.

Va con `TransactionTestCase`: la lectura del ajuste abre su propia conexión con
PyMySQL, y desde ella no se ve lo que una prueba deja sin confirmar.
"""
import os
import tempfile
from unittest import mock

from django.db import connection
from django.test import TransactionTestCase

from core.comun import proyecto as modulo
from core.comun.proyecto import Proyecto as Carpeta
from core.enganches.niveles import NivelesDelProyecto
from core.proyectos.models import AjusteBase, AjusteDelProyecto, Proyecto


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class LasRutasSegunElAjuste(TransactionTestCase):

    serialized_rollback = True

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.raiz = carpeta.name
        self.archivo = os.path.join(self.raiz, "docs", "a.md")
        parche = mock.patch.object(NivelesDelProyecto, "ajustes", return_value=_ajustes())
        parche.start()
        self.addCleanup(parche.stop)
        modulo._RUTAS.clear()
        self.addCleanup(modulo._RUTAS.clear)

    def mostrar(self, ruta=None):
        modulo._RUTAS.clear()
        return Carpeta(self.raiz).mostrar(ruta or self.archivo)

    def test_completas_en_un_proyecto_registrado(self):
        proyecto = Proyecto.objects.create(nombre="uno", ruta=self.raiz)
        AjusteDelProyecto.objects.create(proyecto=proyecto, clave="rutas_en_avisos", valor="completas")
        self.assertEqual(os.path.abspath(self.archivo).replace("\\", "/"), self.mostrar())

    def test_relativas_por_el_proyecto_o_por_la_base(self):
        proyecto = Proyecto.objects.create(nombre="uno", ruta=self.raiz)
        AjusteBase.objects.create(clave="rutas_en_avisos", valor="completas")
        AjusteDelProyecto.objects.create(proyecto=proyecto, clave="rutas_en_avisos", valor="relativas")
        self.assertEqual("docs/a.md", self.mostrar())

    def test_sin_registro_relativas_aunque_la_base_diga_completas(self):
        AjusteBase.objects.create(clave="rutas_en_avisos", valor="completas")
        self.assertEqual("docs/a.md", self.mostrar())

    def test_lo_de_afuera_sale_completo(self):
        with tempfile.TemporaryDirectory() as afuera:
            ruta = os.path.join(afuera, "b.md")
            self.assertEqual(os.path.abspath(ruta).replace("\\", "/"), self.mostrar(ruta))
