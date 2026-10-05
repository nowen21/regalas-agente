# Funcionalidad implementada · Fase `A-EP-025-HU-006-lectura-de-los-jsonl` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-006-lectura-de-los-jsonl` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py leer_consumo` lee los registros de Claude Code de cada proyecto activo y guarda en la base de Cimiento cada llamada con sus tokens, cada enganche con su tamaño y cada archivo leído. Repetirla no duplica. La instalación la programa una vez al día. `hook_presupuesto.py` cuenta cada llamada una sola vez: antes la contaba unas tres.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/lector.py` | ✅ | CP-003 |
| CA-04 | Programa | `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python manage.py leer_consumo`, o con `--proyecto «nombre»` para uno solo. En Windows la corre la tarea programada «Cimiento leer consumo».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Una llamada se cuenta una vez por su `message.id` | Claude Code parte una llamada en varias líneas con el mismo `usage` (H-5 del resumen del 2026-10-04, sesión 3) | No hace falta: está en el lector y en su prueba |
| Los tokens de un enganche o de un archivo se estiman con 3,5 caracteres por token | El registro no trae los tokens de cada pieza; la constante vive en un solo lugar | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

La instalación del estándar corre `preparar_base` y programa la lectura.
