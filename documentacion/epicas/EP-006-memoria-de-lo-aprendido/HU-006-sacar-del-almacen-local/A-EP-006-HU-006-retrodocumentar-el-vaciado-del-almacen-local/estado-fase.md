# Estado de fase — Fase A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |
| **Módulo** | Memoria — [`recuerdos.py`](../../../../../validadores/recuerdos.py) y [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-006](../HU-006-sacar-del-almacen-local.md) · retro-documentación. Es la otra cara de [EP-005 · HU-007](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md): allá se prueba el enganche, acá el resultado. Fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 5 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Lo que haya en el almacén de esta máquina **se observa, no se borra a mano**: vaciarlo haría el trabajo del programa y borraría la evidencia.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. Los dos **corren hoy**; lo que falta es la prueba, en particular la del puntero |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Prueba de que el almacén queda sin archivos — CP-001 |
| T-02 | Pendiente | Observar y anotar qué hay en el almacén de esta máquina — CP-003 |
| T-03 | Pendiente | Prueba de que no queda ni texto ni puntero — CP-002 |
| T-04 | Pendiente | Caso del puntero puesto a mano — CP-002 |
| T-05 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las pruebas usan almacenes de mentira: el real puede tener algo del usuario sin recoger todavía | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El caso del puntero se prueba **a propósito**: es el caso que el índice de la memoria nombra, y un puntero es peor que nada porque parece que hay memoria donde no hay | §2.6 del plan |
| Lo que haya en el almacén de esta máquina se **anota**, no se borra a mano: vaciarlo hace el trabajo del programa y pierde la evidencia de si funcionaba | §2.6 del plan y riesgo `R-01` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si el almacén de esta máquina tiene algo sin recoger** (riesgo `R-01`): se anota qué había y se propone. El programa lo recoge, no la mano.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
