# Estado de fase — Fase A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` |
| **Módulo** | Cuerpo de reglas — los diecisiete capítulos de capa 2, del `03` al `19` |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-005](../HU-005-convenciones-de-ingenieria.md) · retro-documentación, fila de HU-005 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 11 — cierre documental. **Ejecutada y cerrada el 2026-08-22.** **Última puerta pasada:** 5, el plan aprobado por el usuario el 2026-08-17 («autorizados los planes de trabajo»).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 9 tareas · **dudas decididas el 2026-08-18** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase no toca `base/`: lee, mide y anota hallazgos numerados.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | D-03, media: el barrido de solapes mira los nombres de las reglas, no lo que exigen. Dos reglas con el mismo tema y títulos distintos se le escapan, y queda dicho |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Elegir los dos proyectos y las convenciones. Es la duda 1 (riesgo `B-01`) |
| T-02 | Bloqueada | Caso del contraste entre los dos proyectos — CP-001. Depende de T-01 |
| T-03 | Pendiente | Recorrer los diecisiete capítulos buscando nombres de tecnología — CP-002 |
| T-04 | Pendiente | Levantar la tabla tema → capítulo dueño |
| T-05 | Pendiente | Caso del solape — CP-003 |
| T-06 | Pendiente | Numerar las repeticiones encontradas |
| T-07 | Pendiente | Caso de las marcas de lo opcional — CP-004 |
| T-08 | Pendiente | Revisar los capítulos sin marca que solo sirvan a cierto tipo de proyecto |
| T-09 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 9. **Bloqueadas:** T-01 y T-02.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un proyecto de juguete cumple cualquier convención: sin código real no hay dónde la convención estorbe, y la prueba no prueba nada | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El criterio de "qué cuenta como el mismo tema" se escribe **antes** de llenar la tabla, o el CA-02 queda a gusto de quien lo revisa | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) y riesgo `R-02` |
| Nombrar una tecnología para ilustrar no rompe la agnosticidad; exigirla sí. El caso separa las dos cosas antes de contar hallazgos | §6, CP-002 paso 3, del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** cuáles dos proyectos se usan para el CA-01 y de qué lenguajes. Bloquea T-01 y T-02; los CA-02 y CA-03 no dependen de ella.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **Qué pasa si el recorrido encuentra muchos nombres de tecnología** (riesgo `R-01`): se anotan numerados y se propone una fase aparte. Limpiar no es de esta fase.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 deja el CA-01 sin poder empezar. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija los dos proyectos. Los CA-02 y CA-03 pueden arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
