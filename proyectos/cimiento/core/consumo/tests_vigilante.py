# -*- coding: utf-8 -*-
"""`EP-025·HU-011`: el gasto llega a la base en cuanto Claude Code lo escribe.

El vigilante real (`watchdog`) va con `TransactionTestCase`: corre en otro hilo,
con su propia conexión, y desde ella no se ve lo que una prueba deja sin confirmar.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from unittest import mock

from django.core.management import call_command
from django.db import connection
from django.test import TestCase, TransactionTestCase

from core.consumo.management.commands.vigilar_consumo import parar
from core.consumo.models import Llamada
from core.consumo.tests import SESION, escribir_jsonl, llamada, muestra
from core.consumo.vigilante import VigilanteDeConsumo, numero_guardado, proceso_vivo
from core.proyectos.models import Proyecto


class ConCarpetas:

    def armar(self):
        self.base = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.base, True)
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        self.proyecto = Proyecto.objects.create(nombre="uno", ruta=ruta)
        os.makedirs(os.path.join(self.base, self.proyecto.carpeta_claude))
        self.jsonl = os.path.join(self.base, self.proyecto.carpeta_claude, SESION + ".jsonl")


class LoNuevoSeGuardaCuandoCambia(ConCarpetas, TestCase):
    """CP-001, pasos 1 y 2; `EP-025·HU-025`, CP-004 y CP-005: cada aviso guarda en el acto."""

    def setUp(self):
        self.armar()
        self.vigilante = VigilanteDeConsumo(self.base)
        self.vigilante.leer_proyectos()

    def test_cada_aviso_guarda_en_el_acto_sin_duplicar(self):
        escribir_jsonl(self.jsonl, muestra())
        self.assertTrue(self.vigilante.avisar(self.jsonl))
        self.assertEqual(2, Llamada.objects.count())
        self.assertFalse(self.vigilante.avisar(self.jsonl))
        self.assertEqual(2, Llamada.objects.count())
        escribir_jsonl(self.jsonl, [llamada("m-3")])
        self.assertTrue(self.vigilante.avisar(self.jsonl))
        self.assertEqual(3, Llamada.objects.count())

    def test_lo_de_un_proyecto_inactivo_o_ajeno_no_se_lee(self):
        escribir_jsonl(self.jsonl, muestra())
        Proyecto.objects.filter(pk=self.proyecto.pk).update(activo=False)
        self.vigilante.leer_proyectos()
        ajeno = os.path.join(self.base, "otra-carpeta", SESION + ".jsonl")
        os.makedirs(os.path.dirname(ajeno))
        escribir_jsonl(ajeno, muestra())
        for ruta in (self.jsonl, ajeno, os.path.join(tempfile.gettempdir(), "x.jsonl"), self.jsonl + ".txt"):
            self.assertFalse(self.vigilante.avisar(ruta))
        self.assertEqual(0, Llamada.objects.count())

    def test_un_proyecto_nuevo_entra_con_su_primer_aviso(self):
        """`EP-025·HU-025 · CP-005` · La lista se relee cuando llega una carpeta que no conoce."""
        ruta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, ruta, True)
        nuevo = Proyecto.objects.create(nombre="dos", ruta=ruta)
        self.assertNotIn(nuevo.carpeta_claude.lower(), self.vigilante.proyectos)
        jsonl = os.path.join(self.base, nuevo.carpeta_claude, SESION + ".jsonl")
        os.makedirs(os.path.dirname(jsonl))
        escribir_jsonl(jsonl, muestra())
        self.assertTrue(self.vigilante.avisar(jsonl))
        self.assertEqual(2, Llamada.objects.filter(proyecto=nuevo).count())

    def test_un_archivo_que_falla_no_tumba_al_vigilante(self):
        """`EP-025·HU-015` · Lo que tumbó al vigilante al aplicar la migración `0004`."""
        escribir_jsonl(self.jsonl, muestra())
        with mock.patch("core.consumo.vigilante.GuardadoDeConsumo.leer_archivo", side_effect=RuntimeError("columna")):
            self.assertFalse(self.vigilante.avisar(self.jsonl))
        self.assertIn("columna", self.vigilante.ultimo_error)
        self.assertTrue(self.vigilante.avisar(self.jsonl))

    def test_al_arrancar_lee_lo_que_quedo(self):
        escribir_jsonl(self.jsonl, muestra())
        self.vigilante.arrancar()
        self.assertEqual(2, Llamada.objects.count())

    def test_no_tiene_relojes(self):
        """`EP-025·HU-025 · CP-004`, paso 4: ningún intervalo decide cuándo se guarda."""
        import core.consumo.vigilante as modulo
        with open(modulo.__file__, encoding="utf-8") as f:
            fuente = f.read()
        for reloj in ("sleep(", "CADA", "LISTA_CADA", "time.monotonic"):
            self.assertNotIn(reloj, fuente)


class ElVigilanteDeVerdad(ConCarpetas, TransactionTestCase):
    """CP-001, paso 3: `watchdog` avisa y lo escrito llega sin que nada lo pida."""

    serialized_rollback = True

    def setUp(self):
        self.armar()

    def test_lo_escrito_llega_solo(self):
        parar = threading.Event()
        vigilante = VigilanteDeConsumo(self.base)

        def correr():
            try:
                vigilante.correr(parar)
            finally:
                connection.close()

        hilo = threading.Thread(target=correr, daemon=True)
        hilo.start()
        time.sleep(1.5)
        escribir_jsonl(self.jsonl, muestra())
        inicio = time.monotonic()
        while time.monotonic() - inicio < 5 and Llamada.objects.count() < 2:
            time.sleep(0.25)
        llego = time.monotonic() - inicio
        parar.set()
        hilo.join(10)
        self.assertFalse(hilo.is_alive())
        self.assertEqual(2, Llamada.objects.count())
        self.assertLess(llego, 5)


class LaTelemetriaYaNoEsta(TestCase):
    """`EP-025·HU-012 · CP-001`: la ruta de la telemetría salió."""

    def test_v1_logs_no_existe(self):
        from django.urls import Resolver404, resolve
        with self.assertRaises(Resolver404):
            resolve("/v1/logs")
        self.assertFalse(os.path.exists(os.path.join(os.path.dirname(__file__), "telemetria.py")))


class SeArrancaYSeDetiene(TestCase):
    """CP-002, pasos 1 y 2."""

    def setUp(self):
        carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, carpeta, True)
        self.archivo = os.path.join(carpeta, "vigilar-consumo.pid")
        self.dormido = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
        self.addCleanup(self.dormido.kill)
        with open(self.archivo, "w", encoding="utf-8") as f:
            f.write(str(self.dormido.pid))

    def test_parar_detiene_el_proceso_y_borra_su_numero(self):
        self.assertTrue(proceso_vivo(self.dormido.pid))
        self.assertIn("detenido", parar(self.archivo))
        self.dormido.wait(10)
        self.assertFalse(proceso_vivo(self.dormido.pid))
        self.assertFalse(os.path.exists(self.archivo))
        self.assertIn("no estaba corriendo", parar(self.archivo))

    def test_si_ya_corre_uno_no_arranca_otro(self):
        salida = io.StringIO()
        with mock.patch("core.consumo.management.commands.vigilar_consumo.archivo_del_numero",
                        return_value=self.archivo), \
                mock.patch("core.consumo.management.commands.vigilar_consumo.VigilanteDeConsumo") as vigilante:
            call_command("vigilar_consumo", stdout=salida)
        vigilante.assert_not_called()
        self.assertIn("ya corre", salida.getvalue())
        self.assertEqual(self.dormido.pid, numero_guardado(self.archivo))
