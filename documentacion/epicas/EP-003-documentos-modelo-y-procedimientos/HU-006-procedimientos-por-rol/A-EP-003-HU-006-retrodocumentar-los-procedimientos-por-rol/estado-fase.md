# Estado de fase — Fase A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` |
| **Módulo** | Documentos modelo — los diez procedimientos de [`skills/`](../../../../../skills/) |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-006](../HU-006-procedimientos-por-rol.md) · retro-documentación, fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo y elegir el encargo de la duda 1 | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 6 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Ningún procedimiento de `skills/` se corrige en esta fase: lo que les falte se numera.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía. El **CA-03 no tiene precedente**: nadie corrió dos veces el mismo encargo para ver si el tipo de salida se repite |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Levantar la tabla rol → entrada → salida — CP-001 |
| T-02 | Pendiente | Incremento en la especificación, con esa tabla. Va detrás de T-01 |
| T-03 | Pendiente | Caso de los dos procedimientos sin su entrada — CP-002 |
| T-04 | Bloqueada | Caso del mismo encargo corrido dos veces — CP-003. Duda 1 |
| T-05 | Pendiente | Numerar los huecos — CP-004. Sale de T-01 |
| T-06 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 6. **Bloqueadas:** T-04.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La tabla se levanta leyendo los diez, no diseñando la tabla ideal: retro-documentar es fotografiar lo que hay | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El CA-03 se mide por **tipo** de resultado, no por texto: dos corridas nunca dan lo mismo palabra por palabra, y comparar así daría un rojo sin significado | §2.6 del plan |
| Un procedimiento que avisa que le falta el dato y entrega igual no cumple el CA-02: entrega algo construido sobre un supuesto que nadie revisó | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** con qué encargo se prueba el CA-03. Tiene que ser real y chico, y correrse dos veces. Bloquea T-04.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **Si a varios procedimientos les falta declarar su entrada** (riesgo `R-01`): se numeran y se propone una fase que los complete. Acá no se tocan.
- **El CA-03 depende de conducta** (riesgo `R-02`): se acepta que quede con evidencia leída, comparando lo que sí es observable.

---

## 4. Si se bloqueó

- **Estación:** 4 — pausa y presentación. **Motivo:** el plan está escrito y sin aprobar, y falta elegir el encargo del CA-03. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija el encargo. Las otras cinco tareas pueden arrancar apenas se apruebe.
