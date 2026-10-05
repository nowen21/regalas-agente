# Funcionalidad implementada · Fase `A-EP-025-HU-008-tablero-en-vivo` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-008-tablero-en-vivo` |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-008 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Gasto» en el menú muestra el gasto de tokens de todos los proyectos: totales, por proyecto y por día en gráficas, las últimas sesiones, los enganches que más agregan y los archivos que más pesan al leerlos. Se filtra por proyecto y por período y se actualiza cada 10 segundos. Al abrirse lee lo nuevo de los `.jsonl`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/templates/consumo/tablero.html`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html`, `proyectos/cimiento/core/consumo/formato.py`, `proyectos/cimiento/core/consumo/templatetags/gasto.py`, `proyectos/cimiento/templates/base.html` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/tablero.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`/gasto/`, desde «Gasto» en el menú, con cualquier cuenta. `?proyecto=«id»&dias=1|7|30` filtra.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El gasto por día se agrupa en Python | Agruparlo en MariaDB pide las tablas de zonas horarias, que WAMP no trae | No hace falta: está en `tablero.py` |
| Leer los `.jsonl` solo al abrir la página entera | Leer es lo lento; lo vivo llega por telemetría | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No hay migración: lee las tablas de la HU-006.
