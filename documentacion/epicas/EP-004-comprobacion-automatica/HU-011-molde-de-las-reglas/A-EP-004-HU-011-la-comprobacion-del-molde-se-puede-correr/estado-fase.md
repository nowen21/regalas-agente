# Estado de fase — Fase A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr` |
| **Módulo** | Comprobación automática — [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) y [`validar.py`](../../../../../validadores/validar.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-011](../HU-011-molde-de-las-reglas.md) · 🔀 híbrido: el programa existe y **no se puede correr**. Punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md); fila de HU-011 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 9 tareas · **detenida por la duda 1 de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase es la que **desbloquea a varias otras**: media docena de fases de esta sesión cierran un CA "por lectura" porque `metareglas.py` no se puede correr.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 5 |
| **CA en "No"** | Los **cinco están en «No» de entrada**: las comprobaciones están escritas y ninguna se puede correr |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Darle punto de entrada al programa. Duda 1. **Sin esto no hay nada que probar** |
| T-02 | Bloqueada | Caso del identificador repetido — CP-002 |
| T-03 | Bloqueada | Caso de la dependencia que manda hacia arriba — CP-003 |
| T-04 | Bloqueada | Caso de la regla sin checklist — CP-004 |
| T-05 | Bloqueada | Anotar la cuenta real contra las 121 del pendiente 19 |
| T-06 | Bloqueada | Caso de la regla que nombra una tecnología — CP-005 |
| T-07 | Bloqueada | Que el punto de entrada acepte el catálogo de un proyecto. Duda 1 |
| T-08 | Bloqueada | Caso de la regla propia sin respaldo — CP-006 |
| T-09 | Bloqueada | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 9. **Bloqueadas:** las nueve — T-01 es la puerta y todo cuelga de ella.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se le abre la puerta al programa que ya está, sin tocar sus comprobaciones: reescribir y correr a la vez impide saber si un hallazgo es del programa viejo o del nuevo | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Si algo no se puede correr, el programa **muere diciendo por dónde se corre**. Salir con 0 sin haber mirado es peor que fallar | §2.6 del plan y pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |
| La cuenta de 121 reglas sin checklist se hizo a mano; la corrida da la real, y el pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) se corrige con ella | §2.6 del plan |
| Abrir la puerta va a destapar cientos de hallazgos. Se anotan como línea base del primer día para que no se lean como regresión | Riesgo `R-01` del plan |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si el subcomando es uno con dos modos —el estándar en seco y el catálogo del proyecto— o dos subcomandos distintos. **Bloquea la fase entera**: sin punto de entrada no hay nada que probar.
- **La aprobación del plan.** Sin ella no se toca `validar.py`.
- **Esta fase desbloquea a otras.** Varias fases de esta sesión cierran un CA "por lectura" porque este programa no corre; cuando corra, esos CA se pueden medir.
- **Resolver este caso no cierra el pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)** (riesgo `R-03`): queda abierto por sus otros puntos.
- **Si alguna comprobación reporta de más** (riesgo `R-02`): se para y se propone. Corregirla es otra fase.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 bloquea la tarea que abre la puerta, de la que cuelgan las otras ocho. **Qué falta para desbloquear:** que el usuario decida si es un subcomando con dos modos o dos subcomandos.
