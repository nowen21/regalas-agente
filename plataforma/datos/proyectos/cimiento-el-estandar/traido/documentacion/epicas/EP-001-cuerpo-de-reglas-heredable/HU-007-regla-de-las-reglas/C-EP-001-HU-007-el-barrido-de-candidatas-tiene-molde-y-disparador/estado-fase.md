# Estado de fase — Fase C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que una sesión nueva siga desde ahí sin releer la conversación.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador` |
| **Módulo** | Cuerpo de reglas, capítulo `20` y moldes |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-007](../HU-007-regla-de-las-reglas.md) · punto 2 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md) |
| **Última actualización** | 2026-08-22 |

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `a07a964`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «haga los dos para que salga de una de eso», 2026-08-22 | ☑ |
| 3 | Diseño del plan detallado | [plan_trabajo](plan_trabajo.md) y [plan_pruebas](plan_pruebas.md) | ☑ |
| 4 | Pausa y presentación | 👤 se reporta con el resultado; la decisión de §0.1 va a la vista | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo sobre el 33 | ☑ |
| 6 | Ejecución continua | 6 tareas | ☑ |
| 7 | Pruebas | [resultado_pruebas](resultado_pruebas.md), Cumple, 5 de 5 | ☑ |
| 8 | Cierre documental | [funcionalidad_implementada](funcionalidad_implementada.md) | ☑ |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

## 2. Qué la tiene detenida

**Nada.** La fase está cerrada.

## 3. Lo que una sesión nueva tiene que saber

**El `CA-06` nació con la fase**, y esa fue una decisión del agente entre las dos salidas que el pendiente 33 dejó escritas. Se tomó por `20·M2` (un tema, un dueño) y se le muestra al usuario: si prefiere una historia propia para el barrido, el criterio se mueve entero.

**El primer barrido real lo dispara la próxima publicación.** `M20` queda sin validador a propósito, hasta que se cumpla a mano ([`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md)).
