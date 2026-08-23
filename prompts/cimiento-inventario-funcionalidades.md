# Inventario de funcionalidades: lo que Cimiento debe tener   ·   `[CAPA 3]`

Esta es la lista completa de lo que Cimiento debe hacer. De acá salen después los bloques de trabajo, las historias, las tareas, las pruebas y el manual: si algo no está en esta lista, no se construye.

## Cómo se lee

**Están todas: las hechas y las que faltan.** Ninguna se saca porque ya exista o porque ya se haya hablado de ella. Esta lista no dice qué falta: dice qué es Cimiento.

**No dice cuándo ni quién.** Sin fechas, sin quién decidió qué, sin las preguntas que ya se contestaron. Eso se guarda en el planteamiento y en el histórico.

**Estado y Verificado no son lo mismo.** «Estado» es lo que alguien dice que va pasando. «Verificado» es lo único que prueba que está hecho, y solo lo llena una prueba corrida. Las 37 están en «Definida» y sin verificar, porque ninguna ha pasado todavía por una fase con su plan y sus pruebas.

**Cada funcionalidad tiene un número que no se repite ni se reutiliza.** Aunque se descarte, su número queda quemado: hay planes, tareas y pruebas que la nombran por ahí.

## Las tres clases

| Clase | Qué quiere decir |
|---|---|
| **Obligatoria** | Sin esto Cimiento no sirve para lo que se hizo |
| **Complementaria** | Suma valor, pero Cimiento arranca sin ella |
| **Futura** | Se sabe que se quiere, y se decidió que no ahora |

## Resumen

| ID | Funcionalidad | Clase | Parte del sistema | Prioridad | Estado | Verificado |
|---|---|---|---|---|---|---|
| F-001 | Las reglas que no se pueden desobedecer | Obligatoria | Cuerpo de reglas | Alta | Definida | Sin verificar |
| F-002 | Las reglas de cómo se trabaja | Obligatoria | Cuerpo de reglas | Alta | Definida | Sin verificar |
| F-003 | Reglas que se activan solo si aplican | Complementaria | Cuerpo de reglas | Media | Definida | Sin verificar |
| F-004 | Las reglas para escribir reglas | Obligatoria | Cuerpo de reglas | Alta | Definida | Sin verificar |
| F-005 | La explicación para quien llega nuevo | Complementaria | Cuerpo de reglas | Media | Definida | Sin verificar |
| F-006 | Reglas para los programas que trabajan solos | Complementaria | Cuerpo de reglas | Baja | Definida | Sin verificar |
| F-007 | Reglas para los programas que aprenden | Complementaria | Cuerpo de reglas | Baja | Definida | Sin verificar |
| F-008 | El orden que no se puede saltar | Obligatoria | Documentos del ciclo | Alta | Definida | Sin verificar |
| F-009 | Un formato listo para cada documento | Obligatoria | Documentos del ciclo | Alta | Definida | Sin verificar |
| F-010 | Nada arranca sin que el dueño diga qué quiere | Obligatoria | Documentos del ciclo | Alta | Definida | Sin verificar |
| F-011 | Los informes que se arman solos | Complementaria | Documentos del ciclo | Media | Definida | Sin verificar |
| F-012 | Los documentos para entregar | Complementaria | Documentos del ciclo | Media | Definida | Sin verificar |
| F-013 | La lista de las partes del proyecto | Obligatoria | Documentos del ciclo | Media | Definida | Sin verificar |
| F-014 | El programa que revisa | Obligatoria | Comprobador | Alta | Definida | Sin verificar |
| F-015 | Los frenos al guardar | Obligatoria | Enganches | Alta | Definida | Sin verificar |
| F-016 | Lo que se hace solo en cada sesión | Obligatoria | Enganches | Alta | Definida | Sin verificar |
| F-017 | La carpeta del proyecto | Obligatoria | Comprobador | Media | Definida | Sin verificar |
| F-018 | Una sola calificación por proyecto | Complementaria | Comprobador | Media | Definida | Sin verificar |
| F-019 | Todo lo que se habló, guardado | Obligatoria | Memoria | Alta | Definida | Sin verificar |
| F-020 | Lo que quedó de cada sesión | Obligatoria | Memoria | Alta | Definida | Sin verificar |
| F-021 | Lo aprendido que no está en ninguna otra parte | Obligatoria | Memoria | Media | Definida | Sin verificar |
| F-022 | Cómo prefiere trabajar el dueño | Obligatoria | Memoria | Media | Definida | Sin verificar |
| F-023 | El paso a paso de lo que se hizo | Complementaria | Memoria | Baja | Definida | Sin verificar |
| F-024 | Instalar todo con una sola orden | Obligatoria | Instalador | Alta | Definida | Sin verificar |
| F-025 | El aviso de que se quedó atrás | Obligatoria | Enganches | Alta | Definida | Sin verificar |
| F-026 | El camino de ida y vuelta para los errores | Obligatoria | Instalador | Media | Definida | Sin verificar |
| F-027 | La lista de proyectos | Obligatoria | Interfaz | Alta | Definida | Sin verificar |
| F-028 | El proyecto nuevo entra solo a la lista | Obligatoria | Instalador | Media | Definida | Sin verificar |
| F-029 | Ver cómo van todos de una sola vez | Complementaria | Interfaz | Media | Definida | Sin verificar |
| F-030 | El tablero de todos los proyectos | Complementaria | Interfaz | Baja | Definida | Sin verificar |
| F-031 | Cada documento se crea desde la pantalla | Obligatoria | Interfaz | Alta | Definida | Sin verificar |
| F-032 | Los documentos se llenan y se corrigen ahí | Obligatoria | Interfaz | Alta | Definida | Sin verificar |
| F-033 | La lista de funcionalidades se maneja ahí | Obligatoria | Interfaz | Alta | Definida | Sin verificar |
| F-034 | La pantalla no deja saltarse pasos | Obligatoria | Interfaz | Alta | Definida | Sin verificar |
| F-035 | La carpeta del proyecto se consulta ahí | Complementaria | Interfaz | Media | Definida | Sin verificar |
| F-036 | Los documentos se guardan en la base de datos | Obligatoria | Interfaz | Alta | Definida | Sin verificar |
| F-037 | Las revisiones siguen funcionando igual | Obligatoria | Interfaz | Alta | Definida | Sin verificar |

**Cuenta:** 26 obligatorias, 11 complementarias, 0 futuras, de 37. Implementadas: 0. Verificadas: 0.

**Las partes del sistema son siete:** cuerpo de reglas, documentos del ciclo, comprobador, enganches, memoria, instalador e interfaz. La lista completa de partes es la funcionalidad F-013, que todavía no está escrita.

## Las funcionalidades, una por una

