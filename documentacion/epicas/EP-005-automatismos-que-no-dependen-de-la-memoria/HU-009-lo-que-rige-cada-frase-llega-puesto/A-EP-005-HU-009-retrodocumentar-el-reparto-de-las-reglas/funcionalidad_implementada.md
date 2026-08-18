# Funcionalidad implementada — Fase A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas (módulo Automatismos)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas` |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md), §4.1 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-009: [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto), [CA-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-02--se-dice-qué-llegó-puesto-y-qué-llegó-como-índice), [CA-03](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-03--el-arranque-no-se-vuelve-lento) y sus dos requisitos no funcionales |
| **Fecha de cierre** | 2026-08-15 |
| **Commit** | Autorizado el 2026-08-15 |

---

## 1. Qué se implementó — resumen

**Nada de programa: esta fase escribió lo que faltaba de un programa que ya corría.** El reparto de las reglas al abrir la sesión existe desde la versión 5.0.0 y nunca tuvo dicho qué se le exige ni una sola prueba. Una decisión así, viviendo solo en un comentario del código, se deshace en el primer cambio y nadie se entera.

Ahora está escrito, probado y medido.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-10 a RN-12 · qué llega completo y qué en índice | programa | [`validadores/cargador.py`](../../../../../validadores/cargador.py) | ✅ Ya existía | CP-001 |
| RN-13 · se dice cuál rige y cuál hay que abrir | programa | [`validadores/cargador.py`](../../../../../validadores/cargador.py) | ✅ Ya existía | CP-002 |
| RN-14 · un capítulo nuevo del prefijo entra solo | programa | [`validadores/cargador.py`](../../../../../validadores/cargador.py) | ✅ Ya existía | CP-001, paso 3 |
| RN-15 · con el gate sin pasar llega solo esa regla | programa | [`validadores/cargador.py`](../../../../../validadores/cargador.py) | ✅ Ya existía | CP-005 |
| RN-16 · el motivo de no cargarlo todo | documentación | [`automatismos/spec.md`](../../../../automatismos/spec.md), §4.1 | ✅ Escrito acá | — |
| Las cuatro exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `RepartoDeLasReglas` | ✅ Escritas acá | 10 casos en verde |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | Los capítulos `00` y `01` llegan completos, incluido el que vive en carpeta; el resto, como índice | ✅ |
| CA-02 | Los dos encabezados dicen qué rige ya y qué hay que abrir | ✅ |
| CA-03 | 73 KB de 369 KB y 0,21 s, medidos y escritos. El usuario decidió que no se nota | ✅ |

---

## 3. Qué se probó

Diez casos automatizados y tres verificaciones a mano. La que importa: **se rompió el reparto a propósito** y se comprobó que la prueba lo caza. Sin eso, diez casos en verde no dirían si vigilan algo.

Detalle en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 4. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El reparto ya mandaba completos `00` y `01` desde la 5.0.0: la fase retro-documenta, no construye | [`automatismos/spec.md`](../../../../automatismos/spec.md), §4.1 |
| Una prueba en verde no dice si vigila algo: se rompe lo que vigila y se comprueba que lo detecta | §3 del [resultado](resultado_pruebas.md) |
| El [pendiente 25](../../../../../pendientes/hecho/las-reglas-de-como-se-escribe-si-llegaban-puestas.md) se cierra por falso: su causa se dedujo en vez de verificarse | Ese mismo pendiente, con el motivo escrito |
| 0,21 s al abrir la sesión no se nota | Decisión del usuario, 2026-08-15 |

---

## 5. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el capítulo del flujo llegue al escribir un plan | [EP-005 · HU-010](../../HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md) |
| Comprobar que lo entregado cumple la regla que llegó | [EP-004 · HU-013](../../../EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) |
| Que el hallazgo grave detenga el trabajo | [EP-005 · HU-003](../../HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md), `CA-03` |

**La advertencia que deja esta fase:** que la regla llegue es necesario y no es suficiente. `ID8` llegaba completa el 2026-08-14 y se incumplió durante toda una sesión.
