# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-el-inventario-de-cimiento.md](../../2026-08-22-el-inventario-de-cimiento.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** nada abierto de la sesión anterior; esta arranca con el inventario de funcionalidades de Cimiento.

---

## Hallazgos de esta sesión

### H-1 · El inventario declaró «por confirmar» dos capítulos que ya estaban escritos

| Campo | |
|---|---|
| **Qué pasó** | La fila 1.6 del inventario de Cimiento marcaba los capítulos opt-in de RPA y de IA como «Por confirmar (P-1)», y al verificar contra el repo resultó que están construidos: [`21 · Automatización de procesos`](../../../base/21-automatizacion-de-procesos.md) con `AU1`-`AU8` y [`22 · Sistemas que aprenden de datos`](../../../base/22-sistemas-que-aprenden-de-datos.md) con `IA1`-`IA9`, de los pendientes [08](../../../pendientes/hecho/patrones-rpa.md) (cerrado 2026-08-18) y [12](../../../pendientes/hecho/patron-ia.md) (cerrado 2026-08-19). |
| **Por qué importa** | El inventario es la puerta de las épicas ([`02·F26`](../../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)) y va camino a ser el manual del producto. Un ítem que dice «por confirmar» sobre algo ya construido le pide al usuario una decisión que no existe, y en el peor caso manda a construir dos veces. La fila 1.3 ya los contaba como Existe: el mismo documento se contradecía. |
| **Qué lo soluciona** | Una pieza: el inventario se escribe leyendo el estado real del repo, no de memoria. Acá se corrigió a mano; lo que falta es que la contradicción no pueda quedar escrita. |
| **Qué se decidió** | P-1 anotada como contestada sin objeto, y los dos capítulos bajaron a filas propias (1.6 y 1.7). **La corrección que hice primero —marcar la fila «Existe»— la anuló H-3 el mismo día:** era cambiar un error por otro, porque «Existe» seguía siendo afirmación del agente. |
| **Estado** | `resuelto acá` |
| **Responde a** | EP-001 · HU-013 — Capítulos opt-in de dominio (el trabajo ya estaba hecho; lo que fallaba era su registro en el inventario) |
| **Dispara** | — (por ahora; si vuelve a pasar, es candidato a validador de coherencia del inventario) |
| **Orden de resolución** | — |
| **Dónde queda** | [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md), §1 y §7 |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | 2026-08-22 · el-inventario-de-cimiento |
| **Con qué se retoma** | — |

### H-2 · El tablero de la interfaz queda aprobado, y detrás de la medición masiva

| Campo | |
|---|---|
| **Qué pasó** | El usuario contestó P-2 (**no** entra un segundo agente) y P-3 (**sí** a que la interfaz sea tablero de todos los proyectos, con alertas). |
| **Por qué importa** | Son las dos decisiones de alcance que faltaban para cerrar el inventario. Sin ellas no se derivan épicas nuevas, y el ítem 6.3 quedaba flotando entre «idea» y «trabajo comprometido». |
| **Qué lo soluciona** | Una pieza: el tablero necesita antes que la interfaz sepa medir todos los proyectos de una vez (ítem 5.6), que hoy está por construir. Sin eso, el tablero no tiene qué mostrar. |
| **Qué se decidió** | 6.2 **descartado por ahora**, conservando el contrato del adaptador sin construir nada encima. 6.3 pasa a **Por construir**, dependiente de 5.6. |
| **Estado** | `abierto` — el inventario sigue EN REVISIÓN hasta que el usuario confirme que no falta ninguna funcionalidad |
| **Responde a** | EP-007 · Instalación y actualización — es la épica donde vive el registro de proyectos y su medición |
| **Dispara** | 1. **EP-007 · HU nueva — «la interfaz mide todos los proyectos de una vez»** (ítem 5.6). Como usuario del estándar / quiero ver el veredicto de cumplimiento de cada proyecto registrado sin abrirlos uno por uno / para saber cuál se quedó atrás. Contexto: hoy el registro existe (HU-008 y el canal de defectos), pero la medición es proyecto por proyecto. Va primero porque bloquea la siguiente.<br>2. **EP-007 · HU nueva — «el panel es el tablero de todos los proyectos»** (ítem 6.3). Como usuario del estándar / quiero un panel con el cumplimiento de un vistazo y alertas de lo que se desfasó / para no descubrir tarde que un proyecto quedó sin actualizar. Contexto: sale de P-3, contestada el 2026-08-22; depende de la medición masiva de la historia anterior. |
| **Orden de resolución** | Primero de los abiertos: es lo que falta para que el inventario pase a APROBADO y se abra la puerta de las épicas. |
| **Dónde queda** | [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md), §0, §6 y §7 |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | — |
| **Con qué se retoma** | ¿Falta alguna funcionalidad en las 27 filas del inventario? Con esa respuesta pasa a APROBADO y se escriben las dos historias de EP-007. |


