# Funcionalidad implementada · Fase `A-EP-005-HU-025-entrega-por-accion` (módulo Enganches de reglas: `proyectos/cimiento/core/herramientas/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-025-entrega-por-accion` |
| **Módulo** | Enganches de reglas: `proyectos/cimiento/core/herramientas/` y `adaptadores/claude-code/` |
| **Especificación del módulo** | Los CA de la [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-025 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Antes de cada acción, `hook_reglas_accion.py` entrega las reglas de la tarea que la acción pide, una sola vez por sesión y por agente, por partes cuando no caben. Con cada mensaje, `hook_reglas.py` trae solo lo que falta de `responder` y de `recibir-pedido`, y ya no el bloque «LAS REGLAS DE CADA TURNO». El aviso de las señales pasó al abrir la sesión y lee la sesión de la entrada.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `core/herramientas/entrega_de_reglas.py`, `adaptadores/claude-code/hook_reglas_accion.py` | ✅ | CP-001, CP-002 |
| CA-02 | Funcional | `core/herramientas/entrega_de_reglas.py` | ✅ | CP-003, CP-004 |
| CA-03 | Funcional | `adaptadores/claude-code/hook_reglas.py`, `core/herramientas/entrega_de_reglas.py` | ✅ | CP-005, CP-006 |
| CA-04 | Funcional | `adaptadores/claude-code/hook_senales.py`, `core/comun/enganches.py` | ✅ | CP-007 |

**Faltantes / diferimientos:** el CA-05 (`base/tareas.md` y la versión) va en la fase B.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple: 7 de 7 casos |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No se usa a mano: corre solo antes de cada acción y con cada mensaje. Llega a los proyectos con `instalar.py`. Se suspende desde Cimiento con el momento «reglas-de-la-accion». Lo entregado de cada sesión queda en `historico-chat/.estado/reglas-entregadas/<sesión>.json`; borrarlo hace que la entrega empiece de nuevo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La entrega por acción va en un enganche aparte del freno | Suspender el freno apagaría las reglas; se descartó meterla en `hook_antes.py` | S-369 |

## 6. Deuda técnica y pendientes generados

Lo entregado se pierde de la conversación cuando Claude Code la resume, y la cuenta dice que llegó: lo resuelve la HU-027. Las reglas de `cambiar-codigo` llegan en unas diez entregas: lo reduce la HU-026.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El catálogo de enganches (`core/comun/enganches.py`) y `.claude/settings.json`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
