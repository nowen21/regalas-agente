# Estado de fase — Fase «C-EP-001-HU-009-las-tres-reglas-con-nombre-propio» (módulo «Cuerpo de reglas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-001-HU-009-las-tres-reglas-con-nombre-propio` |
| **Módulo** | Cuerpo de reglas — la fila 5 del checklist |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) · [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que **sigue abierto** |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `cf325a3`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «siga» sobre el trabajo del 19 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no informar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo sobre el 19 | ☑ |
| 6 | Ejecución continua | 8 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 Commit `cf325a3`, verificado en el historial | ☑ |
| 10 | Reporte al usuario | va en el reporte del 19 | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en la fila 5, y el transversal de no regresión |
| **Defectos abiertos aceptados** | dos: `04·S11` declarado, y las otras filas de las tres del `01` |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

**La fase toca una fila de veinte, y está declarado desde el §1 del plan.** Las cuatro reglas siguen en NO CUMPLE al terminar, y el conteo del cuerpo no se movió: 72 antes y 72 después.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Por sello y por programa — de ahí salió `S10`, que no estaba en la lista |
| T-02 | Hecha | `C10`, la peor de las cuatro |
| T-03 | Hecha | `C15` y `C16` |
| T-04 | Hecha | `S10` |
| T-05 | Hecha | Las cuatro reselladas, con el largo remedido |
| T-06 | Hecha | `node`, `deno`, `bun`, `dotnet`, `softdeletes` |
| T-07 | Hecha | 7 casos, y las dos suites en verde |
| T-08 | Hecha | `CHANGELOG` 23.7.3, `VERSION`, y el 19 al día |

**Hechas:** 8 de 8.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **Un argumento sobre una fila no es una revisión de la fila.** El sello de `S10` defendió tres nombres y con eso dio la fila por buena; los otros dos estaban tres líneas arriba | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Un criterio que solo vive en un sello se pierde; uno que vive en una prueba se defiende solo.** Los tres nombres que se conservan tienen caso propio | §3 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Escribir en concepto cuesta caracteres**, y por eso el nombre propio sobrevive: se lee más fácil y convence más | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Se comprobó **antes de tocar** que nombrar órdenes del control de versiones era la excepción y no la costumbre: el capítulo `09` se titula «Control de versiones» y ninguna otra regla las nombraba | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |

---

## 3. Pendiente / preguntas abiertas

- **Las otras filas de `C10`, `C15` y `C16`.** Siguen en NO CUMPLE, y son el pendiente 19.
- **`04·S11`.** Declarado, con su motivo en su propio sello. Reescribirlo es parte de partir la regla.
- **Cuántos nombres quedan que nadie conoce.** La lista del detector se estrecha cada vez que aparece uno; no hay forma de saber cuántos faltan.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
