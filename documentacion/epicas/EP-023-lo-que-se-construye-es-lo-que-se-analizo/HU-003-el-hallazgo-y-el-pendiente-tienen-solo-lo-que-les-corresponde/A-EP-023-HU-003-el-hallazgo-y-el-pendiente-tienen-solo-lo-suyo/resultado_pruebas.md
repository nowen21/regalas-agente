# Resultado de Pruebas · Fase `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo` |
| **HU** | [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0, con la sección 3.5 corregida |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `79356eb` más los cambios de la fase, versión 45.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 9 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Media | Lectura de la tabla de `20·M13` y del glosario; el andamio con HU y sin ella | La regla lo dice; con HU nace en `pendientes/` de la HU, sin ella en `pendientes/` del resumen del día | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Media | Lectura de las cuatro plantillas | Las del pendiente traen «De dónde sale», «El problema» y «Por qué importa»; el hallazgo trae «Qué pasó», «Por qué importa» y «Pendiente» | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | Pruebas de la fase y `validar.py pendientes` | El pendiente y el hallazgo con solo sus campos pasan; `pendientes/` del repositorio pasa, también el 103 viejo; el resumen viejo lee su estado escrito | Aprobado | EV-02, EV-03 | Ninguno |
| CP-004 | CA-04 | Alta | Pruebas de la fase | Sin análisis aprobado, abierto; con su HU sin terminar, abierto; con su HU terminada, cerrado, y `pendiente.md` no cambió | Aprobado | EV-02 | Ninguno |
| CP-005 | CA-05 | Alta | Lectura de `13·DOC22` y de la plantilla; pruebas de la fase | Sin pendiente, «abierto, sin pendiente»; con pendiente abierto, «abierto, anotado», y se retoma por su último análisis; con el plan cumplido, «resuelto» | Aprobado | EV-01, EV-02 | Ninguno |
| CP-006 | CA-06 | Media | Búsqueda de «Proyecto de origen»; pruebas de la fase | Ninguna plantilla ni `02·F24` lo pide; el seguimiento toma el estado de su padre | Aprobado | EV-01, EV-02 | Ninguno |
| CP-007 | CA-07 | Alta | Lectura de `02·F13` y `20·M13`; `test_aviso_de_vuelta.py`; `git status` sobre `pendientes/` | Las reglas lo dicen; el proyecto nuevo no tiene `pendientes/` y la validación no falla; en `pendientes/` solo cambió la ruta del enlace al análisis 2 del 103 viejo, que la T-16 corrige | Aprobado | EV-01, EV-02, EV-03 | Ninguno |
| CP-008 | CA-08 | Alta | Pruebas de la fase; `validar.py fases`, `estandar`, `origen` y `pendientes --indice` | `fases` ya no falla por el 103 ni por `HU-036/pendientes`; ningún enlace roto; `origen` lee el 103 en su lugar nuevo; el próximo número cuenta todas las carpetas; el índice queda en `documentacion/pendientes.md` con 108 pendientes | Aprobado | EV-02, EV-03, EV-04 | Ninguno |
| CP-009 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio; queda el aviso de que la especificación es la HU | Aprobado | EV-03 | Ninguno |

**Correspondencia con el plan:** 9 casos en el plan, 9 acá.

**Qué salió distinto de lo esperado:**

- `flujo.py` también trataba `EP-023/pendientes/` como una HU. Se ajustó igual que `fases.py`, dentro de la T-11.
- Las pruebas que fijaban las reglas viejas (el instalador crea `pendientes/`, el pendiente abierto trae su historia, el andamio escribe en `pendientes/README.md`) pasaron a fijar las nuevas.
- `pendientes.py` sigue revisando «Proyecto de origen» en los pendientes viejos que lo traen, porque `cerrar.py` lo usa para el aviso de vuelta de esos pendientes. Ningún pendiente nuevo lo trae ni lo necesita.

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
| CA-08 | CP-008 | Aprobado | Sí |
| RNF-06 | CP-009 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 9 de 9 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 9 de 9 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 0 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-02.

**Justificación:** los CA-01 a CA-08 y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 58, de las cuales 17 son nuevas.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Plantillas y reglas | `plantillas/pendiente.md`, `plantillas/pendiente-de-seguimiento.md`, `plantillas/pendiente-reportado.md`, `plantillas/sesion.md`, `13·DOC22`, `02·F24`, `02·F13`, `base/20-meta-reglas/base.md` |
| EV-02 | Pruebas de la fase | `validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py` (17), `test_pendientes_historia.py`, `test_el_andamio_levanta_la_historia_y_el_pendiente.py`, `test_aviso_de_vuelta.py` |
| EV-03 | Salida de `validar.py estandar`, `origen`, `analisis`, `fases`, `pendientes` y `flujo` | Transcripción de la sesión del 2026-10-01 |
| EV-04 | El índice | `documentacion/pendientes.md` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 9 | 0 | Primera ejecución |
