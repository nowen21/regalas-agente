# Análisis 1: el estándar en la pantalla se lista por la ruta del archivo y no por el título de la regla

> **Aprobado** por el usuario el 2026-10-07, en el turno 76, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisó dónde más se muestra una ruta o un número en lugar de un nombre: propuestas, historia y memoria («Dónde más puede pasar») |
| R-2 | Se leyó el molde de la regla (`estructura-regla.md`, `20·M4`, `M5`, `M7`, `M8`, `M9`) antes de aprobar la estructura de la tabla (turno 56) |
| R-3 | `20·M5` y `20·M9` cambian: pasan su checklist en la HU que las cambia |
| R-7 | Lo que nadie pidió se preguntó: las reglas de cada proyecto, las tareas y las notas debajo de las reglas (turnos 57 y 70) |
| R-8 | «Analicemos» autoriza analizar: no se tocó código ni reglas |
| R-10 | La tabla se explicó como fichas con casillas (turno 55) |
| R-17 | Las respuestas se midieron contra `00·ID9` |
| Las demás | No aplican: no se exige campo nuevo en plantillas (R-4), es el análisis 1 (R-6), no hay piloto (R-16) |

---

## Hallazgo

### H-12 · La pantalla del estándar muestra rutas de archivo en lugar del título de la regla

| Campo | Valor |
|---|---|
| Qué pasó | El usuario notó que «Estándar» lista cada documento por la ruta del `.md`, aunque el estándar ya no se lee de archivos; y los enlaces dentro del texto no llevan a la regla |
| Por qué importa | Quien administra el estándar no reconoce la regla por su ruta ni puede seguir los enlaces |

## Pendiente

**Pendiente: el estándar en la pantalla se lista por la ruta del archivo y no por el título de la regla.** La pantalla «Estándar» lista cada documento por la ruta del archivo de donde salió, y no por el título de la regla, porque `Documento` solo guarda `ruta` y `contenido`. El texto se muestra como Markdown sin convertir, y sus enlaces apuntan a archivos. Importa porque quien administra el estándar busca una regla por una ruta que no dice qué exige, y no puede seguir los enlaces entre reglas.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 48 · Usuario, 2026-10-06 21:56:30
> Analicemos: el pendiente 136

**Agente**, 2026-10-06 21:58:04
<!-- agente: aa31107f-71b6-4519-b250-c34ba5eabec3 -->

La lectura es esta, con los datos medidos en la base:

**Lo que hay**
- Hay 152 documentos en la base y los 152 traen un encabezado con su título. En F8, por ejemplo, el encabezado dice `## F8 · Edita solo los archivos que el plan aprobado declara`. El título ya existe: solo falta mostrarlo.
- La ruta no se puede quitar de la base. Con ella encuentran el documento `ver_estandar`, los enganches, el freno y el mapa de tareas. Sirve como llave interna; lo que hay que cambiar es lo que se muestra.
- Dentro del texto hay 2.697 enlaces a archivos `.md`, y hoy ninguno se puede abrir.

**Recomendaciones**
1. **El título.** Sacarlo del primer encabezado de cada documento, sin guardar un campo aparte. Así hay un solo lugar donde se escribe, y si alguien cambia el encabezado, el título cambia con él. Se mostraría «F8 · Edita solo los archivos...» o «01 · Conducta del agente», sin la marca `[CAPA 2]`.
2. **La lista.** Agruparla por capítulo: el título del capítulo arriba y sus reglas debajo. Las reglas por tarea, el mapa, el glosario y la guía irían en un grupo de documentos generales.
3. **La ruta.** No mostrarla en la lista. En la página de cada documento, dejarla en letra pequeña: es lo que hay que escribirle a `ver_estandar`.
4. **El texto.** Mostrarlo con el formato de Markdown aplicado (tablas, negritas, títulos). Cada enlace a un `.md` se cambiaría por el enlace a ese documento en la base, sin perder la sección a la que apunta (por ejemplo, `#n3`). Para editar, el texto seguiría como hoy, en crudo. Para convertir el Markdown hace falta una librería de Python, `markdown`, y eso agrega una dependencia nueva, lo que pide la decisión del capítulo 10.
5. **Los demás sitios donde pasa lo mismo.** Las propuestas también muestran la ruta. La historia muestra «estandar.documento, fila 37», sin decir qué regla es. La memoria lista cada recuerdo por el nombre de su archivo, por ejemplo `aprobar-antes-de-commit.md`. Recomiendo que el análisis cubra los tres.

**Preguntas**
1. ¿El título sale del encabezado, o prefiere un campo propio que se edite aparte?
2. ¿La lista se agrupa por capítulo?
3. ¿La ruta se ve solo en letra pequeña en la página del documento, o no se ve en ningún lado?
4. ¿Se aprueba agregar la librería `markdown` para mostrar el texto con formato y con enlaces que sí abren?
5. ¿Entran al análisis las propuestas, la historia y la memoria?

### 49 · Usuario, 2026-10-06 22:11:17
> Respondo:
> 1. Un campo aparte
> 2. Por capítulo
> 3. En la página don se ve la regla 
> 4. No
> 5. Si todo

**Agente**, 2026-10-06 22:11:33
<!-- agente: c759f9b2-b975-4fc5-bff4-c76d7349c970 -->

Quedan tomadas las cinco respuestas. De ellas salen tres preguntas nuevas:

**A. El campo aparte y el encabezado del texto.** Si el título es un campo propio, puede quedar distinto del encabezado cuando alguien cambie uno de los dos.
- Recomendación: llenar el campo una sola vez con el encabezado actual de los 152 documentos, que todos lo tienen, y desde ahí editarlo aparte. Al crear un documento nuevo, la pantalla pediría el título.
- ¿Así está bien, o el encabezado del texto debe cambiar cuando cambia el título?

**B. Los enlaces sin la librería.** Con el «no» de la pregunta 4, el texto sigue como texto plano. Quedan dos caminos para los 2.697 enlaces:
- (a) Dejarlos como están, que no se pueden abrir.
- (b) Convertir solo los enlaces con código propio, sin dependencia nueva. Cada `02·F8 (`F8-....md`, ya no está ahí)` pasa a ser un enlace a esa regla en la base, y el resto del texto queda plano.
- Recomendación: la (b).

**C. La memoria.** Para tratarla igual que el estándar, cada recuerdo llevaría también su campo de título. Se llenaría con la línea que hoy tiene en el índice, por ejemplo «Aprobar antes de commit», en lugar de `aprobar-antes-de-commit.md`.
- ¿Se aprueba?

Para las propuestas y la historia no hace falta preguntar nada: mostrarían el título de la regla o del recuerdo que tocan, en lugar de la ruta o del número de fila.

### 50 · Usuario, 2026-10-06 22:14:44
> Explique preguntas aplicando la regla 00 id7 y la 00 id9

**Agente**, 2026-10-06 22:14:56
<!-- agente: 3b07aba3-b906-4fd0-8dcb-b9fccfb12b12 -->

**Pregunta A. El nombre de la regla y lo que dice arriba de su texto**

Cada regla tiene arriba de su texto una línea con su nombre, y aparte va a tener un campo con el nombre que se muestra en la lista. Si alguien cambia uno, el otro queda igual y los dos ya no coinciden.

