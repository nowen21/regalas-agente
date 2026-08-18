# Estado de fase — Fase «B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive» (módulo «Enlaces y citas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive` |
| **Módulo** | Enlaces y citas (`validadores/enlaces.py`) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-005](../HU-005-enlaces-y-citas.md) · [pendiente 18](../../../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md), que **sigue abierto** |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «siga» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no informar entre unidades | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo | ☑ |
| 6 | Ejecución continua | 5 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | va con la decisión sobre el vecino | ☐ |
| 11 | Publicación / despliegue | 👤 falta el `push` | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `RN-03` en su parte reparable — 284 de 284 |
| **Defectos abiertos aceptados** | dos: el vecino de la misma carpeta, y el punto ciego de las comillas invertidas |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | 1031 hoy · 747 vecinos · 284 entre carpetas |
| T-02 | Hecha | `reparar_formato`, con el criterio compartido |
| T-03 | Hecha | 14 casos; **encontraron dos defectos antes de tocar el repositorio** |
| T-04 | Hecha | 284 aplicados, cero enlaces rotos |
| T-05 | Hecha | El 18 al día |

**Hechas:** 5 de 5.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **Una regla puede tener razón en el caso para el que se escribió y volverse contraproducente en el que no se miró — y eso solo se ve aplicándola** | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| **El que reporta y el que arregla comparten el criterio**, o el arreglo deja hallazgos vivos y toca lo que nadie pidió | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| **El destino de un enlace no se toca nunca:** es lo único que puede romper uno que hoy funciona | `CP-002` |
| **Una exclusión que se cuenta contra la raíz equivocada funciona hasta el día que no.** En el repositorio real las dos coinciden | §3 del [`resultado_pruebas.md`](resultado_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Si `DOC14` exceptúa al vecino de la misma carpeta.** 747 enlaces esperan. La puerta está abierta: `reparar_formato(incluir_vecinos=True)`.
- **El punto ciego de las comillas invertidas**, que vive en `comun.enlaces()` y toca a todo el repositorio.
- **El punto 3 del 18** — si el validador entra en la corrida diaria.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó. **Se revirtió una vez**, a propósito y por completo — ver §4 del resultado.
