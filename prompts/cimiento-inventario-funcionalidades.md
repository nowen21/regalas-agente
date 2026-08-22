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
| 1.1 | Las reglas que no se pueden desobedecer | Las reglas que ninguna otra puede contradecir. No las levanta el dueño del proyecto ni una instrucción dada al asistente: si algo choca con ellas, ellas mandan. | Sin verificar |
| 1.2 | Las reglas de cómo se trabaja | Cómo se escribe el programa, cómo se guardan los datos, cómo se prueba lo hecho y cómo se documenta. Sirven sin importar con qué esté construido, y cada proyecto puede exigir más o menos. | Sin verificar |
| 1.3 | Reglas que se activan solo si aplican | Reglas que un proyecto enciende cuando le corresponden: guardar registros que nunca se modifican, poner el programa a disposición de sus usuarios, o vigilarlo mientras está funcionando. | Sin verificar |
| 1.4 | Las reglas para escribir reglas | Cómo se crea una regla nueva, dónde se guarda, cómo se numera y cómo se retira cuando deja de aplicar. | Sin verificar |
| 1.5 | La explicación para quien llega nuevo | El recorrido completo de un proyecto explicado sin términos técnicos, para quien llega sin conocer el tema. | Sin verificar |
| 1.6 | Reglas para los programas que trabajan solos | Lo que exige un programa que hace por su cuenta lo que haría una persona: que no se rompa si la pantalla cambia, que las tareas esperen en fila, que se distinga «esto no se puede hacer» de «esto falló», y que las contraseñas no queden escritas dentro del programa. | Sin verificar |
| 1.7 | Reglas para los programas que aprenden | Lo que exige un programa que aprende de los datos y toma decisiones: llevar la lista de los que están en uso, que cada uno tenga un responsable con nombre, vigilar más de cerca los que pueden causar más daño, y revisarlos en un plazo escrito. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 7 sin probar, de 7.

## 2. Los pasos de todo proyecto y los documentos que deja

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 2.1 | El orden que no se puede saltar | Primero se escribe qué se necesita, después la lista de lo que el producto debe hacer, después el trabajo repartido en partes, y solo al final se construye y se prueba. Ningún paso se salta, por pequeño que sea el trabajo. | Sin verificar |
| 2.2 | Un formato listo para cada documento | Cada documento del proyecto viene con su formato armado y las preguntas que debe responder, para no empezar de una hoja en blanco. | Sin verificar |
| 2.3 | Nada arranca sin que el dueño diga qué quiere | El trabajo no se reparte en partes hasta que el dueño del proyecto apruebe la lista de lo que el producto debe hacer. | Sin verificar |
| 2.4 | Los informes que se arman solos | Con lo que ya está escrito, el programa arma los informes que alguien va a pedir: qué se pidió, qué de eso ya está hecho, qué falló y cómo está construido por dentro. | Sin verificar |
| 2.5 | Los documentos para entregar | Lo mismo que el proyecto guarda, entregado en el formato de Word que suele pedir quien lo recibe. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 5 sin probar, de 5.

## 3. Lo que se revisa solo

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 3.1 | El programa que revisa | Revisa lo que se puede responder con sí o no: enlaces que no llevan a ninguna parte, referencias a algo que no existe, trabajos dejados a medias y contraseñas escritas donde cualquiera las ve. | Sin verificar |
| 3.2 | Los frenos al guardar | Antes de guardar el trabajo y antes de mandarlo, las revisiones corren solas y no dejan pasar lo que está mal. | Sin verificar |
| 3.3 | Lo que se hace solo en cada sesión | Al abrir la sesión y mientras dura, el programa carga las reglas, registra lo que se dice y guarda lo que hay que recordar, sin que nadie tenga que pedirlo. | Sin verificar |
| 3.4 | La carpeta del proyecto | Qué documentos tiene el proyecto, cuáles le faltan y qué tan completos están los que tiene. | Sin verificar |
| 3.5 | Una sola calificación por proyecto | En vez de tres informes sueltos, una sola calificación que dice qué tan bien va cada proyecto. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 5 sin probar, de 5.

