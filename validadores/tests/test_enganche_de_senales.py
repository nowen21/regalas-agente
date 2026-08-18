# -*- coding: utf-8 -*-
"""Pendiente 17 · El enganche que recuerda escribir la señal en el momento.

`13·DOC5` manda registrar como señal lo que no se recupera del código, y el
archivo donde escribirlas no existió acá hasta el 2026-08-14 — después de una
sesión entera de la que casi todo lo aprendido se quedó en la transcripción.

Es la lección del histórico y del resumen otra vez: **lo que depende de que
alguien se acuerde, no pasa.**

Lo que estas pruebas fijan no es que el aviso salga —eso es fácil— sino las
tres condiciones que impiden que se vuelva ruido, porque **un aviso que se
ignora es peor que ninguno**: una vez por sesión, solo si el proyecto lleva
señales, y nunca escribiendo la señal por su cuenta.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import hook_senales   # noqa: E402


class ElAvisoSaleUnaVezPorSesion(unittest.TestCase):

    def _proyecto(self, con_archivo=True):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        if con_archivo:
            ruta = os.path.join(raiz, "documentacion", "senales.md")
            os.makedirs(os.path.dirname(ruta))
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write("# Señales\n\n## S-001 · algo\n")
        return raiz

    def test_la_primera_vez_avisa(self):
        raiz = self._proyecto()
        self.assertIn("señal", hook_senales.aviso(raiz, "sesion-1").lower())

    def test_la_segunda_vez_de_la_misma_sesion_calla(self):
        """Repetirlo en cada turno es la forma más rápida de que se ignore."""
        raiz = self._proyecto()
        hook_senales.aviso(raiz, "sesion-1")
        self.assertEqual("", hook_senales.aviso(raiz, "sesion-1"))

    def test_una_sesion_nueva_vuelve_a_avisar(self):
        raiz = self._proyecto()
        hook_senales.aviso(raiz, "sesion-1")
        self.assertNotEqual("", hook_senales.aviso(raiz, "sesion-2"))

    def test_sin_archivo_de_senales_no_avisa(self):
        """Un proyecto que no lleva señales no recibe un aviso sobre algo que
        no tiene. El enganche no inventa el archivo."""
        raiz = self._proyecto(con_archivo=False)
        self.assertEqual("", hook_senales.aviso(raiz, "sesion-1"))
        self.assertFalse(os.path.exists(
            os.path.join(raiz, "documentacion", "senales.md")))

    def test_no_escribe_ninguna_senal(self):
        """Reconocer qué merece ser señal es criterio, y es del agente."""
        raiz = self._proyecto()
        ruta = os.path.join(raiz, "documentacion", "senales.md")
        with io.open(ruta, encoding="utf-8") as f:
            antes = f.read()
        hook_senales.aviso(raiz, "sesion-1")
        with io.open(ruta, encoding="utf-8") as f:
            despues = f.read()
        self.assertIn("## S-001 · algo", despues)
        self.assertEqual(antes.count("## S-"), despues.count("## S-"),
                         "el enganche escribió una señal")

    def test_la_marca_no_se_ve_al_leer_el_documento(self):
        """Va en un comentario: el archivo lo lee una persona."""
        raiz = self._proyecto()
        hook_senales.aviso(raiz, "sesion-1")
        with io.open(os.path.join(raiz, "documentacion", "senales.md"),
                     encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("<!--", texto.split("## S-001")[-1])

    def test_sin_identificador_de_sesion_avisa_igual(self):
        """Sin sesión no se puede recordar si ya avisó. Se prefiere avisar de
        más antes que callar: el defecto que esto arregla es el silencio."""
        raiz = self._proyecto()
        self.assertNotEqual("", hook_senales.aviso(raiz, ""))
        self.assertNotEqual("", hook_senales.aviso(raiz, ""))


class NoDetieneElTrabajo(unittest.TestCase):
    """Un enganche que rompe el turno es peor que el problema que resuelve."""

    def _correr(self, raiz):
        return subprocess.run(
            [sys.executable, os.path.join(VALIDADORES, "hook_senales.py"),
             "--raiz", raiz],
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=30)

    def test_sale_con_cero_aunque_no_haya_nada(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(0, self._correr(tmp.name).returncode)

    def test_sale_con_cero_sobre_una_ruta_que_no_existe(self):
        r = self._correr(os.path.join(tempfile.gettempdir(), "no-existe-nunca"))
        self.assertEqual(0, r.returncode)

    def test_sobre_este_repositorio_no_se_cae(self):
        raiz = os.path.dirname(VALIDADORES)
        self.assertEqual(0, self._correr(raiz).returncode)


if __name__ == "__main__":
    unittest.main()
