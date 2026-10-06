# Funcionalidad implementada · Fase `A-EP-025-HU-017-guiones-repetidos` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-017-guiones-repetidos` |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-017](../HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-017 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al escribir un `.py` en `historico-chat/scripts/`, el freno mira su texto: si hace algo que Cimiento ya hace (cerrar o reabrir una fase, separar los cambios por sesión, el andamio, cerrar o reabrir un pendiente, instalar o desinstalar, leer el gasto), lo detiene y dice qué orden usar; si se parece a un guion anterior, avisa que la tarea se repite y deja escribir.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/enganches/guiones.py`, `proyectos/cimiento/core/enganches/freno.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/enganches/guiones.py`, `proyectos/cimiento/core/enganches/freno.py` | ✅ | CP-002 |

**Faltantes / diferimientos:** los guiones que se crean por la consola, cuyo texto el freno no ve.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No hay que hacer nada: el freno lo aplica al escribir un guion. Si el guion es legítimo y se detiene, se suspende `04·S18` en Cimiento, en «Suspensiones».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se reconoce lo que el guion toca, no su nombre | El nombre lo elige el agente | No hace falta: está en `guiones.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
