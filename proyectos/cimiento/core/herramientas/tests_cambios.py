# -*- coding: utf-8 -*-
"""Separar los cambios por sesión (`EP-025·HU-016`).

Sin Django: corren con `python -m unittest core.herramientas.tests_cambios`
desde `proyectos/cimiento/`, sobre un repositorio git temporal.
"""
import io
import os
import subprocess
import tempfile
import unittest

from ..validadores.sesiones import Sesiones
from .cambios import CambiosPorSesion

UNA = "aaaa1111-0000-0000-0000-000000000000"
OTRA = "bbbb2222-0000-0000-0000-000000000000"


def _git(raiz, *argumentos):
    return subprocess.run(["git", "-c", "user.name=prueba", "-c", "user.email=prueba@ejemplo.invalid"]
                          + list(argumentos), cwd=raiz, capture_output=True, text=True, check=True).stdout


class SepararLosCambiosPorSesion(unittest.TestCase):

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.raiz = carpeta.name
        _git(self.raiz, "init", "-q")
        self.escribir(".gitignore", "historico-chat/.tocado/\n")
        _git(self.raiz, "add", ".gitignore")
        _git(self.raiz, "commit", "-q", "-m", "base")
        sesiones = Sesiones(self.raiz)
        for archivo, quienes in (("a.txt", [UNA]), ("b.txt", [OTRA]), ("c.txt", [UNA, OTRA])):
            self.escribir(archivo, "x\n")
            for sesion in quienes:
                sesiones.anotar(sesion, os.path.join(self.raiz, archivo))
        self.escribir("d.txt", "de nadie\n")
        self.cambios = CambiosPorSesion(self.raiz)

    def escribir(self, archivo, texto):
        with io.open(os.path.join(self.raiz, archivo), "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def preparados(self):
        return _git(self.raiz, "diff", "--cached", "--name-only").split()

    # CP-003 · Separar por sesión
    def test_cada_sesion_con_lo_suyo(self):
        propios, compartidos, sin_sesion = self.cambios.repartir()
        self.assertEqual({UNA: ["a.txt"], OTRA: ["b.txt"]}, propios)
        self.assertEqual(["c.txt"], compartidos)
        self.assertEqual(["d.txt"], sin_sesion)

    def test_preparar_lleva_solo_lo_de_la_sesion_y_soltar_lo_deshace(self):
        sesion, archivos, compartidos = self.cambios.preparar("aaaa", escribir=True)
        self.assertEqual((UNA, ["a.txt"], ["c.txt"]), (sesion, archivos, compartidos))
        self.assertEqual(["a.txt"], self.preparados())
        self.assertEqual((UNA, ["a.txt"]), self.cambios.soltar("aaaa", escribir=True))
        self.assertEqual([], self.preparados())

    # CP-004 · Rechazos y simulación
    def test_sin_aplicar_no_prepara_nada(self):
        self.assertEqual(["a.txt"], self.cambios.preparar("aaaa")[1])
        self.assertEqual([], self.preparados())

    def test_una_sesion_que_no_existe_se_rechaza(self):
        with self.assertRaises(ValueError):
            self.cambios.preparar("zzzz", escribir=True)
        self.assertEqual([], self.preparados())


if __name__ == "__main__":
    unittest.main()
