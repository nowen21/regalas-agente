# Estado de fase — Fase «A-EP-001-HU-009-clasificar-las-que-faltan» (módulo «Cuerpo de reglas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-009-clasificar-las-que-faltan` |
| **Módulo** | Cuerpo de reglas (`validadores/reglas-validables.md`) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) · [pendiente 19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que **sigue abierto** |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resuelva esos 8» · «hágale» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no preguntar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó las ocho | ☑ |
| 6 | Ejecución continua | 8 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | va en el reporte de las ocho | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 del alcance de la fase |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

**La HU tiene tres criterios y esta fase cubre uno.** Está declarado desde el §0 del plan y no es una fase a medias: los otros dos no dependen de trabajo sino de una decisión y de tiempo por capítulo.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Las quince de conducta, escritas una por una |
| T-02 | Hecha | `G9` y `F4` a validables-faltan · `M15` y `F12` a ya-construidas |
| T-03 | Hecha | Los ocho de despliegue: cinco validables contra proyecto real, tres de criterio |
| T-04 | Hecha | Los seis de observabilidad: tres y tres |
| T-05 | Hecha | El conteo del principio |
| T-06 | Hecha | La HU-009 al día |
| T-07 | Hecha | El pendiente 19, **abierto**, con lo que sigue faltando |
| T-08 | Hecha | `CHANGELOG` 23.1.1 y `VERSION` |

**Hechas:** 8 de 8.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un documento que alimenta a un programa se escribe **como el programa lee**. El rango «C1–C17» ahorraba cuatro líneas y costaba quince hallazgos que nadie sabía si eran reales | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Ser opt-in no exime de aparecer en el registro. Los capítulos `18` y `19` no figuraban ni para decir que no se validan, y eso es lo que los volvió invisibles | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La lista de validables **creció** de ~12 a ~22 al clasificar. Bajar el número era el camino cómodo y habría vaciado el pendiente 01 sin construir nada | `CP-002` del [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Las siete reglas publicadas en «no cumple»** (`F4`, `F5`, `F12`, `M2`, `M4`, `M7`, `M8`). Es el `CA-01` de la HU y **no lo decide el agente**: corregirlas cambia lo que el estándar exige. Ojo con `F12`, cuyo texto está congelado por decisión del usuario: ahí el camino sería legalizar la congelación en `M5`, no reescribir la regla.
- **Las 121 reglas sin bloque de checklist.** Es el `CA-03`, y la propia HU lo plantea por capítulo.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
