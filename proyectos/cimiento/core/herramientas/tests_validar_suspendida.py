"""`EP-025·HU-032`, fase C · La revisión de git suspendida no detiene: CP-006 y CP-007 del plan de pruebas.

Sin Django: corren con `python -m unittest core.herramientas.tests_validar_suspendida` desde `proyectos/cimiento/`.
"""
import io
import shutil
import tempfile
import time
import unittest
from contextlib import redirect_stderr
from unittest import mock

from . import validar
from .validar import revision_git_suspendida

MANANA = time.time() + 86400


class ConUnProyecto(unittest.TestCase):
    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        self.veces = 0

    def consultar(self, lista):
        def consulta():
            self.veces += 1
            return lista
        return consulta


class LaRevisionSuspendidaNoDetiene(ConUnProyecto):
    """CP-006."""

    def test_suspendida_sale_con_cero_y_lo_dice(self):
        lista = [["git-versionado", MANANA, "un archivo grande que sí va"]]
        real = validar.revision_git_suspendida
        with mock.patch.object(validar, "revision_git_suspendida",
                               lambda orden, raiz: real(orden, raiz, consultar=self.consultar(lista))):
            errores = io.StringIO()
            with redirect_stderr(errores):
                codigo = validar.Consola().correr(["versionado", "--raiz", self.raiz, "--preparados"])
        self.assertEqual(0, codigo)
        self.assertIn("suspendida en Cimiento hasta el", errores.getvalue())
        self.assertIn("un archivo grande que sí va", errores.getvalue())

    def test_sin_suspender_o_vencida_no_esta_suspendida(self):
        self.assertIsNone(revision_git_suspendida("versionado", self.raiz, consultar=self.consultar([])))
        vencida = [["git-marcas", time.time() - 10, "ya venció"]]
        self.assertIsNone(revision_git_suspendida("marcas", self.raiz, consultar=self.consultar(vencida)))

    def test_lo_que_no_es_de_git_no_mira_las_suspensiones(self):
        self.assertIsNone(revision_git_suspendida("fases", self.raiz, consultar=self.consultar([])))
        self.assertEqual(0, self.veces)


class UnaSolaConsultaPorGuardado(ConUnProyecto):
    """CP-007."""

    def test_tres_revisiones_seguidas_consultan_una_vez(self):
        consulta = self.consultar([["git-plan", MANANA, "el plan se corrige"]])
        ahora = lambda: 1_700_000_000.0         # noqa: E731 · el mismo minuto para las tres
        resultados = [revision_git_suspendida(orden, self.raiz, consultar=consulta, ahora=ahora)
                      for orden in ("versionado", "marcas", "plan")]
        self.assertEqual(1, self.veces)
        self.assertEqual([None, None], resultados[:2])
        self.assertEqual("el plan se corrige", resultados[2][0])


if __name__ == "__main__":
    unittest.main()
