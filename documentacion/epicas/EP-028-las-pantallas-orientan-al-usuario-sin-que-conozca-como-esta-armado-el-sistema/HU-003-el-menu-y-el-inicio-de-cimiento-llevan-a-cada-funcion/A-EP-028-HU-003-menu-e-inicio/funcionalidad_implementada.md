# Funcionalidad implementada · Fase `A-EP-028-HU-003-menu-e-inicio` (módulo Inicio de Cimiento: `templates/base.html` y `core/inicio/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-003-menu-e-inicio` |
| **Módulo** | Inicio de Cimiento: `templates/base.html` y `core/inicio/` |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El menú de Cimiento se arma por tareas con los submenús de Tabler (Proyectos, Estándar, Historia), marca la pantalla en que se está y alcanza todas las pantallas que no son el detalle de un registro. El menú y el inicio cuentan las propuestas y los reportes que esperan una decisión; el inicio lleva a cada uno y a las tareas principales, y dice cuando no hay nada pendiente.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El menú de la izquierda, en toda pantalla, y el inicio.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Los contadores salen de un procesador de contexto | Están en toda pantalla y conviene una sola fuente; se descartó calcularlos en cada vista | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La sección «Inicio» del manual de ayuda.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
