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

    def test_lo_que_el_analisis_prendido_manda_hacer_de_una_pasa(self):
        pendiente = "documentacion/epicas/EP-009-algo/pendientes/7-algo"
        self.escribir(pendiente + "/analisis-2.md",
                      "# Análisis 2\n\n## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Corregir | 1 | Este análisis, de una y sin fase: `src/otro.py` |\n\n## Otra\n")
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % pendiente)
        self.preparar(FASE + "/plan_trabajo.md", "src/otro.py", "src/tercero.py")
        self.assertEqual(["src/tercero.py"], self.fallas())

    def test_lo_que_un_analisis_aprobado_manda_hacer_entra_con_el(self):
        """Análisis 16 del pendiente 103, acuerdo 1."""
        pendiente = "documentacion/epicas/EP-009-algo/pendientes/7-algo"
        self.escribir(pendiente + "/analisis-2.md",
                      "# Análisis 2\n\n> **Aprobado** por el usuario el 2026-10-03.\n\n## Lo que se tiene que hacer\n\n"
                      "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n"
                      "| 1 | Corregir | 1 | Este análisis, de una y sin fase: `src/otro.py` |\n\n## Otra\n")
        self.preparar(FASE + "/plan_trabajo.md", "src/otro.py", "src/tercero.py")
        self.assertEqual(["src/otro.py", "src/tercero.py"], sorted(self.fallas()))
        self.preparar(FASE + "/plan_trabajo.md", "src/otro.py", "src/tercero.py", pendiente + "/analisis-2.md")
        self.assertEqual(["src/tercero.py"], self.fallas())

    def test_el_hash_anotado_solo_no_toca_la_fase(self):
        """Análisis 16 del pendiente 103, acuerdo 2."""
        self.preparar(FASE + "/plan_trabajo.md")
        self.git("commit", "-q", "-m", "plan")
        self.preparar(FASE + "/estado-fase.md", "src/tercero.py")
        self.assertEqual([], self.fallas())

    def test_avisa_la_prueba_que_lee_lo_que_cambia_y_no_se_declara(self):
        """Análisis 16 del pendiente 103, acuerdo 2."""
        self.escribir("src/a.py", "x = 1\n")
        self.escribir("tests/test_a.py", "import a\n")
        self.escribir("tests/test_otro.py", "import b\n")
        avisos = plan_vs_hecho.pruebas_sin_declarar(os.path.join(self.raiz, *FASE.split("/")), self.raiz)
        self.assertEqual(1, len(avisos))
        self.assertIn("tests/test_a.py", avisos[0].mensaje)
        self.assertNotIn("test_otro", avisos[0].mensaje)

    def test_el_pre_commit_lo_corre(self):
        self.assertIn("validar.py\" plan --raiz \"$(pwd)\" --preparados", instalar.PLANTILLA_PRE_COMMIT)


class LoAutorizanLasReglas(unittest.TestCase):
    """CP-003. Con reglas de ejemplo: si entra o sale una regla real, la prueba no cambia
    (análisis 11 del pendiente 103, acuerdo 4)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.estandar = os.path.join(self.tmp.name, "estandar")
        self.proyecto = os.path.join(self.tmp.name, "proyecto")
        os.makedirs(self.proyecto)
        self.regla("DOC90-escribe-notas.md", "## DOC90 · Escribe notas", "`notas/*.md`")
        self.regla("DOC91-escribe-actas.md", "## DOC91 · Escribe actas  ·  `[DEROGADA en 9.0.0 → ver 13·DOC90]`", "`actas/**`")
        self.regla("DOC92-escribe-senales.md", "## DOC92 · Escribe señales — *opt-in*", "`senales/*.md`")
        self.regla("DOC93-con-ejemplo.md", "## DOC93 · Muestra un ejemplo",
                   None, "```\n**Autoriza escribir:** `ejemplo/**`\n```\n")

    def tearDown(self):
        self.tmp.cleanup()

    def regla(self, nombre, titulo, rutas, cuerpo=""):
        ruta = os.path.join(self.estandar, "base", "13-documentacion", "reglas", nombre)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        linea = "**Aplica a:** escribir-documento\n\n" + ("**Autoriza escribir:** %s\n" % rutas if rutas else "")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write("%s\n\nTexto.\n\n%s\n%s" % (titulo, linea, cuerpo))

    def reglas(self):
        return [r for r, _ in autorizado.de_la_base(self.estandar, self.proyecto)]

    def test_la_regla_vigente_autoriza(self):
        reglas = autorizado.de_la_base(self.estandar, self.proyecto)
        self.assertEqual("13·DOC90", autorizado.quien_autoriza("notas/hoy.md", reglas))
        self.assertIsNone(autorizado.quien_autoriza("src/a.py", reglas))

    def test_la_regla_derogada_no_autoriza(self):
        self.assertNotIn("13·DOC91", self.reglas())

    def test_la_opt_in_apagada_no_autoriza_y_la_encendida_si(self):
        self.assertIn("13·DOC92", self.reglas())
        with io.open(os.path.join(self.proyecto, "CLAUDE.md"), "w", encoding="utf-8") as f:
            f.write("- Patrón opt-in `13` (documentación): no\n")
        self.assertNotIn("13·DOC92", self.reglas())

    def test_el_ejemplo_dentro_de_un_bloque_de_codigo_no_cuenta(self):
        self.assertNotIn("13·DOC93", self.reglas())

    def test_una_regla_nueva_entra_sin_tocar_el_programa(self):
        antes = len(self.reglas())
        self.regla("DOC94-escribe-bitacoras.md", "## DOC94 · Escribe bitácoras", "`bitacoras/*.md`")
        self.assertEqual(antes + 1, len(self.reglas()))


if __name__ == "__main__":
    unittest.main()