### F-001 · Las reglas que no se pueden desobedecer

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Las reglas que ninguna otra puede contradecir. No las levanta el dueño del proyecto ni una instrucción dada al asistente: si algo choca con ellas, ellas mandan. |
| **Para qué sirve** | Para que nada de lo que se pida en una conversación pueda desactivar las protecciones que evitan un daño que no se deshace. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | El asistente, que las carga y las obedece. El dueño del proyecto, que no puede levantarlas. |
| **Qué recibe** | Los archivos de reglas del estándar, al abrir la sesión. |
| **Qué entrega** | Las reglas cargadas en la sesión, por encima de cualquier otra instrucción. |
| **Reglas que debe respetar** | `RN-1` Ninguna capa de un proyecto puede relajarlas ni excluirlas. `RN-2` Un cambio de estado que no se deshace pide aprobación de esa acción concreta, aunque un plan aprobado la contenga. `RN-3` Una contraseña nunca se escribe, ni se registra, ni se guarda. |
| **Depende de** | Ninguna. Es el cimiento del resto. |
| **Terminada cuando** | `CA-1` Al abrir la sesión, las reglas quedan cargadas antes de la primera respuesta. `CA-2` Una instrucción que pida saltarse una de estas reglas se rechaza y se dice por qué. `CA-3` El texto de estas reglas no se puede sobrescribir al instalar en un proyecto. |
| **Qué necesita construirse** | Contenido escrito, más una tarea que corre sola al abrir la sesión. |
| **Prioridad** | Alta. Sin esto, todo lo demás es una recomendación. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es lo único del estándar que no admite excepción por proyecto. Cada regla que se agregue acá encarece toda sesión, así que el grupo se mantiene corto a propósito. |

