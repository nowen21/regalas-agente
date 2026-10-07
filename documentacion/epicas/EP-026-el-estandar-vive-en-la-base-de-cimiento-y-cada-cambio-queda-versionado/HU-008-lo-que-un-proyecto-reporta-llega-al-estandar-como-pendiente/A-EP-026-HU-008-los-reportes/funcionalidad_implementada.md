# Funcionalidad implementada · Fase `A-EP-026-HU-008-los-reportes` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-008-los-reportes` |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-008 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Un proyecto reporta al estándar con `manage.py reportar` o en «Estándar» → «Reportes». El administrador lo marca corregido con la versión que lo corrigió, o lo descarta con su motivo, y el proyecto lo sabe al abrir su sesión siguiente. Con el estándar congelado, el aviso de versión atrasada compara con la versión de la base.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Estándar» → «Reportes». Desde `proyectos/cimiento/`: `manage.py reportar --proyecto <carpeta> --titulo … [--texto …] [--regla …]`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se corrige eligiendo la versión que corrigió; el aviso de versión mira la base con el estándar congelado | La versión sube con la corrección; `VERSION` quedó quieta | S-342 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar `manage.py migrate estandar` (hecho en esta máquina el 2026-10-06).
