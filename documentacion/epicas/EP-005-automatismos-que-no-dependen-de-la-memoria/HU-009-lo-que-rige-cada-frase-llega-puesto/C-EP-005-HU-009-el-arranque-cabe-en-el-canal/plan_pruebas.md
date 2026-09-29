# Plan de Pruebas · Fase `C-EP-005-HU-009-el-arranque-cabe-en-el-canal`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-009-C |
| **Versión** | 2.0: suma el CP-005, ningún texto describe el arranque viejo |
| **Alcance del plan** | HU-009, CA-04 y RNF-01, RNF-02 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado: la versión 1.0 y la 2.0, las dos el 2026-09-28 |

## 3. Estrategia de pruebas

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Que el recorte de memoria e histórico respete el tope y diga dónde está el resto | El agente | Carpeta temporal | Sí |
| Sistema | Que el enganche entregue 10.000 caracteres o menos en el estándar, en un proyecto y con el gate | El agente | Local y carpeta temporal | Sí |
| Aceptación | Que lo entregado se entienda | El usuario | Local | No, leyendo la salida |
| Regresión | Que el gate y el tiempo del arranque sigan igual | El agente | Local | Sí |

Se corren solo las pruebas que la fase toca (`02·F5`): `test_las_reglas_llegan_al_propio_estandar`, los casos de `cargador`, `recuerdos` e `historico` en `pruebas.py`, el caso de arranque de `evals/`, y `validar.py estandar` y `versionado`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | [CA-04](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-04--lo-que-entrega-el-arranque-cabe-entero-y-dice-cómo-llegan-las-reglas) | [CP-001](#cp-001--el-arranque-cabe-y-dice-cómo-llegan-las-reglas), [CP-002](#cp-002--lo-que-no-cabe-se-recorta-y-se-dice), [CP-003](#cp-003--los-claudemd-dicen-cómo-llegan-las-reglas), [CP-005](#cp-005--ningún-texto-describe-el-arranque-viejo) | Funcional | Crítica | Parcial | ☐ |
| HU-009 | RNF-01, RNF-02 | [CP-002](#cp-002--lo-que-no-cabe-se-recorta-y-se-dice), [CP-004](#cp-004--tiempo-versionado-y-pruebas) | No funcional | Media | Sí | ☐ |

**Cobertura:** 3 de 3 exigencias de esta fase cubiertas, 100%.

Se corren también las pruebas de `hook_reglas.py` y de `recuperar.py`, que toca la T-09.

## 6. Casos de prueba

### CP-001 · El arranque cabe y dice cómo llegan las reglas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01, la T-03 y la T-06 terminadas |
| **Datos de entrada** | El repositorio, y un proyecto de prueba en carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `hook_sesion.py --raiz <estándar>` y contar los caracteres de `additionalContext` | 10.000 o menos; código 0 |
| 2 | Lo mismo con un proyecto de prueba que pasa el gate | 10.000 o menos, con la revisión de arranque |
| 3 | Lo mismo con una carpeta que no pasa el gate | 10.000 o menos, con el gate y sin la instrucción de trabajo |
| 4 | Buscar en lo entregado del paso 1 | Dice que las reglas llegan con cada mensaje, nombra `base/mapa-de-tareas.md`, y trae la memoria |
| 5 | Buscar en lo entregado del paso 1 el texto de las reglas | No trae `## N1 ·` ni `[REGLAS BASE DEL ESTÁNDAR` |
| 6 | Correr el caso de arranque de `evals/` | Pasa |

**Resultado esperado final:** en los tres arranques, lo entregado cabe en el canal y llega entero.

### CP-002 · Lo que no cabe se recorta y se dice

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-04, RNF-02 |
| **Tipo** | Funcional, error |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-02, la T-03 y la T-06 terminadas |
| **Datos de entrada** | Una memoria de prueba de 20.000 caracteres en carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `recuerdos.contexto()` con un tope de 3.000 | 3.000 caracteres o menos, sin líneas cortadas, y la ruta de `historico-chat/memory/memory.md` |
| 2 | Pedir `historico.contexto()` con un tope de 1.000 | 1.000 o menos, con la ruta del índice del histórico |
| 3 | Correr el enganche sobre el proyecto de prueba con esa memoria | 10.000 o menos, y el bloque `[LO QUE NO CUPO EN EL ARRANQUE]` dice qué se recortó |
| 4 | Pedir los dos sin tope | Igual que hoy |

**Resultado esperado final:** nada se pierde en silencio: lo recortado queda nombrado con su ruta.

### CP-003 · Los CLAUDE.md dicen cómo llegan las reglas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-04 |
| **Tipo** | Documental |
| **Prioridad** | Alta |
| **Precondiciones** | La T-04 y la T-05 terminadas |
| **Datos de entrada** | `CLAUDE.md`, `plantillas/CLAUDE.md.plantilla`, `validadores/docs/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `CLAUDE.md` §0 | No pide cargar todos los archivos de `base/`; dice que llegan con cada mensaje y nombra el mapa |
| 2 | Leer el paso 2 del arranque en la plantilla | Lo mismo |
| 3 | Leer `validadores/docs/cargador.md` y `hook_sesion.md` | El tope de 10.000 caracteres y el ejemplo de salida nuevo |

**Resultado esperado final:** ningún documento pide lo que el arranque ya no hace.

### CP-004 · Tiempo, versionado y pruebas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / RNF-01 |
| **Tipo** | No funcional, trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-06 y la T-07 terminadas |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y las pruebas tocadas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir el arranque en el estándar | Menos de 3 segundos |
| 2 | Abrir `VERSION` y `CHANGELOG.md` | `39.4.0`, entrada `**MENOR**` en palabras llanas |
| 3 | Correr `validar.py versionado`, `validar.py estandar` y las pruebas de la sección 3 | 0 fallas y OK |

**Resultado esperado final:** el arranque sigue rápido, el cambio queda registrado y lo nuevo tiene sus pruebas.

### CP-005 · Ningún texto describe el arranque viejo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-04 |
| **Tipo** | Documental |
| **Prioridad** | Alta |
| **Precondiciones** | La T-09 a la T-15 terminadas |
| **Datos de entrada** | El repositorio, sin `historico-chat/`, `plataforma/`, `CHANGELOG.md`, `pendientes/hecho/` ni las fases cerradas, que quedan sellados con su versión |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar «CARGADAS, OBLIGATORIAS», «volcado del arranque», «igual que las del arranque», «se cargan solas», «reglas llegan al abrir» y «carga reglas» | Ninguno, fuera de lo que cuenta cómo era antes de la 39.4.0 |
| 2 | Leer las filas de `hook_sesion.py` y `cargador.py` en `anatomia/mapa-del-sitio.md` y la fila «Cargador» de `base/glosario.md` | Dicen lo que hacen ahora |
| 3 | Leer el punto 7 de `notas/compactacion-mata-decisiones.md` | Dice lo que hace el arranque tras resumir la conversación |
| 4 | Leer RN-01 a RN-03 y CA-01 de HU-009, y revisar sus marcas de redacción | Anotados como reemplazados; cero marcas fuera de los bloques de código |
| 5 | Mandar un mensaje con `hook_reglas.py` y leer los avisos | No mencionan las reglas del arranque |
| 6 | Correr las pruebas de `hook_reglas.py` y de `recuperar.py` | OK |

**Resultado esperado final:** la HU cierra sin textos que contradigan lo construido.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) de la fase | 100% |
| Caracteres del arranque | Largo de `additionalContext`, en los tres arranques | 10.000 o menos |
| Fallas de `estandar` y `versionado` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | Versión 1.0 y versión 2.0: «Apruebo los dos planes. Hágalo», en el chat | 2026-09-28 |
