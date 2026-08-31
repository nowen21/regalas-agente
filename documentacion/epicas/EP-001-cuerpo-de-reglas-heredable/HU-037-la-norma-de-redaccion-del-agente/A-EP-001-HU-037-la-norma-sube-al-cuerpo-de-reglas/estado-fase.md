# Estado de fase — Fase `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` |
| **Módulo** | Cuerpo de reglas |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [HU-037](../HU-037-la-norma-de-redaccion-del-agente.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se comprobó que la regla no existía |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-30 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ **El alcance lo decidió el usuario**: todo documento, y también el chat |
| 6 | Diseñador | diseño coherente | ✅ Va en el capítulo donde ya viven las reglas de cómo escribe el agente |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ `metareglas` sin incumplimientos |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ✅ `83d874a` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | CA-01 y CA-03 enteros; el CA-02, en la mitad que se podía tocar |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | El modelo de manual de usuario no cita la regla todavía: tiene cambios sin guardar de otra sesión |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · decidir el alcance con el usuario | Terminada | Todo documento, y también el chat |
| T-02 · escribir la regla con su checklist | Terminada | CP-001 |
| T-03 · clasificarla, diciendo qué mitad no se comprueba | Terminada | CP-002 |
| T-04 · que los modelos la citen en vez de repetirla | Terminada a medias | CP-003 |

**Hechas:** 3 de 4, y la cuarta a medias por un archivo ajeno.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Dónde queda |
|---|---|
| La regla rige también lo que el agente contesta en el chat | El cuerpo de la regla |
| Una norma escrita dentro de un documento modelo solo la hereda quien llene ese modelo | §4.1 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.
- Que el modelo de manual de usuario cite la regla, cuando la otra sesión suelte el archivo.

---

## 4. Si se bloqueó

No se bloqueó. La mitad que falta es de un archivo que otra sesión tiene en curso.
