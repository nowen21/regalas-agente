# Estado de fase — Fase `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `b194424`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ 425 de 425 |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 7 tareas, 7 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ 4 sabotajes, 4 cazados |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-056` |
| 12 | Commit | 👤 autorizado | ✅ `b194424` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 — el `CA-03`, más la no regresión transversal |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · reconocer la forma bajo el encabezado | Terminada | `_VEREDICTO_BAJO_TITULO` |
| T-02 · seguir exigiendo el encabezado | Terminada | Es el riesgo real: ampliar sin aflojar |
| T-03 · un caso por forma | Terminada | 4 pruebas |
| T-04 · un caso de que **no** lea | Terminada | 4 pruebas |
| T-05 · medir antes y después | Terminada | Y destapó que la base se había movido |
| T-06 · las 14 de la fase `A`, sin tocarlas | Terminada | Pasan sin cambio |
| T-07 · sabotear | Terminada | 4 de 4 al primer intento |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un criterio de parada con número exacto caza lo que uno redondeado deja pasar | [`S-056`](../../../../senales.md) |
| Abrir una fase para arreglar un conteo le agrega un caso al conteo | `S-056`, y es `S-053` por tercera vez |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del `push`**, que se pide aparte del commit.

---

## 4. Si se bloqueó

No se bloqueó. **Se suspendió una vez**, por el criterio del plan §4.3: las «no dicen» bajaron seis y el plan exigía siete exactas. Se investigó, se encontró que la base de medición se había movido, y se reanudó. Está contado en el §4.2 del resultado.
