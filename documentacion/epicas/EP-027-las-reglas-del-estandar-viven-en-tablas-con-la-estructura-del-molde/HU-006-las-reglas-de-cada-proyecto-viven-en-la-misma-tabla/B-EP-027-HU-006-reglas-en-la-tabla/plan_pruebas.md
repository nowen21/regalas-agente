# Plan de Pruebas · Fase B-EP-027-HU-006, las reglas en la tabla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU006-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), CA-02 |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el «apruebo» del usuario del 2026-10-07 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-02 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias de esta fase cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Las reglas pasan a la tabla con su proyecto y su grupo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasar un archivo con reglas `### P1` y `### P2` en dos grupos `##` | Dos reglas con su proyecto, sus casillas y su grupo; sube la versión del proyecto |
| 2 | Pasar un archivo con reglas `## RP1` | Las reglas quedan igual |
| 3 | Pasar dos veces | No se duplica nada |

### CP-002 · El archivo queda en la historia y se borra

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasar con `--borrar` | El archivo ya no está; un cambio de la historia del proyecto guarda su texto entero |

### CP-003 · Se ven y se cambian en Cimiento

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir las reglas del proyecto | Cada regla con su código, su título y su grupo |
| 2 | `ver_regla --proyecto` con y sin código | El índice; la regla entera |
| 3 | Cambiar la exigencia de P1 desde la pantalla | La fila tiene la exigencia nueva |
| 4 | La cuenta de consulta intenta cambiar | No puede |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
