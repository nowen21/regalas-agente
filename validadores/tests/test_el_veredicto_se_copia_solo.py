# -*- coding: utf-8 -*-
"""`EP-005 · HU-003 · CA-04` — lo que se deriva del veredicto lo copia el programa (fase C)."""
import datetime
import hashlib
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
ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")
sys.path.insert(0, VALIDADORES)

import cerrar      # noqa: E402
import veredicto   # noqa: E402
from comun import leer   # noqa: E402

HOY = datetime.date.today().isoformat()
FASE = "A-EP-001-HU-001-p"


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return ruta


def huella(ruta):
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def resultado(concepto, conteo="2 de 2"):
    return ("# Resultado\n\n## 6. Veredicto de la fase\n\n| Campo | Valor |\n|---|---|\n"
            "| **Concepto** | **%s** |\n| **CA cumplidos** | %s |\n" % (concepto, conteo))


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(self.tmp, ignore_errors=True))
        self.hu_dir = os.path.join(self.tmp, "documentacion", "epicas", "EP-001-p", "HU-001-p")
        self.fase = os.path.join(self.hu_dir, FASE)
        self.hu_md = os.path.join(self.hu_dir, "HU-001-p.md")
        self.readme_fase = escribir(os.path.join(self.fase, "README.md"),
                                    "# %s\n\n**Estado:** estación 4, esperando aprobación.\n" % FASE)
        self.readme_hu = escribir(os.path.join(self.hu_dir, "README.md"),
                                  "# HU-001-p\n\n| Qué | De qué se trata |\n|---|---|\n"
                                  "| [documentacion/epicas/EP-001-p/HU-001-p/%s/](%s/) | La fase A: la prueba. Plan escrito, esperando aprobación |\n" % (FASE, FASE))
        self.estado = escribir(os.path.join(self.fase, "estado-fase.md"), "## 1. En qué estación va\n")

    def hu_seis(self):
        escribir(self.hu_md, "# HU-001 — La prueba\n\n## 8. Fases que la implementan\n\n"
                 "| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n|---|---|---|---|---|---|\n"
                 "| [%s](%s/README.md) | CA-01 | [p](%s/plan_trabajo.md) | [q](%s/plan_pruebas.md) | cuando se ejecute | Estación 4: plan escrito |\n\n## 9. Otra\n" % (FASE, FASE, FASE, FASE))

    def hu_tres(self):
        escribir(self.hu_md, "# HU-001 — La prueba\n\n## 8. Fases que la implementan\n\n"
                 "| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
                 "| [%s](%s/README.md) | CA-01 | Estación 4: plan escrito |\n\n## 9. Otra\n" % (FASE, FASE))

    def correr(self, ruta):
        entrada = json.dumps({"tool_input": {"file_path": ruta}, "cwd": self.tmp})
        return subprocess.run([sys.executable, os.path.join(ADAPTADOR, "hook_veredicto.py"),
                               "--raiz", self.tmp],
                              input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=60)


class CA04ElVeredictoLlega(Base):

    def test_cp_001_cumple_llega_a_los_tres_sitios_con_seis_columnas(self):
        self.hu_seis()
        r = self.correr(escribir(os.path.join(self.fase, "resultado_pruebas.md"), resultado("Cumple")))
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("SE COPIÓ", r.stdout)
        esperado = "Cerrada el %s: Cumple, 2 de 2 CA" % HOY
        fila = [l for l in leer(self.hu_md).splitlines() if l.startswith("| [%s]" % FASE)][0]
        self.assertTrue(fila.endswith("| %s |" % esperado), fila)
        self.assertIn("| CA-01 | [p](", fila)
        self.assertIn("**Estado:** %s. Falta el commit" % esperado, leer(self.readme_fase))
        self.assertIn("| La fase A: la prueba. %s |" % esperado, leer(self.readme_hu))

    def test_cp_002_no_cumple_llega_igual_con_tres_columnas(self):
        self.hu_tres()
        escribir(os.path.join(self.fase, "resultado_pruebas.md"), resultado("No cumple", "1 de 2"))
        tocados, avisos = veredicto.propagar(os.path.join(self.fase, "resultado_pruebas.md"), HOY)
        self.assertEqual([], avisos)
        fila = [l for l in leer(self.hu_md).splitlines() if l.startswith("| [%s]" % FASE)][0]
        self.assertEqual("| [%s](%s/README.md) | CA-01 | Ejecutada el %s: No cumple, 1 de 2 CA |" % (FASE, FASE, HOY), fila)

    def test_cp_003_sin_concepto_no_se_toca_nada(self):
        self.hu_seis()
        antes = (huella(self.hu_md), huella(self.readme_fase), huella(self.readme_hu))
        r = self.correr(escribir(os.path.join(self.fase, "resultado_pruebas.md"), resultado("Todavía no se ejecutó")))
        self.assertEqual((0, ""), (r.returncode, r.stdout.strip()))
        self.assertEqual(antes, (huella(self.hu_md), huella(self.readme_fase), huella(self.readme_hu)))

    def test_cp_004_el_estado_fase_no_cambia(self):
        self.hu_seis()
        antes = huella(self.estado)
        self.correr(escribir(os.path.join(self.fase, "resultado_pruebas.md"), resultado("Cumple")))
        self.assertEqual(antes, huella(self.estado))

    def test_cp_006_lo_que_no_le_toca_y_lo_que_no_encuentra(self):
        self.hu_seis()
        r = self.correr(escribir(os.path.join(self.fase, "plan_trabajo.md"), "x"))
        self.assertEqual((0, ""), (r.returncode, r.stdout.strip()))
        escribir(self.hu_md, "# HU-001 — La prueba\n\n## 8. Fases\n\n| Fase | CA | Estado |\n|---|---|---|\n")
        r = self.correr(escribir(os.path.join(self.fase, "resultado_pruebas.md"), resultado("Cumple")))
        self.assertEqual(0, r.returncode)
        self.assertIn("NO TIENE DÓNDE COPIARSE", r.stdout)


class CP005CerrarDejaLaFilaEnFormaDeHecho(unittest.TestCase):

    def test_la_fila(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
        escribir(os.path.join(tmp, "pendientes", "99-p.md"), "# Pendiente · p\n")
        indice = escribir(os.path.join(tmp, "pendientes", "README.md"),
                          "# Pendientes\n\n| # | P | Pendiente | Qué resuelve |\n|---|---|---|---|\n"
                          "| 99 | **P2** | [t](99-p.md) | q |\n")
        cerrar.cerrar(tmp, 99, "p", escribir=True)
        texto = leer(indice)
        self.assertIn("| ~~99~~ | — | **hecho** → [t](hecho/p.md) | q |", texto)
        self.assertTrue(os.path.isfile(os.path.join(tmp, "pendientes", "hecho", "p.md")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
