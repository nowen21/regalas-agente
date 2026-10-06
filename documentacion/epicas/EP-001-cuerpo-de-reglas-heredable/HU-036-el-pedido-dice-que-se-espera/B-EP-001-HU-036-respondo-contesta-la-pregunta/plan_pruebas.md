# Plan de Pruebas · Fase B-EP-001-HU-036, Respondo contesta la pregunta   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-001-HU-036 |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-036, fase B |
| **Fecha** | 2026-10-06 |
| **Aprobado por** | [análisis 1 del pendiente 131](../../../../../historico-chat/resumenes/2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

Pruebas unitarias sobre `RecuperadorDeReglas` con el anexo real. Se corre solo `core.herramientas.tests_respondo` ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-036 | CA-02 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-036 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · «Respondo» está en la lista y no recibe el aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-036 / CA-02 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | El anexo tiene la fila «Respondo» |
| **Datos de entrada** | «Respondo: la B», «respondo que sí» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `palabras_de_la_lista()` | Trae «Respondo» |
| 2 | Pedir `palabra_clave("respondo que sí")` | Da «Respondo» |
| 3 | Pedir `como_texto("Respondo: la B")` | No trae el aviso de `01·C28` |

**Resultado esperado final:** la palabra se reconoce, con mayúscula o sin ella.

### CP-002 · «Respondo» no pide tarea propia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-036 / CA-02 |
| **Tipo** | Funcional, alcance |
| **Prioridad** | Alta |
| **Precondiciones** | `base/tareas.md` sin «respondo» |
| **Datos de entrada** | «Respondo: la B» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `tareas_del_mensaje("Respondo: la B")` | Da `{}`: no autoriza ninguna tarea |

**Resultado esperado final:** «Respondo» no trae reglas de ninguna tarea; solo las de todo mensaje.

## 9. Gestión de defectos

Un caso en rojo se corrige dentro de la fase; si exige tocar un archivo fuera del plan, se para y se abre el análisis 2.

## 12. Métricas e informe

El resultado va en `resultado_pruebas.md` de esta fase.
