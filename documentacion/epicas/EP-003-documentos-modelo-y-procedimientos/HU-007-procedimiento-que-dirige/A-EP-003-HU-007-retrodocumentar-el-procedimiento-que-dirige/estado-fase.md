# Estado de fase — Fase A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige` |
| **Módulo** | Documentos modelo — [`skills/sdd-orchestrator/SKILL.md`](../../../../../skills/sdd-orchestrator/SKILL.md) |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-007](../HU-007-procedimiento-que-dirige.md) · retro-documentación, fila de HU-007 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Este documento es, además, el caso de prueba del CA-03.** Si una sesión nueva no puede retomar leyéndolo, eso es exactamente lo que la fase viene a medir.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. El **CA-03 es el que más falla en la práctica**, y el plan lo asume |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Recorrido con bitácora — CP-001. Duda 1 |
| T-02 | Bloqueada | Caso del salto de estación — CP-002. Duda 1 |
| T-03 | Bloqueada | Caso de las puertas de usuario — CP-003. Duda 1 |
| T-04 | Pendiente | Caso de la sesión nueva que retoma — CP-004. **No depende de la duda** |
| T-05 | Pendiente | Anotar los casos en que retomar ya falló |
| T-06 | Pendiente | Comparar trece estaciones contra once etapas — CP-005 |
| T-07 | Pendiente | Incremento en la especificación, correr y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** T-01, T-02 y T-03.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El CA-03 se prueba con una sesión nueva **a ciegas**: quien participó retoma de memoria, y lo que se mide es si el documento alcanza | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Las estaciones se recorren con un encargo real, aunque chico: leer el documento no prueba que se detenga, hay que llegar a la puerta | §2.6 del plan |
| Si las trece estaciones y las once etapas de `F15` no coinciden, se anota; alinearlas es cambio de regla o de procedimiento y pasa por el capítulo `20` | §2.6 del plan y riesgo `R-01` |
| Cada dato que la sesión nueva tenga que preguntar es un campo que al `estado-fase` le falta: el fallo se convierte en la lista de lo que sigue | CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** con qué encargo chico se recorren las estaciones. Bloquea el CA-01 y el CA-02.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **El CA-03 puede fallar** (riesgo `R-02`), porque ya falló. El resultado honesto es escribir qué le faltó al estado de la fase para poder retomar.
- **Si el recorrido consume más de lo estimado** (riesgo `R-03`): el encargo se elige chico, con ese límite en mente.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y sin el encargo de la duda 1 no arrancan el CA-01 ni el CA-02. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija el encargo. El CA-03 y la comparación pueden arrancar apenas se apruebe.
