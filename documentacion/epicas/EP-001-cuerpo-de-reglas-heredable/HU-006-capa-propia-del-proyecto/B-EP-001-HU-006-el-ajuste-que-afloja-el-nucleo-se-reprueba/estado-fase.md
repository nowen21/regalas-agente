# Estado de fase — Fase `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [HU-006](../HU-006-capa-propia-del-proyecto.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyó la fase `A` y su defecto `D-03` |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA-03 |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 2 pruebas nuevas, las dos en verde |
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
| **CA cumplidos** | 1 de 1, el CA-03 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno nuevo. Siguen abiertos el `D-01` y el `D-02` de la fase `A`, que son de otro asunto |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · provocar el caso en una carpeta temporal | Terminada | Cero hallazgos: el rojo era cierto y seguía siéndolo |
| T-02 · hacer que la comprobación lo vea | Terminada | `_afloja_una_blindada`, en `metareglas.py` |
| T-03 · probar el caso malo y el bueno | Terminada | 2 pruebas, las dos en verde |
| T-04 · declarar el veredicto que deja atrás | Terminada | §0 del cierre |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Una regla escrita y no aplicada donde importa es una regla que no rige | `S-061` |
| Se mira el verbo con que la regla declara su respaldo, no la intención | §5 del cierre |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó.
