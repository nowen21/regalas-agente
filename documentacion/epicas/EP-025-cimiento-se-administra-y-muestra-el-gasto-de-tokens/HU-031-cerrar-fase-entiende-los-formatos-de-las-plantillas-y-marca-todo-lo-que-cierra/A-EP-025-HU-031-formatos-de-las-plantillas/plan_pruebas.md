# Plan de Pruebas · Fase A-EP-025-HU-031, los formatos de las plantillas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU031-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-031](../HU-031-cerrar-fase-entiende-los-formatos-de-las-plantillas-y-marca-todo-lo-que-cierra.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 150](../../../../../historico-chat/resumenes/2026-10-09/pendientes/150-cerrar-fase-lee-todos-los-casos-y-marca-todo-lo-que-cierra/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `python -m unittest core.herramientas.tests_fase`. Una fase de juguete con los planes copiados del formato de `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` y `08-plan-pruebas.md`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-031 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-031 | CA-02 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-031 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-031 | RNF-01 | CP-004 | Compatibilidad | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Lee la matriz y los CA de la plantilla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Primera pasada con una fila `[CP-001](#…), [CP-002](#…)`, otra con `CP-003` y una de `RNF-01` con `CP-004` | El resultado trae CP-001 a CP-004, y el veredicto CA-01, CA-02 y RNF-01 |
| 2 | Los CA del plan como `| CA-01 | ☐ |` y `| [CA-02](…) | ☐ |` | La funcionalidad trae CA-01 y CA-02; sus nombres salen de la HU |

### CP-002 · Al cerrar marca todo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Segunda pasada | No queda `☐` en la matriz ni en los CA del plan; la sección 5 tiene la fecha y `☑` |
| 2 | Revisar las Definition of Done | La del plan, marcada menos el commit; con la HU terminada, sus tareas y su Definition of Done marcadas |

### CP-003 · Al reabrir desmarca lo mismo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reabrir la fase cerrada | La matriz, los CA, la sección 5 (sin fecha), la Definition of Done del plan y las casillas de la HU, sin marcar |

### CP-004 · El formato viejo cierra igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las 9 pruebas que ya había | Pasan |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
