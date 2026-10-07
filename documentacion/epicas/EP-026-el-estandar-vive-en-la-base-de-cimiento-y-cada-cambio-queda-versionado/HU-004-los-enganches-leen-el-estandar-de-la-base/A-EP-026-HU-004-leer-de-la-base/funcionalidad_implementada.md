# Funcionalidad implementada · Fase `A-EP-026-HU-004-leer-de-la-base` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-004-leer-de-la-base` |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-004](../HU-004-los-enganches-leen-el-estandar-de-la-base.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-004 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.2.1 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Las reglas que llegan con cada mensaje, lo que el freno deja escribir y el arranque de sesión salen de la base de Cimiento, no de `base/`. Si la base no responde, el enganche de reglas lo dice y el freno no deja modificar. `sincronizar_estandar` pone la base al día con lo guardado en git, en una versión del estándar.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Funciona solo. A mano: `manage.py sincronizar_estandar [--obliga si|no] [--agrega si|no] [--motivo …]` desde `proyectos/cimiento/`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lector con cara de `Archivos` y sincronización con git, no con la carpeta | Los lectores no se reescriben; la carpeta puede tener cambios sin aprobar de otra sesión | S-336 |

## 6. Deuda técnica y pendientes generados

Mientras `base/` no esté congelado (HU-006), un cambio guardado en git no rige hasta `sincronizar_estandar`.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Nada más: queda encendido al estar el código. Correr `sincronizar_estandar` cuando haya cambios de `base/` guardados en git.
