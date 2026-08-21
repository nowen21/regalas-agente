# Resultado de Pruebas — Fase B-EP-001-HU-007-primero-que-el-proceso-sirva   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-001-HU-007-primero-que-el-proceso-sirva` |
| **HU** | [HU-007](../HU-007-regla-de-las-reglas.md) — `CA-05` |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), aprobado por el usuario el 2026-08-21 («si», junto con la confirmación de la opción 1 del pendiente 16) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-21 |
| **Ejecutado por** | El agente; los juicios de cada pregunta quedan escritos para que el usuario los revise |
| **Ambiente y versión** | Este repositorio, árbol de trabajo sin commitear, estándar 28.0.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

**CA-05 · CP-001 — el criterio detiene lo que debía detener**

**El problema que resuelve:** si `M19` no frena una automatización prematura, una regla con proceso inmaduro se construye igual y falla sola en cada commit — que es el defecto que la regla vino a cerrar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir el [pendiente 09](../../../../../pendientes/hecho/autonomia-sin-ia.md) y localizar la fila del ítem 06 y su nota de orden | La fila existe, prioridad **Alta**, y la nota dice que va casi al final | Fila en la tabla del backlog: `06 · Gate F2 mecánico · Alta · Alta`. El orden sugerido lo deja de **penúltimo** («... → 15 → 06 → 16») y la nota dice: «El 06 va casi al final a pesar de ser prioridad Alta: se apoya en el 04 y en el 12, y sin ellos su tasa de falsos positivos lo vuelve inservible» |
| 2 | Aplicarle la primera pregunta de `M19`: ¿la regla (`02·F2`) se cumple hoy a mano y produce el resultado buscado? | Queda la respuesta escrita, con su evidencia | Sí se cumple como criterio —las fases llevan su plan aprobado—, pero su sección lo dice claro: «es la única de las 13 estaciones del orquestador que nada comprueba mecánicamente. Si el agente se la salta, no queda señal» |
| 3 | Aplicarle la tercera pregunta: ¿cuántas falsas alarmas daría automatizada tal como está? | La respuesta la da el propio backlog | Las suficientes para volverlo inservible: «un refactor legítimo toca archivos que ningún plan nombró»; sus recomendaciones ordenan «**No construirlo antes que el 03 y el 12**, que son los que hacen fiables las otras dos listas», y empezar en modo AVISO solo por archivos nuevos |
| 4 | Contrastar el desenlace de `M19` con lo que el backlog decidió caso por caso | Coinciden: no se construye todavía | Coinciden. Y la historia lo confirma: la tabla final del pendiente muestra que el 06 (`flujo.py`) solo se construyó cuando el 03, el 04 y el 12 ya existían — el orden que `M19` habría impuesto por regla se cumplió por tropiezo, descubierto caso por caso |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que decide —la tercera pregunta detiene al ítem 06 con el mismo motivo que el backlog anotó a mano—, pero solo no alcanza: un criterio que detuviera todo habría «acertado» igual. Por eso está CP-002, que comprueba el caso contrario. El paso 4 agrega la confirmación histórica: la construcción real esperó exactamente a las piezas que la tercera pregunta echa de menos. Evidencia EV-01.

---

**CA-05 · CP-002 — el criterio deja pasar lo que debía pasar**

**El problema que resuelve:** el riesgo declarado del propio pendiente 16: que el criterio «sirva como excusa para no automatizar nunca, porque siempre se puede decir que el proceso todavía no está maduro».

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Localizar en el pendiente 09 la evidencia del estado del ítem 01 antes de construirse | Queda a la vista la evidencia de que solo fallaba acordarse | **Desvío declarado:** la cita del plan («dieciséis commits seguidos sin que corriera nada solo; corría porque el agente se acordaba») está en la sección del **ítem 08**, no del 01 — es el mismo patrón de falla, en otro ítem. La evidencia propia del 01 sí está en su sección: la regla existía y se cumplía, y «basta un despiste para que un proyecto herede una regla nueva sin que su número de versión cambie. Es una falla silenciosa» |
| 2 | Aplicarle la primera pregunta: ¿la regla (`20·M10`, versionar todo cambio) se cumplía a mano? | Sí: las entradas existían; fallaba el olvido, no la regla | Sí. El propio CHANGELOG es la evidencia: más de cien entradas escritas a mano antes de que existiera el guardián |
| 3 | Aplicarle la segunda pregunta: ¿los incumplimientos fueron por descuido o por regla mal escrita? | Por descuido, no por redacción | Por descuido: el pendiente lo llama «despiste». El único tropiezo documentado de fondo —las dos entradas `15.4.0`— fue de concurrencia entre sesiones, y lo resolvió `M18`, no una reescritura de `M10` |
| 4 | Aplicar la última frase de `M19`: si lo único que falla es acordarse, se automatiza ya | El criterio no lo frena | No lo frena. Y el hecho posterior lo confirma: se construyó (`versionado.py`, `numeracion.py`, el enganche de `pre-commit` — la tabla final del 09 lo marca ✅) y quedó operando |

**Cómo se verificó que la pareja cumple:** el paso 4 decide — ante un proceso que ya servía a mano, `M19` ordena automatizar ya, que es lo contrario de frenar. El desvío del paso 1 queda dicho en su fila y no cambia el veredicto: la decisión sale de las preguntas 1 y 2 aplicadas al ítem 01 con la evidencia de su propia sección; la cita mal atribuida era ilustración, no premisa. Evidencia EV-01.

