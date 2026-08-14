# Estado de fase — A-EP-001-HU-002-capas-y-precedencia

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-002-capas-y-precedencia` |
| **Módulo** | Cuerpo de reglas |
| **Brief** | [brief.md](../../../../../brief.md) |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-002](../HU-002-capas-y-precedencia.md) |
| **Última actualización** | 2026-08-14 |

## 1. En qué estación va

**Estación actual:** 7, planeación de tareas. **Última puerta pasada:** ninguna. Ninguna de las puertas que pide aprobación del usuario se ha pasado todavía.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Análisis del contexto | contexto entendido | No se hizo como estación aparte. El contexto quedó en el brief |
| 2 | Alcance | alcance aprobado por el usuario | Escrito en el brief, sin aprobación formal |
| 3 | Épica | épica aprobada por el usuario | Escrita, pendiente de aprobación |
| 4 | Historias de usuario | historias aprobadas por el usuario | Escritas las ocho de EP-001, pendientes de aprobación |
| 5 | Especificación del módulo | especificación aprobada por el usuario | No se hizo. Está en duda si aplica a un entregable de texto normativo, igual que en la fase A de HU-001 |
| 6 | Diseño | diseño coherente | No se hizo como estación aparte. Las decisiones de forma están en §2.6 del plan de trabajo |
| 7 | Plan de tareas | plan y pruebas aprobados por el usuario | Los dos escritos, pendientes de aprobación |
| 8 | Implementación | implementado y pruebas en verde | Pendiente |
| 9 | Verificación | trazabilidad sin faltantes | Pendiente |
| 10 | Revisión crítica | sin hallazgos graves | Pendiente |
| 11 | Cierre documental | documentos y aprendizajes al día | Pendiente |
| 12 | Commit | autorizado por el usuario | Pendiente |
| 13 | Publicación | autorizada por el usuario | Pendiente |

**Lo que se saltó y por qué.** Las estaciones 1, 5 y 6 no se recorrieron como paso aparte, por el mismo motivo que en la fase A de HU-001. Queda anotado acá para que no se lea como que se cumplieron: si el usuario decide que la 5 aplica, esta fase no puede avanzar a la 8 sin ella.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Todavía no se ejecutó |
| **Criterios cumplidos** | 0 de 3, sin contar los dos transversales ni el requisito no funcional |
| **Criterios en "No"** | Ninguno, porque no se ha corrido nada |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

## 1.2 Avance de las tareas del plan

Los identificadores se copian de [plan_trabajo.md](plan_trabajo.md) §3, que no se toca. Al cerrar, esto se consolida en el documento de cierre §2.2.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-13 | Pendiente | Ninguna arrancó. La fase espera aprobación de los dos planes y las tres respuestas de §2.7 |

**Hechas:** 0 de 13. **Bloqueadas:** las trece, por la misma causa.

## 2. Decisiones y aprendizajes

| Decisión | Dónde quedó registrada |
|---|---|
| Una sola fase para los tres criterios de HU-002, porque los tres se prueban sobre el mismo orden de precedencia | §0 del [plan de trabajo](plan_trabajo.md) |
| La capa la declara el capítulo y la regla la hereda, salvo que traiga la suya propia | §2.6 del [plan de trabajo](plan_trabajo.md) |
| El desempate se escribe como pasos numerados, y el último paso es pausar, no elegir | §2.6 del [plan de trabajo](plan_trabajo.md) |
| La instrucción del chat no entra en el orden de capas | §2.6 del [plan de trabajo](plan_trabajo.md) |
| Las tres pruebas de conducta las corre el usuario, porque la IA no puede ser juez de sí misma | §3.1 del [plan de pruebas](plan_pruebas.md) |

Todavía no hay dónde registrarlas como aprendizaje buscable: la memoria es [EP-006](../../../EP-006-memoria-de-lo-aprendido/epica.md) y no existe. Mientras tanto viven en los planes.

## 3. Pendiente y preguntas abiertas

Tres dudas bloquean el arranque. Están en §2.7 del [plan de trabajo](plan_trabajo.md) y son la tarea T-01:

1. Si el preámbulo es una capa más o queda fuera del orden, porque no exige nada.
2. Cuántas capas hay en total, contando la del proyecto que todavía no existe, y cómo se nombran.
3. Si una convención puede marcarse como opcional dentro de su capa, o si eso es una capa aparte.

Además falta la aprobación del plan de trabajo y del plan de pruebas, que es la puerta de la estación 7.

Queda una dependencia hacia adelante, que no bloquea: el orden de precedencia nombra la capa propia del proyecto, pero su mecanismo es [HU-006](../../HU-006-capa-propia-del-proyecto/HU-006-capa-propia-del-proyecto.md). Hasta que esa historia se haga, el proyecto de prueba de los casos CP-001 a CP-003 se arma a mano.

## 4. Si se bloqueó

**Estación:** 7. **Motivo:** esperando la aprobación del usuario y la respuesta a las tres dudas. **Qué falta para desbloquear:** que el usuario apruebe los dos planes y responda las tres preguntas de §3. Sin eso no arranca la tarea T-02, que es la que escribe la tabla de capas.
