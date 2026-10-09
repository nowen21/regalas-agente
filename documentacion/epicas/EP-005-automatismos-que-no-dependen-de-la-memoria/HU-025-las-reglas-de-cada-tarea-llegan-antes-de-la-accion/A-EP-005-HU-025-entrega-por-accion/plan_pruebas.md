# Plan de Pruebas · Fase A-EP-005-HU-025, la entrega de reglas por acción   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU025-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.herramientas.tests_entrega_de_reglas core.enganches.tests_suspendidos`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-025 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-025 | CA-02 | CP-003, CP-004 | Funcional | Crítica | Sí | ☐ |
| HU-025 | CA-03 | CP-005, CP-006 | Funcional | Alta | Sí | ☐ |
| HU-025 | CA-04 | CP-007 | Funcional | Alta | Sí | ☐ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Cada acción reconoce su tarea

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir `x.py` | `cambiar-codigo` |
| 2 | Escribir `notas.md` | `escribir-documento` |
| 3 | Escribir en `base/` | también `cambiar-estandar` |
| 4 | Correr `git commit` | `correr-comando` y `tocar-git` |
| 5 | Usar `WebFetch` | `ir-afuera` |
| 6 | Leer un archivo | Ninguna |

### CP-002 · El enganche entrega sin frenar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche con una escritura de `x.py` | Sale con código 0, con `additionalContext` y sin decisión de permiso |

### CP-003 · Una sola vez por sesión y por agente

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir dos veces la misma tarea en la misma sesión | La segunda no repite reglas |
| 2 | Pedirla desde un subagente | Le llegan las suyas |

### CP-004 · Lo que no cupo llega después, y sin leer el estándar cuando ya todo llegó

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Una tarea que no cabe en el tope | La primera entrega nombra lo que falta; la siguiente trae lo que faltaba |
| 2 | Pedir la tarea cuando ya llegó toda | No lee el estándar y no entrega nada |

### CP-005 · El mensaje trae solo lo que falta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Primer mensaje con «Pregunta» | Llegan las de `responder` y no las de `recibir-pedido` |
| 2 | Mensaje con «Hágalo» | Llegan las de `recibir-pedido` |
| 3 | Otro mensaje igual | No llega ninguna de las dos |
| 4 | Un mensaje que cita una regla | Llega la regla citada |
| 5 | Un mensaje sin palabra clave | Llega el aviso de `01·C28` |

### CP-006 · Sin el bloque de cada turno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `hook_reglas.py` con un mensaje | No trae «LAS REGLAS DE CADA TURNO» |

### CP-007 · Las señales al abrir la sesión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el catálogo de enganches | `hook_senales.py` está en `SessionStart` y no en `UserPromptSubmit` |
| 2 | Correr el aviso dos veces con la misma sesión, leída de la entrada | Avisa solo la primera |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 7, en `resultado_pruebas.md`.
