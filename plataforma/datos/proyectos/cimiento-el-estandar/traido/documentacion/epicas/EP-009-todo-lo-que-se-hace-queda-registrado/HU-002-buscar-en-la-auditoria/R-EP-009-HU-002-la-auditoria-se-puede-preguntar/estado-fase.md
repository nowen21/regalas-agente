# Estado de fase — Fase `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` (módulo Auditoría)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `R-EP-009-HU-002-la-auditoria-se-puede-preguntar` |
| **Módulo** | Auditoría |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/epica.md](../../epica.md) · [documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-002-buscar-en-la-auditoria/HU-002-buscar-en-la-auditoria.md](../HU-002-buscar-en-la-auditoria.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ La fase `D` registra; falta poder preguntarle |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01 |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-009, ya aprobada |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/auditoria/spec.md](../../../../auditoria/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Solo lectura: nada de lo registrado se toca |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 14 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ Un defecto crítico hallado y corregido en la fase |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ✅ `d4bf878` |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Con esta fase `EP-009` queda completa.** Registrar y consultar, las dos mitades.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. Se halló uno crítico y se corrigió dentro de la fase |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | Los tres filtros |
| T-02 | Terminada | **El día del `hasta` entra completo** |
| T-03 | Terminada | El aviso de vacío |
| T-04 | Terminada | El tiempo y el aviso de recorte |
| T-05 | Terminada | Los tipos sacados de lo registrado |
| T-06 | Terminada | La orden de consola |
| T-07 | Terminada | 14 pruebas |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna. Los cuatro bloqueos, cerrados.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un rango sobre fechas guardadas como texto corta el último día en la medianoche | [`S-113`](../../../../senales.md) |
| Un recorte que no se avisa se lee como «eso es todo lo que hay» | [`S-113`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **El tiempo con un año de registros habrá que volverlo a medir** cuando la auditoría real llegue a ese volumen.
- **Sin pantalla**, como el resto de los módulos de esta etapa.

---

## 4. Si se bloqueó

No se bloqueó.
