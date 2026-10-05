# Funcionalidad implementada · Fase `A-EP-025-HU-009-avisos-por-limite` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-009-avisos-por-limite` |
| **Módulo** | `proyectos/cimiento/core/enganches/`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/proyectos/`, `adaptadores/claude-code/hook_presupuesto.py` |
| **Especificación del módulo** | Los CA de la [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-009 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Con cada mensaje, el agente recibe un aviso si en el turno anterior un enganche agregó, o un archivo leído ocupó, más tokens que el límite de su proyecto. Cada exceso se avisa una vez y no detiene nada. De paso, el lector cuenta también lo que un enganche escribe como texto plano y nombra cada enganche por su título.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/enganches/presupuesto.py`, `adaptadores/claude-code/hook_presupuesto.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/lector.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/proyectos/limites.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/enganches/niveles.py` | ✅ | CP-003 |

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

Llega solo, con cada mensaje, por `hook_presupuesto.py --modo aviso`. Los límites se cambian en Cimiento, en «Proyectos», «Editar».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El mensaje que se está mandando es el último si después de él no hay respuesta del agente | El texto del mensaje no sirve para reconocerlo: Claude Code le suma el contexto del editor | No hace falta: está en `turno_anterior` |
| El texto plano de un enganche cuenta solo en `UserPromptSubmit` y `SessionStart` | En `Stop` y `PostToolUse` ese texto no llega al modelo | No hace falta: está en `lector.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: el enganche ya estaba conectado en `UserPromptSubmit`.
