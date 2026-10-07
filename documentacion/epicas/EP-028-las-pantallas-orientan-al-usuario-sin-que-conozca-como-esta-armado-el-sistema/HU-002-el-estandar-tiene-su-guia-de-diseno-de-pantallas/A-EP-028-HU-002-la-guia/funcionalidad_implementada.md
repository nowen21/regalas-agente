# Funcionalidad implementada · Fase `A-EP-028-HU-002-la-guia` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-002-la-guia` |
| **Módulo** | Estándar en la base, capítulo `17` |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-002 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El estándar tiene su guía de diseño de pantallas, `base/17-guia-de-pantallas.md`, con las 14 secciones del encargo. Cada sección dice qué se exige y cómo se hace con Tabler, la plantilla de Cimiento; abre con la regla de oro de buscar primero en la plantilla instalada. El capítulo 17 la enlaza.

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

Se lee en el menú «Estándar» o con `manage.py ver_estandar base/17-guia-de-pantallas.md`, antes de crear o arreglar una pantalla.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La guía vive junto al capítulo 17 | Desarrolla el cómo de sus reglas, como `estructura-regla.md` lo hace con la `M5`; se descartó un capítulo nuevo | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El capítulo 17 enlaza la guía.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: la guía ya quedó en la base.
