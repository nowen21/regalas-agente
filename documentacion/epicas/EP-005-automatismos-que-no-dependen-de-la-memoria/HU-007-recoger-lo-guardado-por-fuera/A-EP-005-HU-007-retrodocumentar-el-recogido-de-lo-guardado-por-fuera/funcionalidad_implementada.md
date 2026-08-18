# Funcionalidad implementada — Fase A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera (módulo Automatismos)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** El recogido mueve lo guardado por fuera, deja el almacén sin texto ni puntero, y **nunca borra**: el repetido entra al lado con sufijo y decide el usuario.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera` |
| **Módulo** | Automatismos — [`validadores/hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) y [`recuerdos.py`](../../../../../validadores/recuerdos.py) |
| **Especificación del módulo** | [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md), §4.4 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-007: CA-01, CA-02 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió el incremento con la historia que faltaba.** El recogido funciona y ya tenía doce casos. Lo que no estaba escrito en ninguna especificación es **por qué nunca borra** — y eso no se deduce del código: se aprendió perdiendo memoria de verdad.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-27 · se recoge al abrir y al escribir | programa | [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) | ✅ Ya existía | CP-001 |
| RN-28 · nunca se borra: se mueve, y el repetido entra con sufijo | programa | [`recuerdos.py`](../../../../../validadores/recuerdos.py) · `migrar`, `_libre` | ✅ Ya existía | CP-003, CP-004 |
| RN-29 · las mayúsculas no hacen dos archivos | programa | `_libre`, comparando en minúsculas | ✅ Ya existía | CP-004 |
| RN-30 · con el almacén enlazado no hay nada que mover | programa | `enlazada`, `_es_el_mismo` | ✅ Ya existía | CP-003 |
| Las cuatro reglas, escritas | documentación | [`automatismos/spec.md`](../../../../automatismos/spec.md) §4.4 | ✅ **Escrito acá** | — |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `Recuerdos` y `ElAlmacenLocalQuedaVacio` | ✅ 6 escritas en la fase hermana | 18 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Se recoge; el almacén queda sin texto ni puntero | ✅ |
| CA-02 | El repetido entra al lado; nunca se borra | ✅ |
| Transversal · Límites | Las mayúsculas no hacen dos archivos | ✅ |
| Transversal · Errores | Con el almacén ausente o ilegible, la sesión sigue | ✅ |

---

## 3. Lo que la fase salvó de perderse

**Por qué el recogido nunca borra**, escrito por primera vez en la especificación:

> Una versión anterior **sí borraba** el archivo del almacén cuando era idéntico a uno del repositorio — «no se pierde nada, queda el del repo». Y **destruyó memoria real**: si el almacén es un enlace a la carpeta del repositorio, los dos son **el mismo archivo**, compararlos da idéntico siempre, y el borrado se lleva el único ejemplar.

Eso no se deduce leyendo `migrar()`. Se deduce sabiendo qué pasó, y hasta hoy solo vivía en un comentario del código y en el [pendiente cerrado](../../../../../pendientes/hecho/memoria-borrada-por-el-enganche.md) que lo arregló.

**Es literalmente lo que [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) manda registrar**, aplicado al programa que implementa la memoria.

---

## 4. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El **puntero** se prueba aparte del texto: un archivo que dice «esto vive en el repositorio» envejece igual y manda a un sitio que ya no está | CP-002 del [resultado](resultado_pruebas.md) |
| El caso del nombre repetido usa **contenido distinto**: con contenido igual, un programa que borrara pasaría | CP-004 |
| El incremento de la especificación **incluye el porqué**, no solo la regla | `automatismos/spec.md` §4.4 |

---

## 5. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Qué hace el recogido con lo que **no** es un recuerdo | `D-01` de [`A-EP-006-HU-006`](../../../EP-006-memoria-de-lo-aprendido/HU-006-sacar-del-almacen-local/A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md) — **decisión del usuario**, toca `01·C19` |
| Qué se guarda y con qué alcance | [EP-006 · HU-001](../../../EP-006-memoria-de-lo-aprendido/HU-001-que-se-guarda-tipos-y-alcances/HU-001-que-se-guarda-tipos-y-alcances.md) |

**Lo que deja esta fase:** el recogido es el automatismo más peligroso del estándar —mueve archivos de memoria— y es también el único cuyo diseño está escrito **con la cicatriz a la vista**. Las dos cosas están relacionadas.
