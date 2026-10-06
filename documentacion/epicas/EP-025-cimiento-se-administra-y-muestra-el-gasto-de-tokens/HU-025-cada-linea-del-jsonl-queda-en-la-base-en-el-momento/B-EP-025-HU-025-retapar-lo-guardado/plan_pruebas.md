# Plan de Pruebas · Fase B-EP-025-HU-025, volver a tapar lo guardado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU025-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md), CA-05 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 129](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

`manage.py test core.consumo.tests_retapar`, y la orden sobre la base real.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-025 | CA-05 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-025 | CA-05 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-025 | CA-05 | CP-003 | Funcional | Crítica | No | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La clave que quedó en claro se tapa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar una línea con una clave `sk-ant-` sin tapar, como estaba antes de la fase C | Queda en claro |
| 2 | Correr `retapar_lineas` | Dice 1 línea cambiada; la clave ya no está y `tapadas` sube |
| 3 | Revisar una línea sin clave | No cambió |

### CP-002 · Correrla otra vez no cambia nada

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `retapar_lineas` de nuevo | 0 líneas cambiadas |
| 2 | Comparar la huella | Igual a la de antes |

### CP-003 · Sobre la base real

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `manage.py retapar_lineas` en la base `cimiento` | Termina y dice cuántas cambió |
| 2 | Contar líneas con `sk-ant-` en claro | 0 |

## 9. Gestión de defectos

Van a `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre los 3 diseñados.
