# Estado de fase — Fase «C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible» (módulo «Enganche del resumen»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible` |
| **Módulo** | Enganche del resumen (`validadores/resumen.py`, `validadores/hook_resumen.py`) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-008](../HU-008-enganche-del-resumen.md) · defecto del `CA-02`, que la fase [`A`](../A-EP-005-HU-008-enganche-del-resumen/) dio por cerrado |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «cumpla su tarea» · lo destapó el propio enganche | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no informar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo | ☑ |
| 6 | Ejecución continua | 5 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | va en el reporte del trabajo del día | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-02`, en el caso que no distinguía |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | 3 resúmenes fuera del molde, 29 hallazgos invisibles |
| T-02 | Hecha | `resumen.py` distingue `vacio` de `molde` |
| T-03 | Hecha | El aviso nuevo, antes del de vacío, diciendo cuántos hay |
| T-04 | Hecha | Los tres renumerados, después de escribir la comprobación |
| T-05 | Hecha | 9 casos, y las dos suites en verde |

**Hechas:** 5 de 5.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **Un aviso que se puede desmentir de un vistazo se deja de leer.** El programa no se equivocaba al mirar: al nombrar lo que vio | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Dos avisos, dos marcas.** Con una sola, avisar de uno apaga el otro para siempre — y el aviso se da una vez | §4 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Un silencio no deja rastro.** El resumen contado como vacío se ve igual que uno que lo está, y el aviso que no sale no aparece en ningún registro | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| **La forma equivocada se copió de una sesión a la siguiente porque nada la contradijo.** Tres resúmenes, la misma jornada | §3 del [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Que el próximo resumen se escriba bien no se puede forzar**, y es por diseño: escribir un hallazgo es criterio ([`13·DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
