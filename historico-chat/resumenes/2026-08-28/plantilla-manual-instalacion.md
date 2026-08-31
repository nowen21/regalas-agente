# 2026-08-28 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-28-plantilla-manual-instalacion.md](../../2026-08-28-plantilla-manual-instalacion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo.

---

## Hallazgos de esta sesión

### H-1 · Quedaron dos plantillas para el mismo documento

- **Qué pasó:** Se escribió una plantilla nueva de manual de instalación en la raíz, sobre un prompt que traía la estructura pedida (25 secciones, etiquetas de ubicación, ambientes, reversión). Ya existía [`plantillas/manual-instalacion.md`](../../../plantillas/manual-instalacion.md), de 407 líneas y la misma finalidad.
- **Por qué importa:** Dos plantillas para lo mismo es el defecto que nombra [`20·M12`](../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md). Quien llene la que encuentre primero entrega un manual sin lo que trae la otra: la nueva no tiene las reglas de redacción ni la carpeta `seguimiento/`; la vieja no tiene ambientes, herramientas de acceso, etiquetas de ubicación ni reversión. Además la nueva está en la raíz, y por la tabla de `CLAUDE.md` y por [`20·M13`](../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) una plantilla va en `plantillas/`.
- **Qué lo soluciona:** Fundir las dos en un solo archivo dentro de `plantillas/`, con las partes de cada una, y borrar el de la raíz. Se hizo en esta misma sesión, así que no dispara ninguna historia.
- **Qué se decidió:** El usuario cortó la duda: «la plantilla es manual-instalacion, no hay más». Se fundieron en una sola, [`plantillas/manual-instalacion.md`](../../../plantillas/manual-instalacion.md), con la estructura nueva de 25 secciones y lo que la anterior exigía y la nueva no traía: las reglas de redacción de la cabecera, la carpeta `seguimiento/`, la exigencia de convertir lo aprendido en paso y no en relato, el control de cambios sin motivos históricos y la lista de comprobación antes de publicar. El archivo de la raíz se borró.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [`plantillas/manual-instalacion.md`](../../../plantillas/manual-instalacion.md), 777 líneas · versión `35.10.0` en [`CHANGELOG.md`](../../../CHANGELOG.md) y [`VERSION`](../../../VERSION), como MENOR porque ninguna regla de `base/` obliga a que un manual ya escrito siga la plantilla vigente ([`20·M10`](../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md))
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-2 · La norma de redacción del estándar no está en `base/`: vive dentro de una plantilla

