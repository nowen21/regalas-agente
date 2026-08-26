# Estado de fase — Fase «B-EP-007-HU-001-prepara-su-propia-salida» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-007-HU-001-prepara-su-propia-salida` |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Épica / HU / origen** | [EP-007](../../epica.md) · [HU-001](../HU-001-instalar-con-una-linea.md) · [pendiente 45](../../../../../pendientes/hecho/instalar-prepara-su-propia-salida.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 10 — reporte al usuario. **Última puerta pasada:** 9, commit `1b01451`.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «cree el nuevo y de una soluciónelo» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | el usuario pidió no parar entre plan y ejecución | ☑ |
| 5 | Aprobación del plan detallado | 👤 en el mismo mensaje que la disparó | ☑ |
| 6 | Ejecución continua | 6 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 2 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 autorizado · `1b01451`, 17 archivos | ☑ |
| 10 | Reporte al usuario | hash, resumen y estado | ☑ |
| 11 | Publicación / despliegue | 👤 **acá está detenida** — falta el `push` | ☐ |

**La fase se detuvo una vez, en la estación 7.** El CP-001 pasaba en verde con el arreglo revertido: instalaba en carpeta vacía, y esa corrida nunca imprime una flecha. Lo destapó el CP-002, que existe para eso. Se corrigió el caso y se volvió a correr.

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
| T-01 | Hecha | `instalar()` llama a `preparar_salida()` al entrar |
| T-02 | Hecha | `PreparaSuPropiaSalida` en `test_instalar_reparar.py` |
| T-03 | Hecha | El rodeo de la fase anterior, quitado |
| T-04 | Hecha | `validadores/docs/instalar.md` |
| T-05 | Hecha | El 45 cerrado |
| T-06 | Hecha | `CHANGELOG` 21.2.1 y `VERSION` |

**Hechas:** 6 de 6.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Una prueba de robustez que nunca se vio fallar no se sabe si comprueba algo. El CP-002 la obligó a fallar y destapó que el escenario no reproducía el defecto | Queda en el `DEF-01` del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Un programa que sabe imprimir tiene que saber preparar su salida; delegarlo en quien lo llame le pide al de afuera que conozca las tripas del de adentro | Queda en el §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
- **Los demás validadores no se revisaron.** Si alguno tiene el mismo hueco, es otro pendiente — está declarado fuera de alcance en el §1 del plan.

---

## 4. Si se bloqueó

No está bloqueada.
