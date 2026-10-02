# Resultado de Pruebas · Fase `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si cada criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador` |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 2.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-01 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `292ac33` más los cambios de la fase |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001: `02·F0` pide el análisis en los tres puntos de reparto**

**El problema que resuelve:** sin esto, la cadena no pide analizar antes de repartir el trabajo, y el alcance se decide al construir.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el cuerpo de `F0` | Pide el análisis antes de las épicas, antes de las HU de cada épica y cada vez que entra un pendiente | «con un análisis antes de las épicas, de las HU de cada épica y de cada pendiente» |
| 2 | Comparar sus eslabones con la versión 39.6.0 | No falta ninguno | Siguen los seis: planteamiento, épica, HU, especificación, plan y código |
| 3 | Medir el cuerpo de `F0` | Cabe en 320 caracteres | 318 caracteres leídos |
| 4 | Correr `python validadores/validar.py metareglas` | Sin fallas en `F0` | `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** el paso 1 prueba el criterio; el 3 y el 4 prueban que la regla sigue dentro del molde con el texto nuevo.

**CA-04 · CP-002: `02·F23` pone el análisis antes de la HU**

**El problema que resuelve:** sin esto, un pendiente baja a la HU sin que nadie haya fijado su alcance.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el cuerpo de `F23` | El pendiente pasa por su análisis antes de bajar a la HU | «el pendiente aprobado pasa por su análisis, baja a una historia de usuario» |
| 2 | Medir el cuerpo de `F23` | Cabe en 320 caracteres | 315 caracteres leídos |
| 3 | Correr `python validadores/validar.py metareglas` | Sin fallas en `F23` | `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** el paso 1 prueba el criterio; el 2 y el 3, que cabe en el molde.

**CA-05 · CP-003: `DOC8` derogada y `DOC24` y `DOC25` en su lugar**

