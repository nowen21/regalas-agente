# Estado de fase — Fase A-EP-002-HU-006-quien-manda-sobre-la-version (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-006-quien-manda-sobre-la-version` |
| **Módulo** | Versionado y adopción — el acuerdo sobre quién toca [`VERSION`](../../../../../VERSION) y el [`CHANGELOG`](../../../../../CHANGELOG.md) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-006](../HU-006-quien-sube-la-version.md) · ✨ funcionalidad nueva, bajada del pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md). Fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único, **pendiente de autorización**. **Última puerta pasada:** 8, el cierre documental del 2026-08-18. Los dos criterios quedaron en **cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 7 tareas · hechas el 2026-08-18 | ☑ |
| 7 | Pruebas | [`resultado_pruebas`](resultado_pruebas.md) · **Cumple** | ☑ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Ejecutada y cerrada el 2026-08-18.** Nació [`20·M18`](../../../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md) —lo compartido se relee al escribirlo— y su comprobación, [`validadores/numeracion.py`](../../../../../validadores/numeracion.py).

> **Lo único que falta es la autorización del commit**, que se pide aparte de la aprobación del cambio.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Tres: la ventana de segundos que queda abierta, la entrada perdida que no se detecta, y que elegir el número al guardar es un hábito y no se puede comprobar con un programa |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) · 19 casos automatizados y una simulación con dos copias |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `20·M18`, en su forma general —duda 2— y con su checklist en **CUMPLE** |
| T-02 | Hecha | `M10` **no se toca**: `M18` la extiende, no la deroga. Nada de lo que `M10` exige deja de exigirse |
| T-03 | Hecha | Simulación con dos copias y origen desnudo — y con el contraste de no aplicar la regla |
| T-04 | Hecha | Cada copia subió lo suyo, en las dos corridas |
| T-05 | Hecha | Los casos ocurridos, y uno más: el rastro de la `15.4.0` repetida |
| T-06 | Hecha | El recuento destapó el hallazgo: sin la regla **se pierde una entrada**, y eso no se ve |
| T-07 | Hecha | Clasificada, versionada en la 23.11.0, pendiente 22 cerrado |

**Hechas:** 7 de 7.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Los cuatro casos ocurridos van al resultado como evidencia: una regla de convivencia sin los casos que la motivaron se vuelve a discutir cada vez | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El tramo de las dos numeraciones no se corrige: el registro es rastro, y renumerar rompe toda cita hecha a esas versiones | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La regla se valida contra el 2026-08-14, no contra sí misma: si aplicada a ese día no resuelve el cruce, no sirve | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| Si la regla no se puede comprobar con un programa, se declara así: una regla honesta sobre lo que no comprueba vale más que una comprobación falsa | Riesgo `R-03` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit.** Es lo único.

---

## 4. Si se bloqueó

**No quedó bloqueada.** Estuvo detenida desde el 2026-08-17 por las tres dudas de §2.7 del plan; se decidieron el 2026-08-18 en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) y la fase corrió entera el mismo día.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18** — salida 1 del pendiente 22: el número se sube al guardar. La decisión está escrita en el propio plan, con su motivo.

**Y lo que salió de ejecutarla vale más que la decisión:** la simulación mostró que el cruce se rompe de **dos** maneras, no de una. El número repetido deja rastro; la entrada perdida, no. Eso está en la §3 del [`resultado_pruebas.md`](resultado_pruebas.md).
