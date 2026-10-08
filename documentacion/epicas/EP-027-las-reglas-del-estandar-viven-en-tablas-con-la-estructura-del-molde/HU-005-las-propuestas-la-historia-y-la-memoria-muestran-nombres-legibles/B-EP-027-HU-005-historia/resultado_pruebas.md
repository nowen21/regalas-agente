# Resultado de Pruebas · Fase `B-EP-027-HU-005-historia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-027-HU-005-historia` |
| **HU** | [HU-005](../HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django; versión 57.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-02 | Alta | `LaHistoriaDiceNombres` (3 pruebas) | La tabla dice «Documento del estándar» y la fila, el título; el documento quitado se sigue nombrando; las consultas no crecen con las filas | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 1 caso en el plan, 1 acá.

**Qué salió distinto de lo esperado:** el paso 3 falló la primera vez (11 consultas contra 19): la historia ya hacía una consulta por fila para la versión de cada cambio. Se corrigió en la misma vista.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.historia.tests_nombres_legibles --noinput` | Ran 3 tests in 3.394s, OK |

## 4. Defectos encontrados

Uno, ya corregido: la versión de cada cambio se traía con una consulta por fila (`core/historia/views.py`). Ahora viene con el cambio.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02 | CP-001 | Aprobado | Sí |
| RNF-01 | CP-001, paso 3 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12 | 100% | 1 de 1 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el criterio tiene su caso aprobado, y `core.historia` pasa completa (22 pruebas).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.historia`: 22 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 1 | 0 | Primera ejecución, con la corrección de la consulta por fila |
