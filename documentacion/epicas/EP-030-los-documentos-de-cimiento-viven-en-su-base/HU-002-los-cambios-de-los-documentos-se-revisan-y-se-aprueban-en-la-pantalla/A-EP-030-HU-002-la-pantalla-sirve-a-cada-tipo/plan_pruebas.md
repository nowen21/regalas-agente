# Plan de Pruebas · Fase A-EP-030-HU-002, la pantalla sirve a cada tipo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP030-HU002-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-002](../HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 142](../../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar.tests_revision core.estandar.tests_documentos core.estandar.tests_pantalla`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-002 | CA-02 | CP-002, CP-003 | Funcional | Crítica | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La pantalla muestra el antes y el después de cada tipo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Proponer el cambio de un documento y de un recuerdo, y abrir «Estándar → Propuestas» | Se ven las dos, cada una con las líneas que salen y las que entran |

### CP-002 · Aprobar con el botón

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Oprimir Aprobar en cada propuesta | El texto cambia, la propuesta queda aprobada con la cuenta y la hora |

### CP-003 · Un tipo nuevo se sirve solo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Registrar un tipo de prueba en el camino único y aprobar su propuesta | Se aplica con el código de ese tipo, sin tocar `cambios.py` |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
