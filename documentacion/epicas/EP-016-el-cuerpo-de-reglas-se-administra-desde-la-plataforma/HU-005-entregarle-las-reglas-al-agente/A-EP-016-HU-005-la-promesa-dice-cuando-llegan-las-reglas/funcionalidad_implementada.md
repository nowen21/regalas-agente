# Funcionalidad implementada · Fase `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas` (módulo Reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas` |
| **Módulo** | Reglas |
| **Especificación del módulo** | `F-009` del [inventario](../../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-005 (CA-01) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.4.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

La plataforma ya no promete que las reglas llegan al abrir la sesión. `F-009` se llama «Entregarle al agente las reglas que rigen en el proyecto» y dice lo que pasa: con cada mensaje llegan las de la tarea, y enteras cuando se piden. Al abrir no caben, porque la herramienta acepta 10.000 caracteres por enganche. El código no cambió.

## 2. Trazabilidad  ·  `13·DOC11`

| Tarea | Qué se hizo | Dónde quedó | Evidencia |
|---|---|---|---|
| T-01 | Narrativa, contexto, título del CA-01, estado y bitácora | [HU-005](../HU-005-entregarle-las-reglas-al-agente.md) | CP-001 |
| T-02 | Las tres líneas de `F-009`, y la del agente entre los interesados | [epica.md](../../epica.md) | CP-001 |
| T-03 | `RF-09` y la ficha de `F-009` | `cvds/analisis-requisitos/` | CP-001 |
| T-04 | Pruebas, planificación y decisiones de arquitectura | `cvds/` | CP-001 |
| T-05 | La búsqueda final, y cinco promesas más que encontró | `cvds/planificacion/`, `cvds/diseno/README.md` | CP-001 |

**Faltantes / diferimientos:** ninguno.

## 3. Qué se probó

| Qué | Resultado |
|---|---|
| CP-001, cuatro pasos | Cumple; detalle en [resultado_pruebas.md](resultado_pruebas.md) |
| `validar.py estandar` | Sin incumplimientos |
