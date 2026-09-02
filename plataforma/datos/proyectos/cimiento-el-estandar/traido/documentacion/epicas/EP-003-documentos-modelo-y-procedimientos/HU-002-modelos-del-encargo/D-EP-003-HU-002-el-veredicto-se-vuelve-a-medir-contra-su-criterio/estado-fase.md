# Estado de fase — Fase `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` (módulo Documentos modelo)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` |
| **Módulo** | Documentos modelo |
| **Planteamiento / Épica / HU** | [EP-003](../../epica.md) · [HU-002](../HU-002-modelos-del-encargo.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `b3df9f1`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-27 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ No se toca código |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ✅ `b3df9f1` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 — el `CA-01`, medido contra lo que pide |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` corregido |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · los tres modelos existen | Terminada | — |
| T-02 · recorrer la cadena **corriéndola** | Terminada | **Falló en el ciclo 1**, y ahí estuvo el hallazgo |
| T-03 · el hueco que la `A` señaló | Terminada | Ya no existe: el planteamiento está escrito |
| T-04 · declarar el veredicto y dónde se cobraba | Terminada | — |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un veredicto puede estar mal el día que se escribe, no solo envejecer | [`S-063`](../../../../senales.md) |
| Una historia se crea y nadie vuelve a la tabla de su épica | [`S-064`](../../../../senales.md) |
| Una medición vieja no es una medición: se corre, no se cita | `S-064` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del `push`**, que se pide aparte del commit.

---

## 4. Si se bloqueó

**Se suspendió una vez**, por el criterio del plan §4.3: la cadena falló al correrla. `EP-001` no listaba la `HU-036`.

**Se paró, se reportó, y el usuario amplió el alcance** para arreglar la fila en vez de anotarla: *«¿para qué dejar pendientes si se puede solucionar?»*. Con la cadena en cero, el `CA-01` se pudo medir.