### H-3 · El inventario no era la lista de lo que falta, y el estado no lo fija el agente

| Campo | |
|---|---|
| **Qué pasó** | El usuario corrigió dos cosas de fondo del inventario: «no se debe colocar lo que ya se decidió, el inventario es todo lo que el proyecto debe tener sin importar si ya está hecho» y «cuando se hagan las pruebas es que se sabe si ya se hizo». El agente venía dejando filas por fuera porque «eso ya existe» y llenando 22 «Existe» por lectura del código. |
| **Por qué importa** | El inventario madura hasta ser el manual del producto. Podado, el manual nace sin lo que sí está construido; con estados afirmados, dice que algo funciona sin que nadie lo haya probado. Y es la puerta de las épicas ([`02·F26`](../../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)): lo que no esté en la fila no baja a historia. |
| **Qué lo soluciona** | Dos piezas, las dos hechas acá. Una: el molde encabeza con las dos leyes y cambia la columna de estado por «Verificado», que solo llena la prueba. Otra: gana la columna «De qué se trata», la semilla del manual, escrita a quien va a usar el producto y en la menor extensión con la que se entienda ([`00·ID9`](../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)). |
| **Qué se decidió** | Sin pendiente: se corrigió de una, por instrucción del usuario. Molde reescrito con tres leyes, inventario de Cimiento reescrito con 34 filas, las 34 **Sin verificar**, y versión **32.0.0 MAYOR**, porque un proyecto con inventario escrito tiene que rehacerlo. La tercera ley llegó después: el molde llevaba una sección «Lo que el usuario ya definió» que copiaba decisiones del planteamiento, y se quitó. `02·F26` no se tocó: lo que fallaba era el molde, no la puerta. |
| **Estado** | `resuelto acá` |
| **Responde a** | EP-003 · Documentos modelo y procedimientos guiados |
| **Dispara** | — |
| **Orden de resolución** | — |
| **Dónde queda** | Señal [S-022](../../../documentacion/senales.md) · molde [02-inventario-funcionalidades.md](../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) · [CHANGELOG 32.0.0](../../../CHANGELOG.md) · [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md) |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | 2026-08-22 · el-inventario-de-cimiento |
| **Con qué se retoma** | — |

### H-4 · El índice temático apunta a un resumen que otra sesión renombró

| Campo | |
|---|---|
| **Qué pasó** | `validar.py estandar` falla por un enlace roto: [indice-tematico.md](../indice-tematico.md) línea 553 apunta a `2026-08-22/sesion-3.md`, y ese archivo hoy se llama `el-encuadre-enlaza-la-cadena-no-la-copia.md`. |
| **Por qué importa** | Es la única falla del comprobador en el repositorio, y detiene el `push` de cualquiera. No es de esta sesión: el renombrado lo hizo otra. |
| **Qué lo soluciona** | Una pieza: corregir la línea del índice, o que el renombrado del histórico arregle también el índice temático, como ya hace con el índice del día. |
| **Qué se decidió** | Se corrigió: el enlace apunta ahora al resumen renombrado. Se tocó trabajo de otra sesión porque la falla detenía la publicación de todo el repositorio, y el usuario pidió subir. |
| **Estado** | `resuelto acá` |
| **Responde a** | EP-006 · Memoria de lo aprendido |
| **Dispara** | 1. **EP-006 · HU nueva — «renombrar una sesión arregla todos sus índices»**. Como usuario / quiero que al renombrar un resumen se corrijan todos los índices que lo nombran / para que el comprobador no quede en rojo por un renombrado. Contexto: hoy `historico.py --renombrar` corrige el índice del día pero no el temático, y el hueco ya dejó una falla viva. |
| **Orden de resolución** | Primero de los abiertos: es una falla del comprobador, no una mejora. |
| **Dónde queda** | [historico-chat/resumenes/indice-tematico.md](../indice-tematico.md), línea 553. La historia que dispara sigue sin escribir. |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | 2026-08-22 · el-inventario-de-cimiento |
| **Con qué se retoma** | — |


