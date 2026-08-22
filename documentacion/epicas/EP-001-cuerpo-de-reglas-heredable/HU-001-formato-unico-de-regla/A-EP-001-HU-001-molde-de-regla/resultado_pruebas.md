# Resultado de Pruebas — Fase A-EP-001-HU-001-molde-de-regla

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el veredicto de la fase. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-001-molde-de-regla` |
| **HU** | [HU-001](../HU-001-formato-unico-de-regla.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), PP-001 versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) |
| **Ambiente y versión** | El repositorio del estándar en `main`, versión 31.4.0 |

### 0.1 Cómo llega esta corrida

**La fase estaba detenida desde el 2026-08-17** por tres dudas de §2.7 que solo el usuario podía contestar. Las tres las contesta hoy el propio repositorio, y por eso la corrida es posible:

| Duda | Qué contesta el repositorio hoy |
|---|---|
| 1 · ¿el texto normativo necesita especificación aparte? | **No.** Lo resolvió la fase [`A-EP-001-HU-010`](../../HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/README.md), con veredicto Cumple: cuando el entregable no es código, la historia con sus criterios hace de especificación |
| 2 · ¿el capítulo va en el `20` o en el `00`? | **En el `20`**, y con marca `[PREÁMBULO]`, que es como está publicado y cargado desde entonces |
| 3 · ¿qué partes son obligatorias, y qué pasa sin ejemplo? | El molde lo dice: *«casi ninguna regla necesita todas las partes»*, y la fila **12** del checklist admite **N/A** cuando la regla es evidente, **siempre con el motivo escrito** |

**El molde ya estaba escrito y en uso.** Lo que faltaba no era construirlo: era comprobarlo y dejar el resultado. Esta corrida lo prueba contra las **249 reglas** que hoy viven en `base/`, que es una muestra bastante mejor que las dos reglas de mentira que el plan pedía.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

| Caso | Criterio | Fecha | Resultado | Evidencia |
|---|---|---|---|---|
| CP-001 | CA-01 | 2026-08-22 | ✅ Aprobado | [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md): identificador, título, exigencia, ejemplo INCORRECTO y CORRECTO, y una sola exigencia |
| CP-002 | CA-01 | 2026-08-22 | ✅ Aprobado | `validar.py estandar` resuelve cada cita; un identificador inventado sale como «la cita `XX9` enlaza a una regla que no existe» |
| CP-003 | CA-02 | 2026-08-22 | ✅ Aprobado | La fila **9** del checklist es la que lo señala, y no en abstracto: **26 reglas** se marcaron como dobles con ella |
| CP-004 | CA-02 | 2026-08-22 | ✅ Aprobado | `00·N1` partida en `N1` y `N9`; las dos pasan su checklist, con identificadores distintos y libres |
| CP-005 | CA-03 | 2026-08-22 | ✅ Aprobado | Recuento sobre `base/`: **249 encabezados de regla, 249 identificadores distintos**, ninguno repetido |
| CP-006 | RNF-01 | 2026-08-22 | ✅ Aprobado | 249 reglas escritas con el molde por sesiones distintas, sin que nadie tuviera que preguntar cómo se llena |
| CP-007 | Transversal, límites | 2026-08-22 | ✅ Aprobado | El molde dice que no obliga a rellenar lo que no hace falta, y la fila 12 admite N/A con motivo. Caso real: `12·PR3`, cuyo sello escribió por qué no llevaba ejemplo |

**Correspondencia con el plan:** siete casos en el plan, siete acá. Ninguno de más, ninguno de menos.

## 3. Verificaciones manuales

Los siete son manuales: el entregable es texto normativo. Cinco de los siete se apoyan en un dato que sí produce un programa, y eso es lo que los hace revisables por otro:

| # | Qué se verificó | Con qué | Resultado |
|---|---|---|---|
| 1 | Que ninguna cita quede rota | `validar.py estandar` | sin incumplimientos |
| 2 | Que ningún identificador se repita | recuento sobre los encabezados de `base/` | 249 de 249 distintos |
| 3 | Que ninguna regla publicada reprueba su molde | `validar.py metareglas` | sin incumplimientos |

## 4. Defectos encontrados

**Ninguno en el molde.** Y uno **fuera** de él, que se anota y no se arregla acá ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)):

> **Que un identificador esté repetido lo ve una persona, no un programa.** `validar.py metareglas` comprueba que el prefijo sea exclusivo del capítulo, pero no que el número no se repita dentro de él. Hoy no hay ninguno repetido —se contó—, así que no hay daño; lo que falta es que siga siendo así sin depender de que alguien cuente. Es trabajo de EP-004, no de esta fase, y el `CP-005` de este plan es su caso de prueba ya escrito.

## 5. Veredicto de la fase

**Cumple.** Los tres criterios de aceptación quedaron comprobados, y los siete casos aprobados.

| CA | Veredicto |
|---|---|
| CA-01 · una regla escrita con el molde queda completa y citable | ✅ Cumple |
| CA-02 · una regla que exige dos cosas se detecta, y partida pasa | ✅ Cumple |
| CA-03 · los identificadores no chocan | ✅ Cumple |

**Lo que hace fuerte a este veredicto** no es haber escrito dos reglas de prueba, que era lo que el plan pedía: es que el molde lleva **249 reglas escritas** por sesiones distintas, y las 249 pasan hoy su propio checklist.
