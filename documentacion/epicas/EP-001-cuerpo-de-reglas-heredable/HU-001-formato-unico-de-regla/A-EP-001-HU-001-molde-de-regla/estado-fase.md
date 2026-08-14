# Estado de fase — A-EP-001-HU-001-molde-de-regla

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-001-molde-de-regla` |
| **Módulo** | Cuerpo de reglas |
| **Brief** | [brief.md](../../../../../brief.md) |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-001](../HU-001-formato-unico-de-regla.md) |
| **Última actualización** | 2026-08-13 |

## 1. En qué estación va

**Estación actual:** 7, planeación de tareas. **Última puerta pasada:** ninguna. Ninguna de las puertas que pide aprobación del usuario se ha pasado todavía.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Análisis del contexto | contexto entendido | No se hizo como estación aparte. El contexto quedó en el brief |
| 2 | Alcance | alcance aprobado por el usuario | Escrito en el brief, sin aprobación formal |
| 3 | Épica | épica aprobada por el usuario | Escrita, pendiente de aprobación |
| 4 | Historias de usuario | historias aprobadas por el usuario | Escritas las ocho de EP-001, pendientes de aprobación |
| 5 | Spec del módulo | spec aprobada por el usuario | No se hizo. Está en duda si aplica a un entregable de texto normativo |
| 6 | Diseño | diseño coherente | No se hizo como estación aparte. Las decisiones de forma están en §2.6 del plan de trabajo |
| 7 | Plan de tareas | plan y pruebas aprobados por el usuario | Los dos escritos, pendientes de aprobación |
| 8 | Implementación | implementado y pruebas en verde | Pendiente |
| 9 | Verificación | trazabilidad sin faltantes | Pendiente |
| 10 | Revisión crítica | sin hallazgos graves | Pendiente |
| 11 | Cierre documental | documentos y aprendizajes al día | Pendiente |
| 12 | Commit | autorizado por el usuario | Pendiente |
| 13 | Publicación | autorizada por el usuario | Pendiente |

**Lo que se saltó y por qué.** Las estaciones 1, 5 y 6 no se recorrieron como paso aparte. Queda anotado acá para que no se lea como que se cumplieron: si el usuario decide que la 5 aplica, esta fase no puede avanzar a la 8 sin ella.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Todavía no se ejecutó |
| **Criterios cumplidos** | 0 de 3 |
| **Criterios en "No"** | Ninguno, porque no se ha corrido nada |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

## 2. Decisiones y aprendizajes

| Decisión | Dónde quedó registrada |
|---|---|
| Una sola fase para los tres criterios de HU-001, porque los tres validan el mismo documento | §0 del [plan de trabajo](plan_trabajo.md) |
| Las dos reglas de prueba son las reglas mismas del molde, no reglas inventadas | §2.1 del [plan de trabajo](plan_trabajo.md) |
| Cinco decisiones de forma: dónde vive el molde, cómo se arma el identificador, cómo se cita, cómo van los ejemplos y qué se marca como comprobable | §2.6 del [plan de trabajo](plan_trabajo.md) |

Todavía no hay dónde registrarlas como aprendizaje buscable: la memoria es [EP-006](../../../EP-006-memoria-de-lo-aprendido/epica.md) y no existe. Mientras tanto viven en el plan.

## 3. Pendiente y preguntas abiertas

Tres dudas bloquean el arranque. Están en §2.7 del [plan de trabajo](plan_trabajo.md) y son la tarea T-01:

1. Si un entregable de texto normativo necesita spec aparte, o si la historia de usuario con sus criterios hace las veces de spec.
2. Si el capítulo de reglas sobre reglas se numera 20, al final, o 00, al principio.
3. Qué partes del molde siguen siendo obligatorias cuando la regla no admite ejemplo.

Además falta la aprobación del plan de trabajo y del plan de pruebas, que es la puerta de la estación 7.

## 4. Si se bloqueó

**Estación:** 7. **Motivo:** esperando la aprobación del usuario y la respuesta a las tres dudas. **Qué falta para desbloquear:** que el usuario apruebe los dos planes y responda las tres preguntas de §3. Sin eso no arranca la tarea T-02, que es la que escribe el molde.
