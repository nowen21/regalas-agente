# Resultado de Pruebas · Fase `A-EP-028-HU-004-propuestas-claras`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-028-HU-004-propuestas-claras` |
| **HU** | [HU-004](../HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django, con una cuenta administradora; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `test_cp001_muestra_lo_que_sale_y_lo_que_entra` y `test_cp001_rechazar_pide_el_motivo` | La línea que sale en rojo y la que entra en verde; sin motivo no se rechaza, con motivo queda guardado | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_cp002_preguntas_claras_con_su_ayuda_y_el_tipo_a_la_vista` | Las dos preguntas nuevas, con el título de su «?» y el lugar del tipo que resulta | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** la regresión destapó tres defectos que se corrigieron aquí: la prueba del capítulo 17 (HU-001) vaciaba la base sin `serialized_rollback` y dañaba diez clases (S-349); el menú de la HU-003 ofrecía «Registrar un proyecto» a una cuenta de consulta; y una prueba vieja rechazaba sin motivo.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.estandar.tests_propuestas_claras --noinput` | Ran 3 tests in 5.520s, OK |

## 4. Defectos encontrados

Los tres de §2, corregidos en esta fase. Ninguno queda abierto.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios tienen su caso aprobado y la regresión de 160 pruebas pasa.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar core.ayuda core.historia core.proyectos core.niveles core.inicio`: 160 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 2 | 0 | Primera ejecución |
