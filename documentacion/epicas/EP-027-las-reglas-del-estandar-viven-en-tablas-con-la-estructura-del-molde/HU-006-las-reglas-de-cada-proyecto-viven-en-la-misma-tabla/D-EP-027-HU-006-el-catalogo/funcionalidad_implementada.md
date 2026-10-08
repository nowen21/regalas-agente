# Funcionalidad implementada · Fase `D-EP-027-HU-006-el-catalogo` (módulo Validadores: `core/validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-027-HU-006-el-catalogo` |
| **Módulo** | Validadores: `core/validadores/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-04) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El validador del catálogo (`20·M16`) revisa las reglas de un proyecto en la tabla de Cimiento cuando viven ahí: arma el texto de cada regla desde sus casillas y comprueba su respaldo como siempre. Sin reglas en la tabla, lee el archivo como antes. El mapa del amarre nombra la pieza nueva de la fase C.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04 · El validador del catálogo lee la tabla | CA | `core/validadores/metareglas.py` (`CatalogoDelProyecto.en_la_base`, `validar`) | Hecho | CP-001 |

**Faltantes / diferimientos:** ninguno de esta fase.

### 2.2 Plan de trabajo → ejecución

La tarea del plan quedó hecha.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `anatomia/que-esta-amarrado-a-la-herramienta.md` se declaró en el plan antes de tocarlo.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`validar.py catalogo`, como siempre.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El texto de cada regla se arma desde sus casillas y se revisa igual | Lo que comprueba no cambia; se descartó reescribir el validador | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`anatomia/que-esta-amarrado-a-la-herramienta.md`: 34 amarrados de 120.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno.
