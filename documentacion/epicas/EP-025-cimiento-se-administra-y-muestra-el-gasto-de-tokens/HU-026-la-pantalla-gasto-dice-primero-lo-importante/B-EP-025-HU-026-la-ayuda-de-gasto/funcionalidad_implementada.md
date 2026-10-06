# Funcionalidad implementada · Fase `B-EP-025-HU-026-la-ayuda-de-gasto` (módulo Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-026-la-ayuda-de-gasto` |
| **Módulo** | Cimiento, `core/ayuda/` |
| **Especificación del módulo** | Los CA de la [HU-026](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-026 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La ayuda de «Gasto» describe la franja, las cinco pestañas y el botón ↻, sin «cada 10 segundos». La lista de rutas que no son pantalla cambia `consumo:datos` por `consumo:franja` y `consumo:pestana`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno; `secciones.py` se sumó a la tabla 2.1 antes de tocarlo.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El botón «?» de la pantalla «Gasto» y el manual de Cimiento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Ninguna | No hubo decisiones nuevas | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
