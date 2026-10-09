# Funcionalidad implementada · Fase `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto` (módulo Las pantallas de Cimiento: la pantalla del gasto y la ayuda)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto` |
| **Módulo** | Las pantallas de Cimiento: la pantalla del gasto (`core/consumo/templates/consumo/`) y la ayuda (`core/ayuda/`) |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-cimiento-usa-adminlte-4.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 (CA-04, CA-05) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

- **Las pestañas.** El Resumen tarda cerca de 1,5 s. Si se pulsaba otra pestaña mientras cargaba, o justo después de un mensaje nuevo (que vuelve a pedir lo que se ve), el Resumen llegaba de último y tapaba la pestaña escogida: quedaba marcada una y se veía otra. Ahora la pestaña que se pulsa cancela lo que estaba cargando (`hx-sync`), y el refresco de una pestaña no se mete si hay otra cargando. Mientras carga, un indicador gira junto a las pestañas. Los botones de agrupar de «Dónde se gasta» cargan dentro de la caja (`innerHTML`): antes la reemplazaban entera y las pestañas dejaban de cargar (`htmx:targetError`, reportado por el usuario).
- **La ayuda.** Cada cifra de la franja, cada título y cada columna con nombre de las cinco pestañas tienen su «?», con 34 textos nuevos en `core/ayuda/textos.py`. `ayuda.js` activa los globos de lo que llega por htmx y cierra los de lo que se va.
- **Las tablas.** Todas quedaron dentro de `table-responsive`; las de Contexto, a ancho completo; y la primera columna, que no tenía nombre, lo tiene.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04 · Las pestañas del gasto funcionan | CA | `core/consumo/templates/consumo/tablero.html` y las cinco pestañas | Hecho | CP-001 |
| CA-05 · Las pestañas del gasto tienen su ayuda | CA | Las cinco pestañas, `_franja.html`, `core/ayuda/textos.py`, `core/ayuda/static/ayuda/ayuda.js` | Hecho | CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `templates/base.html` estaba declarado por si la falla venía del orden de los scripts, y no hizo falta tocarlo.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Menú → Gasto de tokens. Un «?» nuevo en una parte que llega por htmx se pone con `{% ayuda_campo "clave" %}` y su texto en `CAMPOS`: el globo se activa solo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La pestaña pulsada reemplaza (`replace`) lo que carga; el refresco se descarta (`drop`) si hay algo cargando | Lo último que pide el usuario manda; se descartó dejar que gane el que llegue de último | Ninguna |
| La ayuda de las pestañas usa el mismo «?» de los formularios | Es el componente de la guía para explicar una parte de la pantalla; se descartó un texto fijo bajo cada tabla | Ninguna |

## 6. Deuda técnica y pendientes generados

El Resumen sigue tardando cerca de 1,5 s y se vuelve a pedir con cada mensaje nuevo. Ya no tapa otra pestaña, pero es lento.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Recargar la pantalla.
