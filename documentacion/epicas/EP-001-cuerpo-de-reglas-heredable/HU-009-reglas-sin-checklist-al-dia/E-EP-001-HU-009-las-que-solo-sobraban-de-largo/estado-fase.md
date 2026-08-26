# Estado de fase — Fase «E-EP-001-HU-009-las-que-solo-sobraban-de-largo» (módulo «Cuerpo de reglas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `E-EP-001-HU-009-las-que-solo-sobraban-de-largo` |
| **Módulo** | Cuerpo de reglas — la fila 10 del checklist |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) · [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que **sigue abierto** |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `cf325a3`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «cumpla su tarea y no quiero más informes» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió expresamente no informar entre unidades | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo sobre el 19 | ☑ |
| 6 | Ejecución continua | 6 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 Commit `cf325a3`, verificado en el historial | ☑ |
| 10 | Reporte al usuario | va en el reporte del 19 | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en la fila 10, para las diez de redacción |
| **Defectos abiertos aceptados** | dos: las cinco de anexo, y las notas del porqué sin escribir |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

**Toca diez de las quince que reprueban solo la fila 10**, y el corte está declarado desde el §1 del plan: las otras cinco no son redacción.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | 15 reprueban solo la fila 10 |
| T-02 | Hecha | 10 de redacción · 5 de anexo o congeladas |
| T-03 | Hecha | Las diez reescritas |
| T-04 | Hecha | **Cinco seguían pasadas tras la primera pasada; `G9` necesitó tres** |
| T-05 | Hecha | Las diez en CUMPLE, con el largo remedido |
| T-06 | Hecha | `CHANGELOG` 23.7.5, `VERSION`, y el 19 al día |

**Hechas:** 6 de 6.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **El bloque de ejemplo es espacio gratis y nadie lo usaba.** La fila 10 mide solo el cuerpo; una enumeración ahí cuesta todo y en el ejemplo, nada | §2 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Lo que sobra casi siempre es el porqué**, y `M5` ya lo decía en la propia fila: acertó ocho de diez veces | §2 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Escribir corto no sale a la primera.** Cinco de diez seguían pasadas tras la primera reescritura | §3 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Acortar es el cambio que más fácil se hace mal sin que se note:** el texto corto se lee mejor y parece mejor aunque falte una exigencia | §3.1 del [`plan_pruebas.md`](plan_pruebas.md) |
| **Una excepción no se resume**, porque resumirla cambia qué permite | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |

---

## 3. Pendiente / preguntas abiertas

- **Las diez notas de `notas/`** con el porqué que se sacó del cuerpo. `M5` dice que ahí va; esta fase lo quitó y no lo puso. No se perdió —los sellos dicen qué salió— pero no está donde debería.
- **Las cinco que no eran de redacción:** `03·D8`, `04·S9`, `04·S10` y `05·E4` piden **anexo**, que obliga a convertir el capítulo en carpeta; `02·F13` se reescribió hace días.
- **`04·S9` no se acorta de paso.** Es el único modelo de excepción completa del cuerpo, y su excepción es lo único que no se puede tocar.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
