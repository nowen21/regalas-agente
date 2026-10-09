# Plan de Pruebas · Fase B-EP-025-HU-028, ningún mensaje sin trabajo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU028-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-028](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md), CA-05 |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, con la orden de erradicar «(sin trabajo)», el 2026-10-08 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde la raíz: `manage.py test core.consumo core.ayuda`. En la base real: `recalcular_trabajo` y `historico-chat/scripts/2026-10-08/diagnostico_sin_trabajo.py`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-028 | CA-05 | CP-005 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-005 · Ningún mensaje queda sin trabajo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar una conversación sin fase ni análisis, con su título | Sus mensajes quedan en «Conversación «título»» |
| 2 | Guardar un mensaje antes de que llegue el título, y después el título | Pasa del código de la conversación al título |
| 3 | Una conversación que empieza sin fase y después toca una | Desde la fase, los mensajes quedan en ella |
| 4 | Correr `recalcular_trabajo` con un mensaje cuya conversación no tiene líneas | Ninguno queda sin trabajo |
| 5 | Diagnóstico en la base real | 0 mensajes sin trabajo |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 1, en `resultado_pruebas.md`.
