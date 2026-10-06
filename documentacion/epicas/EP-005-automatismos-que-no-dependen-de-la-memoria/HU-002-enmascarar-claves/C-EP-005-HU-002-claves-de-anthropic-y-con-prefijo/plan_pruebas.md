# Plan de Pruebas · Fase C-EP-005-HU-002, claves de Anthropic y con prefijo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU002-C |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-002](../HU-002-enmascarar-claves.md), CA-03 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 129](../pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | Tapado y validador con las formas nuevas | El agente | Local | Sí |
| Sistema | `validar.py secretos` sobre el repositorio | El agente | Local | Sí |

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`core.enganches.tests_claves_con_prefijo`, `core.enganches.tests_sesion` (las pruebas del tapado) y `core.validadores`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-03](../HU-002-enmascarar-claves.md#ca-03--las-claves-de-anthropic-y-las-variables-con-prefijo-también-se-tapan) | [CP-001](#cp-001--la-clave-de-anthropic-se-tapa), [CP-002](#cp-002--la-variable-con-prefijo-se-tapa), [CP-003](#cp-003--lo-que-no-es-clave-no-se-tapa), [CP-004](#cp-004--el-validador-la-señala-y-el-repositorio-sigue-limpio) | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La clave de Anthropic se tapa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tapar un texto con una clave `sk-ant-` armada al correr | Una clave tapada; el valor no queda |

### CP-002 · La variable con prefijo se tapa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tapar `ANTHROPIC_API_KEY=` con un valor, sin comillas | Se tapa el valor, la variable queda |
| 2 | Tapar `GITHUB_TOKEN="..."` y `DB_PASSWORD="..."`, con comillas | Se tapan los dos |
| 3 | Tapar `OPENAI_API_KEY: valor` | Se tapa |

### CP-003 · Lo que no es clave no se tapa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tapar `ANTHROPIC_API_KEY=os.environ["ANTHROPIC_API_KEY"]` | Nada |
| 2 | Tapar `MY_API_KEY="your_api_key"` | Nada: es un molde |
| 3 | Tapar un texto que solo nombra `ANTHROPIC_API_KEY` sin valor | Nada |

### CP-004 · El validador la señala y el repositorio sigue limpio

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `revisar_texto` con una clave `sk-ant-` en una línea de código | Una falla «clave de Anthropic» |
| 2 | `revisar_texto` con `ANTHROPIC_API_KEY = "<valor>"` | Una falla o aviso |
| 3 | Correr `python validadores/validar.py secretos` en la raíz | Sin fallas nuevas por esta fase |
| 4 | Correr las suites `tests_sesion` y `core.validadores` | En verde |

## 9. Gestión de defectos

Un defecto va a `resultado_pruebas.md` §4; si obliga a tocar un archivo que el plan no declara, es hallazgo y se detiene la fase.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre los 4 diseñados, en `resultado_pruebas.md`.
