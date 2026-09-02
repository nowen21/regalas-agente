# Estado de fase — Fase A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas (módulo Documentos modelo)   ·   `[CAPA 3]`

> **Checkpoint del orquestador**: el estado persistido en cada puerta para sobrevivir a la compactación. Se actualiza en cada puerta que pasa.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas` |
| **Módulo** | Documentos modelo |
| **Planteamiento / Épica / HU** | [EP-003](../../epica.md) · [HU-011](../HU-011-el-inventario-de-funcionalidades.md) · [pendiente 74](../../../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md) |
| **Última actualización** | 2026-08-21 |

---

## 1. En qué estación va

**Estación actual:** 12 — Commit, esperando la autorización del usuario. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 2026-08-21: pendiente 74, caso semilla y capítulo `02` verificados |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ el orden lo acordó el usuario («siga», tras cerrar el 73) |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-003 existía; solo suma la HU a sus índices |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-08-21, «si» del usuario |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ los CA son la especificación (entregable documental y normativo) |
| 6 | Diseñador | diseño coherente | ☑ plan §2.6: ID `F26`, molde desde el semilla, MAYOR, veredicto de conducta antes que regla nueva del `01` |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-21, «si» del usuario (incluye el corte MAYOR y el ID F26) |
| 8 | Implementador | implementado + pruebas verdes | ☑ 2026-08-21: molde, regla y veredicto; 3 de 3 casos aprobados |
| 9 | Verificador | trazabilidad sin faltantes | ☑ 2026-08-21: cierre §2, 6 de 6 ítems y 8 de 8 tareas |
| 10 | Crítico | sin hallazgos graves | ☑ dos desvíos declarados (validar.py plantilla no valida moldes; el índice real era el mapa), sin efecto en el veredicto |
| 11 | Cierre documental + señales | docs y señales al día | ☑ 2026-08-21: cierre, versión 29.0.0, pendiente 74 en hecho/ con 9 avisos |
| 12 | Commit | 👤 autorizado | ✅ `60ff67e` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | — |
| **Defectos abiertos aceptados** | — |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-08 | Hechas | Detalle en el cierre §2.2 |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una sola HU para molde, regla y veredicto: el problema es uno (la puerta) y partirlo repetiría el hueco del pendiente 60 | Está en el plan §2.6; se evalúa señal al cerrar |

---

## 3. Pendiente / preguntas abiertas

- La autorización del commit (puerta 12), que se pregunta aparte.

---

## 4. Si se bloqueó

No está bloqueada: terminó su cierre documental y espera el commit.
