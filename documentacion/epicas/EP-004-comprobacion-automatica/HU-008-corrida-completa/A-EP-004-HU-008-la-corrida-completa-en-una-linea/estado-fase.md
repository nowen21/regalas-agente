# Estado de fase — Fase A-EP-004-HU-008-la-corrida-completa-en-una-linea (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-008-la-corrida-completa-en-una-linea` |
| **Módulo** | Comprobación automática — [`validadores/validar.py`](../../../../../validadores/validar.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-008](../HU-008-corrida-completa.md) · 🔀 híbrido: los subcomandos existen, la corrida completa no. Fila de HU-008 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo y resolver la duda 1 | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 6 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase toca `validar.py`, que es el punto de entrada de todas las comprobaciones: no se toca sin aprobación.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Los **CA-01 y CA-03 están en «No» de entrada**, y por eso la fase construye: no hay línea que corra todo ni veredicto de la corrida entera |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Escribir el subcomando que corre todo. Duda 1 |
| T-02 | Bloqueada | Que lo que no aplica se saltee con su motivo — CP-003 |
| T-03 | Pendiente | Prueba de que los subcomandos siguen corriendo por separado — CP-001. **Se corre antes de tocar nada** |
| T-04 | Bloqueada | Resumen único de la corrida — CP-004 |
| T-05 | Bloqueada | Prueba del código de salida de la corrida completa — CP-005 |
| T-06 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 6. **Bloqueadas:** T-01, T-02, T-04 y T-05.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La corrida completa llama a los subcomandos que ya hay: reescribir las comprobaciones adentro dejaría dos verdades sobre lo mismo | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Lo que no aplica se saltea **diciendo por qué**. Callar es lo que hace hoy un validador sin punto de entrada, y por eso existe el pendiente [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md) | §2.6 del plan |
| El resumen único no reemplaza las salidas de cada comprobación: quien corre para arreglar necesita el detalle, y el total es para saber si se puede cerrar | §2.6 del plan |
| La lista de qué correr se arma de los subcomandos registrados, no a mano: escrita a mano, la corrida completa deja de ser completa con el primer validador nuevo | Riesgo `R-03` y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** si la corrida completa incluye las comprobaciones lentas —linter, pruebas, audit— o si esas van aparte. Bloquea la construcción; el CA-02 no depende de ella.
- **La aprobación del plan.** Se toca `validar.py`, que es el punto de entrada de todo.
- **Si la corrida queda siempre en rojo por fallas heredadas** (riesgo `R-02`): el resumen las distingue de las propias, o nadie la mira.

---

## 4. Si se bloqueó

- **Estación:** 4 — pausa y presentación. **Motivo:** el plan está escrito y sin aprobar, y la duda 1 bloquea los CA-01 y CA-03, que son lo que la fase construye. **Qué falta para desbloquear:** que el usuario apruebe el plan y decida si lo lento entra a la corrida completa. El CA-02 puede arrancar apenas se apruebe, y conviene que sea lo primero: fija la línea base.