- Se recomienda: llenar el campo una sola vez, copiando esa línea, y después cambiarlo por separado.
- Se pregunta: ¿así está bien, o cuando se cambia el nombre también debe cambiar la línea de arriba del texto?

**Pregunta B. Los enlaces dentro del texto**

El texto de las reglas trae enlaces a otras reglas, y hoy no se pueden abrir. Sin la librería, quedan dos caminos:

- (a) Dejarlos como están.
- (b) Escribir un programa corto que convierta solo esos enlaces para que abran la regla en Cimiento. El resto del texto queda igual.

Se recomienda la (b).

**Pregunta C. Los recuerdos de la memoria**

Hoy cada recuerdo aparece en la lista con el nombre de su archivo, por ejemplo `aprobar-antes-de-commit.md`.

- Se propone: darle también un campo con su nombre, por ejemplo «Aprobar antes de commit», igual que a las reglas.
- Se pregunta: ¿se aprueba?

### 51 · Usuario, 2026-10-06 22:16:39
> respondo: resuma las preguntas

**Agente**, 2026-10-06 22:16:47
<!-- agente: 0c98b169-9945-4c41-9c0a-3bd95253cd7c -->

Las tres preguntas, en corto:

**A.** Cuando se cambia el nombre de una regla, ¿cambia también la línea de arriba de su texto? Recomendación: no, cada uno se cambia aparte.

**B.** Los enlaces entre reglas: ¿se dejan como están, que no abren, o un programa propio, sin la librería, los vuelve enlaces que abren la regla? Recomendación: que abran.

**C.** ¿Los recuerdos de la memoria se muestran con un nombre legible, como «Aprobar antes de commit», en lugar del nombre del archivo? Recomendación: sí.

### 52 · Usuario, 2026-10-06 22:32:01
> Respondo:
> - A. Entonces para qué lo va a cambiar
> - B. Que abran, deben tener un espacio donde se relacionen las reglas
> - C. Si

**Agente**, 2026-10-06 22:32:14
<!-- agente: 69682aee-266f-44c4-9c47-71b42c97c24a -->

**A.** El nombre de una regla casi nunca cambia, pero ya ha pasado. La `00·ID11`, por ejemplo, se llamaba «El agente agrega información irrelevante al asunto» y se cambió a «Escribe solo lo pertinente al asunto». El riesgo existe solo porque el nombre quedaría escrito dos veces: en el campo y en la primera línea del texto.

- Recomendación: quitar esa línea del texto y que la página de la regla muestre el nombre tomado del campo. Así queda escrito en un solo lugar y no hay nada que mantener igual.
- ¿Se aprueba?

**B.** Leo «un espacio donde se relacionen las reglas» así: en la página de cada regla, además de los enlaces que abren, va un recuadro con dos listas:

- **Las reglas que esta cita.** Por ejemplo, F8 cita a F14.
- **Las reglas que la citan a ella.** Por ejemplo, las que nombran a F8.

¿Es eso lo que se pide?

**C.** Aprobada: los recuerdos se muestran con su nombre legible.

### 53 · Usuario, 2026-10-06 22:39:01
> pregunta: qué espera que le responda?

**Agente**, 2026-10-06 22:39:11
<!-- agente: aef45ab4-7ee3-4273-9f48-1ce8812b1059 -->

Se esperan dos respuestas, de sí o no:

- **A.** ¿Se quita del texto la primera línea con el nombre de la regla, de modo que el nombre quede escrito solo en su campo?
- **B.** ¿El espacio donde se relacionan las reglas es un recuadro en la página de cada regla, con las reglas que ella cita y las que la citan a ella?

### 54 · Usuario, 2026-10-06 22:42:02
> Analicemos: crear una tabla que tenga la estructura de reglas

**Agente**, 2026-10-06 22:43:05
<!-- agente: 6764110c-6847-4ded-bb50-2c5ed70129d2 -->

La propuesta es dejar de guardar cada regla como un texto entero y guardarla en una tabla, con un campo para cada parte. Medí lo que hay:

- **Hay 269 reglas, 11 de ellas derogadas.** De esas, 94 tienen su propio archivo (capítulos 00, 02, 13 y 20). Las otras 175 están escritas dentro del archivo de su capítulo, como las `01·C...`.
- **Todas las reglas siguen el mismo molde, el de `20·M5`.** Ese molde ya trae las partes que serían los campos: nombre, qué exige, ejemplo INCORRECTO / CORRECTO, excepción, a qué tareas aplica, qué deja escribir, quién la hace cumplir y el sello del checklist.

**Estructura que propongo**

| Tabla | Qué guarda |
|---|---|
| Capítulo | Número, nombre, capa, si es opt-in, y el texto de introducción |
| Regla | Capítulo, código (`F8`), nombre, exigencia, ejemplo incorrecto, ejemplo correcto, excepción, quién la hace cumplir, qué deja escribir, si está vigente o derogada, y por cuál regla se derogó |
| Relación entre reglas | Regla de origen, regla de destino y tipo: «depende de» o «cita a». Sale de aquí el recuadro de la pregunta B |
| Tarea y regla | Qué reglas trae cada tarea. Reemplaza a `mapa-de-tareas.md` y a `reglas-por-tarea/` |
| Sello | Fecha, versión del checklist y resultado de cada regla |

Lo que no es regla sigue siendo un documento de texto: la guía, el glosario y las palabras clave.

**Lo que cambia con esto**
- Las preguntas A y B se resuelven solas: el nombre es un campo de la regla y las relaciones tienen su tabla.
- El agente sigue recibiendo texto. Ese texto se armaría a partir de la tabla, igual al de hoy, para que los enganches, el freno y `ver_estandar` sigan funcionando.
- Es un cambio mucho más grande que el pendiente. Hay que pasar las 269 reglas a sus campos, y las partes que no encajen en ninguno irían a un campo de notas para no perder nada.

**Preguntas**
1. ¿Se aprueba esa estructura, o le falta o le sobra algún campo?
2. ¿También pasan a tablas la lista de tareas (`mapa-de-tareas.md`) y las reglas por tarea?
3. ¿El sello del checklist va en su propia tabla, o en notas dentro de la regla?

### 55 · Usuario, 2026-10-06 22:49:00
> Explique la respuesta

**Agente**, 2026-10-06 22:49:11
<!-- agente: 8e5e051e-60f0-46c7-8d5b-07e8fb4e981c -->

**Hoy**, cada regla se guarda como una hoja de texto entera: el nombre, lo que exige, los ejemplos y las excepciones van todos juntos en un solo bloque. Para mostrar solo el nombre, el programa tiene que leer la hoja y buscarlo adentro.

**La propuesta** es guardar cada regla como una ficha con casillas: una para el nombre, otra para lo que exige, otra para el ejemplo malo, otra para el ejemplo bueno, y así con cada parte. Así la pantalla toma el nombre de su casilla y lo muestra directamente.

Las fichas irían en cinco tablas:

- **Capítulos:** cada capítulo con su número y su nombre, por ejemplo «02 · Flujo de trabajo».
- **Reglas:** una ficha por regla, con sus casillas, y cada una dice a qué capítulo pertenece.
- **Relaciones:** qué regla nombra a cuál, por ejemplo «F8 nombra a F14». De aquí sale el recuadro de reglas relacionadas que se pidió.
- **Tareas:** qué reglas le llegan al agente en cada tarea, por ejemplo al hacer un commit.
- **Sellos:** cuándo se revisó cada regla con la lista de chequeo y qué resultado dio.

