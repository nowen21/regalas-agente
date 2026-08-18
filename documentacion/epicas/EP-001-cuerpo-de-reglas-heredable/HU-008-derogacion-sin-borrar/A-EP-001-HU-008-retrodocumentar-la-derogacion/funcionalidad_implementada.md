# Funcionalidad implementada — Fase A-EP-001-HU-008-retrodocumentar-la-derogacion (módulo Cuerpo de reglas)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Las ocho derogaciones conservan su texto, dicen desde cuándo y por cuál, **su reemplazo existe**, y ninguna volvió como regla vigente.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-008-retrodocumentar-la-derogacion` |
| **Módulo** | Cuerpo de reglas — [`base/`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) y [`validadores/version.py`](../../../../../validadores/version.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-008: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió las pruebas que nadie había escrito.** La derogación funciona desde la `3.1.0` y **ninguna prueba comprobaba que las ocho siguieran ahí**. La única forma de enterarse de que una desapareció habría sido que alguien siguiera una cita y se topara con el vacío.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| La derogada conserva su archivo y su cuerpo | documentación | Las ocho reglas en `base/` | ✅ Ya existía | CP-001 |
| La marca dice desde cuándo y por cuál | documentación | El encabezado de cada una | ✅ Ya existía | CP-002 |
| **Que el reemplazo exista** | pruebas | Escrito acá | ✅ **Comprobado acá** | CP-002 |
| El identificador no se reutiliza | documentación | Los consecutivos de cada capítulo | ✅ Ya existía | CP-003, CP-004 |
| No se le reclama nada a una derogada | programa | [`metareglas.py`](../../../../../validadores/metareglas.py) · `_fila18_clasificada` | ✅ Ya existía | CP-005 |
| Las cinco exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `DerogacionSinBorrar` | ✅ Escritas acá | 5 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Las ocho conservan su texto, con su versión y su reemplazo, y el reemplazo existe | ✅ |
| CA-02 | Ninguna volvió como vigente; el consecutivo no las toma | ✅ |
| CA-03 | A ninguna se le reclama nada | ✅ |
| Transversal · Límites | Las ocho tienen reemplazo; el caso «sin reemplazo» **no ha ocurrido**, y queda dicho | ✅ |
| Transversal · No regresión | 357 pruebas en verde: derogar no reabrió nada | ✅ |

---

## 3. Las ocho

| Desde | Derogada | Por |
|---|---|---|
| `3.1.0` | `F4.1` `F4.2` `F4.3` `F4.4` `F4.5` | `F14` · `F15` · `F16`+`F17` · `F18` · `F19`+`F20` |
| `4.0.0` | `F6` `F7` | `13·DOC1` · `13·DOC3` |
| `6.0.0` | `ID2` | `00·ID7` |

---

## 4. El incumplimiento que habría sido invisible

**Que un identificador derogado vuelva como regla vigente es peor que borrarlo.**

Si se borra `F6`, toda cita a `F6` deja de resolver y alguien lo nota. Si `F6` **vuelve** como una regla nueva, la cita **sigue resolviendo** — a otra cosa. El enlace funciona, el documento se ve sano, y dice algo que nadie escribió.

Ninguno volvió, y ahora hay una prueba que lo comprueba en cada corrida.

**Y lo que el plan no pedía:** se comprobó que **el reemplazo de cada derogación existe**. Una derogación que remita a una regla inventada manda a buscar lo que no está, y se ve igual de bien escrita que una correcta.

---

## 5. La salvedad que la fase deja escrita

| Qué se comprueba | ¿Corre en el trabajo normal? |
|---|---|
| Que la derogada conserve su texto, su marca y su reemplazo | **Sí**, con la suite |
| Que el identificador no vuelva | **Sí** |
| Que no se le reclame nada | **No**: vive en `metareglas.py`, sin punto de entrada |

La tercera es el punto 2 del [pendiente 53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md). **No deja el CA-03 en «No»**, porque lo que el criterio pide lo comprueba la prueba de esta fase, que sí corre.

**Y el caso «derogación sin reemplazo» no ha ocurrido nunca.** Se dice, en vez de darlo por resuelto: el transversal de límites pide que esté definido, y lo honesto es escribir que todavía no se presentó.

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que `metareglas.py` tenga subcomando | [Pendiente 53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md), punto 2 · fase `B-EP-004-HU-002` propuesta |
| Qué hacer con una derogación **sin** reemplazo | Sin destino: no ha ocurrido |
| Que la derogación sin adoptar detenga la fase | [EP-004 · HU-015](../../../EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md), ya cerrada |

**Lo que deja esta fase:** ocho reglas llevan hasta veinte versiones derogadas y nadie comprobaba que siguieran ahí. Habrían desaparecido sin que ninguna corrida lo notara — solo lo habría visto quien siguiera una cita vieja y se topara con el vacío.
