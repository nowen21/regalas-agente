# Plan de Pruebas · Fase C-EP-025-HU-032, las revisiones de git   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU032-C |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.herramientas.tests_validar_suspendida core.comun.tests`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-032 | CA-03 | CP-006 | Funcional | Crítica | Sí | ☑ |
| HU-032 | CA-03 | CP-007 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-006 · La revisión suspendida no detiene

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validar.py versionado` con `git-versionado` suspendida | Sale con 0 y dice que está suspendida, con motivo y vencimiento |
| 2 | La misma sin suspender | Corre como siempre |
| 3 | Una orden que no es de git, como `fases` | No mira las suspensiones |

### CP-007 · Una sola consulta por guardado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr seguidas `versionado`, `marcas` y `plan` | La base se consulta una vez |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
