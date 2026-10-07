# Funcionalidad implementada · Fase `A-EP-026-HU-010-la-copia-diaria` (módulo Historia de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-010-la-copia-diaria` |
| **Módulo** | Historia de Cimiento, `proyectos/cimiento/core/historia/` |
| **Especificación del módulo** | Los CA de la [HU-010](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-010 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.1.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cada día que se abre una sesión, si falta la copia de hoy, el inicio de sesión la lanza en segundo plano: `cimiento-AAAA-MM-DD.sql.gz` en `C:\Ing. Jose\ia\cimiento-copias`, sin las sesiones del navegador, y quedan las últimas 7. Si la última falló, el inicio de sesión lo avisa. `probar_copia` comprueba que una copia se restaura en una base aparte.

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

Sola, al abrir sesión. A mano: `manage.py copiar_base` y `manage.py probar_copia [archivo]` desde `proyectos/cimiento/`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La copia la escribe Python comprimida y la lanza el inicio de sesión | Sin `mysqldump` ni tarea programada de Windows; sin comprimir pesaba 437 MB | S-333 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Nada: la carpeta de copias la crea la primera copia.
