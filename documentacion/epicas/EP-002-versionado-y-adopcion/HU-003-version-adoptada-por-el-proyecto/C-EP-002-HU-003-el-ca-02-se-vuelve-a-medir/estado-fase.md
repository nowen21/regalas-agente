# Estado de fase — Fase `C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir` (módulo Programas de comprobación)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir` |
| **Módulo** | Programas de comprobación |
| **Planteamiento / Épica / HU** | [EP-002](../../epica.md) · [HU-003](../HU-003-version-adoptada-por-el-proyecto.md) |
| **Última actualización** | 2026-08-29 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyó la fase roja y su resultado |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-29, «terminélo» sobre los rojos que se pueden cerrar |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del criterio |
| 6 | Diseñador | diseño coherente | ✅ No se toca código |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ El molde se aprobó una vez para las cinco |
| 8 | Implementador | implementado + pruebas verdes | ✅ La medición corre y sale verde |
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
| **CA cumplidos** | 1 de 1 — CA-02 · Una versión que no existe se detecta |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · ejecutar el criterio que quedó en rojo | Terminada | el proyecto declara la v99.9.9, que no existe en el registro de cambios del estándar — mientras el número sea falso, el aviso de desfase no dice nada |
| T-02 · comprobar que la medición no se da por buena de más | Terminada | Está en el §4.1 del resultado |
| T-03 · poner al día el `Estado` de la historia | Terminada | — |
| T-04 · declarar el veredicto que deja atrás | Terminada | §0 del cierre |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un veredicto en rojo es una foto, y nadie la vuelve a mirar | `S-061` |
| El reemplazo **se declara, no se deduce del orden** | `EP-004·HU-023` |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. La medición corrió antes de crear esta carpeta, y el guion no
escribe la fase de una historia cuya medición salga en rojo.
