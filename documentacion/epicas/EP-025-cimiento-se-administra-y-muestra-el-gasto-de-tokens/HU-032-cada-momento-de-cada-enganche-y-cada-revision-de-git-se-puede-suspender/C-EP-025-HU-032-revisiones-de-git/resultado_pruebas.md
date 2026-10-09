# Resultado de Pruebas · Fase `C-EP-025-HU-032-revisiones-de-git`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-025-HU-032-revisiones-de-git` |
| **HU** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, carpetas temporales, Windows 11; la consulta a la base simulada y contada; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-006 | CA-03 | Crítica | `test_suspendida_sale_con_cero_y_lo_dice`, `test_sin_suspender_o_vencida_no_esta_suspendida`, `test_lo_que_no_es_de_git_no_mira_las_suspensiones` | `validar.py versionado` suspendida sale con 0 y dice «suspendida en Cimiento hasta el...» con el motivo; sin suspender o vencida corre; `fases` no consulta | Aprobado | EV-01 | Ninguno |
| CP-007 | CA-03 | Alta | `test_tres_revisiones_seguidas_consultan_una_vez` | `versionado`, `marcas` y `plan` seguidas: una consulta; solo `plan` sale suspendida | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** la primera corrida real, con la base de verdad, dejó la lista en `.agente/` de la raíz, que el estándar no ignoraba, y el freno la detuvo (H-3). Se resolvió en el análisis 2: `.gitignore` y el número del vigilante.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python -m unittest core.herramientas.tests_validar_suspendida core.comun.tests` | Ran 26 tests in 2.487s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-03 | CP-006, CP-007 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 2 casos pasan (26 pruebas con las del catálogo), y `validar.py versionado` corre igual con la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/herramientas/validar.py`, `core/herramientas/instalar.py`, `core/comun/enganches.py`, `adaptadores/claude-code/hook_estacion.py`, `core/herramientas/tests_validar_suspendida.py`, `core/comun/tests.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 2 | 0 | Primera ejecución |
