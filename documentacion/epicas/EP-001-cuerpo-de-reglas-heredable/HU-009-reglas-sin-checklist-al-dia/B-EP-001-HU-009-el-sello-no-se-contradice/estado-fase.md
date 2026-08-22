# Estado de fase — Fase «B-EP-001-HU-009-el-sello-no-se-contradice» (módulo «Cuerpo de reglas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-001-HU-009-el-sello-no-se-contradice` |
| **Módulo** | Cuerpo de reglas — los bloques de checklist de `base/` |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) · [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que **sigue abierto** |
| **Última actualización** | 2026-08-18 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resuelva los p0,p1,p2,p3» · «necesito la tarea completada» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pidió no informar entre unidades de la misma orden | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo sobre el 19 | ☑ |
| 6 | Ejecución continua | 8 tareas | ☑ |
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
| **CA cumplidos** | el `CA-01` en su parte comprobable, y el transversal de no regresión |
| **Defectos abiertos aceptados** | uno: las 72 reglas que reprueban, fuera del alcance declarado |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

**Esta fase corrige el sello, no la regla.** Está declarado desde el §1 del plan y no la vuelve una fase a medias: son dos trabajos distintos y el segundo es el pendiente 19 entero.

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | 5 se contradicen · 10 con los totales mal · 1 con dos sellos |
| T-02 | Hecha | `_sello_se_contradice` |
| T-03 | Hecha | `_totales_del_sello` |
| T-04 | Hecha | `_un_solo_sello` |
| T-05 | Hecha | `C10`, `C15`, `C16`, `D1`, `D4` |
| T-06 | Hecha | Los diez, recalculados desde su tabla |
| T-07 | Hecha | 15 casos, y las dos suites en verde |
| T-08 | Hecha | `CHANGELOG` 23.7.2, `VERSION`, y el 19 al día |

**Hechas:** 8 de 8.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **La comprobación se escribe antes de corregir.** Al revés se estrena sobre un cuerpo limpio: cero hallazgos y ninguna forma de saber si sirve | §4 del [`funcionalidad_implementada.md`](funcionalidad_implementada.md) |
| **Una comprobación que reporta de más se apaga a la semana**, y apagada no encuentra nada. La mitad de los casos son de silencio | §4 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Un bloque de siete casillas sin encabezado por columna se transcribe mal.** Cuatro de los cinco errores fueron una casilla corrida en el bloque `C` | §3 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Cuando las dos mitades de un sello discrepan, **manda el texto**: es la que razona. La tabla es su resumen | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |

---

## 3. Pendiente / preguntas abiertas

- **Las 72 reglas en NO CUMPLE.** Es el pendiente 19 entero, y esta fase no toca ninguna: lo único que cambió es que cinco de ellas ya dicen bien cuántas filas les fallan.
- **Que el bloque `C` se siga transcribiendo mal.** Hoy lo agarra la comprobación después de escrito. Escribir el sello a partir de la tabla, en vez de a mano, sería el paso siguiente — y todavía no hay datos de si hace falta.
- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

---

## 4. Si se bloqueó

No se bloqueó.
