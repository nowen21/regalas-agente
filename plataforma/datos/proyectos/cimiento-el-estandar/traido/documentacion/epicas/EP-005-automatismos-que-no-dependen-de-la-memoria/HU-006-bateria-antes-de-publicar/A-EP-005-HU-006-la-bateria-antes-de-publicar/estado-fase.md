# Estado de fase — Fase A-EP-005-HU-006-la-bateria-antes-de-publicar (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-006-la-bateria-antes-de-publicar` |
| **Módulo** | Automatismos — el disparo antes de publicar, sobre la corrida completa de [EP-004 · HU-008](../../../EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-006](../HU-006-bateria-antes-de-publicar.md) · ✨ funcionalidad nueva. Fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 11, el cierre documental.

> **La fase se cerró el 2026-08-26.** Estaba ejecutada desde el 2026-08-22 con sus criterios en verde, y lo que faltaba era el documento de cierre. Las dos fechas se dejan escritas porque son distintas: no se verificó hoy lo que se verificó entonces.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 5 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase **depende de otra**: sin la corrida completa de EP-004 · HU-008 no hay batería que disparar.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | D-01, la batería no corre las pruebas de los validadores |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Que antes de publicar corra la batería. Dudas 1 y 2 |
| T-02 | Bloqueada | Caso del pedido de publicar — CP-001 |
| T-03 | Bloqueada | Que la falla niegue el visto bueno y el aviso no |
| T-04 | Bloqueada | Caso del veredicto — CP-002 y CP-003 |
| T-05 | Bloqueada | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** las cinco.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La batería **niega el visto bueno**, no impide la acción: publicar lo corre una persona, y un programa que dice bloquear lo que no controla miente | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El veredicto dice qué falló y qué se saltó: un «no» sin motivo se ignora o se fuerza | §2.6 del plan |
| Se apoya en la corrida completa en vez de rearmarla: dos formas de correr todo dan dos verdades | §2.6 del plan |
| Un paso que se saltea siempre es peor que ninguno. Por eso se mide cuánto tarda la batería | Riesgo `R-01` y CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si esta fase espera a la corrida completa de [EP-004 · HU-008](../../../EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md), o si arranca con una lista propia y después se apoya en ella.
- **Duda 2 de §2.7:** qué cuenta como «publicar» en un proyecto — el commit a la rama principal, el despliegue, o los dos.
- **La aprobación del plan.** Sin ella no arranca nada.
- **Esta fase tiene una dependencia dura**: sin la corrida completa no hay batería. Si se construye antes, hay que rehacerla (riesgo `R-03`).

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dos dudas bloquean las cinco tareas. Además, la fase depende de que exista la corrida completa de EP-004 · HU-008. **Qué falta para desbloquear:** que el usuario apruebe el plan, decida si se espera a esa corrida y qué cuenta como publicar.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
