# Funcionalidad implementada · Fase `A-EP-025-HU-021-desinstalar` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-021-desinstalar` |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-021](../HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-021 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`instalar.py «ruta» --desinstalar` quita los enganches de git y de Claude Code que puso la instalación, la copia del stack, la plantilla sellada, la integración continua de Cimiento, las carpetas base vacías y la fila del registro, y da de baja el proyecto en Cimiento. En el propio estándar quita además la tarea programada y la telemetría. Lo propio del proyecto se queda. `manage.py registrar --baja` desactiva, y `registrar` reactiva.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/proyectos/registro.py`, `proyectos/cimiento/core/proyectos/management/commands/registrar.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/herramientas/desinstalar.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/herramientas/instalar.py` | ✅ | CP-003 |

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

Desde la raíz del estándar: `python validadores/instalar.py «ruta» --desinstalar` dice qué quitaría; con `--aplicar`, lo quita. Se vuelve a poner con `python validadores/instalar.py «ruta» --aplicar`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se quedan las líneas del `.gitignore` y `core.longpaths` | Sin las líneas, `CLAUDE.md` y `.agente/` aparecerían para versionar; `core.longpaths` pudo ponerlo otro y no estorba | No hace falta: está en `desinstalar.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
