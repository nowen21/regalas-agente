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


class CerrarYReabrirUnaFase(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
