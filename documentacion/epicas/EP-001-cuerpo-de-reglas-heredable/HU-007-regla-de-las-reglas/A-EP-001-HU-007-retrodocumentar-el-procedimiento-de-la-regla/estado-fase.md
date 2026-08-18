# Estado de fase — Fase A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |
| **Módulo** | Cuerpo de reglas — el capítulo [`20 · Meta-reglas`](../../../../../base/20-meta-reglas/base.md), su [molde](../../../../../base/20-meta-reglas/estructura-regla.md) y su [checklist](../../../../../base/20-meta-reglas/checklist.md) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-007](../HU-007-regla-de-las-reglas.md) · retro-documentación, fila de HU-007 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 8 tareas · **dudas decididas el 2026-08-18** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Ninguna regla del estándar se edita en esta fase, ni siquiera para que un caso pase.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía: no se ha corrido nada |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Caso del enrutamiento sobre una regla vigente — CP-001 |
| T-02 | Bloqueada | Caso de la candidata devuelta a su sitio — CP-002. Duda 1 |
| T-03 | Pendiente | Caso de la candidata con nombre propio — CP-003 |
| T-04 | Pendiente | Constancia de que la fila 5 se decide leyendo, y por qué |
| T-05 | Bloqueada | Caso de la candidata doble — CP-004. Duda 1 |
| T-06 | Pendiente | Contraste con `F4` y las reglas que salieron de ella — CP-005 |
| T-07 | Bloqueada | Escribir en `notas/` las candidatas rechazadas — CP-006. Va detrás de T-02 y T-05 |
| T-08 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 8. **Bloqueadas:** T-02, T-05 y T-07.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las candidatas de la prueba son reglas reales, aceptadas y rechazadas: una regla inventada no trae el defecto que el procedimiento tiene que atajar, y después hay que borrarla | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Por qué una candidata no entró se escribe en `notas/`, no dentro de `base/`: `base/` es lo que se exige, no el registro de lo que se descartó | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El criterio de partición se contrasta con `F4`, que ya reprobó las filas 8 y 9 por otra razón: el resultado esperado no sale del criterio que se prueba | CP-005 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** cuáles candidatas rechazadas se usan como caso. El usuario es quien recuerda las que se propusieron y no entraron. Bloquea T-02 y T-05.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **[`validadores/metareglas.py`](../../../../../validadores/metareglas.py) no se puede correr** (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)): la fila 5 se decide leyendo, y el resultado tiene que decirlo.
- **Si al recorrer el checklist una regla vigente reprueba** (riesgo `R-01`): se anota y se suma al pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 deja dos casos sin datos. **Qué falta para desbloquear:** que el usuario apruebe el plan y recuerde qué candidatas se rechazaron. Cuatro de las ocho tareas pueden arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
