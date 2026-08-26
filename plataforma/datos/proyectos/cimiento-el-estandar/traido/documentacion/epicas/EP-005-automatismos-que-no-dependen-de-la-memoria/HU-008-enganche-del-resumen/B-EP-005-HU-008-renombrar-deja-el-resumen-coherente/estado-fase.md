# Estado de fase — Fase «B-EP-005-HU-008-renombrar-deja-el-resumen-coherente» (módulo «Histórico»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-008-renombrar-deja-el-resumen-coherente` |
| **Módulo** | Histórico (`validadores/historico.py`) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-008](../HU-008-enganche-del-resumen.md) · [pendiente 35](../../../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 10 — reporte al usuario. **Última puerta pasada:** 9, commit `9ea5a5b`.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resulva esos 8, recuerde que deben pertenecer a una HU» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | se presentaron los dos y se esperó | ☑ |
| 5 | Aprobación del plan detallado | 👤 «arranque» | ☑ |
| 6 | Ejecución continua | 7 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ con una deuda: los nueve enlaces del §3 |
| 9 | Commit único | 👤 autorizado · `9ea5a5b`, 19 archivos | ☑ |
| 10 | Reporte al usuario | hash, resumen y estado | ☑ |
| 11 | Publicación / despliegue | 👤 **acá está detenida** — falta el `push` | ☐ |

**El commit se hizo con los nueve enlaces rotos puestos.** Se reportaron antes y el usuario pidió commitear igual; quedan escritos en el §3 y en el resumen de la sesión, no se perdieron.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 (el `CA-04`, que nació con esta fase) |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | El `CA-04` en la HU-008, con su tarea técnica, su fila en §8 y la bitácora |
| T-02 | Hecha | `_reenlazar()` en `historico.py`, llamada desde `_mover_resumen()` |
| T-03 | Hecha | `test_historico_renombrar.py`, tres casos |
| T-04 | Hecha | Revertido a propósito: CP-001 y CP-002 rojos, CP-003 verde |
| T-05 | Hecha | `validadores/docs/historico.md` |
| T-06 | Hecha | El 35 cerrado en `pendientes/hecho/` |
| T-07 | Hecha | `CHANGELOG` 21.3.0 y `VERSION` |

**Hechas:** 7 de 7.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un validador que termina en silencio y con código 0 sin comprobar nada es peor que ninguno: su silencio se lee como «todo bien». Pasó acá con `enlaces.py` | §4 y §7 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Cerrar un pendiente mueve su archivo y rompe todo lo que lo citaba. Es el mismo defecto que esta fase acaba de cerrar para las sesiones, un piso más arriba | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Corregir el enlace sin corregir su texto visible deja un enlace que abre y miente | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |

---

## 3. Pendiente / preguntas abiertas

- **La ampliación de plan ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).** Cerrar el 35 dejó enlaces rotos en cuatro archivos que el plan no declara: [`pendientes/36`](../../../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md) y tres resúmenes del 2026-08-16. Presentada al usuario, esperando el OK.
- **Los dos hallazgos del §4 del resultado** no tienen pendiente propio todavía.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
- **Avisarle a `shopnest-mesa`**, que tiene su pendiente de seguimiento abierto esperando este cierre.

---

## 4. Si se bloqueó

No está bloqueada: está esperando una decisión de una línea.
