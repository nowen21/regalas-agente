# Plan de Pruebas · Fase B-EP-005-HU-025, el estándar dice cuándo llegan las reglas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU025-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

No hay prueba automática: es texto del estándar. Se verifica leyéndolo de la base.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-025 | CA-05 | CP-001, CP-002 | Documental | Alta | No | ☐ |

**Cobertura:** 1 de 1 exigencia cubierta = 100 %.

## 6. Casos de prueba

### CP-001 · El texto aprobado está en la base

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `manage.py documento ver estandar base/tareas.md` | Dice que el mensaje trae solo `responder` y `recibir-pedido`, y que la acción trae las reglas de su tarea, una sola vez |

### CP-002 · La versión subió como MENOR

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la salida de `manage.py registrar_version --obliga no --agrega si` | La versión pasa de 56.8.0 a la menor siguiente, con su motivo |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
