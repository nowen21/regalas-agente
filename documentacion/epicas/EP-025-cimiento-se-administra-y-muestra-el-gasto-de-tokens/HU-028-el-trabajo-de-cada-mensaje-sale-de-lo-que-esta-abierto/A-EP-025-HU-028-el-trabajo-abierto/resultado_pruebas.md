# Resultado de Pruebas · Fase `A-EP-025-HU-028-el-trabajo-abierto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-028-el-trabajo-abierto` |
| **HU** | [HU-028](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y la base real de Cimiento; versión 58.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `tests_trabajo_abierto`: `test_el_analisis_prendido_manda`, `test_el_aviso_apagado_no_da_trabajo`, `test_el_aviso_dice_el_analisis_prendido` | El análisis prendido gana aunque el turno toque una fase; apagado o en pausa, el aviso no da trabajo | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_reconoce_las_fases_de_cualquier_letra`, `test_la_orden_de_consola_dice_la_fase` | Las fases `B-` y `C-` se reconocen, también dentro de una orden de consola | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `test_el_mensaje_sin_rastro_sigue_la_conversacion`, `test_otra_conversacion_no_hereda` | El «apruebo» toma el trabajo del mensaje anterior y lo cambia cuando su turno toca otra fase; otra conversación no hereda | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | `test_recalcula_desde_las_lineas_y_da_lo_mismo_la_segunda_vez` y la base real | En la base real, los mensajes de 7 días sin trabajo bajaron de 1.839 a 597 de 1.983 | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada. `tests_segunda_tanda` no hubo que tocarlo: sus mensajes tienen la misma hora, así que ninguno hereda.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.consumo core.ayuda --noinput` | 101 pruebas, OK |
| 2 | La base real | `manage.py migrate consumo` y `manage.py recalcular_trabajo` | 3.238 mensajes de 33 archivos recalculados; sin trabajo, de 3.487 a 1.480 de 3.667 |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-001 | Aprobado: el aviso no cambió | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro casos pasan y, en la base real, los mensajes sin trabajo de la última semana pasaron del 93 % al 30 %.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_trabajo_abierto.py` |
| EV-02 | Antes y después en la base real | `historico-chat/scripts/2026-10-08/salida_recalcular_trabajo.txt` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 4 | 0 | Primera ejecución |