## 4. Lo que se recuerda de una sesión a otra

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 4.1 | Todo lo que se habló, guardado | Todo lo que se dice queda escrito con su hora. Lo registra el programa y no quien conversa, para que nada se pierda ni se altere después. | Sin verificar |
| 4.2 | Lo que quedó de cada sesión | Un resumen de lo que se decidió y de lo que quedó a medias, para no releer la conversación completa. | Sin verificar |
| 4.3 | Lo aprendido que no está en ninguna otra parte | Lo que costó averiguar y no se deduce mirando el programa. Se busca por palabra o por significado. | Sin verificar |
| 4.4 | Cómo prefiere trabajar el dueño | Sus preferencias de trabajo, guardadas junto con el proyecto y no dentro de la herramienta que se usó ese día. | Sin verificar |
| 4.5 | El paso a paso de lo que se hizo | Qué ejecutó el asistente, orden por orden. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 5 sin probar, de 5.

## 5. Poner esto a andar en cada proyecto

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 5.1 | Instalar todo con una sola orden | Con una línea, un proyecto recibe las reglas, los formatos, las revisiones automáticas y la memoria. Si ya los tenía, se actualizan sin borrar lo que alguien haya escrito. | Sin verificar |
| 5.2 | El aviso de que se quedó atrás | Al abrir la sesión, el proyecto avisa si está usando una versión vieja de las reglas. | Sin verificar |
| 5.3 | El camino de ida y vuelta para los errores | Cuando un proyecto encuentra un error en las reglas, lo reporta; se corrige en un solo sitio, y la corrección llega a todos los demás proyectos. | Sin verificar |
| 5.4 | La lista de proyectos | Registrar un proyecto nuevo, cambiarle los datos, darlo de baja y ver cómo va, todo desde la pantalla. | Sin verificar |
| 5.5 | El proyecto nuevo entra solo a la lista | Al instalarse en un proyecto, queda registrado en la lista de inmediato, sin que nadie lo copie a mano. | Sin verificar |
| 5.6 | Ver cómo van todos de una sola vez | La calificación de cada proyecto registrado, sin abrirlos uno por uno. | Sin verificar |
| 5.7 | El tablero de todos los proyectos | Una pantalla que muestra de un vistazo cómo va cada proyecto y avisa cuál se quedó atrás. Necesita antes la fila 5.6. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 7 sin probar, de 7.

## 6. Trabajar el proyecto desde la pantalla

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 6.1 | Cada documento se crea desde la pantalla | Se elige el documento que se necesita y la pantalla lo abre listo para llenar. | Sin verificar |
| 6.2 | Los documentos se llenan y se corrigen ahí | Escribir, cambiar y leer cualquier documento del proyecto sin abrir otro programa aparte. | Sin verificar |
| 6.3 | La lista de lo que el producto debe hacer se maneja ahí | Agregar, cambiar y consultar esa lista desde la misma pantalla. | Sin verificar |
| 6.4 | La pantalla no deja saltarse pasos | No deja repartir el trabajo si antes no se aprobó la lista, ni empezar a construir si antes no se escribió qué se acepta como terminado. | Sin verificar |
| 6.5 | La carpeta del proyecto se consulta ahí | Qué falta y qué está a medias, en el mismo sitio donde se trabaja. | Sin verificar |
| 6.6 | Los documentos se guardan en la base de datos | Lo que se escribe queda en la base de datos, y esa copia es la que manda. | Sin verificar |
| 6.7 | Las revisiones siguen funcionando igual | Aunque los documentos estén en la base de datos, el programa que revisa, los frenos al guardar y la carpeta del proyecto siguen viéndolos. | Sin verificar |

**Cuenta:** 0 probadas bien, 0 probadas mal, 7 sin probar, de 7.

## Qué pasa cuando esto se apruebe

1. Las 36 filas bajan a trabajo, cada una con su nombre y su número.
2. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
