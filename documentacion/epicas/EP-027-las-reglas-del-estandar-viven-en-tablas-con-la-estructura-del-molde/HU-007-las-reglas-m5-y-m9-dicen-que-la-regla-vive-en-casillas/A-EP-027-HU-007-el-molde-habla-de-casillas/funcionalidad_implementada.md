# Funcionalidad implementada · Fase `A-EP-027-HU-007-el-molde-habla-de-casillas` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-007-el-molde-habla-de-casillas` |
| **Módulo** | Estándar en la base, capítulo `20` |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`20·M5` dice que cada parte de la regla va en su casilla y que el texto del agente se arma desde ellas; `20·M9`, el capítulo 20, la fila 18 del checklist y el molde mandan a la casilla «validable», con tres valores. Los cinco cambios se propusieron y el usuario los aprobó en la pantalla (versiones 56.12.0 a 56.16.0).

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Estándar» → «Propuestas».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| «Validable» tiene tres valores y el programa al lado | Con solo sí o no se perdía qué programa comprueba cada regla | S-346 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguna: el texto ya quedó en la base.