- **Qué pasó:** Al pedir que la plantilla nueva se redactara en español colombiano, en tercera persona y en infinitivo, no hubo regla de `base/` que citar. Esa exigencia solo está escrita en el cuerpo de dos plantillas ([`plantillas/manual-usuario.md`](../../../plantillas/manual-usuario.md), regla 11, y la de manual de instalación), como si fuera del documento y no del estándar. El anexo [`marcadores-de-ia.md`](../../../base/00-identidad-y-rol/marcadores-de-ia.md) lo dice de frente en su cierre: la norma del español «necesita su propia regla, y todavía no existe».
- **Por qué importa:** [`00·ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) rige todo documento que el agente entrega, pero solo cubre las marcas de generación automática. Cómo se redacta (infinitivo para lo que el lector hace, tercera persona para lo que se explica, sin el impersonal con «se» en las acciones) queda a criterio de cada documento. Un documento que no sea manual de usuario ni manual de instalación no tiene de dónde heredarla.
- **Qué lo soluciona:**
  **EP-001 · HU nueva — «La norma de redacción sube a `base/`»**
  - **Como** agente que entrega documentos en cualquier proyecto
  - **Quiero** una regla de `base/` que fije variedad del español, persona y forma verbal
  - **Para** que la exigencia no dependa de qué plantilla se esté llenando
  - **Contexto:** hoy la convención está enterrada en la regla 11 de dos plantillas. El anexo de marcadores declara el hueco. La regla tiene que ser agnóstica de stack ([`20·M3`](../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)) y decir el idioma del proyecto, no «español colombiano» fijo.
- **Qué se decidió:** Sin decidir. En esta sesión la convención se aplicó a mano sobre la plantilla nueva, copiándola de la plantilla de manual de usuario.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-001 · HU nueva — «La norma de redacción sube a `base/`»
- **Orden de resolución:** 1 de 2 · va primero: la plantilla ya quedó fundida y es la que va a citar la regla nueva.
- **Dónde queda:** [pendiente 93](../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md)
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** —
- **Con qué se retoma:** ¿La regla fija persona y forma verbal para todo documento, o solo para los que lee alguien que no es del oficio?

### H-3 · `validadores/marcas.py` solo cuenta las marcas mecánicas, y eso se lee como si el texto estuviera limpio

- **Qué pasó:** La plantilla nueva pasó el validador con cero marcas mientras todavía tenía tres de la lista: negrita sobre renglones completos en las nueve convenciones, la fórmula «no solo... que está instalado» y el verbo de relleno «permite». Salieron leyendo, no corriendo el programa.
- **Por qué importa:** El propio anexo avisa que de la sección 4 en adelante hace falta leer, pero el «0 en 0 archivos» del validador no lo dice. Quien lo corra y no conozca el anexo va a creer que el documento cumple [`00·ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) entero.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — «El validador de marcas dice qué no comprueba»**
  - **Como** quien corre el validador antes de entregar
  - **Quiero** que la salida nombre las secciones del anexo que el programa no cuenta
  - **Para** no leer un cero como un aprobado
  - **Contexto:** `marcas.py` cubre las secciones 2 y 3 del anexo. Las de la 4 en adelante piden lectura. Hoy la salida no distingue una cosa de la otra.
- **Qué se decidió:** Sin decidir.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-004 · HU nueva — «El validador de marcas dice qué no comprueba»
- **Orden de resolución:** 2 de 2 · es el que menos bloquea: se puede resolver sin esperar al otro.
- **Dónde queda:** [pendiente 91](../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md)
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** —
- **Con qué se retoma:** ¿Basta con que la salida lo diga, o el checklist de entrega tiene que pedir la lectura a mano?

### H-4 · Cinco rojos que ya no eran ciertos, cerrados midiéndolos

- **Qué pasó:** De las 13 historias que arrastraban un «No cumple», cinco tenían una fase posterior que había hecho el trabajo sin declararlo. Se midió el criterio rojo de cada una **ejecutándolo**, las cinco salieron verde, y se escribieron las cinco fases de cierre que declaran el reemplazo. La cuenta pasó de **96 cumplen / 13 no cumplen** a **101 / 8**.
- **Por qué importa:** Un rojo que dejó de ser cierto no se apaga solo. Es [`S-061`](../../../documentacion/senales.md): nadie vuelve a mirar un veredicto en rojo, y mientras tanto la historia manda a buscar un trabajo que ya está hecho. Los cinco llevaban entre seis y doce días así.
- **Qué lo soluciona:** Ya está hecho. El mecanismo era `EP-004·HU-023`, que existía desde el 2026-08-27 y solo se había usado tres veces.
- **Qué se decidió:** Seguir el precedente de `af3dbd1`: el molde de fase se aprueba una vez para las cinco, y **las cifras de cada documento las mide un programa**, con el criterio de suspensión adentro. Una fase cuya medición saliera en rojo no se escribía. Las cinco salieron verde, así que se escribieron las cinco.
- **Estado:** resuelto acá
- **Responde a:** EP-002 · HU-003 y HU-004 · EP-004 · HU-003 · EP-005 · HU-003 y HU-008
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** Las cinco fases nuevas en sus historias · el medidor y el generador en [`historico-chat/scripts/2026-08-29/`](../../scripts/2026-08-29/) · el `Estado` y la tabla de fases de las cinco historias, al día
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-5 · Hay 26 documentos con un carácter de control invisible pegado dentro

