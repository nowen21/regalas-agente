# -*- coding: utf-8 -*-
"""`EP-005 · HU-009 · CA-01` en la carpeta del propio estándar — fase B.

**Qué protege.** Desde la primera versión del enganche de apertura, la carpeta
del estándar recibía la memoria y el histórico y **ninguna regla**: 30 de 30
aperturas entre el 16 y el 20 de agosto de 2026. Nadie lo midió porque las
reglas viajan por el canal que no se dibuja. Estos casos lo miden.
"""
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")

BLOQUE = "[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]"
GATE = "[ARRANQUE DETENIDO"


def arrancar(raiz):
    entrada = json.dumps({"session_id": "prueba", "cwd": raiz,
                          "hook_event_name": "SessionStart"})
    r = subprocess.run(
        [sys.executable, os.path.join(ADAPTADOR, "hook_sesion.py"), "--raiz", raiz],
        input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=120)
    return r, json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


class CP001ElEstandarRecibeLasReglas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r, cls.contexto = arrancar(RAIZ)

    def test_sale_con_cero_y_json_valido(self):
        self.assertEqual(0, self.r.returncode, self.r.stderr)

    def test_trae_el_bloque_de_reglas(self):
        self.assertIn(BLOQUE, self.contexto)

    def test_trae_el_nucleo_con_su_texto(self):
        self.assertIn("<<< base/00-nucleo-blindado.md >>>", self.contexto)
        self.assertIn("## N1 ·", self.contexto)

    def test_no_trae_el_gate(self):
        """Al estándar no se le aplica `F13`: no es un proyecto."""
        self.assertNotIn(GATE, self.contexto)

    def test_cp_002_la_memoria_y_el_historico_siguen_llegando(self):
        self.assertIn("[MEMORIA DEL AGENTE", self.contexto)
        self.assertIn("[HISTÓRICO DE SESIONES", self.contexto)


class CP003UnHerederoRecibeLoMismoQueAntes(unittest.TestCase):

    def test_con_proyectos_llegan_las_reglas_y_la_revision(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: __import__("shutil").rmtree(tmp, ignore_errors=True))
        os.makedirs(os.path.join(tmp, "proyectos"))
        r, contexto = arrancar(tmp)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn(BLOQUE, contexto)
        self.assertIn("[Revisión de arranque del estándar]", contexto)

    def test_sin_proyectos_llega_solo_el_gate(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: __import__("shutil").rmtree(tmp, ignore_errors=True))
        r, contexto = arrancar(tmp)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn(GATE, contexto)
        self.assertNotIn(BLOQUE, contexto)


class CP004ElTiempoDelArranque(unittest.TestCase):

    def test_menos_de_tres_segundos(self):
        inicio = time.perf_counter()
        r, _ = arrancar(RAIZ)
        self.assertEqual(0, r.returncode)
        self.assertLess(time.perf_counter() - inicio, 3.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
