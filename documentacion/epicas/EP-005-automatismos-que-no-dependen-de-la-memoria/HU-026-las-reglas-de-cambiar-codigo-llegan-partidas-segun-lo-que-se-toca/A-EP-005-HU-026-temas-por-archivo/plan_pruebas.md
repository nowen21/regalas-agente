# Plan de Pruebas · Fase A-EP-005-HU-026, los temas por archivo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU026-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-026](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 2 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.herramientas.tests_entrega_de_reglas`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-026 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-026 | CA-02 | CP-003 | Funcional | Crítica | Sí | ☐ |
| HU-026 | CA-03 | CP-004 | Documental | Alta | No | ☐ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Una prueba recibe pruebas y lo de todos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir `core/tests_x.py` con la tabla | Llegan reglas de los capítulos 08 y de los de `todos`; ninguna del 17 ni del 18 |
| 2 | Medir lo que llega hasta vaciar | No pasa de 25 KB |

### CP-002 · Otro tipo de archivo recibe sus temas aparte

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Vaciar una prueba y escribir `views.py` | Llegan las del 04, 05 y 06, que la prueba no había traído |

### CP-003 · Sin patrón, o sin tabla, llegan todas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir `algo.xyz` con la tabla | Llegan todas las de `cambiar-codigo` |
| 2 | Escribir `tests_x.py` sin la tabla | Llegan todas, como en la HU-025 |

### CP-004 · La tabla queda propuesta en el estándar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `manage.py documento editar estandar base/tareas.md` con `tareas-con-temas.txt` | Queda una propuesta con su número |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
