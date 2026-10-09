# Funcionalidad implementada · Fase `D-EP-025-HU-032-pantalla-en-pestanas` (módulo Las suspensiones de Cimiento: `proyectos/cimiento/core/proyectos/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-025-HU-032-pantalla-en-pestanas` |
| **Módulo** | Las suspensiones de Cimiento: `proyectos/cimiento/core/proyectos/` |
| **Especificación del módulo** | Los CA de la [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-032 (CA-04) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La pantalla de suspensiones va en tres pestañas: «Suspensiones», abierta al entrar, con el botón «Suspender» al principio que abre el formulario en un modal; «Reglas», con las reglas que se pueden suspender, y «Enganches», con los momentos y las revisiones de git y su recomendación, las dos en tablas que ordenan, filtran y paginan como la de suspensiones. Si el formulario trae errores, el modal vuelve abierto.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04 | Pantalla | `core/proyectos/templates/proyectos/suspensiones.html`, `core/proyectos/views.py` | ✅ | CP-008, CP-009 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Cimiento → Proyectos → Suspensiones: el botón «Suspender» abre el formulario; los códigos de reglas y los nombres de enganches están en sus pestañas.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Pestañas y modal de Bootstrap | Se descartó pedir cada pestaña con htmx: las tres partes son cortas y ya están en la página | `S-371` |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-032 en la tabla de la EP-025.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento.
