# Estado de fase — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-005-el-sello-de-version-en-el-cierre` |
| **Módulo** | Versionado y adopción — [`plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md`](../../../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md), [`plantillas/ciclo-vida-proyectos/10-estado-fase.md`](../../../../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) y [`validadores/plantillas.py`](../../../../../validadores/plantillas.py) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-005](../HU-005-sellar-el-trabajo-cerrado.md) · 🔀 híbrido: la regla existe, el campo en los modelos no. Fila de HU-005 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 8 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Cambiar modelos sube versión, así que la fase no toca `plantillas/` sin aprobación.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. El **CA-01 está a medias de entrada**: ningún modelo de cierre pide hoy la versión |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Campo del sello en el modelo del cierre. Dudas 1 y 2 |
| T-02 | Bloqueada | Campo en el modelo del estado de la fase, si la duda 1 lo resuelve así |
| T-03 | Bloqueada | Que el validador de modelos vea el campo, con el alcance de la duda 2 |
| T-04 | Bloqueada | Caso del cierre con y sin sello — CP-001 |
| T-05 | Pendiente | Listar las fases cerradas sin sello, sin tocarlas |
| T-06 | Pendiente | Caso de la retroactividad — CP-003. **No depende de dudas** |
| T-07 | Pendiente | Caso de la excepción de `F22` — CP-004 |
| T-08 | Pendiente | Versionar, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 8. **Bloqueadas:** T-01 a T-04.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El sello vive en el documento de la fase, no en un registro central: un registro aparte se desincroniza de las fases que dice describir | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El sello se pide desde el **estado** de la fase y no solo al cerrar, para que el número no se reconstruya de memoria al final | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y RN-04 de la HU |
| Un sello falso es peor que ninguno, porque parece dato: el modelo pide de dónde se copió el número | Riesgo `R-02` y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si el campo del sello entra en los dos modelos o solo en el del cierre.
- **Duda 2 de §2.7:** si el validador lo exige o solo lo avisa cuando falta.
- **La aprobación del plan.** Cambiar modelos sube versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
- **La fecha de corte** (riesgo `R-01`): sin ella, las fases ya cerradas quedarían en falta en cada corrida.
- **Si otra sesión está tocando `plantillas/` o `VERSION`** (riesgo `R-03`): se comprueba `VERSION` justo antes de subirla, por lo que pasó en el pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dudas 1 y 2 bloquean todo el CA-01. **Qué falta para desbloquear:** que el usuario decida en qué modelos entra el campo y con qué alcance lo mira el validador. El CA-02 puede arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
