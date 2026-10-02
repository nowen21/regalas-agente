# Funcionalidad implementada · Fase `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis` (módulo cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis` |
| **Módulo** | Cuerpo de reglas (`base/`) y `historico-chat/memory/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-05 de la [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-005 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 41.0.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

El agente ya no tiene una regla que le permita agregar lo que nadie pidió. `01·C30` dice que lo pedido es el criterio de aceptación más lo que exigen las reglas del estándar, y que lo que el oficio suele incluir se pregunta en el análisis. `01·C14` quedó derogada, y las tres reglas que se apoyaban en ella quedaron apoyadas en reglas vigentes. Los dos recuerdos que permitían seguir fuera del plan quedaron limitados al plan aprobado.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01, RN-03, RN-05: nada fuera de lo pedido; lo del oficio se pregunta | Regla | `base/01-conducta.md`, `C30` | ✅ | CP-001, CP-002 |
| RN-02: las reglas se complementan | Regla | `C30`, `F19`, `ID1`, `C25`, `C15` | ✅ | CP-001, CP-003, CP-006 |
| RN-04: corregir por cuenta propia solo dentro del plan | Documentación | `historico-chat/memory/` | ✅ | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `C30` | ✅ hecha | `base/01-conducta.md` | CP-001, CP-002 |
| T-02 | `C14` derogada | ✅ hecha | `base/01-conducta.md` | CP-002 |
| T-03 | `C25` debajo de `C4` | ✅ hecha | `base/01-conducta.md` | CP-003 |
| T-04 | Recuerdo «Corregir el defecto detectado» | ✅ hecha | `historico-chat/memory/` | CP-005 |
| T-05 | Recuerdo «Una instrucción se cumple entera» | ✅ hecha | `historico-chat/memory/` | CP-005 |
| T-06 | Reglas por tarea y registro | ✅ hecha | `base/mapa-de-tareas.md`, `base/reglas-por-tarea/`, `validadores/reglas-validables.md` | CP-004 |
| T-07 | Versión 41.0.0 | ✅ hecha | `VERSION`, `CHANGELOG.md` | CP-004 |
| T-08 | Ejemplo de `F19` | ✅ hecha | `base/02-flujo-de-trabajo/reglas/F19-…` | CP-001 |
| T-09 | `C15` extiende a `C30` | ✅ hecha | `base/01-conducta.md` | CP-003 |
| T-10 | `ID1` dentro de lo pedido | ✅ hecha | `base/00-identidad-y-rol/reglas/ID1-…` | CP-006 |

**Correspondencia con el plan:** 10 tareas en el plan, 10 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `historico-chat/scripts/2026-10-02/hu005_capitulo_01.py`, el guion que aplicó T-01, T-02, T-03 y T-09 (`04·S18`). Los cambios de `validadores/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py` y `validadores/tests/test_analisis_en_curso.py` no son de esta fase: son la corrección del H-6, pedida aparte con «Corrija», y entran en el mismo commit y en la misma versión.

**Esfuerzo real contra estimado:** no se midió. El plan estimaba 4,1 horas.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas: `validar.py estandar`, `metareglas`, `checklist`, `tareas`, `version`, `versiones` y `flujo`; `test_version_derogaciones` y `test_analisis_en_curso`; la medición de marcas.
- Verificaciones manuales: ninguna regla cita el ancla vieja de `C14`.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`C30` llega al agente con las tareas escribir-documento y cambiar-codigo. Cuando el agente crea que algo «convendría» y ninguna regla lo exige, lo pregunta en el análisis.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo pedido incluye lo que exigen las reglas | Sin eso, `C30` prohibiría cumplir `04·S1` (análisis 6, conclusión 5) | Por escribir |
| `C25` extiende a `C4` y no a `C30` | `C25` dice qué no decide el agente, que es el asunto de `C4` | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `base/mapa-de-tareas.md` y `base/reglas-por-tarea/`.
- [x] Índice de `historico-chat/memory/`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto adopta la 41.0.0 con el instalador (`02·F22`).
