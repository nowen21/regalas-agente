# -*- coding: utf-8 -*-
"""`EP-023 · HU-007 · fase A` · Nada se escribe fuera del plan aprobado.

CP-001: el plan aprobado desde 48.0.0 dice quién lo aprobó y declara rutas exactas.
CP-002: el commit con un archivo que el plan no declara ni una regla autoriza se rechaza.
CP-003: lo autorizan las reglas de `base/` y las del proyecto.
"""
import io
import os
import re
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
sys.path.insert(0, VALIDADORES)

import autorizado           # noqa: E402
import comun                # noqa: E402
import instalar             # noqa: E402
import plan_vs_hecho        # noqa: E402
from comun import FALLA     # noqa: E402

FASE = "documentacion/epicas/EP-009-algo/HU-001-una-cosa/A-EP-009-HU-001-la-fase"


def plan(version="48.0.0", aprobacion=None, filas=("`src/a.py`",)):
    aprobacion = aprobacion or "Ana Pérez, el 2026-10-02, con la versión " + version
    tabla = "\n".join("| %s | Modificar | Programa | |" % f for f in filas)
    return ("# Plan\n\n**Aprobación** (`02·F4`): %s.\n\n"
            "### 2.1 Archivos que se crean o modifican\n\n"
            "> Es la lista exacta.\n\n"
            "| Archivo (ruta real verificada) | Tipo | Capa | Nota |\n|---|---|---|---|\n%s\n\n"
            "### 2.2 Otra\n" % (aprobacion, tabla))


class ElPlanDiceQueTocaYQuienLoAprobo(unittest.TestCase):
    """CP-001."""

    def test_la_plantilla_pide_la_aprobacion_y_rutas_exactas(self):
        texto = comun.leer(os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md"))
        self.assertIn("| **Aprobación** (", texto)
        self.assertIn("con la versión «X.Y.Z»", texto)
        self.assertIn("rutas exactas entre comillas invertidas", texto)

    def test_la_fila_que_no_es_ruta_exacta_falla(self):
        filas = ("`src/`", "`src/*.py`", "Los validadores", "`src/a.py`", "`src/b.py`, `VERSION`")
        motivos = plan_vs_hecho.revisar_aprobado(plan(filas=filas))
        self.assertEqual(3, len(motivos))
        self.assertTrue(all("§2.1" in m for _, m in motivos))

    def test_la_aprobacion_sin_quien_o_sin_fecha_falla(self):
        for aprobacion in ("el 2026-10-02, con la versión 48.0.0", "Ana Pérez, con la versión 48.0.0"):
            motivos = plan_vs_hecho.revisar_aprobado(plan(aprobacion=aprobacion))
            self.assertEqual(1, len(motivos), aprobacion)
            self.assertIn("quién", motivos[0][1])

    def test_el_plan_aprobado_antes_no_se_revisa(self):
        self.assertEqual([], plan_vs_hecho.revisar_aprobado(plan(version="47.0.0", filas=("`src/`", "Todo"))))


class ElCommitSeComparaConElPlan(unittest.TestCase):
    """CP-002 y la última parte de CP-003."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.git("init", "-q")
        self.escribir(FASE + "/plan_trabajo.md", plan())

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        subprocess.run(["git", "-C", self.raiz] + list(args), check=True, capture_output=True)

    def escribir(self, relativa, texto="x\n"):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def preparar(self, *relativas):
        for r in relativas:
            if not os.path.exists(os.path.join(self.raiz, *r.split("/"))):
                self.escribir(r)
        self.git("add", *relativas)

    def fallas(self):
        return [h.archivo for h in plan_vs_hecho.comparar_preparados(self.raiz) if h.severidad == FALLA]

    def test_lo_declarado_pasa(self):
        self.preparar(FASE + "/plan_trabajo.md", "src/a.py")
        self.assertEqual([], self.fallas())

    def test_lo_no_declarado_ni_autorizado_falla(self):
        self.preparar(FASE + "/plan_trabajo.md", "src/a.py", "src/otro.py")
        self.assertEqual(["src/otro.py"], self.fallas())

    def test_los_documentos_de_la_fase_y_el_resumen_pasan(self):
        self.preparar(FASE + "/plan_trabajo.md", FASE + "/resultado_pruebas.md",
                      "historico-chat/resumenes/2026-10-02/sesion.md")
        self.assertEqual([], self.fallas())

    def test_sin_tocar_una_fase_no_compara(self):
        self.preparar("src/otro.py")
        self.assertEqual([], self.fallas())

    def test_con_el_plan_aprobado_antes_no_compara(self):
        self.escribir(FASE + "/plan_trabajo.md", plan(version="47.0.0"))
        self.preparar(FASE + "/plan_trabajo.md", "src/otro.py")
        self.assertEqual([], self.fallas())

    def test_lo_que_autoriza_una_regla_del_proyecto_pasa(self):
        self.escribir(".agente/reglas-proyecto.md",
                      "# Reglas\n\n### P1 · Las notas\n\n- **Regla:** se escriben.\n"
                      "- **Autoriza escribir:** `notas/*.md`\n")
        self.preparar(FASE + "/plan_trabajo.md", "notas/hoy.md")
        self.assertEqual([], self.fallas())
        self.assertEqual("P1", autorizado.quien_autoriza("notas/hoy.md", autorizado.del_proyecto(self.raiz)))

    def test_el_pre_commit_lo_corre(self):
        self.assertIn("validar.py\" plan --raiz \"$(pwd)\" --preparados", instalar.PLANTILLA_PRE_COMMIT)


class LoAutorizanLasReglas(unittest.TestCase):
    """CP-003."""

    DIEZ = ("01·C19", "01·C28", "04·S18", "02·F12", "13·DOC22", "13·DOC24",
            "13·DOC25", "13·DOC5", "20·M10", "20·M13")

    def test_las_diez_reglas_traen_su_linea(self):
        self.assertEqual(sorted(self.DIEZ), sorted(r for r, _ in autorizado.de_la_base()))

    def test_dice_que_regla_autoriza(self):
        reglas = autorizado.de_la_base()
        casos = {
            "documentacion/epicas/EP-1-a/pendientes/103-b/analisis-2.md": "13·DOC24",
            "historico-chat/scripts/2026-10-02/guion.py": "04·S18",
            "historico-chat/memory/un-recuerdo.md": "01·C19",
            "src/a.py": None,
        }
        for ruta, regla in casos.items():
            self.assertEqual(regla, autorizado.quien_autoriza(ruta, reglas), ruta)

    def test_el_ejemplo_dentro_de_un_bloque_de_codigo_no_cuenta(self):
        texto = comun.leer(os.path.join(RAIZ, "base", "20-meta-reglas", "estructura-regla.md"))
        self.assertTrue(re.search(r"(?m)^\*\*Autoriza escribir:\*\*", texto))
        self.assertNotIn("20·F0", [r for r, _ in autorizado.de_la_base()])


if __name__ == "__main__":
    unittest.main()