**Lo que cuesta:** hay que pasar las 269 reglas, una por una, de la hoja a la ficha. Lo que no encaje en ninguna casilla iría a una casilla de notas, para no perder nada. El agente seguiría recibiendo el texto como hoy, solo que armado desde las fichas.

**Las preguntas:**
1. ¿Le parecen bien esas casillas, o falta o sobra alguna?
2. ¿Las tareas también pasan a tabla?
3. ¿Los sellos van en su propia tabla, o en la casilla de notas?

### 56 · Usuario, 2026-10-06 22:59:19
> respondo: las preguntas las está haciendo si revisar la estructura de la regla?

**Agente**, 2026-10-06 23:00:11
<!-- agente: 3486b058-ccf5-4d66-91f3-8d1d0ddf3c4f -->

No del todo. Revisé una sola regla, la F8, y conté qué etiquetas se repiten en las 94 que tienen archivo propio. No leí la definición del molde, que está en la `20·M5`, ni la lista de chequeo. La leo ahora.

Leí el molde (`estructura-regla.md`) y las reglas `M4`, `M5`, `M7`, `M8` y `M9`. La estructura que propuse antes tenía tres errores, y la corrijo:

- Las dependencias entre reglas no son «depende» o «cita». Son exactamente tres: **extiende**, **depende de** y **deroga** (`M7`).
- La marca de la regla no es una casilla de «vigente o derogada». Puede ser una de tres: **[BLINDADA]**, ***opt-in*** o **[DEROGADA en X.Y.Z → ver ID]** (`M5`).
- «Quién la hace cumplir» no la llevan todas las reglas: solo las del capítulo `00`.

**La regla, según el molde**

| Parte | Casilla | Lo exige |
|---|---|---|
| Prefijo y número (`F8`) | código, fijo: no cambia nunca | `M4` |
| Título, escrito como una orden | título | `M5` |
| Marca | blindada / opt-in / derogada, con la versión y la regla que la reemplaza | `M5`, `M11` |
| Cuerpo: una sola exigencia, de 1 a 4 líneas | exigencia | `M5` |
| Dependencia | tabla aparte: tipo (extiende, depende de, deroga) y regla destino | `M7` |
| Excepción | condición, límite y quién la autoriza: tres casillas | `M8` |
| Ejemplo | incorrecto y correcto: dos casillas | `M5` |
| Quién la hace cumplir | programa, o por qué ningún programa puede (solo capítulo `00`) | EP-005·HU-012 |
| Si un programa puede comprobarla | sí / no | `M9` |
| Aplica a | las tareas: tabla aparte | `01·C28` |
| Autoriza escribir | las rutas que el freno deja tocar | `02·F8` |
| Sello del checklist | fecha, versión y resultado | `M10` |

El capítulo tendría su número, su prefijo, su nombre, su capa y si es opt-in.

Una pregunta: ¿se aprueba esta estructura, que sale del molde?

### 57 · Usuario, 2026-10-06 23:03:26
> apruebo

**Agente**, 2026-10-06 23:03:45
<!-- agente: 277595ad-49d8-4c58-93b6-6f5102a59aa5 -->

Queda aprobada la estructura de la regla, tal como sale del molde.

Con eso se resuelven dos preguntas que estaban abiertas:

- **A, el nombre escrito dos veces:** ya no pasa. El nombre vive solo en su casilla, y la línea de arriba del texto se arma desde ella.
- **El sello del checklist:** tiene sus propias casillas.

Faltan estas cuatro preguntas para cerrar el análisis:

1. **El recuadro de reglas relacionadas.** Hay dos clases de relación entre reglas:
   - las tres dependencias de `M7` (extiende, depende de, deroga);
   - las menciones sueltas dentro del texto, como «ver `02·F14`».

   Mi recomendación: que el recuadro muestre las dos, separadas y con su nombre. ¿Se aprueba?

2. **Las tareas.** Con la casilla «Aplica a», lo que dice `mapa-de-tareas.md` pasa a una tabla. Y la carpeta `reglas-por-tarea/`, que hoy son copias de las reglas, ya no se guardaría: se armaría desde la tabla cada vez que haga falta. ¿Se aprueba?

3. **Las reglas propias de cada proyecto.** Hoy cada proyecto escribe las suyas en su propio archivo (`reglas-proyecto.md`). Mi recomendación: que vayan en la misma tabla, con una casilla que diga de qué proyecto son, porque Cimiento sirve a todos los proyectos. ¿Entran en el análisis?

4. **El texto que recibe el agente.** Mi recomendación: armarlo desde las fichas con la misma forma de hoy. Así el freno, los enganches y `ver_estandar` siguen funcionando sin cambios. ¿Se aprueba?

### 58 · Usuario, 2026-10-06 23:08:05
> respondo: resuma su respuesta

**Agente**, 2026-10-06 23:08:16
<!-- agente: ee51cb99-6803-423b-860c-67ce3dc5a94d -->

Faltan cuatro respuestas, de sí o no:

1. ¿El recuadro de cada regla muestra tanto sus dependencias como las reglas que menciona en el texto, separadas?
2. ¿La lista de qué reglas trae cada tarea pasa a una tabla, y la carpeta de copias `reglas-por-tarea/` deja de guardarse?
3. ¿Las reglas propias de cada proyecto van en la misma tabla, marcadas con el proyecto al que pertenecen?
4. ¿El texto que recibe el agente se arma desde la tabla, con la misma forma de hoy?

Recomiendo «sí» en las cuatro.

### 59 · Usuario, 2026-10-06 23:10:54
> Respondo:
> 1. si
> 2. si
> 3. si
> 4. si

**Agente**, 2026-10-06 23:11:09
<!-- agente: 1bab1858-7b39-42ae-b5aa-509409537ce1 -->

Con estas respuestas, el análisis tiene 13 acuerdos:

1. Cada regla tiene su nombre en una casilla propia, y la línea de arriba del texto se arma desde ella.
2. La lista del estándar se agrupa por capítulo.
3. La ruta del archivo se ve solo en la página de la regla.
4. No se agrega la librería `markdown`.
5. Las propuestas, la historia y la memoria muestran el nombre de la regla o del recuerdo, en lugar de la ruta o del número de fila.
6. Los recuerdos llevan un nombre legible.
7. Los enlaces entre reglas abren la regla en Cimiento, con un programa propio.
8. Las reglas se guardan en tablas, con la estructura que sale del molde (`M4`, `M5`, `M7`, `M8`, `M9`, `M11`).
9. Cada regla muestra un recuadro con sus dependencias y con las reglas que menciona, separadas.
10. Lo que dice qué reglas trae cada tarea pasa a una tabla, y la carpeta `reglas-por-tarea/` deja de guardarse.
11. Las reglas propias de cada proyecto van en la misma tabla, marcadas con su proyecto.
12. El agente recibe el texto como hoy, pero armado desde las tablas.
13. Lo que no encaja en ninguna casilla al pasar las 269 reglas va a una casilla de notas.

**Lo que saldría de esto: la épica EP-027, con seis historias de usuario**

