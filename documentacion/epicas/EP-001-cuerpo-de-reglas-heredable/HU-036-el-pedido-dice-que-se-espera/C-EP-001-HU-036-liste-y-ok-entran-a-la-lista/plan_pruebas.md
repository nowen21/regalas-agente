# Plan de Pruebas · Fase C-EP-001-HU-036, Liste y OK entran a la lista   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-001-HU-036 |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-036, fase C |
| **Fecha** | 2026-10-06 |
| **Aprobado por** | El usuario, el 2026-10-06 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

Pruebas unitarias sobre `RecuperadorDeReglas`, con el anexo real `base/01-conducta/palabras-clave.md`. Se corre solo `core.herramientas.tests_liste_y_ok` ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

**Por qué con el anexo real y no con uno de prueba.** Lo que se quiere comprobar es que las filas que el usuario escribió en el archivo de verdad se leen bien. Un anexo inventado probaría el lector, no el cambio.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-036 | CA-02 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-036 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-036 | CA-03 | CP-003 | Funcional | Alta | Sí | ☐ |

**Cobertura:** 2 de 2 criterios cubiertos = 100 %.

## 6. Casos de prueba

### CP-001 · `Liste` y `OK` están en la lista y no reciben el aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-036 / CA-02 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | El anexo tiene las filas `Liste` y `OK` |
| **Datos de entrada** | «Liste las palabras», «ok», «OK, entendido» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `palabras_de_la_lista()` | Trae «Liste» y «OK» |
| 2 | Pedir `palabra_clave("ok")` | Da «OK» |
| 3 | Pedir `palabra_clave("Liste las palabras")` | Da «Liste» |
| 4 | Pedir `trae_palabra_clave("OK, entendido")` | Da verdadero |

**Resultado esperado final:** las dos palabras se reconocen con mayúscula o sin ella, y ningún mensaje que abra con ellas recibe el aviso de `01·C28`.

### CP-002 · `OK` no autoriza ninguna tarea

| Campo | Valor |
|---|---|
| **HU / CA** | HU-036 / CA-02 |
| **Tipo** | Funcional, alcance |
| **Prioridad** | Alta |
| **Precondiciones** | `base/mapa-de-tareas.md` sin «ok» ni «liste» |
| **Datos de entrada** | «ok», «Liste las palabras» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `tareas_del_mensaje("ok")` | Da `{}`: no autoriza ninguna tarea |
| 2 | Pedir `tareas_del_mensaje("Liste las palabras")` | Da `{}` |

**Resultado esperado final:** ninguna de las dos trae reglas de tarea; solo llegan las de todo mensaje. Es lo que distingue el acuse de recibo de «Continúe».

### CP-003 · La forma de la pregunta entre signos se trata como ausente

| Campo | Valor |
|---|---|
| **HU / CA** | HU-036 / CA-03 |
| **Tipo** | Funcional, borde |
| **Prioridad** | Alta |
| **Precondiciones** | El anexo ya no tiene la fila de la pregunta entre signos |
| **Datos de entrada** | «¿qué sigue?» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `palabras_de_la_lista()` | Ninguna de sus filas empieza por `¿` |
| 2 | Pedir `trae_palabra_clave("¿qué sigue?")` | Da falso |
| 3 | Pedir `aviso_sin_palabra()` | La lista que trae no nombra la forma entre signos |

**Resultado esperado final:** una pregunta escrita entre signos se trata como mensaje sin palabra, que es lo que ya pasaba, y el aviso deja de ofrecer una forma que no funciona.

## 9. Gestión de defectos

Un caso en rojo se corrige dentro de la fase. Si exige tocar un archivo que el plan no declara, se para y se abre el análisis siguiente ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

## 12. Métricas e informe

El resultado va en `resultado_pruebas.md` de esta fase.
