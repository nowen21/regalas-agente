# Funcionalidad implementada · Fase `A-EP-025-HU-032-catalogo-y-pantalla` (módulo Las suspensiones de Cimiento: `proyectos/cimiento/core/proyectos/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-032-catalogo-y-pantalla` |
| **Módulo** | Las suspensiones de Cimiento: `proyectos/cimiento/core/proyectos/`, con el catálogo de `core/comun/enganches.py` y sus ayudas |
| **Especificación del módulo** | Los CA de la [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-032 (CA-01) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cada momento de un enganche tiene un nombre fijo (`MOMENTOS`, por evento y guion) y cada revisión de git otro (`REVISIONES_GIT`, por la orden de `validar.py`); lo que no conviene suspender lleva su motivo (`NO_CONVIENE`). La pantalla de suspensiones deja suspender cualquiera de ellos, el histórico incluido, y muestra la tabla con la recomendación. Un enganche sin nombre se guarda como «freno», como antes.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Catálogo y pantalla | `core/comun/enganches.py`, `core/proyectos/ajustes.py`, `forms.py`, `views.py`, `suspensiones.html` | ✅ | CP-001, CP-002 |

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

En Cimiento → Proyectos → Suspensiones: «Un enganche o una revisión de git», con el nombre de la tabla de abajo, motivo y vencimiento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El nombre sale de `(evento, guion)` | El instalador, el desinstalador y el checklist desarman `HOOKS_CLAUDE` en cinco campos; se descartó un sexto | `S-365` |

## 6. Deuda técnica y pendientes generados

Lo suspendido todavía no apaga nada: lo leen los enganches en la fase B y git en la fase C.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-032 en la tabla de la EP-025; el README de la carpeta de la HU.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento.
