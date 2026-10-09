# -*- coding: utf-8 -*-
"""`EP-029·HU-003` · El aviso, el commit y la instalación: CP-001 a CP-005 de la fase A.

La lectura sin Django va con `TransactionTestCase`: abre su propia conexión con
PyMySQL, y desde ella no se ve lo que una prueba deja sin confirmar. Las órdenes
de pip se simulan (`08·T3`): ninguna prueba instala nada. Los valores esperados
salen de la HU (RN-02, RN-03 y RN-05), no del código (`08·T8`).
"""
import io
import os
import tempfile
from datetime import timedelta
from types import SimpleNamespace
from unittest import mock

from django.core.management import call_command
from django.db import connection
from django.test import SimpleTestCase, TestCase, TransactionTestCase
from django.utils import timezone

from core.comun import AVISO, FALLA, Proyecto as Carpeta
from core.enganches.sesion import ArranqueDeSesion
from core.herramientas.instalar import PLANTILLA_PRE_COMMIT
from core.proyectos.models import AjusteDelProyecto, Proyecto
from core.pruebas import parte as modulo_parte
from core.pruebas.aviso import NUNCA, SIN_PARTE, RevisionDelProyecto
from core.pruebas.models import PruebasDelProyecto, Revision
from core.pruebas.parte import ParteQueRevisa


def _ajustes():
    d = connection.settings_dict
    return {"NAME": d["NAME"], "USER": d["USER"], "PASSWORD": d["PASSWORD"], "HOST": d["HOST"], "PORT": d["PORT"]}


