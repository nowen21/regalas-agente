# Estado de fase — Fase A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo` |
| **Módulo** | Automatismos — [`hook_md.py`](../../../../../validadores/hook_md.py) y [`cargador.py`](../../../../../validadores/cargador.py) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-010](../HU-010-la-regla-llega-al-escribir-el-archivo.md) · ✨ funcionalidad nueva. Fila de HU-010 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo y resolver las dudas 1 y 2 | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 6 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase toca el enganche que corre en **cada escritura**: no se toca sin aprobación.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Los **CA-01 y CA-02 están en «No» de entrada**: hoy llega el índice al abrir la sesión, y hay que acordarse de abrir el capítulo. El CA-03 está resuelto para los enlaces, y falta que valga para la entrega |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir la entrega del capítulo. Dudas 1 y 2 |
| T-02 | Bloqueada | Caso de cada documento con su capítulo — CP-001 |
| T-03 | Bloqueada | Que lo ya entregado no se repita |
| T-04 | Bloqueada | Prueba de la no repetición — CP-003 |
| T-05 | Pendiente | Caso del silencio ante lo que no le toca — CP-004. **No depende de las dudas** |
| T-06 | Bloqueada | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 0 de 6. **Bloqueadas:** todas menos T-05.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La relación documento → capítulo se **declara en una tabla**: adivinarla del nombre del archivo falla con los documentos que no siguen la convención, y el estándar ya tiene varios | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Lo entregado en la sesión no se repite: el arranque ya pesa, y repetir capítulos en cada escritura haría inutilizable la sesión | §2.6 del plan |
| Si la entrega falla, las comprobaciones de enlaces corren igual: perder algo que funciona por algo que no es el peor cambio posible | §2.6 del plan y riesgo `R-03` |
| Lo que no está en la tabla no entrega nada y **se reporta como hueco**: adivinar mal es peor que no entregar, porque un capítulo equivocado se lee y se aplica | Riesgo `R-02` y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** qué capítulo rige cada tipo de documento. La tabla la decide quien mantiene el estándar.
- **Duda 2 de §2.7:** si llega el capítulo completo o solo la regla que aplica, dado lo que pesa.
- **La aprobación del plan.** Se toca el enganche que corre en cada escritura.
- **Cuánto suma la entrega se mide** (riesgo `R-01`): un número, no una impresión, porque ocurre en cada escritura.

---

## 4. Si se bloqueó

- **Estación:** 4 — pausa y presentación. **Motivo:** el plan está escrito y sin aprobar, y las dos dudas bloquean todo menos el caso del silencio. **Qué falta para desbloquear:** que el usuario apruebe el plan, defina la tabla documento → capítulo y decida si llega el capítulo entero o solo la regla.
