# Inventario de funcionalidades: lo que Cimiento debe tener   ·   `[CAPA 3]`

Esta es la lista completa de lo que Cimiento debe hacer. Cada fila dice qué es, para qué sirve y si ya se probó.

## Cómo se lee

**Están todas: las hechas y las que faltan.** Ninguna se saca porque ya exista o porque ya se haya hablado de ella. Esta lista no dice qué falta: dice qué es Cimiento.

**No dice cuándo ni quién.** Sin fechas, sin quién decidió qué, sin las preguntas que ya se contestaron. Eso se guarda en el planteamiento y en el histórico.

**«Sin verificar» quiere decir que nadie lo ha probado todavía.** No quiere decir que falte. Esa casilla solo la cambia una prueba corrida, y se anota cuál y cuándo.

Con el tiempo esta lista se vuelve el manual de Cimiento. Por eso está escrita para quien va a usarlo.

## 1. Las reglas

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 1.1 | Las reglas que no se pueden desobedecer | Un puñado de reglas que nadie puede saltarse, ni el dueño del proyecto ni quien le dé órdenes al programa. Si otra regla las contradice, mandan estas. | Sin verificar |
| 1.2 | Las reglas de cómo se trabaja | Cómo se escribe el programa, cómo se guardan los datos, cómo se prueba lo hecho y cómo se anota lo que se hizo. Sirven sin importar con qué esté construido, y cada proyecto puede exigir más o menos. | Sin verificar |
| 1.3 | Reglas extra que se encienden si se necesitan | Un proyecto puede activar reglas que otros no necesitan: guardar cosas que nunca se borran, publicar el programa para que la gente lo use, o vigilarlo mientras funciona. | Sin verificar |
| 1.4 | Las reglas para escribir reglas | Cómo se crea una regla nueva, dónde se guarda, cómo se le pone número y cómo se retira cuando deja de servir. | Sin verificar |
| 1.5 | La explicación para el que llega nuevo | Todo el camino de un proyecto contado en palabras normales, para alguien que no sabe nada del tema. | Sin verificar |
| 1.6 | Reglas para los programas que hacen tareas solos | Lo que hay que cuidar cuando un programa hace solo lo que haría una persona: que no se rompa si la pantalla cambia, que las tareas esperen en fila, que se distinga «esto no se puede hacer» de «esto se dañó», y que las contraseñas no queden escritas adentro. | Sin verificar |
| 1.7 | Reglas para los programas que aprenden | Lo que hay que cuidar cuando un programa aprende de los datos y decide cosas: tener la lista de los que están funcionando, que cada uno tenga un responsable con nombre y apellido, vigilar más los que pueden hacer más daño, y revisarlos cada cierto tiempo. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 7 sin probar, de 7.

## 2. Los pasos de todo proyecto y los papeles que deja

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 2.1 | El orden que no se puede saltar | Primero se escribe qué se necesita, después la lista de lo que el producto debe hacer, después el trabajo partido en pedazos, y solo al final se construye y se prueba. Ningún paso se salta, ni cuando el trabajo es chiquito. | Sin verificar |
| 2.2 | Una hoja lista para cada papel | Cada documento del proyecto tiene su hoja ya armada, con las preguntas que hay que contestar, para que nadie empiece de una hoja en blanco. | Sin verificar |
| 2.3 | Nada arranca sin que el dueño diga qué quiere | El trabajo no se parte en pedazos hasta que el dueño del proyecto apruebe la lista de lo que el producto debe hacer. | Sin verificar |
| 2.4 | Los resúmenes que se arman solos | Con lo que ya está escrito, el programa arma los resúmenes que alguien va a pedir: qué se pidió, qué de eso ya está, qué salió mal y cómo está armado por dentro. | Sin verificar |
| 2.5 | Los documentos para entregar | Lo mismo que el proyecto guarda, convertido al formato de Word que suele pedir quien lo recibe. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 5 sin probar, de 5.

## 3. Lo que se revisa solo

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 3.1 | El programa que revisa | Revisa lo que se puede contestar con sí o no: enlaces que no llevan a ninguna parte, menciones a algo que no existe, trabajos dejados a medias y contraseñas escritas donde cualquiera las ve. | Sin verificar |
| 3.2 | Los frenos al guardar | Antes de guardar el trabajo y antes de mandarlo, las revisiones corren solas y no dejan pasar lo que está mal. | Sin verificar |
| 3.3 | Lo que se hace solo en cada conversación | Al empezar a trabajar y mientras se trabaja, el programa carga las reglas, anota lo que se dice y guarda lo que hay que recordar, sin que nadie tenga que acordarse. | Sin verificar |
| 3.4 | La carpeta del proyecto | Qué papeles tiene el proyecto, cuáles le faltan y qué tan llenos están los que tiene. | Sin verificar |
| 3.5 | Una sola nota por proyecto | En vez de tres informes sueltos, una sola nota que dice qué tan bien va cada proyecto. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 5 sin probar, de 5.

