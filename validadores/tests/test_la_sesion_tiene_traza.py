# -*- coding: utf-8 -*-
"""`EP-005 · HU-016` — la traza de la sesión, paso a paso.

**Qué protege.** De una sesión quedaba qué se dijo y cuánto costó, no qué se
ejecutó. Estos casos fijan que el lector saque la línea de tiempo con sus
duraciones y errores, que el cierre diga los totales, que `--escribir` la
deje junto al histórico sin duplicar el índice, que lo raro no reviente — y
que ningún contenido de resultado se copie a la salida.

Las marcas de tiempo son fijas (`08·T3`): las duraciones se conocen de
antemano.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
sys.path.insert(0, VALIDADORES)

import traza    # noqa: E402

BASE = "2026-08-20T10:00:%02d.000Z"


def _uso(id_, nombre, entrada, segundo):
    return {"type": "assistant", "timestamp": BASE % segundo,
            "message": {"content": [
                {"type": "tool_use", "id": id_, "name": nombre, "input": entrada}]}}


def _respuesta(id_, segundo, error=False):
    return {"type": "user", "timestamp": BASE % segundo,
            "message": {"content": [
                {"type": "tool_result", "tool_use_id": id_,
                 "is_error": error, "content": "CENTINELA-" + id_}]}}


def _escribir(carpeta, lineas, nombre="abc.jsonl"):
    ruta = os.path.join(carpeta, nombre)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        for linea in lineas:
            f.write((linea if isinstance(linea, str) else json.dumps(linea)) + "\n")
    return ruta


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="cimiento-traza-")
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))

    def transcripcion(self):
        """Tres pasos con respuestas a 2, 5 y 1 segundos; el segundo con error."""
        return _escribir(self.tmp, [
            _uso("t1", "Read", {"file_path": "a.md"}, 0), _respuesta("t1", 2),
            _uso("t2", "Bash", {"command": "python x.py"}, 10),
            _respuesta("t2", 15, error=True),
            _uso("t3", "WebFetch", {"url": "https://e.test"}, 20),
            _respuesta("t3", 21)])

    def correr(self, *args):
        return subprocess.run(
            [sys.executable, os.path.join(VALIDADORES, "validar.py"),
             "traza"] + list(args),
            capture_output=True, text=True, encoding="utf-8", timeout=120)


class CA01LaLineaDeTiempo(Base):

    def test_cp_001_tres_pasos_uno_con_error(self):
        r = self.correr(self.transcripcion())
        self.assertEqual(0, r.returncode, r.stderr)
        filas = [l for l in r.stdout.splitlines() if l.startswith("| ")]
        datos = [l for l in filas if l.split("|")[1].strip().isdigit()]
        self.assertEqual(3, len(datos))
        self.assertIn("Read", datos[0]);      self.assertIn("2 s", datos[0])
        self.assertIn("a.md", datos[0]);      self.assertIn("ok", datos[0])
        self.assertIn("Bash", datos[1]);      self.assertIn("5 s", datos[1])
        self.assertIn("python x.py", datos[1]); self.assertIn("error", datos[1])
        self.assertIn("WebFetch", datos[2]);  self.assertIn("1 s", datos[2])
        self.assertIn("10:00:00", datos[0])
        # RNF-02 · privacidad: ningún contenido de resultado se copia
        self.assertNotIn("CENTINELA", r.stdout)


class CA02ElCierre(Base):

    def test_cp_002_los_totales(self):
        r = self.correr(self.transcripcion())
        self.assertIn("3 pasos", r.stdout)
        self.assertIn("1 error", r.stdout)
        self.assertIn("Bash 1", r.stdout)
        self.assertIn("Read 1", r.stdout)
        self.assertIn("WebFetch 1", r.stdout)
        self.assertIn("Bash (5 s)", r.stdout)       # el más lento
        self.assertIn("21 s", r.stdout)             # del primer uso a la última respuesta


class CA03EscribeJuntoAlHistorico(Base):

    def _proyecto(self):
        carpeta = os.path.join(self.tmp, "historico-chat")
        os.makedirs(carpeta)
        with io.open(os.path.join(carpeta, "2026-08-20-sesion.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write("<!-- sesion: abc -->\n\n# 2026-08-20 — Sesión\n")
        return carpeta

    def test_cp_003_escribe_e_indexa_una_vez(self):
        self._proyecto()
        ruta = self.transcripcion()
        r = self.correr(ruta, "--escribir", "--raiz", self.tmp)
        self.assertEqual(0, r.returncode, r.stderr)
        destino = os.path.join(self.tmp, "historico-chat", "trazas",
                               "2026-08-20-sesion.md")
        self.assertTrue(os.path.isfile(destino))
        texto = io.open(destino, encoding="utf-8").read()
        self.assertIn("| 1 |", texto)
        self.assertIn("3 pasos", texto)
        indice = io.open(os.path.join(self.tmp, "historico-chat", "trazas",
                                      "README.md"), encoding="utf-8").read()
        self.assertIn("historico-chat/trazas/2026-08-20-sesion.md", indice)

        self.correr(ruta, "--escribir", "--raiz", self.tmp)
        indice = io.open(os.path.join(self.tmp, "historico-chat", "trazas",
                                      "README.md"), encoding="utf-8").read()
        self.assertEqual(1, indice.count("(2026-08-20-sesion.md)"))

    def test_cp_004_sin_historico_no_inventa(self):
        ruta = self.transcripcion()
        r = self.correr(ruta, "--escribir", "--raiz", self.tmp)
        self.assertEqual(1, r.returncode)
        self.assertFalse(os.path.isdir(os.path.join(self.tmp, "historico-chat",
                                                    "trazas")))

        os.makedirs(os.path.join(self.tmp, "historico-chat"))
        r = self.correr(ruta, "--escribir", "--raiz", self.tmp)
        self.assertEqual(1, r.returncode)
        self.assertFalse(os.path.isdir(os.path.join(self.tmp, "historico-chat",
                                                    "trazas")))


class CA04LoRaroNoRevienta(Base):

    def test_cp_005_ilegible_sin_respuesta_vacio_inexistente(self):
        ruta = _escribir(self.tmp, [
            _uso("t1", "Read", {"file_path": "a.md"}, 0),
            "esto no es JSON",
            _respuesta("t1", 2),
            _uso("t2", "Bash", {"command": "x"}, 5)])
        r = self.correr(ruta)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("2 pasos", r.stdout)
        self.assertIn("sin respuesta", r.stdout)

        vacia = _escribir(self.tmp, [], nombre="vacia.jsonl")
        r = self.correr(vacia)
        self.assertEqual(1, r.returncode)
        self.assertNotIn("Traceback", r.stderr)

        r = self.correr(os.path.join(self.tmp, "no-existe.jsonl"))
        self.assertEqual(1, r.returncode)
        self.assertNotIn("Traceback", r.stderr)


class ElModuloEmparejaPorId(Base):

    def test_las_respuestas_desordenadas_no_confunden(self):
        """Con llamadas en paralelo la respuesta del segundo llega primero."""
        ruta = _escribir(self.tmp, [
            _uso("t1", "Read", {"file_path": "a.md"}, 0),
            _uso("t2", "Grep", {"pattern": "x"}, 1),
            _respuesta("t2", 3), _respuesta("t1", 6)])
        lista = traza.pasos(ruta)
        self.assertEqual("6 s", lista[0]["duracion"])
        self.assertEqual("2 s", lista[1]["duracion"])


if __name__ == "__main__":
    unittest.main()
