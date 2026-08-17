# Estado de fase — Fase «A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen» (módulo «Programas de comprobación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen` |
| **Módulo** | Programas de comprobación (`validadores/plantillas.py`) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-004](../HU-004-forma-de-los-documentos.md) · [pendiente 43](../../../../../pendientes/hecho/el-origen-de-la-regla-de-negocio.md) |
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
| **CA cumplidos** | 1 de 1 |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | El `CA-04` en la HU-004 |
| T-02 | Hecha | `spec` en la tabla de moldes |
| T-03 | Hecha | `reglas_sin_origen()`, cuarta comprobación |
| T-04 | Hecha | Tres casos, con las dos reglas reales |
| T-05 | Hecha | Vistos en rojo con la comprobación desactivada |
| T-06 | Hecha | `validadores/docs/plantillas.md` |
| T-07 | Hecha | El 43 cerrado, y lo que dejó abierto en un pendiente nuevo |
| T-08 | Hecha | `CHANGELOG` 22.1.0 y `VERSION` |

**Hechas:** 8 de 8.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un `spec.md` no se comparaba contra ninguna plantilla: el módulo más importante del proyecto era invisible para el validador de forma | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| La comprobación se ata al molde y no al título de la sección: un `## 4. Reglas de negocio` en otro documento puede querer decir otra cosa | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Se pide un identificador y no una frase, porque una frase no se puede seguir hasta ninguna parte | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El validador nuevo destapó 31 incumplimientos del propio estándar, y no se apagó para que el número diera cero | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Las 31 reglas sin origen** de las dos especificaciones de este repositorio, en su pendiente propio.
- **Comprobar que el identificador exista de verdad**, que es trazabilidad y es otra fase.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
- **Avisarle a `shopnest-mesa`**, que reportó el 43 y tiene su pendiente de seguimiento abierto.

---

## 4. Si se bloqueó

No se bloqueó.
