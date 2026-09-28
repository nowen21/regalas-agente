# Plan de Pruebas · Fase `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-023-B |
| **Versión** | 2.0: suma el CP-005 del recuperador (CA-07) |
| **Alcance del plan** | HU-023, CA-04 a CA-07 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado: la versión 1.0 y la 2.0, las dos el 2026-09-28 |

## 3. Estrategia de pruebas

Los casos que rompen algo a propósito corren en carpetas temporales. El resto corre sobre el repositorio.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Que el validador y la corrección del amarre reporten lo que deben | El agente | Carpeta temporal | Sí |
| Sistema | Que el repositorio quede con 0 reglas sin tareas y el amarre completo | El agente | Local | Sí, con `validar.py` |
| Aceptación | Que las tareas de cada regla tengan sentido | El usuario | Local | No, con el resumen por tarea |
| Regresión | Que `metareglas`, `estandar` y las pruebas del instalador sigan sin fallas | El agente | Local | Sí |

Se corren solo los validadores y las pruebas que la fase toca (`02·F5`): `tareas`, `amarre`, `metareglas`, `estandar`, `versionado`, y las pruebas del mapa de tareas, del amarre, del instalador y del recuperador.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-023 | [CA-04](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-04--el-validador-detecta-lo-que-falta-o-no-cuadra) | [CP-001](#cp-001--el-validador-detecta-lo-que-no-cuadra) | Funcional, error | Crítica | Sí | ☐ |
| HU-023 | [CA-05](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-05--toda-regla-vigente-declara-sus-tareas) | [CP-002](#cp-002--todas-las-reglas-declaran-sus-tareas) | Funcional | Crítica | Parcial | ☐ |
| HU-023 | [CA-06](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-06--el-mapa-del-amarre-no-da-por-clasificado-lo-que-solo-se-nombra) | [CP-003](#cp-003--el-amarre-no-se-deja-enganar) | Funcional, error | Crítica | Sí | ☐ |
| HU-023 | [CA-07](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-07--el-recuperador-trae-las-reglas-de-la-tarea-que-pide-el-mensaje) | [CP-005](#cp-005--el-recuperador-trae-las-reglas-de-la-tarea) | Funcional | Crítica | Sí | ☐ |
| HU-023 | RNF-01, RNF-02 | [CP-004](#cp-004--versionado-y-pruebas) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 6 de 6 exigencias de esta fase cubiertas, 100%.

## 6. Casos de prueba

### CP-001 · El validador detecta lo que no cuadra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-04 |
| **Tipo** | Funcional, error |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 a la T-04 terminadas |
| **Datos de entrada** | Reglas de prueba en carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En la prueba, una regla vigente sin línea `**Aplica a:**` | Falla, nombrando la regla |
| 2 | En la prueba, una regla con una tarea que no está en la lista | Falla, nombrando la regla y la tarea |
| 3 | En la prueba, cambiar una tarea sin volver a escribir el mapa | Falla, diciendo que el mapa quedó viejo |
| 4 | En la prueba, una regla derogada sin línea | No se reporta |
| 5 | En la prueba, una carpeta sin `base/tareas.md` | No reporta nada |
| 6 | Buscar `tareas` en el bucle del `pre-push` de `instalar.py` y en `.githooks/pre-push` | Está en los dos |

**Resultado esperado final:** el validador falla en los tres casos que la HU pide, no molesta donde no hay reglas, y corre antes de cada publicación.

### CP-002 · Todas las reglas declaran sus tareas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-05 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-05 a la T-07 terminadas |
| **Datos de entrada** | El repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python validadores/validar.py tareas` | 0 fallas |
| 2 | Contar las reglas distintas del mapa y las vigentes que cuenta `metareglas.py` | 252 y 252 |
| 3 | Correr `python validadores/validar.py metareglas` | Ninguna regla con el sello vencido ni con el largo cambiado |
| 4 | Mostrarle al usuario cuántas reglas quedaron en cada tarea | El usuario lo lee |

**Resultado esperado final:** ninguna regla vigente queda fuera del mapa, y ninguna cambió qué exige.

### CP-003 · El amarre no se deja engañar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-06 |
| **Tipo** | Funcional, error |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-08 a la T-10 terminadas |
| **Datos de entrada** | Un mapa de prueba en carpeta temporal, y el repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En la prueba, un programa nombrado solo en una frase del mapa | Se reporta sin clasificar |
| 2 | En la prueba, el mismo programa en una fila de tabla | No se reporta |
| 3 | En la prueba, el mismo programa en una línea que solo lista nombres | No se reporta |
| 4 | Correr `python validadores/validar.py amarre` | 0 fallas |
| 5 | Correr `python -m unittest test_el_mapa_del_amarre_no_envejece` desde `validadores/tests` | OK, sin las 3 fallas de la línea base |

**Resultado esperado final:** solo se da por clasificado lo que está clasificado, y el mapa del amarre queda completo.

### CP-004 · Versionado y pruebas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / RNF-01, RNF-02 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-04, la T-09 y la T-11 terminadas |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y `validadores/tests/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `39.3.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `39.3.0`, marcada `**MENOR**`, en palabras llanas |
| 3 | Correr `python validadores/validar.py versionado` y `test_la_entrada_del_registro_se_entiende` | 0 fallas y OK |
| 4 | Correr las pruebas del mapa de tareas, del amarre y del instalador | OK |

**Resultado esperado final:** el cambio queda registrado y lo nuevo tiene sus pruebas.

### CP-005 · El recuperador trae las reglas de la tarea

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-07 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-13 a la T-16 terminadas |
| **Datos de entrada** | Mensajes reales de la sesión del 2026-09-28 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasarle al recuperador «suba a git» | Trae `00·N2`, más las de `recibir-pedido` y `responder` |
| 2 | Pasarle «aplique las reglas de la caja de reglas de redacción al readme» | Trae `00·ID8`, `00·ID9`, `00·ID11` y `00·ID12` |
| 3 | Pasarle «cree el pendiente del H2» | Trae `02·F23` y `01·C28` |
| 4 | Pasarle «hola» | Trae solo las de `recibir-pedido` y `responder` |
| 5 | Medir el tamaño de lo que se inyecta en los cuatro | Dentro del tope de 10 KB, o con lo que no cupo nombrado |
| 6 | Correr los casos del recuperador de `validadores/pruebas.py` | OK |
| 7 | Abrir `.claude/settings.json` del estándar | `hook_reglas.py` está en `UserPromptSubmit` |

**Resultado esperado final:** con cada mensaje, el agente recibe las reglas de la tarea que el mensaje pide, sin adivinar por palabras sueltas.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) de la fase | 100% |
| Reglas vigentes sin tareas | Conteo de `validar.py tareas` | 0 |
| Fallas de `amarre`, `metareglas`, `estandar` y `versionado` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | Versión 1.0: «Apruebo los dos planes», en el chat. Versión 2.0: «Apruebo los dos planes», en el chat | 2026-09-28 |
