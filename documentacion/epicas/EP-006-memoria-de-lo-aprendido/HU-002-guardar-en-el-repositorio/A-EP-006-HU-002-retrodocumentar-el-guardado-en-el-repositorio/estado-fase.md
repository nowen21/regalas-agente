# Estado de fase — Fase A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |
| **Módulo** | Memoria — [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md) y [`memoria/senales.db`](../../../../../memoria/esquema.sql) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-002](../HU-002-guardar-en-el-repositorio.md) · 🔀 híbrido: los recuerdos cumplen, las señales no. Fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 6 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** La memoria **no se mueve** en esta fase: el límite de la base binaria se mide y se propone.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. El **CA-01 está a medias de entrada**: los recuerdos son texto y se ven en el historial; las señales viven en una base binaria y su cambio no se puede leer |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Caso del recuerdo visible en el historial — CP-001 |
| T-02 | Pendiente | Medir qué se puede leer del historial de la base — CP-002 |
| T-03 | Pendiente | Proponer la salida, **sin decidirla** |
| T-04 | Pendiente | Prueba del índice en los dos sentidos — CP-003 |
| T-05 | Pendiente | Caso de llegar al recuerdo por el índice — CP-004 |
| T-06 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El límite de la base binaria se **mide y se propone**: cambiar dónde vive la memoria es una decisión de fondo, y decidir por cuenta propia dónde vive lo aprendido es peor que el límite | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El índice se prueba en los dos sentidos: una línea sin archivo es un índice que miente, y ya pasó con otros índices del repositorio | §2.6 del plan |
| La forma de los recuerdos no se unifica con la de las señales: son dos cosas distintas, y unirlas es lo que [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md) dice que no se debe hacer | §2.6 del plan |
| El índice se **usa**, no solo se cuenta: uno completo pero inútil cumple el conteo y no el criterio | CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Qué hacer con las señales en base binaria** queda como **propuesta al usuario**, no como decisión de esta fase (riesgo `R-02`).
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.
- **Si el índice de recuerdos resulta incompleto** (riesgo `R-01`): se corrige. Es un archivo del repositorio y no rompe nada.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
