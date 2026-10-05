# Funcionalidad implementada · Fase `A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba` (módulo `base/02-flujo-de-trabajo/` y `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba` |
| **Módulo** | `base/02-flujo-de-trabajo/` y `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-aprobar-el-analisis-aprueba-lo-que-sale-de-el.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-008 (CA-01, CA-02 y CA-03) |
| **Fecha de cierre** | 2026-10-04 |
| **Versión del estándar al cerrar** | 54.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`02·F4` y `02·F25` dicen que el plan que sale de un análisis aprobado y cumple sus filas ya tiene el OK, y lo cita. La plantilla del plan muestra cómo citarlo, y el freno y la comparación del commit lo aceptan solo si el análisis está aprobado y nombra la HU del plan.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Regla | `base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md`, `base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/enganches/plan_vs_hecho.py`, `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/origen.py` | ✅ | CP-002 |
| CA-03 | Plantilla | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

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

En la fila **Aprobación** del plan se escribe el enlace al análisis aprobado en lugar del nombre de quien aprueba: `[análisis N del pendiente P](«ruta»/analisis-N.md)`, el AAAA-MM-DD, con la versión X.Y.Z.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El análisis citado tiene que nombrar la HU del plan en «Lo que se tiene que hacer» | Sin eso, cualquier análisis aprobado aprobaría cualquier plan | No hace falta: está en la regla y en el código |
| La versión que vale para el freno sigue saliendo de la línea de aprobación | El programa ya lee esa línea; cambiar su forma rompía los planes aprobados | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `base/reglas-por-tarea/`, regenerado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 54.0.0.