## 4. Lo que se recuerda de una vez para otra

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 4.1 | Todo lo que se habló, guardado | Cada cosa que se dice queda escrita con su hora. La escribe el programa y no quien conversa, para que nada se pierda ni se cambie después. | Sin verificar |
| 4.2 | Lo que quedó de cada conversación | Un resumen de lo que se decidió y de lo que quedó a medias, para no tener que leer toda la conversación otra vez. | Sin verificar |
| 4.3 | Lo aprendido que no está en ninguna otra parte | Las cosas que costó averiguar y que no se pueden adivinar mirando el programa. Se buscan por palabra o por lo que quieren decir. | Sin verificar |
| 4.4 | Cómo le gusta trabajar al dueño | Las mañas y preferencias de quien manda, guardadas junto con el proyecto y no dentro del programa que se usó ese día. | Sin verificar |
| 4.5 | El paso a paso de lo que se hizo | Qué órdenes ejecutó el ayudante, una por una. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 5 sin probar, de 5.

## 5. Poner esto a andar en cada proyecto

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 5.1 | Poner todo en un proyecto con una sola orden | Con una línea, un proyecto recibe las reglas, las hojas, las revisiones automáticas y la memoria. Si ya las tenía, se le actualizan sin borrar lo que alguien haya escrito. | Sin verificar |
| 5.2 | El aviso de que se quedó atrás | Apenas se empieza a trabajar, el proyecto avisa si está usando una versión vieja de las reglas. | Sin verificar |
| 5.3 | El camino de ida y vuelta para los errores | Cuando un proyecto encuentra un error en las reglas, lo reporta; el error se arregla en un solo sitio, y el arreglo le llega a todos los demás proyectos. | Sin verificar |
| 5.4 | La lista de proyectos | Anotar un proyecto nuevo, cambiarle los datos, sacarlo de la lista y ver cómo va, todo desde la pantalla. | Sin verificar |
| 5.5 | El proyecto nuevo entra solo a la lista | Cuando se instala en un proyecto, queda anotado en la lista de una vez, sin que nadie lo copie a mano. | Sin verificar |
| 5.6 | Ver cómo van todos de una sola vez | La nota de cada proyecto anotado, sin tener que abrirlos uno por uno. | Sin verificar |
| 5.7 | El tablero de todos los proyectos | Una pantalla que muestra de un vistazo cómo va cada proyecto y avisa cuál se quedó atrás. Necesita antes lo de la fila 5.6. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 7 sin probar, de 7.

## 6. Trabajar el proyecto desde la pantalla

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 6.1 | Cada papel se crea desde la pantalla | Se escoge qué documento se necesita y la pantalla lo abre listo para llenar. | Sin verificar |
| 6.2 | Los papeles se llenan y se corrigen ahí | Escribir, cambiar y leer cualquier documento del proyecto sin abrir otro programa aparte. | Sin verificar |
| 6.3 | La lista de lo que el producto debe hacer se maneja ahí | Agregar, cambiar y consultar esa lista desde la misma pantalla. | Sin verificar |
| 6.4 | La pantalla no deja saltarse pasos | No deja partir el trabajo si antes no se aprobó la lista, ni empezar a construir si antes no se escribió qué se acepta como terminado. | Sin verificar |
| 6.5 | La carpeta del proyecto se ve ahí | Qué falta y qué está a medias, mirado en el mismo sitio donde se trabaja. | Sin verificar |
| 6.6 | Los papeles se guardan en la base de datos | Lo que se escribe queda guardado en la base de datos, y esa copia es la que manda. | Sin verificar |
| 6.7 | Las revisiones siguen funcionando igual | Aunque los papeles estén en la base de datos, el programa que revisa, los frenos al guardar y la carpeta del proyecto siguen viendo todo. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 7 sin probar, de 7.

## Qué pasa cuando esto se apruebe

1. Las 36 filas bajan a trabajo, cada una con su nombre y su número.
2. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
