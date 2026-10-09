# Estado de fase · Fase `A-EP-029-HU-008-danar-a-proposito` (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-008-danar-a-proposito` |
| **Módulo** | Pruebas de Cimiento, `proyectos/cimiento/core/pruebas/` |
| **Planteamiento / Épica / HU** | [EP-029](../../epica.md) · [HU-008](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md) |
| **Última actualización** | 2026-10-09 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ [Análisis 1 del pendiente 148](../../../../../historico-chat/resumenes/2026-10-08/pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/analisis-1.md) |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Con el análisis de origen |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-029 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-008, aprobada con el análisis |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados por el análisis |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 3 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ Hallazgos: los del cierre del plan |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 3 de 3. **Bloqueadas:** ninguna.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Cada daño le pone al archivo una hora distinta, para que Python no corra el `.pyc` viejo | `S-362` |
| `cerrar_fase` lee un solo caso por fila de la matriz del plan de pruebas; el resultado se completó a mano | Hallazgo en el resumen de la sesión del 2026-10-09 |

## 3. Pendiente / preguntas abiertas

Ninguna.

## 4. Si se bloqueó

No aplica.
