# Estado de fase — Fase A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |
| **Módulo** | Memoria — [`memoria/semantica.py`](../../../../../memoria/semantica.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-004](../HU-004-busqueda-por-significado.md) · retro-documentación; salió del pendiente [05](../../../../../pendientes/hecho/memoria-semantica.md), ya cerrado. Fila de HU-004 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** Las dependencias del modelo se instalan en un **entorno aislado**: desinstalarlas o instalarlas en el entorno de trabajo lo rompería.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía. Los dos **corren hoy**; lo que falta es la prueba, y en particular la de que nada sale de la máquina |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Caso de la búsqueda con otras palabras — CP-001 |
| T-02 | Pendiente | Caso de que lo combinado no pierda — CP-002 |
| T-03 | Pendiente | Prueba del escenario sin dependencias — CP-003 |
| T-04 | Pendiente | Caso de que nada sale de la máquina — CP-004 |
| T-05 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El escenario sin modelo se **simula**, no se desinstalan las dependencias: desinstalar rompe el entorno de trabajo de quien corre la prueba | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Que nada salga de la máquina se **comprueba**, porque es una regla blindada. Y se comprueba sobre el programa, no sobre la red: con la red caída, un programa que manda datos pasaría igual | §2.6 del plan y riesgo `R-02` |
| La mejora se mide con búsquedas reales, no con un puntaje del modelo: importa si encuentra lo que alguien buscaría | §2.6 del plan |
| Si la mejora es chica, es un resultado útil: se escribe la medida y se decide con el dato | Riesgo `R-01` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.
- **Si la mejora resulta chica** (riesgo `R-01`): la parte opcional puede quedar sin uso, y eso se decide con la medida a la vista.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