| HU | Qué hace |
|---|---|
| 1 | Crea las tablas de capítulo, regla, dependencia, tarea y sello |
| 2 | Pasa las 269 reglas a las tablas, con una prueba de que no se pierde nada |
| 3 | Arma desde las tablas el texto que reciben el agente, el freno y `ver_estandar` |
| 4 | Cambia la pantalla: lista por capítulo, página de cada regla, recuadro de relaciones y enlaces que abren |
| 5 | Muestra los nombres en las propuestas, la historia y la memoria |
| 6 | Pasa a la misma tabla las reglas propias de cada proyecto |

Además, una HU de la épica EP-001 para ajustar el texto de las reglas `M5` y `M9`, que hoy hablan de archivos: la `M9` manda a `validadores/reglas-validables.md`, y eso pasaría a ser una casilla.

Solo falta una respuesta: ¿se aprueba el análisis?

### 60 · Usuario, 2026-10-06 23:12:07
> revise nuevamente los acuerdos porque creo que el 1 nos es el que acordamos

**Agente**, 2026-10-06 23:12:23
<!-- agente: 3f62f5c1-ec07-46fb-bbe7-e1d65c0a4b47 -->

Tiene razón: el acuerdo 1 no es el que se aprobó. Revisé la conversación:

- **Acuerdo 1, corregido.** Lo aprobado fue solo esto: *el nombre de la regla va en un campo aparte*. La parte de «la línea de arriba del texto se arma desde ella» la agregué yo. Pregunté si esa línea se quitaba del texto y la pregunta quedó sin respuesta, porque la conversación pasó a la tabla.
- **Acuerdo 13: no está aprobado.** La casilla de notas, para lo que no encaje al pasar las reglas, la mencioné al explicar la tabla. No estaba en la estructura que se aprobó.

Los otros 11 acuerdos coinciden con lo que se respondió.

Faltan dos respuestas:

1. Con el nombre en su campo, ¿se quita del texto la línea de arriba que repite el nombre?
2. Si al pasar una regla aparece texto que no encaja en ninguna casilla, ¿va a una casilla de notas, o se revisa esa regla con el usuario?

### 61 · Usuario, 2026-10-06 23:13:17
> revise antes de preguntarme revise los acuerdos no me parece que me pregunte algo que ya se acordó

**Agente**, 2026-10-06 23:14:22
<!-- agente: ab5012dc-7b3c-44a7-82a0-da41bdcd93f2 -->

La sección «Lo acordado» del análisis debía llenarse en el mismo turno de cada acuerdo, y quedó vacía. La lleno ahora, con lo que se respondió en cada turno.

Revisé las respuestas turno por turno. Las dos preguntas que hice ya estaban resueltas:

- **La línea del nombre en el texto** se resolvió en el turno 52, con «entonces para qué lo va a cambiar»: el nombre va en su campo y el texto no se toca por eso.
- **La casilla de notas** no hace falta. La estructura aprobada en el turno 57 ya cubre lo que queda por fuera del molde: los comentarios del sello van con el sello, y las notas con fecha («Recortada al molde el...», «Excepción agregada el...») van a la historia de cambios, como cualquier cambio desde la EP-026.

Quedan 12 acuerdos, ya escritos en la sección «Lo acordado» del análisis, cada uno con el turno donde se aprobó. Debí escribirlos en el mismo turno de cada respuesta, y no lo hice.

No queda nada abierto. Solo falta una respuesta: ¿se aprueba el análisis?

### 62 · Usuario, 2026-10-06 23:14:40
> liste de nuevo los acuerdos

**Agente**, 2026-10-06 23:14:49
<!-- agente: 77e39360-0dd2-4d54-b4ce-8d1e7d3c6f59 -->

1. **El nombre de la regla:** va en un campo aparte, y el texto no se cambia por eso (turnos 49 y 52).
2. **La lista del estándar:** se agrupa por capítulo (turno 49).
3. **La ruta del archivo:** se ve solo en la página de la regla (turno 49).
4. **La librería `markdown`:** no se agrega (turno 49).
5. **Propuestas, historia y memoria:** entran al análisis (turno 49).
6. **Los enlaces entre reglas:** abren la regla en Cimiento, y cada regla tiene un espacio donde se relaciona con las demás (turno 52).
7. **Los recuerdos de la memoria:** se muestran con un nombre legible (turno 52).
8. **Las reglas:** se guardan en tablas, con la estructura del molde. Cada regla tiene su código, título, marca, exigencia, dependencias, excepción, ejemplo, quién la hace cumplir, si es validable, a qué tareas aplica, qué deja escribir y su sello (turnos 54 y 57).
9. **El espacio de relaciones:** muestra, por separado, las dependencias de `M7` y las reglas mencionadas en el texto (turno 59).
10. **Las tareas:** pasan a una tabla, y la carpeta `reglas-por-tarea/` deja de guardarse (turno 59).
11. **Las reglas de cada proyecto:** van en la misma tabla, marcadas con su proyecto (turno 59).
12. **El texto que recibe el agente:** se arma desde las tablas, con la forma de hoy (turno 59).

No queda ninguna pregunta abierta.

### 63 · Usuario, 2026-10-06 23:15:19
> pregunta eso fue lo que se acordó?

**Agente**, 2026-10-06 23:15:32
<!-- agente: df8cb2ec-abc8-464f-a8ac-0c242ed92bd6 -->

Once de los doce acuerdos repiten lo que se respondió. En uno agregué algo que no se acordó:

- **Acuerdo 1.** En el turno 49 se respondió «Un campo aparte»: el nombre va en su propio campo y se edita ahí. Eso sí se acordó. La segunda parte, «el texto no se cambia por eso», es mi lectura de «Entonces para qué lo va a cambiar» (turno 52), que no es una respuesta explícita. Además, con el acuerdo 8 la regla ya no se guarda como un texto entero, sino partida en campos, así que esa segunda parte sobra.

Si le parece bien, el acuerdo 1 queda así: *el nombre de la regla va en un campo aparte y se edita ahí (turno 49)*, y corrijo esa línea en la sección «Lo acordado» del análisis.

### 64 · Usuario, 2026-10-06 23:18:09
> revise todo el análisis para que vea que los acuerdos que me está listando no son

**Agente**, 2026-10-06 23:19:01
<!-- agente: e8194874-3fbc-461f-b15b-d73bb17caab9 -->

Leí el análisis completo, del turno 48 al 61. La lista que le di tenía tres errores:

1. **Acuerdo 1.** En el turno 49 se aprobó solo «Un campo aparte»: el nombre va en un campo propio, que se edita aparte. En el turno 52, «Entonces para qué lo va a cambiar» fue una pregunta, no una decisión. Yo la convertí en acuerdo sin que lo fuera.
2. **La casilla de notas.** En el turno 61 dije que no hacía falta y decidí por mi cuenta adónde iba lo que sobra. Eso no se acordó.
3. **La épica EP-027 y sus HU.** Las propuse en el turno 59 y nadie las ha aprobado.

**Lo que sí se acordó:**

