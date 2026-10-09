# -*- coding: utf-8 -*-
"""`EP-029·HU-001` · Los ajustes de la revisión de pruebas y su estado: CP-001 a CP-005 de la fase A.

Los valores esperados salen de la HU (RN-02 y RN-03), no del código (`08·T8`).
"""
import tempfile
from datetime import timedelta

from django.test import SimpleTestCase, TestCase
from django.utils import timezone

from core.ayuda.textos import CAMPOS
from core.proyectos import ajustes
from core.proyectos.forms import ConfiguracionForm, ProyectoForm
from core.proyectos.models import Proyecto
from core.pruebas.models import PruebasDelProyecto, Revision

REVISION, DIAS = "revision_pruebas", "dias_revision"


class SinValoresPropiosValeLoDeFabrica(SimpleTestCase):
    """CP-001."""

    def test_de_fabrica(self):
        efectivos = ajustes.efectivos()
        self.assertEqual(("solo avisar", "fábrica"), efectivos[REVISION])
        self.assertEqual((7, "fábrica"), efectivos[DIAS])

    def test_el_del_proyecto_manda_solo_para_el(self):
        efectivos = ajustes.efectivos(del_proyecto={REVISION: "no dejar guardar", DIAS: "3"})
        self.assertEqual(("no dejar guardar", "proyecto"), efectivos[REVISION])
        self.assertEqual((3, "proyecto"), efectivos[DIAS])

    def test_el_de_la_base_vale_si_el_proyecto_no_tiene(self):
        self.assertEqual((5, "base"), ajustes.efectivos(base={DIAS: "5"})[DIAS])


class LoQueNoEsValidoSeRechaza(SimpleTestCase):
    """CP-002."""

    def test_una_opcion_que_no_existe(self):
        with self.assertRaises(ValueError):
            ajustes.limpio(REVISION, "avisar siempre")

    def test_cero_dias(self):
        with self.assertRaises(ValueError):
            ajustes.limpio(DIAS, "0")


class LosAjustesSalenEnLosFormulariosConSuAyuda(TestCase):
    """CP-003."""

    def test_los_dos_formularios_los_traen(self):
        for formulario in (ProyectoForm(), ConfiguracionForm()):
            self.assertIn(REVISION, formulario.fields)
            self.assertIn(DIAS, formulario.fields)

    def test_la_ayuda_existe_y_no_usa_terminos_tecnicos(self):
        for clave in (REVISION, DIAS):
            ayuda = CAMPOS["configuracion." + clave]
            texto = str(ayuda).lower()
            for palabra in ("cobertura", "coverage", "commit"):
                self.assertNotIn(palabra, texto, "%s dice «%s»" % (clave, palabra))


def _proyecto(nombre="uno"):
    return Proyecto.objects.create(nombre=nombre, ruta=tempfile.mkdtemp())


class SeGuardaUnaRevisionYEsLaUltima(TestCase):
    """CP-004."""

    def test_la_de_hoy_es_la_ultima(self):
        proyecto = _proyecto()
        Revision.objects.create(proyecto=proyecto, fecha=timezone.now() - timedelta(days=1),
                                herramienta="coverage.py", porcentaje=40)
        hoy = Revision.objects.create(
            proyecto=proyecto, herramienta="coverage.py", porcentaje=72.5,
            archivos=[{"archivo": "app/vistas.py", "porcentaje": 50, "sin_pruebas": [10, 11]}],
            navegador=Revision.PASARON)
        ultima = Revision.ultima(proyecto)
        self.assertEqual(hoy.pk, ultima.pk)
        self.assertEqual("coverage.py", ultima.herramienta)
        self.assertEqual("app/vistas.py", ultima.archivos[0]["archivo"])
        self.assertEqual(Revision.PASARON, ultima.navegador)


class UnProyectoSinRevisiones(TestCase):
    """CP-005."""

    def test_nunca_revisado(self):
        proyecto = _proyecto()
        self.assertIsNone(Revision.ultima(proyecto))
        self.assertFalse(PruebasDelProyecto.de(proyecto).tiene_parte)

    def test_marcar_que_tiene_la_parte(self):
        proyecto = _proyecto()
        estado = PruebasDelProyecto.de(proyecto)
        estado.tiene_parte = True
        estado.save()
        self.assertTrue(PruebasDelProyecto.de(proyecto).tiene_parte)
