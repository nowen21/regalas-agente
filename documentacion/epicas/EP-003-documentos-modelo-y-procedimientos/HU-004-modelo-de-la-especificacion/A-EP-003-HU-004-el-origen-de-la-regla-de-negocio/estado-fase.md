# Estado de fase — Fase «A-EP-003-HU-004-el-origen-de-la-regla-de-negocio» (módulo «Documentos modelo»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-003-HU-004-el-origen-de-la-regla-de-negocio` |
| **Módulo** | Documentos modelo (`plantillas/plantilla-spec-modulo.md`) |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-004](../HU-004-modelo-de-la-especificacion.md) · [pendiente 43](../../../../../pendientes/hecho/el-origen-de-la-regla-de-negocio.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resuelva esos 8, recuerde que deben pertenecer a una HU» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no preguntar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó las ocho | ☑ |
| 6 | Ejecución continua | 5 tareas, una corregida | ☑ |
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
| **CA cumplidos** | 1 de 1 |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | El `CA-04` en la HU-004 |
| T-02 | Hecha | El §4 del modelo, con su nota |
| T-03 | Hecha | Comprobado con las dos reglas del caso real |
| T-04 | **Corregida** | Decía «cerrar el 43» y era prematuro: el pendiente pide además el validador, que es otra fase. Se cierra allá |
| T-05 | Hecha | `CHANGELOG` 22.0.0 y `VERSION` |

**Hechas:** 4 de 5; la quinta se corrigió por prematura, con el motivo escrito en el §4 del resultado.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Dos reglas que dicen casi lo mismo pueden tener procedencias distintas: una manda registrar y baja de un requisito, la otra manda no cerrar y no baja de nada. Con el molde viejo se veían igual de bien escritas | §2 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| El origen va en medio de la frase, no al final: ahí el hueco no se puede disimular | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Un cambio de plantilla puede ser MAYOR. Lo que decide no es el tamaño sino si obliga a un proyecto al día a hacer algo nuevo | §5 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |

---

## 3. Pendiente / preguntas abiertas

- **El pendiente 43 sigue abierto**, esperando la fase del validador en EP-004.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
