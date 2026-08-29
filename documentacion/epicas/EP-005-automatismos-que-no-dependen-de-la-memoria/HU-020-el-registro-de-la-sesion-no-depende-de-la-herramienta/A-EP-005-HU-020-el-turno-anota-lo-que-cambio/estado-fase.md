# Estado de fase — Fase `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` (módulo Enganches)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` |
| **Módulo** | Enganches |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-020](../HU-020-el-registro-de-la-sesion-no-depende-de-la-herramienta.md) |
| **Última actualización** | 2026-08-28 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (la redacción de los CA es la especificación funcional, `02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `e8c4495` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5, más los 2 requisitos no funcionales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Los tres de §4 quedaron corregidos y verificados dentro del ciclo 1 |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 | Terminada | 11 pruebas miran el registro; **ninguna fija su contenido exacto**, así que se podía tocar |
| T-01 | Terminada | Medido: `git status --porcelain` da ` M`, ` D` y `??`; los ignorados **no se piden a propósito** |
| T-02 | Terminada | `_estado_de_git` y `cambios_del_turno` |
| T-03 | Terminada | `anotar_el_turno`, apoyado en `anotar`, que ya no duplicaba |
| T-04 | Terminada | `adaptadores/claude-code/hook_turno.py` |
| T-05 | Terminada | Colgado como enganche de `Stop` en `instalar.HOOKS_CLAUDE` |
| T-06 | Terminada | **0 de 12 commits avisarían**, contra 7 de 12 del diseño descartado |
| T-07 | Terminada | 15 pruebas, clase `ElTurnoAnotaLoQueCambio` |
| T-08 | Terminada | Corrido sobre este repositorio: turno 1 sin reclamar nada, turno 2 anotó lo del guion |
| T-09 | Terminada | `VERSION` a `35.8.0` y su entrada en el `CHANGELOG` |
| T-10 | Terminada | **7 sabotajes, 7 cazados** — dos se colaron primero y destaparon tres defectos |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un archivo que ninguna sesión registró **no parece de otro: parece de nadie**, y por ahí entró lo ajeno | [`S-071`](../../../../senales.md) |
| El hueco por el que entró lo ajeno es el mismo por el que pasa casi todo lo propio: afinar la comprobación habría hablado en 7 de 12 commits | [`S-072`](../../../../senales.md) |
| **Una clase de pruebas en verde no dice nada sobre las de al lado**: una aserción quedó pegada en la prueba de otro enganche y la clase sola no lo vio | `S-073` |
| **Un sabotaje que se cuela sin razón aparente suele señalar código muerto**, no una prueba floja: el `os.utime` que rompí no hacía nada | `S-074` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del commit.** El cambio está listo y leído; falta que el usuario autorice guardarlo (estación 12).

---

## 4. Si se bloqueó

No se bloqueó.
