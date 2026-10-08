# Estado de fase · Fase `A-EP-025-HU-019-la-regla-y-su-plantilla` (módulo `base/02-flujo-de-trabajo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-019-la-regla-y-su-plantilla` |
| **Módulo** | `base/02-flujo-de-trabajo/` |
| **Planteamiento / Épica / HU** | [EP-025](../../epica.md) · [HU-019](../HU-019-toda-accion-trae-su-contraria.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md) |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Con el análisis de origen |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-025 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-019, aprobada con el análisis |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados por el análisis |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 5 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ Hallazgos: los del cierre del plan |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |
| 12 | Commit | 👤 autorizado | ✅ `eda8871` |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

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
| La regla va en el `02` y cita `03·D2` como caso | En el checklist de `F30` |

## 3. Pendiente / preguntas abiertas

Reabierta el 2026-10-05: la sección 2.1 declaraba la carpeta base/reglas-por-tarea/ en vez de sus archivos, y validar.py flujo lo marca como falla (02·F8).

## 4. Si se bloqueó

No aplica.
