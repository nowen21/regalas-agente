# -*- coding: utf-8 -*-
"""`EP-026·HU-006` · Pruebas de congelar `base/`: CP-001 a CP-004 de la fase A."""
import datetime
import io
import os
import shutil
import tempfile
from unittest import mock

from django.core.management import call_command
from django.test import TestCase

from core.comun import Archivos
from core.comun import Proyecto as Carpeta
from core.enganches.cargador import Cargador
from core.enganches.freno import Freno
from core.herramientas.recuperar import RecuperadorDeReglas
from core.historia import versiones
from core.historia.models import ESTANDAR
from core.proyectos.models import AjusteBase
from core.validadores.guardian_version import VersionDelCambio

from . import congelado, en_base
from .importar import documentos

PERMITIDO = {"fases": [], "reglas": [], "de_una": set(), "corrija": False}
CONGELADA = "core.estandar.congelado.congelada"


class ElFreno(TestCase):
    """CP-001."""

    def test_con_la_marca_detiene_lo_quieto_del_estandar(self):
        raiz = Carpeta.estandar()
        freno = Freno(raiz)
        with mock.patch(CONGELADA, return_value=True):
            for rel in ("base/01-conducta.md", "VERSION", "CHANGELOG.md"):
                self.assertEqual(congelado.MOTIVO, freno.motivo(os.path.join(raiz, rel), PERMITIDO), rel)
            self.assertNotEqual(congelado.MOTIVO, freno.motivo(os.path.join(raiz, "plantillas", "x.md"), PERMITIDO))
        with mock.patch(CONGELADA, return_value=False):
            self.assertNotEqual(congelado.MOTIVO, freno.motivo(os.path.join(raiz, "base", "x.md"), PERMITIDO))

    def test_en_otra_carpeta_no_cuenta(self):
        otra = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, otra, True)
        self.assertFalse(congelado.congelada(otra))


class ElCommit(TestCase):
    """CP-002."""

    def validar(self, preparados, fecha):
        with mock.patch(CONGELADA, return_value=True), \
                mock.patch("core.estandar.congelado.ultima_version_del_estandar", return_value=fecha):
            return VersionDelCambio(Carpeta.estandar(), preparados=preparados).validar()

    def test_base_no_entra_y_plantillas_pide_su_version(self):
        ahora = datetime.datetime.now(datetime.timezone.utc)
        self.assertTrue(self.validar(["base/01-conducta.md"], ahora))
        self.assertTrue(self.validar(["VERSION"], ahora))
        self.assertTrue(self.validar(["plantillas/x.md"], None))
        self.assertTrue(self.validar(["plantillas/x.md"], ahora - datetime.timedelta(days=3650)))
        self.assertEqual([], self.validar(["plantillas/x.md"], ahora))
        self.assertEqual([], self.validar(["proyectos/cimiento/core/x.py"], None))


class CongelarYDescongelar(TestCase):
    """CP-003."""

    def test_congela_alinea_la_version_y_se_deshace(self):
        call_command("congelar_base", stdout=io.StringIO())
        self.assertEqual(congelado.SI, AjusteBase.objects.get(clave=congelado.CLAVE).valor)
        self.assertGreaterEqual(versiones.ultima(ESTANDAR), versiones.del_archivo())
        call_command("congelar_base", deshacer=True, stdout=io.StringIO())
        self.assertFalse(AjusteBase.objects.filter(clave=congelado.CLAVE).exists())


class DondeLeerLasReglas(TestCase):
    """CP-004."""

    def test_dicen_ver_estandar(self):
        raiz = Carpeta.estandar()
        docs = {}
        for ruta, completa in documentos(raiz):
            with io.open(completa, encoding="utf-8", newline="") as f:
                docs[ruta] = f.read()
        lector = en_base.ArchivosEnBase(raiz, docs)
        texto = RecuperadorDeReglas(raiz, lector).como_texto("Hágalo y corra las pruebas")
        self.assertIn("ver_estandar", texto)
        self.assertNotIn("ver_estandar", RecuperadorDeReglas(raiz, Archivos()).como_texto("Hágalo y corra las pruebas"))
        self.assertIn("ver_estandar", Cargador.instruccion(raiz, True))
        self.assertNotIn("ver_estandar", Cargador.instruccion(raiz))
