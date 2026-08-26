# Estado de fase — Fase «A-EP-004-HU-014-comparar-los-dos-veredictos» (módulo «Programas de comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-014-comparar-los-dos-veredictos` |
| **Módulo** | Programas de comprobación (`validadores/fases.py`) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-014](../HU-014-un-solo-veredicto-por-fase.md) · [pendiente 28](../../../../../pendientes/hecho/un-solo-veredicto-por-fase.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `02ac968`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resuelva esos 8» · «hágale» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no preguntar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó las ocho | ☑ |
| 6 | Ejecución continua | 9 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 Commit `02ac968`, verificado en el historial | ☑ |
| 10 | Reporte al usuario | va en el reporte de las ocho | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | La lectura del concepto, con las dos formas escritas |
| T-02 | Hecha | El `CA-01` |
| T-03 | Hecha | El `CA-02`, leyendo el §5 del resultado |
| T-04 | Hecha | El `CA-03` |
| T-05 | Hecha | Cuatro casos |
| T-06 | Hecha | Vistos en rojo antes de darlos por buenos |
| T-07 | Hecha | `validadores/docs/fases.md` |
| T-08 | Hecha | El 28 cerrado |
| T-09 | Hecha | `CHANGELOG` 23.1.0 y `VERSION` |

**Hechas:** 9 de 9.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| De las dos salidas del pendiente se eligió la que **no cambia ningún molde**: un programa compara y avisa. La otra —que el `estado-fase` enlace en vez de copiar— obligaría a reescribir todas las fases cerradas | §0 del [`plan_trabajo.md`](plan_trabajo.md) |
| Se comparan conceptos normalizados: «Cumple, con una salvedad» no contradice a «Cumple» | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Se reconocen las dos formas de escribir el concepto, porque reprobar por la forma vieja sería reabrir lo cerrado | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La comprobación no encontró nada porque su único caso conocido se había corregido horas antes. Su valor no es lo que encuentra hoy | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
- **Si algún día el `estado-fase` deja de copiar el veredicto**, esta comprobación sobra y se retira.

---

## 4. Si se bloqueó

No se bloqueó.