### H-5 · Todo el ciclo de vida se administra desde la interfaz, y falta decidir dónde vive el documento

| Campo | |
|---|---|
| **Qué pasó** | El usuario contestó P-4: desde la interfaz no se administra solo el inventario, sino **todos los entregables del ciclo**. |
| **Por qué importa** | Cambia el tamaño de lo que hay que construir: no es una fila del inventario, es un grupo entero, y ninguna de las siete épicas existentes cubre la interfaz. |
| **Qué lo soluciona** | Una pieza escrita acá: el grupo 6 del inventario, con cinco filas: los documentos nacen desde la interfaz, se llenan y corrigen ahí, el inventario se administra ahí, la cadena no deja saltar eslabones, y el expediente se consulta donde se trabaja. |
| **Qué se decidió** | El grupo 6 entra al producto, con siete filas. Y el usuario cerró la pregunta de arquitectura: **los documentos viven en la base**. De ahí sale la fila 6.7, que es la exigencia que esa decisión abre: con los documentos en la base, el comprobador, los frenos de git y el expediente tienen que seguir viendo lo que se escribe. Cómo se logra —copia generada al repositorio, o comprobadores que lean la base— es del plan, no del inventario. |
| **Estado** | `abierto` — la decisión está tomada; falta la épica que recoja los grupos 5 y 6 |
| **Responde a** | EP-003 · Documentos modelo y procedimientos guiados, en lo que toca a los moldes; la parte de interfaz no tiene épica |
| **Dispara** | 1. **EP nueva — «La interfaz de Cimiento»**. Como usuario del estándar / quiero administrar los proyectos y su ciclo de vida desde la aplicación / para no depender de editar archivos a mano. Contexto: los grupos 5 y 6 del inventario (12 filas) no caben en ninguna de las siete épicas; EP-007 es el instalador, no la aplicación. No sale solo de este hallazgo: también recoge 5.4 a 5.7.<br>2. **EP nueva · HU — «dónde vive cada documento del ciclo»**. Como usuario / quiero que lo que escribo en la interfaz siga siendo comprobable por los validadores / para no perder los frenos que ya existen. Contexto: depende de P-5; va antes que cualquier historia del grupo 6. |
| **Orden de resolución** | Segundo de los abiertos, detrás de H-4: la falla del comprobador se arregla antes que un diseño nuevo. |
| **Dónde queda** | [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md), grupo 6 y P-5 |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | — |
| **Con qué se retoma** | Abrir la épica de la interfaz: son 14 filas (grupos 5 y 6) que ninguna de las siete existentes cubre. |


### H-6 · La prueba del niño estaba escrita pero el documento no la pasaba

