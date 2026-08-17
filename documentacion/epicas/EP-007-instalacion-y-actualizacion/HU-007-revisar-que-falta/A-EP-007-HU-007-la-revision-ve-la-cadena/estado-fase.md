# Estado de fase — Fase «A-EP-007-HU-007-la-revision-ve-la-cadena» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-007-HU-007-la-revision-ve-la-cadena` |
| **Módulo** | Instalación (`validadores/checklist.py`) |
| **Épica / HU / origen** | [EP-007](../../epica.md) · [HU-007](../HU-007-revisar-que-falta.md) · [pendiente 30](../../../../../pendientes/hecho/la-revision-ve-la-cadena.md) |
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
| 6 | Ejecución continua | 7 tareas, con una ampliación | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 2 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | va en el reporte de las ocho | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

**La fase se detuvo una vez, en la estación 7.** El `CP-001` buscaba la palabra «completa» para afirmar que el resumen **no** decía que estaba completa — y «incompleta» la contiene, así que daba rojo contra un resumen correcto. Se corrigió el caso y se volvió a correr.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **Defectos abiertos aceptados** | ninguno. Los dos eran de las pruebas |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | La fila del punto, con la nota de que no lo instala nadie |
| T-02 | Hecha | `_cadena()` y su entrada en el mapa |
| T-03 | Hecha | Tres casos |
| T-04 | Hecha | Rojos al quitar la fila de la lista |
| T-05 | Hecha | `validadores/docs/checklist.md` |
| T-06 | Hecha | El 30 cerrado |
| T-07 | Hecha | `CHANGELOG` 23.0.0 y `VERSION` |
| **Ampliación** | Hecha | `test_instalar_reparar.py`: su `CP-004` exigía cero faltantes tras instalar, y el punto nuevo no lo instala nadie |

**Hechas:** 7 de 7, más una ampliación de plan.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Lo que faltaba no era dejar el planteamiento puesto: era **decir que falta**. Copiar la plantilla cruda lo habría dado por cumplido | §1 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| Un punto de la revisión puede no ser instalable, y eso hay que escribirlo en su propia fila o alguien va a correr el instalador esperándolo | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Buscar una palabra para negar una frase falla cuando la palabra vive dentro de su contrario: «incompleta» contiene «completa» | `DEF-01` del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Agregar un punto que nadie instala rompe toda prueba que afirme «después de instalar no falta nada» | `DEF-02` del [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Este repositorio no tiene planteamiento** y reprueba su propio punto nuevo. Escribirlo es decidir qué es este proyecto.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
- **Avisarle a `shopnest-mesa`**, que lo reportó.

---

## 4. Si se bloqueó

No se bloqueó.
