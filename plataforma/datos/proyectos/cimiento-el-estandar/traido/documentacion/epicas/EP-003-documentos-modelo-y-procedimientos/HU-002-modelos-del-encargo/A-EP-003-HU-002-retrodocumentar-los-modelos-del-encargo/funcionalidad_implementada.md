# Funcionalidad implementada — Fase A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo (módulo Documentos modelo)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los tres modelos existen y se encadenan sin una sola falla en 68 historias. Falla el CA-01 por su primera mitad: **el planteamiento de esta casa está vacío**.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |
| **Módulo** | Documentos modelo — [`plantillas/`](../../../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md) |
| **Especificación del módulo** | [`documentacion/documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md), §4.1 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-002: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase midió el encadenamiento sobre el árbol real y escribió las cuatro reglas que lo gobiernan.** Los tres modelos existen desde el principio; lo que faltaba era comprobar que **de verdad se encadenan**, y en cuántos casos.

Se encadenan en 68 de 68. Y la cadena empieza en un eslabón vacío.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-10 · los tres modelos y su cadena | documentación | `plantillas/ciclo-vida-proyectos/01-planteamiento.md`, `epica.md`, `HU.md` | ✅ Ya existían | CP-001 |
| RN-11 · el enlace en los dos lados | programa | [`trazabilidad.py`](../../../../../validadores/trazabilidad.py) · `DOC16` | ✅ Ya existía | CP-001 |
| RN-12 · todo criterio dice cómo validarlo | documentación | `plantillas/ciclo-vida-proyectos/04-HU.md` | ✅ Ya existía | CP-002 |
| RN-13 · la épica sin historias tiene forma | documentación | Los dos modelos | ✅ Ya existía | CP-003 |
| **El planteamiento de esta casa** | documentación | **Vacío** | ❌ **No existe** | CP-004 |
| Las cuatro reglas, escritas | documentación | [`documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md) §4.1 | ✅ **Escrito acá** | — |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ModelosDelEncargo` | ✅ Escritas acá | 4 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Los tres modelos existen y encadenan sin fallas; **el planteamiento está vacío** | ❌ |
| CA-02 | El modelo obliga a «cómo validarlo» y «aprobado cuando» | ✅ |
| CA-03 | El documento que falta se reporta | ✅ |
| Transversal · Límites · No regresión | «Todavía no hay» tiene su sección; los 68 siguen válidos | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---:|
| Épicas | **7** |
| Historias de usuario | **68** |
| Fallas de encadenamiento épica ↔ HU | **0** |
| Planteamiento de este repositorio | **Vacío** |

**Cero fallas en 68 historias es la mejor prueba de que los moldes funcionan.** Y la última fila es la que deja la fase en «No cumple»: los modelos se encadenan bien entre sí, y la cadena arranca en un eslabón que nadie llenó.

---

## 4. Lo que no cumple, y por qué no lo arregla esta fase

**Este repositorio no tiene planteamiento.** Es el documento que dice qué es el proyecto antes de que haya ninguna épica; sin él, las siete cuelgan de nada.

Ya está anotado en el [pendiente 56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md), con una frase que esta fase confirma: *«esta casa reprueba el punto de la cadena que ella misma acaba de escribir»*.

**Lo que la fase agrega es que el molde funciona.** Lo que falta no es la plantilla: es llenarla. Y eso, como dice el propio pendiente, **no es tarea de código — es decidir qué es este proyecto, y sale de una conversación**.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El encadenamiento se mide sobre el **árbol real**, no sobre un ejemplo: 68 casos dicen algo que 2 no | CP-001 del [resultado](resultado_pruebas.md) |
| «Todavía no hay historias» y «falta la sección» son **estados distintos**, y el molde los distingue | CP-003 |
| El planteamiento vacío se reporta y **no se llena**: llenarlo es decidir qué es el proyecto | §4 de este documento |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Llenar el planteamiento | [Pendiente 56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md) — **sale de una conversación con el usuario** |
| Los modelos de la fase | [HU-003](../../HU-003-modelos-de-la-fase/HU-003-modelos-de-la-fase.md) |
| Los modelos de la capa de proyecto | [HU-005](../../HU-005-modelos-de-la-capa-de-proyecto/HU-005-modelos-de-la-capa-de-proyecto.md) |

**La advertencia que deja esta fase:** los moldes del encargo funcionan tan bien que 68 historias los cumplen sin una falla. Y el documento del que todas cuelgan está en blanco desde el primer día, sin que ninguna comprobación lo notara — porque ninguna mira hacia arriba del todo.
