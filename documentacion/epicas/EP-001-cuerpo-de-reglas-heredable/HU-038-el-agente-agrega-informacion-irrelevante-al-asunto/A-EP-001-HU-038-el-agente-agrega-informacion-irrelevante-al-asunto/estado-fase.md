# Estado de fase · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` |
| **Módulo** | Cuerpo de reglas, capítulo 00 |
| **Planteamiento / Épica / HU** | [EP-001](../../epica.md) · [HU-038](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md) · [pendiente 95](../../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md) |
| **Última actualización** | 2026-09-27 |

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Ninguna regla exige pertinencia; `ID11` libre |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ Pendiente 95 aprobado el 2026-09-27 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ EP-001 ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ HU-038, 2026-09-27 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ Las RN-01 a RN-04 de HU-038, redactadas por el usuario |
| 6 | Diseñador | diseño coherente | ✅ Va en el capítulo 00 y extiende `ID7`, `ID8` e `ID9` |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ 2026-09-27; título en imperativo por `20·M5`, decidido por el usuario |
| 8 | Implementador | implementado + pruebas verdes | ✅ Las 9 tareas hechas; `metareglas` y `estandar` sin fallas |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 5 de 5 exigencias con caso aprobado |
| 10 | Crítico | sin hallazgos graves | ✅ Un defecto de severidad baja, corregido en la fase |
| 11 | Cierre documental + señales | docs y señales al día | ✅ `funcionalidad_implementada.md` escrito; HU-038 en Terminada |
| 12 | Commit | 👤 autorizado | ✅ `3c85fe3` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · crear el archivo de la regla | Terminada | CP-001 |
| T-02 · fila en la tabla del capítulo | Terminada | CP-001 |
| T-03 · redactar el cuerpo con RN-01 a RN-04 | Terminada | CP-002, 318 caracteres leídos |
| T-04 · declarar la dependencia | Terminada | CP-003 |
| T-05 · clasificarla | Terminada | CP-004 |
| T-06 · versionar | Terminada | 38.1.0, MENOR |
| T-07 · cerrar el pendiente 95 y actualizar HU-038 | Terminada | Pendiente 95 cerrado y HU-038 en Terminada |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El nombre del archivo de la regla es el de la HU, no el imperativo del capítulo | Decisión del usuario, en el plan §2.6 |
| Aplicar la regla a los pendientes 96 y 97 no es parte de esta fase | Decisión del usuario, 2026-09-27 |
| El encabezado de la regla va en imperativo, «Escribe solo lo pertinente al asunto», porque `20·M5` lo exige | Decisión del usuario, 2026-09-27 |

## 3. Pendiente / preguntas abiertas

- El commit, que autoriza el usuario.
