# Funcionalidad implementada · Fase `B-EP-027-HU-005-historia` (módulo Historia: `core/historia/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-027-HU-005-historia` |
| **Módulo** | Historia: `core/historia/` |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-005 (CA-02) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La historia nombra cada cambio por lo que es. La columna «Qué se guarda» dice «Documento del estándar», «Regla» o «Recuerdo», y la columna «Cuál» dice el nombre de lo que cambió; lo que ya se quitó se nombra desde la fila que guardó la historia. El filtro de arriba usa los mismos nombres. Las filas de una página se nombran con una consulta por tabla, y la versión de cada cambio ya no se trae fila por fila.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-02 · La historia con nombres legibles | CA | `core/historia/nombres.py`, `views.py` (`Lista`), `templates/historia/lista.html` | Hecho | CP-001 |
| RNF-01 · Sin una consulta por fila | RNF | `nombres.py` (`nombrar`), `views.py` (`select_related`) | Hecho | CP-001, paso 3 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Menú «Historia»: las columnas «Qué se guarda» y «Cuál», y el filtro de arriba.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo que ya no existe se nombra desde la fila que guardó el cambio | La historia guarda la fila entera; se descartó mostrar el número | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
