# Resultado de Pruebas · Fase `A-EP-025-HU-006-lectura-de-los-jsonl`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-006-lectura-de-los-jsonl` |
| **HU** | [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElLector` (6 pruebas), `LaOrdenGuardaSinDuplicar.test_guarda_lo_de_la_muestra` y `manage.py leer_consumo` contra la base real | Dos llamadas, dos enganches y un archivo, con proyecto y sesión; la orden real leyó los 12 proyectos sin error | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Alta | `test_dos_veces_no_duplica_y_no_vuelve_a_abrir`, `test_lo_nuevo_se_suma` y la orden real repetida | Las mismas cantidades; una llamada más al agregarla; en la segunda corrida real, 11 de 12 proyectos sin nada nuevo (el otro es esta sesión, que sigue escribiendo) | Aprobado | EV-01, EV-02 | Ninguno |
| CP-003 | CA-03 | Media | `test_una_linea_ilegible_se_salta`, `test_la_ultima_linea_sin_salto_queda_para_despues`, `test_la_linea_completada_despues_se_guarda` | Lo legible queda; la línea sin salto entra en la lectura siguiente | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Media | `test_la_suma_de_la_sesion_cuenta_una_vez_la_llamada_partida` y `LaLecturaDelConsumoQuedaProgramada` (5 pruebas) | Dos consumos, no tres; la simulación no corre nada; en Windows, `schtasks /Create`; «ya estaba»; «OMITIDO» fuera de Windows | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** la primera corrida real falló por D-01 de la HU-003 (la tabla de la plataforma vieja). Se corrigió allá, en su ciclo 2, y esta fase se volvió a correr.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La orden contra la base real | `manage.py leer_consumo` | 12 proyectos; el estándar: 7531 llamadas y 35.796.810 tokens de entrada |
| 2 | Los miles con punto, como en Colombia | `manage.py leer_consumo --proyecto dp_card` | «2.678.636 tokens de entrada» |
| 3 | Las pruebas del instalador que tocó la fase | `PrepararCimiento`, `LaLecturaDelConsumoQuedaProgramada`, `PyMySQLParaElFreno` | 16 pruebas, todas pasan |

## 4. Defectos encontrados

Ninguno de esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-001 | `test_no_guarda_texto` | Sí |
| RNF-02 | CP-002 | Un archivo sin cambios no se abre | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan en la base de pruebas y la orden lee los proyectos reales.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/` (12 pruebas en `tests.py`) y `proyectos/cimiento/core/herramientas/tests_instalacion.py` |
| EV-02 | Base real | Tablas `consumo_*` de la base `cimiento` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
