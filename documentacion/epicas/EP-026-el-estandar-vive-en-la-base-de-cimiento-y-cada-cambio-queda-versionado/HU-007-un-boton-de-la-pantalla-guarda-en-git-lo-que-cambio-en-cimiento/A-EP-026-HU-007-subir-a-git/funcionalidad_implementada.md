# Funcionalidad implementada · Fase `A-EP-026-HU-007-subir-a-git` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-007-subir-a-git` |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

En «Estándar» → «Subir a git» se ve lo que cambió cada sesión, lo compartido y lo sin sesión. El administrador escribe el asunto, la idea del usuario y lo que hizo el agente, y el botón hace el commit solo de esa sesión y, si se marca, lo sube. Si el commit falla, nada queda preparado y la pantalla muestra el error.

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

«Estándar» → «Subir a git» (`/estandar/git/`).

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Commit de una sola sesión, con tres campos para el mensaje, y soltar si falla | Respeta la convención y no deja nada preparado para el commit siguiente | S-341 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Nada: usa la cuenta de git del computador.
