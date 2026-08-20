# -*- coding: utf-8 -*-
"""`EP-005 · HU-013` — el checkpoint de la fase se reclama solo.

**Qué protege.** El `estado-fase.md` existe para sobrevivir a la compactación
y lo escribe el agente cuando se acuerda. Estos casos fijan que, al escribir
un documento de puerta, el hueco se vea en el momento; y que el enganche no
toque el checkpoint ni hable cuando no le toca.

Las fechas se fuerzan con `os.utime`: el orden de escritura no puede depender
del reloj (`08·T3`).
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")
sys.path.insert(0, VALIDADORES)

import checkpoint   # noqa: E402


def escribir(ruta, texto="x", fecha=None):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)
    if fecha is not None:
        os.utime(ruta, (fecha, fecha))
    return ruta


def huella(ruta):
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: __import__("shutil").rmtree(self.tmp, ignore_errors=True))
        self.fase = os.path.join(self.tmp, "documentacion", "epicas",
                                 "EP-001-prueba", "HU-001-prueba",
                                 "A-EP-001-HU-001-prueba")
        os.makedirs(self.fase)

    def correr(self, ruta, entrada=None):
        """El enganche como lo llama la herramienta: JSON por la entrada."""
        if entrada is None:
            entrada = json.dumps({"tool_input": {"file_path": ruta}, "cwd": self.tmp})
        return subprocess.run(
            [sys.executable, os.path.join(ADAPTADOR, "hook_checkpoint.py"),
             "--raiz", self.tmp],
            input=entrada, capture_output=True, text=True, encoding="utf-8",
            timeout=60)


class CA01SinCheckpointSeAvisa(Base):

    def test_cp_001_falta_y_se_nombra_la_fase(self):
        ruta = escribir(os.path.join(self.fase, "resultado_pruebas.md"))
        r = self.correr(ruta)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("A-EP-001-HU-001-prueba", r.stdout)
        self.assertIn("SIN CHECKPOINT", r.stdout)
        # RNF-02: dice dónde, relativo al proyecto
        self.assertIn("documentacion/epicas/EP-001-prueba", r.stdout)


class CA02ElCheckpointAtrasado(Base):

    def test_cp_002_atrasado_se_avisa_con_el_documento(self):
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=1000)
        ruta = escribir(os.path.join(self.fase, "funcionalidad_implementada.md"), fecha=2000)
        r = self.correr(ruta)
        self.assertIn("QUEDÓ ATRÁS", r.stdout)
        self.assertIn("funcionalidad_implementada.md", r.stdout)
        self.assertIn("A-EP-001-HU-001-prueba", r.stdout)

    def test_cp_003_al_dia_calla(self):
        ruta = escribir(os.path.join(self.fase, "funcionalidad_implementada.md"), fecha=2000)
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=3000)
        r = self.correr(ruta)
        self.assertEqual(0, r.returncode)
        self.assertEqual("", r.stdout.strip())


class CA03LoQueNoEsPuertaCalla(Base):

    def test_cp_004_los_cuatro_silencios(self):
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=1000)
        fuera = escribir(os.path.join(self.tmp, "notas", "suelta.md"), fecha=5000)
        for nombre in ("estado-fase.md", "plan_pruebas.md", "README.md"):
            ruta = escribir(os.path.join(self.fase, nombre), fecha=5000)
            with self.subTest(archivo=nombre):
                r = self.correr(ruta)
                self.assertEqual(0, r.returncode)
                self.assertEqual("", r.stdout.strip())
        r = self.correr(fuera)
        self.assertEqual("", r.stdout.strip())

    def test_cp_005_la_huella_no_cambia(self):
        estado = escribir(os.path.join(self.fase, "estado-fase.md"), "## 1. En qué estación va\n", fecha=1000)
        ruta = escribir(os.path.join(self.fase, "resultado_pruebas.md"), fecha=2000)
        antes = huella(estado)
        r = self.correr(ruta)
        self.assertIn("QUEDÓ ATRÁS", r.stdout)
        self.assertEqual(antes, huella(estado))


class Limites(Base):

    def test_cp_006_la_entrada_rota_y_el_archivo_que_ya_no_esta(self):
        r = self.correr("", entrada="esto no es JSON")
        self.assertEqual(0, r.returncode)
        self.assertEqual("", r.stdout.strip())
        ruta = os.path.join(self.fase, "resultado_pruebas.md")     # nunca se escribió
        r = self.correr(ruta)
        self.assertEqual(0, r.returncode)
        self.assertEqual("", r.stdout.strip())

    def test_cp_007_solo_mira_fechas(self):
        """RNF-01: un documento ilegible avisa igual, porque no se lee."""
        escribir(os.path.join(self.fase, "estado-fase.md"), fecha=1000)
        ruta = os.path.join(self.fase, "resultado_pruebas.md")
        with open(ruta, "wb") as f:
            f.write(os.urandom(64))
        os.utime(ruta, (2000, 2000))
        self.assertEqual("atrasado", checkpoint.rezago(ruta)[0])

    def test_el_modulo_reconoce_la_fase_por_su_nombre(self):
        self.assertEqual(self.fase, checkpoint.fase_de(os.path.join(self.fase, "plan_trabajo.md")))
        self.assertEqual("", checkpoint.fase_de(os.path.join(self.tmp, "plan_trabajo.md")))

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "checkpoint.py"), encoding="utf-8") as f:
            self.assertIn("no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
