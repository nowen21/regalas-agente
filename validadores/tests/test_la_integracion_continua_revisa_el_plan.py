# -*- coding: utf-8 -*-
"""`EP-023 · HU-007 · CA-02` · La integración continua revisa el plan.

Lo que faltaba del CA-02, hecho de una en el análisis 14 del pendiente 103
(acuerdo 11): la instalación agrega la revisión a la integración continua del
proyecto que la tiene, y `validar.py plan --rango` revisa lo que trae un rango
de commits.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import instalar       # noqa: E402
import plan_vs_hecho  # noqa: E402

REPO = "https://ejemplo.invalid/cimiento.git"
FASE = "documentacion/epicas/EP-001-algo/HU-001-una-cosa/A-EP-001-HU-001-una-cosa"
PLAN = ("# Plan\n\n**Aprobación** (`02·F4`): Ing. Prueba, el 2026-10-03, con la versión 53.1.0.\n\n"
        "### 2.1 Archivos que se crean o modifican\n\n"
        "| Archivo (ruta real verificada) | Tipo | Capa | Nota |\n|---|---|---|---|\n"
        "| `src/declarado.py` | Nuevo | Código | Lo que hace la fase |\n\n### 2.2 Otra\n")


class Base(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, relativa, texto):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta

    def leer(self, relativa):
        return io.open(os.path.join(self.raiz, *relativa.split("/")), encoding="utf-8").read()


class LaInstalacionAgregaLaRevision(Base):

    def test_con_github_crea_su_flujo_con_el_repo_como_dato(self):
        self.escribir(".github/workflows/pruebas.yml", "name: pruebas\n")
        pasos = instalar.instalar_ci(self.raiz, True, repo=REPO)
        self.assertIn("crear .github/workflows/cimiento.yml: la integración continua revisa el plan", pasos)
        texto = self.leer(instalar.CI_GITHUB)
        self.assertIn("CIMIENTO_REPO: " + REPO, texto)
        self.assertIn("plan --raiz", texto)
        self.assertIn('--rango "$DESDE..HEAD"', texto)

    def test_el_dato_del_proyecto_no_se_pisa(self):
        self.escribir(".github/workflows/pruebas.yml", "name: pruebas\n")
        self.escribir(instalar.CI_GITHUB, "CIMIENTO_REPO: el-del-proyecto\n")
        instalar.instalar_ci(self.raiz, True, repo=REPO)
        self.assertEqual("CIMIENTO_REPO: el-del-proyecto\n", self.leer(instalar.CI_GITHUB))

    def test_con_gitlab_crea_su_archivo_y_lo_incluye(self):
        self.escribir(".gitlab-ci.yml", "pruebas:\n  script: [make test]\n")
        instalar.instalar_ci(self.raiz, True, repo=REPO)
        self.assertIn("CIMIENTO_REPO: " + REPO, self.leer(instalar.CI_GITLAB))
        self.assertIn("include:\n  - local: .cimiento-ci.yml", self.leer(".gitlab-ci.yml"))
        instalar.instalar_ci(self.raiz, True, repo=REPO)
        self.assertEqual(1, self.leer(".gitlab-ci.yml").count("include:"))

    def test_gitlab_con_include_propio_no_se_toca_y_se_avisa(self):
        self.escribir(".gitlab-ci.yml", "include:\n  - local: otro.yml\n")
        pasos = instalar.instalar_ci(self.raiz, True, repo=REPO)
        self.assertTrue(any(p.startswith("AVISO") for p in pasos))
        self.assertEqual("include:\n  - local: otro.yml\n", self.leer(".gitlab-ci.yml"))

    def test_sin_integracion_continua_no_se_agrega(self):
        pasos = instalar.instalar_ci(self.raiz, True, repo=REPO)
        self.assertEqual(["sin integración continua: no se agrega la revisión del plan"], pasos)
        self.assertFalse(os.path.exists(os.path.join(self.raiz, ".github")))

    def test_sin_de_donde_descargar_no_se_agrega_y_se_dice(self):
        self.escribir(".github/workflows/pruebas.yml", "name: pruebas\n")
        pasos = instalar.instalar_ci(self.raiz, True, repo="")
        self.assertTrue(pasos[0].startswith("OMITIDO"))
        self.assertFalse(os.path.exists(os.path.join(self.raiz, *instalar.CI_GITHUB.split("/"))))


class ElRangoSeRevisaContraElPlan(Base):

    def git(self, *args):
        subprocess.run(["git", "-C", self.raiz, *args], check=True, capture_output=True)

    def test_lo_que_el_plan_no_declara_falla_y_lo_declarado_pasa(self):
        self.git("init", "-q")
        self.git("config", "user.email", "prueba@ejemplo.invalid")
        self.git("config", "user.name", "Prueba")
        self.escribir("LEEME.md", "x\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "inicio")
        self.escribir(FASE + "/plan_trabajo.md", PLAN)
        self.escribir("src/declarado.py", "x = 1\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "la fase")
        self.assertEqual([], plan_vs_hecho.comparar_rango(self.raiz, "HEAD~1..HEAD"))
        self.escribir("src/otro.py", "y = 2\n")
        self.escribir(FASE + "/estado-fase.md", "estado\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "algo más")
        fallas = plan_vs_hecho.comparar_rango(self.raiz, "HEAD~2..HEAD")
        self.assertEqual(["src/otro.py"], [h.archivo for h in fallas])


if __name__ == "__main__":
    unittest.main()
