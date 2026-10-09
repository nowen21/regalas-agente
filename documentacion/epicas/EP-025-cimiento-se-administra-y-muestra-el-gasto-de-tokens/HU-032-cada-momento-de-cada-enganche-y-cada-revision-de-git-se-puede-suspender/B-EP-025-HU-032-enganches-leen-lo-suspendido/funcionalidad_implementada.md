# Funcionalidad implementada · Fase `B-EP-025-HU-032-enganches-leen-lo-suspendido` (módulo Los enganches de Cimiento: `proyectos/cimiento/core/enganches/` y sus adaptadores en `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-032-enganches-leen-lo-suspendido` |
| **Módulo** | Los enganches de Cimiento: `proyectos/cimiento/core/enganches/` y sus adaptadores en `adaptadores/claude-code/` |
| **Especificación del módulo** | Los CA de la [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-032 (CA-02) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al arrancar, cada uno de los 18 adaptadores de Claude Code llama a `salir_si_esta_suspendido(__file__)`: lee la entrada, saca su momento de `(evento, guion)` y, si está suspendido en Cimiento, sale con 0 sin hacer nada; si no, le devuelve la entrada intacta al programa. En cada mensaje, el primer enganche que gana el turno (un archivo creado con `O_EXCL` en `.agente/`) consulta la base y deja la lista de la sesión; los demás esperan hasta 2 s y la leen. Los eventos sin mensaje propio usan la lista del mensaje en curso. Sin base, o si algo falla, el enganche corre como siempre. El freno solo se apaga entero con la suspensión «freno».

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-02 | Lógica | `core/enganches/suspendidos.py`, `core/enganches/niveles.py`, `adaptadores/claude-code/hook_*.py` | ✅ | CP-003, CP-004, CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios para quien trabaja: lo que se suspende en Cimiento → Proyectos → Suspensiones deja de correr desde el mensaje siguiente.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Revisar al comienzo de `main()` con la entrada devuelta intacta | Cada adaptador lee la entrada a su manera y solo se puede leer una vez; se descartó cambiar cómo la lee cada uno | — |

## 6. Deuda técnica y pendientes generados

Si dos sesiones trabajan en el mismo proyecto, cada una tiene su lista: `.agente/suspendidos.«sesión».json`. Las de más de un día se borran solas.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-032 en la tabla de la EP-025.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento; el instalador ya instala los adaptadores.
