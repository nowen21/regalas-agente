# Funcionalidad implementada · Fase `C-EP-025-HU-032-revisiones-de-git` (módulo Las revisiones de git: `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-025-HU-032-revisiones-de-git` |
| **Módulo** | Las revisiones de git: `proyectos/cimiento/core/herramientas/`, con el adaptador de `post-commit` y lo que queda de `NO_SE_SUSPENDEN` |
| **Especificación del módulo** | Los CA de la [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-032 (CA-03) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Antes de correr una revisión de git, `validar.py` busca su nombre en `REVISIONES_GIT` y, si está suspendida en Cimiento, sale con 0 y escribe hasta cuándo y por qué. La primera revisión de cada guardado consulta la base y les deja la lista a las demás (la de la sesión «git», por minuto). `hook_estacion.py` (post-commit) hace lo mismo. `NO_SE_SUSPENDEN` ya no existe.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-03 | Lógica | `core/herramientas/validar.py` (`revision_git_suspendida`), `adaptadores/claude-code/hook_estacion.py` | ✅ | CP-006, CP-007 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `.gitignore` y `core/consumo/vigilante.py`, por el análisis 2 del pendiente 149, de una y sin fase.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En Cimiento → Proyectos → Suspensiones, por ejemplo `git-marcas`: el siguiente `git commit` no se detiene por las marcas y lo dice.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La revisión se reconoce por la orden de `validar.py` | Se descartó pasar el nombre desde cada plantilla de git: obligaba a reinstalar los `.githooks` de cada proyecto | — |

## 6. Deuda técnica y pendientes generados

Si el agente corre a mano una revisión suspendida, también sale suspendida: lo dice con su motivo.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-032 en la tabla de la EP-025.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento.
