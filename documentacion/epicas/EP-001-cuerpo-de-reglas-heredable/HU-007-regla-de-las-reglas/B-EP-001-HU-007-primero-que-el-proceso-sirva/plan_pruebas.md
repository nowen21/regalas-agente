# Plan de Pruebas — Fase B-EP-001-HU-007-primero-que-el-proceso-sirva   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-001-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-001-HU-007-primero-que-el-proceso-sirva` · [HU-007](../HU-007-regla-de-las-reglas.md), `CA-05` |
| **Fecha** | 2026-08-21 |
| **Elaborado por** | El agente, por orden del usuario |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Formato proporcional a una sola fase: secciones 3, 5, 6, 9 y 12. El entregable que se prueba es un criterio escrito (`20·M19`), así que las pruebas son de análisis sobre casos reales del repositorio, no de código.

---

## 3. Estrategia de pruebas

**Un solo nivel: aceptación sobre documentos.** `M19` es una regla de criterio —así quedó registrada en [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md): la juzga una persona, no un programa—, de modo que probarla es aplicarla a casos cuyo desenlace correcto **ya se conoce por otra vía**, y comprobar que la regla llega al mismo desenlace por sus propios pasos.

**La técnica es la del oráculo histórico.** Los tres casos son hechos medidos del propio repositorio, anteriores a la regla, con su resultado documentado:

| Caso | El hecho, ya documentado | Lo que la regla tiene que hacer con él |
|---|---|---|
| Ítem 06 del [backlog de automatizaciones](../../../../../pendientes/hecho/autonomia-sin-ia.md) (gate `F2` mecánico) | Prioridad Alta y aun así relegado al penúltimo lugar: sin los ítems 04 y 12, «su tasa de falsos positivos lo vuelve inservible» | **Detenerlo** por la tercera pregunta, con ese mismo motivo |
| Ítem 01 del mismo backlog (guardián de versión y CHANGELOG) | «Se publicaron dieciséis commits seguidos sin que corriera nada solo. Corría porque el agente se acordaba» | **Dejarlo pasar**: solo fallaba acordarse, y eso es automatizar ya |
| La regla `F4` antes de partirse | Reprobó su propio checklist por exigir dos cosas; de ahí salieron `F4.1`-`F4.5` (hoy derogadas hacia `F14`-`F18`) | **Mandar corregir la regla** por la segunda pregunta, antes que construirle validador |

