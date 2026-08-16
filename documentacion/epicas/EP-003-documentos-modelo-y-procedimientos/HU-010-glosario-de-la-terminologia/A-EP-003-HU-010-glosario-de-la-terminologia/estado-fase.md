# Estado de fase — A-EP-003-HU-010-glosario-de-la-terminologia

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-010-glosario-de-la-terminologia` |
| **Módulo** | Documentos modelo |
| **Brief** | [brief.md](../../../../../brief.md) |
| **Épica** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md) |
| **Última actualización** | 2026-08-14 |

## 1. En qué estación va

**Estación actual:** 9, verificación. **Última puerta pasada:** la 7, el usuario aprobó los dos planes el 2026-08-14 ("aprobado").

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Análisis del contexto | contexto entendido | Hecho. El contexto es el hallazgo H-8 y el [pendientes/21-el-glosario-y-los-terminos-en-ingles.md](../../../../../pendientes/21-el-glosario-y-los-terminos-en-ingles.md) |
| 2 | Alcance | alcance aprobado por el usuario | Escrito en la HU §3.3 y en el plan §1 |
| 3 | Épica | épica aprobada por el usuario | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../../epica.md) ya existe |
| 4 | Historias de usuario | historias aprobadas por el usuario | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md) escrita el 2026-08-14 |
| 5 | Especificación del módulo | especificación aprobada por el usuario | Existe: [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Esta fase le agrega su incremento en T-12 |
| 6 | Diseño | diseño coherente | Las siete decisiones de forma están en §2.6 del plan de trabajo |
| 7 | Plan de tareas | plan y pruebas aprobados por el usuario | Aprobados por el usuario el 2026-08-14 |
| 8 | Implementación | implementado y pruebas en verde | Hecho. Las quince tareas del plan, y siete de ocho casos aprobados |
| 9 | Verificación | trazabilidad sin faltantes | **Detenida.** Los tres criterios cumplen, pero RNF-01 no: la puerta no pasa |
| 10 | Revisión crítica | sin hallazgos graves | Cinco defectos: tres corregidos, dos aceptados. Ninguno grave |
| 11 | Cierre documental | documentos y aprendizajes al día | Hecho, pendiente de rehacer si CP-006 destapa algo: especificación del módulo, registro de cambios, `VERSION`, HU, índices y pendiente 21 |
| 12 | Commit | autorizado por el usuario | Bloqueado por la estación 9 |
| 13 | Publicación | autorizada por el usuario | Pendiente |

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple**: RNF-01 sin caso ejecutado |
| **Criterios cumplidos** | 3 de 3 criterios de aceptación · 1 de 2 requisitos no funcionales |
| **Criterios en "No"** | RNF-01, que se entienda sin saber del tema. Falta CP-006 |
| **Defectos abiertos aceptados** | D-01: el glosario tiene 67 entradas y la historia suponía unas treinta |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

## 1.2 Avance de las tareas del plan

Los identificadores se copian de [plan_trabajo.md](plan_trabajo.md) §3, que no se toca. Al cerrar, esto se consolida en el documento de cierre §2.2.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-15 | Hecha | El detalle tarea por tarea está en §2.2 del `funcionalidad_implementada.md` |

**Hechas:** 15 de 15. **Bloqueadas:** ninguna.

## 2. Decisiones y aprendizajes

| Decisión | Dónde quedó registrada |
|---|---|
| Una sola fase para los tres criterios, porque los tres se validan sobre el mismo documento | §0 del [plan de trabajo](plan_trabajo.md) |
| El glosario vive en `base/`, sin número de capítulo y sin checklist | §2.6 del [plan de trabajo](plan_trabajo.md) |
| Cuatro grupos en vez de una lista alfabética, con orden alfabético dentro de cada grupo | §2.6 del [plan de trabajo](plan_trabajo.md) |
| La entrada define y enlaza; nunca copia el texto de la regla | §2.6 del [plan de trabajo](plan_trabajo.md), y se prueba en CP-007 |
| Renombrar los roles queda fuera: esta fase deja el inventario | §1 del [plan de trabajo](plan_trabajo.md) |

## 3. Pendiente y preguntas abiertas

Las dos dudas se cerraron el 2026-08-14: el glosario va en `base/` y se trabajó sobre `main`.

Queda una prueba sin correr, CP-006: que alguien que no escribió el glosario lea cinco entradas y diga con sus palabras qué es cada una. No la puede hacer el agente. No bloquea el cierre, porque verifica legibilidad y no contenido.

Y queda pendiente el commit, que lo autoriza el usuario aparte.

## 4. Si se bloqueó

**Estación:** 9. **Motivo:** RNF-01 no tiene caso ejecutado. **Qué falta para desbloquear:** correr CP-006, que es que alguien que no escribió el glosario lea cinco entradas y diga con sus palabras qué es cada una. No lo puede hacer el agente.