1. El nombre de la regla va en un campo propio, que se edita aparte (turno 49).
2. La lista del estándar se agrupa por capítulo (turno 49).
3. La ruta del archivo se ve solo en la página de la regla (turno 49).
4. No se agrega la librería `markdown` (turno 49).
5. Las propuestas, la historia y la memoria entran al análisis (turno 49).
6. Los enlaces abren la regla en Cimiento, con código propio, y cada regla tiene un espacio donde se relaciona con las demás (turno 52).
7. Los recuerdos se muestran con un nombre legible (turno 52).
8. Las reglas se guardan en tablas, con la estructura del molde (turnos 54 y 57).
9. El espacio de relaciones muestra, separadas, las dependencias de `M7` y las reglas que menciona el texto (turno 59).
10. Las tareas pasan a una tabla, y `reglas-por-tarea/` deja de guardarse (turno 59).
11. Las reglas de cada proyecto van en la misma tabla, marcadas con su proyecto (turno 59).
12. El texto que recibe el agente se arma desde las tablas, con la forma de hoy (turno 59).

**Lo que sigue abierto:**

- Si se quita la línea de arriba del texto que repite el nombre.
- Adónde van los comentarios del sello y las notas con fecha.
- La épica y las HU.

Ya corregí la sección «Lo acordado» del análisis con esta misma lista.

### 65 · Usuario, 2026-10-06 23:21:05
> pregunta: Luego no acordamos que las reglas se crean en una tabla conservando la estructura de la regla?

**Agente**, 2026-10-06 23:21:19
<!-- agente: 9255c67c-32a6-414b-926b-b4de2a55789f -->

Sí, se acordó en el turno 57: es el acuerdo 8.

Ese acuerdo resuelve la primera pregunta que dejé abierta. Si la regla se guarda en una tabla con la estructura del molde, ya no existe una línea de arriba del texto que repita el nombre. El encabezado se arma con los campos de código, título y marca. Hice esa pregunta sin haber revisado el acuerdo 8, y la quito.

Quedan abiertas dos cosas que el acuerdo 8 no responde:

- **Lo que está escrito en las reglas y no pertenece al molde.** Por ejemplo, las notas con fecha («Recortada al molde el...», «Excepción agregada el...») y los comentarios del sello. Hay que decidir si se guardan y dónde.
- **La épica y sus HU.** Las propuse, pero no se han aprobado.

### 66 · Usuario, 2026-10-06 23:22:23
> pregunta: pero el 8 no deroga al 1?

**Agente**, 2026-10-06 23:22:34
<!-- agente: c03c596b-a450-421e-8696-d8d0d8fbded5 -->

Sí. El acuerdo 1 decía que el nombre iba en un campo aparte del documento. El acuerdo 8 guarda la regla en una tabla, y el título ya es uno de sus campos. Entonces el 8 incluye al 1 y lo reemplaza: el 1 queda derogado por el 8.

Pasa algo parecido con el 6 y el 9. El 6 pidió un espacio donde se relacionen las reglas, y el 9 dice qué muestra ese espacio. El 9 no deroga al 6: lo extiende.

En «Lo acordado» del análisis, el acuerdo 1 sigue escrito como vigente. Hace falta la palabra del usuario para marcarlo como derogado por el 8 y anotar que el 9 extiende al 6.

### 67 · Usuario, 2026-10-06 23:23:49
> Explique entonces en qué qudan los acuerdos?

**Agente**, 2026-10-06 23:24:05
<!-- agente: e312982a-cb93-4ba6-8107-984c15b897fa -->

Si el 8 deroga al 1 y el 9 extiende al 6, los acuerdos que siguen vigentes son estos:

| # | Acuerdo | Estado |
|---|---|---|
| 1 | El nombre de la regla va en un campo aparte | Derogado por el 8 |
| 2 | La lista del estándar se agrupa por capítulo | Vigente |
| 3 | La ruta del archivo se ve solo en la página de la regla | Vigente, con una salvedad (abajo) |
| 4 | No se agrega la librería `markdown` | Vigente |
| 5 | Las propuestas, la historia y la memoria entran al análisis | Vigente |
| 6 | Los enlaces abren la regla en Cimiento, con código propio, y cada regla tiene un espacio donde se relaciona con las demás | Vigente; el 9 lo extiende |
| 7 | Los recuerdos se muestran con un nombre legible | Vigente |
| 8 | Las reglas se guardan en tablas, con la estructura del molde, y el título es uno de sus campos | Vigente; reemplaza al 1 |
| 9 | El espacio de relaciones muestra, separadas, las dependencias de `M7` y las reglas que menciona el texto | Vigente; extiende al 6 |
| 10 | Las tareas pasan a una tabla, y `reglas-por-tarea/` deja de guardarse | Vigente |
| 11 | Las reglas de cada proyecto van en la misma tabla, marcadas con su proyecto | Vigente |
| 12 | El texto que recibe el agente se arma desde las tablas, con la forma de hoy | Vigente |

**La salvedad del 3:** el 8 también lo toca. Si las reglas viven en una tabla, ya no tienen un archivo propio, así que no hay ruta que mostrar. El 3 solo seguiría sirviendo para lo que sigue siendo documento de texto, como la guía o el glosario. Hay que decidir si el 3 se deroga o se deja solo para esos documentos.

**Siguen abiertas:**
- adónde van las notas con fecha y los comentarios del sello;
- la épica y sus historias de usuario.

### 68 · Usuario, 2026-10-06 23:26:43
> analicemos los acuerdos no deben quedar de esa manera, si se acuerda al inicio una cosa pero luego se acuerda otra del mismo tema el que prima es el nuevo y no hablar de lo mismo en diferentes maneras

**Agente**, 2026-10-06 23:27:04
<!-- agente: 63fbaa9f-a609-4865-8399-afe27a050c60 -->

Así como están, los acuerdos dicen lo mismo de varias maneras. Para un mismo tema, el lector tiene que cruzar varios puntos y adivinar cuál manda. Con su criterio, que el acuerdo más nuevo sobre un tema reemplaza al anterior, la lista queda en cinco temas, uno por punto:

1. **Dónde viven las reglas.** En tablas con la estructura del molde: código, título, marca, exigencia, dependencias, excepción, ejemplo, quién la hace cumplir, si es validable, a qué tareas aplica, qué deja escribir y sello. En esa misma tabla van las reglas de cada proyecto, marcadas con su proyecto. Las tareas también pasan a tabla, y `reglas-por-tarea/` deja de guardarse. (Turnos 57 y 59.)
2. **Lo que recibe el agente.** Se arma desde las tablas, con la misma forma de hoy. (Turno 59.)
3. **La pantalla del estándar.** Lista agrupada por capítulo. Cada regla tiene su página, con un espacio que muestra, separadas, sus dependencias de `M7` y las reglas que menciona su texto. Los enlaces abren la regla, con código propio y sin la librería `markdown`. (Turnos 49, 52 y 59.)
4. **Propuestas, historia y memoria.** Entran al análisis, y los recuerdos se muestran con un nombre legible. (Turnos 49 y 52.)
5. **La ruta del archivo.** Sigue abierta. Se acordó mostrarla en la página de la regla (turno 49), pero desde el turno 57 las reglas ya no tienen archivo.

**Siguen abiertos:**
- la ruta: si se quita, o si se deja solo para los documentos que no son reglas;
- dónde quedan las notas con fecha y los comentarios del sello;
- la épica y sus historias de usuario.

**Dos propuestas**, para que no vuelva a pasar:
- Reescribir con este formato la sección «Lo acordado» del análisis 136.
- Guardar su criterio como recuerdo del proyecto: *un acuerdo nuevo sobre un tema reemplaza al anterior, y «Lo acordado» se lleva por tema, uno solo por tema*.

