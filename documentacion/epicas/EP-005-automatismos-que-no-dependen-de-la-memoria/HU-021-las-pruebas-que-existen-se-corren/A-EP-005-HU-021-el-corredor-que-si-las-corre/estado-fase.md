# Estado de fase — Fase `A-EP-005-HU-021-el-corredor-que-si-las-corre` (módulo Pruebas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-021-el-corredor-que-si-las-corre` |
| **Módulo** | Pruebas |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-021](../HU-021-las-pruebas-que-existen-se-corren.md) |
| **Última actualización** | 2026-08-28 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (la redacción de los CA es la especificación funcional, `02·F19`) |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-28 |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `2a7bb85` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A — el estándar no se despliega |

> **La fila 12 estuvo marcada por error, y se corrigió a mano.** El enganche de `post-commit` la selló con `7d665b2` — el commit que **creó** esta carpeta. Ese commit no cerró la fase: la abrió. Queda anotado en §3 como defecto del enganche.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5, más los 2 requisitos no funcionales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-00 | Terminada | 61 verdes, 6 rojos, **con nombres** |
| T-01 | Terminada | **No rompió ninguno.** La subida a 5 fallas era de `corredor.py`, comprobado apartándolo |
| T-02 | Terminada | `validadores/corredor.py` · `650 prueba(s) en 67 archivo(s)` |
| T-03 | Terminada | Vacía, inexistente y sin pruebas: rojo en las tres |
| T-04 | Terminada | **Lo tumbó.** 9,6 min × 245 commits/14 días = 39,3 h. Se cuelga el reclamo |
| T-05 | Terminada | `pre-push`, línea 46, con `|| true` |
| T-06 | Terminada | Las dos suites en el `README`, con su tiempo |
| T-07 | Terminada | Uno cerrado, cinco enrutados a dos destinos |
| T-08 | Terminada | 22 pruebas, clase `LasPruebasQueExistenSeCorren` |
| T-09 | Terminada | Instalador corrido; el enganche real comprobado |
| T-10 | Terminada | `35.9.0` |
| T-11 | Terminada | **12 de 12 cazados**, tras corregir tres mal armados |

**Hechas:** 12 de 12. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Cuatro registros llevados a mano se quedaron atrás el mismo día; tres tenían comprobador y nadie lo corría | [`S-075`](../../../../senales.md) |
| **El enganche que sella la estación 12 no distingue el commit que cierra una fase del que la abre** | `S-076` |

---

## 3. Pendiente / preguntas abiertas

- **Defecto del enganche de la estación 12.** Marca como «commit autorizado» cualquier fase cuya carpeta toque el commit, aunque ese commit **la esté creando**. Acá se corrigió a mano; el arreglo va con su cadena, porque la fase que lo construyó es `A-EP-005-HU-019` y esto es su defecto, no el de esta.

---

## 4. Si se bloqueó

No se bloqueó.
