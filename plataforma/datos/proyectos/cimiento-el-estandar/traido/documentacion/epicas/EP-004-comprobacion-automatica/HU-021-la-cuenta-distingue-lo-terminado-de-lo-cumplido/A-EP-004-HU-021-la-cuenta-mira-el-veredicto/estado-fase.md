# Estado de fase — Fase `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` (módulo Programas de comprobación)   ·   `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó, se cerró y se publicó el mismo 2026-08-27, y **este documento se quedó siendo la plantilla en blanco**. Lo destapó la [HU-022](../../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md), que se construyó **para esto**.
>
> **No se inventa nada:** todo sale del [plan_trabajo.md](plan_trabajo.md), del [resultado_pruebas.md](resultado_pruebas.md) y del [cierre](funcionalidad_implementada.md), que sí se escribieron. **Este documento es un seguimiento en vivo, y en vivo no se llevó** — se deja dicho en vez de fingir que sí.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `735d00c`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-27 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 417 de 417 |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 13 tareas, 13 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Seis sabotajes, seis cazados |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-055` |
| 12 | Commit | 👤 autorizado | ✅ `735d00c` |
| 13 | Publicación / despliegue | 👤 autorizado | ✅ Publicada el 2026-08-27 |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` corregido |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1.2 Avance de las tareas del plan

> **Consolidado al cerrar, no llevado en vivo.** Sale del §2.2 del [cierre](funcionalidad_implementada.md).

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · el campo de veredicto en el molde del cierre | Terminada | Antes ofrecía `Cumple / Cumple con observaciones` |
| T-02 · quitar de los tres moldes la prohibición | Terminada | La regla decía lo contrario de lo que se hace |
| T-03 · leer el veredicto del resultado | Terminada | `veredicto_de` |
| T-04 · contar las tres | Terminada | `por_veredicto` |
| T-05 · que la línea las diga | Terminada | Se entiende sin documentación |
| T-06 a T-09 · las pruebas | Terminada | 14 pruebas nuevas |
| T-10 · medir antes de escribir | Terminada | Los dos números en el `CHANGELOG` |
| T-11 a T-12 · versionar | Terminada | `35.2.0` |
| T-13 · sabotear | Terminada | Seis, seis cazados |

**Hechas:** 13 de 13. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un número de avance necesita una prueba que lo contradiga | [`S-055`](../../../../senales.md) |
| El veredicto se lee del resultado, que es quien lo produce | `S-055` |
| Lo que no se puede leer se cuenta aparte, no se reparte | `S-038` |

---

## 3. Pendiente / preguntas abiertas

Ninguna de esta fase. Lo que dejó abierto está en el §6 del cierre: **las historias que no cumplen y las que no dicen si cumplen**, ahora visibles.

**Y el defecto que esta fase no vio:** su lector reconocía dos de las tres formas del veredicto. Se corrigió en la fase [`B`](../B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas/funcionalidad_implementada.md), y lo que quedaba en la [`C`](../C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee/funcionalidad_implementada.md).

---

## 4. Si se bloqueó

No se bloqueó.

**Y esta fase es su propio ejemplo:** al crearla con el andamio, la `HU-021` contaba como terminada **antes de escribir una línea**. Está en `S-055` y es lo que disparó la `HU-022`.
