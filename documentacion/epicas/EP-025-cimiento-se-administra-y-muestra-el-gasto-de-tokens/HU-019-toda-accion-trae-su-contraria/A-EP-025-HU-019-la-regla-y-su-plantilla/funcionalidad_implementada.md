# Funcionalidad implementada · Fase `A-EP-025-HU-019-la-regla-y-su-plantilla` (módulo `base/02-flujo-de-trabajo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-019-la-regla-y-su-plantilla` |
| **Módulo** | `base/02-flujo-de-trabajo/` |
| **Especificación del módulo** | Los CA de la [HU-019](../HU-019-toda-accion-trae-su-contraria.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-019 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La regla `02·F30`, «Toda acción trae su contraria», y la sección 2.8 del plan de trabajo, donde cada fase declara la contraria de cada acción que agrega. Versión 55.0.0, mayor.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Documentación | `base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md`, `base/02-flujo-de-trabajo/base.md`, `base/mapa-de-tareas.md`, `validadores/reglas-validables.md` | ✅ | CP-001 |
| CA-02 | Documentación | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | ✅ | CP-002 |
| CA-03 | Documentación | `CHANGELOG.md`, `VERSION` | ✅ | CP-003 |

**Faltantes / diferimientos:** el validador, hasta que la regla se cumpla a mano (`20·M19`).

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Al planear una fase, llenar la sección 2.8 del plan: cada acción nueva, su contraria y la prueba que hace las dos.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| No validable por ahora | Que la contraria sea la correcta es criterio | No hace falta: está en el checklist de `F30` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El catálogo del `02`, `base/mapa-de-tareas.md` y `validadores/reglas-validables.md`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Llega a cada proyecto con la versión 55.0.0.
