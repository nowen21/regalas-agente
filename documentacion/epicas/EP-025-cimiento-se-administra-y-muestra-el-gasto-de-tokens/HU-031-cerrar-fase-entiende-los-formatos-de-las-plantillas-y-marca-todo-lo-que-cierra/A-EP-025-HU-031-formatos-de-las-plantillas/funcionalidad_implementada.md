# Funcionalidad implementada · Fase `A-EP-025-HU-031-formatos-de-las-plantillas` (módulo Herramientas de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-031-formatos-de-las-plantillas` |
| **Módulo** | Herramientas de Cimiento, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-031](../HU-031-cerrar-fase-entiende-los-formatos-de-las-plantillas-y-marca-todo-lo-que-cierra.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-031 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`cerrar_fase` lee la matriz del plan de pruebas con varios casos por fila, con enlace o sin él, y con filas de RNF; y los CA del plan de trabajo con nombre, sin él o como enlace, tomando el nombre de la HU. La segunda pasada marca además la sección 5 del plan (fecha y ☑), su Definition of Done menos el commit y, con la HU terminada, sus tareas técnicas y su Definition of Done. `reabrir_fase` desmarca lo mismo.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Lógica | `core/herramientas/fase.py` (`casos`, `plan`) | ✅ | CP-001 |
| CA-02 | Lógica | `core/herramientas/fase.py` (`_marcar_cerrada`, `reabrir`, `_poner_estado`, `_verificacion`, `_definition_of_done`) | ✅ | CP-002, CP-003 |

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

Sin cambios: `python manage.py cerrar_fase «carpeta» [--pruebas "…"] [--aplicar]` y `reabrir_fase`. Ahora sirve con los planes escritos con las plantillas.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La casilla del commit no se marca al cerrar | El commit es la estación 12, que el cierre no hace | — |

## 6. Deuda técnica y pendientes generados

Las 46 fases ya cerradas con la Definition of Done del plan sin marcar se quedan así (acuerdo 3). EP-030·HU-004 reescribe `fase.py` al pasar los documentos a la base.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-031 en la tabla de la EP-025; el README de la carpeta de la HU.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento.
