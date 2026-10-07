# Funcionalidad implementada · Fase `A-EP-028-HU-006-tablas-avanzadas` (módulo Tablas de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-006-tablas-avanzadas` |
| **Módulo** | Tablas de Cimiento |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Las siete listas de registros de Cimiento usan la tabla avanzada de Tabler con List.js, que ya traía la plantilla: se ordenan pulsando el título de la columna y se filtran debajo; cinco se paginan escogiendo 10, 20, 50 o 100 filas, con un pie común (`templates/includes/tabla_pie.html`), y las dos que ya paginaba la base (historia y versiones) ordenan y filtran lo que se ve. El código va una sola vez, en `static/tablas.js`. Sin datos, cada tabla lo dice con el bloque vacío de Tabler.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** quitar columnas técnicas queda en la EP-027·HU-005

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

En cada lista: pulsar el título de una columna ordena; escribir o escoger debajo filtra; el pie escoge cuántas filas ver.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Historia y versiones conservan la paginación de la base | Tienen miles de filas; se descartó cargarlas enteras para List.js | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
