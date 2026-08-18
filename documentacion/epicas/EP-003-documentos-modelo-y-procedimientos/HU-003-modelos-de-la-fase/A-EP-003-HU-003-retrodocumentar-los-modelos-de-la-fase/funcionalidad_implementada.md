# Funcionalidad implementada — Fase A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase (módulo Documentos modelo)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los cinco modelos existen, ninguna pregunta la responden dos, el plan no lleva columna de estado, y **51 planes aprobados se ejecutaron esta sesión sin reescribir ninguno**.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase` |
| **Módulo** | Documentos modelo — [`plantillas/planes/`](../../../../../plantillas/planes/trabajo.md) |
| **Especificación del módulo** | [`documentacion/documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md), §4.2 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-003: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió por qué los moldes son como son.** Los cinco existen desde el principio; lo que faltaba era la constancia de **qué pregunta responde cada uno** y, sobre todo, **por qué el plan no lleva columna de estado**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-14 · cinco modelos, cinco preguntas | documentación | `plantillas/planes/` y `plantillas/estado-fase.md` | ✅ Ya existían | CP-001 |
| RN-15 · el plan no lleva estado | documentación | `plantillas/planes/trabajo.md` | ✅ Ya existía | CP-004 |
| RN-16 · el avance vive en el estado de fase | documentación | `plantillas/estado-fase.md` | ✅ Ya existía | CP-004 |
| RN-17 · la fase recién abierta tiene forma | documentación | El mismo | ✅ Ya existía | Transversal |
| Que la fase incompleta se reporte | programa | [`fases.py`](../../../../../validadores/fases.py) | ✅ Ya existía | CP-002 |
| Que la tarea sin criterio se reporte | programa | [`flujo.py`](../../../../../validadores/flujo.py) · `F18` | ✅ Ya existía | CP-005 |
| Las cuatro reglas, escritas | documentación | [`documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md) §4.2 | ✅ **Escrito acá** | — |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ModelosDeLaFase` | ✅ Escritas acá | 4 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Los cinco existen; ninguna pregunta se repite; el que falta se reporta nombrándolo | ✅ |
| CA-02 | El molde no lleva estado, y 51 planes no se tocaron al ejecutar | ✅ |
| CA-03 | La tarea sin criterio se reporta. 136 avisos de línea base | ✅ |
| Transversal · Límites · No regresión | La fase sin ejecutar tiene forma; los 70 planes siguen válidos | ✅ |

---

## 3. La decisión que sostiene el CA-02

**El plan no lleva columna de estado, y es a propósito.**

Una columna de estado invitaría a tocar el plan mientras se ejecuta. Y en ese momento el plan deja de servir para lo único que sirve: **comparar lo que se dijo contra lo que pasó**. Un plan que se edita sobre la marcha siempre coincide con el resultado, y esa coincidencia no vale nada.

**El avance sí hay que llevarlo**, y vive en el `estado-fase.md`, que copia los identificadores del plan **sin tocar el original**.

**La prueba de que funciona no es teórica:** esta misma sesión ejecutó **51 planes aprobados** y no reescribió ninguno. Los defectos que aparecieron —y aparecieron muchos— se anotaron en el resultado, no en el plan.

---

## 4. La línea base que deja

| Medición, 2026-08-17 | Valor |
|---|---:|
| Líneas de `validar.py flujo` | **151** |
| De ellas, avisos de `F18` —tarea sin criterio— | **136** |
| De `F2` | 12 |
| De `F14` | 3 |
| Planes reescritos después de aprobar | **0** de 51 |

**Los 136 no son un defecto del molde.** Son tareas de cierre —«correr las pruebas», «cerrar la trazabilidad»— que no cuelgan de un criterio porque no cubren ninguno: son el trabajo de terminar. Queda anotado con su fecha para ver si sube.

---

## 5. La vuelta que tiene esta fase

Esta es la fase que documenta **los modelos de la fase**. Y el defecto que arrastran las 51 ejecutadas hoy es que **su plan de pruebas no cuenta los criterios transversales** mientras declara «cobertura 100%».

El molde `planes/pruebas.md` **no obliga** a escribir una fila por transversal. Queda dicho acá, donde corresponde, y es la decisión que se le lleva al usuario: si el molde debe exigirla.

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Si el molde del plan de pruebas debe exigir una fila por transversal | **Decisión del usuario** |
| Los modelos del encargo | [HU-002](../../HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) |
| Los puntos donde aprueba una persona | [HU-008](../../HU-008-puntos-de-aprobacion/HU-008-puntos-de-aprobacion.md) |

**Lo que deja esta fase:** el molde del plan está bien diseñado y la prueba de que lo está la dio esta misma sesión — 51 planes ejecutados, ninguno reescrito. El molde del plan de **pruebas**, en cambio, deja pasar un hueco que se repitió 51 veces.
