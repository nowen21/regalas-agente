# Estado de fase — Fase «D-EP-001-HU-009-enlazar-en-vez-de-repetir» (módulo «Cuerpo de reglas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `D-EP-001-HU-009-enlazar-en-vez-de-repetir` |
| **Módulo** | Cuerpo de reglas — la fila 11 del checklist |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) · [pendiente 19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que **sigue abierto** |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «cumpla su tarea» sobre el trabajo del 19 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no informar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo sobre el 19 | ☑ |
| 6 | Ejecución continua | 5 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | va en el reporte del 19 | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en la fila 11, para las dos que no piden decisión |
| **Defectos abiertos aceptados** | tres: `12·PR3`, `01·C16` y `04·S7` |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

**La categoría queda a medias a propósito**, y está declarado desde el §1 del plan: de los cinco casos, dos se arreglan escribiendo y tres necesitan una decisión o un cambio en cuatro reglas a la vez.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Frase por frase, con la regla prestada delante |
| T-02 | Hecha | `Q7` al molde de `14·EST3` |
| T-03 | Hecha | `PR4` y su ejemplo, que era de logs |
| T-04 | Hecha | Las dos en CUMPLE, con el largo remedido |
| T-05 | Hecha | `CHANGELOG` 23.7.4, `VERSION`, y el 19 al día |

**Hechas:** 5 de 5.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **Un enlace delante de un texto repetido se lee como diligencia.** Las dos cumplían la mitad que se ve, y por eso duraron | §2 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **La forma correcta ya estaba escrita en otra regla del mismo cuerpo.** `14·EST3` toma de `C3` lo mismo que `Q7` y cumplía | §3 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Un ejemplo que ilustra lo que la regla dejó de decir es peor que ninguno:** manda a buscar la exigencia donde ya no está | §4 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **El conteo exacto es la red contra el cambio no declarado.** Bajar dos, ni una más ni una menos | [CP-006](plan_pruebas.md#cp-006--el-conteo-baja-exactamente-dos) |

---

## 3. Pendiente / preguntas abiertas

- **`12·PR3`** — no exige nada propio. Quedarse con lo que el `04` no dice, **o derogarla**. Decisión del usuario.
- **`01·C16`** — repite a `01·C2` y lo admite por escrito. Su arreglo pasa por normalizar el bloque `Encadenamiento` en cuatro reglas a la vez.
- **`04·S7`** — sus dos sellos prescriben derogarla en favor de [`10·DEP3`](../../../../../base/10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día). **Derogar obliga a adoptar** ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) en todos los proyectos: es del usuario.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
