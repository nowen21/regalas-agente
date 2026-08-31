# Estado de fase — Fase `B-EP-006-HU-004-degradar-sin-el-modelo` (módulo Memoria)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-004-degradar-sin-el-modelo` |
| **Módulo** | Memoria |
| **Planteamiento / Épica / HU** | [EP-006](../../epica.md) · [HU-004](../HU-004-busqueda-por-significado.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

**Estuvo detenida trece días en la estación 4**, con su plan y su plan de pruebas escritos y sin aprobar. El usuario la aprobó el 2026-08-30 y la fase se ejecutó ese mismo día.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ La fase `A` dejó el defecto probado |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ El CA no cambia |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ Escritos el 2026-08-17, aprobados el 2026-08-30 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 59 pruebas de la memoria, 59 en verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | El CA-02, sin el modelo la búsqueda sigue funcionando |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · atrapar el fallo al cargar o al indexar | Terminada | CP-002 |
| T-02 · seguir con lo léxico | Terminada | CP-002 |
| T-03 · decirlo en el modo, sin callarlo | Terminada | CP-002 |
| T-04 · destapar la prueba | Terminada | 59 en verde |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Dónde queda |
|---|---|
| Un defecto que la fase anterior dejó probado con fallo esperado se arregla y se destapa, no se borra | §4 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. Estuvo esperando una aprobación, que es distinto.
