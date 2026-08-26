# Estado de fase — Fase A-EP-005-HU-015-el-portero-del-contenido-externo (módulo Automatismos — enganches)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-015-el-portero-del-contenido-externo` |
| **Módulo** | Automatismos — enganches |
| **Planteamiento / Épica / HU** | [pendiente 72](../../../../../pendientes/hecho/lo-que-llega-de-afuera-llega-marcado.md) → [EP-005](../../epica.md) → [HU-015](../HU-015-lo-que-llega-de-afuera-llega-marcado.md) |
| **Última actualización** | 2026-08-20 |

---

## 1. En qué estación va

**Estación actual:** 12 — Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ («listo hágalo», 2026-08-20) |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ (EP-005, ya existía) |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ (HU-015 escrita desde el pendiente 72) |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (`documentacion/automatismos/spec.md` §4.8) |
| 6 | Diseñador | diseño coherente | ☑ (§2.6 del plan) |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ («si», 2026-08-20) |
| 8 | Implementador | implementado + pruebas verdes | ☑ (9 de 9 en la suite nueva) |
| 9 | Verificador | trazabilidad sin faltantes | ☑ (`funcionalidad_implementada.md` §2, sin faltantes) |
| 10 | Crítico | sin hallazgos graves | ☑ (las fallas de las suites son ajenas y anteriores; documentado en el resultado, CP-008) |
| 11 | Cierre documental + señales | docs y señales al día | ☑ (S-016; contrato, mapas, registro, especificación, CHANGELOG 28.0.0; pendiente 72 en `hecho/`) |
| 12 | Commit | 👤 autorizado | ☐ **esperando la autorización del usuario** (`00·N2`) |
| 13 | Publicación / despliegue | 👤 autorizado | ☑ parcial: instalado en los 9 proyectos por el T-07 del plan aprobado; el commit del estándar sigue pendiente |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 (y 2 de 2 RNF) |
| **CA en "No"** | — |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `validadores/externo.py` |
| T-02 | Hecha | `adaptadores/claude-code/hook_externo.py` |
| T-03 | Hecha | Origen MCP y `Read` fuera de la raíz |
| T-04 | Hecha | 9 casos en verde |
| T-05 | Hecha | Fila en `HOOKS_CLAUDE`; instalación y reclamo probados |
| T-06 | Hecha | Registro, contrato, especificación, mapas |
| T-07 | Hecha | 9 de 9 proyectos; el sobre verificado en vivo |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Agregar contexto, no reemplazar; por nombre y argumentos; `Read` externo solo fuera de la raíz | [S-016](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- La autorización del commit, que el usuario da aparte.

---

## 4. Si se bloqueó

- No está bloqueada.
