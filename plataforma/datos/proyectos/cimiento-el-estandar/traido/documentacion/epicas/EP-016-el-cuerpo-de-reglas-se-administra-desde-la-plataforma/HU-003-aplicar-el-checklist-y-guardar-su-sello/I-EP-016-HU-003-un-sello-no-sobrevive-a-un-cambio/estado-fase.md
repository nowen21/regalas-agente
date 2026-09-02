# Estado de fase — Fase `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` (módulo Reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` |
| **Módulo** | Reglas |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md](../../epica.md) · [documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-003-aplicar-el-checklist-y-guardar-su-sello/HU-003-aplicar-el-checklist-y-guardar-su-sello.md](../HU-003-aplicar-el-checklist-y-guardar-su-sello.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ 20 filas; 248 reglas con sello; **185 falsos si se mide por fechas** |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-016 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ El veredicto se le pregunta a quien sabe darlo |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 16 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Los 185 falsos se vieron antes de que salieran |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `4c0de39` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Lo más importante de esta fase es un nombre.** La comparación barata se llama `parece_vencido`, y hay una prueba que comprueba que no exista una que se llame como si las fechas decidieran.

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
| T-01 | Terminada | Las 20 filas del checklist |
| T-02 | Terminada | El sello de una regla |
| T-03 | Terminada | **La comparación, con su nombre** |
| T-04 | Terminada | El veredicto del estándar |
| T-05 | Terminada | El molde, con los motivos |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 16 pruebas |
| T-08 | Terminada | **0 contra 185**: las dos formas de medir, al lado |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna. Los tres bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| El nombre de una función es parte de lo que promete: `parece_vencido` no es `esta_vencido` | [`S-110`](../../../../senales.md) |
| Una medición barata puede dar 185 falsos donde la buena da cero | [`S-110`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **Escribir el sello en la regla** no está: se arma el bloque y se devuelve.
- **Responder las filas** sigue siendo de una persona, y así queda.
- **Sin pantalla**, como el resto del módulo.

---

## 4. Si se bloqueó

No se bloqueó.
