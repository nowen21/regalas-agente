# Resultado de Pruebas · Fase `C-EP-027-HU-006-el-agente-las-recibe`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-027-HU-006-el-agente-las-recibe` |
| **HU** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y una carpeta temporal de proyecto; versión 57.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-03 | Alta | `ElIndiceLlegaAlAbrir` (3 pruebas) | Llega el índice con código, título, grupo y el comando `ver_regla`; con tope cabe y dice cuántas se listan; sin reglas en la base, nada | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-03 | Alta | `ElFrenoDejaLoQueAutorizan` (2 pruebas) | Lo autorizado sale de la tabla, con el código de la regla; sin reglas en la base, del archivo como antes | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** con un tope justo no cabía ninguna fila, porque la nota de cuántas se listan nombraba el comando entero. Se acortó.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.enganches.tests_reglas_del_proyecto --noinput` | Ran 5 tests in 12.980s, OK |
| 2 | El enganche de arranque | `python -m py_compile adaptadores/claude-code/hook_sesion.py` y el índice de un proyecto real sin reglas en la base | Compila; devuelve vacío y el proyecto sigue con su archivo |

## 4. Defectos encontrados

Ninguno de esta fase. La regresión de `core.enganches` tiene la falla del [pendiente 140](../../../../../historico-chat/resumenes/2026-10-07/pendientes/140-la-regla-opt-in-de-un-capitulo-que-no-es-opt-in-no-se-apaga/pendiente.md), de antes.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-03 | CP-001, CP-002 | Aprobado | Sí |
| RNF-01 | CP-001 | Aprobado: una consulta por arranque | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos casos están aprobados; `core.enganches` corre 515 pruebas con la sola falla del pendiente 140.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.enganches`: 515 pruebas, una falla conocida (pendiente 140) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 2 | 0 | Primera ejecución |
