# Estado de fase — Fase `B-EP-007-HU-002-el-registro-de-version-se-anuncia` (módulo Instalación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-007-HU-002-el-registro-de-version-se-anuncia` |
| **Módulo** | Instalación |
| **Planteamiento / Épica / HU** | [EP-007](../../epica.md) · [HU-002](../HU-002-mostrar-antes-de-hacer.md) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyó el defecto `D-01` de la fase `A` y su prueba |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del CA-02 |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ 4 de 4 de la clase, sin fallos esperados |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ✅ `e048420` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el CA-02 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. El `D-02` de la fase `A` sigue abierto y no deja ningún CA en «No» |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · reproducir el defecto | Terminada | La prueba estaba escrita como fallo esperado desde el 2026-08-22 |
| T-02 · que la simulación mire la huella que va a quedar | Terminada | `_huellas_previstas`, en `instalar.py` |
| T-03 · que anuncie el archivo, no la carpeta | Terminada | `versiones.nombre_previsto` |
| T-04 · sacar la prueba del fallo esperado | Terminada | 4 de 4 en verde |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La simulación no mentía sobre lo que iba a hacer: se miraba en el espejo equivocado | Este cierre, §5 |
| Anunciar la carpeta y no el archivo deja el registro fuera de lo que se compara | §3 del resultado |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. Lo que bloqueaba a la fase `A` era `02·F8`: su plan aprobado no
declaraba `instalar.py`, y por eso el arreglo quedó propuesto y no hecho. El
plan de esta fase sí lo declara.
