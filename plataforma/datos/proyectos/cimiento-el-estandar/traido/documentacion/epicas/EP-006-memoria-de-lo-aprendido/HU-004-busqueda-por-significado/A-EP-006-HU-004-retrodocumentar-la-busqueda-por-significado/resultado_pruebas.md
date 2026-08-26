# Resultado de pruebas — Fase A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` |
| **HU** | [HU-004](../HU-004-busqueda-por-significado.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-004 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Bases temporales, y una **copia** de `memoria/senales.db` (237 señales) para medir la mejora. Estándar 23.2.0 · Python 3.11.9 · modelo `minishlab/potion-base-8M`, presente en esta máquina |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 2 | 2 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). La búsqueda por significado **encuentra lo que la de palabra no encuentra** —eso quedó medido— y no pierde nada de lo que ya encontraba. Lo que falla es el CA-02: dice «sin el modelo la búsqueda sigue funcionando», y con las librerías instaladas pero **el modelo ausente la búsqueda se cae entera**, arrastrando también a la búsqueda por palabra, que no necesita nada.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--encuentra-la-señal-buscándola-con-otras-palabras) | CA-01 | Alta | 2026-08-17 | Base temporal, y tres consultas reales sobre la copia de 237 señales | Aprobado | EV-01, EV-02 | — |
| [CP-002](plan_pruebas.md#cp-002--lo-combinado-no-pierde-lo-que-la-búsqueda-por-palabra-encontraba) | CA-01 | Alta | 2026-08-17 | Las mismas consultas, con y sin significado | Aprobado, **con ruido medido** | EV-02 | D-03 |
| [CP-003](plan_pruebas.md#cp-003--sin-las-dependencias-la-búsqueda-responde-igual-y-lo-dice) | CA-02 | Crítica | 2026-08-17 | `semantica.disponible()` apagado, y el modelo apuntado a uno inexistente | **Falla el caso «sin el modelo»** | EV-01 | D-01 |
| [CP-004](plan_pruebas.md#cp-004--nada-sale-de-la-máquina) | Transversal | Crítica | 2026-08-17 | Indexar y buscar con el socket cortado | **Falla el paso 2** | EV-01 | D-02 |

---

### Detalle de CP-001 — Encuentra la señal buscándola con otras palabras

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar con las palabras exactas de la señal | La encuentra | La encuentra |
| 2 | Buscar con una consulta que no comparte **ninguna** palabra | La encuentra igual | La encuentra. «cayó la máquina sin RAM» trae «El servidor de correo dejó de responder por falta de memoria» |
| 3 | Comprobar que sin el modelo el paso 2 **no** la encontraría | No la encuentra | No la encuentra: la léxica devuelve vacío. **Eso es lo que aporta** |
| 4 | Repetir con tres consultas reales | Se anota cuántas mejoraron | **Las tres.** Ver la tabla de abajo |
| 5 | Anotar la medida de la mejora | Queda el dato | Anotada |

**Las tres consultas reales, sobre la copia de 237 señales:**

| Consulta | Léxica | Híbrida | Perdidos | Nuevos |
|---|---:|---:|---:|---:|
| «por qué se cayó el servidor» | **0** | 5 | 0 | 5 |
| «cómo se nombran las cosas» | **0** | 5 | 0 | 5 |
| «riesgo de perder datos» | **0** | 5 | 0 | 5 |

**Las tres mejoraron, y las tres partían de cero.** Es el dato que el plan pedía para decidir si vale instalarlo: escritas como las escribiría una persona —en preguntas, no en palabras clave—, la búsqueda por palabra **no devuelve absolutamente nada**.

---

### Detalle de CP-002 — Lo combinado no pierde lo que la búsqueda por palabra encontraba

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr las consultas sin significado | Queda la línea base | Vacía en las tres |
| 2 | Correr las mismas con significado | Salen resultados | Cinco en cada una |
| 3 | Comprobar que todo lo de la línea base sigue apareciendo | Nada se perdió | **Nada se perdió**, ni acá ni en la prueba automatizada con una consulta que sí tiene resultados léxicos |
| 4 | Anotar lo que aparece de más | Es la ganancia | 15 resultados donde antes había 0 |
| 5 | Anotar lo que aparece de más y **no** sirve | Es el ruido | **La mayoría es ruido.** Ver abajo |

**El ruido, medido.** Para «por qué se cayó el servidor», los cinco que devuelve son:

| Señal | De qué trata | ¿Sirve? |
|---|---|---|
| `S-098` | El recargador de Django corre en dos procesos | Parcialmente |
| `S-118` | Un aviso del framework que solo molesta en otra máquina | Parcialmente |
| `S-128` | Los dos casos espejo de una poda hacen falta los dos | **No** |
| `S-230` | Buscar la ruta vieja por `/uploads` no encuentra el defecto | **No** |
| `S-103` | `plan_trabajo` se deriva de los CA de la HU | **No** |

**Dos de cinco tienen algo que ver; tres son ruido.** El resultado honesto: la semántica pasa de *no encontrar nada* a *encontrar algo, mayormente ruido*. Sirve —cero resultados no ayuda a nadie— y **no reemplaza leer**. Queda como `D-03`, que no es un defecto del programa sino una medida que faltaba: nadie había cuantificado la precisión, y una fusión por rango recíproco siempre devuelve `k` resultados, tengan que ver o no.

---

### Detalle de CP-003 — Sin las dependencias, la búsqueda responde igual y lo dice

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr una búsqueda sin las dependencias | Responde, con la búsqueda por palabra | Responde |
| 2 | Comprobar que no falla ni pide instalar nada | No falla | No falla |
| 3 | Comprobar que **dice** que el significado no está disponible | Lo dice | Lo dice: `[búsqueda léxica (semántica no instalada)]` |
| 4 | Comprobar que da lo mismo que la léxica explícita | Los mismos | Los mismos |
| 5 | Comprobar que el entorno no se modificó | Sin cambios | Sin cambios |

**Los cinco pasos pasan… para el escenario que el caso escribió**, que es «sin las dependencias». **Pero el CA-02 no dice «sin las dependencias»: dice «sin el modelo».** Y ese escenario, que el plan no separó, **falla**:

> Con `numpy` y `model2vec` instalados y **el modelo ausente**, `cmd_search` termina con `LocalEntryNotFoundError` y **no devuelve nada**. Se cae la búsqueda entera, incluida la parte léxica, que no necesita ni modelo ni red.

La causa está a la vista en el programa: `semantica.disponible()` comprueba que las dos librerías **importen**, y nada más. Que el modelo se pueda cargar no lo comprueba nadie, y `cmd_search` llama a `semantica.indexar(con)` sin atrapar el error. Es el defecto `D-01`.

---

### Detalle de CP-004 — Nada sale de la máquina

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Calcular los vectores de la señal | Se calculan | Se calculan, en local |
| 2 | Comprobar que el programa **no abrió ninguna conexión** | Ninguna | **Abrió una.** `StaticModel.from_pretrained` consulta el repositorio del modelo al cargarlo. Se vio cortando el socket: la carga intenta salir a la red |
| 3 | Comprobar que el modelo se leyó del disco local | Del disco | Del disco: la lectura sale de la caché local del `hub` |
| 4 | Buscar por significado y repetir la comprobación | Ninguna conexión | La misma de arriba, y solo esa: **al buscar no hay más tráfico** |
| 5 | Comprobar que no depende de que la red esté caída | No depende | **No depende.** Con la red caída, indexar y buscar dan exactamente el mismo resultado que con red |

**Qué se puede afirmar y qué no.** El **contenido de las señales no sale de la máquina**: el texto se embebe en local y los vectores se guardan en la misma base. Eso se comprobó cortando la red y viendo que el resultado no cambia. Lo que **no** se puede afirmar es el paso 2 tal como está escrito: el programa **sí** abre una conexión, al repositorio del modelo, para ver si hay versión nueva. No manda datos de las señales, pero conectarse es conectarse. Es el defecto `D-02`.

> **Por qué no se descubrió antes.** La conexión es silenciosa y falla hacia la caché: si hay red, nadie la nota; si no hay, tampoco, porque el `hub` degrada solo. Solo aparece cortando el socket a propósito, que es lo que hizo este caso.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que ninguna prueba tocara la base real | Huella SHA-256 de `memoria/senales.db` en cada prueba | Igual antes y después |
| 2 | Cuánto mejora, con datos reales | Tres consultas sobre una **copia** de las 237 señales | 0 → 5 en las tres |
| 3 | Qué tan buenos son esos resultados | Leyendo los cinco títulos de una consulta | 2 sirven, 3 son ruido |
| 4 | Lo que cuesta la primera búsqueda y las siguientes | Cronometrando en frío y en caliente | **5,02 s la primera · 0,009 s las siguientes** |
| 5 | Que la suite entera siga verde | `python memoria/pruebas.py` | 59 pruebas · verde, con 5 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | Con las librerías instaladas y **el modelo ausente**, la búsqueda se cae entera —se lleva la léxica por delante—. `disponible()` mira que las librerías importen, no que el modelo cargue, y `cmd_search` no atrapa el error | Probado con fallo esperado en [`memoria/pruebas.py`](../../../../../memoria/pruebas.py). El arreglo toca `memoria.py` y `semantica.py`, que §2.1 del [plan aprobado](plan_trabajo.md) excluye. Se propone al usuario |
| D-02 | Media | Cargar el modelo **abre una conexión** al repositorio remoto. No viaja el contenido de las señales, pero el paso 2 de CP-004 pide «ninguna conexión» y hay una | Igual: dicho acá y propuesto. Se resuelve fijando el modo sin conexión al cargar |
| D-03 | Baja | **Nadie había medido la precisión.** De cinco resultados de una consulta real, dos sirven y tres son ruido: la fusión por rango recíproco siempre devuelve `k`, tengan que ver o no | Medido acá. No es defecto del programa: es un dato que faltaba para saber qué esperar |
| D-04 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales** de la HU. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-004-busqueda-por-significado.md#ca-01--encuentra-lo-que-se-escribió-con-otras-palabras) | CP-001, CP-002 | Encuentra con palabras distintas, y no pierde nada de lo que la léxica encontraba. Tres de tres consultas reales pasaron de 0 a 5 resultados | Sí |
| [CA-02](../HU-004-busqueda-por-significado.md#ca-02--sin-el-modelo-la-búsqueda-sigue-funcionando) | CP-003 | **Sin las dependencias** sí, y lo dice. **Sin el modelo, no**: la búsqueda se cae entera | **No** |
| RNF · que la memoria sirva aunque el modelo no esté | CP-003 | Lo mismo que el CA-02 | **No** |
| Transversal · Privacidad | CP-004 | El **contenido de las señales** no sale: se comprobó con la red caída. Pero el programa **sí abre una conexión** al cargar el modelo, y el caso pedía ninguna | **No** |
| Transversal · Rendimiento | Verificación 4 | La primera búsqueda cuesta **5,02 s**; las siguientes, **0,009 s**. Indexar no recalcula lo que no cambió | Sí |

**Los que no cumplen:** el **CA-02**, su RNF y el transversal de **privacidad**. Los tres se trasladan a una fase `B-EP-006-HU-004`.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| Consultas que mejoran con significado | Plan §12 | Anotado con su número | 3 de 3, de 0 a 5 resultados | Sí |
| Resultados que la híbrida pierde respecto de la léxica | Plan §12 | **0** | 0 | Sí |
| Conexiones abiertas al indexar y buscar | Plan §12 | **0** | **1**, al cargar el modelo | **No** |
| Señales de la base real modificadas | Plan §12 | 0 | 0 | Sí |

**Lo que no se cumplió:** la meta de cero conexiones. No se reescribe el plan: la meta estaba bien puesta y el programa no la cumple. Queda como `D-02`, con la decisión sin tomar de si se fija el modo sin conexión o se acepta la consulta al repositorio.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-01 quedó verificado y **medido con datos reales**: tres consultas escritas como las escribiría una persona pasaron de cero resultados a cinco, sin perder nada de lo que la búsqueda por palabra ya encontraba. Lo que no cumple es la promesa de que instalarlo sea opcional: el CA-02 dice «sin el modelo la búsqueda sigue funcionando» y, con las librerías puestas y el modelo ausente, se cae entera. Y el transversal de privacidad pedía cero conexiones: hay una.

**Qué falta para que cumpla:**

1. Que `disponible()` compruebe también que el modelo carga, o que `cmd_search` atrape el fallo y degrade a léxica (`D-01`). **Es lo más grave**: hoy un proyecto que instale las librerías y se quede sin el modelo pierde la memoria entera, no solo el significado.
2. Que el modelo se cargue en modo sin conexión (`D-02`).

Los dos tocan `memoria.py` y `semantica.py`, que el plan aprobado excluye. **Piden una fase `B-EP-006-HU-004`.**

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`memoria/pruebas.py`](../../../../../memoria/pruebas.py), clase `BusquedaPorSignificado`: 7 pruebas — 6 en verde y 1 como fallo esperado, que es `D-01` |
| EV-02 | Medición sobre datos reales | Las tablas de §2 (CP-001 y CP-002), sobre una copia de las 237 señales |
| EV-03 | Medición de tiempo | §3, verificación 4: 5,02 s en frío · 0,009 s en caliente |
| EV-04 | Corrida completa | `python memoria/pruebas.py` — 59 pruebas, verde, 5 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
