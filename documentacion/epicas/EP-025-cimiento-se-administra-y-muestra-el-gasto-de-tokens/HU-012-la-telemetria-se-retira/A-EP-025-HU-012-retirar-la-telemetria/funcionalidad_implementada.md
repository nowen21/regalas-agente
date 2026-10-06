# Funcionalidad implementada · Fase `A-EP-025-HU-012-retirar-la-telemetria` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-012-retirar-la-telemetria` |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-012](../HU-012-la-telemetria-se-retira.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-012 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Salieron la ruta `/v1/logs`, su vista, el lector de la telemetría y su guardado. La instalación dejó de activarla y quita las seis variables que había puesto en `~/.claude/settings.json`, solo con el valor que puso; la desinstalación usa lo mismo. El gasto llega por un solo camino, el `.jsonl`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/desinstalar.py` | ✅ | CP-002 |

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

No hay que hacer nada: la instalación del estándar quita las variables donde quedaron.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Sale solo la variable con el valor exacto de la instalación | Una con otro valor la puso el usuario | No hace falta: está en `instalar.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La bitácora de la HU-007 dice que quedó sin efecto.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Correr la instalación del estándar.
