# Resultado de Pruebas · Fase `B-EP-025-HU-032-enganches-leen-lo-suspendido`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-025-HU-032-enganches-leen-lo-suspendido` |
| **HU** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, carpetas temporales, Windows 11; la consulta a la base simulada y contada; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-003 | CA-02 | Crítica | `test_ocho_a_la_vez_consultan_una_vez_y_ven_lo_mismo`, `test_sin_mensaje_propio_usa_la_lista_del_mensaje_y_otro_mensaje_consulta_otra_vez`, `test_un_turno_caido_no_deja_esperando_para_siempre` | 8 hilos a la vez: 1 consulta y los 8 ven lo suspendido; sin mensaje propio no consulta; un mensaje nuevo consulta una vez más; un turno viejo se retoma | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Crítica | `test_suspendido_sale_con_cero`, `test_vencido_o_sin_base_corre`, `test_sin_suspension_el_programa_lee_la_misma_entrada`, `test_el_adaptador_suspendido_no_escribe_nada` | Sale con 0; vencido o sin base corre; la entrada llega igual al programa; `hook_relacionadas.py` suspendido sale con 0 sin escribir | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-02 | Crítica | `test_suspender_el_historico_no_apaga_el_freno`, `test_suspender_freno_lo_apaga_como_antes`, y las 17 de `tests_configuracion` | El histórico suspendido deja el freno frenando; «freno» lo apaga como antes | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el freno tomaba toda suspensión de tipo «enganche» como el freno entero (`niveles.py:117`); se corrigió en la fase, como declara el plan.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python -m unittest core.enganches.tests_suspendidos` | Ran 9 tests in 1.293s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02 | CP-003, CP-004, CP-005 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 3 casos pasan (9 pruebas), y las 17 del freno siguen pasando.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/enganches/suspendidos.py`, `core/enganches/niveles.py`, los 18 adaptadores de `adaptadores/claude-code/`, `core/enganches/tests_suspendidos.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 3 | 0 | Primera ejecución |
| 2 | 2026-10-09 | 10 | 0 | Reabierta: H-7, la hora del vencimiento salía en UTC (análisis 4 del pendiente 149). La consulta lee el vencimiento con `TIMESTAMPDIFF`, y `test_el_vencimiento_vuelve_en_la_misma_hora_que_se_guardo` la corre contra la base de pruebas; dañada a propósito con `UNIX_TIMESTAMP`, la prueba falla |