**El problema que resuelve:** sin esto, conviven dos formas de cerrar un análisis y cada proyecto escoge la suya.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `DOC8` | Título con `[DEROGADA en 40.0.0 → ver 13·DOC24 y 13·DOC25]`, nota de por qué y el texto original | Así quedó, con su texto original debajo de la nota |
| 2 | Leer `DOC24` | El análisis individual cierra al final de su mismo archivo y no se reescribe | Lo dice, con su ejemplo INCORRECTO / CORRECTO |
| 3 | Leer `DOC25` | El análisis principal se reescribe con su lista de cambios | Lo dice, con su ejemplo INCORRECTO / CORRECTO |
| 4 | Buscar `DOC8` en `base/`, `plantillas/` y `validadores/` | Solo aparece en la regla derogada, en las que la reemplazan y en el CHANGELOG | También aparece en `validadores/reglas-antes-de-la-accion.md`, que es una foto fechada del 2026-09-16 y no una cita viva; no se tocó. `base/mapa-de-tareas.md` ya no la nombra |
| 5 | Leer `validadores/reglas-validables.md` | `DOC24` y `DOC25` están registradas | Están, en la lista de las que no valida un programa, con el porqué |
| 6 | Correr `python validadores/validar.py metareglas` | Sin fallas en `DOC8`, `DOC24` ni `DOC25` | `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 prueban el criterio; el 4 y el 5, que nada quedó citando la regla vieja como vigente. El paso 4 salió con un archivo de más, y se explica en la misma fila.

**CA-02 y CA-16 · CP-004: la plantilla del análisis**

**El problema que resuelve:** sin plantilla, cada análisis toma otra forma y el validador no sabe qué buscar.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `plantillas/analisis.md` | Trae las siete partes del criterio | Las trae: la tabla de reglas, el hallazgo, el pendiente, la conversación, lo que aportó cada parte, las conclusiones, las lecciones y lo que se tiene que hacer |
| 2 | Leer la tabla de HU de su propuesta final | Pide la parte del problema que resuelve cada HU | Tiene la columna «Parte del problema que resuelve» |
| 3 | Correr `python validadores/validar.py plantilla plantillas/analisis.md` | La plantilla está registrada y pasa | `0 falla(s)`; los 24 avisos son sus propias notas, que se borran al llenarla |
| 4 | Contar sus marcas con `validadores/marcas.py` | Cero marcas | 0 |

**Cómo se verificó que la pareja cumple:** el paso 1 cubre el CA-02 y el 2 el CA-16. El plan nombraba el subcomando `plantillas`; el que existe es `plantilla`.

**CA-06 · CP-005: el análisis sin una de las cuatro partes no cierra**

**El problema que resuelve:** sin esto, un análisis se aprueba sin revisar lo que ya existe, lo aprendido o el entorno, y esas brechas salen como hallazgos al ejecutar.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `python validadores/validar.py analisis` sobre el repositorio | Los análisis 1 a 5 del pendiente 103 pasan | `OK: sin incumplimientos` |
| 2 | Copiar el análisis 3 a una carpeta temporal sin la sección «Lo aprendido» y correr `analisis.revisar` | Falla y nombra la sección | `x/analisis-3.md: falta la sección «Lo aprendido»` |
| 3 | Copia aprobada sin la sección del entorno | Falla y nombra la sección | Probado en `test_al_aprobado_sin_el_entorno_se_le_nombra`: falla y nombra «El entorno» |
| 4 | Copia sin la marca «Aprobado» y sin una sección | Pasa | Probado en `test_el_abierto_incompleto_todavia_no_se_juzga`: pasa |
| 5 | Correr `python -m unittest validadores/tests/test_analisis.py` | En verde | `Ran 6 tests · OK` |
| 6 | Comprobar que `validadores/analisis.py` está en el mapa del sitio | Está | Está en el árbol de `anatomia/mapa-del-sitio.md`. Se comprobó leyendo: `validar.py sitio` solo revisa las carpetas de primer nivel, no los validadores |

**Cómo se verificó que la pareja cumple:** el paso 2 es el que decide, sobre un análisis real; el 1 prueba que el validador no da alarmas falsas sobre los análisis que sí están completos.

**CA-07 · CP-006: la versión 40.0.0**

**El problema que resuelve:** sin esto, los proyectos que heredan no se enteran de que una regla dejó de regir.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `VERSION` | 40.0.0 | `40.0.0` |
| 2 | Leer la entrada del CHANGELOG | «⚠ obliga a migrar», lo que cada proyecto tiene que hacer, `20·M10` y `02·F22` | Las trae |
| 3 | Correr `python validadores/validar.py metareglas` (fila 19) y `tareas` | Sin fallas | Los dos, `OK: sin incumplimientos` |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 prueban el criterio. El plan nombraba `validar.py versionado`, que revisa secretos y artefactos; la fila 19 la revisa `metareglas`. Su primer aviso pidió reescribir el comienzo de la entrada sin identificadores ni rutas (`20·M17`), y así quedó.

**RNF-06 · CP-007: cada criterio cita su origen**

**El problema que resuelve:** sin esto, lo construido no se puede rastrear hasta lo que se decidió.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Revisar que cada tarea del plan cite su CA y cada CA su «Sale de» | Ninguna sin origen | Las ocho tareas citan su CA; los siete CA citan su punto |

**Cómo se verificó que la pareja cumple:** lectura del plan y de la HU.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | 2026-10-01 | Cuerpo de `F0` leído y medido: 318 caracteres; `metareglas` sin fallas | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-04 | Alta | 2026-10-01 | Cuerpo de `F23` leído y medido: 315 caracteres; `metareglas` sin fallas | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-05 | Alta | 2026-10-01 | `DOC8` derogada, `DOC24` y `DOC25` leídas, búsqueda de `DOC8` | Aprobado | EV-01, EV-02 | Ninguno |
| CP-004 | CA-02, CA-16 | Alta | 2026-10-01 | `plantillas/analisis.md` leída; `validar.py plantilla` sin fallas; 0 marcas | Aprobado | EV-03 | Ninguno |
| CP-005 | CA-06 | Crítica | 2026-10-01 | `validar.py analisis` sobre el repositorio; copia del análisis 3 sin «Lo aprendido»; 6 pruebas | Aprobado | EV-04 | Ninguno |
| CP-006 | CA-07 | Media | 2026-10-01 | `VERSION` en 40.0.0; entrada del CHANGELOG; `metareglas` y `tareas` sin fallas | Aprobado | EV-01 | Ninguno |
| CP-007 | RNF-06 | Media | 2026-10-01 | Lectura del plan y de la HU | Aprobado | EV-05 | Ninguno |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** el plan nombraba tres subcomandos que no son los que existen o no miran lo que decía: `plantillas` (es `plantilla`), `versionado` (revisa secretos; la versión la revisa `metareglas`) y `sitio` (no revisa validadores). Se corrió el que sí lo comprueba y se dice en cada caso.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que `analisis.py` esté en el mapa del sitio | Lectura del árbol de `anatomia/mapa-del-sitio.md` | Está |
| 2 | Que ningún archivo cambiado sume marcas de redacción | `marcas.py`, comparando cada archivo contra el commit anterior | Ninguno sumó |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-004 | Aprobado | Sí |
| CA-04 | CP-002 | Aprobado | Sí |
| CA-05 | CP-003 | Aprobado | Sí |
| CA-06 | CP-005 | Aprobado | Sí |
| CA-07 | CP-006 | Aprobado | Sí |
| CA-16 | CP-004 | Aprobado | Sí |
| RNF-06 | CP-007 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 8 de 8 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 7 de 7 | Sí |
| Tasa de aprobación | Plan §12.1 | 100% | 7 de 7 | Sí |
| Casos críticos y altos | Plan §3.4 | 100% | 5 de 5 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 1: el H-4, que detuvo la versión 1 del plan antes de empezar | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los siete criterios de la fase y el RNF-06 tienen su caso ejecutado y aprobado. Ningún defecto.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de `validar.py metareglas` y `tareas` | Transcripción de la sesión del 2026-10-01 |
| EV-02 | Búsqueda de `DOC8` | Transcripción de la sesión del 2026-10-01 |
| EV-03 | `plantillas/analisis.md` y la salida de `validar.py plantilla` | El archivo y la transcripción |
| EV-04 | `validadores/tests/test_analisis.py` y la salida de `validar.py analisis` | El archivo y la transcripción |
| EV-05 | El plan de trabajo y la HU-001 | Esta carpeta y la de la HU |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-01 | 7 | 0 | Primera ejecución |
