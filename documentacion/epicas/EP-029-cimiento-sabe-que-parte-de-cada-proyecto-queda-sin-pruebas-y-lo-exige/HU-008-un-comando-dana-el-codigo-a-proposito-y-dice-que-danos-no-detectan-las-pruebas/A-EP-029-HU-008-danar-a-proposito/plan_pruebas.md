# Plan de Pruebas · Fase A-EP-029-HU-008, dañar el código a propósito   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU008-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-008](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 148](../../../../../historico-chat/resumenes/2026-10-08/pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas.tests_danar`. Cada caso arma en una carpeta temporal un módulo `suma.py`, su prueba con `unittest`, y corre el comando sobre esa carpeta.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-008 | CA-02 | CP-003, CP-004, CP-005 | Funcional | Crítica | Sí | ☑ |
| HU-008 | CA-03 | CP-006 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Un daño detectado y otro no

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dañar `a + b` por `a - b`, que la prueba revisa | Sale «detectado» |
| 2 | Dañar una función que ninguna prueba llama | Sale «no detectado» |

### CP-002 · Un daño cuyo texto no aparece, o aparece dos veces

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un daño con un texto original que no está en el archivo | Sale «no se aplicó», y el archivo no cambia |
| 2 | Un daño con un texto que aparece dos veces | Sale «no se aplicó» |

### CP-003 · El daño que escribe un archivo nuevo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un daño que hace que la prueba escriba `rastro.txt` | Al terminar, `rastro.txt` no existe |

### CP-004 · El daño que cuelga las pruebas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un daño que mete un ciclo sin fin, con `--tiempo 5` | Sale «detectado (se pasó del tiempo)» y el archivo vuelve a estar igual |

### CP-005 · Se cae a mitad de un daño

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Hacer que correr las pruebas lance un error con el daño puesto | El error sale, y el archivo dañado es igual al original |
| 2 | Terminar una corrida normal | Cada archivo es igual al original y la corrida final sin daños pasa |

### CP-006 · Las pruebas fallan sin daños

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el comando sobre un proyecto cuya prueba falla | Dice que primero hay que arreglar las pruebas y no cambia ningún archivo |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 6, en `resultado_pruebas.md`.
