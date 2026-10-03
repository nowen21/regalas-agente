# Funcionalidad implementada · Fase `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis` (módulo `base/`, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis` |
| **Módulo** | `base/`, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Los CA-01 a CA-07 de la [HU-004](../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-004 (CA-01 a CA-07) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 47.0.0 |
| **Commit** | `cfcc89d` |

## 1. Qué se implementó, resumen

Un hallazgo al ejecutar un plan lo detiene y vuelve al análisis; el plan pasa a su versión siguiente con aprobación nueva, y la fase cerrada se reabre si el hallazgo es sobre lo que construyó. La fase y su HU no pueden decir que cerraron mientras el análisis del hallazgo siga sin aprobar, y el plan dice cuántos hallazgos salieron.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01, CA-03, CA-04, CA-05 y CA-07: las reglas | Regla | `02·F8`, `02·F9`, `02·F28`, `13·DOC12`, `13·DOC24`, `base/02-flujo-de-trabajo/base.md`, `base/02-flujo-de-trabajo/nomenclatura-de-fases.md` | ✅ | CP-001, CP-003 a CP-005, CP-007 |
| CA-02: un hallazgo detiene y nada cierra | Plantilla y validador | `plantillas/ciclo-vida-proyectos/10-estado-fase.md`, `validadores/fases.py` | ✅ | CP-002 |
| CA-06: el plan registra sus hallazgos | Plantilla | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | ✅ | CP-006 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 9 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): Ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase, que nombra la sección 3.5 de su plan de pruebas.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Cuando aparece un hallazgo al ejecutar, se detiene el trabajo, se abre el análisis siguiente del pendiente y el estado de la fase anota el motivo. `python validadores/validar.py fases` falla si la fase o la HU dicen que cerraron con ese análisis sin aprobar.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El anexo de `02·F12` se ajustó con una línea fechada | El usuario lo aprobó en el análisis 1 del pendiente 103 (punto 18); el texto literal anterior quedó como estaba | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna. Salió el hallazgo H-13 (los planes se escribían sin leer lo que el análisis decidió), anotado en el resumen de la sesión.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 47.0.0 con el instalador.
