# Funcionalidad implementada · Fase `A-EP-027-HU-005-propuestas-y-memoria` (módulo Estándar en la base: `core/estandar/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-005-propuestas-y-memoria` |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-005 (CA-01) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Las propuestas dicen qué cambian por su nombre: el título del documento, con el código de la regla si es una, o el del recuerdo. La memoria de cada proyecto lista cada recuerdo por su nombre legible, con su descripción debajo, y el recuerdo abierto lleva ese nombre de título. Cada tabla del estándar sabe decir su nombre («documento del estándar», «regla»...) y cada fila su nombre legible, con `nombre_legible()`: la historia lo usa en la fase B.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · Propuestas y memoria con nombres legibles | CA | `core/estandar/models.py` (`nombre_legible`, `descripcion`), `presentar.py` (`recuerdo_legible`, `titulo_de_texto`), `propuestas.html`, `recuerdos.html`, `recuerdo.html` | Hecho | CP-001 |

**Faltantes / diferimientos:** la historia, en la fase B (`core/historia/`).

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

«Estándar → Propuestas por aprobar» y la memoria de cada proyecto, en «Estándar → Reglas y documentos».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Cada modelo dice su nombre con `nombre_legible()` | Una sola manera para todas las pantallas; se descartó que cada pantalla lo armara | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate estandar`: la migración `0006_nombres` solo cambia nombres que Django guarda en su estado.
