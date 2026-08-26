# Estado de fase — Fase «A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22» (módulo «Programas de comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22` |
| **Módulo** | Programas de comprobación (`validadores/version.py`, `validadores/flujo.py`) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-015](../HU-015-derogacion-sin-adoptar.md) · [pendiente 38](../../../../../pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `02ac968`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resuelva esos 8, recuerde que deben pertenecer a una HU» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no preguntar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó las ocho | ☑ |
| 6 | Ejecución continua | 8 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 Commit `02ac968`, verificado en el historial | ☑ |
| 10 | Reporte al usuario | va en el reporte de las ocho | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

**No se detuvo en ninguna estación.**

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
| T-01 | Hecha | CP-001, contra las derogaciones reales |
| T-02 | Hecha | CP-002, sobre la función pura |
| T-03 | Hecha | CP-003, por el recorrido de `flujo.py` |
| T-04 | Hecha | CP-004, los transversales |
| T-05 | Hecha | `validadores/docs/version.md` |
| T-06 | Hecha | La HU-015 al día |
| T-07 | Hecha | El 38 cerrado |
| T-08 | Hecha | `CHANGELOG` 21.3.1 y `VERSION` |

**Hechas:** 8 de 8.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Retrodocumentar no es dar fe de lo que no se vio: la evidencia se produce corriendo hoy, no citando lo que otra sesión dijo haber probado a mano | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Lo que un trabajo sin fase pierde no es la documentación —esta la tenía— sino el plan de pruebas | §5 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| Un caso que afirma sobre datos reales tiene que comprobar primero que esos datos existen, o pasa sin mirar nada | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) y el riesgo `B-03` del plan |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
- **La especificación del módulo de comprobación** sigue sin existir.

---

## 4. Si se bloqueó

No se bloqueó.
