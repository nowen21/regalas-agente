# Funcionalidad implementada · Fase `A-EP-029-HU-001-ajustes-y-estado-de-la-revision` (módulo Pruebas de Cimiento: `core/pruebas/` y los ajustes de `core/proyectos/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-001-ajustes-y-estado-de-la-revision` |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/` y los ajustes de `core/proyectos/` |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1, con la migración que agregó el análisis 2 del pendiente 141 |
| **HU / CA cubiertas** | HU-001 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La configuración de cada proyecto tiene dos opciones nuevas: «Revisión de pruebas: qué tan estricto ser» (solo avisar, no dejar guardar, o nada; de fábrica, solo avisar) y «Revisión de pruebas: cada cuántos días» (de fábrica, 7). Las dos van en las tres capas de siempre y salen, con su «?», en «Proyectos» → «Editar» y en «Configuración». La app nueva `core/pruebas/` guarda si cada proyecto tiene la parte que revisa y cada revisión: fecha, herramienta, porcentaje, archivos sin pruebas y resultado del navegador.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Ajustes | `core/proyectos/ajustes.py`, `core/proyectos/migrations/0007_ajustes_de_revision.py` | Hecho | CP-001, CP-002 |
| CA-02 | Ayuda | `core/ayuda/textos.py` | Hecho | CP-003 |
| CA-03 | Modelo | `core/pruebas/models.py`, `core/pruebas/migrations/0001_inicial.py` | Hecho | CP-004, CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. La migración `0007_ajustes_de_revision.py` faltaba en el plan (H-2 del 2026-10-07) y la agregó el análisis 2 del pendiente 141 antes de escribirla.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En «Proyectos» → «Editar», o en «Configuración» para el valor común: las dos opciones de «Revisión de pruebas». Desde el código, `Revision.ultima(proyecto)` y `PruebasDelProyecto.de(proyecto)`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las opciones se guardan con las palabras que ve el usuario | El formulario las muestra tal cual (acuerdo 8); se descartaron códigos internos | Ninguna |
| App nueva `core/pruebas/` | La revisión crece en las HU-002, 003 y 005; se descartó meterla en `core/proyectos/` | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`INSTALLED_APPS` en `config/settings/base.py`. Cimiento no tiene un catálogo de módulos que nombre sus apps.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate` en la máquina de Cimiento.
