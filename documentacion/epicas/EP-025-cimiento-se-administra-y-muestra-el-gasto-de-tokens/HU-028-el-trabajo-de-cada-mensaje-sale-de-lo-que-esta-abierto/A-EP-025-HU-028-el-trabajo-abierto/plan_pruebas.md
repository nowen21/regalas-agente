# Plan de Pruebas · Fase A-EP-025-HU-028, el trabajo abierto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU028-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-028](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, con «apruebo» a las opciones 1 y 2, el 2026-10-08 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde la raíz: `manage.py test core.consumo core.ayuda`. En la base real: `manage.py recalcular_trabajo`, contando «(sin trabajo)» antes y después.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-028 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-028 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-028 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-028 | CA-04 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El análisis prendido es el trabajo del mensaje

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un mensaje con el aviso «La conversación entra al análisis pendientes/119-x/analisis-2.md» y un turno que toca una fase | El trabajo es el análisis, con origen «análisis» |
| 2 | Guardar uno con «Ningún análisis está prendido» | El aviso no da trabajo |

### CP-002 · Se reconocen todas las fases y las órdenes de consola

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Deducir el trabajo de una ruta de una fase `B-` | Es esa fase |
| 2 | Guardar un turno cuya orden de consola nombra la carpeta de una fase | El trabajo es esa fase, con origen «archivos» |

### CP-003 · El mensaje sin rastro sigue en el trabajo de la conversación

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un mensaje con trabajo y después un «Apruebo» sin rastro, en la misma conversación | El «Apruebo» queda con el mismo trabajo, con origen «conversación» |
| 2 | Leer después el turno de ese «Apruebo», que toca otra fase | El trabajo pasa a esa fase |
| 3 | Un mensaje sin rastro en otra conversación | Queda sin trabajo |

### CP-004 · Lo ya guardado se recalcula

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con líneas de sesión guardadas y mensajes sin trabajo, correr `recalcular_trabajo` | Los mensajes quedan con el trabajo de CP-001 a CP-003 |
| 2 | Correrla otra vez | Nada cambia |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
