# Estado de fase — Fase «A-EP01-HU03-Descripción» (módulo «M»)   ·   `[CAPA 3]`

> **Checkpoint del orquestador** (`sdd-orchestrator`): el estado persistido en cada puerta para **sobrevivir a la compactación** ("la compactación mata decisiones"). Se escribe/actualiza en **cada puerta** que pasa. Al reanudar, el director lee este archivo y continúa desde la última puerta pasada. Se guarda en `documentacion/<modulo>/estado-fase.md`. Reemplaza los `«…»` y borra esta caja.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `«A-EP01-HU03-Descripción»` |
| **Módulo** | «M» |
| **Brief / Épica / HU** | «punteros» |
| **Última actualización** | AAAA-MM-DD |

---

## 1. En qué estación va

**Estación actual:** «N — nombre». **Última puerta pasada:** «N».

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorer · análisis | contexto entendido | ☐ |
| 2 | Proposer · alcance | 👤 alcance aprobado | ☐ |
| 3 | Épica Writer | 👤 épica aprobada | ☐ |
| 4 | HU Writer | 👤 HUs aprobadas | ☐ |
| 5 | Spec Writer | 👤 spec aprobada | ☐ |
| 6 | Designer | diseño coherente | ☐ |
| 7 | Task Planner | 👤 plan + pruebas aprobados | ☐ |
| 8 | Implementer | implementado + pruebas verdes | ☐ |
| 9 | Verifier | trazabilidad sin faltantes | ☐ |
| 10 | Crítico | sin hallazgos graves | ☐ |
| 11 | Cierre documental + señales | docs y señales al día | ☐ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

> De dónde sale el estado de la estación 9. **No se escribe de memoria ni "porque se vio funcionar"**: se copia del `resultado_pruebas.md` de la fase, §6.

| Campo | Valor |
|---|---|
| **Concepto** | «Cumple / Cumple con observaciones / No cumple / Todavía no se ejecutó» |
| **CA cumplidos** | «cuántos de cuántos» |
| **CA en "No"** | «cuáles. Con uno solo, la fase no cierra» |
| **Defectos abiertos aceptados** | «cuáles y quién los aceptó» |
| **Fuente** | [`resultado_pruebas.md`] |

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| | |

---

## 3. Pendiente / preguntas abiertas

- «Qué falta, qué se está esperando (una aprobación, una respuesta del usuario, una dependencia).»

---

## 4. Si se bloqueó

- **Estación:** «N». **Motivo:** «pruebas rojas / hallazgo grave del Crítico / alcance rechazado / dependencia faltante». **Qué falta para desbloquear:** «…».
