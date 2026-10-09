# -*- coding: utf-8 -*-
"""Cerrar y reabrir una fase (`EP-025·HU-016`).

Sin Django: corren con `python -m unittest core.herramientas.tests_fase` desde
`proyectos/cimiento/`.
"""
import io
import os
import sys
import tempfile
import unittest

from .fase import MARCA, Fase

EPICA = "EP-001-algo"
HU = "HU-001-la-historia"
FASE = "A-EP-001-HU-001-la-fase"

PLAN = """# Plan de Trabajo · Fase `%s` (módulo `m/`)   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Módulo** | `m/` |

**Aprobación** (`02·F4`): [análisis 1](x.md), el 2026-10-05, con la versión 1.0.0

| CA de HU-001 | Estado |
|---|---|
| CA-01 · Uno | ☐ |
| CA-02 · Dos | ☐ |

## 1. Objetivo

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Uno | Programa | Baja |
| CA-02 | Dos | Documentación | Baja |

## 3. Desglose

### CA-01 · Uno

| ID | Qué | Dónde | Por qué |
|---|---|---|---|
| T-01 | Hacer | `a.py` | CA-01 |

### CA-02 · Dos

| ID | Qué | Dónde | Por qué |
|---|---|---|---|
| T-02 | Hacer | `b.md` | CA-02 |

## 13. Cierre

«Se llena al cerrar la fase.»
""" % FASE

PRUEBAS = """# Plan de Pruebas · Fase `%s`   ·   `[CAPA 3]`

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-001 | CA-02 | CP-002 | Errores | Media | Sí | ☐ |

## 6. Casos
""" % FASE

HU_MD = """# HU-001 · La historia

| Campo | Valor |
|---|---|
| **Estado** | En curso |

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|

---

## 9. Dependencias y riesgos
"""

EPICA_MD = """# EP-001 · Algo

## 9. Historias

| ID | Título | Estado |
|---|---|---|
| [HU-001](%s/%s.md) | La historia | En curso |

## 15. Orden

| # | HU | Depende de | Por qué | Estado |
|---|---|---|---|---|
| 1 | HU-001 | Ninguna | Primera | En curso |
""" % (HU, HU)


def _leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def _escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _llenar(ruta):
    """Lo que haría quien cierra: decir que cumple y llenar el resto."""
    texto = _leer(ruta).replace("**Concepto:** %s" % MARCA, "**Concepto:** Cumple")
    _escribir(ruta, texto.replace(MARCA, "lleno"))


class ConUnaFase(unittest.TestCase):
    """Una fase de juguete en una carpeta temporal, con los planes en el formato viejo."""

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.epica = os.path.join(carpeta.name, "documentacion", "epicas", EPICA)
        self.hu = os.path.join(self.epica, HU)
        self.fase = os.path.join(self.hu, FASE)
        os.makedirs(self.fase)
        _escribir(os.path.join(self.epica, "epica.md"), EPICA_MD)
        _escribir(os.path.join(self.hu, HU + ".md"), HU_MD)
        _escribir(self.doc("plan_trabajo.md"), PLAN)
        _escribir(self.doc("plan_pruebas.md"), PRUEBAS)
        for archivo in ("estado-fase.md", "resultado_pruebas.md", "funcionalidad_implementada.md"):
            _escribir(self.doc(archivo), "# Plantilla · Fase «A-EP01-HU03-Descripción»\n")

    def doc(self, archivo):
        return os.path.join(self.fase, archivo)

    def llenar_todo(self):
        for archivo in ("estado-fase.md", "resultado_pruebas.md", "funcionalidad_implementada.md"):
            _llenar(self.doc(archivo))

    def hu_md(self):
        return _leer(os.path.join(self.hu, HU + ".md"))

    def epica_md(self):
        return _leer(os.path.join(self.epica, "epica.md"))


