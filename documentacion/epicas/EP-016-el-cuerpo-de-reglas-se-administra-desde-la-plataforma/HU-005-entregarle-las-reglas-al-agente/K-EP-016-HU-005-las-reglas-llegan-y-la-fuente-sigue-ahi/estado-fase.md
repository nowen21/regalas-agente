# Estado de fase — Fase `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` (módulo Reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` |
| **Módulo** | Reglas |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-005-entregarle-las-reglas-al-agente/HU-005-entregarle-las-reglas-al-agente.md](../HU-005-entregarle-las-reglas-al-agente.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 248 vigentes, 124 archivos, 679 511 caracteres |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-016 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Se entrega el texto, no un resumen |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 9 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **La fuente se nombra también cuando todo sale bien.** Es lo que recuerda que esta pieza no es un intermediario obligatorio: sin ella, los archivos se leen igual.

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
| T-01 | Terminada | Los capítulos en su orden |
| T-02 | Terminada | Su texto, con rutas relativas |
| T-03 | Terminada | La cuenta de vigentes |
| T-04 | Terminada | El tiempo |
| T-05 | Terminada | La fuente, nombrada pase lo que pase |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 9 pruebas |
| T-08 | Terminada | **0,17 s sobre 679 511 caracteres** |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Una pieza que acelera tiene que recordar que no es obligatoria: la fuente se nombra siempre | [`S-110`](../../../../senales.md) |
| Un resumen de una regla es otra regla, y sería la que el agente obedece | [`S-110`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Enchufarlo al arranque de una sesión** no está: hoy es una orden que se pide. El enganche sigue leyendo la fuente, y **eso es correcto por diseño**.
- **Cómo se comporta con un cuerpo diez veces más grande** no se sabe.
- **Sin pantalla**, como el resto del módulo.

---

## 4. Si se bloqueó

No se bloqueó.