---

**CA-05 · CP-003 — el criterio manda corregir antes que automatizar**

**El problema que resuelve:** automatizar una regla mal escrita es congelar el error y ponerlo a repetirse en cada commit.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar en `base/02-flujo-de-trabajo/reglas/` que existen `F4`, las cinco `F4.x` derogadas y sus sucesoras | Los archivos están, y cada `F4.x` declara su derogación con destino | Están los 31 archivos del capítulo: `F4`, `F4.1`-`F4.5` (cada una con su aviso «DEROGADA en 3.1.0 → ver F14...») y `F14`-`F18` vivas |
| 2 | Aplicarle a la `F4` de entonces la segunda pregunta de `M19`: ¿se incumplía por descuido o por estar mal escrita? | Por estar mal escrita: exigía varias cosas a la vez | Por mal escrita, y quedó medido: la auditoría del capítulo la reprobó en las filas 8 y 9 del checklist — «`F4`, `F4.3`, `F4.5` llevan dos exigencias que se cumplen por separado; partirlas crea IDs nuevos» (CHANGELOG), y «`F4.1` a `F4.5` ... nacieron de partir reglas más grandes» |
| 3 | Seguir lo que `M19` dice para esa respuesta | Manda corregir la regla —partirla— antes que construirle validador | Eso dice su texto: «Si se incumple porque está mal escrita, se corrige la regla» |
| 4 | Contrastar con lo que de verdad pasó | Coincide: primero la regla, después el programa | Coincide: `F4` se partió (primero `F4.1`-`F4.5`, luego con ID limpio `F14`-`F18` por `M4`), la `F4` de hoy quedó con una sola exigencia y checklist 20/20, y el validador de forma (`metareglas.py`, ítem 05 del backlog) llegó después, sobre reglas de una sola exigencia |

**Cómo se verificó que la pareja cumple:** el paso 3 decide y el 4 lo respalda con la historia real: el orden que `M19` exige es el que el estándar terminó siguiendo, con la diferencia de que entonces se descubrió a golpes y ahora está escrito como regla. El paso 1 deja el punto de partida verificable por cualquiera con un `ls`. Evidencia EV-02.

---

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | Crítica | 2026-08-21 | El ítem 06 del pendiente 09: su fila (Alta), su lugar penúltimo en el orden, su nota de falsos positivos y su tabla de construcción — la tercera pregunta lo detiene con ese mismo motivo | Aprobado | EV-01 | — |
| CP-002 | [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | Crítica | 2026-08-21 | El ítem 01 del pendiente 09: `M10` cumplida a mano (el CHANGELOG entero), falla solo de despiste — la última frase de `M19` lo deja pasar, y se construyó y quedó en verde | Aprobado | EV-01 | — |
| CP-003 | [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | Crítica | 2026-08-21 | La `F4` doble: reprobada en filas 8-9 por la auditoría, partida en `F4.1`-`F4.5` → `F14`-`F18` antes de que existiera `metareglas.py` — la segunda pregunta manda ese mismo orden | Aprobado | EV-02 | — |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** solo el desvío del paso 1 de CP-002 (cita del plan atribuida al ítem 01 cuando pertenece a la sección del 08), declarado en su fila y sin efecto sobre el veredicto.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Los tres casos completos — `M19` es regla de criterio: la juzga una persona, no un programa | Lectura y juicio sobre los documentos citados, con cada respuesta escrita en §2 | Los tres desenlaces de `M19` coinciden con el desenlace histórico documentado |
| 2 | Que ningún paso ejecutara algo que cambiara estado | Revisión de los pasos: todos son lecturas (`ls`, abrir archivos) | Nada cambió de estado; no se usaron datos reales |

---

## 4. Defectos encontrados

Ninguno.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | CP-001, CP-002, CP-003 | El criterio está escrito como regla del capítulo `20` (línea base del plan, checklist CUMPLE), detiene el caso que debía detener (CP-001), deja pasar el que debía pasar (CP-002) y manda corregir antes que automatizar el que estaba mal escrito (CP-003) — los cuatro brazos del «Aprobado cuando» | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura del CA de la fase | Plan §5 | 100% | 1 de 1 | Sí |
| Casos críticos ejecutados | Plan §12 | 100% | 3 de 3 | Sí |
| Tasa de aprobación | Plan §12 | 100% | 3 de 3 | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el único CA de la fase quedó en «Sí» con sus tres casos aprobados (§5): `M19` reproduce por regla los tres desenlaces que el repositorio ya había pagado por aprender caso por caso. El único desvío de ejecución (CP-002, paso 1) quedó declarado y no toca el veredicto.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Documento fuente con las citas de los ítems 01, 06 y 08 | [`pendientes/hecho/autonomia-sin-ia.md`](../../../../../pendientes/hecho/autonomia-sin-ia.md) — la tabla del backlog, el orden sugerido y su nota, las secciones 01 y 06, y la tabla final «las dieciséis están» |
| EV-02 | Los archivos de la partición y su registro | `base/02-flujo-de-trabajo/reglas/` (`F4`, `F4.1`-`F4.5` derogadas, `F14`-`F18`) y las entradas del [CHANGELOG](../../../../../CHANGELOG.md) sobre las filas 8-9 de `F4` y el nacimiento de `F4.1`-`F4.5` |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-21 | 3 | 0 | Primera ejecución |
