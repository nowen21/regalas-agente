# Funcionalidad implementada · Fase `A-EP-026-HU-003-la-importacion` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-003-la-importacion` |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-el-estandar-55-1-0-entra-a-la-base.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.1.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Todo `base/` está en la base de Cimiento, un documento por archivo con su ruta y su texto exacto, y la memoria de cada proyecto registrado, un recuerdo por archivo. Es la versión 56.1.0 del estándar en la base. Lo que se guarde en ellos tiene historia y sube la versión que le toca.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Ya corrió en esta máquina: `manage.py importar_estandar`, una sola vez. Los documentos se leen desde la base con la HU-004 y se editan con la HU-005.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El estándar entra como documentos enteros con su ruta, no partido en columnas | Los lectores de hoy los sirven sin reescribirse; partirlo dejaría dos copias | S-335 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar `manage.py migrate estandar` y correr `manage.py importar_estandar` una vez (hecho en esta máquina el 2026-10-06).
