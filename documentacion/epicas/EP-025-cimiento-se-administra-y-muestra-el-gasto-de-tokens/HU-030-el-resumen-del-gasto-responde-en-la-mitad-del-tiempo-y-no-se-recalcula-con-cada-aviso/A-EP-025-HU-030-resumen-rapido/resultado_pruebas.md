# Resultado de Pruebas · Fase `A-EP-025-HU-030-resumen-rapido`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-030-resumen-rapido` |
| **HU** | [HU-030](../HU-030-el-resumen-del-gasto-responde-en-la-mitad-del-tiempo-y-no-se-recalcula-con-cada-aviso.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, MariaDB de WAMP, Windows 11; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `test_por_tipo_cada_llamada_cae_en_su_dia_local`, `test_el_total_por_dia_da_lo_mismo`, `test_la_base_devuelve_una_fila_por_hora` | Ayer suma 100 y hoy 23 de entrada; los totales, 101 y 26; una sola consulta, con `GROUP BY` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Alta | Tres corridas de `GastoDelPeriodo().pestana("resumen")` sobre la base real, con 10.598 llamadas en 7 días | 0,408 s, 0,277 s y 0,285 s; antes, 1,118 s, 1,263 s y 1,214 s | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `test_el_aviso_pasa_por_la_espera_de_30_segundos`, `test_escondida_no_refresca_y_al_volver_si`, `test_el_boton_actualiza_en_el_momento` | El aviso pasa por `alLlegarAviso` con 30.000 ms; con la pantalla escondida no refresca; el botón dispara `actualizar` en el momento | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el Resumen bajó más de lo previsto: a la cuarta parte, no a la mitad.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python manage.py test core.consumo.tests_rapido core.consumo.tests_tablero core.consumo.tests_en_vivo core.consumo.tests_pestanas` | Ran 41 tests in 6.827s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 3 casos pasan, las 35 pruebas que ya había del gasto siguen pasando, y la medición queda por debajo de la meta del RNF-01.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tablero.py`, `core/consumo/templates/consumo/tablero.html`, `core/consumo/tests_rapido.py`; la salida de las pruebas y la medición de CP-002 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 3 | 0 | Primera ejecución |
