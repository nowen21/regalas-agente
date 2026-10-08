# Plan de Pruebas · Fase A-EP-027-HU-003, todo pasa por las tablas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU003-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-003](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Cambiar un documento pasa por las tablas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar desde la pantalla el documento de F1 con su exigencia cambiada | La fila de F1 tiene la exigencia nueva; el texto guardado es el armado |
| 2 | Aprobar una propuesta que cambia el título de una regla | La fila tiene el título nuevo |
| 3 | Sincronizar con un documento de git que cambia una regla | La fila tiene el cambio |

### CP-002 · Nada se borra

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quitar el documento de una regla | La regla sigue en las tablas, sin documento |
| 2 | Guardar un documento sin una de sus reglas | Esa regla sigue en las tablas, sin documento |

### CP-003 · El agente recibe el texto armado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir con `ver_estandar` el documento de una regla cambiada | Sale el texto armado, con el cambio |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
