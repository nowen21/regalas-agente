# Plan de Pruebas · Fase A-EP-026-HU-003, la importación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU003-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-003](../HU-003-el-estandar-55-1-0-entra-a-la-base.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.historia`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-003 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Todo `base/` entra, idéntico

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Importar el estándar real a la base de pruebas | Un documento por cada `.md` de `base/` |
| 2 | Comparar el texto de cada documento con su archivo | Idénticos |

### CP-002 · La memoria de un proyecto entra

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Registrar un proyecto con dos recuerdos y su índice | Dos recuerdos del proyecto en la base; el índice `memory.md` también, como recuerdo |

### CP-003 · Versión de partida y una sola vez

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Importar | Una versión del estándar con el número de `VERSION`, y cada documento es un cambio de ella |
| 2 | Importar otra vez | Se niega y no cambia nada |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