### F-002 · Las reglas de cómo se trabaja

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Cómo se escribe el programa, cómo se guardan los datos, cómo se prueba lo hecho y cómo se documenta. Sirven sin importar con qué esté construido. |
| **Para qué sirve** | Para que dos proyectos distintos, o dos sesiones del mismo, se trabajen igual sin tener que acordarlo cada vez. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | El asistente, que las aplica. El dueño del proyecto, que puede exigir más o menos en la capa de su proyecto. |
| **Qué recibe** | Los archivos de reglas del estándar y los ajustes propios del proyecto. |
| **Qué entrega** | El conjunto de reglas que rige esa sesión, con los ajustes ya aplicados. |
| **Reglas que debe respetar** | `RN-1` Ninguna nombra un lenguaje, un framework ni una herramienta. `RN-2` Un ajuste del proyecto puede apretar una regla, nunca contradecir el grupo F-001. |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` Cada regla dice una sola cosa exigible y trae un ejemplo de lo correcto y lo incorrecto. `CA-2` Ninguna menciona una tecnología concreta. `CA-3` El proyecto puede apretar una regla desde su propia capa y eso se refleja en la sesión. |
| **Qué necesita construirse** | Contenido escrito. |
| **Prioridad** | Alta. Es el grueso de lo que el producto entrega. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es el grupo que más crece, y el que más rápido se vuelve inmanejable si una regla dice dos cosas a la vez. |

### F-003 · Reglas que se activan solo si aplican

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Reglas que un proyecto enciende cuando le corresponden: guardar registros que nunca se modifican, poner el programa a disposición de sus usuarios, o vigilarlo mientras está funcionando. |
| **Para qué sirve** | Para que un proyecto chico no cargue con exigencias que no le aplican, y uno grande no se quede sin ellas. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | El dueño del proyecto, que decide cuáles enciende. El asistente, que solo aplica las encendidas. |
| **Qué recibe** | La lista de grupos encendidos, declarada por el proyecto. |
| **Qué entrega** | Las reglas de esos grupos, sumadas a las que siempre aplican. |
| **Reglas que debe respetar** | `RN-1` Vienen apagadas: se encienden a propósito, nunca por descuido. `RN-2` Encender un grupo no puede apagar nada de F-001 ni de F-002. |
| **Depende de** | F-002 |
| **Terminada cuando** | `CA-1` Un proyecto declara qué grupos enciende y en la sesión aparecen solo esos. `CA-2` Un grupo apagado no aporta ninguna exigencia. |
| **Qué necesita construirse** | Contenido escrito, más la lectura de lo que el proyecto declara. |
| **Prioridad** | Media. Un proyecto puede empezar sin encender ninguno. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Un grupo escrito sin ningún proyecto que lo use se llena de suposiciones. Conviene escribirlos cuando haya caso real. |

### F-004 · Las reglas para escribir reglas

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Cómo se crea una regla nueva, dónde se guarda, cómo se numera y cómo se retira cuando deja de aplicar. |
| **Para qué sirve** | Para que el cuerpo de reglas no se vuelva un montón de avisos sueltos, y para que nadie tenga que adivinar dónde va lo que quiere agregar. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | El asistente, cada vez que agrega o cambia una regla. El dueño del proyecto, que aprueba el cambio. |
| **Qué recibe** | La necesidad de una regla nueva, o el defecto de una que ya existe. |
| **Qué entrega** | La regla escrita en su sitio, con su número, su entrada en el registro de cambios y la versión subida. |
| **Reglas que debe respetar** | `RN-1` Se busca antes de crear: si ya existe una que lo cubre, se ajusta esa. `RN-2` Una regla exige una sola cosa. `RN-3` Los números no se reutilizan: una regla retirada conserva el suyo. `RN-4` Todo cambio suma entrada al registro y sube la versión. |
| **Depende de** | F-002 |
| **Terminada cuando** | `CA-1` Una regla nueva pasa la revisión de forma que le corresponde antes de darse por escrita. `CA-2` Una regla retirada conserva su texto y su número, y apunta a la que la reemplaza. `CA-3` Un cambio sin entrada en el registro y sin subir la versión no se puede guardar. |
| **Qué necesita construirse** | Contenido escrito, más una revisión automática que lo verifique. |
| **Prioridad** | Alta. Sin esto el cuerpo de reglas se degrada solo. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es el grupo que se aplica a sí mismo, y por eso el más fácil de incumplir sin darse cuenta. |

### F-005 · La explicación para quien llega nuevo

| Campo | Qué dice |
|---|---|
| **De qué se trata** | El recorrido completo de un proyecto explicado sin términos técnicos, para quien llega sin conocer el tema. |
| **Para qué sirve** | Para que alguien pueda entender cómo se trabaja sin leerse el cuerpo de reglas completo. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | Cualquier persona que se acerque al proyecto por primera vez. |
| **Qué recibe** | Nada. Es un documento que se lee. |
| **Qué entrega** | El camino completo contado de principio a fin, con enlace a la regla que manda en cada paso. |
| **Reglas que debe respetar** | `RN-1` No exige nada por su cuenta: solo explica lo que las reglas ya exigen. `RN-2` Si una regla cambia, esto se revisa. |
| **Depende de** | F-002 |
| **Terminada cuando** | `CA-1` Alguien que no conoce el proyecto lee el documento y sabe qué pasos hay que dar y en qué orden. `CA-2` Cada paso enlaza a la regla que lo exige. |
| **Qué necesita construirse** | Contenido escrito. |
| **Prioridad** | Media. El producto funciona sin esto, pero nadie nuevo entra. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Envejece cada vez que una regla cambia, y nadie se da cuenta hasta que engaña a alguien. |

### F-006 · Reglas para los programas que trabajan solos

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Lo que exige un programa que hace por su cuenta lo que haría una persona: que no se rompa si la pantalla cambia, que las tareas esperen en fila, que se distinga «esto no se puede hacer» de «esto falló», y que las contraseñas no queden escritas dentro del programa. |
| **Para qué sirve** | Para que un proyecto de ese tipo no tenga que aprender a golpes lo que ya se sabe del oficio. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | El asistente, en un proyecto que encienda este grupo. |
| **Qué recibe** | La declaración del proyecto de que este grupo aplica. |
| **Qué entrega** | Las exigencias propias de ese tipo de programa, sumadas a las de siempre. |
| **Reglas que debe respetar** | `RN-1` No nombra ninguna herramienta del oficio. `RN-2` Cubre el programa que se construye, no la ejecución del robot. |
| **Depende de** | F-003 |
| **Terminada cuando** | `CA-1` Un proyecto de este tipo enciende el grupo y recibe sus exigencias. `CA-2` Ninguna regla del grupo menciona una herramienta concreta. |
| **Qué necesita construirse** | Contenido escrito. |
| **Prioridad** | Baja. Aplica solo a un tipo de proyecto. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | El asistente construye el programa, no lo ejecuta: no maneja pantallas ni teclado por su cuenta. |

### F-007 · Reglas para los programas que aprenden

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Lo que exige un programa que aprende de los datos y toma decisiones: llevar la lista de los que están en uso, que cada uno tenga un responsable con nombre, vigilar más de cerca los que pueden causar más daño, y revisarlos en un plazo escrito. |
| **Para qué sirve** | Para que nadie ponga a decidir a un programa sin saber quién responde cuando se equivoque. |
| **Parte del sistema** | Cuerpo de reglas |
| **Quién la usa** | El asistente, en un proyecto que encienda este grupo. El responsable de cada modelo, que queda con nombre. |
| **Qué recibe** | La declaración del proyecto de que este grupo aplica. |
| **Qué entrega** | Las exigencias propias de ese tipo de programa, sumadas a las de siempre. |
| **Reglas que debe respetar** | `RN-1` Que el programa sugiera y que el programa ejecute se aprueban por separado. `RN-2` El control se gradúa por lo que la decisión pueda dañar, no por lo que cueste construirlo. |
| **Depende de** | F-003 |
| **Terminada cuando** | `CA-1` Un proyecto de este tipo enciende el grupo y recibe sus exigencias. `CA-2` Todo modelo en uso queda en una lista antes de recibir tráfico. |
| **Qué necesita construirse** | Contenido escrito. |
| **Prioridad** | Baja. Aplica solo a un tipo de proyecto. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Se cruza con las reglas de datos personales y con las de vigilar un sistema en marcha, y hay que evitar repetir lo que aquellas ya exigen. |

### F-008 · El orden que no se puede saltar

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Primero se escribe qué se necesita, después la lista de lo que el producto debe hacer, después el trabajo repartido en partes, y solo al final se construye y se prueba. |
| **Para qué sirve** | Para que nadie empiece a construir sobre un problema que nadie escribió, que es la forma más cara de equivocarse. |
| **Parte del sistema** | Documentos del ciclo |
| **Quién la usa** | El asistente, que no puede avanzar sin el paso anterior. El dueño del proyecto, que aprueba en cada puerta. |
| **Qué recibe** | La necesidad que da origen al trabajo. |
| **Qué entrega** | El trabajo listo para construirse, con cada paso anterior escrito y aprobado. |
| **Reglas que debe respetar** | `RN-1` Ningún paso se salta ni se fusiona, por pequeño que sea el trabajo. `RN-2` Si falta el paso anterior, se detiene y se escribe primero. `RN-3` Una tarea del backlog entra por el principio del camino, no por el final. |
| **Depende de** | F-002 |
| **Terminada cuando** | `CA-1` Intentar construir sin el paso anterior escrito se detiene con el motivo. `CA-2` La cadena completa queda registrada para cada trabajo terminado. |
| **Qué necesita construirse** | Contenido escrito, más una revisión automática que detecte el salto. |
| **Prioridad** | Alta. Es el corazón del producto. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | La tentación de saltarse pasos es mayor cuanto más chico parece el trabajo, y ahí es donde más se ha incumplido. |

### F-009 · Un formato listo para cada documento

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Cada documento del proyecto viene con su formato armado y las preguntas que debe responder, para no empezar de una hoja en blanco. |
| **Para qué sirve** | Para que dos trabajos parecidos no queden documentados de dos formas distintas, y para que nadie se invente qué poner. |
| **Parte del sistema** | Documentos del ciclo |
| **Quién la usa** | El asistente, que copia el formato y lo llena. Quien lea después, que encuentra siempre lo mismo en el mismo sitio. |
| **Qué recibe** | El momento del camino en el que está el trabajo. |
| **Qué entrega** | El formato que corresponde a ese momento, listo para llenar. |
| **Reglas que debe respetar** | `RN-1` Se entrega limpio, sin las marcas de escritura que el estándar prohíbe. `RN-2` Cambiar el nombre de una sección hace que todo documento ya escrito reporte que le falta, así que no se cambia a la ligera. |
| **Depende de** | F-008 |
| **Terminada cuando** | `CA-1` Cada documento del camino tiene su formato. `CA-2` Un documento llenado se puede comparar contra su formato y se sabe qué le falta. |
| **Qué necesita construirse** | Contenido escrito, más una revisión automática que compare documento contra formato. |
| **Prioridad** | Alta. Sin formatos, el camino de F-008 no se puede recorrer. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Los formatos viajan a todos los proyectos: lo que sobre en uno, sobra en todos. |

### F-010 · Nada arranca sin que el dueño diga qué quiere

| Campo | Qué dice |
|---|---|
| **De qué se trata** | El trabajo no se reparte en partes hasta que el dueño del proyecto apruebe la lista de lo que el producto debe hacer. |
| **Para qué sirve** | Para que el alcance no lo suponga quien construye, que es como se terminan escribiendo veintiún trabajos sobre un alcance equivocado. |
| **Parte del sistema** | Documentos del ciclo |
| **Quién la usa** | El dueño del proyecto, que aprueba o corrige. El asistente, que no puede repartir el trabajo antes. |
| **Qué recibe** | La propuesta del proyecto y todo lo que ya se sepa de él. |
| **Qué entrega** | Esta misma lista, aprobada, con cada funcionalidad identificada. |
| **Reglas que debe respetar** | `RN-1` Se lista todo lo que el producto debe tener, esté construido o no. `RN-2` Lo que no esté decidido se marca como pregunta, no como decisión. `RN-3` Cada bloque de trabajo cita las funcionalidades que cubre. |
| **Depende de** | F-008, F-009 |
| **Terminada cuando** | `CA-1` Un intento de repartir el trabajo sin la lista aprobada se detiene. `CA-2` Cada bloque de trabajo nombra por su número las funcionalidades que cubre. `CA-3` Una funcionalidad que no aparece en ningún bloque se reporta. |
| **Qué necesita construirse** | Contenido escrito, más una revisión automática que compruebe la puerta. |
| **Prioridad** | Alta. Es la puerta que evita el error más caro. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Hoy la puerta está escrita como regla pero ninguna revisión automática la comprueba. |

### F-011 · Los informes que se arman solos

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Con lo que ya está escrito, el programa arma los informes que alguien va a pedir: qué se pidió, qué de eso ya está hecho, qué falló y cómo está construido por dentro. |
| **Para qué sirve** | Para no escribir dos veces lo mismo, y para que el informe nunca contradiga al documento del que salió. |
| **Parte del sistema** | Documentos del ciclo |
| **Quién la usa** | El dueño del proyecto y quien reciba la entrega. |
| **Qué recibe** | Los documentos del proyecto ya escritos. |
| **Qué entrega** | Los informes armados, cada uno diciendo de dónde salió cada dato. |
| **Reglas que debe respetar** | `RN-1` No se editan a mano: si algo está mal, se corrige el documento de origen. `RN-2` Si falta el origen, el informe lo dice en vez de inventarlo. |
| **Depende de** | F-009 |
| **Terminada cuando** | `CA-1` Los informes se generan sin escribir nada nuevo. `CA-2` Cambiar el documento de origen y volver a generar cambia el informe. `CA-3` Un dato sin origen aparece marcado como faltante. |
| **Qué necesita construirse** | Lógica que lee documentos y escribe otros. |
| **Prioridad** | Media. Se puede entregar sin esto, escribiéndolos a mano una vez. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | El riesgo es que alguien corrija el informe en vez del origen, y a la siguiente generación se pierda la corrección. |

### F-012 · Los documentos para entregar

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Lo mismo que el proyecto guarda, entregado en el formato de Word que suele pedir quien lo recibe. |
| **Para qué sirve** | Para que la entrega formal no obligue a mantener una segunda copia de todo. |
| **Parte del sistema** | Documentos del ciclo |
| **Quién la usa** | Quien recibe la entrega. El dueño del proyecto, que la produce. |
| **Qué recibe** | Los documentos del proyecto y la lista de cuáles se entregan. |
| **Qué entrega** | Los archivos listos para enviar. |
| **Reglas que debe respetar** | `RN-1` Se generan del original, nunca se mantienen aparte. `RN-2` Lo generado no se corrige a mano. |
| **Depende de** | F-011 |
| **Terminada cuando** | `CA-1` Se produce el paquete de entrega sin escribir nada nuevo. `CA-2` Lo entregado dice lo mismo que el original. |
| **Qué necesita construirse** | Lógica que convierte documentos de un formato a otro. |
| **Prioridad** | Media. Depende de a quién haya que entregarle. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Falta decidir qué documentos entran al paquete y con qué presentación. Es una pregunta abierta para el dueño. |

### F-013 · La lista de las partes del proyecto

| Campo | Qué dice |
|---|---|
| **De qué se trata** | En qué partes está dividido el proyecto por dentro, para qué sirve cada una y dónde está, para que quien llegue después no tenga que adivinarlo. |
| **Para qué sirve** | Para que una parte nueva no aparezca sin que nadie sepa que existe, y para poder decir a qué parte pertenece cada funcionalidad. |
| **Parte del sistema** | Documentos del ciclo |
| **Quién la usa** | El asistente, que la consulta y la actualiza. Quien llegue al proyecto y necesite ubicarse. |
| **Qué recibe** | Cada parte nueva que se cree, antes de cerrar el trabajo que la creó. |
| **Qué entrega** | La lista de partes con su nombre, para qué sirve cada una y dónde vive. |
| **Reglas que debe respetar** | `RN-1` Una parte nueva se registra antes de cerrar el trabajo que la creó. `RN-2` No cuentan como parte nueva un arreglo interno ni un pedazo de una parte que ya existe. |
| **Depende de** | F-009 |
| **Terminada cuando** | `CA-1` La lista existe y nombra todas las partes del proyecto. `CA-2` Cerrar un trabajo que creó una parte nueva sin registrarla se detiene. `CA-3` Cada funcionalidad de esta lista apunta a una parte que existe en ella. |
| **Qué necesita construirse** | Contenido escrito, más una revisión automática. |
| **Prioridad** | Media. Se nota su falta cuando el proyecto ya creció. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Cimiento todavía no tiene la suya, y las siete partes que nombra esta lista salieron de mirar el proyecto, no de un documento. |

### F-014 · El programa que revisa

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Revisa lo que se puede responder con sí o no: enlaces que no llevan a ninguna parte, referencias a algo que no existe, trabajos dejados a medias y contraseñas escritas donde cualquiera las ve. |
| **Para qué sirve** | Para que lo comprobable no dependa de que alguien se acuerde de mirarlo. |
| **Parte del sistema** | Comprobador |
| **Quién la usa** | El asistente, que lo corre. El dueño del proyecto, que lee el resultado. |
| **Qué recibe** | La carpeta del proyecto y qué revisión se quiere correr. |
| **Qué entrega** | La lista de fallas y avisos, cada uno con archivo, línea y la regla que se incumple. |
| **Reglas que debe respetar** | `RN-1` Solo revisa lo que se responde con sí o no, nunca lo que pide criterio. `RN-2` Una falla detiene, un aviso informa, y la diferencia se decide por si hay daño. `RN-3` Cada hallazgo dice qué regla se incumple. |
| **Depende de** | F-002 |
| **Terminada cuando** | `CA-1` Cada revisión se puede correr sola o todas juntas. `CA-2` Todo hallazgo nombra archivo, línea y regla. `CA-3` Corre sin instalar nada aparte. |
| **Qué necesita construirse** | Lógica que lee archivos y reporta. |
| **Prioridad** | Alta. Es lo que hace que las reglas se cumplan sin vigilancia. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Una revisión demasiado ancha llena de avisos que nadie lee, y deja de servir. |

### F-015 · Los frenos al guardar

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Antes de guardar el trabajo y antes de mandarlo, las revisiones corren solas y no dejan pasar lo que está mal. |
| **Para qué sirve** | Para que nada incumplido llegue al repositorio, sin que nadie tenga que acordarse de revisar. |
| **Parte del sistema** | Enganches |
| **Quién la usa** | El asistente y cualquier persona que guarde o publique trabajo. |
| **Qué recibe** | Lo que está a punto de guardarse o publicarse. |
| **Qué entrega** | El paso, o la detención con el motivo y cómo arreglarlo. |
| **Reglas que debe respetar** | `RN-1` Lo que detiene es una falla, no un aviso. `RN-2` El freno de las marcas de escritura falla cuando la cuenta sube, no cuando es distinta de cero. `RN-3` Un cambio de lo que viaja a los proyectos no pasa sin su entrada en el registro y su versión. |
| **Depende de** | F-014 |
| **Terminada cuando** | `CA-1` Guardar algo con una falla se detiene y se dice cuál. `CA-2` Publicar corre la batería completa y se detiene si hay falla. `CA-3` Los frenos se instalan solos al instalar el estándar en un proyecto. |
| **Qué necesita construirse** | Tareas que corren solas en momentos fijos. |
| **Prioridad** | Alta. Sin freno, la revisión es opcional. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Un freno que se salta a menudo deja de ser freno. Si estorba, el problema es la revisión, no el freno. |

### F-016 · Lo que se hace solo en cada sesión

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Al abrir la sesión y mientras dura, el programa carga las reglas, registra lo que se dice y guarda lo que hay que recordar, sin que nadie tenga que pedirlo. |
| **Para qué sirve** | Para que la memoria y el cumplimiento no dependan de que el asistente se acuerde. |
| **Parte del sistema** | Enganches |
| **Quién la usa** | El asistente y el dueño del proyecto, sin hacer nada. |
| **Qué recibe** | La apertura de la sesión y cada mensaje que se envía. |
| **Qué entrega** | Las reglas cargadas, la conversación registrada y los recuerdos guardados donde corresponde. |
| **Reglas que debe respetar** | `RN-1` La conversación la escribe el programa, no el asistente. `RN-2` Lo que se registra solo crece: no se corrige ni se borra. `RN-3` Los recuerdos quedan en el proyecto, no dentro de la herramienta que se usó ese día. |
| **Depende de** | F-001, F-019 |
| **Terminada cuando** | `CA-1` Al abrir la sesión las reglas quedan cargadas sin pedirlo. `CA-2` Cada mensaje queda registrado con su hora. `CA-3` Un recuerdo escrito en la herramienta se mueve solo al proyecto. |
| **Qué necesita construirse** | Tareas que corren solas en momentos fijos. |
| **Prioridad** | Alta. Sin esto se pierde lo que pasó. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es la parte más atada a la herramienta concreta que se use, y por eso vive apartada del resto. |

### F-017 · La carpeta del proyecto

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Qué documentos tiene el proyecto, cuáles le faltan y qué tan completos están los que tiene. |
| **Para qué sirve** | Para saber en un vistazo si un proyecto está documentado o solo lo parece. |
| **Parte del sistema** | Comprobador |
| **Quién la usa** | El dueño del proyecto. El asistente, al abrir la sesión. |
| **Qué recibe** | La carpeta del proyecto y la lista de documentos que el camino exige. |
| **Qué entrega** | Qué hay, qué falta y qué tan lleno está cada documento. |
| **Reglas que debe respetar** | `RN-1` Informa, no detiene. `RN-2` Un documento con su formato copiado y sin llenar cuenta como vacío, no como hecho. |
| **Depende de** | F-009, F-014 |
| **Terminada cuando** | `CA-1` Se lista qué documentos del camino tiene y cuáles le faltan. `CA-2` Un documento sin llenar se reporta como vacío. |
| **Qué necesita construirse** | Lógica que lee archivos y reporta. |
| **Prioridad** | Media. Ayuda a ver el hueco, no lo tapa. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Medir «qué tan lleno» sin criterio es fácil de engañar llenando con relleno. |

### F-018 · Una sola calificación por proyecto

| Campo | Qué dice |
|---|---|
| **De qué se trata** | En vez de tres informes sueltos, una sola calificación que dice qué tan bien va cada proyecto. |
| **Para qué sirve** | Para poder comparar proyectos entre sí y saber cuál necesita atención primero. |
| **Parte del sistema** | Comprobador |
| **Quién la usa** | El dueño del proyecto. |
| **Qué recibe** | El resultado de la instalación, el de la carpeta del proyecto y el del camino recorrido. |
| **Qué entrega** | Una calificación, con el detalle de qué la baja. |
| **Reglas que debe respetar** | `RN-1` La calificación siempre se puede desarmar en las partes que la formaron. `RN-2` No se inventa un número si falta uno de los tres insumos: se dice cuál falta. |
| **Depende de** | F-014, F-017, F-024 |
| **Terminada cuando** | `CA-1` Un proyecto arroja una sola calificación. `CA-2` La calificación se puede desarmar en sus partes. `CA-3` Si falta un insumo, se dice cuál en vez de calcular igual. |
| **Qué necesita construirse** | Lógica que combina resultados. |
| **Prioridad** | Media. Los tres informes ya existen por separado. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Falta acordar cómo pesa cada parte. Es una pregunta abierta para el dueño. |

### F-019 · Todo lo que se habló, guardado

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Todo lo que se dice queda escrito con su hora. Lo registra el programa y no quien conversa, para que nada se pierda ni se altere después. |
| **Para qué sirve** | Porque la conversación se borra y el proyecto no. Sin esto, lo que se acordó ayer no existe mañana. |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El dueño del proyecto y el asistente, en sesiones posteriores. |
| **Qué recibe** | Cada mensaje del dueño y cada respuesta del asistente. |
| **Qué entrega** | El archivo de la sesión, con su hora, y su línea en la lista de sesiones. |
| **Reglas que debe respetar** | `RN-1` Lo escribe el programa: si lo escribe el asistente, sale duplicado y con horas inventadas. `RN-2` Solo crece: no se corrige ni se recorta. `RN-3` Cada sesión recibe un nombre que dice de qué trató. |
| **Depende de** | F-016 |
| **Terminada cuando** | `CA-1` El primer mensaje de una sesión ya queda registrado. `CA-2` Cada anotación lleva la hora del reloj de la máquina. `CA-3` Un cambio en lo ya escrito se detecta y se reporta. |
| **Qué necesita construirse** | Tarea que corre sola, más almacenamiento de archivos. |
| **Prioridad** | Alta. Es la base de toda la memoria. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Ya pasó seis veces que el asistente la escribiera a mano y saliera duplicada. |

### F-020 · Lo que quedó de cada sesión

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Un resumen de lo que se decidió y de lo que quedó a medias, para no releer la conversación completa. |
| **Para qué sirve** | Porque nadie relee una conversación de tres horas para encontrar la decisión que se tomó en el minuto cuarenta. |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El dueño del proyecto y el asistente, al retomar. |
| **Qué recibe** | Cada hallazgo, en el momento en que aparece. |
| **Qué entrega** | El resumen con cada hallazgo, qué lo soluciona, qué se decidió, qué trabajo abre y si quedó cerrado. |
| **Reglas que debe respetar** | `RN-1` Se escribe cuando aparece el hallazgo, no al cerrar: una conversación no tiene final. `RN-2` Un hallazgo que viene de otra sesión se nombra, no se copia. `RN-3` Se anotan los resueltos también. |
| **Depende de** | F-019 |
| **Terminada cuando** | `CA-1` Cada hallazgo queda con los campos que el formato pide. `CA-2` El resumen dice si la sesión se puede cerrar y qué falta. `CA-3` Un resumen sin hallazgos se reporta mientras la sesión ya produjo algo. |
| **Qué necesita construirse** | Contenido escrito, más una tarea que avisa cuando falta. |
| **Prioridad** | Alta. Es lo que se lee, no la conversación. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Lo escribe el asistente, no el programa, y por eso es lo que más se queda sin escribir. |

### F-021 · Lo aprendido que no está en ninguna otra parte

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Lo que costó averiguar y no se deduce mirando el programa. Se busca por palabra o por significado. |
| **Para qué sirve** | Para no volver a pagar el mismo aprendizaje, y para que la razón de una decisión sobreviva a quien la tomó. |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El asistente, antes de decidir algo parecido. El dueño del proyecto. |
| **Qué recibe** | Lo que se decidió, lo que costó averiguar y lo que se descartó. |
| **Qué entrega** | Cada aprendizaje con qué pasó, por qué importa, dónde queda y con qué se relaciona. |
| **Reglas que debe respetar** | `RN-1` Uno que se revierte no se borra: se marca como reemplazado y se enlaza el nuevo. `RN-2` Lo que falta hacer no es un aprendizaje: eso va al backlog. |
| **Depende de** | F-019 |
| **Terminada cuando** | `CA-1` Se puede buscar por palabra exacta y por significado. `CA-2` Un aprendizaje reemplazado sigue existiendo y apunta al que lo reemplaza. |
| **Qué necesita construirse** | Contenido escrito, almacenamiento y búsqueda. |
| **Prioridad** | Media. El proyecto avanza sin esto, pero repitiendo errores. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Se confunde a diario con el backlog: los dos salen del mismo momento y dicen cosas distintas. |

### F-022 · Cómo prefiere trabajar el dueño

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Sus preferencias de trabajo, guardadas junto con el proyecto y no dentro de la herramienta que se usó ese día. |
| **Para qué sirve** | Para no tener que repetir la misma indicación en cada conversación nueva. |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El asistente, que las obedece. El dueño, que las corrige cuando dejan de valer. |
| **Qué recibe** | Lo que el dueño indica sobre cómo quiere que se trabaje. |
| **Qué entrega** | Un archivo por preferencia, con su línea en la lista. |
| **Reglas que debe respetar** | `RN-1` Viven en el proyecto: el almacén de la herramienta queda vacío. `RN-2` Una preferencia con alternativa se cumple por la alternativa más cómoda, así que se escribe sin alternativas. `RN-3` Si el dueño la repite, lo que se arregla es el texto de la preferencia, no la conducta de esa vez. |
| **Depende de** | F-016 |
| **Terminada cuando** | `CA-1` Toda preferencia queda en el proyecto y el almacén de la herramienta queda vacío. `CA-2` Una preferencia escrita en la herramienta se mueve sola. |
| **Qué necesita construirse** | Almacenamiento de archivos, más una tarea que corre sola. |
| **Prioridad** | Media. Sin esto, el dueño repite indicaciones. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | La prueba de que una preferencia funciona no es que esté escrita: es que el dueño no tenga que repetirla. |

### F-023 · El paso a paso de lo que se hizo

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Qué ejecutó el asistente, orden por orden. |
| **Para qué sirve** | Para poder reconstruir cómo se llegó a un resultado cuando algo sale raro. |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El dueño del proyecto, cuando algo no cuadra. |
| **Qué recibe** | Cada orden que el asistente ejecuta. |
| **Qué entrega** | La lista ordenada de lo ejecutado en la sesión. |
| **Reglas que debe respetar** | `RN-1` Ninguna contraseña ni dato sensible queda escrito ahí. `RN-2` Solo crece. |
| **Depende de** | F-016 |
| **Terminada cuando** | `CA-1` Se puede ver qué se ejecutó y en qué orden. `CA-2` Un dato sensible aparece enmascarado. |
| **Qué necesita construirse** | Tarea que corre sola, más almacenamiento. |
| **Prioridad** | Baja. Sirve para averiguar, no para trabajar. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Crece rápido y casi nunca se lee. Vale la pena decidir cuánto se conserva. |

### F-024 · Instalar todo con una sola orden

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Con una línea, un proyecto recibe las reglas, los formatos, las revisiones automáticas y la memoria. Si ya los tenía, se actualizan sin borrar lo que alguien haya escrito. |
| **Para qué sirve** | Para que sumar un proyecto no cueste una tarde de copiar archivos, que es lo que hace que nadie lo haga. |
| **Parte del sistema** | Instalador |
| **Quién la usa** | Quien instala, que suele ser el dueño del proyecto. |
| **Qué recibe** | La carpeta del proyecto donde se va a instalar. |
| **Qué entrega** | El proyecto con todo puesto, y un resumen de qué se agregó, qué se actualizó y qué se dejó igual. |
| **Reglas que debe respetar** | `RN-1` No pisa lo que alguien escribió: lo que ya existe y fue modificado se respeta. `RN-2` Muestra qué va a hacer antes de hacerlo. `RN-3` Corre sin instalar nada aparte. |
| **Depende de** | F-002, F-009, F-015 |
| **Terminada cuando** | `CA-1` Un proyecto vacío queda listo con una sola orden. `CA-2` Volver a correrlo sobre un proyecto ya instalado no borra nada escrito. `CA-3` Antes de tocar nada se muestra qué va a pasar. |
| **Qué necesita construirse** | Lógica que copia y compara archivos. |
| **Prioridad** | Alta. Es la puerta de entrada de todo lo demás. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es lo que más daño puede hacer si se equivoca: escribe dentro de proyectos ajenos. |

### F-025 · El aviso de que se quedó atrás

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Al abrir la sesión, el proyecto avisa si está usando una versión vieja de las reglas. |
| **Para qué sirve** | Para que un proyecto no siga meses con reglas viejas sin que nadie se entere. |
| **Parte del sistema** | Enganches |
| **Quién la usa** | El dueño del proyecto y el asistente. |
| **Qué recibe** | La versión que sigue el proyecto y la versión del estándar. |
| **Qué entrega** | El aviso con la diferencia, y qué cambió en el medio. |
| **Reglas que debe respetar** | `RN-1` Informa, no actualiza solo. `RN-2` Si en la diferencia hay una regla retirada sin adoptar, sí detiene el trabajo. |
| **Depende de** | F-016, F-024 |
| **Terminada cuando** | `CA-1` Un proyecto desactualizado lo sabe en su primer mensaje. `CA-2` El aviso dice qué cambió, no solo que cambió. `CA-3` Una regla retirada sin adoptar detiene el trabajo. |
| **Qué necesita construirse** | Tarea que corre sola, más comparación de versiones. |
| **Prioridad** | Alta. Sin esto la actualización nunca ocurre. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Un aviso que aparece siempre se vuelve ruido y deja de leerse. |

### F-026 · El camino de ida y vuelta para los errores

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Cuando un proyecto encuentra un error en las reglas, lo reporta; se corrige en un solo sitio, y la corrección llega a todos los demás proyectos. |
| **Para qué sirve** | Para que un error encontrado en un proyecto no se arregle diez veces ni se quede sin arreglar nueve. |
| **Parte del sistema** | Instalador |
| **Quién la usa** | Cualquier proyecto instalado. El dueño del estándar, que corrige. |
| **Qué recibe** | El reporte del proyecto que encontró el error. |
| **Qué entrega** | La corrección publicada y el aviso a todos los proyectos. |
| **Reglas que debe respetar** | `RN-1` El proyecto reporta, no corrige el estándar por su cuenta. `RN-2` La corrección sale con su versión, para que se sepa desde cuándo aplica. |
| **Depende de** | F-024, F-025 |
| **Terminada cuando** | `CA-1` Un proyecto puede reportar un error sin salir de su carpeta. `CA-2` La corrección llega a los demás sin que cada uno la busque. |
| **Qué necesita construirse** | Almacenamiento compartido, más lógica de aviso. |
| **Prioridad** | Media. Con pocos proyectos se puede hacer a mano. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | El valor crece con el número de proyectos, y hoy son diez. |

### F-027 · La lista de proyectos

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Registrar un proyecto nuevo, cambiarle los datos, darlo de baja y ver cómo va, todo desde la pantalla. |
| **Para qué sirve** | Para no administrar los proyectos editando un archivo a mano, que es donde se pierden. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto. |
| **Qué recibe** | Los datos de cada proyecto: nombre, dónde está, con qué está construido. |
| **Qué entrega** | La lista consultable, y el archivo que los demás programas siguen leyendo. |
| **Reglas que debe respetar** | `RN-1` Un proyecto dado de baja no se borra: se conserva su historia. `RN-2` Lo que se genera hacia afuera nunca vacía lo que tenía contenido. |
| **Depende de** | F-036 |
| **Terminada cuando** | `CA-1` Se puede registrar, editar, dar de baja y consultar sin tocar un archivo. `CA-2` Un proyecto dado de baja deja de recibir avisos e instalaciones y conserva su historia. `CA-3` Generar la lista hacia afuera con la base vacía se rechaza. |
| **Qué necesita construirse** | Pantalla, lógica de servidor y almacenamiento de datos. |
| **Prioridad** | Alta. Es la primera razón por la que existe la pantalla. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Ya se perdió el contenido tres veces por un generador que volcaba una base vacía sobre el archivo real. |

### F-028 · El proyecto nuevo entra solo a la lista

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Al instalarse en un proyecto, queda registrado en la lista de inmediato, sin que nadie lo copie a mano. |
| **Para qué sirve** | Para que la lista no dependa de que alguien se acuerde de anotar lo que acaba de instalar. |
| **Parte del sistema** | Instalador |
| **Quién la usa** | Quien instala. |
| **Qué recibe** | Los datos del proyecto donde se acaba de instalar. |
| **Qué entrega** | El proyecto anotado en la lista. |
| **Reglas que debe respetar** | `RN-1` Escribe en la lista de verdad, no en el archivo que se genera desde ella. `RN-2` Si el proyecto ya estaba, se actualiza en vez de duplicarse. |
| **Depende de** | F-024, F-027 |
| **Terminada cuando** | `CA-1` Instalar en un proyecto nuevo lo deja anotado sin pasos extra. `CA-2` Instalar dos veces no lo duplica. |
| **Qué necesita construirse** | Lógica de servidor y almacenamiento de datos. |
| **Prioridad** | Media. Anotarlo a mano funciona, hasta que se olvida. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Escribir en el archivo generado en vez de en la lista real fue exactamente el error que ya se cometió. |

### F-029 · Ver cómo van todos de una sola vez

| Campo | Qué dice |
|---|---|
| **De qué se trata** | La calificación de cada proyecto registrado, sin abrirlos uno por uno. |
| **Para qué sirve** | Porque con diez proyectos, revisarlos de a uno significa no revisarlos. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto. |
| **Qué recibe** | La lista de proyectos activos. |
| **Qué entrega** | La calificación de cada uno, con el detalle de qué la baja. |
| **Reglas que debe respetar** | `RN-1` Un proyecto dado de baja no se mide. `RN-2` Si un proyecto no se puede medir, se dice por qué en vez de dejarlo en blanco. |
| **Depende de** | F-018, F-027 |
| **Terminada cuando** | `CA-1` Se mide todo lo registrado con una sola acción. `CA-2` Cada resultado se puede abrir para ver qué lo baja. `CA-3` Un proyecto que no se pudo medir aparece con el motivo. |
| **Qué necesita construirse** | Pantalla y lógica de servidor. |
| **Prioridad** | Media. Es lo que hace útil tener la lista. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Medir diez proyectos puede tardar, y conviene decidir si se mide al pedirlo o cada cierto tiempo. |

### F-030 · El tablero de todos los proyectos

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Una pantalla que muestra de un vistazo cómo va cada proyecto y avisa cuál se quedó atrás. |
| **Para qué sirve** | Para enterarse de que un proyecto se está quedando atrás antes de que sea caro arreglarlo. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto. |
| **Qué recibe** | Las mediciones de todos los proyectos. |
| **Qué entrega** | El panel con el estado de cada uno y los avisos de lo que se desfasó. |
| **Reglas que debe respetar** | `RN-1` Un aviso que aparece siempre deja de leerse: solo se avisa lo que cambió o lo que pasó un límite. |
| **Depende de** | F-029 |
| **Terminada cuando** | `CA-1` Se ve el estado de todos los proyectos en una sola pantalla. `CA-2` Se avisa cuál se quedó atrás y desde cuándo. |
| **Qué necesita construirse** | Pantalla y lógica de servidor. |
| **Prioridad** | Baja. Es la evolución natural de F-029, no su reemplazo. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Falta acordar qué se considera «quedarse atrás» y a partir de cuándo se avisa. |

### F-031 · Cada documento se crea desde la pantalla

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Se elige el documento que se necesita y la pantalla lo abre listo para llenar. |
| **Para qué sirve** | Para que empezar un documento no dependa de saber dónde está su formato ni cómo se llama la carpeta. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto y el asistente. |
| **Qué recibe** | El proyecto y el documento que se quiere crear. |
| **Qué entrega** | El documento creado a partir de su formato, en el sitio que le toca. |
| **Reglas que debe respetar** | `RN-1` Nace de su formato, nunca de una hoja en blanco. `RN-2` No deja crear un documento cuyo paso anterior no exista. |
| **Depende de** | F-009, F-036 |
| **Terminada cuando** | `CA-1` Se crea cualquier documento del camino desde la pantalla. `CA-2` El documento nace con las secciones de su formato. `CA-3` Crear uno sin su paso anterior se rechaza con el motivo. |
| **Qué necesita construirse** | Pantalla, lógica de servidor y almacenamiento de datos. |
| **Prioridad** | Alta. Es la puerta de todo el grupo. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Si el formato cambia, hay que decidir qué pasa con los documentos ya creados con el anterior. |

### F-032 · Los documentos se llenan y se corrigen ahí

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Escribir, cambiar y leer cualquier documento del proyecto sin abrir otro programa aparte. |
| **Para qué sirve** | Para que administrar el proyecto no dependa de editar archivos a mano, que es de donde vienen la mitad de los errores. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto y el asistente. |
| **Qué recibe** | El documento que se quiere abrir y lo que se escriba en él. |
| **Qué entrega** | El documento guardado, con lo escrito. |
| **Reglas que debe respetar** | `RN-1` Lo que se guarda queda en la base de datos, que es la copia que manda. `RN-2` No se pierde lo escrito si dos personas tocan el mismo documento. |
| **Depende de** | F-031, F-036 |
| **Terminada cuando** | `CA-1` Se puede llenar y corregir cualquier documento desde la pantalla. `CA-2` Lo guardado se recupera igual. `CA-3` Dos ediciones a la vez no se pisan en silencio. |
| **Qué necesita construirse** | Pantalla, lógica de servidor y almacenamiento de datos. |
| **Prioridad** | Alta. Sin esto, la pantalla solo sirve para mirar. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Hoy varias sesiones trabajan a la vez sobre los mismos documentos, y eso ya causó choques. |

### F-033 · La lista de funcionalidades se maneja ahí

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Agregar, cambiar y consultar la lista de lo que el producto debe hacer, desde la misma pantalla. |
| **Para qué sirve** | Para que el alcance del proyecto se administre donde se trabaja, y no editando un documento largo a mano. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto, que aprueba y corrige. El asistente, que propone. |
| **Qué recibe** | Cada funcionalidad con sus campos. |
| **Qué entrega** | La lista consultable, filtrable por clase, por parte del sistema y por estado. |
| **Reglas que debe respetar** | `RN-1` El número de una funcionalidad no se reutiliza, aunque se descarte. `RN-2` La casilla de verificación no se llena a mano: la llena la prueba. `RN-3` Una funcionalidad sin «terminada cuando» no se puede aprobar. |
| **Depende de** | F-032 |
| **Terminada cuando** | `CA-1` Se agrega, cambia y consulta una funcionalidad sin tocar el documento. `CA-2` Se puede filtrar por clase, parte y estado. `CA-3` Intentar reutilizar un número se rechaza. `CA-4` La casilla de verificación no admite edición manual. |
| **Qué necesita construirse** | Pantalla, lógica de servidor y almacenamiento de datos. |
| **Prioridad** | Alta. Es la lista de la que sale todo el trabajo. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es la funcionalidad que administra este mismo documento. |

### F-034 · La pantalla no deja saltarse pasos

| Campo | Qué dice |
|---|---|
| **De qué se trata** | No deja repartir el trabajo si antes no se aprobó la lista, ni empezar a construir si antes no se escribió qué se acepta como terminado. |
| **Para qué sirve** | Para que el orden se cumpla porque la pantalla no ofrece otra salida, y no porque alguien se acuerde de la regla. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto y el asistente. |
| **Qué recibe** | El paso que se intenta dar y el estado de los pasos anteriores. |
| **Qué entrega** | El paso permitido, o el rechazo con el motivo y qué falta. |
| **Reglas que debe respetar** | `RN-1` El rechazo dice qué falta y dónde se hace, nunca solo «no se puede». `RN-2` No hay forma de saltarse el orden desde la pantalla. |
| **Depende de** | F-008, F-010, F-031 |
| **Terminada cuando** | `CA-1` Repartir el trabajo sin la lista aprobada se rechaza. `CA-2` Construir sin criterios escritos se rechaza. `CA-3` Cada rechazo dice qué falta y dónde se arregla. |
| **Qué necesita construirse** | Pantalla y lógica de servidor. |
| **Prioridad** | Alta. Es lo que convierte la regla en algo que no se puede incumplir. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Si el bloqueo estorba en un caso legítimo, la gente busca la salida por fuera de la pantalla. Hay que prever el caso excepcional. |

### F-035 · La carpeta del proyecto se consulta ahí

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Qué falta y qué está a medias, en el mismo sitio donde se trabaja. |
| **Para qué sirve** | Para ver el hueco donde se puede tapar, y no en un informe aparte que nadie abre. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El dueño del proyecto. |
| **Qué recibe** | El estado de los documentos del proyecto. |
| **Qué entrega** | Qué documentos hay, cuáles faltan y cuáles están a medias, con el enlace para ir a llenarlos. |
| **Reglas que debe respetar** | `RN-1` Informa, no bloquea. `RN-2` Cada hueco enlaza al sitio donde se llena. |
| **Depende de** | F-017, F-032 |
| **Terminada cuando** | `CA-1` Se ve el estado del ciclo del proyecto en la pantalla. `CA-2` Cada faltante lleva al sitio donde se completa. |
| **Qué necesita construirse** | Pantalla y lógica de servidor. |
| **Prioridad** | Media. El informe ya existe por fuera. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Repite lo que F-017 ya calcula: acá es la forma de verlo, no un cálculo nuevo. |

### F-036 · Los documentos se guardan en la base de datos

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Lo que se escribe queda en la base de datos, y esa copia es la que manda. |
| **Para qué sirve** | Para poder buscar, filtrar y relacionar los documentos entre sí, cosa que un montón de archivos sueltos no permite. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | Todo lo que lea o escriba documentos del proyecto. |
| **Qué recibe** | Cada documento que se crea o se cambia. |
| **Qué entrega** | El documento guardado, recuperable y consultable. |
| **Reglas que debe respetar** | `RN-1` Ante una diferencia entre la base y cualquier copia, manda la base. `RN-2` Nada se guarda de forma que no se pueda recuperar entero. |
| **Depende de** | Ninguna. Es la base del grupo. |
| **Terminada cuando** | `CA-1` Un documento escrito se recupera igual. `CA-2` Se puede buscar por su contenido y por sus datos. `CA-3` La base sobrevive a una actualización del programa sin perder nada. |
| **Qué necesita construirse** | Almacenamiento de datos y lógica de servidor. |
| **Prioridad** | Alta. Todo el grupo 6 se apoya en esto. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es el cambio de fondo del proyecto: hasta hoy todo vivía en archivos. La convivencia con lo que ya está escrito en archivos hay que resolverla, y de eso trata F-037. |

### F-037 · Las revisiones siguen funcionando igual

| Campo | Qué dice |
|---|---|
| **De qué se trata** | Aunque los documentos estén en la base de datos, el programa que revisa, los frenos al guardar y la carpeta del proyecto siguen viéndolos. |
| **Para qué sirve** | Para no perder, al mudar los documentos, todas las comprobaciones que hoy protegen el trabajo. |
| **Parte del sistema** | Interfaz |
| **Quién la usa** | El programa que revisa, los frenos al guardar y quien los lea. |
| **Qué recibe** | Los documentos guardados en la base. |
| **Qué entrega** | Los documentos disponibles para revisar, de la forma que se acuerde. |
| **Reglas que debe respetar** | `RN-1` Ninguna comprobación que hoy existe puede dejar de funcionar. `RN-2` Si se genera una copia hacia afuera, no se edita a mano y nunca vacía lo que tenía contenido. |
| **Depende de** | F-014, F-015, F-017, F-036 |
| **Terminada cuando** | `CA-1` Todas las revisiones que hoy corren siguen corriendo con los documentos en la base. `CA-2` Los frenos al guardar siguen deteniendo lo que está mal. `CA-3` La carpeta del proyecto se sigue calculando igual. |
| **Qué necesita construirse** | Lógica de servidor, y almacenamiento o generación de archivos según lo que se decida. |
| **Prioridad** | Alta. Sin esto, mudar los documentos es perder los frenos. |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Hay dos caminos y falta escoger: que la base genere una copia en archivos, como ya se hace con la lista de proyectos, o que las revisiones aprendan a leer la base. La primera conserva todo lo que funciona hoy; la segunda es más limpia y cuesta más. |

## Preguntas: las contesta el usuario

- **P-1 · ¿Cómo siguen viendo los documentos las revisiones cuando estén en la base?** Un camino es que la base genere una copia en archivos, igual que ya se hace con la lista de proyectos, y nada de lo que hoy funciona se toca. El otro es que las revisiones lean la base, que es más limpio y cuesta más. Propuesta del agente: el primero, y el segundo cuando haya razón para pagarlo. Detiene solo a F-037.
- **P-2 · ¿Qué documentos entran al paquete de entrega y con qué presentación?** Detiene solo a F-012.
- **P-3 · ¿Cómo pesa cada parte en la calificación única de un proyecto?** Detiene solo a F-018.
- **P-4 · ¿A partir de cuándo se considera que un proyecto se quedó atrás?** Detiene solo a F-030.

## Qué pasa cuando esto se apruebe

1. El planteamiento se revisa para que diga esto, y no lo que se hubiera supuesto antes.
2. El trabajo se parte en bloques a partir de esta lista, y cada bloque dice qué funcionalidades cubre por su número.
3. Cada «Terminada cuando» se vuelve el criterio de aceptación de su historia, y de ahí salen las pruebas. No se inventan aparte.
4. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
5. La lista se va volviendo el manual de Cimiento, sin volver a escribirla.
