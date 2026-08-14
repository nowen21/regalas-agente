# Resultado de Pruebas — Fase A-EP-001-HU-001-molde-de-regla

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el veredicto de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el [estado-fase.md](estado-fase.md) para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del documento de cierre. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

> **Todavía no se ha ejecutado nada.** El formato queda puesto con la fase, y se va llenando a medida que se corran los casos. Lo que aparece como "no ejecutado" es eso literalmente: no se ha probado, y no se puede leer como aprobado.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-001-molde-de-regla` |
| **HU** | [HU-001](../HU-001-formato-unico-de-regla.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), PP-001 versión 1.0 |
| **Ciclo** | 1, sin empezar |
| **Fecha de ejecución** | Sin ejecutar |
| **Ejecutado por** | Sin asignar |
| **Ambiente y versión** | El repositorio del estándar, en la rama `feature/A-EP-001-HU-001-molde-de-regla` |

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 0 | 0 | 0 | 0 | 7 |

**Casos no ejecutados y por qué:** los siete. La fase está detenida esperando la aprobación de los dos planes y la respuesta a las tres dudas de §2.7 del [plan_trabajo.md](plan_trabajo.md). Sin el molde escrito no hay qué probar.

## 2. Ejecución caso por caso

Los casos, sus criterios y sus prioridades están copiados de [plan_pruebas.md](plan_pruebas.md) §5 y §3.4. No se agregó ni se quitó ninguno.

| Caso | Criterio | Prioridad (del plan) | Fecha | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | Sin ejecutar | No ejecutado | — | — |
| CP-002 | CA-01 | Crítica | Sin ejecutar | No ejecutado | — | — |
| CP-003 | CA-02 | Alta | Sin ejecutar | No ejecutado | — | — |
| CP-004 | CA-02 | Media | Sin ejecutar | No ejecutado | — | — |
| CP-005 | CA-03 | Alta | Sin ejecutar | No ejecutado | — | — |
| CP-006 | RNF-01 | Media | Sin ejecutar | No ejecutado | — | — |
| CP-007 | Transversal, límites | Media | Sin ejecutar | No ejecutado | — | — |

**Correspondencia con el plan:** siete casos en el plan, siete acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada todavía, porque no se ha corrido ningún caso.

## 3. Verificaciones manuales

Los siete casos de esta fase son manuales: el entregable es texto normativo y no hay nada automatizado que correr. La tabla de §2 es, para esta fase, también la de verificaciones manuales.

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| — | Sin ejecutar | | |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| Ninguno | | | | | |

**Defectos abiertos que se aceptan y por qué:** ninguno. No se ha ejecutado nada.

## 5. Veredicto por criterio de aceptación

| Criterio de HU-001 | Casos que lo cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 · Una regla con el molde queda citable | CP-001, CP-002 | Sin ejecutar | No evaluado |
| CA-02 · Una regla con dos exigencias no pasa | CP-003, CP-004 | Sin ejecutar | No evaluado |
| CA-03 · Un identificador repetido se detecta | CP-005 | Sin ejecutar | No evaluado |
| RNF-01 · El molde se entiende sin saber del tema | CP-006 | Sin ejecutar | No evaluado |
| Transversal, límites | CP-007 | Sin ejecutar | No evaluado |

**Los que no cumplen:** ninguno está en "No". Están todos en "no evaluado", que no es lo mismo y no se puede contar como cumplido.

## 5.1 Lo que el plan exigía

Copiado de [plan_pruebas.md](plan_pruebas.md). Cada fila dice dónde lo pide el plan.

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios de aceptación | Plan §5 | 100%, ningún criterio sin caso | 100% en diseño, 0% ejecutado | No evaluado |
| Casos críticos ejecutados | Plan §3.4 | Los dos, CP-001 y CP-002 | 0 de 2 | No evaluado |
| Casos altos ejecutados | Plan §3.4 | Los dos, CP-003 y CP-005 | 0 de 2 | No evaluado |
| Casos ejecutados sobre diseñados | Plan §12.1 | 100%, porque son siete | 0 de 7 | No evaluado |
| Preguntas que tuvo que hacer quien leyó el molde | Plan §12.1, medido en CP-006 | Cero | Sin medir | No evaluado |

**Lo que no se cumplió:** nada está en incumplimiento. Todo está sin evaluar, porque la fase no ha arrancado.

## 6. Veredicto de la fase

**Concepto:** todavía no se ejecutó.

**Justificación:** la fase no ha arrancado. Está detenida en la estación 7, esperando que el usuario apruebe el plan de trabajo y el plan de pruebas y responda las tres dudas que bloquean la primera tarea.

**Qué falta para que cumpla:**

1. Aprobación de los dos planes.
2. Respuesta a las tres dudas de §2.7 del [plan_trabajo.md](plan_trabajo.md).
3. Ejecutar el trabajo y correr los siete casos.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| Ninguna | | |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | Sin empezar | 0 | 0 | Primera corrida, todavía sin ejecutar |
