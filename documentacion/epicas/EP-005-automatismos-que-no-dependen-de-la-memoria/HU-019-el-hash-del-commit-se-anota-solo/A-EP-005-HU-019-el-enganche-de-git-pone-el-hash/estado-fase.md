# Estado de fase — Fase `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` (módulo Enganches)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` |
| **Módulo** | Enganches |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-019](../HU-019-el-hash-del-commit-se-anota-solo.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ Salidas 1 y 3 del pendiente 87 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ 2026-08-27 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19` |
| 6 | Diseñador | diseño coherente | ✅ La duda 1, resuelta midiendo |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 500 de 500 |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 11 tareas, 11 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Cinco sabotajes, tres ciclos |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-066`, `S-067`, `S-068` |
| 12 | Commit | 👤 autorizado | ☐ **Esperando aprobación del usuario** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` a `DEF-04` corregidos |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 · impacto sobre las pruebas del instalador | Terminada | Ninguna compara la lista |
| T-01 · **resolver la duda 1 midiendo** | Terminada | El archivo queda sin guardar: `S-067` |
| T-02 · encontrar la fase que el commit cierra | Terminada | Por la forma del nombre, no por una lista |
| T-03 · escribir solo si hay fila, vacía y con cierre en git | Terminada | Tres condiciones |
| T-04 · el enganche, que nunca deshace un commit | Terminada | Termina en 0 pase lo que pase |
| T-05 · que el instalador lo cuelgue | Terminada | `post-commit` en `HOOKS` |
| T-06 · el conteo con sus tres grupos | Terminada | `22 · 1 · 106`, con nombres |
| T-07 · los cinco CA | Terminada | 16 pruebas, seis con git de verdad |
| T-08 · **correrlo commiteando** | Terminada | Escribe el hash correcto |
| T-09 · `CHANGELOG` y `VERSION` | Terminada | `35.6.0`, MENOR |
| T-10 · sabotear | Terminada | Cinco; el cuarto falló de dos formas distintas |

**Hechas:** 11 de 11. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Antes de automatizar el llenado de un campo, contar en cuántos documentos existe | [`S-066`](../../../../senales.md) |
| Un enganche que arregla algo después del commit no puede meterlo dentro de ese commit | [`S-067`](../../../../senales.md) |
| Un sabotaje que no se pudo aplicar no es un sabotaje que pasó | [`S-068`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del commit**, que se pide aparte de la aprobación del cambio.
- **Las 22 fases con la marca pendiente y las 106 sin la fila.** Se cuentan y se nombran; ponerlas al día se decide aparte.

---

## 4. Si se bloqueó

No se bloqueó, y **la duda declarada se resolvió midiendo antes de escribir código**: el hash no existe hasta que el commit está hecho, así que la anotación llega después y **el archivo queda sin guardar**. Las otras dos salidas rompían una regla — una se muerde la cola, la otra cruza `00·N1`.