def _carpeta(test, *archivos):
    tmp = tempfile.TemporaryDirectory()
    test.addCleanup(tmp.cleanup)
    for archivo in archivos:
        ruta = os.path.join(tmp.name, *archivo.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        open(ruta, "w").close()
    return tmp.name


class ConProyecto(TransactionTestCase):
    # Deja la base como estaba: sin esto, los datos de las migraciones se pierden
    # para las clases que corren después (la convención de Cimiento).
    serialized_rollback = True

    def proyecto(self, parte=True, dias_desde=None, estricto=None):
        ruta = _carpeta(self)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        PruebasDelProyecto.objects.create(proyecto=proyecto, tiene_parte=parte)
        if dias_desde is not None:
            Revision.objects.create(proyecto=proyecto, fecha=timezone.now() - timedelta(days=dias_desde))
        if estricto:
            AjusteDelProyecto.objects.create(proyecto=proyecto, clave="revision_pruebas", valor=estricto)
        return ruta

    def avisos(self, ruta):
        return RevisionDelProyecto(ruta, ajustes=_ajustes()).avisos()


class AvisaLoQueFalta(ConProyecto):
    """CP-001."""

    def test_vencida(self):
        textos, detiene = self.avisos(self.proyecto(dias_desde=12))
        self.assertEqual(1, len(textos))
        self.assertIn("hace 12 días", textos[0])
        self.assertIn("Toca hacer otra", textos[0])
        self.assertFalse(detiene)

    def test_nunca(self):
        self.assertEqual([NUNCA], self.avisos(self.proyecto())[0])

    def test_sin_la_parte(self):
        self.assertIn(SIN_PARTE, self.avisos(self.proyecto(parte=False, dias_desde=1))[0])

    def test_al_dia(self):
        self.assertEqual(([], False), self.avisos(self.proyecto(dias_desde=2)))


class CallaCuandoNoCorresponde(ConProyecto):
    """CP-002."""

    def test_con_nada(self):
        self.assertEqual(([], False), self.avisos(self.proyecto(dias_desde=30, estricto="nada")))

    def test_sin_registro(self):
        self.assertEqual(([], False), self.avisos(_carpeta(self)))

    def test_el_arranque_trae_el_aviso(self):
        ruta = self.proyecto(dias_desde=12)
        with mock.patch.object(RevisionDelProyecto, "ajustes", lambda self: _ajustes()):
            hallazgos = ArranqueDeSesion(Carpeta(ruta)).revisar_pruebas()
        self.assertEqual([AVISO], [h.severidad for h in hallazgos])
        self.assertIn("hace 12 días", hallazgos[0].mensaje)


class ElCommit(ConProyecto):
    """CP-003."""

    def correr_pruebas(self, ruta):
        from core.herramientas.validar import Consola
        salida = io.StringIO()
        with mock.patch.object(RevisionDelProyecto, "ajustes", lambda self: _ajustes()), \
                mock.patch("sys.stdout", salida):
            return Consola().correr(["pruebas", "--raiz", ruta]), salida.getvalue()

    def test_no_dejar_guardar_falla(self):
        codigo, salida = self.correr_pruebas(self.proyecto(dias_desde=12, estricto="no dejar guardar"))
        self.assertEqual(1, codigo)
        self.assertIn("no deja guardar", salida)

    def test_solo_avisar_deja_pasar(self):
        codigo, _ = self.correr_pruebas(self.proyecto(dias_desde=12))
        self.assertEqual(0, codigo)

    def test_la_plantilla_lo_llama_y_rechaza(self):
        self.assertIn('validar.py" pruebas --raiz "$(pwd)" || {', PLANTILLA_PRE_COMMIT)


class Falsa:
    """Hace de pip y de Python: responde lo que se le diga a cada orden."""

    def __init__(self, tiene_coverage=False):
        self.tiene_coverage = tiene_coverage
        self.ordenes = []

    def __call__(self, partes, **_):
        self.ordenes.append(partes)
        codigo = 0 if (partes[1:3] != ["-c", "import coverage"] or self.tiene_coverage) else 1
        return SimpleNamespace(returncode=codigo, stdout="", stderr="")


def _django(test):
    return _carpeta(test, "manage.py", ".venv/Scripts/python.exe")


class ElInstaladorPoneCoverage(SimpleTestCase):
    """CP-004."""

    def test_le_falta(self):
        falsa = Falsa()
        pasos, tiene, puesta = ParteQueRevisa(ejecutar=falsa).poner(_django(self), aplicar=True)
        self.assertEqual((True, True), (tiene, puesta))
        self.assertIn(["-m", "pip", "install", "coverage"], [o[1:] for o in falsa.ordenes])
        self.assertEqual([modulo_parte.INSTALAR], pasos)

    def test_ya_la_tenia(self):
        falsa = Falsa(tiene_coverage=True)
        pasos, tiene, puesta = ParteQueRevisa(ejecutar=falsa).poner(_django(self), aplicar=True)
        self.assertEqual((True, False), (tiene, puesta))
        self.assertNotIn("install", [p for o in falsa.ordenes for p in o])

    def test_sin_lenguaje(self):
        falsa = Falsa()
        pasos, tiene, _ = ParteQueRevisa(ejecutar=falsa).poner(_carpeta(self), aplicar=True)
        self.assertFalse(tiene)
        self.assertEqual([modulo_parte.SIN_LENGUAJE], pasos)
        self.assertEqual([], falsa.ordenes)


class ElDesinstaladorQuitaSoloLoSuyo(TestCase):
    """CP-005."""

    def test_la_puso_cimiento(self):
        falsa = Falsa()
        pasos = ParteQueRevisa(ejecutar=falsa).quitar(_django(self), puesta=True, aplicar=True)
        self.assertEqual([modulo_parte.QUITAR], pasos)
        self.assertIn(["-m", "pip", "uninstall", "-y", "coverage"], [o[1:] for o in falsa.ordenes])

    def test_era_del_proyecto(self):
        falsa = Falsa()
        pasos = ParteQueRevisa(ejecutar=falsa).quitar(_django(self), puesta=False, aplicar=True)
        self.assertEqual([modulo_parte.SE_QUEDA], pasos)
        self.assertEqual([], falsa.ordenes)

    def test_marcar_y_quitar(self):
        ruta = _carpeta(self)
        proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        call_command("marcar_pruebas", ruta=ruta, tiene=True, puesta=True, stdout=io.StringIO())
        estado = PruebasDelProyecto.de(proyecto)
        self.assertEqual((True, True), (estado.tiene_parte, estado.instalada_por_cimiento))
        salida = io.StringIO()
        call_command("marcar_pruebas", ruta=ruta, quitar=True, stdout=salida)
        self.assertIn("puesta=1", salida.getvalue())
        self.assertFalse(PruebasDelProyecto.objects.filter(proyecto=proyecto).exists())