- **Qué pasó:** Al mirar la tabla de fases de una historia para agregarle una fila, la fila existente empezaba con un `U+0001` en vez de con la barra de la tabla, así que esa fila no se renderiza como fila. Buscándolo, aparece en **26 archivos `.md`**, 13 de ellos en `documentacion/`.
- **Por qué importa:** No se ve leyendo y sobrevive a cualquier reescritura del contenido. Rompe la tabla en silencio: quien lea la historia en un visor de markdown no ve el renglón de esa fase. Es la clase de marca que la sección 3 del anexo [`marcadores-de-ia.md`](../../../base/00-identidad-y-rol/marcadores-de-ia.md) manda quitar, y `U+0001` no está en su lista.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — «Los caracteres de control invisibles se cuentan y se quitan»**
  - **Como** quien lee un documento del proyecto
  - **Quiero** que ningún carácter de control se cuele en un `.md`
  - **Para** que una tabla no se rompa sin que nadie lo vea
  - **Contexto:** [`validadores/marcas.py`](../../../validadores/marcas.py) ya cuenta y limpia siete caracteres invisibles. `U+0001` no es uno de ellos, y hay 26 archivos con él.
- **Qué se decidió:** No tocarlo en esta sesión. Son 26 archivos ajenos al trabajo de hoy, y arreglarlos de paso los metería en un commit que no habla de eso.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-004 · HU nueva — «Los caracteres de control invisibles se cuentan y se quitan»
- **Orden de resolución:** 3 de 3 · el más barato de los tres abiertos, y el que menos bloquea.
- **Dónde queda:** [pendiente 92](../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md)
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** —
- **Con qué se retoma:** ¿La lista de invisibles de `marcas.py` se amplía a todo el rango de control, o solo a los que aparecieron?

### H-6 · Tres rojos más, y los cinco que quedan son decisiones, no trabajo

- **Qué pasó:** Se midieron los ocho rojos sin fase posterior. Tres eran trabajo y se hicieron: un ajuste de proyecto que declara aflojar una `[BLINDADA]` pasaba sin reclamo (`EP-001·HU-006`); la prueba del número de versión exigía una unicidad que el registro decidió no cumplir (`EP-002·HU-001`); y la simulación del instalador no anunciaba el registro de versión (`EP-007·HU-002`). Los otros cinco no son trabajo: son decisiones del usuario, y cuatro de ellas ya estaban escritas como tales en el propio repositorio.
- **Por qué importa:** «Ocho historias en rojo» se lee como ocho tareas. Medirlas una por una mostró que son dos cosas distintas, y confundirlas lleva a lo peor de los dos lados: o el agente decide por su cuenta lo que no le toca, o el trabajo hecho se queda sin declarar. La prueba de `EP-006·HU-006` lo dice textual: *«elegir entre ellas no es del que ejecuta»*.
- **Qué lo soluciona:** Las tres primeras, hechas. Las cinco restantes esperan respuesta, cada una con su pregunta escrita.
- **Qué se decidió:** En `EP-002·HU-001`, que la prueba exija lo que el registro sostiene —que un número repetido esté declarado— en vez de una unicidad que se decidió no cumplir. El `CHANGELOG.md` no se tocó.
- **Estado:** abierto, por los cinco que faltan
- **Responde a:** EP-001 · HU-006 · EP-002 · HU-001 · EP-007 · HU-002
- **Dispara:** —
- **Orden de resolución:** 1 de 4 · las cinco decisiones bloquean todo lo demás de esta cuenta.
- **Dónde queda:** Tres fases nuevas · [`validadores/metareglas.py`](../../../validadores/metareglas.py), [`instalar.py`](../../../validadores/instalar.py) y [`versiones.py`](../../../validadores/versiones.py) · los guiones en [`historico-chat/scripts/2026-08-30/`](../../scripts/2026-08-30/) · el conteo, de 8 rojos a 5
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** —
- **Con qué se retoma:** Las cinco preguntas: la clave en prosa, y las cuatro de EP-006 sobre qué se guarda y dónde.

### H-7 · El agente escribió fuera del proyecto tres guiones que producían documentos del repositorio

