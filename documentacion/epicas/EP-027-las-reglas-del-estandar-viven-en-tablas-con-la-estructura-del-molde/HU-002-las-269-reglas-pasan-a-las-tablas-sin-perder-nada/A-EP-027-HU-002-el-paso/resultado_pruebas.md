# Resultado de Pruebas · Fase `A-EP-027-HU-002-el-paso`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-027-HU-002-el-paso` |
| **HU** | [HU-002](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django, con el estándar importado de `base/`, y la base viva; versión 57.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `TodasQuedanEnLasTablas` (3 pruebas) y `ElRegistroDeValidables` | Una fila por regla; F1 con su capítulo, sus tareas en orden, su ejemplo y su sello; F0 con sus tres dependencias unidas; G2 «sí» con `commits.py`, F2 «falta el programa», C1 «no» | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `NadaSePierde` (2 pruebas) | Ningún renglón nuevo; los que faltan son exactamente los de las notas, y la de C1 está en su historia con fecha 2026-08-22 | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `PasarDosVecesNoDuplica` | Las mismas filas y notas; ningún documento cambia | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** nada en la fase. La regresión de `core.enganches` tiene una prueba en rojo que no es de esta fase (ver §4).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.estandar.tests_pasar_reglas --noinput` | Ran 7 tests in 69.562s, OK |
| 2 | La copia antes de tocar la base viva (`00·N7`) | `manage.py copiar_base` y `manage.py probar_copia` | `cimiento-2026-10-07.sql.gz` se restaura: 31 tablas, 158.382 filas |
| 3 | El paso en la base viva | `manage.py migrate estandar` y `manage.py pasar_reglas` | 270 reglas; 63 documentos armados de nuevo; versión 57.4.0 (MENOR) |
| 4 | Lo que recibe el agente | Los documentos de `base/reglas-por-tarea/` que cambió esa versión | Ninguno |
| 5 | Las tablas en la base viva | Conteo | 156 notas en la historia; 91 dependencias, todas con destino; 10 tareas; 25 capítulos; «validable»: 165 no, 57 sí, 38 falta el programa, 10 sin declarar (C28, F4.1 a F4.5, G8, DOC8, I7, M16) |

## 4. Defectos encontrados

Ninguno de esta fase. La regresión `manage.py test core.estandar core.enganches` corre 570 pruebas con una falla: `test_la_opt_in_apagada_no_autoriza_y_la_encendida_si`, que está en rojo desde `041984a` (EP-026·HU-009). Va al [pendiente 140](../../../../../historico-chat/resumenes/2026-10-07/pendientes/140-la-regla-opt-in-de-un-capitulo-que-no-es-opt-in-no-se-apaga/pendiente.md).

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado, el paso en la base viva dejó las 270 reglas y no cambió lo que recibe el agente.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar.tests_pasar_reglas`: 7 OK |
| EV-02 | El paso en la base viva | §3, filas 2 a 5 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 3 | 0 | Primera ejecución |
