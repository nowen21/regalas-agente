# Estado de fase — Fase A-EP-004-HU-018-el-numero-de-pendiente-libre (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-018-el-numero-de-pendiente-libre` |
| **Módulo** | Comprobación automática — la carpeta [`pendientes/`](../../../../../pendientes/README.md) y su índice |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-018](../HU-018-numero-de-pendiente-ya-tomado.md) · ✨ funcionalidad nueva, nacida del hallazgo H-2 del [inventario de HU](../../../../../historico-chat/resumenes/2026-08-16/las-hu-sin-su-fase.md). Fila de HU-018 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 7 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: los dos casos que motivan la HU están documentados y el desfase de hoy se puede medir.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Los **tres están en «No» de entrada**: el número se elige a ojo leyendo el índice |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Comprobación que dice el próximo número libre |
| T-02 | Pendiente | Caso de la numeración con huecos — CP-001 |
| T-03 | Pendiente | Que dos archivos con el mismo número se reporten |
| T-04 | Pendiente | Caso del número repetido — CP-002 |
| T-05 | Pendiente | Cruce carpeta ↔ índice en los dos sentidos |
| T-06 | Pendiente | Caso del cruce — CP-003 |
| T-07 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El próximo libre es el **siguiente al mayor**, no el primer hueco: un hueco puede ser un pendiente cerrado y movido, y reusar su número rompe las citas que lo nombran | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El programa **avisa y no asigna**: asignar el número pisaría lo que otra sesión esté haciendo | §2.6 del plan |
| El cruce se reporta en los dos sentidos. La línea sin archivo es el síntoma de un pendiente movido a `hecho/` sin actualizar el índice, y es el caso que hoy se da | §2.6 del plan |
| Avisar no evita el choque: lo muestra. Repartir turnos es la decisión del pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md), y ese límite queda escrito | Riesgo `R-01` y CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **Hoy ya hay desfase entre la carpeta y el índice** (riesgo `R-02`): se anota antes de empezar, para no confundirlo con lo nuevo.
- **Cruce con la fase de [HU-016](../../HU-016-el-pendiente-cerrado-nombra-su-fase/A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/plan_trabajo.md)**, que puede crear el mismo archivo de validador. La que llegue segunda se suma en vez de reescribir.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
