# Estado de fase — Fase `AB-EP-022-HU-002-el-agente-no-aprueba` (módulo Acceso)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `AB-EP-022-HU-002-el-agente-no-aprueba` |
| **Módulo** | Acceso |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/epica.md](../../epica.md) · [documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer.md](../HU-002-separar-lo-que-cada-grupo-puede-hacer.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ `aprobar --quien` aceptaba cualquier texto |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-022 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/acceso/spec.md](../../../../acceso/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Dos grupos, y el porqué vive con el permiso |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 10 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑  |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase cierra `EP-022` y se cierra el pendiente 94.** Y queda tapado el mismo hueco que `EP-017` cerró en los documentos, un nivel más abajo.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | Los dos grupos |
| T-02 | Terminada | Quién puede qué |
| T-03 | Terminada | El rechazo con su porqué |
| T-04 | Terminada | `aprobar` exige cuenta |
| T-05 | Terminada | Las 17 pruebas al día |
| T-06 | Terminada | 10 pruebas |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una firma que dice quién sin probarlo tiene el mismo problema que una escrita a mano | [`S-125`](../../../../senales.md) |
| De cuatro actores definidos, solo los que entran necesitan cuenta | [`S-125`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **No hay permisos por proyecto:** un grupo rige en toda la plataforma.
- **Quien pueda editar la base puede darse cualquier permiso.** Lo que se logra es que saltárselo sea deliberado.
- **Lo registrado antes de que hubiera cuentas no se reescribe.**

---

## 4. Si se bloqueó

No se bloqueó.
