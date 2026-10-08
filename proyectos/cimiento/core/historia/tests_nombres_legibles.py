# -*- coding: utf-8 -*-
"""`EP-027·HU-005` · CP-001 de la fase B: la historia con nombres legibles."""
from django.contrib.auth.models import Group, User
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext

from core.cuentas.permisos import ADMINISTRADOR
from core.estandar.models import Documento
from core.historia.registro import quien_y_por_que

TEXTO = "# 99 · Capítulo de prueba\n\nNada.\n"


class LaHistoriaDiceNombres(TestCase):

    def setUp(self):
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(self.admin)

    def crear(self, ruta="base/99-prueba.md"):
        with quien_y_por_que(quien="prueba", motivo="prueba"):
            return Documento.objects.create(ruta=ruta, contenido=TEXTO)

    def test_la_tabla_y_la_fila_por_su_nombre(self):
        self.crear()
        html = self.client.get("/historia/", {"tabla": "estandar.documento"}).content.decode()
        self.assertIn("Documento del estándar", html)
        self.assertIn("99 · Capítulo de prueba", html)
        self.assertNotIn("<code>estandar.documento</code>", html)

    def test_lo_que_se_quito_se_sigue_nombrando(self):
        documento = self.crear()
        with quien_y_por_que(quien="prueba", motivo="prueba"):
            documento.delete()
        html = self.client.get("/historia/", {"tabla": "estandar.documento", "accion": "borrar"}).content.decode()
        self.assertIn("99 · Capítulo de prueba", html)

    def test_las_consultas_no_crecen_con_las_filas(self):
        self.crear("base/99-uno.md")
        with CaptureQueriesContext(connection) as pocas:
            self.client.get("/historia/", {"tabla": "estandar.documento"})
        for n in range(8):
            self.crear("base/99-otro-%d.md" % n)
        with CaptureQueriesContext(connection) as muchas:
            self.client.get("/historia/", {"tabla": "estandar.documento"})
        self.assertEqual(len(pocas), len(muchas))
