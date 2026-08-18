# Estado de fase — Fase A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` |
| **Módulo** | Versionado y adopción — [`CHANGELOG.md`](../../../../../CHANGELOG.md) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-002](../HU-002-registro-de-cambios.md) · retro-documentación, fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 6 — ejecución continua, **detenida**. **Última puerta pasada:** 5, el plan aprobado por el usuario el 2026-08-17 («autorizados los planes de trabajo»).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 7 tareas · **detenida por la duda 1 de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** El registro no se reescribe en esta fase: lo que falte se lista.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. Se sabe de antemano que el **CA-02 va a quedar en «No»**: hoy nada frena un cambio sin entrada, y el CP-003 está escrito para dejar esa evidencia |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Prueba de que ninguna versión queda sin entrada — CP-001 |
| T-02 | Pendiente | Recorrido de todas las entradas contra la RN-02 — CP-002 |
| T-03 | Pendiente | Caso del cambio sin entrada, en copia — CP-003 |
| T-04 | Pendiente | Constancia de que la exigencia no tiene quién la haga cumplir |
| T-05 | Bloqueada | Caso del lector ajeno — CP-004. Duda 1 |
| T-06 | Pendiente | Prueba de la cita por identificador — CP-005 |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** T-05.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba se escribe en `pruebas.py` y no dentro de `metareglas.py`, que no se puede correr: una comprobación que no corre no comprueba nada | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Las entradas incompletas se listan, no se completan: el registro es rastro y reescribirlo borra lo que pasó | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y RN-04 de la HU |
| El caso del CA-02 se escribe **esperando** que nada frene el cambio. Escrito al revés, el rojo se leería como defecto de esta fase en vez de como el hueco que documenta | §3.3 y CP-003 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** quién hace de lector del CA-03. Tiene que ser alguien que no siguió los cambios. Bloquea T-05.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **El CA-02 no lo cierra esta fase.** Lo que falta —que un cambio sin entrada no pase— es [EP-005 · HU-005](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md). Acá solo queda la evidencia.
- **El tramo de las dos numeraciones vivas** (pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md)) puede hacer fallar el CP-001. Se documenta como excepción.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y falta elegir el lector del CA-03. **Qué falta para desbloquear:** que el usuario apruebe el plan y diga quién hace de lector. Las otras seis tareas pueden arrancar apenas se apruebe.
