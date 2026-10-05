# Estado de fase · Fase `A-EP-025-HU-006-lectura-de-los-jsonl` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-006-lectura-de-los-jsonl` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/` |
| **Planteamiento / Épica / HU** | [EP-025](../../epica.md) · [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Análisis 1 del pendiente 119 |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Acuerdos 7, 8 y 9 del análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-025 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-006, aprobada con el análisis |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados por el análisis, el 2026-10-04 |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 8 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Ninguna todavía | |

## 3. Pendiente / preguntas abiertas

Ninguna.

## 4. Si se bloqueó

**2026-10-05.** La orden `leer_consumo` falló contra la base real: la tabla `proyectos_proyecto` es la de la plataforma vieja (`interfaz/`), con 13 proyectos reales, y el módulo `core/proyectos/` de la HU-003 usa la misma etiqueta. Resolverlo toca datos del usuario, la plataforma vieja y el instalador, que ningún plan declara: vuelve al análisis. El lector, el guardado, la orden, `hook_presupuesto.py` y el paso de programar ya están hechos y sus pruebas pasan en la base de pruebas.

**Desbloqueada el 2026-10-05.** Se corrigió en el ciclo 2 de la fase de la HU-003, por orden del usuario: la base se respaldó, se reinició con las migraciones y se llenó con los proyectos que existen.
