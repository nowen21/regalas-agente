# Funcionalidad implementada · Fase `B-EP-005-HU-025-el-estandar-lo-dice` (módulo Estándar: `base/tareas.md`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-025-el-estandar-lo-dice` |
| **Módulo** | Estándar: `base/tareas.md`, que vive en la base de Cimiento |
| **Especificación del módulo** | Los CA de la [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-025 (CA-05) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 59.3.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`base/tareas.md` dice ahora que con cada mensaje llegan solo las reglas de `responder` y, cuando la palabra autoriza cambiar algo, las de `recibir-pedido`; que las de cada tarea llegan con la acción; y que cada regla llega una sola vez en la sesión. Lo aprobó el usuario como propuesta 18, y la versión subió a 59.2.0, MENOR.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-05 | Documental | `base/tareas.md`, sección «Cómo se elige la tarea, sin adivinar», en la base | ✅ | CP-001, CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

La T-01 quedó hecha. La T-02 no hizo falta: Cimiento sube la versión al aprobar la propuesta.

**Tareas que no se hicieron:** la T-02, por esa razón.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple: 2 de 2 casos |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Se lee con `manage.py documento ver estandar base/tareas.md`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se cambió solo la sección del mensaje; la tercera columna de la tabla se queda | Quitarla toca el mapa y es otra decisión | No hace falta: está en el plan, §2.6 |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
