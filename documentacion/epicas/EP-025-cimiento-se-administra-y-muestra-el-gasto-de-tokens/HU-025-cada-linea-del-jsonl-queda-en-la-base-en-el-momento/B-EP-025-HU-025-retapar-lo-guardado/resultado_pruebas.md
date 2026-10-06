# Resultado de Pruebas · Fase `B-EP-025-HU-025-retapar-lo-guardado`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-025-HU-025-retapar-lo-guardado` |
| **HU** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento local con MariaDB, sobre `2513a97` con los cambios de la fase sin guardar; versión 55.3.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-05 | Crítica | Una línea con una clave `sk-ant-` armada al correr y otra sin clave, en `tests_retapar` | La clave salió, entró la marca, `tapadas` subió a 1 y la línea sin clave no cambió | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-05 | Crítica | Una segunda corrida de `retapar_lineas` en la misma prueba | `0 con claves que ahora se tapan`, y la huella siguió igual | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-05 | Crítica | `manage.py retapar_lineas` sobre la base `cimiento`, y conteo de `sk-ant-` en claro después | `102.478 línea(s) revisadas; 8 con claves que ahora se tapan.`, en 6 min 39 s; después, 0 `sk-ant-` en claro | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** Nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.consumo.tests_retapar` | Ran 2 tests in 0.036s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-05 | CP-001, CP-002, CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** Los tres casos pasan, y la base real quedó sin claves de Anthropic en claro.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/consumo/tests_retapar.py`, la salida de §3 y el conteo de CP-003 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 3 | 0 | Primera ejecución |
