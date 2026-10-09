# Funcionalidad implementada · Fase `A-EP-005-HU-027-nucleo-y-resumen` (módulo Enganches de reglas: `proyectos/cimiento/core/herramientas/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-027-nucleo-y-resumen` |
| **Módulo** | Enganches de reglas: `proyectos/cimiento/core/herramientas/` y `adaptadores/claude-code/` |
| **Especificación del módulo** | Los CA de la [HU-027](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-027 (CA-01 y CA-02) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al abrir la sesión, `hook_reglas_sesion.py` entrega el núcleo (las reglas blindadas); lo que no cabe llega con los mensajes siguientes, porque el mensaje lo trata como una tarea más. Después de un resumen de la conversación (`compact`) o de limpiarla (`clear`), la cuenta del agente principal vuelve a cero: el núcleo, `responder` y las reglas de cada tarea llegan otra vez. Al retomar (`resume`) no cambia nada, y los subagentes conservan su cuenta.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `core/herramientas/entrega_de_reglas.py` (`al_abrir`, `NUCLEO`), `adaptadores/claude-code/hook_reglas_sesion.py` | ✅ | CP-001, CP-002 |
| CA-02 | Funcional | `core/herramientas/entrega_de_reglas.py` (`SIN_LO_ENTREGADO`) | ✅ | CP-003, CP-004 |

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
| **Veredicto** | Cumple: 4 de 4 casos |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No se usa a mano: corre al abrir la sesión, al retomarla y después de cada resumen. Llega a los proyectos con `instalar.py`. Se suspende desde Cimiento con el momento «nucleo-al-abrir».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Después de un resumen se vuelve a cero en vez de mandar todo de una vez | Todo junto no cabe en el tope; el mensaje y cada acción ya entregan lo que falta | No hace falta: está en el plan |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El catálogo de enganches (`core/comun/enganches.py`) y `.claude/settings.json`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
