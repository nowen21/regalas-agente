# Estado de fase — Fase A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` |
| **Módulo** | Comprobación automática — [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) y [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-001](../HU-001-criterio-de-lo-comprobable.md) · retro-documentación, fila de HU-001 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 6 tareas · **dudas decididas el 2026-08-18** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Tocar `M9` sube versión, así que no se toca sin aprobación.

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: la duda 1 de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. El **CA-01 está cumplido en forma pero no en sitio**: el criterio vive en `validadores/`, así que no se hereda |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir el criterio donde decida la duda 1 |
| T-02 | Bloqueada | Rehacer el bloque de checklist de `M9` si su texto cambió |
| T-03 | Pendiente | Caso de las reglas de criterio humano — CP-002 |
| T-04 | Pendiente | Caso de las reglas difusas — CP-003 |
| T-05 | Pendiente | Conteo por categoría con su fecha — CP-004 |
| T-06 | Pendiente | Versionar si tocó `base/`, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 6. **Bloqueadas:** T-01 y T-02.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El criterio queda escrito en un solo sitio y el otro documento lo enlaza: la fila 11 del checklist prohíbe el texto prestado, y dos copias se separan solas | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Las pruebas toman reglas reales de cada clase: una regla inventada no discute, y el CA-02 necesita una sobre la que se pueda discutir de verdad | §2.6 del plan |
| El caso del CA-03 prueba **el criterio**, no las reglas: si con el criterio no se puede partir una regla difusa, al criterio le falta texto | Riesgo `R-02` y CP-003 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si el criterio entra al cuerpo de `M9`, o si `M9` lo enlaza y el criterio se queda en `validadores/`. Bloquea T-01 y T-02; las pruebas no dependen de ella.
- **La aprobación del plan.** Tocar `M9` sube versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
- **Hoy el criterio no viaja a un proyecto heredero**, porque vive en `validadores/`. Es lo que la duda 1 resuelve.
- **Si aparecen reglas mal clasificadas** (riesgo `R-01`): se anotan y se suman al pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Reclasificar lo decide el usuario.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 bloquea el CA-01. **Qué falta para desbloquear:** que el usuario decida dónde vive el criterio. Los CA-02 y CA-03 pueden arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
