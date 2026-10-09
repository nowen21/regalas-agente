# -*- coding: utf-8 -*-
"""`EP-025·HU-029`: el vigilante se reinicia solo cuando cambia el código de Cimiento."""
import os
import shutil
import tempfile
import threading
import time

from django.test import SimpleTestCase

from core.consumo.reinicio import CIMIENTO, Reinicio, es_codigo, orden_del_vigilante
from core.consumo.vigilante import VigilanteDeConsumo, numero_guardado


def ruta(*partes):
    return os.path.join(CIMIENTO, *partes)


class QueCuentaComoCodigo(SimpleTestCase):
    """CP-001, pasos 1 y 2."""

    def test_el_codigo_de_cimiento_cuenta(self):
        self.assertTrue(es_codigo(ruta("core", "consumo", "guardar.py")))
        self.assertTrue(es_codigo(ruta("config", "settings", "base.py")))

    def test_pruebas_entornos_y_lo_que_no_es_python_no_cuentan(self):
        for otra in (ruta("core", "consumo", "tests_trabajo_abierto.py"), ruta("core", "x", "test_y.py"),
                     ruta(".venv", "Lib", "site-packages", "django", "x.py"),
                     ruta("core", "consumo", "__pycache__", "guardar.py"), ruta("node_modules", "a", "b.py"),
                     ruta(".agente", "x.py"), ruta(".git", "hooks", "x.py"),
                     ruta("core", "consumo", "templates", "consumo", "tablero.html"),
                     os.path.join(tempfile.gettempdir(), "x.py")):
            self.assertFalse(es_codigo(otra), otra)

    def test_el_nuevo_se_arranca_con_el_mismo_python_y_manage(self):
        orden = orden_del_vigilante()
        self.assertEqual([os.path.join(CIMIENTO, "manage.py"), "vigilar_consumo"], orden[1:])
        self.assertTrue(os.path.isfile(orden[0]))


class ElRelevo(SimpleTestCase):
    """CP-001, paso 3, y CP-002, pasos 1 y 2."""

    def setUp(self):
        self.carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.carpeta, True)
        self.archivo = os.path.join(self.carpeta, "vigilar-consumo.pid")
        self.parar = threading.Event()
        self.lanzados = []
        with open(self.archivo, "w", encoding="utf-8") as f:
            f.write("111")

    def reinicio(self, escribe_el_nuevo=True, espera=3):
        def lanzar(orden, **_):
            self.lanzados.append(orden)
            if escribe_el_nuevo:            # el nuevo: un proceso vivo que no es el viejo
                with open(self.archivo, "w", encoding="utf-8") as f:
                    f.write(str(os.getpid()))
        return Reinicio(self.parar, orden=["nuevo"], lanzar=lanzar, archivo=self.archivo, numero=111,
                        calma=0.3, espera=espera, raiz=CIMIENTO)

    def test_varios_cambios_seguidos_dan_un_solo_reinicio(self):
        reinicio = self.reinicio()
        for nombre in ("guardar.py", "lector.py", "trabajo.py"):
            self.assertTrue(reinicio.aviso(ruta("core", "consumo", nombre)))
        self.assertFalse(reinicio.aviso(ruta("core", "consumo", "tests_x.py")))
        self.assertTrue(self.parar.wait(5))
        self.assertEqual([["nuevo"]], self.lanzados)
        self.assertEqual(os.getpid(), numero_guardado(self.archivo))

    def test_si_el_nuevo_no_arranca_el_viejo_sigue_y_lo_anota(self):
        reinicio = self.reinicio(escribe_el_nuevo=False, espera=1)
        self.assertFalse(reinicio.reiniciar())
        self.assertFalse(self.parar.is_set())
        self.assertEqual(111, numero_guardado(self.archivo))
        self.assertIn("no arrancó", reinicio.ultimo_error)

    def test_si_no_se_puede_lanzar_el_viejo_sigue(self):
        def falla(orden, **_):
            raise OSError("sin permiso")
        reinicio = Reinicio(self.parar, orden=["nuevo"], lanzar=falla, archivo=self.archivo, numero=111, calma=0.1)
        self.assertFalse(reinicio.reiniciar())
        self.assertEqual(111, numero_guardado(self.archivo))
        self.assertIn("sin permiso", reinicio.ultimo_error)


class ArrancaSinConsola(SimpleTestCase):
    """CP-002, paso 3 · Desde el inicio de sesión (`pythonw`) no hay consola: antes eso lo tumbaba."""

    def test_sin_consola_el_mensaje_no_lo_tumba(self):
        from unittest import mock

        from core.consumo.management.commands import vigilar_consumo
        carpeta = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, carpeta, True)
        archivo = os.path.join(carpeta, "vigilar-consumo.pid")
        with mock.patch("sys.stdout", None), mock.patch("sys.stderr", None), \
                mock.patch.object(vigilar_consumo, "archivo_del_numero", return_value=archivo):
            comando = vigilar_consumo.Command()
            comando.handle(parar=True)
            self.assertIsNotNone(comando.stdout._out)


class ElAvisoDeVerdad(SimpleTestCase):
    """CP-001, paso 4: `watchdog` avisa del código igual que de los `.jsonl`."""

    def test_escribir_un_py_en_la_carpeta_vigilada_llega_como_aviso(self):
        base, codigo = tempfile.mkdtemp(), tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, base, True)
        self.addCleanup(shutil.rmtree, codigo, True)
        parar, avisos = threading.Event(), []
        vigilante = VigilanteDeConsumo(base)
        vigilante.reinicio = Reinicio(parar, raiz=codigo)
        vigilante.reinicio.aviso = lambda r: avisos.append(r) or True
        observador = vigilante.observador()
        try:
            time.sleep(1)
            with open(os.path.join(codigo, "modulo.py"), "w", encoding="utf-8") as f:
                f.write("x = 1\n")
            limite = time.monotonic() + 5
            while time.monotonic() < limite and not avisos:
                time.sleep(0.1)
        finally:
            observador.stop()
            observador.join(5)
        self.assertTrue(any(a.endswith("modulo.py") for a in avisos))
