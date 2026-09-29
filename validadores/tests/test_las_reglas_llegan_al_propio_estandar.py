# -*- coding: utf-8 -*-
"""`EP-005 · HU-009 · CA-04`: lo que entrega el arranque cabe en el canal.

**Qué protege.** Hasta la 39.3.1 el enganche de apertura mandaba las reglas de
`00` y `01` enteras: unos 86.000 caracteres. La herramienta acepta 10.000 por
enganche; lo que pasa de ahí lo guarda en un archivo fuera del repositorio y le
deja al agente un avance de 2.000. Todo arranque llegó cortado, y nadie lo
midió porque el agente no ve lo que no le llega.

Estos casos miden lo que de verdad se entrega, en el estándar, en un proyecto,
con el gate y con una memoria más larga que el tope. Las reglas llegan con cada
mensaje (`hook_reglas.py`); al arrancar solo se dice cómo.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")
sys.path.insert(0, VALIDADORES)

import historico   # noqa: E402
import recuerdos   # noqa: E402

TOPE = 10_000
BLOQUE = "[LAS REGLAS DEL ESTÁNDAR: LLEGAN CON CADA MENSAJE]"
GATE = "[ARRANQUE DETENIDO"
NO_CUPO = "[LO QUE NO CUPO EN EL ARRANQUE]"


def arrancar(raiz):
    entrada = json.dumps({"session_id": "prueba", "cwd": raiz,
                          "hook_event_name": "SessionStart"})
    r = subprocess.run(
        [sys.executable, os.path.join(ADAPTADOR, "hook_sesion.py"), "--raiz", raiz],
        input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=120)
    return r, json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


def carpeta(caso):
    tmp = tempfile.mkdtemp()
    caso.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
    return tmp


def memoria_larga(raiz, filas=120):
    """Una memoria de unos 20.000 caracteres, con filas de recuerdo reales."""
    donde = os.path.join(raiz, "historico-chat", "memory")
    os.makedirs(donde)
    cuerpo = ["# Memoria", "", "Explicación. " * 40, "", "| Recuerdo | De qué |",
              "|---|---|"]
    cuerpo += [f"| [Recuerdo {i}](r{i}.md) | {'Lo que pide el usuario. ' * 6}|"
               for i in range(filas)]
    with open(os.path.join(donde, "memory.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(cuerpo) + "\n")


def historico_largo(raiz, sesiones=40):
    donde = os.path.join(raiz, "historico-chat")
    os.makedirs(donde, exist_ok=True)
    lineas = [f"- [2026-09-{i:02d}-s.md](2026-09-{i:02d}-s.md) — {'tema ' * 20}"
              for i in range(1, sesiones + 1)]
    with open(os.path.join(donde, "README.md"), "w", encoding="utf-8") as f:
        f.write("# Histórico\n\n" + "\n".join(lineas) + "\n")


class CP001ElArranqueCabeYDiceComoLleganLasReglas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r, cls.contexto = arrancar(RAIZ)

    def test_sale_con_cero_y_json_valido(self):
        self.assertEqual(0, self.r.returncode, self.r.stderr)

    def test_en_el_estandar_cabe_en_el_canal(self):
        self.assertLessEqual(len(self.contexto), TOPE)

    def test_dice_como_llegan_las_reglas_y_nombra_el_mapa(self):
        self.assertIn(BLOQUE, self.contexto)
        self.assertIn("base/mapa-de-tareas.md", self.contexto)

    def test_no_trae_el_texto_de_las_reglas(self):
        self.assertNotIn("## N1 ·", self.contexto)
        self.assertNotIn("[REGLAS BASE DEL ESTÁNDAR", self.contexto)

    def test_no_trae_el_gate(self):
        """Al estándar no se le aplica `F13`: no es un proyecto."""
        self.assertNotIn(GATE, self.contexto)

    def test_la_memoria_sigue_llegando(self):
        self.assertIn("[MEMORIA DEL AGENTE", self.contexto)

    def test_en_un_proyecto_cabe_con_la_revision(self):
        tmp = carpeta(self)
        os.makedirs(os.path.join(tmp, "proyectos"))
        r, contexto = arrancar(tmp)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertLessEqual(len(contexto), TOPE)
        self.assertIn(BLOQUE, contexto)
        self.assertIn("[Revisión de arranque del estándar]", contexto)

    def test_sin_estructura_cabe_y_llega_solo_el_gate(self):
        tmp = carpeta(self)
        r, contexto = arrancar(tmp)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertLessEqual(len(contexto), TOPE)
        self.assertIn(GATE, contexto)
        self.assertNotIn(BLOQUE, contexto)


class CP002LoQueNoCabeSeRecortaYSeDice(unittest.TestCase):

    def test_la_memoria_con_tope_cabe_sin_filas_cortadas(self):
        tmp = carpeta(self)
        memoria_larga(tmp)
        texto = recuerdos.contexto(tmp, tope=3000)
        self.assertLessEqual(len(texto), 3000)
        self.assertIn("historico-chat/memory/memory.md", texto)
        for linea in texto.splitlines():
            if linea.startswith("| ["):
                self.assertTrue(linea.endswith("|"), linea)

    def test_el_historico_con_tope_cabe_y_dice_donde_esta_el_resto(self):
        tmp = carpeta(self)
        historico_largo(tmp)
        texto = historico.contexto(tmp, tope=1000)
        self.assertLessEqual(len(texto), 1000)
        self.assertIn("historico-chat/README.md", texto)

    def test_sin_tope_quedan_como_antes(self):
        tmp = carpeta(self)
        memoria_larga(tmp)
        historico_largo(tmp)
        self.assertIn("Explicación.", recuerdos.contexto(tmp))
        self.assertEqual(historico.contexto(tmp),
                         historico.contexto(tmp, historico.LIMITE))

    def test_con_memoria_larga_el_arranque_cabe_y_lo_dice(self):
        tmp = carpeta(self)
        os.makedirs(os.path.join(tmp, "proyectos"))
        memoria_larga(tmp)
        historico_largo(tmp)
        r, contexto = arrancar(tmp)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertLessEqual(len(contexto), TOPE)
        self.assertIn(NO_CUPO, contexto)
        self.assertIn("la memoria se recortó", contexto)


class CP004ElTiempoDelArranque(unittest.TestCase):

    def test_menos_de_tres_segundos(self):
        inicio = time.perf_counter()
        r, _ = arrancar(RAIZ)
        self.assertEqual(0, r.returncode)
        self.assertLess(time.perf_counter() - inicio, 3.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
