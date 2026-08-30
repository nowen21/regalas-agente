# Estado de fase — Fase `B-EP-002-HU-001-el-numero-repetido-se-declara` (módulo Versionado y adopción)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-002-HU-001-el-numero-repetido-se-declara` |
| **Módulo** | Versionado y adopción |
| **Planteamiento / Épica / HU** | [EP-002](../../epica.md) · [HU-001](../HU-001-numero-de-version-y-que-significa.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyeron las dos entradas `15.4.0` y el pendiente 22 |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30, sobre la propuesta escrita |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ La lectura del CA-01, acordada en esta sesión |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 5 pruebas de la clase, 5 en verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 3 tareas, 3 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el CA-01 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · leer qué exige el CA-01 y qué decidió el registro | Terminada | El registro decidió no renumerar, y dice por qué |
| T-02 · que la prueba exija lo que se sostiene | Terminada | Sale del fallo esperado |
| T-03 · probar el repetido callado | Terminada | Sin eso, la prueba nueva pasa con cualquier registro |

**Hechas:** 3 de 3. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Una prueba que exige lo que se decidió no cumplir no mide nada: enseña a ignorarla | Este cierre, §5 |
| El número repetido no se renumera, se declara | Registro del 2026-08-15 |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó.
