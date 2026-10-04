# Funcionalidad implementada · Fase `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente` (módulo `validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente` |
| **Módulo** | `validadores/` |
| **Especificación del módulo** | El CA-09 de la [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 (CA-09) |
| **Fecha de cierre** | 2026-10-03 |
| **Versión del estándar al cerrar** | 52.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Apruebo el análisis» no pone la marca si el hallazgo del análisis, desde el número 2, falta en «De dónde sale» de su pendiente, o si el título de «Hallazgo» no trae su número. El aviso dice cuál falta.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-09: la aprobación se niega y dice qué falta | Programa | `validadores/analisis_en_curso.py` | ✅ | CP-001, CP-002 |
| CA-09: la plantilla pide el pendiente en su versión siguiente | Plantilla | `plantillas/analisis.md`, ya lo pedía | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno de la fase. `validadores/tests/test_analisis_en_curso.py` se tocó bajo la fila 4 del análisis 14 del pendiente 103.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Antes de «Apruebo el análisis», pasar el pendiente a su versión siguiente con el hallazgo del análisis en «De dónde sale».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El hallazgo se reconoce por su número en el título de «Hallazgo» | El pendiente cita sus hallazgos por número | No hace falta: está en el plan |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 52.0.0.
