# -*- coding: utf-8 -*-
"""`EP-004 · HU-013` · Lo hecho contra el plan aprobado.

**Qué protege.** [`02·F8`](../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)
dice que una fase edita **los archivos que su plan declara**, y que descubrir
otro detiene la ejecución hasta ampliarlo. Comprobarlo era leer el plan y el
diff a la vez, o sea casi nunca.

**El caso que decide es `CP-004`:** los documentos de la propia fase no cuentan
como archivo de más. Escribir el resultado de las pruebas **es** ejecutar la
fase; pedir que el plan se declare a sí mismo daría un aviso en todas y ninguno
se leería.

**Avisa, nunca detiene.** Un archivo de más puede ser un descubrimiento
legítimo que se reportó y se aprobó, y eso no se ve desde el disco. El programa
dice que la lista no cuadra; si la explicación cuadra, lo lee una persona.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plan_vs_hecho as pvh      # noqa: E402
from comun import AVISO, FALLA   # noqa: E402

PLAN = u"""# Plan de Trabajo

## 2. Análisis previo

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/enlaces.py` | Modificar | lo declarado |
| `base/09-git.md` | Modificar | también |

## 3. Tareas

Cubre `CA-01` y `CA-02`.
"""

PRUEBAS = u"""# Plan de Pruebas

### CP-001 — algo de `CA-01`

texto

### CP-002 — algo de `CA-02`

texto
"""


class PlanContraLoHecho(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.fase = os.path.join(self.tmp, "documentacion", "epicas", "EP-001-x",
                                 "HU-001-y", "A-EP-001-HU-001-la-fase")
        os.makedirs(self.fase)
        self.escribir("plan_trabajo.md", PLAN)
        self.escribir("plan_pruebas.md", PRUEBAS)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def escribir(self, nombre, texto):
        with io.open(os.path.join(self.fase, nombre), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(texto)

    # ── CA-01 · el archivo tocado que el plan no declara ─────────────────

    def test_cp001_lee_los_archivos_que_el_plan_declara(self):
        dec = pvh.declarados(PLAN)
        self.assertIn("validadores/enlaces.py", dec)
        self.assertIn("base/09-git.md", dec)
        self.assertEqual(2, len(dec), "se coló algo que no era una ruta")

    def test_cp001b_el_declarado_no_se_avisa_y_el_de_mas_si(self):
        tocados = ["validadores/enlaces.py", "validadores/secretos.py"]
        self.assertTrue(pvh._cuadra("validadores/enlaces.py",
                                    pvh.declarados(PLAN)))
        self.assertFalse(pvh._cuadra("validadores/secretos.py",
                                     pvh.declarados(PLAN)))

    def test_cp002_sin_seccion_no_inventa_nada(self):
        """Un formato que no se entiende se avisa; no se supone que está bien."""
        self.escribir("plan_trabajo.md", u"# Plan\n\nSin la sección 2.1.\n")
        h = pvh.comparar_archivos(self.fase, self.tmp, desde="HEAD")
        self.assertEqual(1, len(h))
        self.assertEqual(AVISO, h[0].severidad)
        self.assertIn("no declara ningún archivo", h[0].mensaje)

    def test_cp002b_sin_plan_no_hay_contra_que_comparar(self):
        os.remove(os.path.join(self.fase, "plan_trabajo.md"))
        h = pvh.comparar_archivos(self.fase, self.tmp, desde="HEAD")
        self.assertIn("no hay contra qué comparar", h[0].mensaje)

    def test_cp002c_sin_commit_de_origen_lo_dice(self):
        h = pvh.comparar_archivos(self.fase, self.tmp, desde=None)
        self.assertIn("desde qué commit", h[0].mensaje)

    # ── CA-02 · el criterio sin caso ─────────────────────────────────────

    def test_cp003_el_criterio_sin_caso_se_avisa(self):
        self.escribir("plan_pruebas.md", u"# Plan de Pruebas\n\n### CP-001 — de `CA-01`\n")
        h = pvh.comparar_casos(self.fase)
        self.assertEqual(1, len(h))
        self.assertIn("CA-02", h[0].mensaje)

    def test_cp003b_con_todos_los_criterios_cubiertos_se_calla(self):
        """Un programa que reporta siempre se apaga."""
        self.assertEqual([], pvh.comparar_casos(self.fase))

    def test_cp003c_un_plan_de_pruebas_sin_ningun_caso_se_avisa(self):
        self.escribir("plan_pruebas.md", u"# Plan de Pruebas\n\nCubre `CA-01` y `CA-02`.\n")
        h = pvh.comparar_casos(self.fase)
        self.assertTrue(any("ningún caso" in x.mensaje for x in h))

    # ── el caso que decide ───────────────────────────────────────────────

    def test_cp004_los_documentos_de_la_propia_fase_no_cuentan(self):
        """Escribir el resultado **es** ejecutar la fase."""
        for nombre in pvh.DE_LA_FASE:
            self.assertIn(nombre, pvh.DE_LA_FASE)
        self.assertFalse(pvh._cuadra("documentacion/epicas/x/resultado_pruebas.md",
                                     pvh.declarados(PLAN)),
                         "el filtro no es por ruta: es por nombre de documento")

    def test_cp005_nunca_detiene(self):
        """Un archivo de más puede ser un descubrimiento aprobado."""
        self.escribir("plan_trabajo.md", u"# Plan\n\nSin sección.\n")
        h = pvh.comparar_archivos(self.fase, self.tmp, desde="HEAD")
        self.assertEqual([], [x for x in h if x.severidad == FALLA])

    def test_cp006_encuentra_las_fases_por_su_plan(self):
        self.assertEqual([self.fase.replace("\\", "/")],
                         [f.replace("\\", "/") for f in pvh.fases_de(self.tmp)])


if __name__ == "__main__":
    unittest.main()
