# HU-023 · Cada tarea sabe qué reglas le aplican

> Nace del [pendiente 100](../../../../pendientes/100-cada-tarea-sabe-que-reglas-le-aplican.md), aprobado por el usuario el 2026-09-28.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-023 |
| **Épica / Feature** | [EP-005 · Automatismos que no dependen de que alguien se acuerde](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas, todos los capítulos, y `validadores/` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Terminada el 2026-09-29, con el ciclo 4 de la fase `C` |

## 2. Narrativa

- **Como** agente que va a hacer una tarea
- **Quiero** un mapa que lleve de la tarea a las reglas que le aplican, con su enlace
- **Para** leer solo esas antes de actuar, sin cargar todas

## 3. Contexto y descripción

No hay un mapa que lleve de una tarea a las reglas que le aplican. El 2026-09-28 el usuario decidió que el agente no cargue las reglas al arrancar, sino que antes de cada tarea identifique y lea las que le corresponden. Hoy los índices de `base/` están ordenados por capítulo, y para encontrar una regla hay que saber de antemano en qué capítulo está.

El antecedente, [validadores/reglas-antes-de-la-accion.md](../../../../validadores/reglas-antes-de-la-accion.md), clasifica las reglas por cuándo se pueden comprobar, no por a qué tarea aplican, y cuenta 248 reglas cuando `metareglas.py` cuenta hoy 261.

Va en esta épica y no por la historia dueña de cada capítulo porque toca las reglas de todos los capítulos a la vez, con una línea que no cambia qué exige ninguna. Es el mismo caso de [`EP-005·HU-012`](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md), que agregó a cada regla del núcleo quién la hace cumplir.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay una lista cerrada de tareas, escrita en `base/`. Una tarea que no está en la lista no se usa |
| RN-02 | Cada regla vigente declara a qué tareas aplica, en una línea `**Aplica a:**` después de su ejemplo. La línea no es parte del cuerpo: no cuenta para el largo ni anula el checklist, igual que «Nadie la hace cumplir» |
| RN-03 | El mapa `base/mapa-de-tareas.md` lo escribe un programa leyendo esas líneas, nunca una persona. Por cada tarea lista sus reglas, con el enlace a cada una |
| RN-04 | Un validador falla si una regla vigente no declara sus tareas, si nombra una tarea fuera de la lista o si el mapa no coincide con lo que declaran las reglas. Corre solo antes de publicar, sin que nadie tenga que llamarlo |
| RN-05 | El validador del mapa del amarre da por clasificado un programa solo si lo nombra una fila de tabla o una línea que lista nombres, no una frase cualquiera. Todo programa de `validadores/` y del adaptador queda clasificado. Viene de H-8 de la sesión del 2026-09-28, que salió en la fase `A` |
| RN-06 | Con cada mensaje del usuario, el recuperador reconoce las tareas que el mensaje pide y le entrega al agente las reglas que el mapa pone bajo esas tareas. `recibir-pedido` y `responder` van siempre, porque todo mensaje es un pedido y lleva respuesta. Ningún capítulo queda fuera por suponer que llegó al arrancar. Viene de H-9 de la sesión del 2026-09-28 |
| RN-07 | **Nada se elige adivinando.** Con cada mensaje, las tareas salen de la palabra clave de [`01·C28`](../../../../base/01-conducta.md#c28--sin-la-palabra-que-diga-qué-se-espera-el-agente-no-actúa), que es una lista cerrada, y no de las demás palabras del mensaje. Antes de cada acción del agente, las tareas salen de la acción misma: el comando que va a correr, el archivo que va a escribir o el servicio que va a consultar. Las dos correspondencias están escritas en `base/tareas.md`. **Reemplaza la elección por palabras del mensaje de RN-06**, que tomó «reglas» como pedido de cambiar el estándar |
| RN-08 | Las reglas de cada tarea se juntan, con su texto completo, en un archivo por tarea que escribe un programa, como el mapa, en `base/reglas-por-tarea/`. Los validadores que recorren `base/` no cuentan esos archivos como reglas repetidas. El agente lee ese archivo con la herramienta de lectura, así que le llega entero: el texto de un enganche se corta en 10.000 caracteres, y las reglas de una tarea suman de 9.946 a 217.871 |
| RN-09 | Si el mensaje del usuario no abre con una palabra de `01·C28`, el agente no actúa: la recuerda en una línea y espera. Las reglas salen de la palabra con que el usuario responda, y le llegan al agente por dentro, sin que muestre que las lee. Viene de lo decidido por el usuario el 2026-09-29: *«cada vez que el usuario escriba algo que no esté de acuerdo con la C28, me la recuerde y, a partir de la respuesta que yo le dé, determine cuáles son las reglas que debe utilizar»*. **Reemplaza la versión anterior de esta RN**, que obligaba a leer por comando las reglas antes de cada acción y de cada respuesta: llenaba la conversación y no hacía cumplir nada |
| RN-10 | El enganche detiene toda escritura de archivo fuera de la carpeta del proyecto, y dice dónde va el guion de apoyo ([`04·S9`](../../../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas), [`04·S18`](../../../../base/04-seguridad.md#s18--el-guion-de-apoyo-se-escribe-dentro-del-repositorio-y-se-queda)). Viene del 2026-09-28: el agente escribió guiones en la carpeta temporal de la herramienta y el usuario pidió corregirlo |

### 3.2 Supuestos

- `metareglas.py` cuenta 261 reglas: 252 vigentes y 9 derogadas. Se anotan las vigentes; las derogadas no.

### 3.3 Fuera de alcance

- La instrucción que el agente recibe al arrancar la sesión.
- Cambiar qué exige cualquier regla.

## 4. Criterios de aceptación

### CA-01 · La lista de tareas existe y es cerrada

```gherkin
Dado que el mapa necesita agrupar las reglas por tarea
Cuando se abre la lista de tareas en base/
Entonces cada tarea tiene su nombre y una frase que dice cuándo aplica
Y no hay dos tareas que cubran lo mismo
```

**Cómo validarlo:**

1. Abrir `base/tareas.md`. Resultado esperado: una tabla con cada tarea, su nombre corto y cuándo aplica.
2. Leer las filas de dos en dos. Resultado esperado: ninguna acción del agente cae en dos tareas a la vez.
- **Aprobado cuando:** la lista existe y ninguna tarea se superpone con otra.

### CA-02 · Una regla declara sus tareas sin cambiar lo que exige

```gherkin
Dado una regla vigente con su checklist en CUMPLE
Cuando se le agrega su línea **Aplica a:**
Entonces el largo de su cuerpo no cambia
Y su checklist no queda anulado
```

**Cómo validarlo:**

1. Tomar una regla con su checklist en CUMPLE y medir su cuerpo con `Regla.largo()` de `validadores/metareglas.py`.
2. Agregarle la línea `**Aplica a:**` con una tarea de la lista.
3. Medir de nuevo. Resultado esperado: el mismo número.
4. Correr `python validadores/validar.py metareglas`. Resultado esperado: no dice que el checklist de esa regla quedó anulado.
- **Aprobado cuando:** el largo no cambia y el checklist sigue vigente.

### CA-03 · El mapa sale de las reglas

```gherkin
Dado que las reglas declaran sus tareas
Cuando se corre el programa que arma el mapa
Entonces base/mapa-de-tareas.md lista cada tarea con sus reglas, enlazadas
Y si una regla cambia sus tareas, el mapa cambia al volver a correrlo
```

**Cómo validarlo:**

1. Correr el programa. Resultado esperado: escribe `base/mapa-de-tareas.md`.
2. Abrir el mapa y buscar una regla que declare dos tareas. Resultado esperado: aparece bajo las dos, con su enlace.
3. Cambiarle a esa regla una tarea por otra y volver a correr el programa. Resultado esperado: el mapa la muestra bajo la tarea nueva y no bajo la vieja.
- **Aprobado cuando:** los tres pasos dan lo esperado.

### CA-04 · El validador detecta lo que falta o no cuadra

```gherkin
Dado el validador del mapa
Cuando una regla no declara tareas, o nombra una fuera de la lista, o el mapa quedó viejo
Entonces falla y dice cuál regla y por qué
Y con el repositorio al día, pasa
```

**Cómo validarlo:**

1. En una copia de prueba, quitarle a una regla su línea `**Aplica a:**` y correr el validador. Resultado esperado: falla nombrando la regla.
2. Ponerle una tarea que no está en la lista. Resultado esperado: falla nombrando la tarea.
3. Cambiar una tarea sin volver a generar el mapa. Resultado esperado: falla diciendo que el mapa quedó viejo.
4. Correrlo sobre el repositorio como queda. Resultado esperado: pasa.
- **Aprobado cuando:** los cuatro pasos dan lo esperado.

### CA-05 · Toda regla vigente declara sus tareas

```gherkin
Dado que el formato y el mapa existen
Cuando se recorren las reglas vigentes de base/
Entonces todas tienen su línea **Aplica a:**
```

**Cómo validarlo:**

1. Correr el validador del mapa sobre el repositorio. Resultado esperado: 0 reglas sin tareas.
2. Contar las reglas del mapa y las que cuenta `metareglas.py`. Resultado esperado: el mismo número.
- **Aprobado cuando:** ninguna regla vigente queda fuera del mapa.

### CA-06 · El mapa del amarre no da por clasificado lo que solo se nombra

```gherkin
Dado un programa de validadores/ que el mapa del amarre solo nombra en una frase
Cuando se corre validar.py amarre
Entonces lo reporta como sin clasificar
Y con todos los programas clasificados en su tabla o su lista, pasa
```

**Cómo validarlo:**

1. En una copia de prueba, nombrar un programa sin clasificar dentro de una frase del mapa y correr el validador. Resultado esperado: lo reporta como sin clasificar.
2. Ponerlo en una fila de tabla con su columna. Resultado esperado: deja de reportarlo.
3. Correr `python validadores/validar.py amarre` sobre el repositorio. Resultado esperado: 0 fallas, con todos los programas de `validadores/` y del adaptador clasificados.
4. Correr `python -m unittest test_el_mapa_del_amarre_no_envejece` desde `validadores/tests`. Resultado esperado: OK.
- **Aprobado cuando:** los cuatro pasos dan lo esperado.

### CA-07 · El recuperador trae las reglas de la tarea que pide el mensaje

```gherkin
Dado que el usuario escribe un mensaje
Cuando el enganche de cada turno llama al recuperador
Entonces el agente recibe las reglas que el mapa pone bajo las tareas del mensaje
Y siempre las de recibir-pedido y responder
```

**Cómo validarlo:**

1. Pasarle al recuperador «suba a git». Resultado esperado: trae `00·N2`.
2. Pasarle «aplique las reglas de la caja de reglas de redacción al readme». Resultado esperado: trae `00·ID8`, `00·ID9`, `00·ID11` y `00·ID12`.
3. Pasarle «cree el pendiente del H2». Resultado esperado: trae `02·F23` y `01·C28`.
4. Abrir `.claude/settings.json` del estándar. Resultado esperado: el enganche `hook_reglas.py` está en `UserPromptSubmit`.
- **Aprobado cuando:** los cuatro pasos dan lo esperado.

### CA-08 · La palabra clave dice las tareas del mensaje

```gherkin
Dado que el usuario escribe un mensaje
Cuando el recuperador elige las reglas
Entonces las tareas salen solo de la palabra clave del mensaje
Y un mensaje sin palabra clave trae solo las reglas que rigen todo mensaje
```

**Cómo validarlo:**

1. Pasarle «Suba». Resultado esperado: las tareas son `tocar-git`, `recibir-pedido` y `responder`.
2. Pasarle «es sencillo, debe entender las reglas». Resultado esperado: solo `recibir-pedido` y `responder`; ninguna de `cambiar-estandar`.
3. Pasarle «Escriba el plan del estándar». Resultado esperado: `escribir-documento`, sin `cambiar-estandar` ni `trabajar-cadena`.

Se aprueba cuando ninguna tarea sale de una palabra que no sea la clave.

### CA-09 · Sin la palabra de C28 el agente no actúa, y nada se escribe fuera del proyecto

```gherkin
Dado que el usuario escribe un mensaje que no abre con una palabra de 01·C28
Cuando el enganche de cada mensaje llama al recuperador
Entonces el agente recibe el aviso de que falta la palabra, con la lista, y no actúa
Y si el mensaje cita una regla, recibe también su texto
Y si una escritura queda fuera del proyecto, se detiene
```

**Cómo validarlo:**

1. Pasarle al recuperador «pero por qué no funciona». Resultado esperado: el aviso de `01·C28` con la lista completa de palabras, y ninguna instrucción de leer archivos.
2. Pasarle «Suba». Resultado esperado: las reglas de `tocar-git`, con `00·N2`, sin el aviso.
3. Pasarle «qué dice 02·F24?». Resultado esperado: el aviso y el texto de `02·F24`.
4. Simular la escritura de un archivo en la carpeta temporal del sistema. Resultado esperado: se detiene y dice que el guion va en `historico-chat/scripts/AAAA-MM-DD/`.
5. Simular un comando. Resultado esperado: pasa sin detenerse.

Se aprueba cuando un mensaje sin la palabra no produce acción y ninguna escritura sale del proyecto.

### CA-10 · Los archivos de reglas por tarea no envejecen

```gherkin
Dado que una regla cambia o cambia la línea de sus tareas
Cuando corre el validador de tareas
Entonces falla si algún archivo de reglas por tarea no coincide con lo que dicen las reglas
```

**Cómo validarlo:**

1. Escribir los archivos y correr `validar.py tareas`. Resultado esperado: sin fallas.
2. En una copia, cambiar una regla sin volver a escribirlos. Resultado esperado: falla nombrando el archivo viejo.

Se aprueba cuando el archivo de una tarea no puede quedar distinto de sus reglas.

### Criterios de aceptación transversales

- [ ] No regresión: `metareglas`, `estandar` y la suite de pruebas quedan sin fallas nuevas (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El cambio se registra en `CHANGELOG.md` y sube `VERSION` |
| RNF-02 | **Mantenibilidad** | El programa y el validador tienen sus pruebas en `validadores/tests/` |

## 6. Diseño y referencias

- Documento funcional: el [pendiente 100](../../../../pendientes/100-cada-tarea-sabe-que-reglas-le-aplican.md).
- Precedente de una línea fuera del cuerpo de la regla: `_FUERA_DEL_CUERPO` en `validadores/metareglas.py`.
- Antecedente de clasificación: [validadores/reglas-antes-de-la-accion.md](../../../../validadores/reglas-antes-de-la-accion.md).

## 7. Tareas técnicas derivadas

- [ ] Escribir la lista cerrada de tareas
- [ ] Hacer que `metareglas.py` deje la línea `**Aplica a:**` fuera del cuerpo
- [ ] Escribir el programa que arma el mapa, con sus pruebas
- [ ] Escribir el validador del mapa, con sus pruebas
- [ ] Anotar las 252 reglas vigentes
- [ ] Corregir el validador del amarre y clasificar los programas que le faltan
- [ ] Versionar el cambio

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa`](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/) | CA-01, CA-02, CA-03 | | [plan_trabajo](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/plan_pruebas.md) | [resultado](A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/resultado_pruebas.md) | Cerrada 2026-09-28 · Cumple |
| [`B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas`](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/) | CA-04, CA-05, CA-06, CA-07 | CA-01, CA-02 | [plan_trabajo](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/plan_trabajo.md) | [plan_pruebas](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/plan_pruebas.md) | [resultado](B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas/resultado_pruebas.md) | Cerrada 2026-09-28 · Cumple |
| [`C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar`](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/) | CA-08, CA-09, CA-10 | CA-07 | [plan_trabajo](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/plan_trabajo.md) | [plan_pruebas](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/plan_pruebas.md) | [resultado](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/resultado_pruebas.md) | Cerrada el 2026-09-29: Cumple, ciclo 4 |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la lista de tareas quede tan fina que cada regla caiga en muchas, o tan gruesa que no sirva para elegir | La lista se prueba en la fase `A` contra las reglas del núcleo antes de anotar el resto |
| Riesgo | Que anotar 252 reglas a mano meta errores | El validador de la fase `B` los detecta, y cada tarea nombrada tiene que estar en la lista |

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Lista, mapa, programa y validador en rama principal
- [ ] Pruebas del programa y del validador pasando
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Aceptada por el usuario

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No espera a otra historia |
| **N**egociable | ☑ | La lista de tareas se decide en la fase `A` |
| **V**aliosa | ☑ | Sin el mapa, el agente no sabe qué regla leer antes de una tarea |
| **E**stimable | ☑ | Una lista, dos programas y una línea por regla |
| **S**mall (pequeña) | ☑ | Partida en dos fases: el formato y el mapa, y después las 242 que faltan, con el validador |
| **T**esteable | ☑ | El programa y el validador se prueban con casos; la lista se lee |

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-28 | El agente | Creación de la HU, a partir del pendiente 100 |
| 2026-09-28 | El agente | Fase `A` cerrada con veredicto Cumple: la lista de tareas, la línea `**Aplica a:**` en el núcleo y el programa del mapa, versión 39.2.0 |
| 2026-09-28 | El agente | Suma RN-05 y CA-06 por H-8, que salió en la fase `A`: el usuario decidió que se resuelve en esta HU. Se abre la fase `B`, con CA-04 a CA-06 |
| 2026-09-28 | El agente | Suma RN-06 y CA-07 por H-9: el recuperador de reglas ya existía y fallaba, y el usuario eligió que la fase `B` lo haga trabajar con el mapa. El plan de la fase se reescribe y vuelve a aprobación |
| 2026-09-28 | El agente | Fase `B` cerrada con veredicto Cumple: las 252 reglas con sus tareas, el validador, la corrección del amarre y el recuperador por tareas conectado en el estándar, versión 39.3.0 |
| 2026-09-28 | El agente | Suma RN-07 a RN-09 y CA-08 a CA-10, y abre la fase `C`. El agente corrió las 568 pruebas de `pruebas.py` contra `02·F5`, que le había llegado solo por su nombre; y la elección por palabras tomó «reglas» como pedido de cambiar el estándar. El usuario decidió que las reglas se elijan sin adivinar y que el agente las tenga completas antes de actuar. Se reabre H-1 de la sesión, que es el mismo problema |
| 2026-09-28 | El agente | Se reabre la fase `C`. El agente la cerró con tres cosas que el usuario no autorizó: los archivos por tarea en la raíz y no en `base/` como decía el plan, la relectura solo al resumirse y no en cada interacción, y H-1 cerrado antes de tiempo. El usuario pidió corregirlo. Suma RN-10 porque el agente escribió guiones fuera del repositorio, y CA-09 gana los pasos 4 a 7 |
| 2026-09-28 | El agente | Ciclo 3 de la fase `C`: la herramienta de lectura no volvía a mandar un archivo que no cambió, y el enganche contaba ese aviso como lectura. RN-09 dice ahora que ese aviso no cuenta y que las reglas se leen con un comando; CA-09 gana los pasos 8 y 9 |
| 2026-09-29 | El agente | El usuario descartó la lectura obligatoria: llenaba la conversación y no hacía cumplir nada. Pidió que, sin la palabra de `01·C28`, el agente la recuerde y espere, y que las reglas salgan de la respuesta. RN-09 y CA-09 se reescriben; se quitan `leidas.py` y los modos de lectura de `hook_antes.py`, que queda solo con el freno de escrituras fuera del proyecto |