| Campo | |
|---|---|
| **Qué pasó** | El usuario preguntó si un niño que lee las funcionalidades sabe de qué se tratan. Se midió fila por fila: **21 de las 36 no pasaban**, y la columna del nombre estaba peor que la de la descripción. |
| **Por qué importa** | La exigencia se había escrito en el molde una hora antes, y el documento que la estrenaba la incumplía. Una regla que su propio primer caso no cumple no es una regla: es un deseo. Y este documento madura hasta ser el manual del producto, así que el que no lo entienda de afuera se queda sin manual. |
| **Qué lo soluciona** | Dos piezas, las dos hechas acá. Una: el molde dice ahora que la prueba cubre las tres cosas, nombre del grupo, nombre de la funcionalidad y descripción, y trae el ejemplo de una fila que la pasa al lado de una que no. Otra: las 36 filas del inventario de Cimiento reescritas. |
| **Qué se decidió** | Las palabras que se fueron: «núcleo blindado», «expediente», «desfase», «traza», «veredicto», «altas», «enganches», «prompt», «git», «épica», «fase», «eslabones». Ninguna fila cambió de significado: cambiaron de idioma. Versión **32.1.1**. |
| **Estado** | `resuelto acá` |
| **Responde a** | EP-003 · Documentos modelo y procedimientos guiados |
| **Dispara** | — |
| **Orden de resolución** | — |
| **Dónde queda** | [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md) y el molde [02-inventario-funcionalidades.md](../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | 2026-08-22 · el-inventario-de-cimiento |
| **Con qué se retoma** | — |

### H-7 · Escribir claro se pasó de largo y salió infantil

| Campo | |
|---|---|
| **Qué pasó** | Con la prueba del niño recién aplicada, las descripciones empezaron a rodear lo que querían decir: «un puñado de reglas que nadie puede saltarse», «las mañas de quien manda», «ni cuando el trabajo es chiquito». El usuario lo paró: «es cierto que un niño lo debe entender pero tampoco tan infantil». |
| **Por qué importa** | El inventario va camino a ser el manual del producto. Un manual que suena a cuento pierde autoridad, y el lector deja de creerle antes de terminar la fila. La exigencia era que se entendiera, no que sonara sencillo. |
| **Qué lo soluciona** | Una pieza: el molde dice ahora cuál es el tono, y no solo cuál es la prueba. Palabras comunes y frases cortas, sin rodear lo que se quiere decir ni explicar de más, en el tono con que se le explica algo a un adulto que no es del oficio. |
| **Qué se decidió** | Las 36 filas pasadas otra vez, y el ejemplo del molde corregido, porque el «CORRECTO» que traía era justo la versión infantil. Versión **32.1.2**. |
| **Estado** | `resuelto acá` |
| **Responde a** | EP-003 · Documentos modelo y procedimientos guiados |
| **Dispara** | — |
| **Orden de resolución** | — |
| **Dónde queda** | El molde [02-inventario-funcionalidades.md](../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) y [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md) |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | 2026-08-22 · el-inventario-de-cimiento |
| **Con qué se retoma** | — |


### H-8 · El inventario pasa de lista a fuente de verdad del alcance

| Campo | |
|---|---|
| **Qué pasó** | El usuario especificó qué debe permitir el molde del inventario: identificar cada funcionalidad de forma única, su objetivo, a qué parte del sistema pertenece, quién la usa, qué recibe y qué entrega, sus reglas de negocio, de qué depende, cuándo se considera terminada, prioridad y estado, qué hay que construirle y qué hay que tener en cuenta. Y que sirva después para generar planes, historias, tareas, pruebas y documentación. |
| **Por qué importa** | Con una fila por funcionalidad, la lista servía para aprobar el alcance y para armar el manual, pero no para construir: al partir el trabajo había que volver a preguntarlo todo, y por eso dos historias del mismo producto salían con criterios distintos. |
| **Qué lo soluciona** | Dos piezas, las dos hechas acá. Una: el molde pasa de tabla a ficha de catorce campos, con el resumen de una línea por funcionalidad encima. Otra: el inventario de Cimiento migrado, 37 fichas completas. |
| **Qué se decidió** | Numeración `F-001` que no se reutiliza. Tres clases escritas: obligatoria, complementaria y futura, que no es lo mismo que lo que todavía no se sabe si entra. «Terminada cuando» baja tal cual a criterio de aceptación y de ahí salen las pruebas. Estado y Verificado siguen siendo dos casillas. Nada nombra tecnología. Versión **33.0.0**, mayor. |
| **Estado** | `abierto` — las 37 fichas están escritas y falta que el usuario las apruebe |
| **Responde a** | EP-003 · Documentos modelo y procedimientos guiados |
| **Dispara** | 1. **EP-003 · HU nueva — «la ficha de funcionalidad alimenta la historia»**. Como dueño del proyecto / quiero que los criterios escritos en la ficha bajen tal cual a la historia y a sus pruebas / para no escribirlos dos veces ni distinto. Contexto: el molde ya lo declara en su cierre, pero ninguna regla lo exige ni ninguna revisión lo comprueba. |
| **Orden de resolución** | Segundo de los abiertos, detrás de la aprobación del inventario. |
| **Dónde queda** | El molde [02-inventario-funcionalidades.md](../../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) y [prompts/cimiento-inventario-funcionalidades.md](../../../prompts/cimiento-inventario-funcionalidades.md) |
| **Nace en** | 2026-08-22 · el-inventario-de-cimiento |
| **Cerrado en** | — |
| **Con qué se retoma** | Las cuatro preguntas que quedaron abiertas en el inventario, y la aprobación de las 37 fichas. |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, H-3, H-4, H-6 y H-7 |
| Todo hallazgo abierto tiene su pendiente creado | ☐ H-2 y H-5 siguen sin archivo en `pendientes/` |
| Toda historia disparada está escrita en su épica | ☐ las tres historias y la épica de la interfaz están descritas acá, no creadas |
| Lo que se hizo está aprobado y guardado | ☑ comiteado y publicado |

**Falta para cerrar:** bajar H-2 y H-5 a `pendientes/`, y abrir la épica de la interfaz, que es donde caen las 14 filas de los grupos 5 y 6 del inventario.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
