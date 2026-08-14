# Estado de fase — Fase A-EP-004-HU-010-declaracion-y-comprobacion (módulo Programas de comprobación)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-010-declaracion-y-comprobacion` |
| **Módulo** | Programas de comprobación |
| **Brief / Épica / HU** | [brief.md](../../../../../brief.md) · [EP-004](../../epica.md) · [HU-010](../HU-010-convencion-declarada-por-el-proyecto.md) |
| **Última actualización** | 2026-08-14 |

---

## 1. En qué estación va

**Estación actual:** 7 — Task Planner. **Última puerta pasada:** 4.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorer · análisis | contexto entendido | ☑ |
| 2 | Proposer · alcance | 👤 alcance aprobado | ☑ |
| 3 | Épica Writer | 👤 épica aprobada | ☑ |
| 4 | HU Writer | 👤 HUs aprobadas | ☑ |
| 5 | Spec Writer | 👤 especificación aprobada | ☐ |
| 6 | Designer | diseño coherente | ☐ |
| 7 | Task Planner | 👤 plan + pruebas aprobados | ☐ |
| 8 | Implementer | implementado + pruebas verdes | ☐ |
| 9 | Verifier | trazabilidad sin faltantes | ☐ |
| 10 | Crítico | sin hallazgos graves | ☐ |
| 11 | Cierre documental + señales | docs y señales al día | ☐ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

La estación 5 queda pendiente de una decisión, no de un documento: se propone que la HU haga de especificación, como en la fase `A-EP-001-HU-001-molde-de-regla`. Es la duda 1 del plan de trabajo §2.7.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Todavía no se ejecutó |
| **CA cumplidos** | 0 de 6 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La declaración va en los dos archivos que ya existen, no en uno nuevo | Sin registrar todavía |
| Lo que el proyecto no declara no se comprueba, y se avisa | Sin registrar todavía |
| Se escribió código antes de tener plan aprobado, y quedó como línea base | Sin registrar todavía |

---

## 3. Pendiente / preguntas abiertas

- La aprobación del plan de trabajo y del plan de pruebas.
- Si la HU hace de especificación para esta fase, o se escribe una especificación aparte.
- Si estas tres comprobaciones entran en la corrida automática o se corren a demanda.

---

## 4. Si se bloqueó

- **Estación:** 7. **Motivo:** los dos planes están sin aprobar. **Qué falta para desbloquear:** que el usuario los lea y los apruebe, y que responda las dos dudas de §2.7 del plan de trabajo.