class CerrarYReabrirUnaFase(ConUnaFase):

    # CP-001 · Cerrar
    def test_la_primera_pasada_escribe_y_dice_que_falta(self):
        accion, tocados, faltan = Fase(self.fase).cerrar(escribir=True)
        self.assertTrue(accion.startswith("faltan"))
        self.assertTrue(faltan)
        self.assertEqual(3, len(tocados))
        resultado = _leer(self.doc("resultado_pruebas.md"))
        self.assertIn("| CP-001 | CA-01 | Alta |", resultado)
        self.assertIn("| CP-002 | CA-02 | Media |", resultado)
        funcionalidad = _leer(self.doc("funcionalidad_implementada.md"))
        self.assertIn("| CA-01 | Programa | `a.py` | ✅ | CP-001 |", funcionalidad)
        self.assertIn("**Hechas:** 2 de 2", _leer(self.doc("estado-fase.md")))
        self.assertEqual(HU_MD, self.hu_md())
        self.assertEqual(EPICA_MD, self.epica_md())

    def test_sin_marcas_cierra_en_el_plan_la_hu_y_la_epica(self):
        Fase(self.fase).cerrar(escribir=True)
        self.llenar_todo()
        accion, _, faltan = Fase(self.fase).cerrar(escribir=True)
        self.assertEqual(("cerrada", []), (accion, faltan))
        self.assertNotIn("☐", _leer(self.doc("plan_pruebas.md")))
        plan = _leer(self.doc("plan_trabajo.md"))
        self.assertIn("Las 2 tareas quedaron hechas", plan)
        self.assertIn("| CA-01 · Uno | ☑ |", plan)
        hu = self.hu_md()
        self.assertIn("| `%s` | CA-01 a CA-02 |" % FASE, hu)
        self.assertIn("| **Estado** | Terminada |", hu)
        self.assertIn("| La historia | Terminada |", self.epica_md())
        self.assertIn("| Primera | Terminada |", self.epica_md())
        self.assertIn("| **Concepto** | Cumple |", _leer(self.doc("estado-fase.md")))
        self.assertIn("| **Veredicto** | Cumple |", _leer(self.doc("funcionalidad_implementada.md")))

    def test_cerrar_otra_vez_no_cambia_nada(self):
        Fase(self.fase).cerrar(escribir=True)
        self.llenar_todo()
        Fase(self.fase).cerrar(escribir=True)
        hu = self.hu_md()
        self.assertEqual([], Fase(self.fase).cerrar(escribir=True)[1])
        self.assertEqual(hu, self.hu_md())

    # CP-002 · Reabrir
    def test_reabrir_devuelve_todo_a_en_curso_y_pide_el_ciclo_nuevo(self):
        Fase(self.fase).cerrar(escribir=True)
        self.llenar_todo()
        Fase(self.fase).cerrar(escribir=True)
        accion, _ = Fase(self.fase).reabrir("falló en otro proyecto", escribir=True)
        self.assertEqual("reabierta", accion)
        self.assertIn("| **Estado** | En curso |", self.hu_md())
        self.assertIn("| `%s` |" % FASE, self.hu_md())
        self.assertIn("| La historia | En curso |", self.epica_md())
        self.assertIn("| Primera | En curso |", self.epica_md())
        estado = _leer(self.doc("estado-fase.md"))
        self.assertIn("**Estación actual:** 8", estado)
        self.assertIn("Reabierta el", estado)
        self.assertIn("**Reabierta**", _leer(self.doc("plan_trabajo.md")))
        self.assertIn("☐", _leer(self.doc("plan_pruebas.md")))
        self.assertIn("| 2 |", _leer(self.doc("resultado_pruebas.md")))
        # Sin llenar el ciclo 2 no se cierra; llenándolo, sí.
        self.assertTrue(Fase(self.fase).cerrar(escribir=True)[2])
        self.llenar_todo()
        self.assertEqual("cerrada", Fase(self.fase).cerrar(escribir=True)[0])
        self.assertIn("Cerrada otra vez", _leer(self.doc("plan_trabajo.md")))
        self.assertIn("| **Estado** | Terminada |", self.hu_md())

    def test_no_se_reabre_lo_que_no_esta_cerrado(self):
        with self.assertRaises(ValueError):
            Fase(self.fase).reabrir("por si acaso", escribir=True)
        with self.assertRaises(ValueError):
            Fase(self.fase).reabrir("", escribir=True)

    # CP-004 · Rechazos y simulación
    def test_una_carpeta_que_no_es_fase_se_rechaza(self):
        with self.assertRaises(ValueError):
            Fase(self.hu)

    def test_si_las_pruebas_fallan_no_toca_nada(self):
        with self.assertRaises(ValueError):
            Fase(self.fase).cerrar(escribir=True, pruebas='"%s" -c "import sys; sys.exit(1)"' % sys.executable)
        self.assertIn("«", _leer(self.doc("resultado_pruebas.md")).split("\n")[0])

    def test_con_las_pruebas_en_verde_el_resultado_lo_dice(self):
        Fase(self.fase).cerrar(escribir=True, pruebas='"%s" -c "print(1)"' % sys.executable)
        resultado = _leer(self.doc("resultado_pruebas.md"))
        self.assertIn("| Aprobado | EV-01 |", resultado)
        self.assertIn("**Concepto:** Cumple.", resultado)

    def test_sin_aplicar_no_toca_nada(self):
        accion, tocados, faltan = Fase(self.fase).cerrar()
        self.assertTrue(faltan)
        self.assertEqual(3, len(tocados))
        self.assertIn("«", _leer(self.doc("estado-fase.md")).split("\n")[0])


# ── `EP-025·HU-031` · Los planes en el formato de las plantillas ──────────────
# Copiados de `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` y `08-plan-pruebas.md`:
# varios casos por fila, con enlace; una fila de RNF; CA sin nombre y como enlace.

