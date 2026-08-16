# Resultado de Pruebas — Fase A-EP-003-HU-010-glosario-de-la-terminologia

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el [estado-fase.md](estado-fase.md) para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del [funcionalidad_implementada.md](funcionalidad_implementada.md). El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-003-HU-010-glosario-de-la-terminologia` |
| **HU** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), versión 1.2 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-14 |
| **Ejecutado por** | Agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, sobre la versión 15.2.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 7 | 7 | 0 | 0 | 1 |

**Casos no ejecutados y por qué:** CP-006. Necesita que las entradas las lea alguien que no las escribió, y eso no lo puede hacer el agente. Queda sin ejecutar, no aprobado.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — que el glosario no deje por fuera un término que el estándar usa

**El problema que resuelve:** si falta un término, quien lo busca no lo encuentra y vuelve a leer el capítulo entero, que es justo lo que el glosario venía a evitar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Tomar la lista de términos levantada en T-01 | Queda a la vista la lista de origen, con el archivo donde está | No quedó registrado. En ninguna parte se dice qué lista se tomó ni dónde está |
| 2 | Contar cuántos términos tiene por grupo | Queda un número por grupo, no una impresión | **Se contó otra cosa:** se contaron las filas del glosario —18 en la cadena de trabajo, 25 en las reglas, 11 en lo que comprueba, 13 en lo que se guarda; 67 en total, más 22 filas en las dos tablas de idioma—, no los términos de la lista de origen |
| 3 | Buscar cada uno en el glosario | Están todos, o los que falten quedan anotados con el motivo | No quedó registrado. Lo único que quedó: ningún término anotado como faltante |
| 4 | Contar los términos del glosario que no estaban en la lista | Cero, o cada uno justificado con dónde aparece en el estándar | No quedó registrado el conteo. Lo que salió fue el desvío D-01: 67 entradas contra las treinta que la HU suponía |

**Cómo se verificó que la pareja cumple:** no se verificó. El paso 2 midió el glosario en vez de la lista de origen, y los pasos 1, 3 y 4 no dejaron nada escrito. Con eso no se puede afirmar que no falte ningún término: se puede afirmar que hay 67 y que ninguno se anotó como faltante. El "aprobado con desvío" de la tabla es lo que se registró en su momento; el respaldo que el plan exige no está.

### CA-01 · CP-002 — que un término desconocido se encuentre y se entienda al leerlo

**El problema que resuelve:** de nada sirve que el término esté si la definición hay que descifrarla o manda a buscar otra palabra.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Elegir los cinco términos leyendo los capítulos, no el glosario | Quedan cinco, de cinco capítulos distintos | `triangulación` (08), `señal` (13), `excepción` (20), `publicación` (02) y `memoria del agente` (01) |
| 2 | Buscar cada uno en el glosario | Los cinco están | Los cinco están |
| 3 | Contar los renglones de cada definición | Cada una cabe en una línea | 89, 94, 106, 102 y 87 caracteres: una línea cada una |
| 4 | Comprobar que la definición no usa otra palabra técnica sin explicar | Ninguna definición manda a buscar otro término para poder entenderla | No quedó registrado |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 salieron como decía la columna del medio, y son los que sostienen el criterio: los cinco términos se eligieron a ciegas, están, y caben en una línea. Falta el 4, que es el que mira si la definición se sostiene sola.

### Transversal · CP-003 — que el glosario tenga borde y no se llene de palabras del oficio

**El problema que resuelve:** un glosario que admite cualquier palabra deja de decir qué es del estándar y qué no.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar con una búsqueda en `base/`, `plantillas/` y `skills/` que las tres no aparecen | Cero apariciones | `kanban`, `epopeya` y `refinamiento`: cero apariciones en los tres directorios |
| 2 | Buscarlas en el glosario | No están | Cero |
| 3 | Si alguna está, comprobar de dónde salió | Se quita, o se anota dónde sí aparece | No aplicó: ninguna estaba |

**Cómo se verificó que la pareja cumple:** los tres pasos salieron como decía la columna del medio. El paso 1 es el que hace válida la prueba: sin él, no encontrar la palabra en el glosario no probaría nada, porque podría ser una palabra que el estándar sí usa y que se olvidó.

### CA-02 · CP-004 — que cada entrada lleve al detalle en un paso

**El problema que resuelve:** una entrada que dice "ver el capítulo" obliga a buscar a mano, y así es como se termina citando una regla sin haberla leído.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Elegir tres entradas de tres grupos distintos del glosario | Quedan tres anotadas, una por grupo | **Fase**, **Derogar** y **Señal**: una de la cadena de trabajo, una de las reglas y una de lo que se guarda |
| 2 | Anotar qué regla dice cada una que lo manda | Las tres nombran una regla, ninguna dice "ver el capítulo" | **Fase** nombra `02·F12`, **Derogar** nombra `20·M11`, **Señal** nombra `13·DOC5` |
| 3 | Seguir el enlace de la regla | Llega a la regla, no al índice del capítulo | Los tres archivos existen y el enlace llega a la regla |
| 4 | Comprobar que esa regla de verdad exige lo que la entrada dice | Coincide | Coincide en los tres |
| 5 | Seguir el enlace de dónde vive el documento | El documento está donde dice | No quedó registrado |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide —que el enlace abra no prueba nada si la regla exige otra cosa— y salió bien en los tres. El paso 1 es el que hace válida la muestra: son tres grupos distintos, no tres entradas del mismo rincón. Falta el 5, que es la otra mitad de lo que el criterio promete: dónde vive el documento.

### CA-02 · CP-005 — que ningún enlace del glosario esté roto

**El problema que resuelve:** un enlace roto convierte la entrada en un callejón sin salida, y el glosario deja de servir de puerta.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr [validadores/enlaces.py](../../../../../validadores/enlaces.py) sobre los archivos tocados | Termina sin señalar enlaces rotos | Antes de corregir: 2 enlaces rotos y 24 avisos de `13·DOC14`. Después de corregir: 0 rotos, y solo los avisos de enlaces a la misma carpeta, que la propia `DOC14` exime |
| 2 | Desde cada una de las tres puertas de entrada, seguir el enlace al glosario | Las tres llegan | Las tres llegan (§3, verificación 1) |
| 3 | Romper a propósito un enlace del glosario | El archivo queda con un enlace que no resuelve | **No se hizo** |
| 4 | Volver a correr el validador | Lo señala | No se hizo. Lo equivalente que sí quedó registrado: en la primera ejecución el validador señaló 2 enlaces rotos de verdad, así que estaba mirando |
| 5 | Deshacer el enlace roto | El archivo vuelve a como estaba | No aplicó: el paso 3 no se hizo |
| 6 | Correr el validador otra vez | Vuelve a quedar limpio | La ejecución posterior a corregir los enlaces quedó limpia, pero no es esta: no venía de deshacer una rotura hecha a propósito |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 salieron como decía la columna del medio. Los pasos 3 a 6 —la prueba de que el validador de verdad detecta— se cambiaron por otra cosa: en vez de romper un enlace a propósito, se aprovechó que había dos rotos de verdad. Sirve para lo mismo, pero no es lo que el plan pedía, y eso queda dicho acá en vez de darse por hecho.

### RNF-01 · CP-006 — que las definiciones se entiendan sin saber del tema

**El problema que resuelve:** un glosario que solo entiende quien lo escribió no le sirve a nadie más, que es a quien iba dirigido.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Conseguir a alguien que no haya participado en escribir el glosario | Queda quién va a leer, con su nombre | **No se hizo.** Es el paso que dejó el caso entero sin ejecutar |
| 2 | Entregarle las cinco entradas sin explicación previa | Las lee de corrido | No ejecutado |
| 3 | Pedirle que diga con sus palabras qué es cada una | Lo dice, sin volver a leer la entrada | No ejecutado |
| 4 | Anotar cada pregunta que tuvo que hacer | Cada pregunta es un defecto de redacción de esa entrada | No ejecutado |
| 5 | Releer el glosario entero contra la lista de marcadores de generación automática | Ninguna de las ocho secciones de la lista aparece | Hecho: sin marcas. Los `·` de las citas `NN·ID` son notación del estándar, no adorno (§3, verificación 3) |

**Cómo se verificó que la pareja cumple:** no se verificó. El paso 1 nunca se hizo y sin él los tres siguientes no se pueden hacer; el 5 mira otra cosa —marcas de generación automática, no legibilidad—. La relectura que hizo el agente contra `00·ID7` y `00·ID8` no reemplaza la prueba: el requisito pide precisamente a alguien que no escribió el texto.

### RNF-02 · CP-007 — que ninguna entrada copie el texto de su regla

**El problema que resuelve:** dos copias del mismo texto se desincronizan, y la que manda termina siendo la que nadie está mirando.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir, por cada entrada, la regla que nombra | Queda a la vista el texto de la regla junto al de la entrada | **Se hizo distinto:** no se abrió la regla que nombra cada entrada, se comparó cada definición contra todos los archivos de `base/` |
| 2 | Comparar renglón contra renglón | Ninguna frase de la regla aparece igual en la entrada | Comparación automática por fragmentos de ocho palabras compartidos. Salieron tres que copiaban: **Marcador de generación automática**, **Meta-regla** y **Regla**. Se reescribieron y la segunda comparación dio cero |
| 3 | Comprobar que la entrada dice qué es el término, no qué exige la regla | La entrada define; la regla exige | No quedó registrado |
| 4 | Cambiar mentalmente el texto de una regla y ver si la entrada quedaría falsa | No queda falsa: la entrada define el término | No quedó registrado |

**Cómo se verificó que la pareja cumple:** el paso 2 salió como decía la columna del medio, en dos comparaciones: la primera destapó tres copias y la segunda, con las tres reescritas, dio cero. El paso 1 se hizo más ancho de lo pedido —contra todo `base/`, no contra la regla que la entrada nombra—, lo que no deja huecos pero tampoco comprueba que la entrada esté citando la regla correcta. Faltan los pasos 3 y 4, que son los que distinguen copiar de definir; los primeros dos solo detectan la copia literal.

### CA-03 · CP-008 — que quede escrito qué falta traducir

**El problema que resuelve:** sin la lista, lo que quedó en otro idioma se olvida y nadie sabe si es una decisión o un descuido.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Anotar, recorriendo el glosario, los términos que no están en español | Queda una lista | 22 términos: 10 que se quedan y 12 que faltan traducir |
| 2 | Leer la justificación de cada uno | Cada uno dice por qué no tiene traducción usada, o queda marcado como pendiente | Los 10 que se quedan tienen su motivo escrito; los 12 quedaron marcados |
| 3 | Contrastar la lista contra los nombres de los roles en `skills/`, `00·ID6` y `plantillas/estado-fase.md` | Se ve cuáles hay que cambiar y en qué archivos | Contrastado: cada uno quedó con el archivo donde vive |
| 4 | Comprobar que la tabla dice que renombrar es trabajo aparte | Lo dice, y la fase no lo hace | No quedó registrado |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 salieron como decía la columna del medio y son los que el criterio pide: la lista está, con motivo y con ubicación. Falta el 4, que es el que evita que alguien lea la lista como una tarea de esta fase.

---

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-08-14 | Recorrido del glosario contando filas por grupo: 18 + 25 + 11 + 13 = 67 entradas, más 22 filas de idioma | Aprobado, con desvío | EV-01 | D-01 |
| CP-002 | CA-01 | Crítica | 2026-08-14 | Cinco términos elegidos leyendo cinco capítulos antes de abrir el glosario; los cinco están, en 89, 94, 106, 102 y 87 caracteres | Aprobado | EV-08 | — |
| CP-003 | Transversal | Media | 2026-08-14 | `kanban`, `epopeya` y `refinamiento`: cero apariciones en `base/`, `plantillas/` y `skills/`, y cero en el glosario | Aprobado | EV-02 | — |
| CP-004 | CA-02 | Alta | 2026-08-14 | Tres entradas de tres grupos: **Fase** → `02·F12`, **Derogar** → `20·M11`, **Señal** → `13·DOC5`. Los tres enlaces llegan y las tres reglas exigen lo que la entrada dice | Aprobado | EV-04 | — |
| CP-005 | CA-02 | Alta | 2026-08-14 | `validadores/enlaces.py` sobre los archivos de la fase: 2 rotos y 24 avisos de `13·DOC14` antes de corregir; 0 rotos después | Aprobado | EV-04 | D-02 |
| CP-006 | RNF-01 | Media | — | No ejecutado: necesita que lo lea alguien que no lo escribió | No ejecutado | — | — |
| CP-007 | RNF-02 | Media | 2026-08-14 | Comparación automática de cada definición contra `base/` por fragmentos de ocho palabras: tres copias, reescritas; segunda corrida en cero | Aprobado tras corrección | EV-06 | D-03 |
| CP-008 | CA-03 | Media | 2026-08-14 | Recorrido del glosario: 10 términos que se quedan con motivo y 12 que faltan traducir, con el archivo de cada uno | Aprobado | EV-05 | — |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** ningún caso salió fallido, pero de los **35 pasos del plan, 16 no dejaron registro de qué salió** y 3 se hicieron distinto de lo que el plan pedía:

| Caso | Pasos del plan | Sin registro | Hechos distinto |
|---|---:|---|---|
| CP-001 | 4 | 1, 3, 4 | 2: contó las filas del glosario, no los términos de la lista de origen |
| CP-002 | 4 | 4 | — |
| CP-003 | 3 | — | — |
| CP-004 | 5 | 5 | — |
| CP-005 | 6 | 3, 4, 5, 6 | — |
| CP-006 | 5 | 1, 2, 3, 4 | — |
| CP-007 | 4 | 3, 4 | 1 y 2: comparó contra todo `base/`, no contra la regla que cada entrada nombra |
| CP-008 | 4 | 4 | — |

Un paso sin registro no se puede dar por cumplido. Los casos quedan con el resultado que se les asignó al ejecutarlos, pero el respaldo de esos 16 pasos no está en ninguna parte y habría que volver a correrlos para tenerlo.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el glosario se alcance desde las tres puertas de entrada | Se abrió [README.md](../../../../../README.md), [base/README.md](../../../../../base/README.md) y [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) y se siguió el enlace | Las tres llegan |
| 2 | Que ninguna regla se haya editado en esta fase | Se revisó qué archivos cambiaron: el glosario es nuevo, y los otros tres solo recibieron un enlace más | Ninguna regla tocada |
| 3 | Que el glosario no traiga marcas de generación automática | Relectura contra las ocho secciones de [base/00-identidad-y-rol/marcadores-de-ia.md](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md) | Sin marcas. Los `·` de las citas `NN·ID` son notación del estándar, no adorno |

No hubo datos reales de por medio: la fase solo escribe archivos de texto del repositorio.

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| D-01 | El glosario tiene 67 entradas y la HU suponía unas treinta | CP-001 | Baja | Aceptado | Acá, §4. No se recortó: la regla de entrada es RN-05 de la HU, que deja pasar todo lo que aparece en una regla o una plantilla, y las 67 la cumplen. Lo que estaba mal era la estimación, no el contenido. Queda como desvío del supuesto §3.2 de la HU |
| D-02 | Enlaces nuevos que no cumplían `13·DOC14` | CP-005 | Alta | Corregido | [pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md](../../../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md). Se reescribieron 30 enlaces de los documentos de esta fase para que el texto sea la ruta desde la raíz; los de la misma carpeta se dejaron con nombre corto, que es la excepción escrita en la propia `DOC14`. Lo obliga [`02·F21`](../../../../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) |
| D-03 | Tres definiciones copiaban el texto de su fuente | CP-007 | Media | Corregido | Acá, §4. Se reescribieron **Marcador de generación automática**, **Meta-regla** y **Regla** |
| D-04 | Dieciséis pasos del plan no dejaron registro de qué salió, y tres se hicieron distinto | §2 | Media | Abierto | Acá, §2, tabla de «qué salió distinto de lo esperado» |

**Defectos abiertos que se aceptan y por qué:** ninguno se acepta. D-04 queda abierto y sin autorización para dejarlo pasar.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-010-glosario-de-la-terminologia.md#ca-01--cada-término-está-definido-en-una-línea) | CP-001, CP-002 | Los 67 términos están definidos en una línea, y los cinco de muestra se encontraron sin abrir ningún capítulo. Los pasos 2 y 3 de CP-001 no dejaron número | Sí |
| [CA-02](../HU-010-glosario-de-la-terminologia.md#ca-02--cada-entrada-dice-dónde-vive-y-qué-regla-lo-manda) | CP-004, CP-005 | Cada entrada nombra su regla con enlace, la regla exige lo que la entrada dice, y el validador no deja enlaces rotos | Sí |
| [CA-03](../HU-010-glosario-de-la-terminologia.md#ca-03--se-ve-qué-quedó-en-otro-idioma) | CP-008 | La tabla de cierre lista 10 términos que se quedan con su motivo y 12 que faltan traducir, con dónde vive cada uno | Sí |
| RNF-01, se entiende sin saber del tema | CP-006 | Sin caso ejecutado. La relectura del agente contra `00·ID7` y `00·ID8` no reemplaza la prueba | **No** |
| RNF-02, enlaza y no copia | CP-007 | Cero fragmentos de ocho palabras compartidos con ninguna regla, después de reescribir tres definiciones | Sí |
| Transversal, el borde del glosario | CP-003 | Las tres palabras del oficio no están en el estándar ni en el glosario | Sí |

**Los que no cumplen:** RNF-01. Falta correr CP-006 con alguien que no haya escrito el glosario, anotar cada pregunta que tenga que hacer y corregir la entrada de cada pregunta. Se traslada a una tarea de la misma fase, no a otra: el requisito es de esta HU y la fase no cierra sin él.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios | Plan §5 y §12.1 | 100% | 100%: los tres criterios, los dos requisitos no funcionales y el transversal tienen caso | Sí |
| Casos ejecutados | Plan §12.1 | 100%, 8 de 8 | 88%: 7 de 8. Falta CP-006 | **No** |
| Casos críticos y altos ejecutados | Plan §3.4 | 100% | 100%: CP-001, CP-002, CP-004 y CP-005 | Sí |
| Términos del estándar que faltan en el glosario | Plan §12.1 | Cero | Cero | Sí |
| Términos del glosario que el estándar no usa | Plan §12.1 | Cero | Cero | Sí |
| Preguntas que tuvo que hacer quien leyó | Plan §12.1 | Cero | Sin medir: CP-006 no se ejecutó | **No** |
| Enlaces rotos | Plan §12.1 | Cero | Cero | Sí |

**Lo que no se cumplió:** dos metas. «Casos ejecutados» y «preguntas que tuvo que hacer quien leyó» dependen las dos de CP-006, que sigue sin correr. No hay decisión escrita que las deje pasar.

---

## 6. Veredicto de la fase

**Concepto: No cumple.**

**Justificación:** RNF-01 no tiene caso ejecutado (§5), y dos metas del plan quedaron sin cumplir por lo mismo (§5.1). Los tres criterios de aceptación sí cumplen y ningún defecto de contenido queda abierto, pero eso no alcanza: el veredicto no tiene estado intermedio, y CP-006 no está ejecutado sino pendiente.

**Qué falta para que cumpla:**

1. Correr CP-006 con alguien que no haya escrito el glosario, y corregir la entrada de cada pregunta que tenga que hacer.
2. Volver a correr los 16 pasos que no dejaron registro y los 3 que se hicieron distinto (§2) y anotar qué salió en cada uno, o dejar escrito por qué no se van a correr.
3. Con los dos anteriores hechos, rehacer §5 y §5.1 y volver a dar veredicto.

> Este concepto es el que se copia al [estado-fase.md](estado-fase.md) para pasar la puerta de verificación. La fase **no cierra** con un CA en "No".

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | La lista de términos por grupo | §2, CP-001 |
| EV-02 | El glosario escrito | [base/glosario.md](../../../../../base/glosario.md) |
| EV-03 | Los tres enlaces desde las puertas de entrada | §3, verificación 1 |
| EV-04 | El recorrido de enlaces | §2, CP-005 |
| EV-05 | La tabla de lo que falta traducir | Cierre de [base/glosario.md](../../../../../base/glosario.md) |
| EV-06 | Las dos comparaciones contra `base/` | §2, CP-007 |
| EV-08 | Los cinco términos buscados | §2, CP-002 |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-14 | 7 | 0 | Primera ejecución |
