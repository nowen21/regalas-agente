# -*- coding: utf-8 -*-
"""`EP-005 · HU-014` — el consumo de la sesión se ve mientras se puede actuar.

**Qué protege.** El reporte de cierre de la 27.0.0 no cambia (`CA-01`), y el
aviso por tramo sale una vez por cada millón cruzado, en el mensaje que sigue
al cruce, y calla entre cruces (`CA-02`, `CA-03`).
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
sys.path.insert(0, VALIDADORES)

import presupuesto   # noqa: E402


def turno(entrada, salida=0, cache=0):
    return json.dumps({"message": {"usage": {
        "input_tokens": entrada, "output_tokens": salida,
        "cache_read_input_tokens": cache}}}) + "\n"


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: __import__("shutil").rmtree(self.tmp, ignore_errors=True))
        self.ruta = os.path.join(self.tmp, "sesion.jsonl")

    def transcripcion(self, *lineas):
        with open(self.ruta, "w", encoding="utf-8") as f:
            f.write("".join(lineas))
        return self.ruta

    def correr(self, *args, ruta=None, sin_ruta=False):
        entrada = {} if sin_ruta else {"transcript_path": ruta or self.ruta}
        return subprocess.run(
            [sys.executable, os.path.join(ADAPTADOR, "hook_presupuesto.py"),
             "--raiz", self.tmp, *args],
            input=json.dumps(entrada), capture_output=True, text=True,
            encoding="utf-8", timeout=60)


class CA01ElReporteDeCierreNoCambia(Base):

    def test_cp_001(self):
        self.transcripcion(turno(100, 20, 5), turno(50, 30))
        esperado = ("Consumo de la sesión: 2 turno(s) · 150 fichas de entrada · "
                    "50 de salida · 5 leídas de caché")
        for args in ((), ("--modo", "cierre")):
            with self.subTest(args=args):
                r = self.correr(*args)
                self.assertEqual(0, r.returncode, r.stderr)
                self.assertIn(esperado, r.stdout)


class CA02AlCruzarUnTramoSeAvisaUnaVez(Base):

    def test_cp_002_el_ultimo_turno_cruza_el_millon(self):
        self.transcripcion(turno(500_000), turno(450_000), turno(100_000))
        r = self.correr("--modo", "aviso")
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("TRAMO 1", r.stdout)
        self.assertIn("1,050,000", r.stdout)

    def test_cp_003_un_turno_mas_dentro_del_mismo_tramo(self):
        self.transcripcion(turno(500_000), turno(450_000), turno(100_000), turno(10_000))
        r = self.correr("--modo", "aviso")
        self.assertEqual(0, r.returncode)
        self.assertEqual("", r.stdout.strip())

    def test_cp_004_el_segundo_millon(self):
        self.transcripcion(turno(500_000), turno(450_000), turno(100_000),
                           turno(10_000), turno(990_000))
        r = self.correr("--modo", "aviso")
        self.assertIn("TRAMO 2", r.stdout)


class CA03SinTranscripcionCallaYNuncaDetiene(Base):

    def test_cp_005_sin_ruta_ruta_inexistente_y_linea_ilegible(self):
        r = self.correr("--modo", "aviso", sin_ruta=True)
        self.assertEqual((0, ""), (r.returncode, r.stdout.strip()))
        r = self.correr("--modo", "aviso", ruta=os.path.join(self.tmp, "no-existe.jsonl"))
        self.assertEqual((0, ""), (r.returncode, r.stdout.strip()))
        self.transcripcion(turno(1_000_000), "esto no es JSON\n")
        r = self.correr("--modo", "aviso")
        self.assertEqual(0, r.returncode)
        self.assertIn("TRAMO 1", r.stdout)


class Limites(unittest.TestCase):

    def test_cp_006_exactamente_el_tramo_y_el_umbral_apagado(self):
        abajo = [{"entrada": 999_998}, {"entrada": 1}]       # 999.999
        justo = [{"entrada": 999_999}, {"entrada": 1}]       # 1.000.000
        self.assertFalse(presupuesto.cruzo_tramo(abajo)[0])
        cruzo, n, _ = presupuesto.cruzo_tramo(justo)
        self.assertTrue(cruzo)
        self.assertEqual(1, n)
        self.assertFalse(presupuesto.cruzo_tramo([{"entrada": 5_000_000}], 0)[0])
        self.assertFalse(presupuesto.cruzo_tramo([])[0])

    def test_la_cache_no_cuenta_para_el_tramo(self):
        self.assertFalse(presupuesto.cruzo_tramo([{"entrada": 10, "cache": 5_000_000}])[0])

    def test_el_tramo_por_defecto_es_un_millon(self):
        self.assertEqual(1_000_000, presupuesto.TRAMO)


class RNF02NoSeNota(Base):

    def test_cp_007_la_transcripcion_mas_grande_se_lee_rapido(self):
        """Sobre la transcripción real más grande de esta máquina, si la hay;
        si no, sobre una de 3.500 turnos armada acá."""
        carpeta = os.path.expanduser("~/.claude/projects/c--Ing--Jose-ia-agente")
        candidatas = []
        if os.path.isdir(carpeta):
            candidatas = [os.path.join(carpeta, n) for n in os.listdir(carpeta)
                          if n.endswith(".jsonl")]
        ruta = max(candidatas, key=os.path.getsize) if candidatas else \
            self.transcripcion(*[turno(3_000, 1_000)] * 3_500)
        inicio = time.perf_counter()
        r = self.correr("--modo", "aviso", ruta=ruta)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertLess(time.perf_counter() - inicio, 2.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