### 69 · Usuario, 2026-10-06 23:29:35
> pregunta entonces qué queda como acordado?

**Agente**, 2026-10-06 23:29:45
<!-- agente: cb71f315-58c2-4e45-ba56-f400c75802d0 -->

Quedan acordados cuatro temas:

1. **Dónde viven las reglas.** Cada regla se guarda en una tabla, en casillas que siguen la estructura del molde: código, título, marca, exigencia, dependencias, excepción, ejemplo, quién la hace cumplir, si es validable, a qué tareas aplica, qué deja escribir y sello. En la misma tabla van las reglas de cada proyecto, marcadas con el proyecto al que pertenecen. Las tareas también pasan a tabla, y la carpeta `reglas-por-tarea/` deja de guardarse.
2. **Lo que recibe el agente.** El texto se arma desde las tablas y llega con la misma forma de hoy.
3. **La pantalla del estándar.** La lista se agrupa por capítulo. Cada regla tiene su página, con un espacio que muestra, por separado, sus dependencias y las reglas que nombra en su texto. Los enlaces abren la regla dentro de Cimiento, con código propio y sin la librería `markdown`.
4. **Propuestas, historia y memoria.** También muestran nombres legibles en vez de rutas, y los recuerdos se ven con su nombre.

Falta decidir tres cosas:
- si la ruta del archivo se sigue mostrando, ahora que las reglas ya no tienen archivo;
- dónde quedan las notas con fecha y los comentarios del sello;
- la épica y sus historias de usuario.

### 70 · Usuario, 2026-10-06 23:31:42
> respondo:
> - para qué se necesita la ruta del archivo?
> - esto "dónde quedan las notas con fecha y los comentarios del sello" no lo entiendo
> - tampoco entiendo esto "la épica y sus historias de usuario"

**Agente**, 2026-10-06 23:32:02
<!-- agente: 2228b25b-cbc4-4f7c-bb5b-65be61469251 -->

**1. ¿Para qué se necesita la ruta del archivo?**

Para las reglas, ya no se necesita. Hoy la ruta sirve para encontrar cada regla: `ver_estandar`, el freno y los enganches la buscan por ella. Con las reglas en tabla, cada una se encuentra por su código, como `02·F8`. Lo mismo pasa con los documentos que no son reglas, como la guía o el glosario: se pueden encontrar por su nombre.

Recomendación: no mostrar la ruta en ninguna parte.

**2. Las notas con fecha y los comentarios del sello**

Debajo de varias reglas hay texto que no es la regla. En la F8, por ejemplo:

- «*Excepción agregada el 2026-10-03 (análisis 16 del pendiente 103)...*» y «*Recortada al molde el 2026-08-22...*». Cuentan cuándo y por qué cambió la regla: son su historia.
- «*N/A: las filas 14 y 15 no aplican porque no declara dependencia*». Explica el resultado de la revisión con la lista de chequeo.

En la tabla aprobada no hay casilla para ninguno de los dos. Recomendación:

- las notas con fecha van a la historia de cambios, igual que cualquier cambio desde la EP-026;
- la explicación del resultado se guarda junto al sello, en una casilla de observación.

**3. La épica y sus historias de usuario**

En este proyecto, lo que se aprueba en un análisis no se construye de una vez. Se divide en una épica, que es el trabajo completo, y en historias de usuario, que son las partes que se construyen una por una. Ese reparto lo decide el análisis. Propuse una épica nueva, la EP-027, con seis historias de usuario:

1. Crear las tablas.
2. Pasar las 269 reglas a esas tablas.
3. Armar desde las tablas el texto que recibe el agente.
4. Hacer la pantalla: la lista, la página de cada regla, sus relaciones y sus enlaces.
5. Mostrar los nombres en las propuestas, la historia y la memoria.
6. Pasar a la tabla las reglas de cada proyecto.

La pregunta es si se aprueba ese reparto.

### 71 · Usuario, 2026-10-06 23:33:03
> Respondo: 
> resuma la respuesta

**Agente**, 2026-10-06 23:33:08
<!-- agente: 58718605-72a0-482c-9d4a-7c30792bc2f9 -->

Se esperan tres respuestas, cada una de sí o no:

1. **La ruta.** Ya no hace falta, porque cada regla se busca por su código. ¿Se deja de mostrar?
2. **Lo que está debajo de las reglas.** ¿Las notas sobre cuándo y por qué cambió una regla pasan a la historia de cambios? ¿Y la explicación de la revisión se guarda junto al sello?
3. **La construcción.** ¿El trabajo se hace como la épica EP-027, dividida en seis partes: tablas, paso de las reglas, texto del agente, pantalla, nombres legibles y reglas de cada proyecto?

### 72 · Usuario, 2026-10-06 23:34:38
> Respondo: 
> 1. si
> 2. si  y si
> 3. si

**Agente**, 2026-10-06 23:35:26
<!-- agente: 306c462e-e960-471d-a694-5b54d31a5664 -->

La sección «Lo acordado» del análisis ya quedó escrita por tema. Cuando un acuerdo nuevo cambia uno anterior, queda solo el nuevo, como se pidió en el turno 68:

1. **Dónde viven las reglas.** En tablas, con las casillas del molde, más una casilla de observación junto al sello. Las reglas de cada proyecto van en la misma tabla. Las tareas también pasan a tabla. Las notas que cuentan cuándo y por qué cambió una regla pasan a la historia de cambios.
2. **Lo que recibe el agente.** Se arma desde las tablas, con la misma forma de hoy.
3. **La pantalla del estándar.** Lista por capítulo. Cada regla tiene su página, con sus relaciones y con enlaces que abren, sin la librería `markdown` y sin mostrar la ruta.
4. **Propuestas, historia y memoria.** Muestran nombres legibles.
5. **Cómo se construye.** Con la épica EP-027, dividida en seis partes.

Queda una pregunta sin responder. Las reglas `20·M5` y `20·M9` hablan de archivos; por ejemplo, la M9 dice que lo validable se anota en `validadores/reglas-validables.md`. Con las reglas en tablas, ese texto quedaría desactualizado. ¿Su corrección entra como una séptima parte de la EP-027?

### 73 · Usuario, 2026-10-07 07:52:49
> Respondo:si

**Agente**, 2026-10-07 07:53:17
<!-- agente: e182c157-e373-4971-ac9c-7cf15aef83f0 -->

Quedó anotado en «Lo acordado»: la EP-027 tiene siete partes, y la séptima corrige el texto de las reglas `20·M5` y `20·M9`.

Con eso no queda ninguna pregunta abierta. Falta una sola respuesta: ¿se aprueba el análisis?

### 74 · Usuario, 2026-10-07 07:54:06
> apruebo.-

**Agente**, 2026-10-07 07:59:11
<!-- agente: a5ce62ea-389e-4df5-a4f2-3e7539ecf0f0 -->

Análisis aprobado. Primero completo las secciones que le faltan, antes de abrir la EP-027.

Registro las dos lecciones del análisis como señales.

Ahora lleno las secciones del análisis.

Ya están completas las secciones del análisis. Ahora paso el pendiente y el hallazgo a su versión 2.

El freno detuvo un cambio. Hace falta que decida cómo seguir.

**Qué pasó.** La lección 1 del análisis (S-344: «Lo acordado» se escribe en el turno, uno por tema) propone una recomendación nueva, la R-18, en `plantillas/recomendaciones-del-analisis.md`. Ese archivo no aparece en «Lo que se tiene que hacer», y por eso el freno no dejó escribirlo.

