# Funcionalidad implementada · Fase `A-EP-027-HU-006-version-del-proyecto` (módulo Historia: `core/historia/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-006-version-del-proyecto` |
| **Módulo** | Historia: `core/historia/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-01) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El cambio de una regla de un proyecto sube la versión de ese proyecto, y el de una regla del estándar, la del estándar. La tarea y la dependencia de una regla siguen a su regla.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · La regla del proyecto versiona su proyecto | CA | `core/historia/versiones.py` (`ambito_de`) | Hecho | CP-001 |

**Faltantes / diferimientos:** las fases B a E de la HU-006.

### 2.2 Plan de trabajo → ejecución

La tarea del plan quedó hecha.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No tiene entrada propia: lo usa la historia al guardar.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La regla es del proyecto si trae proyecto y del estándar si no | En `VERSIONADAS`, una tabla sin proyecto no lleva versión; se descartó cambiar ese sentido | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno.
