# Plan de Pruebas · Fase `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-023-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-023, CA-01 a CA-03 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado el 2026-09-28 |

## 3. Estrategia de pruebas

Las pruebas del programa corren sobre carpetas temporales con reglas de prueba, para poder cambiar una regla sin tocar el repositorio. La lista se lee. El resto se comprueba sobre el propio repositorio.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Que el programa junte bien las tareas y escriba el mapa | El agente | Carpeta temporal | Sí |
| Sistema | Que la línea no cambie el largo ni anule el checklist, y que el mapa del repositorio salga del programa | El agente | Local | Sí, con `validar.py` y el programa |
| Aceptación | Que la lista de tareas sirva y no se superponga | El usuario | Local | No |
| Regresión | Que `metareglas` y `estandar` sigan sin fallas | El agente | Local | Sí |

Se corren solo los validadores y las pruebas que la fase toca (`02·F5`): `metareglas`, `estandar`, `versionado`, las pruebas nuevas y las de `metareglas.py`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-023 | [CA-01](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-01--la-lista-de-tareas-existe-y-es-cerrada) | [CP-001](#cp-001--la-lista-existe-y-no-se-superpone) | Funcional | Crítica | No | ☐ |
| HU-023 | [CA-02](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-02--una-regla-declara-sus-tareas-sin-cambiar-lo-que-exige) | [CP-002](#cp-002--la-línea-no-cambia-la-regla) | Funcional, caso borde | Crítica | Sí | ☐ |
| HU-023 | [CA-03](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-03--el-mapa-sale-de-las-reglas) | [CP-003](#cp-003--el-mapa-sale-de-las-reglas) | Funcional | Crítica | Sí | ☐ |
| HU-023 | RNF-01, RNF-02 | [CP-004](#cp-004--versionado-y-pruebas) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 5 de 5 exigencias de esta fase cubiertas, 100%.

## 6. Casos de prueba

### CP-001 · La lista existe y no se superpone

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 terminada, con la lista aprobada por el usuario |
| **Datos de entrada** | `base/tareas.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `base/tareas.md` | Una tabla con cada tarea: nombre corto y cuándo aplica |
| 2 | Comparar las tareas de dos en dos | Ninguna acción del agente cae en dos tareas a la vez |
| 3 | Tomar cada regla del núcleo ya anotada | Cada una encontró al menos una tarea que le sirve |

**Resultado esperado final:** la lista es cerrada, no se superpone y alcanza para el núcleo.

### CP-002 · La línea no cambia la regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-02 |
| **Tipo** | Funcional, caso borde |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-02 y la T-03 terminadas |
| **Datos de entrada** | Una regla de prueba en carpeta temporal, y `N1` a `N10` del repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En la prueba, medir con `Regla.largo()` una regla sin la línea y la misma con la línea | El mismo número |
| 2 | En la prueba, comparar con `_sin_declaracion` el texto sellado y el texto con la línea | Iguales: el sello no vence |
| 3 | Medir `N1` a `N10` del repositorio antes y después de anotarlas | El mismo largo en las diez |
| 4 | Correr `python validadores/validar.py metareglas` | Ninguna regla del núcleo aparece con el sello vencido |

**Resultado esperado final:** la línea queda fuera del cuerpo y del sello.

### CP-003 · El mapa sale de las reglas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-03 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-04 a la T-06 terminadas |
| **Datos de entrada** | Reglas de prueba en carpeta temporal, y el núcleo del repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En la prueba, armar el mapa con una regla que declara dos tareas | La regla aparece bajo las dos, con su enlace |
| 2 | En la prueba, cambiarle una tarea por otra y volver a armar el mapa | Aparece bajo la nueva y no bajo la vieja |
| 3 | Correr las pruebas con `python -m unittest test_cada_tarea_sabe_que_reglas_le_aplican` desde `validadores/tests` | OK |
| 4 | Correr `python validadores/mapa_tareas.py` sobre el repositorio | Escribe `base/mapa-de-tareas.md` con `N1` a `N10` bajo sus tareas |
| 5 | Abrir un enlace del mapa | Lleva a la regla |

**Resultado esperado final:** el mapa lo escribe el programa y sigue a las reglas.

### CP-004 · Versionado y pruebas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / RNF-01, RNF-02 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-05 y la T-07 terminadas |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y `validadores/tests/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `39.2.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `39.2.0`, marcada `**MENOR**`, en palabras llanas |
| 3 | Correr `python validadores/validar.py versionado` y `python -m unittest test_la_entrada_del_registro_se_entiende` desde `validadores/tests` | 0 fallas y OK |
| 4 | Buscar el archivo de pruebas nuevo | Existe en `validadores/tests/` |

**Resultado esperado final:** el cambio queda registrado y el programa tiene sus pruebas.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) de la fase | 100% |
| Fallas de `metareglas`, `estandar` y `versionado` | Conteo | 0 |
| Pruebas nuevas | Pasan / corren | Todas |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | «Apruebo», en el chat | 2026-09-28 |
