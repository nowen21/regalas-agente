# -*- coding: utf-8 -*-
"""`EP-026·HU-008` · Pruebas de los reportes: CP-001 a CP-004 de la fase A."""
import io
import shutil
import tempfile
from unittest import mock

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.db import connection
from django.test import TestCase, TransactionTestCase

from core.comun import Proyecto as Carpeta
from core.cuentas.permisos import ADMINISTRADOR
from core.historia import versiones
from core.historia.models import ESTANDAR, Cambio, Version
from core.proyectos.models import Proyecto
from core.validadores.version import VersionDelEstandar

from .avisos import de_los_reportes
from .models import ABIERTO, CORREGIDO, Reporte


def _proyecto(test, nombre="reporta"):
    carpeta = tempfile.mkdtemp()
    test.addCleanup(shutil.rmtree, carpeta, True)
    return Proyecto.objects.create(nombre=nombre, ruta=carpeta)


class ReportarYCorregir(TestCase):
    """CP-001 y CP-002."""

    def setUp(self):
        self.proyecto = _proyecto(self)
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.client.force_login(self.admin)

    def test_reportar_no_sube_version_y_corregir_apunta_a_la_que_corrigio(self):
        antes = Version.objects.filter(ambito=ESTANDAR).count()
        call_command("reportar", proyecto=self.proyecto.ruta, titulo="F8 frena lo autorizado", regla="02·F8",
                     stdout=io.StringIO())
        reporte = Reporte.objects.get()
        self.assertEqual(ABIERTO, reporte.estado)
        self.assertEqual(antes, Version.objects.filter(ambito=ESTANDAR).count())
        self.assertTrue(Cambio.objects.filter(tabla="estandar.reporte", fila=str(reporte.pk)).exists())
        self.assertContains(self.client.get("/estandar/reportes/"), "F8 frena lo autorizado")

        version = versiones.nueva(ESTANDAR, None, "PARCHE", "corrige F8", None, "prueba")
        self.client.post("/estandar/reportes/%d/resolver/" % reporte.pk, {"version": version.pk})
        reporte.refresh_from_db()
        self.assertEqual(CORREGIDO, reporte.estado)
        self.assertEqual(version, reporte.corregido_en)
        self.assertEqual(self.admin, reporte.resuelto_por)


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


class ElProyectoSeEntera(TransactionTestCase):
    """CP-003. Con `TransactionTestCase`: el aviso lee la base por otra conexión."""

    serialized_rollback = True

    def test_se_avisa_una_sola_vez(self):
        proyecto = _proyecto(self)
        version = versiones.nueva(ESTANDAR, None, "MENOR", "corrige", None, "prueba")
        Reporte.objects.create(proyecto=proyecto, titulo="algo mal", quien="agente", estado=CORREGIDO,
                               corregido_en=version)
        texto = de_los_reportes(proyecto.ruta, ajustes=_ajustes())
        self.assertIn("algo mal", texto)
        self.assertIn(version.numero, texto)
        self.assertEqual("", de_los_reportes(proyecto.ruta, ajustes=_ajustes()))
        self.assertTrue(Reporte.objects.get().avisado)


class ElAvisoDeVersionMiraLaBase(TestCase):
    """CP-004."""

    def test_con_el_estandar_congelado_la_vigente_y_las_publicadas_salen_de_la_base(self):
        raiz = Carpeta.estandar()
        with mock.patch("core.estandar.congelado.congelada", return_value=True), \
                mock.patch("core.estandar.congelado.versiones_en_la_base", return_value=["99.1.0", "99.0.0"]):
            self.assertEqual("99.1.0", VersionDelEstandar.vigente(raiz))
            publicadas = VersionDelEstandar(raiz, estandar=raiz).versiones_publicadas()
            self.assertIn("99.0.0", publicadas)
            self.assertIn("56.8.0", publicadas)