**Sin ejecución automatizada.** Ningún caso corre programas que cambien estado; el único comando es de lectura (`validar.py vigencia`, que ya existe y es la fuente del dato de la segunda pregunta).

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| [HU-007](../HU-007-regla-de-las-reglas.md) | [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | [CP-001](#cp-001--el-criterio-detiene-lo-que-debía-detener), [CP-002](#cp-002--el-criterio-deja-pasar-lo-que-debía-pasar), [CP-003](#cp-003--el-criterio-manda-corregir-antes-que-automatizar) | Aceptación / análisis | Crítica | No | ☐ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100%. La HU no declara RNF nuevos para esta fase; los tres de su §5 son de la HU entera y los cierra la fase que la termine.

**Los tres casos son los tres brazos del «Aprobado cuando» del CA:** detiene el que debía detener (CP-001), deja pasar el que debía pasar (CP-002), y manda corregir antes que automatizar el que estaba mal escrito (CP-003). El cuarto brazo —que el criterio esté escrito como regla del capítulo `20`— lo cubre la línea base del plan de trabajo (§2): `M19` existe y su checklist está en CUMPLE.

---

## 6. Casos de prueba

### CP-001 — El criterio detiene lo que debía detener

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-05 |
| **Tipo** | Aceptación — el freno |
| **Prioridad** | Crítica |
| **Precondiciones** | [`M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) escrita; el [pendiente 09](../../../../../pendientes/hecho/autonomia-sin-ia.md) con su ítem 06 documentado |
| **Datos de entrada** | El ítem 06 del backlog: gate `F2` mecánico (código sin especificación) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el pendiente 09 y localizar la fila del ítem 06 y su nota de orden | La fila existe, prioridad **Alta**, y la nota dice que va casi al final |
| 2 | Aplicarle la primera pregunta de `M19`: ¿la regla (`F2`) se cumple hoy a mano y produce el resultado buscado? | Queda la respuesta escrita, con su evidencia |
| 3 | Aplicarle la tercera pregunta: ¿cuántas falsas alarmas daría automatizada tal como está? | La respuesta la da el propio backlog: sin los ítems 04 y 12, su tasa de falsos positivos lo vuelve inservible |
| 4 | Contrastar el desenlace de `M19` con lo que el backlog decidió caso por caso | Coinciden: no se construye todavía. El criterio llega por regla a donde el backlog llegó por tropiezo |

**Resultado esperado final:** la tercera pregunta detiene el ítem 06, con el mismo motivo que el backlog anotó a mano.
**Postcondiciones:** ninguna — análisis sobre documentos, nada cambia de estado.

---

### CP-002 — El criterio deja pasar lo que debía pasar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-05 |
| **Tipo** | Aceptación — el corte contra el abuso |
| **Prioridad** | Crítica |
| **Precondiciones** | Las mismas de CP-001 |
| **Datos de entrada** | El ítem 01 del backlog: guardián de versión y CHANGELOG, en el estado que tenía **antes** de construirse |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Localizar en el pendiente 09 la evidencia del estado del ítem 01 antes de construirse | Queda a la vista: dieciséis commits seguidos publicados sin que corriera nada solo; corría porque el agente se acordaba |
| 2 | Aplicarle la primera pregunta: ¿la regla (`20·M10`, versionar todo cambio) se cumplía a mano? | Sí: las entradas del CHANGELOG existían; lo que fallaba era el olvido, no la regla |
| 3 | Aplicarle la segunda pregunta: ¿los incumplimientos fueron por descuido o por regla mal escrita? | Por descuido (acordarse), no por redacción |
| 4 | Aplicar la última frase de `M19`: si lo único que falla es acordarse, se automatiza ya | El criterio no lo frena. Y el hecho posterior lo confirma: se construyó (`versionado.py`, `numeracion.py`, enganche de pre-commit) y quedó en verde |

**Resultado esperado final:** el criterio deja pasar el ítem 01 sin frenarlo — la prueba de que `M19` no sirve de excusa para no automatizar nunca.
**Postcondiciones:** ninguna.

---

### CP-003 — El criterio manda corregir antes que automatizar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-05 |
| **Tipo** | Aceptación — el orden correcto |
| **Prioridad** | Crítica |
| **Precondiciones** | La historia de `F4` documentada en el capítulo `02`: la regla original, sus piezas `F4.1`-`F4.5` y las derogaciones hacia `F14`-`F18` |
| **Datos de entrada** | La regla `F4` en su versión anterior a la partición, que exigía más de una cosa |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar en `base/02-flujo-de-trabajo/reglas/` que existen `F4`, las cinco `F4.x` derogadas y sus sucesoras | Los archivos están, y cada `F4.x` declara su derogación con destino |
| 2 | Aplicarle a la `F4` de entonces la segunda pregunta de `M19`: ¿se incumplía por descuido o por estar mal escrita? | Por estar mal escrita: exigía varias cosas a la vez, contra `20·M5` |
| 3 | Seguir lo que `M19` dice para esa respuesta | Manda **corregir la regla** —partirla— antes que construirle validador |
| 4 | Contrastar con lo que de verdad pasó | Coincide: la regla se partió primero (`F4.1`-`F4.5`, luego `F14`-`F18` con ID limpio), y el validador de forma llegó después, sobre reglas de una sola exigencia |

**Resultado esperado final:** ante una regla doble, `M19` produce el mismo orden que la historia real: primero la regla, después el programa. De haberse automatizado tal cual, el validador habría congelado la regla doble.
**Postcondiciones:** ninguna.

---

## 9. Gestión de defectos

Si un caso no da lo esperado, el defecto se registra en el `resultado_pruebas.md` §4 con su severidad, y la fase **no cierra** con un defecto crítico o alto abierto. En particular: si `M19` no alcanza el desenlace esperado de un caso, la regla está mal escrita o mal probada — se pausa y se propone (`02·F20`); **no se edita la regla para que la prueba pase**, porque editarla anula su checklist.

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | CA con caso / CA totales de la fase | 100% (1 de 1) |
| Casos ejecutados | Ejecutados / diseñados | 100% (3 de 3) |
| Tasa de aprobación | Aprobados / ejecutados | 100% — con uno fallido la fase no cierra |

El resumen de la ejecución, el veredicto por criterio y el concepto final viven en el `resultado_pruebas.md` de la fase. Este plan define qué se mide; aquel dice cuánto dio.
