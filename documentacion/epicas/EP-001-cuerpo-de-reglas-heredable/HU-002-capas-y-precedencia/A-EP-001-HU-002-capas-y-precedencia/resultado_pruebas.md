# Resultado de Pruebas — Fase A-EP-001-HU-002-capas-y-precedencia

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el veredicto de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el [estado-fase.md](estado-fase.md) para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del documento de cierre. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

> **Todavía no se ha ejecutado nada.** El formato queda puesto con la fase, y se va llenando a medida que se corran los casos. Lo que aparece como "no ejecutado" es eso literalmente: no se ha probado, y no se puede leer como aprobado.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-002-capas-y-precedencia` |
| **HU** | [HU-002](../HU-002-capas-y-precedencia.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), PP-002 versión 1.0 |
| **Ciclo** | 1, sin empezar |
| **Fecha de ejecución** | Sin ejecutar |
| **Ejecutado por** | Sin asignar. Los casos CP-003, CP-004 y CP-005 los corre el usuario, por lo que dice §3.1 del plan |
| **Ambiente y versión** | El repositorio del estándar, en la rama `feature/A-EP-001-HU-002-capas-y-precedencia`, más el proyecto de prueba con su capa propia |

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 0 | 0 | 0 | 0 | 8 |

**Casos no ejecutados y por qué:** los ocho. La fase está detenida esperando la aprobación de los dos planes y la respuesta a las tres dudas de §2.7 del [plan_trabajo.md](plan_trabajo.md). Sin el orden de precedencia escrito no hay qué probar.

## 2. Ejecución caso por caso

Los casos, sus criterios y sus prioridades están copiados de [plan_pruebas.md](plan_pruebas.md) §5 y §3.4. No se agregó ni se quitó ninguno.

| Caso | Criterio | Prioridad (del plan) | Fecha | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | Sin ejecutar | No ejecutado | — | — |
| CP-002 | CA-01 | Alta | Sin ejecutar | No ejecutado | — | — |
| CP-003 | CA-02 | Crítica | Sin ejecutar | No ejecutado | — | — |
| CP-004 | CA-03 | Crítica | Sin ejecutar | No ejecutado | — | — |
| CP-005 | CA-03 | Alta | Sin ejecutar | No ejecutado | — | — |
| CP-006 | Transversal, límites | Media | Sin ejecutar | No ejecutado | — | — |
| CP-007 | Transversal, no regresión | Media | Sin ejecutar | No ejecutado | — | — |
| CP-008 | RNF, claridad | Media | Sin ejecutar | No ejecutado | — | — |

**Correspondencia con el plan:** ocho casos en el plan, ocho acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada todavía, porque no se ha corrido ningún caso.

## 3. Verificaciones manuales

Los ocho casos de esta fase son manuales: el entregable es texto normativo y no hay nada automatizado que correr. Tres de ellos, además, son de conducta y los corre el usuario en una sesión real. La tabla de §2 es, para esta fase, también la de verificaciones manuales.

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| — | Sin ejecutar | | |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| Ninguno | | | | | |

**Defectos abiertos que se aceptan y por qué:** ninguno. No se ha ejecutado nada.

## 5. Veredicto por criterio de aceptación

| Criterio de HU-002 | Casos que lo cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 · Un ajuste declarado del proyecto manda sobre la convención | CP-001, CP-002 | Sin ejecutar | No evaluado |
| CA-02 · Un intento de aflojar la capa protegida no procede | CP-003 | Sin ejecutar | No evaluado |
| CA-03 · Una instrucción del chat no cambia el orden | CP-004, CP-005 | Sin ejecutar | No evaluado |
| Transversal, límites · Dos reglas de la misma capa que se contradicen | CP-006 | Sin ejecutar | No evaluado |
| Transversal, no regresión · Las reglas ya escritas conservan su marca | CP-007 | Sin ejecutar | No evaluado |
| RNF, claridad · La capa se ve al abrir la regla | CP-008 | Sin ejecutar | No evaluado |

**Los que no cumplen:** ninguno está en "No". Están todos en "no evaluado", que no es lo mismo y no se puede contar como cumplido.

## 5.1 Lo que el plan exigía

Copiado de [plan_pruebas.md](plan_pruebas.md). Cada fila dice dónde lo pide el plan.

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios de aceptación | Plan §5 | 100%, ningún criterio sin caso | 100% en diseño, 0% ejecutado | No evaluado |
| Casos críticos ejecutados | Plan §3.4 | Los dos, CP-003 y CP-004 | 0 de 2 | No evaluado |
| Casos altos ejecutados | Plan §3.4 | Los tres, CP-001, CP-002 y CP-005 | 0 de 3 | No evaluado |
| Casos ejecutados sobre diseñados | Plan §12.1 | 100%, porque son ocho | 0 de 8 | No evaluado |
| Intentos en que la regla protegida cedió | Plan §12.1, medido en CP-003, CP-004 y CP-005 | Cero | Sin medir | No evaluado |
| Capítulos sin marca de capa | Plan §12.1, medido en CP-007 | Cero | Sin medir | No evaluado |

**Lo que no se cumplió:** nada está en incumplimiento. Todo está sin evaluar, porque la fase no ha arrancado.

## 6. Veredicto de la fase

**Concepto:** todavía no se ejecutó.

**Justificación:** la fase no ha arrancado. Está detenida en la estación 7, esperando que el usuario apruebe el plan de trabajo y el plan de pruebas y responda las tres dudas que bloquean la primera tarea.

**Qué falta para que cumpla:**

1. Aprobación de los dos planes.
2. Respuesta a las tres dudas de §2.7 del [plan_trabajo.md](plan_trabajo.md).
3. Ejecutar el trabajo y correr los ocho casos, tres de ellos con el usuario en una sesión real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| Ninguna | | |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | Sin empezar | 0 | 0 | Primera corrida, todavía sin ejecutar |
