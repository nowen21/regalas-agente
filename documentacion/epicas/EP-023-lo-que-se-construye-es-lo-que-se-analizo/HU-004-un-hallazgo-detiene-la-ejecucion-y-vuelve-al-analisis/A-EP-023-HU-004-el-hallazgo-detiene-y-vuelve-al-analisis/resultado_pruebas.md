# Resultado de Pruebas · Fase `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-023-HU-004-el-hallazgo-detiene-y-vuelve-al-analisis` |
| **HU** | [HU-004](../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `d5e33a3` más los cambios de la fase, versión 47.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Media | Lectura de `02·F28` | Dice que cada documento cambia en su mismo archivo, que pasa a su versión siguiente, y que el análisis se numera sin reescribirse | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_hallazgo_detiene_la_fase.py` y `validar.py fases` | La plantilla del estado anota el hallazgo; con el análisis del hallazgo abierto, la fase con «Cumple» y la HU con «Terminada» fallan; aprobado el análisis, pasan; el repositorio no tiene fallas nuevas | Aprobado | EV-02 | Ninguno |
| CP-003 | CA-03 | Media | Lectura de `13·DOC24` | Dice que el siguiente trata solo lo que falló y sus implicaciones | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | Lectura de `02·F8` y `02·F9` | Las dos dicen que la ejecución se detiene y vuelve al análisis | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-05 | Alta | Lectura de `02/base.md`, el anexo de `02·F12` y `13·DOC12` | El plan pasa a su versión siguiente con aprobación nueva, y la fase cerrada se reabre si aparece un hallazgo | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-06 | Media | Lectura de la plantilla del plan | La sección 13 pide cuántos hallazgos salieron, con el enlace a cada análisis | Aprobado | EV-01 | Ninguno |
| CP-007 | CA-07 | Media | Lectura de `13·DOC24` y de la plantilla del análisis | Dicen que el análisis decide primero si el hallazgo es parte del plan en curso | Aprobado | EV-01 | Ninguno |
| CP-008 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio; queda el aviso de que la especificación es la HU | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá.

**Qué salió distinto de lo esperado:** `13·DOC24` quedó primero con 413 caracteres y el molde da 320 (`20·M5`); se recortó dentro de la T-04 sin perder lo que piden los criterios.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `marcas.py`, contra el commit anterior | Ninguna nueva |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| CA-05 | CP-005 | Aprobado | Sí |
| CA-06 | CP-006 | Aprobado | Sí |
| CA-07 | CP-007 | Aprobado | Sí |
| RNF-06 | CP-008 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 8 de 8 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 8 de 8 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-02.

**Justificación:** los CA-01 a CA-07 y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 4 de `test_hallazgo_detiene_la_fase.py`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Reglas y plantillas | `02·F8`, `02·F9`, `02·F28`, `13·DOC12`, `13·DOC24`, `base/02-flujo-de-trabajo/base.md`, `base/02-flujo-de-trabajo/nomenclatura-de-fases.md`, `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `plantillas/ciclo-vida-proyectos/10-estado-fase.md`, `plantillas/analisis.md` |
| EV-02 | Prueba y validador | `validadores/tests/test_hallazgo_detiene_la_fase.py`, `validadores/fases.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 8 | 0 | Primera ejecución |