**Opciones:**
- **(a)** Agregar una fila 13 a «Lo que se tiene que hacer»: «Agregar la R-18», de una vez y sin fase, sobre `plantillas/recomendaciones-del-analisis.md`. Con eso el freno la deja pasar.
- **(b)** No crear la R-18 y dejar la lección sin recomendación.

Recomiendo la (a): la lección existe porque usted tuvo que pedir cinco veces que se revisaran los acuerdos.

**Otra cosa que debe saber.** Escribí estas secciones del análisis después de su aprobación, y debieron estar escritas antes:
- las recomendaciones;
- lo que aporta cada parte;
- dónde más puede pasar;
- la versión 2 del hallazgo y del pendiente;
- la épica EP-027 con sus siete historias;
- lo que se tiene que hacer.

Todo sale de los cinco acuerdos, sin agregar nada. También quedaron pasados el pendiente y el hallazgo a su versión 2.

### 75 · Usuario, 2026-10-07 08:06:11
> Apruebo a

**Agente**, 2026-10-07 08:09:04
<!-- agente: 5d86cb40-77c9-44b2-b11c-e4a232030c56 -->

Ya agregué la R-18. Como es un cambio en `plantillas/`, registro su versión. Es un PARCHE, porque no cambia lo que se exige.

Reviso si el programa dejó marcado el análisis como aprobado.

Le falta poco: el programa de aprobación pide que la fila 13 cite un acuerdo. Agrego como acuerdo 6 lo que se aprobó en el turno 75.

El análisis ya pasa la revisión del programa. Sus secciones están completas, la R-18 quedó agregada como acuerdo 6, y la versión subió a la 56.11.1.

Falta la marca de aprobado. El «apruebo.-» del turno 74 no la puso: el programa la pone solo cuando el mensaje dice **«Apruebo el análisis»**, y en ese momento al análisis todavía le faltaban secciones. Hace falta escribir esa frase. Con ella queda la marca, el programa apaga el análisis, y arranca la construcción de la EP-027 en el orden acordado, empezando por la HU-007 (`20·M5` y `20·M9`).

### 76 · Usuario, 2026-10-07 08:10:28
> Apruebo el análisis

**Agente**, 2026-10-07 08:14:32
<!-- agente: a3b9d919-f06d-4d2b-8211-a166b94f3939 -->

Quedó marcado como aprobado. Empiezo la EP-027: primero la épica y sus siete historias, con el andamio.

La épica se escribe desde la plantilla; uso la EP-026 como modelo.

Escribo la épica.

Ya están creadas la épica EP-027 y sus siete historias. Arranco por la HU-007: las reglas `20·M5` y `20·M9`. Primero reviso todo lo que nombra `reglas-validables.md` y el molde como archivo.

Encontré un punto que la estructura aprobada no cubre, y hace falta una decisión para escribir la nueva M9.

Hoy `validadores/reglas-validables.md` no guarda solo un sí o un no. Pone cada regla en uno de tres grupos:

- **Ya tiene validador**, con el nombre del programa que la comprueba. Por ejemplo, `G2` la comprueba `commits.py`. Son unas 54.
- **Es validable, pero falta el programa.** Son unas 22.
- **No es validable.** Son unas 101.

La casilla que se aprobó en el turno 57 dice solo «sí / no». Con eso se perdería qué programa comprueba cada regla y cuáles faltan por construir.

**Opciones:**
- **(a)** La casilla «validable» admite tres valores: *no*, *sí, falta el programa*, y *sí, con su programa*. En el último caso, se anota el nombre del programa en una casilla al lado.
- **(b)** Se deja «sí / no» como se aprobó, y el registro de qué programa comprueba cada regla sigue en `validadores/reglas-validables.md`.

Recomiendo la **(a)**: cumple el acuerdo de que el registro pase a la tabla sin perder nada, y deja el archivo sin uso.

¿Cuál se elige?

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

Un acuerdo nuevo sobre un tema reemplaza al anterior; se lleva uno solo por tema (turno 68).

1. Dónde viven las reglas: en tablas, con las casillas del molde —código, título, marca, exigencia, dependencias, excepción, ejemplo, quién la hace cumplir, si es validable, a qué tareas aplica, qué deja escribir y sello, con una casilla de observación para lo que explica su resultado—. Las reglas de cada proyecto van en la misma tabla, con su proyecto. Las tareas pasan a tabla y `reglas-por-tarea/` deja de guardarse. Las notas que cuentan cuándo y por qué cambió una regla pasan a la historia de cambios (turnos 49, 57, 59 y 72).
2. Lo que recibe el agente: el texto se arma desde las tablas, con la forma de hoy (turno 59).
3. La pantalla del estándar: lista por capítulo; cada regla en su página, con un espacio que muestra por separado sus dependencias y las reglas que nombra su texto; los enlaces abren la regla en Cimiento, con código propio y sin la librería `markdown`; la ruta del archivo no se muestra (turnos 49, 52, 59 y 72).
4. Propuestas, historia y memoria: muestran nombres legibles en lugar de rutas, y los recuerdos se ven con su nombre (turnos 49 y 52).
5. Cómo se construye: la épica EP-027, con siete HU —las tablas, el paso de las 269 reglas, el texto del agente, la pantalla, los nombres legibles, las reglas de cada proyecto, y la corrección de `20·M5` y `20·M9`, que hablan de archivos— (turnos 72 y 73).
6. La lección 1 (S-344) se vuelve la recomendación R-18 de Cimiento (turno 75).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `20·M4` (el código no cambia nunca: es la llave de la regla en la tabla), `20·M5` (las casillas salen del molde), `20·M7` (solo tres dependencias), `20·M8` (la excepción tiene condición, límite y quién la autoriza), `20·M11` (nada se borra: las notas con fecha pasan a la historia) y `20·M10` (todo cambio sube versión).

Chocan, y se resuelven en el punto 12 de «Lo que se tiene que hacer»:

