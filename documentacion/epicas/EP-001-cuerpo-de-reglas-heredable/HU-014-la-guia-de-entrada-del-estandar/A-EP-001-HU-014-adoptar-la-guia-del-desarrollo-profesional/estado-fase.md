# Estado de fase — Fase A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> **Checkpoint del orquestador**: el estado persistido en cada puerta para sobrevivir a la compactación. Se actualiza en cada puerta que pasa.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional` |
| **Módulo** | Cuerpo de reglas |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md) · [pendiente 73](../../../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md) |
| **Última actualización** | 2026-08-21 |

---

## 1. En qué estación va

**Estación actual:** 12 — Commit, esperando la autorización del usuario. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 2026-08-21: pendiente 73 y su adjunto analizados |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ el usuario eligió bajar el 73 («73», 2026-08-21) tras el análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-001 existía; solo suma la HU a sus índices |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-08-21, «si» del usuario |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ los CA son la especificación (entregable documental) |
| 6 | Diseñador | diseño coherente | ☑ decisión de sitio en el plan §2.6: `base/guia-de-entrada.md`, fuera del arranque |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-08-21, «si» del usuario |
| 8 | Implementador | implementado + pruebas verdes | ☑ 2026-08-21: guía escrita, 2 de 2 casos aprobados |
| 9 | Verificador | trazabilidad sin faltantes | ☑ 2026-08-21: cierre §2, 5 de 5 ítems y 5 de 5 tareas |
| 10 | Crítico | sin hallazgos graves | ☑ un desvío declarado (línea de índice de 102 bytes), aceptado en el resultado §4 |
| 11 | Cierre documental + señales | docs y señales al día | ☑ 2026-08-21: cierre, versión 28.2.0, pendiente 73 en hecho/ con 9 avisos |
| 12 | Commit | 👤 autorizado | ☐ **esperando al usuario** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 2 de 2 |
| **CA en "No"** | — |
| **Defectos abiertos aceptados** | — |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 a T-05 | Hechas | Detalle en el cierre §2.2 |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La dirección de fondo del usuario (administrar proyectos desde Cimiento, no desde un `.md`) se capturó aparte: [pendiente 75](../../../../../pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md) y sus palabras en [prompts/la-administracion-de-proyectos-desde-cimiento.md/](../../../../../prompts/la-administracion-de-proyectos-desde-cimiento.md) | No es señal: es trabajo por hacer, y va en su pendiente |

---

## 3. Pendiente / preguntas abiertas

- La autorización del commit (puerta 12), que se pregunta aparte.

---

## 4. Si se bloqueó

No está bloqueada: terminó su cierre documental y espera el commit.