- **Qué pasó:** Los guiones que escribieron los documentos de dos fases se crearon en el bloc temporal de la herramienta, fuera del repositorio, porque el heredoc de la terminal se rompía con las comillas. Lo notó el usuario.
- **Por qué importa:** La regla existe y es [`04·S18`](../../../base/04-seguridad.md#s18--el-guion-de-apoyo-se-escribe-dentro-del-repositorio-y-se-queda), que salió del pendiente 89 justamente por esto. **Y el enganche que avisa también existe, está colgado y disparó las tres veces**: comprobado corriéndolo, `hook_rutas.py` imprime el aviso y nombra el destino correcto. Avisa con código 0, y el agente siguió de largo. Eso es lo que hay que anotar: no faltaba el control, el control habló y no cambió nada. Además deja sin evidencia lo que el documento afirma: los guiones son de dónde salen las cifras de esas fases.
- **Qué lo soluciona:** Ya movidos a [`historico-chat/scripts/2026-08-30/`](../../scripts/2026-08-30/) y borrados del bloc temporal.
- **Qué se decidió:** Que las carpetas de `c:\\tmp` donde se provocan los casos sí se quedan: es lo que manda la decisión 35 del pendiente 59, y las pruebas las crean y las borran solas. Lo que no puede salir del repositorio es el guion que produce un documento del repositorio.
- **Estado:** resuelto acá en lo suyo; **abierto** lo que destapó
- **Responde a:** `EP-005` · `HU-018`, que construyó el enganche
- **Dispara:** la pregunta de si un aviso alcanza para esto, o si escribir un guion fuera del repositorio tiene que detener como detiene un enlace roto
- **Orden de resolución:** —
- **Dónde queda:** [`historico-chat/scripts/2026-08-30/`](../../scripts/2026-08-30/), y el aviso sin efecto queda dicho acá
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** ¿Un aviso con código 0 alcanza para una regla que ya se dejó de cumplir dos veces?

### H-8 · Los trece rojos quedaron en cero, y once de ellos no eran trabajo

- **Qué pasó:** la cuenta de veredictos pasó de **96 cumplen / 13 no cumplen** a **109 / 0**. De los trece, cinco ya no eran ciertos y solo faltaba declararlo, tres eran trabajo de verdad y se hizo, y **cinco eran decisiones del usuario** que llevaban entre ocho y trece días esperando.
- **Por qué importa:** una lista de rojos se lee como una lista de tareas, y de trece solo tres lo eran. Los otros diez se cerraron midiendo o preguntando, no construyendo. El costo de no haber preguntado antes se mide en días: `EP-006·HU-001` estuvo trece esperando una decisión de dos frases.
- **Qué lo soluciona:** ya está hecho. Las cinco decisiones quedaron aplicadas y cada una con su motivo escrito en el cierre de su fase.
- **Qué se decidió:** las señales viven en la base de Cimiento, que es la línea base de todos los proyectos, y por eso no se versiona en este repositorio · manda el recuerdo sobre la señal cuando se contradicen · se escribe la regla `04·S19`, que prohíbe guardar un dato personal o un secreto en la memoria · la clave dicha dentro de una frase no se tapa, y queda declarado · el programa que vacía el almacén local se lleva todo.
- **Estado:** resuelto acá
- **Responde a:** las trece historias con veredicto en rojo
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** nueve fases nuevas · la regla [`04·S19`](../../../base/04-seguridad.md) · versión `36.0.0` · los guiones en [`historico-chat/scripts/2026-08-30/`](../../scripts/2026-08-30/)
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-9 · Dos criterios se cerraron declarando lo que **no** cubren

- **Qué pasó:** `EP-001·HU-003` cierra con tres de seis formas de clave sin tapar, y `EP-006·HU-006` cierra metiendo al repositorio archivos que no son recuerdos. Las dos son lo decidido, y las dos lo dicen en su cierre.
- **Por qué importa:** es la diferencia entre releer un criterio y borrarlo. Un criterio que se da por cumplido escondiendo lo que no cubre deja al que lo lea después creyendo que ese frente está cubierto, y es la mentira optimista que esta cuenta existe para impedir.
- **Qué lo soluciona:** que el límite vaya escrito en el cierre, con su motivo y con qué lo defiende en su lugar. En `HU-003` la defensa de la clave dentro de una frase no es el programa: es [`00·N6`](../../../base/00-nucleo-blindado.md), que prohíbe escribirla.
- **Qué se decidió:** el límite se escribe, no se calla.
- **Estado:** resuelto acá
- **Responde a:** EP-001 · HU-003 · EP-006 · HU-006
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el §4.1 del resultado de las dos fases `B`
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-10 · Las cinco historias que «no decían si cumplían» lo decían

- **Qué pasó:** quedaban cinco historias contadas en la tercera cuenta, la de las que no dicen si cumplen. Al abrirlas una por una, **las cinco declaran su veredicto en la primera línea de su sección final**. El que no sabía leerlas era el programa: dos formas que no reconocía, `**Concepto: Cumple.**` con los dos puntos dentro de la negrita, y el título `## 6. Concepto final`. La cuenta quedó en **114 cumplen, 0 no cumplen, 0 sin veredicto**.
- **Por qué importa:** es la **cuarta** fase del mismo lector, y el patrón se repite en las tres anteriores: cada una contó las formas que ya sabía reconocer y llamó «otra cosa» a todo lo demás **sin abrirlo**. La fase `B` dijo «39 sin encabezado» y eran 2. Estas cinco se resolvieron leyéndolas, que es lo que ninguna había hecho con las que le quedaban.
- **Qué lo soluciona:** ya está hecho, en la fase `D` de `EP-004·HU-021`. Ninguno de los cinco resultados se tocó: son fases cerradas, así que se corrige quien lee y no lo leído ([`20·M11`](../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).
- **Qué se decidió:** ampliar **qué título vale**, nunca dónde se busca. La prueba que sostiene el cambio es la que impide leer de más: una tabla de criterios en «Cumple» con el veredicto de la fase en «No cumple» tiene que seguir dando «No cumple».
- **Estado:** resuelto acá
- **Responde a:** EP-004 · HU-021
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la fase `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse` · [`validadores/fases.py`](../../../validadores/fases.py)
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-11 · Lo que queda por hacer no es trabajo del agente: son aprobaciones y archivos de otras sesiones

- **Qué pasó:** al medir las 9 historias sin terminar y las 7 pruebas en rojo, casi nada resultó ser trabajo pendiente. De las 9: **cinco son fases abiertas esperando la aprobación del usuario** (cuatro en la estación 4 con su plan escrito, una en la 7) y cuatro son historias de producto sin ninguna fase. De las 7 pruebas: una era un defecto de la propia prueba y se arregló, **cinco son de archivos que otra sesión tiene en curso**, y la última pide tocar 27 archivos que tienen otras dos sesiones.
- **Por qué importa:** «nueve sin terminar y siete en rojo» se lee como dieciséis tareas, y solo una lo era. El resto está detenido por dos cosas que el agente no puede mover: una firma y una sesión ajena. Confundirlas hace que el número parezca deuda técnica cuando es cola de aprobación.
- **Qué lo soluciona:** las cinco fases, con la puerta 4. Lo de los enlaces, con que las otras sesiones cierren o con una decisión de tocarlos igual.
- **Qué se decidió:** no arreglar los 32 archivos libres de los 59: bajaría de 98 enlaces a 49 y **la prueba seguiría roja**, con un cambio a medias en `base/` que obligaría a versionar sin cerrar nada.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** 1 de 1 · es lo único que queda de esta cuenta.
- **Dónde queda:** las cinco fases detenidas, en sus historias · la prueba `test_cero_entre_carpetas_fuera_de_prompts`
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** —
- **Con qué se retoma:** ¿Se aprueban las cinco fases detenidas, y se tocan los 27 archivos ajenos o se espera?

### H-12 · Cuatro fases llevaban trece días detenidas esperando una firma

- **Qué pasó:** cuatro de las cinco fases detenidas en la estación 4 se ejecutaron el mismo día en que el usuario las aprobó. Las cuatro arreglaban un defecto que su propia fase anterior había dejado **probado y marcado como fallo esperado**. La cuenta pasó de 115 a **118 historias que cumplen**.
- **Por qué importa:** el trabajo no estaba pendiente: estaba escrito, planeado y probado, esperando una firma. Trece días. El más grave de los cuatro dejaba la memoria inservible cuando faltaba un modelo opcional, y se llevaba por delante la búsqueda por palabra, que no necesita nada.
- **Qué lo soluciona:** ya está hecho. Lo que queda por decidir es si una fase que espera aprobación debería avisar sola cuando lleva días parada.
- **Qué se decidió:** ejecutarlas en el orden en que se pidieron, y corregir en la misma fase lo que cada una destapó: el capítulo 16 fuera del molde, y una prueba que pasaba o fallaba según el mes en que se corriera.
- **Estado:** resuelto acá
- **Responde a:** EP-004 · HU-002 · EP-006 · HU-003, HU-004 y HU-007
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** cuatro fases `B` cerradas · las 59 pruebas de la memoria sin un solo fallo esperado, donde había cinco
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-13 · El fallo esperado sirvió: al arreglar, la corrida obligó a volver

- **Qué pasó:** las cuatro fases anteriores no podían arreglar su defecto, porque su plan aprobado declaraba no tocar el programa. En vez de anotarlo en prosa, lo dejaron **probado y marcado como fallo esperado**. Al arreglarlo hoy, la corrida reportó «éxitos inesperados» y obligó a volver a destapar cada prueba, una por una.
- **Por qué importa:** un defecto anotado en un documento se pierde; uno anotado como fallo esperado **reclama solo el día que deja de ser cierto**. Es la única forma de dejar constancia que se defiende sola, y funcionó cinco veces hoy.
- **Qué lo soluciona:** nada: es lo que hay que copiar.
- **Qué se decidió:** cuando `02·F8` impida arreglar lo que una fase encuentra, se deja la prueba escrita y marcada, no una nota.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el §4.1 del resultado de las tres fases de memoria
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

### H-14 · Provocar el caso encontró lo que trece días de lectura no vieron

- **Qué pasó:** la última fase detenida tenía cinco criterios sin ejecutar. Dos se verificaron contra proyectos reales; los otros tres **no se pueden ver en ninguno** —uno tiene las migraciones en un formato que el programa no lee, el otro no declara sus entidades— y hubo que provocarlos en un proyecto de prueba. Al hacerlo apareció un defecto de meses: el reclamo de que una entidad inmutable no tiene su permiso **salía en todo proyecto**, porque desde Python 3.7 `re.escape` no escapa los ángulos y el marcador `<recurso>` nunca se reemplazaba.
- **Por qué importa:** se rompió **sin que nadie tocara el código**: cambió lo que hacía una función de la biblioteca estándar por debajo. Y el daño no es el falso positivo sino lo que enseña: un reclamo que sale siempre deja de leerse, y con él los que sí eran ciertos.
- **Qué lo soluciona:** ya está hecho, con su prueba de no regresión y su contraprueba.
- **Qué se decidió:** cada criterio provocado lleva su contraprueba, porque un validador que reclamara siempre pasaría igual. Y las declaraciones del proyecto de prueba se escribieron dos veces mal antes de acertar: un caso mal armado se lee idéntico a un programa roto, y lo que los separa es mirar qué espera el programa antes de acusarlo.
- **Estado:** resuelto acá
- **Responde a:** EP-004 · HU-010
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [`S-086`](../../../documentacion/senales.md) y [`S-087`](../../../documentacion/senales.md) · el guion que provoca los cuatro casos, en [`historico-chat/scripts/2026-08-30/`](../../scripts/2026-08-30/)
- **Nace en:** 2026-08-28 · plantilla-manual-instalacion
- **Cerrado en:** 2026-08-28 · plantilla-manual-instalacion
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ [91](../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md), [92](../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md), [93](../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md) |
| Toda historia disparada está escrita en su épica | ☐ Las tres salen de su pendiente **cuando el usuario las apruebe**, que es la puerta 4 |
| Lo que se hizo está aprobado y guardado | ☐ Falta guardar los tres pendientes y este resumen |

**Lo que impide cerrar, en una línea:** las cinco decisiones del usuario sobre los rojos que quedan, y la aprobación de las tres historias que estos pendientes disparan.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
