# Estado de fase — Fase A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |
| **Módulo** | Documentos modelo — [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md), [`plantillas/ciclo-vida-proyectos/03-epica.md`](../../../../../plantillas/ciclo-vida-proyectos/03-epica.md) y [`plantillas/ciclo-vida-proyectos/04-HU.md`](../../../../../plantillas/ciclo-vida-proyectos/04-HU.md) |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-002](../HU-002-modelos-del-encargo.md) · retro-documentación, fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 6 tareas, las 6 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: la fase arranca en cuanto se apruebe el plan.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 2 de 3, y los dos transversales |
| **CA en "No"** | El **CA-01**: los modelos encadenan bien, y el planteamiento de esta casa está vacío |
| **Defectos abiertos aceptados** | 2 — `D-01` este repositorio no tiene planteamiento (pendiente 56, sale de una conversación); `D-02` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Incremento en la especificación del módulo. Va con lo que salga de la medición |
| T-02 | **Hecha** | Prueba del encadenamiento HU ↔ épica — CP-001 |
| T-03 | **Hecha** | Caso de los criterios comprobables — CP-002 |
| T-04 | **Hecha** | Caso del encargo a medias — CP-003 |
| T-05 | **Hecha** | Constancia del planteamiento faltante — CP-004 |
| T-06 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El encadenamiento se prueba sobre las HU reales del árbol: una épica armada para la ocasión no trae los casos raros | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El planteamiento del propio estándar no se escribe acá: redactarlo leyendo el repositorio saldría describiendo la solución en vez del problema, y apagaría el aviso sin arreglar nada | §2.6 del plan y pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md) |
| El incremento de la especificación **exige y enlaza**, no copia el modelo: una especificación que describe la plantilla es un documento largo que nadie usa | Riesgo `R-02` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **El estándar sigue sin planteamiento propio** (pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md)). Esta fase lo deja escrito; no lo escribe.
- **Si la prueba del encadenamiento falla en varias HU viejas** (riesgo `R-01`): se listan y se anotan. Corregirlas es trabajo de la fase de cada HU.
- **Si otra sesión está tocando la especificación del módulo** (riesgo `R-03`): se relee justo antes de escribir.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
