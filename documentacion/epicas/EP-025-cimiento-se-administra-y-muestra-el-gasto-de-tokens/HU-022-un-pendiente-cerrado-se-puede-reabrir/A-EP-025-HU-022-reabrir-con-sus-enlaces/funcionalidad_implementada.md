# Funcionalidad implementada · Fase `A-EP-025-HU-022-reabrir-con-sus-enlaces` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-022-reabrir-con-sus-enlaces` |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-022](../HU-022-un-pendiente-cerrado-se-puede-reabrir.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-022 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`cerrar.py reabrir` devuelve un pendiente de `hecho/` a `pendientes/`, arrastra sus citas en los dos sentidos, deja su fila del índice abierta y anota en el pendiente cuándo y por qué se reabrió.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/herramientas/cerrar.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/herramientas/cerrar.py` | ✅ | CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Desde la raíz del estándar: `python validadores/cerrar.py reabrir 53 --motivo "volvió a fallar" --fecha 2026-10-05` dice qué haría; con `--aplicar`, lo hace.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El aviso de vuelta del cierre no se deshace | Ya pudo leerse en el otro proyecto; la orden lo dice | No hace falta: está en `cerrar.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