PLAN_PLANTILLA = """# Plan de Trabajo · Fase `%s` (módulo `m/`)   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Módulo** | `m/` |

**Aprobación** (`02·F4`): [análisis 1](x.md), el 2026-10-05, con la versión 1.0.0

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| CA-01 | ☐ |
| [CA-02](../%s.md#ca-02--dos) | ☐ |

## 3. Desglose

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Hacer | Lógica | 1 h | — | EV-01 |

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas | EV-01 | | ☐ |
| CA-02 | Pruebas | EV-01 | | ☐ |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase

## 13. Cierre

**Hallazgos al ejecutar:** «se llena al cerrar»
""" % (FASE, HU)

PRUEBAS_PLANTILLA = """# Plan de Pruebas · Fase `%s`   ·   `[CAPA 3]`

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | [CP-001](#cp-001--uno), [CP-002](#cp-002--uno-negativo) | Funcional | Crítica | Sí | ☐ |
| HU-001 | CA-02 | CP-003 | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF-01 | CP-004 | Seguridad | Crítica | No | ☐ |

## 6. Casos
""" % FASE

HU_PLANTILLA = HU_MD.replace("## 8. Fases", """### CA-01 · Uno

### CA-02 · Dos

## 7. Tareas técnicas derivadas

- [ ] Hacer.

## 8. Fases""").replace("## 9. Dependencias y riesgos", """## 9. Dependencias y riesgos

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
""")


class LosFormatosDeLasPlantillas(ConUnaFase):

    def setUp(self):
        super().setUp()
        _escribir(os.path.join(self.hu, HU + ".md"), HU_PLANTILLA)
        _escribir(self.doc("plan_trabajo.md"), PLAN_PLANTILLA)
        _escribir(self.doc("plan_pruebas.md"), PRUEBAS_PLANTILLA)

    def cerrar(self):
        Fase(self.fase).cerrar(escribir=True)
        self.llenar_todo()
        return Fase(self.fase).cerrar(escribir=True)

    # CP-001 · Lee la matriz y los CA de la plantilla
    def test_lee_todos_los_casos_y_los_ca_sin_nombre(self):
        fase = Fase(self.fase)
        self.assertEqual(["CP-001", "CP-002", "CP-003", "CP-004"], [cp for _ca, cp, _t, _p in fase.casos()])
        self.assertEqual([("CA-01", "Uno"), ("CA-02", "Dos")], fase.plan()["cas"])
        fase.cerrar(escribir=True)
        resultado = _leer(self.doc("resultado_pruebas.md"))
        for fila in ("| CP-001 | CA-01 | Crítica |", "| CP-002 | CA-01 | Crítica |", "| CP-003 | CA-02 | Alta |",
                     "| CP-004 | RNF-01 | Crítica |", "| CA-01 | CP-001, CP-002 |", "| RNF-01 | CP-004 |"):
            self.assertIn(fila, resultado)
        self.assertIn("| CA-02 |", _leer(self.doc("funcionalidad_implementada.md")))

    # CP-002 · Al cerrar marca todo
    def test_al_cerrar_marca_todo(self):
        self.assertEqual("cerrada", self.cerrar()[0])
        self.assertNotIn("☐", _leer(self.doc("plan_pruebas.md")))
        plan = _leer(self.doc("plan_trabajo.md"))
        self.assertIn("| CA-01 | ☑ |", plan)
        self.assertIn("| [CA-02](../%s.md#ca-02--dos) | ☑ |" % HU, plan)
        hoy = Fase(self.fase).hoy
        self.assertIn("| CA-01 | Pruebas | EV-01 | %s | ☑ |" % hoy, plan)
        self.assertIn("- [x] Pruebas en verde", plan)
        self.assertIn("- [ ] Rama lista para el commit", plan)
        hu = self.hu_md()
        self.assertIn("- [x] Hacer.", hu)
        self.assertIn("- [x] Todos los criterios de aceptación verificados", hu)

    # CP-003 · Al reabrir desmarca lo mismo
    def test_al_reabrir_desmarca_lo_mismo(self):
        self.cerrar()
        Fase(self.fase).reabrir("falló", escribir=True)
        self.assertNotIn("☑", _leer(self.doc("plan_pruebas.md")))
        plan = _leer(self.doc("plan_trabajo.md"))
        self.assertIn("| CA-01 | ☐ |", plan)
        self.assertIn("| CA-01 | Pruebas | EV-01 |  | ☐ |", plan)
        self.assertNotIn("- [x]", plan)
        self.assertNotIn("- [x]", self.hu_md())

    def test_con_la_hu_en_curso_no_desmarca_lo_marcado_a_mano(self):
        _escribir(os.path.join(self.hu, HU + ".md"), HU_PLANTILLA.replace("- [ ] Hacer.", "- [x] Hacer.").replace(
            "|---|---|---|---|---|---|---|\n", "|---|---|---|---|---|---|---|\n| `B-EP-001-HU-001-otra` | CA-02 | (vacío) "
            "| a | b | c | En curso |\n"))
        self.cerrar()
        self.assertIn("| **Estado** | En curso |", self.hu_md())
        self.assertIn("- [x] Hacer.", self.hu_md())


if __name__ == "__main__":
    unittest.main()
