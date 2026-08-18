# Estado de fase — Fase A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` |
| **Módulo** | Cuerpo de reglas ([`base/00-nucleo-blindado.md`](../../../../../base/00-nucleo-blindado.md)) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 6 — ejecución continua, **lista para arrancar**. **Última puerta pasada:** 5, el plan aprobado por el usuario el 2026-08-17 («autorizados los planes de trabajo»).

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

**Nada se ejecutó todavía.** Esta fase no toca `base/` hasta que el plan esté aprobado ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía: no se ha corrido nada |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir el criterio de entrada al núcleo. La duda 1 de §2.7 la bloquea (riesgo `B-01`) |
| T-02 | Pendiente | Caso de la operación irreversible — CP-001 |
| T-03 | Pendiente | Caso del capítulo que llega completo — CP-002 |
| T-04 | Pendiente | Caso de la clave que se detecta — CP-003 |
| T-05 | Pendiente | Constancia de que nada enmascara antes de escribir |
| T-06 | Pendiente | Caso del error que no se disimula — CP-004 |
| T-07 | Pendiente | Medir el capítulo después de T-01 — CP-005 paso 1 |
| T-08 | Pendiente | Comprobar a mano las seis marcas `[BLINDADA]` — CP-005 pasos 2 y 3 |
| T-09 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 9. **Bloqueadas:** T-01.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El criterio de entrada al núcleo va en la cabecera del capítulo, no como una regla `N7`: qué entra al núcleo es meta-regla, y el núcleo debe quedarse corto | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El CA-02 se cierra solo en su mitad normativa: dar por cumplido lo que nadie comprobó es justo el defecto que esta fase viene a corregir | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Probar una prohibición exige comprobar el efecto, no la respuesta: el CP-001 compara los datos contra su línea base | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La duda 1 de §2.7 del plan:** si el criterio de entrada al núcleo entra en esta fase o se difiere a HU-007, que es la regla de las reglas. Bloquea T-01; los CA-01 y CA-03 no dependen de ella.
- **La aprobación del plan.** Sin ella no se toca `base/`.
- **La otra mitad del CA-02** — enmascarar antes de escribir — vive en [EP-005 · HU-002](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) y no se construye acá.
- **[`validadores/metareglas.py`](../../../../../validadores/metareglas.py) no se puede correr** (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)): por eso el CP-005 revisa las marcas a mano.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 sigue abierta. **Qué falta para desbloquear:** que el usuario decida si el criterio de entrada al núcleo entra acá o en HU-007.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
