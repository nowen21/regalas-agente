# Estado de fase — Fase A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion` |
| **Módulo** | Documentos modelo — la tabla de estaciones de [`skills/sdd-orchestrator`](../../../../../skills/sdd-orchestrator/SKILL.md), y las reglas `00·N2`, `01·C17` y `02·F4` |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-008](../HU-008-puntos-de-aprobacion.md) · 🔀 híbrido: las reglas existen, la lista no vive en la capa que se hereda. Fila de HU-008 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 7 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Escribir la lista en `base/` sube versión, así que no se toca sin aprobación.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. El **CA-01 está a medias de entrada**: la lista existe como tabla de un procedimiento, no como documento de la capa que un proyecto hereda |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir la lista en `base/`. Dudas 1 y 2 |
| T-02 | Bloqueada | Incremento en la especificación del módulo |
| T-03 | Bloqueada | Caso del lector ajeno — CP-001. Depende de T-01 |
| T-04 | Pendiente | Caso de las tres respuestas ambiguas — CP-002. **Prueba una regla que ya existe** |
| T-05 | Pendiente | Caso de las dos aprobaciones consecutivas — CP-003 |
| T-06 | Bloqueada | Comprobar que la lista enlaza y no copia — CP-004 |
| T-07 | Pendiente | Versionar si tocó `base/`, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** T-01, T-02, T-03 y T-06.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La lista se escribe con los puntos que ya rigen: cambiar quién aprueba qué es decisión del usuario, no de una retro-documentación | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La lista enlaza `00·N2` y `01·C17` en vez de repetirlas: la fila 11 del checklist prohíbe el texto prestado | §2.6 del plan |
| Lo que la regla ataja no es el «no», es el «bueno…». Por eso el caso prueba tres formas de ambigüedad, no un sí y un no | §2.6 del plan y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| Que la lista viva dentro de un procedimiento y no en `base/` significa que un proyecto heredero recibe las reglas sueltas y no la lista | ORIGEN del [`plan_trabajo.md`](plan_trabajo.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si la lista entra a `base/` como regla nueva del capítulo de flujo, o como documento del capítulo sin ser regla.
- **Duda 2 de §2.7:** si en esta fase el procedimiento del director pasa a enlazar la lista, o eso queda para otra.
- **La aprobación del plan.** Escribir en `base/` sube versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
- **Si aparece un punto de aprobación que hoy no se pide** (riesgo `R-02`): cambia el tipo de subida a MAYOR, y se declara antes de cerrar.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dudas 1 y 2 bloquean el CA-01 entero. **Qué falta para desbloquear:** que el usuario decida dónde vive la lista y si el procedimiento del director pasa a enlazarla. Los CA-02 y CA-03 pueden arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
