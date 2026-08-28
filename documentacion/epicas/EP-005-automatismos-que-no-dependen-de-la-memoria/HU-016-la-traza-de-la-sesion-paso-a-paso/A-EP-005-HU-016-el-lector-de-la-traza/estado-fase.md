# Estado de fase — Fase A-EP-005-HU-016-el-lector-de-la-traza (módulo Automatismos — lectores de la sesión)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-016-el-lector-de-la-traza` |
| **Módulo** | Automatismos — lectores de la sesión |
| **Planteamiento / Épica / HU** | [pendiente 73](../../../../../pendientes/hecho/la-sesion-tiene-su-traza.md) → [EP-005](../../epica.md) → [HU-016](../HU-016-la-traza-de-la-sesion-paso-a-paso.md) |
| **Última actualización** | 2026-08-20 |

---

## 1. En qué estación va

**Estación actual:** 12 — Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ («listo hágalo», 2026-08-20) |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ (EP-005, ya existía) |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ (HU-016 escrita desde el pendiente 73) |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ (`documentacion/automatismos/spec.md` §4.9) |
| 6 | Diseñador | diseño coherente | ☑ (§2.6 del plan) |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ («si», 2026-08-20) |
| 8 | Implementador | implementado + pruebas verdes | ☑ (6 de 6 en la suite nueva) |
| 9 | Verificador | trazabilidad sin faltantes | ☑ (`funcionalidad_implementada.md` §2, sin faltantes) |
| 10 | Crítico | sin hallazgos graves | ☑ (los dos tropiezos del cierre — el mapa del amarre y la entrada del registro — los atraparon sus pruebas y quedaron corregidos) |
| 11 | Cierre documental + señales | docs y señales al día | ☑ (S-017; especificación, mapas, README del histórico, CHANGELOG 28.0.0) |
| 12 | Commit | 👤 autorizado | ✅ `eedad93` |
| 13 | Publicación / despliegue | 👤 autorizado | ☑ no aplica aparte: viaja con `validadores/` en el `git pull` |

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
| T-01 a T-05 | Hechas | `traza.py`, subcomando, `archivo_de_sesion`, 6 casos |
| T-06 | Hecha | Especificación, mapas, README del histórico |
| T-07 | Hecha | La sesión real: 191 pasos, 0,69 s, en `historico-chat/trazas/` |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Lector a demanda, sin copiar resultados, nombrada como su histórico, emparejada por identificador | [S-017](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- La autorización del commit, que el usuario da aparte.

---

## 4. Si se bloqueó

- No está bloqueada.
