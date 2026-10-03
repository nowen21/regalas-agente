# -*- coding: utf-8 -*-
"""`EP-023 · HU-002 · fase B` · Los acuerdos llegan al agente, y el plan marca lo suyo.

CP-001: los acuerdos de la fase en curso.
CP-002: los del análisis prendido, con su tope; el enganche nunca detiene.
CP-003: cada decisión del plan aprobado desde 50.0.0 cita su acuerdo o es propuesta del agente.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(VALIDADORES)
sys.path.insert(0, VALIDADORES)

import acuerdos             # noqa: E402
import comun                # noqa: E402
import instalar             # noqa: E402
import origen               # noqa: E402

EPICA = "documentacion/epicas/EP-009-algo"
PENDIENTE = EPICA + "/pendientes/110-algo-falla"
HU = EPICA + "/HU-001-una-cosa"
FASE = HU + "/A-EP-009-HU-001-la-fase"
APROBADO = "> **Aprobado** por el usuario el 2026-10-03, en el turno 2.\n\n"


def analisis(numero, aprobado=True, acuerdos_=("Tema uno: lo primero (turno 1).", "Tema dos: lo segundo (turno 1).")):
    puntos = "\n".join("%d. %s" % (i, a) for i, a in enumerate(acuerdos_, 1))
    filas = "\n".join("| %d | Hacer %d | %d | HU-001 |" % (i, i, i) for i in range(1, len(acuerdos_) + 1))
    return ("# Análisis %d\n\n%s### 1 · Usuario, 2026-10-03 08:00:00\n\n> algo\n\n"
            "## Lo acordado\n\n%s\n\n## Lo que se tiene que hacer\n\n"
            "| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |\n|---|---|---|---|\n%s\n\n"
            "## Lo que aporta al análisis principal\n" % (numero, APROBADO if aprobado else "", puntos, filas))


def plan(version="50.0.0", sale="Análisis 1, acuerdo 1", con_columna=True):
    aprobacion = "**Aprobación** (`02·F4`): Ana Pérez, el 2026-10-03, con la versión %s.\n\n" % version
    if con_columna:
        tabla = ("| Decisión | Alternativa descartada | Justificación | Sale de |\n|---|---|---|---|\n"
                 "| Hacer algo | Otra cosa | Porque sí | %s |\n" % sale)
    else:
        tabla = "| Decisión | Alternativa descartada | Justificación |\n|---|---|---|\n| Hacer algo | Otra cosa | Porque sí |\n"
    return ("# Plan\n\n%s| CA de HU-001 | Estado |\n|---|---|\n| CA-01 · Uno | ☐ |\n\n"
            "### 2.6 Decisiones técnicas\n\n%s\n### 2.7 Dudas\n\nNinguna.\n\n## 3. Tareas\n" % (aprobacion, tabla))


class Proyecto(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        self.escribir(PENDIENTE + "/analisis-1.md", analisis(1))
        self.escribir(HU + "/HU-001-una-cosa.md",
                      "# HU-001\n\n## 4. Criterios\n\n### CA-01 · Uno\n\n**Sale de:** análisis 1, punto 1.\n\n"
                      "### CA-02 · Dos\n\n**Sale de:** análisis 1, punto 2.\n\n## 5. Otra\n")
        os.makedirs(os.path.join(self.raiz, *FASE.split("/")))

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, relativa, texto):
        ruta = os.path.join(self.raiz, *relativa.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def claves(self):
        return [c for c, _ in acuerdos.de_la_fase(os.path.join(self.raiz, *FASE.split("/")))]


class LosAcuerdosDeLaFase(Proyecto):
    """CP-001."""

    def test_la_fase_recien_creada_recibe_los_de_todos_sus_ca(self):
        self.assertEqual(["Análisis 1 del pendiente 110, acuerdo 1", "Análisis 1 del pendiente 110, acuerdo 2"],
                         self.claves())

    def test_con_plan_recibe_solo_los_de_sus_ca(self):
        self.escribir(FASE + "/plan_trabajo.md", plan())
        self.assertEqual(["Análisis 1 del pendiente 110, acuerdo 1"], self.claves())

    def test_con_el_commit_anotado_ya_no_esta_en_curso(self):
        self.assertEqual(1, len(acuerdos.fases_en_curso(self.raiz)))
        self.escribir(FASE + "/estado-fase.md", "| 12 | Commit | 👤 autorizado | ✅ `abc1234` |\n")
        self.assertEqual([], acuerdos.fases_en_curso(self.raiz))

    def test_la_fase_vieja_cerrada_no_esta_en_curso(self):
        self.escribir(FASE + "/plan_trabajo.md", "# Plan\n\nAprobado por el usuario.\n")
        self.escribir(FASE + "/funcionalidad_implementada.md", "# Cierre\n")
        self.assertEqual([], acuerdos.fases_en_curso(self.raiz))

    def test_la_fase_nueva_con_cierre_y_sin_commit_sigue_en_curso(self):
        self.escribir(FASE + "/plan_trabajo.md", plan())
        self.escribir(FASE + "/funcionalidad_implementada.md", "# Cierre\n")
        self.assertEqual(1, len(acuerdos.fases_en_curso(self.raiz)))


class LosAcuerdosDelAnalisisPrendido(Proyecto):
    """CP-002."""

    def prender(self):
        self.escribir(PENDIENTE + "/analisis-2.md", analisis(2, acuerdos_=("Tema tres: lo tercero (turno 1).",)))
        self.escribir(PENDIENTE + "/analisis-3.md", analisis(3, aprobado=False))
        self.escribir("historico-chat/.estado/analisis-en-curso.txt",
                      "analisis=%s/analisis-3.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE)

    def test_llegan_los_de_los_analisis_aprobados_del_pendiente(self):
        self.prender()
        claves = [c for c, _ in acuerdos.del_analisis_prendido(self.raiz)]
        self.assertEqual(["Análisis 1 del pendiente 110, acuerdo 1", "Análisis 1 del pendiente 110, acuerdo 2",
                          "Análisis 2 del pendiente 110, acuerdo 1"], claves)

    def test_los_que_no_caben_llegan_nombrados(self):
        self.prender()
        texto = acuerdos.texto(self.raiz, tope=len(acuerdos.ENCABEZADO) + 400)
        self.assertIn("[NO CUPIERON", texto)
        self.assertIn("Análisis 2 del pendiente 110, acuerdo 1: Tema tres", texto)

    def test_el_enganche_no_detiene_con_una_entrada_danada(self):
        enganche = os.path.join(RAIZ, "adaptadores", "claude-code", "hook_acuerdos.py")
        r = subprocess.run([sys.executable, enganche, "--raiz", os.path.join(self.raiz, "no-existe")],
                           input=b"esto no es json", capture_output=True)
        self.assertEqual(0, r.returncode)

    def test_el_instalador_registra_el_enganche(self):
        self.assertIn("hook_acuerdos.py", [h[2] for h in instalar.HOOKS_CLAUDE])


class LaDecisionDelPlanDiceDeDondeSale(Proyecto):
    """CP-003."""

    def fallas(self, texto):
        self.escribir(FASE + "/plan_trabajo.md", texto)
        ruta = os.path.join(self.raiz, *(FASE + "/plan_trabajo.md").split("/"))
        datos = {1: origen.leer_analisis(os.path.join(self.raiz, *(PENDIENTE + "/analisis-1.md").split("/")))}
        return [m for _, m in origen._revisar_plan(ruta, datos)]

    def test_la_plantilla_tiene_la_columna(self):
        texto = comun.leer(os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md"))
        self.assertIn("| Decisión | Alternativa descartada | Justificación | Sale de |", texto)

    def test_sin_acuerdo_ni_marca_falla(self):
        self.assertEqual(1, len(self.fallas(plan(sale="Me pareció bien"))))

    def test_un_acuerdo_que_no_existe_falla(self):
        self.assertIn("que no existe", self.fallas(plan(sale="Análisis 1, acuerdo 9"))[0])

    def test_cita_valida_o_propuesta_pasan(self):
        self.assertEqual([], self.fallas(plan()))
        self.assertEqual([], self.fallas(plan(sale="Propuesta del agente")))

    def test_sin_la_columna_falla(self):
        self.assertIn("«Sale de»", self.fallas(plan(con_columna=False))[0])

    def test_el_plan_aprobado_antes_no_se_revisa(self):
        self.assertEqual([], self.fallas(plan(version="49.0.0", sale="Me pareció bien")))
        self.assertEqual([], self.fallas(plan(version="49.0.0", con_columna=False)))


if __name__ == "__main__":
    unittest.main()
