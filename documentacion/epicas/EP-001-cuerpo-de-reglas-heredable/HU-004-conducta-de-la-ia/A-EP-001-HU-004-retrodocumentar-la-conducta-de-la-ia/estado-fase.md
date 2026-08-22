# Estado de fase — Fase A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia` |
| **Módulo** | Cuerpo de reglas ([`base/01-conducta.md`](../../../../../base/01-conducta.md) y [`base/00-identidad-y-rol/`](../../../../../base/00-identidad-y-rol/base.md)) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-004](../HU-004-conducta-de-la-ia.md) · híbrido: retro-documenta el capítulo `01` y construye las dos reglas que faltan. Fila de HU-004 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 11 — cierre documental. **Ejecutada el 2026-08-22.**

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 10 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase agrega dos reglas a `base/01-conducta.md`, y eso no se toca sin aprobación ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | D-01, nada obliga a correr el recuento de marcas antes de entregar un documento |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir la regla del CA-01. La duda 1 de §2.7 la bloquea (riesgo `B-01`) |
| T-02 | Pendiente | Caso de la pregunta que no ejecuta — CP-001 |
| T-03 | Bloqueada | Dejar el recuerdo apuntando a la regla. Depende de la duda 2 |
| T-04 | Bloqueada | Escribir la regla del CA-02, con su límite. Duda 1 |
| T-05 | Pendiente | Caso del defecto dentro y fuera del alcance — CP-002 |
| T-06 | Bloqueada | Recuerdo apuntando a la regla. Duda 2 |
| T-07 | Pendiente | Caso de los marcadores de IA — CP-003. No depende de ninguna duda |
| T-08 | Pendiente | Constancia de que ningún programa lo comprueba |
| T-09 | Pendiente | Clasificar y aplicar el checklist a las dos reglas nuevas — CP-004 |
| T-10 | Pendiente | Correr, escribir el resultado, versionar y cerrar la trazabilidad |

**Hechas:** 0 de 10. **Bloqueadas:** T-01, T-03, T-04 y T-06.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un recuerdo de este repositorio no viaja a un proyecto heredero: lo que se le exige a cualquier proyecto es regla, no memoria | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La regla de corregir sin preguntar lleva su límite en el cuerpo, no al pie: sin él le pasaría por encima a una `[BLINDADA]` | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y riesgo `R-01` |
| Una regla de conducta se prueba pidiéndole a la IA justo lo que no debe hacer, y mirando el disco en vez de la respuesta | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si las dos exigencias suben a regla del capítulo `01`. Es cambio de `base/` y lo decide el usuario. Bloquea T-01 y T-04.
- **Duda 2 de §2.7:** si el recuerdo se queda con su texto o se recorta a un puntero a la regla. Bloquea T-03 y T-06.
- **La aprobación del plan.** Sin ella no se toca `base/`.
- **Nadie comprueba con un programa que un texto traiga marcadores de IA.** Es de EP-004 y no se construye acá; queda dicho en el resultado.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y las dos dudas siguen abiertas; entre ellas bloquean las cuatro tareas que son el corazón de la fase. **Qué falta para desbloquear:** que el usuario apruebe el plan y responda las dudas 1 y 2. El CA-03 puede avanzar sin ellas.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