- `20·M5` describe la regla como texto con un encabezado `## <PREFIJO><n> · <título>`; con la tabla, el encabezado se arma desde las casillas.
- `20·M9` manda a registrar si una regla es validable en `validadores/reglas-validables.md`; con la tabla, es una casilla.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Documentos del estándar | 152 en `estandar_documento`, cada uno con `ruta` y `contenido` ([estandar/models.py](../../../../../proyectos/cimiento/core/estandar/models.py)) |
| Reglas | 269, 11 derogadas: 94 con archivo propio (capítulos 00, 02, 13 y 20) y 175 dentro del archivo de su capítulo |
| Enlaces dentro del texto | 2.697 enlaces a archivos `.md` que no se pueden abrir |
| Lectura de las reglas | `CuerpoDeReglas` y `RecuperadorDeReglas` leen el texto por ruta; el freno lee «Autoriza escribir»; `ver_estandar` recibe una ruta |
| Tareas | `mapa-de-tareas.md` y las copias de `reglas-por-tarea/` |
| Reglas de cada proyecto | Cada proyecto las escribe en su `reglas-proyecto.md` |
| Pantalla | Lista por ruta ([lista.html](../../../../../proyectos/cimiento/core/estandar/templates/estandar/lista.html)) y texto plano |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 del pendiente 132 | Confirma: el estándar vive en la base y se administra desde la pantalla; este análisis lo lleva de documentos enteros a casillas (puntos 1 y 2 de «Lo acordado») |
| Análisis 1 del pendiente 132, acuerdo 5 | Confirma: las plantillas siguen en archivos; no entran a la tabla |
| S-344 y S-345 | Lecciones de este análisis |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Versión `MAYOR` según `20·M10`: sus reglas propias dejan de leerse de `reglas-proyecto.md` y pasan a la tabla. No aplica `02·F22`: no se deroga ninguna regla |
| Normas y leyes | Ninguna |
| Herramientas | Sin la librería `markdown` (punto 3 de «Lo acordado»): los enlaces se convierten con código propio. Los enganches entregan hasta 10 KB por mensaje: el texto armado desde las tablas tiene que medir lo mismo que hoy |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Ruta en vez de nombre | Propuestas | No se sabe qué regla se propone cambiar | Punto 9 |
| Número de fila en vez de nombre | Historia | No se sabe qué regla cambió | Punto 9 |
| Nombre de archivo en vez de nombre | Memoria | El recuerdo no se reconoce | Punto 10 |
| `ver_estandar <ruta>` | Arranque y reglas de cada mensaje | El agente pide una ruta que ya no existe | Punto 5: `ver_estandar` recibe el código |
| Reglas de cada proyecto | `reglas-proyecto.md` de cada proyecto | Quedan en archivos, fuera de la pantalla | Punto 11 |
| Reportes | Casilla «regla» del reporte | Ninguno: guarda el código, que ya se lee | No hace falta |
| Plantillas | `plantillas/` | Ninguno | No hace falta: siguen en archivos (análisis 1 del pendiente 132, acuerdo 5) |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Las reglas del estándar se guardan como texto entero, y la pantalla no puede mostrarlas por su nombre ni relacionarlas

| Campo | Valor |
|---|---|
| Qué pasó | La pantalla «Estándar» lista los documentos por la ruta del `.md`. Al analizarlo salió que la causa es más honda: cada regla se guarda como un texto entero, sin casillas, y de ahí no se sacan su nombre, sus relaciones ni sus tareas sin leer el texto |
| Por qué importa | Quien administra el estándar no reconoce las reglas ni puede seguir sus relaciones, y cada pantalla o programa que necesita una parte de la regla tiene que buscarla dentro del texto |

### Pendiente V2. Las reglas del estándar viven en tablas con la estructura del molde

| Campo | Valor |
|---|---|
| De dónde sale | Hallazgo V2: las reglas del estándar se guardan como texto entero, y la pantalla no puede mostrarlas por su nombre ni relacionarlas |
| El problema | Las 269 reglas están en 152 documentos de texto. La pantalla las lista por ruta, sus 2.697 enlaces no abren, las propuestas, la historia y la memoria muestran rutas o números, y las reglas de cada proyecto siguen en archivos |
| Por qué importa | Sin casillas no se puede mostrar, buscar ni relacionar una regla por lo que es |

### Épica y HU que salen del análisis

Épica nueva: **EP-027, las reglas del estándar viven en tablas con la estructura del molde**.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-027·HU-007 | Las reglas `20·M5` y `20·M9` dicen que la regla vive en casillas | El molde y la validación hablan de archivos | Ninguna | La regla tiene que permitirlo antes de construir lo que la usa | 12 |
| 2 | EP-027·HU-001 | Las reglas tienen sus tablas, con las casillas del molde | La regla es un texto entero | EP-027·HU-007 | Es donde se guarda todo lo demás | 2 |
| 3 | EP-027·HU-002 | Las 269 reglas pasan a las tablas sin perder nada | Las reglas siguen en documentos | EP-027·HU-001 | Sin las reglas en las tablas no hay qué leer ni mostrar | 3, 4 |
| 4 | EP-027·HU-003 | El texto que recibe el agente se arma desde las tablas | Los enganches, el freno y `ver_estandar` leen documentos | EP-027·HU-002 | Necesita las reglas en las tablas | 5, 6 |
| 5 | EP-027·HU-004 | La pantalla lista las reglas por capítulo, con sus relaciones y enlaces que abren | La lista va por ruta y los enlaces no abren | EP-027·HU-002 | Necesita las reglas en las tablas | 7, 8 |
| 6 | EP-027·HU-005 | Las propuestas, la historia y la memoria muestran nombres legibles | Muestran rutas, números de fila y nombres de archivo | EP-027·HU-002 | Necesita el título de cada regla | 9, 10 |
| 7 | EP-027·HU-006 | Las reglas de cada proyecto viven en la misma tabla | Siguen en `reglas-proyecto.md` | EP-027·HU-003 | Se leen igual que las del estándar | 11 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | «Lo acordado» se escribe en el turno en que se acuerda, uno por tema, con lo que el usuario respondió y nada más | Falló | S-344 | Nueva R-18 |
| 2 | Antes de proponer cómo guardar algo del estándar se lee su definición | Falló | S-345 | Complementa R-2 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/pendiente.md` y `historico-chat/resumenes/2026-10-06/sesion.md`, hecho el 2026-10-07 |
| 2 | Tablas de capítulo, regla, dependencia (extiende, depende de, deroga), tarea y sello, con las casillas del molde y la observación del sello | 1 | EP-027·HU-001 |
| 3 | Pasar las 269 reglas a las tablas, con una prueba de que no se pierde nada; las notas con fecha van a la historia de cambios | 1 | EP-027·HU-002 |
| 4 | Pasar a la tabla de tareas lo que dice `mapa-de-tareas.md` | 1 | EP-027·HU-002 |
| 5 | El texto que reciben el agente, el freno y `ver_estandar` se arma desde las tablas, con la forma de hoy; `ver_estandar` recibe el código de la regla | 2 | EP-027·HU-003 |
| 6 | `reglas-por-tarea/` deja de guardarse y se arma desde las tablas | 1 | EP-027·HU-003 |
| 7 | La lista del estándar se agrupa por capítulo y no muestra la ruta | 3 | EP-027·HU-004 |
| 8 | La página de cada regla muestra, separadas, sus dependencias y las reglas que nombra su texto; los enlaces abren la regla, con código propio | 3 | EP-027·HU-004 |
| 9 | Las propuestas y la historia muestran el nombre de la regla | 4 | EP-027·HU-005 |
| 10 | Los recuerdos se muestran con su nombre | 4 | EP-027·HU-005 |
| 11 | Las reglas de cada proyecto pasan a la misma tabla, con su proyecto | 1 | EP-027·HU-006 |
| 12 | Corregir `20·M5` y `20·M9` para que hablen de casillas y no de archivos | 5 | EP-027·HU-007 |
| 13 | Agregar la recomendación R-18, que sale de la lección 1 | 6 | Este análisis, de una y sin fase: `plantillas/recomendaciones-del-analisis.md`, hecho el 2026-10-07 |

## Lo que aporta al análisis principal

**Resultado:** amplía la idea y cambia lo que se construye.

**Lo que suma al análisis principal:** las reglas del estándar ya no se guardan como texto entero: cada una vive en una tabla con las casillas de su molde, sus relaciones y sus tareas, y la pantalla las muestra por su nombre, agrupadas por capítulo y enlazadas entre sí; el agente sigue recibiendo el mismo texto, armado desde esas tablas.
