# Estado de fase — Fase `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) |
| **Última actualización** | 2026-08-27 |

---

## 1. En qué estación va

**Estación actual:** 13 · Publicación. **Última puerta pasada:** 12, en `fce6e41`.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-08-27 |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 7 tareas, 7 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ Cuatro sabotajes |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `S-058` |
| 12 | Commit | 👤 autorizado | ✅ `fce6e41` |
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
| T-01 · el patrón del título exacto | Terminada | `_VEREDICTO_TITULO_SOLO` |
| T-02 · un caso por título que sí se lee | Terminada | 3 pruebas |
| T-03 · que **no** lea «por criterio de aceptación» | Terminada | Es el caso crítico: 40 fases lo escriben así |
| T-04 · que **no** lea `final` ni los otros dos | Terminada | 3 pruebas |
| T-05 · medir, y nombrar las diez | Terminada | Siete a «cumplen», **tres a «no cumplen»** |
| T-06 · las 22 de `A` y `B`, sin tocarlas | Terminada | Pasan sin cambio |
| T-07 · sabotear | Terminada | Cuatro, con su resultado en el §4.1 |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Contar las formas que uno ya reconoce no es enumerarlas | [`S-058`](../../../../senales.md) |
| Un patrón más ancho que el hecho no falla hoy, y es el mismo error de mañana | `S-058` |
| Recuperar solo lo que cumple deja el número mejor y más falso | `S-058` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del `push`**, que se pide aparte del commit.
- **Las cinco fases que de verdad no dicen si cumplen**, y **los tres «No cumple» que aparecieron**. No son de esta fase: cada uno es trabajo propio.

---

## 4. Si se bloqueó

No se bloqueó.

**Y algo que conviene dejar dicho:** abrir esta fase movió la línea antes de escribir una sola prueba. Al crear su carpeta, la `HU-021` salió de «terminadas» — de `57 cumplen` a `56`. Es `S-053` por **cuarta** vez en el día, y queda como evidencia en el [pendiente 88](../../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md).
