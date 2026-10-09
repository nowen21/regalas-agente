"""`EP-026·HU-011` · `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes."""
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest

CIMIENTO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANAGE = os.path.join(CIMIENTO, "manage.py")


def _manage():
    spec = importlib.util.spec_from_file_location("manage_de_cimiento", MANAGE)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _python_del_computador():
    """El Python sobre el que se armó el ambiente: el que el aviso llama `python`."""
    for ruta in (os.path.join(sys.base_prefix, "python.exe"), os.path.join(sys.base_prefix, "bin", "python3")):
        if os.path.isfile(ruta):
            return ruta
    return None


class ElPythonQueToca(unittest.TestCase):
    """CP-001 y CP-002: a qué Python se vuelve a abrir, y cuándo no."""

    def setUp(self):
        self.manage = _manage()
        self.tmp = tempfile.TemporaryDirectory()
        self.carpeta = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def _con_venv(self):
        scripts = os.path.join(self.carpeta, ".venv", "Scripts")
        os.makedirs(scripts)
        ruta = os.path.join(scripts, "python.exe")
        open(ruta, "w").close()
        return ruta

    def test_con_otro_python_devuelve_el_de_venv(self):
        ruta = self._con_venv()
        self.assertEqual(self.manage.python_que_toca(self.carpeta, prefijo=os.path.join(self.carpeta, "otro")), ruta)

    def test_sin_venv_no_devuelve_ninguno(self):
        self.assertIsNone(self.manage.python_que_toca(self.carpeta, prefijo=os.path.join(self.carpeta, "otro")))

    def test_ya_con_el_de_venv_no_devuelve_ninguno(self):
        self._con_venv()
        self.assertIsNone(self.manage.python_que_toca(self.carpeta, prefijo=os.path.join(self.carpeta, ".venv")))


@unittest.skipUnless(_python_del_computador() and _manage().python_que_toca(prefijo=sys.base_prefix),
                     "esta máquina no tiene un Python aparte del de Cimiento")
class AbiertoConElPythonDelComputador(unittest.TestCase):
    """CP-001 y CP-003: la orden responde y las tildes salen en UTF-8."""

    def test_responde_y_escribe_las_tildes(self):
        r = subprocess.run([_python_del_computador(), MANAGE, "shell", "-c", "print('capítulo')"],
                           cwd=CIMIENTO, capture_output=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stderr.decode("utf-8", "replace"))
        self.assertIn("capítulo", r.stdout.decode("utf-8"))
