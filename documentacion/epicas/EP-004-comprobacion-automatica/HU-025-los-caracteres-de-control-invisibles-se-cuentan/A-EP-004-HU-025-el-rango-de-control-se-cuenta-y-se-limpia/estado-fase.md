# Estado de fase — Fase `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-025-el-rango-de-control-se-cuenta-y-se-limpia` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-025](../HU-025-los-caracteres-de-control-invisibles-se-cuentan.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se contó el árbol antes de tocar nada |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-30 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ Los tres criterios |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 5 pruebas nuevas, 5 en verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ✅ `91c7d2a` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · contar el rango completo | Terminada | CP-002 |
| T-02 · que la limpieza los quite | Terminada | CP-004 |
| T-03 · la fila en el anexo, para que la lista y el programa digan lo mismo | Terminada | El anexo |
| T-04 · limpiar los archivos que ya lo traían | Terminada | CP-005 |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Dónde queda |
|---|---|
| Se barre el rango, no los que fueron apareciendo | §4.1 del resultado |
| El histórico no se reescribe, ni la copia de la plataforma | §4.2 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó.
