# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo — salvo que en el desfase haya una derogación sin adoptar, que sí detiene la fase ([`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)).

---

## 37.2.2 — 2026-09-02

**Un documento que ya estaba escrito se contaba como si no existiera.** La revisión del expediente buscaba cada entregable por el nombre de su archivo, y a uno de ellos el estándar le da dos nombres distintos: lo llama «documentación de API» en un lado y «contrato de la interfaz» en el otro.

Quien lo escribiera con el segundo nombre —el que el propio estándar usa en su tabla de moldes— lo veía reportado como faltante, y podía terminar escribiéndolo dos veces.

**PARCHE** (corrección): un proyecto al día no tiene que hacer nada. Lo que cambia es que un documento que ya existía deja de contarse como ausente.

**Lo que pasó es lo de siempre en este repositorio:** una convención tiene dos nombres y el lector conocía uno. El nombre no se cambió en ningún proyecto; el que se adaptó fue el que busca.

- `validadores/expediente.py` — el molde 16 acepta también `contrato-de-la-interfaz.md`.

## 37.2.1 — 2026-09-01

**El aviso de «qué cambió desde entonces» salía vacío, y llevaba así cincuenta y cuatro versiones.** Un proyecto que quedó atrás recibe el aviso de desfase; lo único que le sirve para decidir si sube hoy es qué pasó en el camino, y esa parte no salía.

**PARCHE** (corrección): un proyecto al día no tiene que hacer nada. Lo que cambia es que el aviso vuelve a contar lo que tenía que contar.

**Lo que pasó fue que la convención cambió y el lector se quedó atrás.** El registro se escribía con el tipo delante y el título después; cuando `M17` pidió que la entrada abriera contando qué pasó, el orden se invirtió. El lector solo entendía el orden viejo.

**Medido:** reconocía **143 de 197** entradas, y la más reciente que entendía era la **34.2.0**. Todo lo posterior era invisible, así que un proyecto en la 35 preguntando qué cambió recibía **nada**, sin que nadie dijera por qué. Ahora reconoce 162, y la más reciente es la del día.

**Y no se tocó ninguna entrada del registro.** Las dos formas valen y el lector lee las dos: reescribir cincuenta y cuatro entradas para que un programa las entienda es al revés.

## 37.2.0 — 2026-08-31

**Dos modelos de documento entran, y los dos marcan sus huecos como los marca la casa.** Uno es nuevo —el documento de arquitectura de un sistema— y el otro es el manual de usuario, reescrito entero con otra estructura: pasó de dieciséis secciones a veintiséis.

**MENOR** (aditivo): un proyecto al día no tiene que hacer nada. Lo que copie de ahora en adelante viene con la marca correcta.

**Los dos llegaron marcando sus huecos con una notación propia**, y así no podían entrar. Son 936 huecos entre los dos: cada proyecto que copiara uno de esos modelos habría marcado los suyos de una forma que su propia comprobación le reporta. Ahora usan la de todos los modelos.

**Y los dos le hablaban al lector de tú a tú** —«reemplace», «elimine», «no invente»—, que es justo lo que la norma de redacción descarta. Dieciséis líneas pasaron a decir lo mismo sin señalar a nadie.

**La norma de redacción se cita, no se copia.** Es lo que hizo falta aprender: cuando estaba escrita **dentro** de un modelo, solo la heredaba quien llenara ese modelo, y al reemplazar el manual de usuario se perdió entera. Ahora los dos apuntan a la regla, y la regla vive en un solo sitio.

**Qué no cambió:** el contenido de los dos modelos. Lo que se tocó es cómo se marcan los huecos, cómo se le habla a quien los llena, y la cita de la norma.

Detrás: [`13·DOC19`](base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) y [`00·ID10`](base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md). Los modelos son `plantillas/documento-arquitectura.md` y `plantillas/manual-usuario.md`.

---

## 37.1.0 — 2026-08-31

**Una norma escrita informa; un programa la hace cumplir, y hasta hoy las dos se leían igual.** Quien abría una norma de las que no se relajan veía una exigencia, sin manera de saber si detrás había algo que la ejecutara o no había nada. Se contó: de las dieciocho que rigen, **catorce dependían de que el agente se acordara**, y siete ni siquiera se nombraban en un programa.

**MENOR** (aditivo): las normas de los proyectos no cambian, y un proyecto al día no tiene que hacer nada.

**Ahora cada una lo dice, en su propio texto.** Cinco nombran la pieza que las ejecuta; trece declaran que no la tienen, **con el motivo escrito**. Las dos respuestas valen: la mayoría del núcleo se sostiene en la aprobación del usuario, que ningún programa ve. La que no vale es callarse.

**Y no vale decir «nadie» sin decir por qué.** Una casilla marcada no es una decisión, y ese era el camino corto para dar la exigencia por cumplida sin cumplirla.

**Las tres normas sobre cómo escribe el agente ya tienen quien las mida.** Al cerrar cada turno se cuenta, sobre lo que acaba de escribir, el trato directo, las marcas mecánicas y cuánto ocupa; si hay algo que decir, se dice, y si no, se calla. **Mide y no detiene**, y es a propósito: cuando eso corre, el texto ya salió, y devolverlo le costaría al usuario leer la versión larga primero y la corta después.

**El molde de la norma tiene su sitio nuevo**, después del ejemplo, y antes de publicar se comprueba que ninguna se quede sin responder.

**Lo que esto no dice, y queda escrito para que no se lea de más:** que la pieza declarada de verdad ejecute la exigencia. Se comprueba que exista y que la respuesta esté; lo otro lo lee una persona.

Detrás: [`00·ID8`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), [`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) e [`00·ID10`](base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md) con su pieza; `validadores/ejecutable.py`, `validadores/redaccion.py` y el enganche de cierre de turno; la sección 6 de [`estructura-regla.md`](base/20-meta-reglas/estructura-regla.md). Sale de la fase `A-EP-005-HU-012`.

---

## 37.0.0 — 2026-08-30

**Cómo escribe el agente ya no depende de qué documento esté llenando.** Hasta hoy la exigencia de escribir en la lengua del proyecto, en tercera persona y con las acciones en infinitivo vivía dentro de dos documentos modelo, como una de sus reglas internas. Quien escribiera cualquier otra cosa no tenía de dónde heredarla, y la convención se aplicaba copiándola a mano, que es la forma más segura de que se copie distinta.

**MAYOR** ⚠ obliga a migrar: rige para todo lo que el agente entrega, y un proyecto al día tiene que escribir así de aquí en adelante.

**La regla es** [`00·ID10`](base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md).

**Qué alcance tiene, y lo decidió el usuario.** Todo documento que el agente entrega **y también lo que contesta en el chat**. No es un detalle: la respuesta del chat es lo que más se lee y lo único que no queda versionado, así que es donde la convención se pierde primero.

**No fija un idioma, y eso es lo que la hace heredable.** Dice «el que usa el proyecto», que ya era exigible; lo que agrega es cuál variedad de ese idioma, la persona y la forma verbal. Un proyecto que trabaje en otro idioma la cumple igual.

**El impersonal con «se» se nombra aparte**, porque es la forma en que la regla se incumple sin darse cuenta: «se copia el archivo» suena correcto y no dice quién lo hace, así que el lector no sabe si le toca a él.

**Qué se puede comprobar con un programa y qué no.** La persona y la forma verbal se cuentan sobre un texto; la variedad del idioma pide leer, y es justamente la mitad que hizo falta el día que esto salió a la luz.

**El modelo de manual de instalación ya la cita** en vez de repetirla. El de manual de usuario queda pendiente: tiene cambios sin guardar de otra sesión y tocarlo sería llevarse trabajo ajeno.

---

## 36.0.3 — 2026-08-30

**Había caracteres invisibles metidos dentro de veintiséis documentos, y donde caían rompían la tabla sin que nadie lo viera.** Uno de ellos, al principio de una fila, hacía que esa fila dejara de ser fila: desaparecía del cuadro y quedaba como un párrafo suelto debajo. En un documento del proyecto, eso hacía que una línea entera de una tabla no se viera.

**PARCHE**: quita lo que no se ve y no significa nada; ninguna palabra del texto cambia.

**Qué se hizo.** El programa que cuenta lo invisible ahora barre el rango completo de caracteres de control, no los que fueron apareciendo: agregarlos de a uno deja el trabajo a medias por definición, porque el próximo se cuela igual. Quedan fuera los tres que sí significan algo al escribir, que son el salto de línea, el retorno y el tabulador.

**Y la lista escrita dice lo mismo que el programa.** El anexo que enumera estas marcas recibió su fila, para que no vuelvan a separarse.

**Se limpiaron catorce archivos.** Los que quedan están en la carpeta de datos de la plataforma, que es una copia traída, y en el histórico, que no se reescribe.

---

## 36.0.2 — 2026-08-30

**Cuatro reglas del capítulo de cumplimiento llevaban meses publicadas sin que nadie las hubiera revisado.** No por descuido: el programa que revisa las reglas no las reconocía como reglas, porque estaban escritas un nivel más abajo que las demás. El capítulo salía en verde por el mismo motivo por el que pasaría un examen que no se corrige.

**PARCHE**: cambia la forma de las cuatro y les agrega lo que les faltaba; no cambia lo que exigen.

**Qué se hizo con ellas.** Suben al nivel que el molde pide, las dos partes del capítulo dejan de ser encabezado para no chocar con ellas, la tercera recibe el ejemplo de lo incorrecto y lo correcto que nunca tuvo, y las cuatro reciben su bloque de checklist aplicado.

**Y el programa aprendió a distinguir la regla de su eco.** Un título con forma de regla escrito un nivel abajo es una de dos cosas: la regla, o una sección que la nombra. Lo que las separa es que el identificador es único, así que el que ya se definió arriba es un eco. Sin esa distinción, el analizador contaba una regla dos veces y reclamaba un identificador repetido que no existía.

**Una comprobación pasó de avisar a detener:** que toda regla diga si se puede comprobar con un programa. Era aviso mientras el analizador no las veía a todas, porque reclamar por algo que el propio programa no podía mirar entero es ruido que se aprende a ignorar. Las derogadas siguen exentas.

---

## 36.0.1 — 2026-08-30

**El texto de un enlace ahora dice dónde vive lo que abre.** Noventa y ocho enlaces del repositorio mostraban un texto que no correspondía con el archivo al que llevaban: quien los leía no podía saber si el documento estaba al lado o en otra carpeta, y tenía que abrirlo para averiguarlo.

**PARCHE**: cambia el texto que se ve, no lo que se exige ni a dónde llevan los enlaces.

**Qué se tocó.** Cincuenta y nueve archivos, dos de ellos del cuerpo de reglas. La corrección la hizo el propio programa que la comprueba, y después la comprobación quedó en cero.

**Por qué estuvo tanto tiempo así.** La prueba que lo mide existía y estaba en rojo desde hacía días, en una suite que hasta el 28 de agosto no corría nadie.

---

## 36.0.0 — 2026-08-30

**Lo que el agente recuerda de una sesión a otra ya no puede llevar el nombre de una persona ni una contraseña.** Hasta hoy nada lo prohibía: se podía anotar el caso entero, con quién era y con qué clave, y eso quedaba guardado para leerse otra vez cada mañana. Ahora lo que se guarda es qué se aprendió, sin el caso.

**MAYOR** ⚠ obliga a migrar: un proyecto al día tiene que revisar su memoria y sacar lo que no debería estar.

**La regla es** [`04·S19`](base/04-seguridad.md#s19--en-la-memoria-no-se-guarda-un-dato-personal-ni-un-secreto).

**De dónde sale.** Una historia llevaba trece días en rojo por esto. El criterio transversal de privacidad de `EP-006·HU-001` pedía que la memoria no guardara datos personales ni claves, y al buscar la regla que lo dijera **no había ninguna**: `13·DOC5` dice qué se registra como señal, y no dice qué no.

**Qué exige.** Que lo escrito en la memoria diga **qué se aprendió** y nunca el dato con el que se aprendió. El ejemplo de la regla contrapone las dos formas de anotar el mismo hallazgo: el caso con la persona y su clave, contra el aprendizaje sin el caso.

**Por qué en seguridad y no en documentación.** No es una convención de cómo se escribe: es qué dato puede salir de una sesión y quedar guardado. `00·N6` ya prohíbe escribir una credencial en cualquier parte y esta no la toca: agrega el **dato personal**, que el núcleo no cubre.

**Y por qué el sitio importa.** Un dato en un registro se lee una vez y envejece. Un dato en la memoria se carga al abrir cada sesión: no envejece, se vuelve a decir.

**Qué se puede comprobar y qué no**, dicho en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): la clave la caza `enmascarar.py`, que hoy corre sobre la transcripción y no sobre la memoria, así que falta apuntarlo ahí. El dato personal no se detecta sin decidir qué nombre propio es de una persona y cuál de un módulo, y eso es leer.

---

## 35.10.0 — 2026-08-29

**El molde del manual de instalación se rehízo entero.** El anterior daba por hecho un servidor y dos piezas. El nuevo pregunta por cada ambiente, por cómo se entra a cada uno, y por cómo se vuelve atrás cuando la instalación falla.

**MENOR** (nadie tiene que cambiar nada: quien ya tenga un manual escrito lo conserva).

**Qué cambió.** [plantillas/manual-instalacion.md](plantillas/manual-instalacion.md) pasó de 14 secciones a 25, y de 407 líneas a 777. Lo que no tenía: la tabla de ambientes (desarrollo, pruebas, QA, producción) con un bloque de datos por cada uno; las herramientas de acceso, que ahora son un bloque reemplazable para que cambiar de herramienta no obligue a reescribir el manual; el procedimiento de reversión, que antes solo existía como paso suelto dentro de la actualización; y la tabla de solución de problemas con las columnas de diagnóstico y verificación.

**Los comandos ahora dicen dónde se ejecutan, con etiqueta.** `[LOCAL]`, `[SERVIDOR]`, `[CONTENEDOR]`, `[BASE DE DATOS]` y `[HERRAMIENTA]`, definidas en su propia sección, y ningún comando aparece sin la suya. El molde anterior lo pedía en prosa («en su computador» o «dentro del servidor»), y en un manual con contenedores esa frase no alcanza.

**Cada paso tiene cuatro partes con nombre:** precondición, acción, resultado esperado y validación. Antes eran cuatro también, descritas en la regla 1 pero sin rótulo, así que en el manual escrito quedaban mezcladas con la prosa del paso.

**Y los bloques que se repiten están marcados como tales.** Ambientes, herramientas, dependencias, componentes y servicios llevan un aviso de «bloque repetible»: se copia uno por cada cosa que el proyecto tenga y se borran los que sobren, sin que la numeración de las demás secciones se mueva. Un proyecto con tres componentes y otro con uno usan el mismo molde.

**Lo que se conservó del molde anterior**, porque es lo que lo hacía distinto de una lista de comandos: las reglas de redacción de la cabecera (ahora trece), la carpeta `seguimiento/` donde queda la salida de la ejecución real, la exigencia de que lo aprendido en una instalación se vuelva paso y no relato, el control de cambios sin motivos históricos, y la lista de comprobación antes de publicar.

**Por qué es MENOR y no MAYOR.** Ninguna regla de `base/` obliga a que un manual ya escrito siga la plantilla vigente. El que exista se conserva; el próximo sale del molde nuevo.

---

## 35.9.0 — 2026-08-28

**Había 650 pruebas escritas que ningún comando corría.** Ahora se corren con una orden, esa orden dice cuántas corrió, y **cero pruebas es rojo**.

**MENOR** (aditivo: un subcomando y un corredor; nadie tiene que cambiar nada).

**Cómo apareció.** Buscando qué prueba debía haber cazado que una lista se quedara vieja seis días. **La prueba existía, escrita diez días antes, y nunca había corrido.** No era una: `validadores/tests/` tiene 67 archivos y 650 pruebas, y ninguno de los cuatro comandos que podrían ejecutarlas lo hacía. La orden documentada desde la primera prueba del repositorio **se caía antes de correr nada**, por un archivo vacío que faltaba, y su error se leía como ruido.

**Lo que aparece al correrlas: 61 archivos en verde y 6 en rojo.** Uno cuenta 98 enlaces entre carpetas mal escritos donde su criterio exige cero; otro dice que un enganche se quedó del lado equivocado de la frontera del adaptador. Varias son de trabajo de estos días.

**Por qué no bastó con crear el archivo que faltaba.** Con él, la orden carga. Pero `unittest discover` sobre una carpeta vacía **termina en cero**, y eso es el defecto que estábamos arreglando, no su arreglo: un silencio que se lee como éxito. Se creó igual —que la documentación mienta es la otra mitad del problema— y encima va un corredor que **cuenta lo que corrió**.

**Y no se cuelga de cada commit, porque se midió.** Las 650 tardan **9,6 minutos**, y este repositorio hace **16 commits por día**: correrlas ahí costaría **39 horas cada dos semanas**. Un peaje así se apaga en una tarde, y entonces quedamos peor que antes, con un control que figura como puesto. **Así que el enganche reclama en vez de correr:** al publicar, mira una fecha y dice si hay commits que esas pruebas no vieron. Cuesta lo que cuesta leer un archivo.

**Se puede pedir un subconjunto**, que es lo que hace cumplible `02·F5` sobre esta carpeta: una fase corre las pruebas que toca, no las 650. **Y las dos suites siguen separadas a propósito**: juntarlas daría 1165 pruebas y 13 minutos en cada fase, que es justo lo que esa regla evita.

**Lo que ya se cerró de los seis rojos:** uno. El mapa del amarre decía «26 amarradas» y su prueba busca la frase exacta «26 amarrados». Los otros cinco quedan **declarados con su nombre y lo que dice cada uno**, para que ninguno se arrastre sin decisión escrita.

---

## 35.8.0 — 2026-08-28

**El registro de lo que toca cada conversación dejó de depender de cómo se escribió el archivo.** Antes solo anotaba lo que el agente escribía con sus herramientas de edición; ahora anota **lo que cambió durante el turno**, sin mirar quién lo escribió.

**MENOR** (nadie tiene que cambiar nada; el registro no se guarda en el control de versiones y caduca solo).

**El daño que lo hizo falta.** Un guardado se llevó **712 líneas de trabajo de otra conversación**, barridas al agregar todo de una vez. La comprobación que existe para eso **corrió y dijo que estaba bien**: pregunta si lo que entra lo tocaron **dos conversaciones registradas**, y a esos archivos no los había registrado ninguna. **Un archivo sin registro no parece de otro: parece de nadie.**

**Por qué no se arregló la comprobación.** Se probó la idea obvia —avisar de lo que no tiene registro— y se midió contra los doce guardados anteriores: **habría hablado en siete, con hasta 31 archivos de una vez**. La causa es que la mayoría de los archivos se escriben desde programas que se corren en la terminal, y esos no dejaban rastro. **«Sin registro» no significaba «de otro»: significaba «escrito como se escribe casi todo».**

**Lo que se agrega:** al terminar cada turno, la conversación anota los archivos que cambiaron **dentro de ese turno**. Si otra estaba escribiendo al mismo tiempo, **las dos lo anotan**, y la comprobación que ya existía ve el choque. **No hizo falta comprobación nueva: hizo falta que su registro dejara de tener el hueco.**

**Dos cosas dichas de frente.** La primera vuelta **no reclama nada**: sin una hora anterior contra la cual comparar, cualquier criterio se llevaría todo lo que estuviera a medias, y la primera conversación del día se atribuiría el proyecto entero. Y **anotar de más es deliberado**: que dos conversaciones toquen el mismo archivo es justo lo que hay que ver.

**Nunca estorba.** Si algo le falla, el turno termina igual: cuando esto corre, la respuesta ya se dio.

---

## 35.7.1 — 2026-08-28

**Se recortó el texto de la regla nueva sobre dónde van los programas de apoyo.** Medía más de lo que el molde admite.

**PARCHE** (no cambia qué se exige: la regla pide lo mismo, dicho más corto).

**Y su lista de comprobación decía que cumplía, sin haberla corrido.** Veinte casillas marcadas, y una era falsa — justo la del tamaño. Se firmó en el mismo minuto en que se escribió la regla, por la misma mano, sin ejecutar el programa que lo mide.

**Lo que sobraba no era largo: era el porqué.** El texto mezclaba **la orden** —dónde va el programa— con **la explicación** —que sin eso queda el resultado y se pierde el cómo—. La explicación se movió a la nota de abajo, que es donde la ponen las demás reglas.

---

## 35.7.0 — 2026-08-28

**Dos moldes nuevos: el manual de usuario y el manual de instalación.** Hasta hoy cada proyecto escribía los suyos desde cero, y los dos que existían salieron llenos de nombres del proyecto que los escribió.

**MENOR** (nadie tiene que cambiar nada; quien ya tenga manuales los conserva).

**Qué son.** [plantillas/manual-usuario.md](plantillas/manual-usuario.md) y [plantillas/manual-instalacion.md](plantillas/manual-instalacion.md). Son **modelos**: se copian al proyecto, se reemplaza cada «…» y se llena cada sección siguiendo su recuadro 📋, que dice *qué va · cómo se escribe · de dónde sale el dato*. Los recuadros se borran al llenar; el lector final nunca los ve.

**Lo que los distingue.** Abren con diez reglas de redacción para que **no asuman nada del lector** —una acción por paso, decir qué se ve antes y después, qué hacer si no pasa, ninguna palabra técnica sin explicar, nada de «simplemente»— y cierran con la lista de comprobación antes de publicar, que exige haberlos ejecutado en el sistema real siguiendo solo el texto.

**No nombran ningún programa.** Las piezas se llaman por su función («la puerta de entrada», «la parte de datos», «la base de datos») y lo propio de cada sistema va en marcas «…». La primera versión, escrita en un proyecto, nombraba sus pantallas, sus programas y sus historias; el usuario la devolvió: una base con nombres propios no se puede copiar. De ahí salió la regla de la casa: **antes de entregar un molde, buscar nombres de proyecto, programas, herramientas, puertos y códigos — cero coincidencias.**

**Y no cuentan lo que pasó: lo convierten en pasos.** El primer manual escrito con el molde salió relatando la instalación de pruebas (fechas, duraciones, «en este servidor salió...», «no hizo falta...») y con marcas «(por verificar)» donde algo no se había ejecutado. El usuario lo devolvió: un manual no asume nada, ni siquiera que al lector le va a pasar lo mismo. La regla 7 de los dos moldes quedó así: lo aprendido en una ejecución anterior se vuelve un paso más, una bifurcación dentro del paso o una fila de solución de problemas; nada se marca «(por verificar)». La tabla de instalaciones hechas salió del molde (es operación, vive en el seguimiento) y el control de cambios perdió la columna de motivos históricos.

> **De qué commit salió esta entrada, dicho porque el registro atribuía mal.** Los dos moldes y este texto se escribieron en una sesión y quedaron sin guardar. **Los guardó el commit `6abffdc` de otra sesión**, que trataba de algo distinto —el hash del commit— y los barrió con un `git add -A` sin nombrarlos en su mensaje. Se descubrió el 2026-08-28 porque el número de versión no cuadraba. **Nada se perdió**; lo que fallaba era la autoría. Está en `S-071`.

**Y en tercera persona.** Ni «usted» ni imperativos: impersonal («se abre», «se escribe») o con sujeto («quien instala», «el ciudadano»). Es la regla 11 de los dos moldes; el usuario la pidió al revisar el primer manual escrito de «usted».

**El de instalación cubre los tres momentos:** instalar desde cero, actualizar una instalación que ya existe (con la vuelta atrás escrita antes de necesitarla) y mantener la que funciona. Y deja dicho que un cambio de herramienta de construcción es un cambio de manual: un manual probado deja de estarlo cuando cambia la herramienta con la que se instala.

---
## 35.6.0 — 2026-08-27

**La casilla del commit se marca sola.** Antes había que volver al documento a escribirla, y casi nadie volvía: el commit ocurre **después** de que el trabajo se dio por terminado.

**MENOR** (nadie tiene que cambiar nada; los documentos que no tienen esa casilla no se tocan).

**Por qué nadie la marcaba.** No era descuido: es la forma del ciclo. La última casilla es la única que se cumple **fuera del momento** en que se escribe el documento que la registra. Solo el 2026-08-27 se marcó a mano cinco veces, y cada vez costó un guardado aparte.

**Lo que apareció al medir, y cambió el alcance.** De los 140 documentos de estado del proyecto:

| | |
|---|---|
| Con la casilla marcada | 11 |
| Sin marcar | 23 |
| **Sin la casilla siquiera** | **106** |

**Tres de cada cuatro no tienen dónde marcar.** No se les inventa: **se cuentan aparte y se nombran**, porque un programa que le agregue estructura a un documento viejo hace más daño que el problema que corrige.

**Y las 23 sin marcar eran dos cosas distintas:** **22 están guardadas de hecho** —comprobado contra el historial— y **una no lo está**. Juntarlas decía «23 sin guardar» donde hay una. Ahora se dicen por separado, con nombres.

**El costo, dicho de frente.** El hash **no existe hasta que el guardado está hecho**, así que la anotación llega después: **el documento queda modificado y sin guardar**, y entra en el guardado siguiente. Las otras dos salidas se descartaron con motivo — rehacer el guardado cambia el hash y el documento apuntaría a uno que ya no existe, y guardar por su cuenta sería un cambio sin aprobación.

**Nunca estorba.** Si algo le falla, **el guardado queda hecho igual**: cuando esto corre, ya terminó.

---

## 35.5.0 — 2026-08-27

**Un trabajo marcado como «no cumple» ya se puede dar por resuelto, diciendo cuál se resolvió.** Antes esa marca no tenía forma de quitarse: se podía arreglar el problema, comprobarlo y dejarlo escrito, y el número seguía contando el trabajo como pendiente.

**MENOR** (nadie tiene que cambiar nada de lo que ya tiene; el campo es opcional).

**Cómo se descubrió.** Se hicieron dos trabajos que arreglaban cosas marcadas así, se comprobó ejecutándolas que hoy funcionan, y los dos quedaron en verde. **El número no se movió.** Seguía diciendo 16.

**Por qué pasaba.** La cuenta mira todos los trabajos de una historia, y basta uno marcado en rojo para que la historia entera cuente como no cumplida — lo cual es correcto mientras el problema siga ahí. Lo que faltaba era distinguir **«todavía no se hizo»** de **«se hizo después, y alguien lo verificó»**. Sin esa diferencia, **la cuenta solo sabía subir**.

**Qué se agrega:** un campo opcional en el documento de cierre — **«Reemplaza el veredicto de»** — donde se nombra el trabajo anterior que queda resuelto.

**Se declara, y no se adivina.** Se midió antes de diseñarlo: de las 16 historias con algo en rojo, ocho tenían un trabajo posterior, **y solo dos de esas ocho habían vuelto a verificar el problema**. Las otras seis hicieron algo distinto. Dar por resuelto lo anterior solo porque vino algo después habría dado por buenas seis historias con el problema intacto.

**Tres condiciones, y las tres hacen falta:** quien lo declara tiene que estar en verde —un rojo no cierra otro rojo—, el trabajo nombrado tiene que ser de la misma historia, y no puede nombrarse a sí mismo. **Si el nombre no encaja se avisa, con el nombre escrito, y no se cierra nada.**

**Lo que se declaró ahora, y lo que no:**

| Antes | Ahora |
|---|---|
| `66 cumplen, 16 no cumplen` | `68 cumplen, 14 no cumplen` |

**Se movieron exactamente dos**, que son las dos que habían vuelto a verificar. **Las otras catorce siguen contando**, y eso es lo correcto: nadie ha comprobado que se resolvieran.

**El texto anterior no se toca.** El documento que dijo «no cumple» sigue diciéndolo: la cuenta lo deja atrás, pero el rastro de que hubo un problema es justamente lo que hay que conservar.

---

## 35.4.0 — 2026-08-27

**Escribir un archivo fuera de la carpeta del proyecto ahora avisa en el momento, y dice dónde debía ir.** Antes solo estaba escrito que no se hiciera, y nada lo comprobaba.

**MENOR** (nadie tiene que cambiar nada de lo que ya tiene; lo que cambia es que ahora hay quien lo diga).

**Por qué hizo falta.** La regla existía desde el 2026-08-20 y se precisó el 22. **Se dejó de cumplir el 24**, y siguió cuatro días: 38 programas de apoyo quedaron en una carpeta temporal del sistema en vez de en el repositorio.

**El daño no era de orden.** El **resultado** de cada cambio quedaba guardado y **el cómo se borraba con el temporal**: a la pregunta «¿con qué se hizo esto?» no había respuesta en ninguna parte. Es la segunda vez que esa pregunta se queda sin respuesta — la primera es la que originó la regla.

**Qué se agrega:**

| Pieza | Qué hace |
|---|---|
| La regla `04·S18` | Dice **dónde sí** van los programas de apoyo, que es la mitad que le faltaba a `04·S9` |
| Un enganche | Avisa al escribir fuera, **nombrando el destino**. Avisa: no mueve ni borra |

**Lo que no cubre, dicho para que no se lea de más:** lo que se escribe desde una línea de comandos no se ve, porque la herramienta no entrega esa ruta.

**Por qué un aviso y no un bloqueo.** Quien escribe fuera suele estar a mitad de algo; detenerlo rompe el trabajo y esconde el problema en vez de mostrarlo. Y un aviso que se equivoca una vez por sesión se apaga: por eso la mitad de las comprobaciones nuevas verifican que **no** hable donde no debe.

---

## 35.3.0 — 2026-08-27

**Una fase recién abierta contaba como terminada.** El andamio crea sus cinco documentos vacíos, y el conteo miraba que existieran. Ahora un documento que **sigue siendo su plantilla** no cuenta como escrito.

**MENOR** (nadie tiene que hacer nada; lo que cambia es que el número deja de contar como escrito lo que no lo está).

**Lo que se veía antes y lo que se ve ahora**, sobre este mismo repositorio:

| Antes | Ahora |
|---|---|
| `32 sin terminar · 85 terminadas` | `39 sin terminar · 78 terminadas` |

**No se perdió trabajo: hay siete documentos que nunca se escribieron y hasta hoy contaban como escritos.** El programa los nombra uno por uno, así que se puede ir a arreglarlos sin volver a medir:

| Documento | Qué es |
|---|---|
| `plan_pruebas.md` de `B-EP-002-HU-003`, `B-EP-002-HU-004`, `B-EP-004-HU-011`, `B-EP-004-HU-012` y `B-EP-005-HU-002` | La plantilla `08` sin tocar, con sus 36 marcadores |
| `estado-fase.md` de `A-EP-004-HU-021` y `A-EP-007-HU-009` | La plantilla `10` sin tocar, con 16 |

**Los cinco primeros son fases con su código y sus pruebas construidas.** Lo que falta ahí no es papeleo: **nadie sabe con qué casos se comprobaron.**

**Cómo se distingue un documento escrito de un formulario.** No por **cuántos** marcadores tiene, sino por **cuántos son los de su plantilla**. `«Cumple»` es prosa; `«2-4 líneas en lenguaje claro»` está en el molde y solo ahí. Contar sin cruzar ya se probó y falla: señaló tres documentos escritos, cerrados y publicados el mismo día.

**El corte no se eligió: lo dio el reparto.** De los 664 documentos de fase, 577 no tienen ninguno del molde, 80 tienen uno o dos, y 7 tienen tres o más. **Ninguno tiene entre 3 y 15.**

**Los marcadores se leen de las plantillas de `plantillas/ciclo-vida-proyectos/`**, no de una lista en el código: cambiar una plantilla ajusta la comprobación sola.

---

## 35.2.0 — 2026-08-27

**El número que responde «cuánto falta» contaba como hecho el trabajo que no cumplió.** Ahora distingue lo que se terminó de lo que además cumple, y lo dice en la misma línea.

**MENOR** (nadie tiene que hacer nada; lo que cambia es que el número dice la verdad).

**Lo que se veía antes y lo que se ve ahora**, sobre este mismo repositorio:

| Antes | Ahora |
|---|---|
| `117 en total · 85 completas · 32 incompletas` | `117 en total · 32 sin terminar · 85 terminadas, de las cuales 51 cumplen, 11 no cumplen y 23 no dicen si cumplen` |

**No se perdió trabajo: antes se contaba de más.** De 85 documentos de trabajo terminados, **51 cumplen su exigencia**. Once cerraron declarando que no la cumplen, y 23 no dicen si la cumplen o no.

**Por qué pasaba, y no era descuido de nadie.** El conteo miraba que los documentos estuvieran, y eso dice si el trabajo se **terminó**, no si **cumplió**. Y el molde del documento de cierre ofrecía «Cumple» o «Cumple con observaciones»: **no tenía forma de decir «No cumple»**, así que quien no cumplía tenía que escribirlo suelto, cada uno a su manera, donde ningún programa lo lee.

**Los moldes ahora usan una sola palabra para cada cosa:** `Cumple` o `No cumple`, sin tercer valor, y el documento de cierre tiene su campo.

**Y se corrigió una regla que no describía lo que se hace.** Los moldes decían que un trabajo con una exigencia sin cumplir **no se cierra**. En la práctica se cierra — declarando qué faltó y adónde fue a parar — y eso es lo correcto: **cerrar no es aprobar**. Dejarlo abierto para siempre esconde lo que falta, porque nadie vuelve a leer un documento a medias.

**Lo que no se puede leer se cuenta aparte**, ni entre lo que cumple ni entre lo que no. Repartirlo haría que el número mintiera de otra forma.

**Qué verá quien ya tenía el estándar.** Su número de trabajos completos va a bajar, y con él aparece el reparto. **No hay nada que migrar**: los documentos siguen igual, y lo que cambia es qué se cuenta.

---

## 35.1.0 — 2026-08-26

**En Windows, guardar un archivo cuya ruta pasa de 260 caracteres falla, y el mensaje no dice qué hacer.** Ahora el instalador deja puesto el ajuste que lo permite, y queda escrito qué hacer si aparece de todas formas.

**MENOR** (nadie tiene que hacer nada: quien vuelva a instalar lo recibe, y quien no, sigue como estaba).

**Le pasó a este estándar y detuvo un commit dos veces.** Al guardar 1005 documentos traídos, 59 rutas pasaban del tope y la mayor llegaba a 307 caracteres.

**Acortar nombres no era la salida, y se midió.** La ruta más larga de este repositorio mide 252 en su propio sitio, con 8 caracteres de holgura; anidarla necesita 55. Acortar la convención de carpetas ahorra 14. Ninguna combinación de nombres crea los 55 que faltan.

**Lo que esto no alcanza, y conviene saberlo:** la configuración del control de versiones **no viaja al clonar** — vive dentro de la carpeta oculta del repositorio, que cada clon crea nueva. Quien clone y no instale se va a tropezar igual, y por eso el documento de despliegue explica qué hacer, con el comando.

**El instalador no toca la configuración de la máquina.** Existe una forma que valdría para todo lo que se clone de aquí en adelante, y queda escrita para quien la quiera: es un cambio fuera del proyecto, y esa decisión no la toma el instalador.

**Y si alguien puso el ajuste en «false» a propósito, no se pisa:** se dice que se encontró así y se sigue.

---

## 35.0.0 — 2026-08-26

**Cada documento de trabajo dice en qué estado está — sin empezar, en curso, terminado — y hasta ahora el estándar enseñaba tres palabras distintas para «terminado», según qué molde tuviera abierto quien escribía.** Ahora hay una sola palabra para cada estado, escrita en un único sitio, y un programa comprueba que se use.

**MAYOR** ⚠ obliga a migrar: quien ya tenga documentos escritos cambia la palabra de su campo **Estado** por la del vocabulario nuevo. Es una palabra por documento, y el detalle que venga detrás se conserva.

**«Terminado» se escribía de tres formas, y el estándar era el que las enseñaba.** El molde de la épica decía `Completada`, el de la historia `Done`, el de la tarea `Hecha`. Y la lista de la épica estaba escrita **dos veces sin coincidir**: `01-planteamiento` no traía `Cancelada` y `03-epica` sí. De 115 historias de este repositorio, **111 usaban una palabra que su propio molde no decía** — no por descuido, sino porque quien escribía una historia después de una épica repetía lo que acababa de leer.

**Ahora los estados se definen en el glosario y en ningún otro sitio.** Los cuatro moldes lo citan en vez de llevar su propia lista. La regla es una: mismo concepto, misma palabra. Que una épica, una historia y una tarea tengan **conjuntos** distintos sigue siendo correcto — una épica se cancela y una tarea se bloquea —, pero «terminado» es `Terminada` en las tres.

**Y el vocabulario pasó al español.** Decía `Backlog / Ready / Done`, y [`01·C20`](base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) pide traducir. El glosario es justamente el documento que lleva la lista de lo que se queda en otro idioma y por qué: escribirlos ahí sin razón habría sido incumplir en el archivo donde más se nota.

**Qué tiene que hacer un proyecto que ya tenía el estándar.** Cambiar la palabra del campo **Estado** de sus épicas, historias y planes:

| Decía | Pasa a |
|---|---|
| `Backlog` · `Escrita` | `Pendiente` |
| `Ready` · `Aprobada` (en una historia) | `Lista` |
| `En implementación` · `En QA` | `En curso` · `En prueba` |
| `Done` · `Completada` · `Cumplida` · `Cerrada` · `Hecha` | `Terminada` |

**No corre prisa y nada se detiene:** la comprobación **avisa**, no falla. Pero un aviso que no se atiende se vuelve ruido, y el ruido es como se terminan apagando las comprobaciones.

**«Terminada» y no «Cerrada»**, aunque `Cerrada` se usara: en el estándar `cerrada` ya significa otra cosa — es como se marca una **estación** de fase. Reusarla mezclaría dos vocabularios.

**De dónde salió.** De preguntarse por qué se pudo afirmar cuatro veces que una historia cerrada estaba abierta, sin que nada lo cazara (`S-048`). La respuesta era que ningún programa podía saberlo: hacía falta una lista de sinónimos que envejece.

---

## 34.2.0 — 2026-08-26

**MENOR** (el inventario deja de pedir una cuenta a mano; ningún proyecto queda obligado a nada, y lo que aparece es un aviso).

**El inventario de historias dejaba de cuadrar solo, y ahora no puede.** La plantilla pedía mantener a mano tres números —total, completas, incompletas— y una tabla con una fila por historia y una casilla por documento. Eso se desfasa: en el estándar pasó tres veces, y la última decía 78 historias donde el árbol tenía 113. **Cuatro de sus filas daban por completa una historia que no lo estaba**, que es la dirección que hace daño: esconde trabajo en vez de inventarlo.

**Ahora la plantilla remite al comando que lo calcula**, con su `--raiz` para correrlo desde un proyecto. No hay nada que instalar: los validadores del estándar no se copian, los enganches los llaman en su sitio.

**Y el estandar avisa si la cuenta vuelve a escribirse a mano**, en el primer nivel de `pendientes/` o de `documentacion/`, que es donde el inventario vive. Avisa y no corrige, como todos los programas de comprobación.

**Qué cambia para un proyecto que ya tenía el estándar.** Verá un aviso nuevo si su inventario guarda la cuenta escrita. **Su inventario no se toca ni se migra**: el aviso informa, y quitarle los números es decisión del proyecto. La plantilla nueva rige los inventarios que se armen de aquí en adelante.

**Lo que la plantilla enseñaba y no sale del árbol se conserva:** en qué orden se escriben los cinco documentos de una fase, la diferencia entre construir y retrodocumentar, y por qué una fase nace con su `plan_trabajo.md` adentro. Y gana una sección para lo único que sigue escribiéndose a mano: **por qué cambió la cuenta**, que es lo que impide leer una subida como un retroceso.

---

## 34.1.0 — 2026-08-24

**MENOR** (los moldes aprenden de haberse usado; nadie tiene que hacer nada, y ningún proyecto deja de cumplir por esto).

**Los documentos modelo se llenaron de verdad, y eso mostró qué les faltaba.** Al escribir con ellos la planificación, el análisis y el diseño de un proyecto entero, aparecieron seis huecos que ninguna lectura había detectado. Ahora están cubiertos.

**Lo aprobado se puede mover, y ahora se sabe cuándo se movió.** El documento de planificación gana una sección donde se anota todo cambio posterior a la aprobación: qué cambió, por qué y quién lo pidió. Y dice algo que en la práctica costó caro: si un cambio deja sin efecto un acta o un estudio ya firmados, se declara, porque no siguen valiendo solo por estar escritos.

**Los siete documentos de etapa avisan de qué no hay que partir.** Se escriben desde lo que el sistema debe llegar a ser, no desde lo que ya está construido, y traen la prueba para saberlo: si se borra mentalmente lo hecho y el documento sigue siendo cierto, está bien escrito.

**El documento de datos pregunta ahora qué se calcula y qué se guarda.** Un dato guardado que también se puede calcular es una segunda verdad que envejece. Y pide escribir qué deja fuera a propósito, para que nadie lo agregue después creyendo que se olvidó.

**El de pantallas pregunta qué se ve cuando falta algo**, que es la mitad del diseño y la que se olvida: una pantalla en blanco hace creer que el dato no existe. Y qué pide confirmación antes de hacerse, separando lo que se deshace solo de lo que no.

**El de integración pregunta qué se promete y qué no**, con hasta cuándo. Lo que no se promete por escrito se promete sin querer: quien integra da por seguro todo lo que no esté dicho.

**Y las decisiones de arquitectura recuerdan que la firma es del texto que se leyó.** Si la decisión se edita después de aprobada, la aprobación deja de valer.

---

## 34.0.0 — 2026-08-24

**MAYOR** ⚠ obliga a migrar: cambia cómo se le pide algo al agente. Cada pedido tiene que abrir con una palabra que diga qué se espera.

**El agente decidía por su cuenta qué clase de pedido había recibido, y se equivocaba hacia el lado caro.** Alguien preguntaba «¿le cambio el encabezado?» y en esa misma respuesta el agente ya lo había cambiado. La regla que exige aprobación para tocar algo estaba escrita desde el principio y se cumplía: lo que fallaba era antes, cuando el agente leía una pregunta y entendía un permiso.

**Ahora el pedido dice qué se espera, y el agente no interpreta.** Se abre con una palabra: preguntar, explicar, analizar, revisar, proponer, buscar, comparar, verificar, hacer, corregir, escribir, subir, recordar, registrar, revertir, aprobar, continuar o parar. Las primeras ocho no tocan nada; las siete siguientes cambian el proyecto; las tres últimas mandan sobre el trabajo mismo.

**Sin esa palabra el agente no hace nada**, aunque el pedido parezca evidente. Responde con la lista y espera. Y una palabra parecida no cuenta: «arregle» se parece a «corrija», no está en la lista, y aceptarla devolvería el problema que la lista vino a quitar.

**La palabra dice el máximo, no el mínimo.** Con «revise» se reporta lo que se encuentre y no se corrige, aunque el arreglo sea de un renglón.

**Qué hay que hacer para ponerse al día:** empezar cada pedido con su palabra. La lista completa está en el anexo del capítulo de conducta, y el agente la trae cuando falte.

**El detalle:** la historia [`HU-036`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/HU-036-el-pedido-dice-que-se-espera.md) y su fase. **La regla nace declarada como no comprobable por programa:** ninguno puede leer un pedido y decir si el agente hizo de más, y fingir esa comprobación habría sido peor que no tenerla.

---

## 33.4.0 — 2026-08-24

**MENOR** (los moldes de etapa crecen; nadie tiene que hacer nada, y ningún proyecto deja de cumplir por esto).

**Los documentos de cada etapa ahora preguntan lo que antes nadie preguntaba.** El usuario aportó, para cada una de las siete etapas, la explicación larga de lo que ahí se hace, y de ahí salió lo que a los documentos les faltaba. Al de requisitos se le agregó de dónde salió cada exigencia, con quién se habló y a quién no se consultó, cómo se escribe una exigencia para que se pueda comprobar, y cómo se sigue cada una hasta la prueba que demuestra que se cumplió. Al de diseño, la seguridad, con qué herramientas se va a construir, y la fila que delata la exigencia que no quedó a cargo de ninguna pieza.

**En construcción y pruebas, lo que se olvida hasta que duele.** Cómo se levanta el proyecto en una máquina limpia, qué se exige al revisar el código y quién lo revisa. Y del lado de las pruebas: los cuatro niveles, cómo se derivan los casos de los bordes y de lo inválido, el defecto con su gravedad y su dueño, volver a correr lo que ya servía para que la corrección no lo rompa, y la prueba del usuario con su firma.

**En despliegue y mantenimiento, lo que decide si el sistema sobrevive.** La lista que se marca entera antes de tocar producción, el ensayo de la migración con datos de verdad, la comprobación apenas queda arriba, la capacitación y el acompañamiento de los primeros días, y qué recibe quien lo va a operar. Y en mantenimiento: los cuatro trabajos que se llaman igual y cuestan distinto, la gravedad con su tiempo de respuesta, el análisis de impacto antes de tocar, y qué se mide para poder defender el presupuesto del año siguiente.

**Los catálogos quedan junto a su molde.** Cada etapa tiene ahora dos archivos: el molde que se copia y se llena, y el documento largo que explica la etapa completa con sus técnicas, sus diagramas y sus errores frecuentes. El molde toma de ahí lo que hay que llenar; el catálogo se lee cuando hace falta el porqué.

**Sigue en evaluación.** Vive en `plantillas/cvds/`, y todavía no entra a `plantillas/ciclo-vida-proyectos/` con su número.

---

## 33.3.0 — 2026-08-23

**MENOR** (seis moldes nuevos, en evaluación; nadie tiene que hacer nada, y ningún proyecto deja de cumplir por esto).

**Las siete etapas del ciclo ya tienen con qué escribirse, no solo con qué leerse.** El texto que explicaba cada etapa se leía y se seguía; ahora cada una tiene su molde, con la misma estructura: qué entra a la etapa y si viene aprobado, las secciones propias con su definición, los entregables con su molde y su destinatario, las puertas de qué no se puede hacer hasta qué, y la decisión de cierre.

**Los moldes de etapa no reemplazan a los del expediente: los gobiernan.** Cada entregable enlaza al molde que ya existe en `plantillas/ciclo-vida-proyectos/` en vez de repetirlo, y lo que agrega el molde de etapa es lo que no tenía dónde escribirse: los requisitos no funcionales, las reglas del negocio, el glosario, las dudas abiertas, los límites de cada módulo, la vuelta atrás del despliegue y las rutinas del mantenimiento.

**El molde de planificación se afinó con lo que apareció al llenarlo.** El problema se escribe con diez preguntas y no con un párrafo; los objetivos son diez, en infinitivo, y cada uno dice en qué se nota y para quién; el desglose del trabajo sale de los objetivos y no de lo ya construido, con una columna que lo comprueba; la estimación se hace sobre ese desglose y como si se construyera desde cero. Supuestos, restricciones y dependencias quedaron en tres secciones separadas, y el cronograma se separó del desglose.

**Lo que el ejercicio de llenarlo dejó a la vista.** Escrito para este mismo proyecto, y suponiendo que no hay nada construido, salieron siete requisitos no funcionales que nunca estuvieron escritos, cinco decisiones de arquitectura sin documento, y dos cosas que ninguna comprobación detecta: que nadie ajeno al autor ha instalado el estándar siguiendo solo el manual, y que el mantenimiento entero depende de una sola persona.

**Sigue en evaluación.** Vive en `plantillas/cvds/`, con la copia llenada en `cvds/`, y todavía no entra a `plantillas/ciclo-vida-proyectos/` con su número.

---

## 33.2.1 — 2026-08-22

**PARCHE** (enlaces rotos; no cambia qué se exige).

**Los enlaces del ciclo de vida apuntaban a una carpeta que no existe.** El texto de las siete etapas y el molde de planificación citaban los moldes como `../plantillas/ciclo-vida-proyectos/`, y desde donde viven eso resuelve a `plantillas/cvds/plantillas/`. Eran 44 enlaces: ninguno abría. Ahora los moldes se citan como hermanos y `base/` con el marcador que usan todas las plantillas.

---

## 33.2.0 — 2026-08-22

**MENOR** (un molde nuevo, en evaluación; nadie tiene que hacer nada, y ningún proyecto deja de cumplir por esto).

**La primera etapa del ciclo de vida ya tiene con qué escribirse.** El texto que explicaba la planificación —qué se hace, qué documentos salen, a quién se entregan— se leía y se seguía, pero no se llenaba: había que redactar de cero cada vez. Ahora es un molde de quince secciones con sus espacios marcados: problema, alcance con lo que queda fuera, supuestos y restricciones, viabilidad, recursos, presupuesto, esfuerzo, cronograma, riesgos, roles, interesados, calidad, entregables y la decisión, que puede ser «no se hace».

**La sección del problema se escribe desde la necesidad, no desde lo construido.** Es lo que se rompe al aplicarlo a un proyecto que ya está andando: se describe el producto en vez del problema que lo justificaba. El molde manda reconstruirlo al revés —por cada cosa que hoy existe, qué pasaba cuando no existía— y trae la prueba para saber si salió bien: si se borra mentalmente lo construido y el texto sigue entendiéndose, está bien escrito.

**Los objetivos son diez, en infinitivo, y cada uno dice en qué se nota y para quién.** Los tres primeros salen solos; llegar al décimo es lo que obliga a bajar de la generalidad. Si de un objetivo no se puede escribir en qué se nota, no es un objetivo: es una función, y va al inventario.

**Y una sección que no estaba en ningún molde: supuestos, restricciones y dependencias.** Lo que se da por cierto sin comprobar y qué pasa si resulta falso, lo que no se negocia —incluido el formato de los entregables— y lo que se necesita de gente que no está en el equipo. Es lo más barato de escribir y lo más caro de omitir.

**Está en evaluación, y por eso no vive todavía con los demás moldes.** Queda en `plantillas/cvds/planificacion/`, con una copia llenada con este mismo proyecto en `cvds/` para ver qué contesta. Esa prueba dejó a la vista tres huecos reales del estándar: nunca se estimó esfuerzo, no hay presupuesto, y el frente operativo sigue sin evidencia porque nadie ajeno al autor lo ha instalado.

---

## 33.1.0 — 2026-08-22

**MENOR** (cuatro comprobaciones que antes callaban o mentían; nadie tiene que hacer nada, y ningún proyecto deja de cumplir por esto).

**Una clave que alguien pega en el chat ya no queda escrita a la vista.** El programa que las tapa reconocía las que escribe otro programa, con el valor entre comillas, y no las que teclea una persona. Quien escribiera su clave sin comillas la dejaba en el registro de la conversación, que se guarda para siempre. Ahora se tapan las tres formas en que de verdad se escriben, y se conserva el nombre de la variable, para que quien lea después siga entendiendo de qué se hablaba.

**Lo que se decidió con una medición y no con una opinión:** taparlo todo estropea el registro, así que antes de dejar el cambio se midió sobre todas las conversaciones guardadas. Ninguna línea cambiaría. Y esa misma medición mostró el único caso que había que dejar quieto: un pedazo de programa pegado en el chat, donde la palabra «clave» es el nombre de una variable y no un secreto.

**Un proyecto ya no puede decir que sigue una versión que no existe.** Podía escribir cualquier número, y si era mayor que el verdadero pasaba algo peor que no detectarlo: el aviso de estar atrasado **se apagaba**, porque el programa concluía que iba adelantado. Ahora se comprueba que el número exista de verdad, y que coincida con lo que el instalador dejó anotado la última vez. Buscándolo apareció el caso en un proyecto real: dice seguir una versión y su propia constancia dice otra, las dos del mismo día.

**Y el aviso de estar atrasado ahora llega solo, al abrir.** Estaba construido desde hacía tiempo y había que pedirlo a mano, así que no llegaba nunca a donde tenía que llegar. Se veía funcionar todos los días en un solo sitio: aquí, donde estas comprobaciones se corren de a una. En un proyecto instalado no aparecía jamás. Además ahora dice **qué cambió** entre las dos versiones, empezando por si alguna obliga a rehacer algo, que es lo único que cambia la decisión de ponerse al día.

**Y una comprobación dejó de acusar sobre lo que no pudo leer.** Apuntada a un proyecto, buscaba allí cuatro archivos que solo existen aquí, no los encontraba y reportaba igual: cinco veredictos falsos, uno de ellos con el hueco vacío donde iba el dato que no consiguió. Ahora dice en una línea que esa carpeta no es la que revisa, y cuál es la forma correcta de pedirlo.

**El detalle.** Cuatro fases, una por historia: [`B-EP-005-HU-002`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa/resultado_pruebas.md), [`B-EP-002-HU-003`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/B-EP-002-HU-003-la-version-declarada-se-comprueba/resultado_pruebas.md), [`B-EP-002-HU-004`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio/resultado_pruebas.md) y [`B-EP-004-HU-011`](documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo/resultado_pruebas.md). Cierran los cuatro pendientes que dejó ejecutar las quince fases detenidas, y **buena parte de sus 38 pruebas comprueban lo que NO debe hacerse**: una comprobación que reprueba de más se apaga a la semana, y entonces no queda nada.

---

## 33.0.0 — 2026-08-22

**MAYOR** ⚠ obliga a migrar: un proyecto que ya tenga su lista de funcionalidades escrita la rehace con la estructura nueva. Lo que cambia es que cada funcionalidad pasa de una fila a una ficha.

**Una fila no alcanzaba para construir nada.** La lista decía qué hace el producto y si estaba probado, y eso servía para aprobar el alcance y para armar el manual. Pero cuando llegaba la hora de partir el trabajo, había que volver a preguntarlo todo: quién usa esto, qué recibe, qué entrega, qué reglas del negocio la gobiernan, de qué otra funcionalidad depende y cómo se sabe que está terminada. Esa información se inventaba de nuevo en cada historia, y por eso dos historias del mismo producto salían con criterios distintos.

**Ahora cada funcionalidad tiene su ficha, con catorce campos.** Qué hace, para qué sirve, a qué parte del sistema pertenece, quién la usa, qué recibe, qué entrega, qué reglas debe respetar, de qué depende, cuándo se considera terminada, qué hay que construirle, prioridad, estado, si está verificada, y lo que hay que tener en cuenta. El resumen de arriba sigue existiendo, con una línea por funcionalidad, para verlas todas juntas.

**Tres cosas que la ficha resuelve y antes no.** Cada funcionalidad tiene un número propio que no se reutiliza, aunque se descarte, porque planes y pruebas la nombran por ahí. El «Terminada cuando» se convierte tal cual en el criterio de aceptación de su historia y de ahí salen las pruebas, sin inventarlos aparte. Y las tres clases quedan escritas: obligatoria, complementaria y futura, que no es lo mismo que lo que todavía no se sabe si entra, y por eso eso último sigue en su propia sección.

**Estado y verificación son dos casillas distintas, y se sostiene.** «Estado» es lo que alguien dice que va pasando. «Verificado» solo lo llena una prueba corrida. Una funcionalidad puede estar implementada y sin verificar: quiere decir que se construyó y que nadie lo ha demostrado.

**Sigue sin nombrar tecnología.** La ficha pregunta si necesita pantalla, lógica de servidor, almacenamiento, conexión con un sistema de afuera o una tarea que corre sola. No pregunta con qué se hace: eso vive en la ficha de tecnología del proyecto.

**El detalle.** El molde [`02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md). La regla que lo exige, [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md), no cambia: la lista aprobada sigue siendo la puerta.

---

## 32.1.2 — 2026-08-22

**PARCHE** (afina el tono que pide el molde del inventario; no cambia qué se exige).

**Claro no es lo mismo que infantil, y la primera pasada se fue al otro lado.** Al escribir para que cualquiera entienda, las descripciones empezaron a rodear lo que querían decir: «un puñado de reglas que nadie puede saltarse», «las mañas de quien manda», «ni cuando el trabajo es chiquito». Se entendían, pero sonaban a cuento infantil, y un documento que va camino a ser el manual de un producto no puede sonar así.

**El tono queda escrito en el molde:** palabras comunes y frases cortas, sin rodear lo que se quiere decir ni explicar de más. Es el tono con que se le explica algo a un adulto que no es del oficio. Ni jerga ni cuento.

**El detalle.** El molde [`02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), con el ejemplo corregido, y las 36 filas de [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md) pasadas otra vez.

---

## 32.1.1 — 2026-08-22

**PARCHE** (aclara dónde llega una exigencia que ya estaba, y le pone ejemplo; nadie tiene que hacer nada nuevo).

**El nombre de una funcionalidad cuenta tanto como su descripción.** La lista de lo que un producto debe hacer ya se escribía para que la entienda cualquiera, pero el nombre de cada fila seguía siendo una etiqueta de casa. Un nombre así deja la fila a medias: quien la lee de afuera pasa de largo antes de llegar a la explicación. Ahora se dice explícitamente que la prueba cubre las tres cosas, el nombre del grupo, el nombre de la funcionalidad y su descripción, y el molde trae el ejemplo de una fila que la pasa al lado de una que no.

**Se midió sobre un caso real.** De las 36 filas del inventario del propio Cimiento, 21 no pasaban la prueba, y la columna del nombre estaba peor que la de la descripción. Palabras como «núcleo blindado», «expediente», «desfase», «traza» o «veredicto» no le dicen nada a quien va a usar el producto, aunque adentro se entiendan solas. Las 36 quedaron reescritas.

**El detalle.** El molde [`02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), con el ejemplo en la sección del grupo, y el inventario reescrito en [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md).

---

## 32.1.0 — 2026-08-22

**MENOR** (una exigencia nueva sobre cómo se escribe el molde del inventario; nada de lo ya escrito deja de valer).

**La lista de lo que un producto debe hacer ahora se escribe para que la entienda cualquiera.** Antes solo la columna que describe cada funcionalidad se escribía así; el resto del documento hablaba en el idioma de quien lo construye, y quien iba a usar el producto no lo entendía. La exigencia cubre ahora el documento entero, y trae con qué medirla: **un niño lo lee y entiende qué hace el producto**. Si para entender algo hay que saber del proyecto, está escrito para adentro y se rehace.

No es una idea nueva: es lo que ya pedían [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) y [`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md), pocas palabras y ninguna que haya que ir a buscar, aplicado ahora a un documento concreto y con una prueba que cualquiera puede correr.

**Qué salió al aplicarla.** «Proyección: por confirmar con el usuario» se llama ahora «Lo que todavía no se sabe si entra». «No se derivan épicas» es «no se parte el trabajo en bloques». «Los ítems aprobados bajan a requisitos» es «cada fila baja a trabajo con su nombre y su número». Se fueron también «alcance», «trazabilidad» y «bloquea los ítems que la citan». Ninguna sección cambió de propósito: cambió de idioma.

**Y las secciones fijas perdieron el número.** Eran «2. Proyección», «3. Preguntas» y «4. Qué pasa». Un proyecto con seis grupos de funcionalidades las numera 7, 8 y 9, y el comprobador las reportaba como secciones faltantes en todos. Sin número, coinciden siempre.

**El detalle.** El molde [`02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md). El inventario de Cimiento ([prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md)) queda cerrado con el molde nuevo: 36 filas en seis grupos, todas sin verificar, sin preguntas abiertas.

---

## 32.0.1 — 2026-08-22

**PARCHE** (una carpeta que el documento del proyecto nombraba de dos formas; nadie tiene que hacer nada).

**Una misma carpeta se llamaba de dos maneras en el mismo archivo.** El documento que se instala en cada proyecto para decirle al agente cómo trabajar ahí nombraba de dos formas distintas el sitio donde queda el historial de actualizaciones. Solo una de las dos es la real, y es donde el instalador escribe.

**Cómo se encontró:** buscando. Se fue a mirar el historial de un proyecto real, se buscó en el sitio que decía el segundo nombre, no estaba, y por un momento pareció que el historial no existía. Existía, con dieciocho registros. Un nombre a medias hace perder el tiempo en la dirección más cara: la de creer que falta algo que está.

**El detalle.** Sale del defecto D-03 de la fase [`A-EP-002-HU-003`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/A-EP-002-HU-003-retrodocumentar-la-version-adoptada/resultado_pruebas.md). Los otros dos defectos de esa fase, que sí son de fondo, quedaron en el [pendiente 82](pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md).

---

## 32.0.0 — 2026-08-22

**MAYOR** ⚠ obliga a migrar: un proyecto que ya tenga su inventario de funcionalidades escrito lo reescribe con la estructura nueva. Lo que cambia es la columna de estado y lo que se puede dejar por fuera.

**El inventario no era la lista de lo que falta, y se estaba usando así.** El molde definía cuatro estados por ítem —Existe, Parcial, Por construir, Por confirmar— y el agente los llenaba leyendo el código. De ahí salían dos vicios. El primero: si algo ya estaba construido, la fila tendía a no escribirse, porque «eso ya existe». El segundo: «Existe» era una afirmación del agente sobre lo que le pareció al leer, no una prueba.

**Y toda la historia que el molde arrastraba.** Abría con «Lo que el usuario ya definió», pedía la fecha del estado, guardaba las preguntas contestadas con su respuesta y cerraba con quién lo escribió y cuándo. Nada de eso es el producto: son decisiones que ya viven en el planteamiento y en el histórico, duplicadas acá con la duda de cuál manda. **El inventario se lee ahora como si nada estuviera construido**, aunque se llene con lo que ya se sabe. También se fue el encabezado que anunciaba el estado del documento y repetía la regla que lo rige: no le decía nada a quien lo lee para saber qué hace el producto. En su lugar hay una frase: «esta es la lista completa de lo que el producto debe hacer; cada fila dice qué es, para qué sirve y si ya se probó», y tres puntos de «cómo se lee» en el idioma de quien lo va a usar. Una pregunta contestada deja de ser pregunta: sube a fila del producto, o se va del documento.

**Las tres leyes que ahora encabezan el molde.** *Se lista todo lo que el producto debe tener, esté construido o no*: ninguna fila se omite porque ya exista, porque ya se haya decidido o porque aparezca en otro documento. *Este documento no lleva historia*: ni fechas, ni quién decidió qué, ni qué se preguntó y se contestó. Y *que algo esté hecho lo dice la prueba, no el agente*: la columna «Verificado» solo se llena con la prueba corrida y su fecha, y sin prueba dice **Sin verificar**, que no es lo mismo que «no existe».

**Por qué importa más de lo que parece:** el inventario no se archiva al arrancar, madura hasta ser el manual del producto. Un inventario podado entrega un manual sin lo que sí está construido, y un inventario con estados afirmados entrega un manual que dice que algo funciona sin que nadie lo haya probado.

**La columna nueva.** Cada fila gana «De qué se trata»: qué hace y para qué sirve, escrito para quien va a usar el producto y en la menor extensión con la que se entienda ([`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)). Es la semilla del manual, y antes no existía: la descripción de uso se pedía en prosa y no tenía dónde vivir.

**Lo que no cambia.** [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) sigue igual: el inventario aprobado sigue siendo la puerta de las épicas, y lo no decidido se sigue marcando «por confirmar». Lo que se corrigió es el molde, no la puerta.

**Y el molde entero pasó la prueba del niño.** No solo la columna: el encabezado, los avisos de cada sección, los nombres de las secciones y el cierre. Salieron «alcance», «derivar épicas», «ítem», «trazabilidad» y «proyección», que obligan a saber del proyecto para entender qué hace el producto. «Proyección: por confirmar con el usuario» pasó a llamarse «Lo que todavía no se sabe si entra». Las secciones fijas perdieron el número, para que un proyecto con seis grupos de funcionalidades siga coincidiendo con su molde. La exigencia queda escrita en la caja del molde, con [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) al lado de `00·ID9`: **un niño lo lee y entiende qué hace el producto; si hay que saber del proyecto, está escrito para adentro y se rehace.**

**El detalle.** El molde [`02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) y la señal [S-022](documentacion/senales.md), con las palabras del usuario que lo originaron. El primer inventario reescrito con el molde nuevo es el de Cimiento ([prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md)): 34 filas, las 34 sin verificar.

---

## 31.15.0 — 2026-08-22

**MENOR** (el recuento de marcas deja de contar lo que nunca fue marca; ningún commit que hoy pasa empieza a fallar).

**Nueve mil marcas que no eran marcas.** El anexo de marcadores dice, en sus propias filas, «la raya larga (`—`) **como inciso**» y «el punto medio (`·`) separando frases **en prosa**». Un título no es un inciso. Una celda de tabla no es un párrafo. El rótulo de un campo cuyo valor es el espacio por llenar no es una viñeta de prosa: es un formulario. El programa las contaba todas igual, y por eso perseguir un recuento limpio empujaba a estropear los documentos.

**No se declaró ninguna excepción: se implementó lo que ya estaba escrito.** Es la segunda vez que pasa lo mismo. El 2026-08-18 el punto medio de los encabezados estaba nombrado en el comentario del código y no implementado en la expresión, y el recuento bajó de 16 477 a 15 485. Ahora baja de **15 485 a 6 440**.

**Los moldes del ciclo de vida quedaron en cero**, sin renombrar una sola sección y sin que ninguno pida algo distinto de lo que pedía. Eso importa porque renombrar la sección de un molde hace que todos los documentos ya escritos con él reporten que les falta: son 651 en este repositorio.

**Y en prosa todo sigue igual.** La misma viñeta llenada con una frase vuelve a contar, el inciso entre rayas cuenta como siempre, y el punto medio entre dos frases también. Cada caso se probó con su pareja, para que una expresión demasiado ancha no dejara a `00·ID8` sin quien la haga cumplir.

**Lo que esto le cambia a un proyecto instalado:** la deuda de notación que arrastraba desaparece sin que toque un archivo, porque nunca fue deuda. El trinquete del commit no se mueve: falla cuando la cuenta sube, y esta solo baja.

**El detalle.** Fase [`C-EP-004-HU-012`](documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion/funcionalidad_implementada.md), que cierra el [pendiente 78](pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md) junto con la fase B del mismo día. La decisión queda escrita en [`marcadores-de-ia.md`](base/00-identidad-y-rol/marcadores-de-ia.md), al lado de la del 2026-08-18.

---

## 31.14.0 — 2026-08-22

**MENOR** (un aviso nuevo en el `pre-commit`; nadie tiene que hacer nada, y ningún commit se rechaza por esto).

**Un commit ya no se lleva en silencio el trabajo de otra sesión.** Con dos conversaciones abiertas sobre el mismo repositorio, un `git add` general no distingue de quién es cada archivo: la que commitea primero publica lo que la otra tiene a medio construir. Pasó acá el 2026-08-22, y lo que quedó publicado durante ocho minutos fue un validador con el criterio que reprobaba documentos correctos. El caso ya estaba escrito como riesgo en el planteamiento del estándar; esta es la primera vez que se documenta con daño medido.

**No se pregunta de quién es el commit, sino si mezcla.** Averiguar qué sesión lanza el enganche es imposible: lo lanza `git`, que no sabe nada de sesiones. Dada vuelta, la pregunta se contesta sola, porque la señal que importa no necesita identidad: **si lo que entra al commit lo tocaron dos sesiones distintas, alguien está publicando trabajo que no es suyo.** Un commit legítimo sale de una sola conversación.

**Avisa y deja pasar.** Retomar lo que otra sesión dejó a medias es legítimo, y a veces es lo que se quiere; lo que no es normal es hacerlo sin darse cuenta. Rechazar el commit tampoco era opción, y está medido en el registro de la 26.x: un enganche que rechaza siempre se apaga en una tarde, y ese es el defecto más caro de esta casa. Por lo mismo, el registro de cada sesión caduca a las doce horas: sin eso, el de la semana pasada haría saltar el aviso en cada commit.

**El registro no se versiona.** Es estado de trabajo, no memoria. Guardarlo con el resto lo convertiría en el próximo archivo que dos sesiones se pisan, que es justo lo que se está resolviendo.

**El detalle.** Historia [`HU-017`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-017-el-commit-no-se-lleva-lo-ajeno/HU-017-el-commit-no-se-lleva-lo-ajeno.md) y su fase [`A-EP-005-HU-017`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-017-el-commit-no-se-lleva-lo-ajeno/A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones/funcionalidad_implementada.md), del [pendiente 80](pendientes/hecho/dos-sesiones-a-la-vez-no-se-pisan.md). Nace `validadores/sesiones.py` y el subcomando `validar.py sesiones`, con diez casos, y **cinco de los diez comprueban que el aviso NO salte**: es lo que decide si esto sigue vivo dentro de un mes.

---

## 31.13.0 — 2026-08-22

**MENOR** (el molde del planteamiento gana instrucciones y un campo; los planteamientos ya escritos siguen valiendo).

**El mismo molde sirve ahora para un proyecto que empieza y para uno que ya está construido.** Antes no decía nada del segundo caso, y el que lo llenaba improvisaba: se ponía a **describir lo que hay** en vez de **plantear lo que se necesita**. Pasó acá mismo, con el planteamiento de este repositorio, y hubo que rehacerlo dos veces. Ahora el molde dice de dónde se levanta la información cuando no hay a quién entrevistar, y trae la tabla de las cuatro traducciones que es donde se falla: «el sistema **es**» pasa a «**hace falta**», la métrica de hoy pasa a la exigencia, el incidente ya ocurrido pasa a riesgo, y lo ya construido **sí** entra en el alcance, porque se plantea lo que el proyecto necesita y no lo que le falta.

**Y reconstruir es también auditar.** Si al escribirlo aparece algo ya construido que no cabe en el alcance o choca con un no negociable, no se acomoda el documento para que quepa: se anota como hallazgo y lo decide el usuario. Sin esa frase el molde se vuelve una máquina de justificar hacia atrás lo que ya esté en el disco.

**La procedencia tiene ahora un solo dueño:** un campo en la identificación. Antes se colaba donde alcanzara, y en el único planteamiento reconstruido que existía se coló justo encima del encuadre, que desapareció sin que nadie lo notara. Por eso el molde declara además que **el encuadre no se borra**: lo que se borra al llenar es el recuadro de instrucciones, y solo ese.

**El encuadre dejó de copiar la cadena y ahora la enlaza.** La copia se había desactualizado: decía «análisis → alcance → épica/HU» donde la regla dice «planteamiento → épica → HU». Dos versiones de la misma cadena en el mismo repositorio, y la que se leía primero era la equivocada.

**Un arreglo que salió de probarlo:** el molde manda nombrar el archivo `prompts/<slug>-planteamiento.md`, y el validador solo reconocía el nombre pelado, así que la comprobación de la versión anterior **no alcanzaba a ninguno** de los documentos que este molde produce. Ya los reconoce. El primer intento aceptaba cualquier sufijo y resolvía mal 29 documentos, tomando cada resultado de pruebas por un plan de pruebas; se midió y se acotó antes de dejarlo.

**El detalle.** Fase [`C-EP-003-HU-002`](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/funcionalidad_implementada.md). Queda un caso sin correr y está dicho: la prueba de darle los dos documentos a un lector que no participó, para ver si distingue cuál se escribió sobre algo ya construido.

---

## 31.12.0 — 2026-08-22

**MENOR** (una comprobación nueva y una limpieza de los moldes; ningún documento ya escrito deja de valer).

**Un documento ya no puede perder la instrucción que dice cómo se usa.** Toda plantilla del ciclo pone, antes de su primer separador, un texto que no es para borrar: dice qué es ese documento y qué no autoriza. En el molde del planteamiento es el que le recuerda al agente que eso es insumo y no una orden de entregar código. Nada impedía reemplazarlo al llenar, y ya había pasado: el planteamiento de este mismo repositorio se escribió con una nota de procedencia en ese lugar, con la fecha y las fuentes, y el encuadre desapareció sin que nadie lo notara. Ahora `validar.py plantilla` lo reprueba, y reprueba también que ahí se cuente de dónde salió el documento en vez de cómo se usa.

**Se comprueba que esté y que no cuente procedencia, no que diga lo correcto.** Juzgar la redacción es de una persona. Y el texto se reconoce **por su posición**, no por su rótulo: el rótulo cambió dos veces en un solo día, y un validador atado a una redacción reprueba lo que está bien apenas alguien corrige el molde.

**Los moldes del ciclo dejaron de llevar adorno.** De 197 marcas de generación automática a 126, y las que quedan no son adorno: son el rótulo de un campo del formulario, una celda de tabla, el nombre de una sección o un identificador con su enunciado. Se clasificaron una por una antes de tocar nada, y eso fue lo que salvó los moldes: un reemplazo a ciegas habría quitado los rótulos de los campos y renombrado 23 secciones, y renombrar una sección hace que los 650 documentos ya escritos con ese molde reporten que les falta.

**Lo que queda pendiente, y es del usuario:** decidir si esas cuatro formas se declaran notación en la lista de marcadores, como ya se hizo el 2026-08-18 con el punto medio de los encabezados, o si se reescriben los moldes asumiendo el daño.

**El detalle.** Fase [`B-EP-004-HU-004`](documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado/funcionalidad_implementada.md), del [pendiente 77](pendientes/hecho/el-planteamiento-conserva-su-encuadre.md), con nueve casos y un barrido sobre 650 documentos reales que obligó a corregir el criterio dos veces. Y fase [`B-EP-004-HU-012`](documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo/funcionalidad_implementada.md), del [pendiente 78](pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md), que queda abierto porque su meta original, llegar a cero, depende de una decisión que es del usuario: qué hacer con las 126 marcas que quedan, que son todas notación.

---

## 31.11.0 — 2026-08-22

**MENOR** (una comprobación nueva para el cierre de una fase; nadie tiene que hacer nada).

**Ya se puede comprobar si una fase tocó los archivos que su plan decía.** El estándar exige desde siempre que una unidad de trabajo edite lo que su plan declaró, y que descubrir otro archivo detenga la ejecución hasta ampliarlo por escrito; comprobarlo era leer el plan y los cambios a la vez, o sea casi nunca. Ahora una orden los compara contra el punto del que salió la fase, y avisa lo que no cuadra. También dice qué criterio de aceptación se quedó sin ningún caso que lo compruebe.

**Avisa y no detiene**, porque un archivo de más puede ser un descubrimiento que se reportó y se aprobó, y eso no se ve desde los archivos. Lo que el programa afirma es que la lista no cuadra; si la explicación cuadra, lo lee una persona.

**Y su primera corrida encontró un incumplimiento del trabajo de esta misma jornada:** la mejora anterior tocó tres archivos que su plan no declaraba. La decisión de separarlos fue buena; lo que faltó fue anotarla antes de ejecutar. Queda escrito en las dos fases.

**El detalle.** Fase [`A-EP-004-HU-013`](documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/README.md), del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), con sus decisiones 10 y 22. Nace [`validadores/plan_vs_hecho.py`](validadores/plan_vs_hecho.py) y el subcomando `validar.py plan`, con once casos. Lo que **no** se automatiza queda declarado: comparar los pasos ejecutados con los escritos exige leer los dos textos, y eso sigue siendo de una persona.

## 31.10.0 — 2026-08-22

**MENOR** (la revisión completa termina diciendo por cuál regla se incumple más; nadie tiene que hacer nada).

**Ahora se sabe qué regla da más problemas, con un número.** Una regla que produce cien hallazgos por semana casi nunca significa un equipo descuidado: significa una regla mal escrita, o una que hace falta automatizar. Sin ese dato la conversación era opinión contra opinión. La revisión completa termina agrupando lo encontrado por regla, y guarda una línea por corrida para poder comparar dos.

**Del registro se guarda el número, nunca lo revisado.** En un mensaje de incumplimiento viaja el contenido del archivo, y ahí puede ir una clave: un archivo de métricas que copie lo revisado es una fuga con nombre de estadística. Se guarda el identificador de la regla, cuántas veces, la fecha y la versión. Nada más, y fuera del control de versiones porque es generado.

**El primer dato ya dice algo:** la regla de no dejar marcas de generación automática produce **dos de cada tres hallazgos** del repositorio, porque se mide sobre todo el árbol mientras la regla exige limpieza en lo que se **entrega**. Queda anotado para quien decida si se acota la medición o se amplía la regla.

**El detalle.** Fase [`A-EP-004-HU-009`](documentacion/epicas/EP-004-comprobacion-automatica/HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/README.md), del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), con su decisión 25. La regla de cada hallazgo sale del mensaje que los veinticuatro validadores ya escriben, así que no hubo que tocarlos: se acumulan donde todos pasan. Once casos de prueba nuevos.

## 31.9.0 — 2026-08-22

**MENOR** (el documento de cierre de una fase gana un campo; lo ya cerrado no se toca).

**Un trabajo cerrado ya dice bajo qué reglas se cerró.** Sin eso, cada regla nueva hace parecer incumplido lo viejo, y hay que reabrirlo para averiguar si lo estaba, que es exactamente lo que el estándar dice que **no** pasa: una norma nueva no reabre lo cerrado. Ahora el documento de cierre trae el número de versión del estándar en el momento de cerrar, y la comprobación de fases avisa cuando falta.

**Avisa, no detiene:** un cierre sin ese dato no rompe nada hoy, solo deja una pregunta sin respuesta. Y no se exige hacia atrás: lo cerrado antes de hoy queda de su lado.

**El detalle.** Fase [`A-EP-002-HU-005`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/README.md), del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), con sus decisiones 7 y 28. El campo entra al molde del cierre y no al de apertura, porque al abrir todavía no hay nada que sellar. La comprobación reconoce la fila del molde y también la frase escrita a mano, para no reportar la forma en vez del contenido. Los quince cierres escritos hoy quedaron sellados con la versión bajo la que de verdad cerraron.

## 31.8.0 — 2026-08-22

**MENOR** (dos comprobaciones nuevas sobre la carpeta de pendientes; ningún proyecto tiene que hacer nada hacia atrás).

**Un pendiente ya tiene que decir de dónde viene y en qué se convirtió.** Hacia arriba: uno abierto que no nombra la historia a la que baja **detiene la corrida**, porque sin ella no se puede construir. Hacia abajo: uno cerrado que no dice en qué fase se hizo **queda avisado**, no detenido: ya no rompe nada, solo cortó su rastro.

**Y midió la deuda que había.** De los pendientes cerrados desde el 2026-08-16, cuando nació la exigencia, **24 no dicen en qué fase se hicieron**. No se rellenaron a las corridas a propósito: reconstruir de memoria la fase de veinticuatro es el camino directo a escribir una que no fue. Cada uno lo gana cuando alguien lo toque, y mientras tanto la corrida lo recuerda.

**Nada se exige hacia atrás.** Lo cerrado antes de esa fecha, y lo que ni siquiera declara fecha, queda de su lado: treinta avisos que nunca se van apagan la comprobación entera.

**El detalle.** Fases [`A`](documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/README.md) y [`B`](documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/README.md) de EP-004 · HU-016, del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), con las decisiones 26 y 27 que ese pendiente ya traía. Ocho casos de prueba nuevos.

## 31.7.0 — 2026-08-22

**MENOR** (una orden nueva que revisa todo de una vez, y una comprobación que faltaba; nadie tiene que hacer nada).

**Una sola orden dice cómo está el proyecto.** Había más de cuarenta comprobaciones sueltas y saber cómo estaba todo exigía acordarse de cuáles aplican y leer cuarenta resúmenes; lo que hay que recordar, no se corre. Ahora `validar.py todo` corre las 31 que aplican y termina en una línea: cuántas se corrieron y cuántas fallaron. Lo lento sigue aparte, con el motivo escrito al pie de la corrida, porque una revisión que tarda es una que nadie hace.

**Y su primera corrida encontró tres cosas que nadie miraba**, todas ciertas: tres programas creados ese mismo día no estaban en el mapa de qué se queda si mañana cambia la herramienta, y dos comprobaciones de instalación estaban midiendo al estándar como si fuera un proyecto que lo hereda.

**Lo segundo: dos reglas ya no pueden compartir identificador sin que se sepa.** Se comprobaba que cada capítulo tuviera su prefijo, pero no que el número no se repitiera dentro de él; con dos reglas iguales, toda cita a ese número es ambigua. Se contaron a mano las 249 y ninguna se repetía, lo que decía que el orden estaba bien por costumbre y no por comprobación.

**El detalle.** Fases [`A-EP-004-HU-008`](documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/A-EP-004-HU-008-la-corrida-completa-en-una-linea/README.md) y [`A-EP-004-HU-011`](documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr/README.md), del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). Doce casos de prueba nuevos; el que decide en la corrida completa es que un subcomando nuevo entre solo, sin listas a mano.

## 31.6.0 — 2026-08-22

**MENOR** (una comprobación nueva al guardar, sobre el repositorio del estándar; ningún proyecto tiene que hacer nada).

**Cambiar una regla y olvidar la versión ya no se puede.** El estándar exige que todo cambio de lo que viaja a los proyectos suba el número de versión y escriba su entrada en el registro, y hasta hoy eso dependía de que alguien se acordara. Ahora, al guardar, si el cambio toca las reglas o los moldes y falta alguno de los dos, el guardado **se detiene** y el mensaje dice cuál falta. Un cambio que no toca las reglas no nota nada: pedir versión donde no toca es el ruido que apaga cualquier control.

**El detalle.** Fase [`A-EP-005-HU-005`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version/README.md), del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). Nace [`validadores/guardian_version.py`](validadores/guardian_version.py), que corre dentro de `validar.py versionado --preparados`, o sea dentro del enganche que ya existía: dos enganches sobre el mismo momento se pisan. Siete casos de prueba, con el que decide, que un commit ajeno a las reglas no note nada. No juzga si la entrada del registro dice la verdad ni si el tipo de versión es el correcto: eso exige leer, y queda escrito en su contrato.

**Y se cerró la fase [`B-EP-005-HU-003`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/B-EP-005-HU-003-el-hallazgo-grave-detiene/README.md)**, que no cambia nada del programa: comprueba, corriendo el enganche como lo corre la herramienta, que un documento con un enlace roto se devuelve para corregir, que uno sano no molesta, y que el archivo nunca se toca.

## 31.5.0 — 2026-08-22

**MENOR** (las comprobaciones dejan de caerse ante un archivo que no pueden leer; nadie tiene que hacer nada).

**Un archivo con la codificación rota ya no tumba la revisión entera.** Hasta hoy, un documento guardado por un editor viejo o venido de otro programa hacía que la comprobación terminara con un volcado técnico, **perdiendo todos los problemas que ya había encontrado**. Ahora se lee lo que se pueda, la revisión sigue con los demás archivos, y el que no se pudo leer bien aparece en el reporte con su ruta y con el aviso de que lo que se diga de él puede estar incompleto.

**Por qué no basta con leer y callar:** eso convertiría un archivo roto en uno que parece sano. Se hacen las dos cosas, seguir y decirlo.

**El detalle.** Fase [`B-EP-004-HU-003`](documentacion/epicas/EP-004-comprobacion-automatica/HU-003-formato-del-hallazgo/B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida/README.md), del [pendiente 59](pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). `comun.leer` gana sus tres salidas y el registro de lo ilegible, que `reportar` agrega solo; `pendientes.py` recupera la lectura común que había tenido que escribirse aparte; el contrato de `docs/comun.md` lo dice. La prueba que lo denunciaba llevaba días marcada como fallo esperado y hoy pasa destapada. De paso quedaron a la vista ocho pruebas que estaban en rojo desde el 2026-08-21 citando moldes que se habían movido, y se corrigieron.

## 31.4.0 — 2026-08-22

**MENOR** (una forma nueva de buscar en el histórico; nadie tiene que hacer nada).

**Ahora se puede buscar por tema lo que se habló, y no solo por fecha.** Una sesión toca varios asuntos y su nombre solo dice uno: con 59 resúmenes acumulados, encontrar dónde se decidió algo era abrirlos uno por uno. Los temas ya estaban escritos, en el título de cada hallazgo, así que se recogen todos en un archivo: **345 temas, cada uno enlazado a la sesión donde se trató**.

**El detalle.** Punto 8 del pendiente [33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), en la fase [`C` de EP-005 · HU-001](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/C-EP-005-HU-001-el-historico-se-busca-por-tema/README.md). Nace [`validadores/temas.py`](validadores/temas.py) con el subcomando `validar.py temas --aplicar` y siete casos de prueba; el índice se genera, y quedar atrás es aviso, nunca falla. No agrupa temas parecidos: junta lo que ya estaba escrito, que es lo que un programa puede hacer sin fingir que entiende.

## 31.3.0 — 2026-08-22

**MENOR** (lo que el estándar mejore en el README del histórico llega a los proyectos ya instalados; nadie tiene que hacer nada).

**Un proyecto instalado hace meses ya no se queda con el texto de hace meses.** Cuando el estándar mejoraba el README del histórico, los proyectos nuevos lo recibían y los que ya estaban instalados no: su archivo seguía diciendo lo de siempre, y nadie lo notaba porque existe, se lee bien y dice cosas ciertas, solo que menos. Ahora el instalador le agrega lo que el estándar sumó, **sin tocar una línea de lo que el proyecto escribió**, y dice qué agregó. Es el mismo mecanismo que el archivo de instrucciones del agente ya usaba.

**Lo primero que va a llegar por ahí:** la respuesta a qué manda cuando el histórico y lo acordado se contradicen. Manda lo acordado, y el histórico dice de dónde salió; el histórico no se edita nunca para que cuadre, porque su valor es decir lo que se dijo.

**El detalle.** Punto 8 del pendiente [33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), en la fase [`B` de EP-007 · HU-005](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma/README.md). `instalar_historico` reusa `_completar_secciones`, el mecanismo de `01·C18`, con seis casos de prueba nuevos; el que decide es el que comprueba que lo escrito por el proyecto sobrevive palabra por palabra.

## 31.2.0 — 2026-08-22

**MENOR** (una comprobación nueva del repositorio del estándar; ningún proyecto tiene que hacer nada).

**El mapa que dice dónde está cada cosa ya no puede quedarse viejo sin que nadie lo note.** Ese mapa es por donde entra quien abre el repositorio y no sabe dónde está nada, y estaba escrito a mano: una carpeta nueva simplemente no aparecía, y quien lo leyera creería que no existe. Ahora hay una comprobación que lo dice. En su primera corrida encontró cuatro carpetas que existen y no estaban nombradas, y una que el mapa nombraba y ya no existe: el mapa decía doce carpetas y son dieciséis.

**El detalle.** Punto 8 del pendiente [33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), en la fase [`B` de EP-005 · HU-011](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece/README.md). Nace [`validadores/sitio.py`](validadores/sitio.py) con el subcomando `validar.py sitio` y siete casos de prueba, copiando la forma de `amarre.py`: la carpeta que falta es falla, la que sobra es aviso, y con el mapa al día se calla. El mapa quedó actualizado y su cabecera dice cómo comprobarlo.

## 31.1.0 — 2026-08-22

**MENOR** (el modelo de historia de usuario gana una columna opcional; nada obliga a nadie).

**Una historia ya puede decir qué criterio depende de cuál.** Su tabla de fases decía qué se cubre y con qué documentos, pero no si un criterio no se puede comprobar mientras otro no esté cumplido. Sin eso, dos fases se ordenan al revés y el error aparece al probar, cuando ya se construyó. Se resolvió con una columna, no con una sección nueva: la historia cuyos criterios son independientes la deja vacía y no paga nada por tenerla.

**El detalle.** Punto 8 del pendiente [33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), abierto desde el 2026-08-07, en la fase [`B` de EP-003 · HU-002](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual/README.md). La columna se llena con criterios, no con fases, y queda escrito en el propio molde. Sin validador a propósito: decidir si un criterio depende de otro exige leer los dos.

## 31.0.0 — 2026-08-22

**MAYOR** ⚠ obliga a migrar (antes de publicar una versión hay que releer el tramo y anotar lo que se pidió dos veces).

**Lo que alguien pide dos veces deja de perderse entre sesiones.** Hasta hoy, un criterio que el usuario repetía en sesiones distintas solo se convertía en regla si alguien lo notaba en el momento; si no, se repetía la corrección tres o cuatro veces más. Desde esta versión, antes de publicar se relee el tramo que se cierra y lo repetido se escribe en un documento con su salida: ya está cubierto, merece regla nueva, hay que afinar una existente, o no es regla del estándar. Decidir cuáles se escriben sigue siendo del usuario.

**Qué hay que hacer para adoptarla.** Al cerrar la próxima versión, escribir el barrido con el molde nuevo, [plantillas/candidatas-a-regla.md](plantillas/candidatas-a-regla.md). No hay que barrer hacia atrás: rige del tramo en curso en adelante.

**El detalle.** Nace [`20·M20`](base/20-meta-reglas/reglas/M20-antes-de-publicar-una-version-se-barre-lo-que-se-pidio-dos-veces.md), que extiende a `01·C10` (esa atrapa el patrón en el momento; esta relee lo que en el momento no se notó), y el criterio `CA-06` de EP-001 · HU-007, en la fase [`C`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador/README.md). Sale del punto 2 del pendiente [33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), abierto desde el 2026-08-06, donde el defecto estaba dicho así: «sin disparador, se hace cuando el usuario lo pida es un favor, no una norma». El barrido se había hecho una sola vez, el 2026-08-13, con 27 fichas; las cuatro salidas del molde las cubren todas.

## 30.9.1 — 2026-08-22

**PARCHE** (la regla de accesibilidad dice con palabras lo que su lista ya exigía, y gana ejemplo; nada cambia en lo que se pide).

**La accesibilidad mínima se cumple entera o no se cumple, y ahora la regla lo dice.** La regla de accesibilidad enumeraba cuatro cosas (etiquetas, contraste, teclado, color) sin decir si eran cuatro exigencias o una sola, y su sello traía las dos lecturas escritas una debajo de la otra. El usuario eligió: es una, con la lista como su contenido. También gana el ejemplo que le faltaba, una pantalla con las etiquetas perfectas y el contraste ilegible.

**Y `12·PR3` no se deroga.** Estaba en la lista de derogaciones del pendiente [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), pero esa lista venía de cuando la regla no exigía nada propio; reescrita el 2026-08-18, hoy es la única que dice que un dato personal es sensible por defecto, sin esperar a que el proyecto lo declare. Se le mostró al usuario y decidió que queda. Con esto no queda ninguna de las 26 candidatas a partirse sin resolver.

## 30.9.0 — 2026-08-22

**MENOR** (diecisiete reglas de tres capítulos caben ya en su molde, y nacen dos anexos; nada cambia en lo que se exige).

**Ninguna regla del estándar se pasa ya del largo que ella misma fija.** El estándar le da cuatro líneas a cada regla, y quince reglas de los capítulos de datos, documentación y meta-reglas decían en el sello que cabían en cuatro líneas y medían hasta el doble. Dos de ellas no se podían recortar sin perder algo, porque su contenido era una tabla y una lista de pasos: esas dos ganaron **anexo**, la misma salida que el usuario aprobó para la nomenclatura de fases.

**El detalle.** Es la ronda de los capítulos `03`, `13` y `20` del pendiente [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nacen [la tabla canónica de trazabilidad](base/13-documentacion/tabla-de-trazabilidad.md), que sale del cuerpo de `DOC11`, y [el orden del desempate](base/20-meta-reglas/desempate.md), que sale del de `M6` con sus seis pasos intactos. Las otras quince se recortaron dejando lo que exigen; los porqués están en [notas/porques-recortados-al-molde.md](notas/porques-recortados-al-molde.md). Con esto `validar.py metareglas` no reporta ni una falla ni un aviso de largo.

## 30.8.3 — 2026-08-22

**PARCHE** (doce reglas del capítulo `02` dicen lo mismo en menos palabras; nada cambia en lo que se exige).

**Las reglas del flujo de trabajo ya caben en el molde que el estándar les da.** `F0`, `F8`, `F9`, `F10`, `F11`, `F14`, `F16`, `F17`, `F20`, `F22`, `F23` y `F26` pasaban de las cuatro líneas, algunas al doble, con un sello que decía que cabían. Lo que salió eran explicaciones y remisiones a detalles que ya viven en el capítulo o en otra regla; queda anotado en [notas/porques-recortados-al-molde.md](notas/porques-recortados-al-molde.md).

**El detalle.** Es la ronda del capítulo `02` del pendiente [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Las excepciones y los ejemplos no se tocaron, y las dependencias declaradas siguen igual. Con este capítulo los avisos de largo bajan de 30 a 18.

## 30.8.2 — 2026-08-22

**PARCHE** (tres reglas del capítulo `01` dicen lo mismo en menos palabras; nada cambia en lo que se exige).

**Las reglas de cómo responde el agente ahora caben en su propio molde.** `C5` («responde corto»), `C21` y `C22` pasaban de las cuatro líneas que el estándar le da a una regla, con un sello que decía que cabían. Se recortaron sin perder nada de lo que exigen; lo que salió eran explicaciones, y queda en [notas/porques-recortados-al-molde.md](notas/porques-recortados-al-molde.md).

**El detalle.** Pendiente [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), capítulo `01`. Las particiones que ese pendiente pedía acá (`C10`, `C14`, `C17`) ya se habían hecho el 2026-08-18, cuando nacieron `C24`, `C25` y `C26`: del `01` solo quedaba esta deuda de la fila 10.

## 30.8.1 — 2026-08-22

**PARCHE** (cuatro reglas del capítulo `00` dicen lo mismo en menos palabras; nada cambia en lo que se exige).

**Las reglas de cómo escribe el agente ahora cumplen lo que piden.** `ID5`, `ID7`, `ID8` e `ID9` exigen escribir corto y claro, y las cuatro pasaban del molde de cuatro líneas con un sello que decía que cabían. Se recortaron a lo que exigen; lo que salió eran explicaciones de por qué, y quedan en [notas/porques-recortados-al-molde.md](notas/porques-recortados-al-molde.md), que pasa a recoger todos los recortes (antes solo los de `18` y `19`). El glosario decía que el núcleo tiene seis reglas; tiene nueve desde la 24.0.0.

**El detalle.** Pendiente [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), capítulo `00`. Los sellos de las cuatro se vuelven a fechar con el cuerpo nuevo. Quedan 33 reglas en otros capítulos con la misma deuda de la fila 10, que siguen por capítulo.

## 30.8.0 — 2026-08-22

**MENOR** (las veintisiete reglas que estaban publicadas reprobando su propio checklist pasan a cumplirlo; ninguna cambia lo que exige, y el capítulo `02` gana un anexo).

**El cuerpo de reglas ya no tiene ninguna regla publicada en «no cumple».** Hasta hoy había veintisiete: los capítulos `18` y `19` enteros sin ejemplo, `C1`, `C15`, `C16`, `C18`, `S4` y `T4` pasadas de largo o con texto prestado, `DEP3` repitiendo a una regla derogada, `F12` con 1 898 caracteres de texto literal, y cuatro meta-reglas (`M2`, `M4`, `M7`, `M8`) reprobando por lo que otras reglas les contradecían. `20·M14` dice que sin CUMPLE una regla no se publica, y estaban publicadas. Ahora `validar.py metareglas` da cero fallas.

**El detalle.** Pendiente [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), primera ronda. Los catorce de `18` y `19` ganan su ejemplo INCORRECTO/CORRECTO y cinco (`DP8`, `OB1`, `OB3`, `OB5`, `OB6`) se recortan al molde; sus porqués quedan en [notas/porques-recortados-al-molde.md](notas/porques-recortados-al-molde.md). `C1`, `C15`, `C16`, `C18`, `S4` y `T4` se reescriben en cuatro líneas y declaran su dependencia en la forma de `M7`; el bloque «Encadenamiento» que usaban `C15`, `C16`, `C18` y `D8` desaparece. `DEP3` declara que deroga a `04·S7`. El texto literal del usuario que era el cuerpo de `F12` se conserva entero como anexo [base/02-flujo-de-trabajo/nomenclatura-de-fases.md](base/02-flujo-de-trabajo/nomenclatura-de-fases.md); la regla queda con una exigencia y los `F12.N` son puntos del anexo, no identificadores de regla, así que `M4` vuelve a cumplirse. Quedan para la segunda ronda las veintiséis reglas que llevan más de una exigencia y se parten (MAYOR), decididas por el usuario.

## 30.7.0 — 2026-08-22

**MENOR** (cada capítulo de `base/` gana una línea que dice quién es dueño de su texto; ninguna regla cambia de exigencia).

**Cada capítulo del estándar tiene ahora una historia de usuario que escribe su texto.** Hasta hoy, diecinueve de los veintiún capítulos medidos no tenían ninguna: el cuerpo de reglas se había escrito sin recorrer la cadena que él mismo exige, y a la pregunta «¿de dónde salió esta regla?» la respuesta era «de que a alguien le pareció». El usuario eligió una historia por capítulo, y nacieron veintiuna (del `02` al `22`); el `00` y el `01` ya tenían la suya. Cada capítulo lo declara en su cabecera, para que se lea desde el capítulo mismo.

**El detalle.** Pendiente [60](pendientes/hecho/cada-capitulo-tiene-su-historia.md). Nacen HU-015 a HU-035 en [EP-001](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md), cada una dueña del texto de su capítulo con dos criterios: el capítulo la nombra, y un cambio del capítulo tiene dónde bajarse (`02·F23`). Los 23 archivos de cabecera de `base/` llevan la línea «Historia dueña del texto». Las fases de retrodocumentación de cada capítulo quedan por ejecutar y el inventario de HU las cuenta como incompletas, que es lo correcto. Es el mismo hueco que el 47 tenía un piso más abajo y el 56 en la cabeza de la cadena; con los tres cerrados, Cimiento ya puede recorrer su propia cadena de arriba abajo.

## 30.6.1 — 2026-08-22

**PARCHE** (documentación del propio estándar; nada cambia en lo que se exige).

**Cimiento ya tiene su planteamiento y su inventario.** Exigía a todos un planteamiento y un inventario de funcionalidades, y no tenía los suyos: su revisión de instalación reprobaba la cadena en casa. Ahora dice, en lenguaje de negocio, qué problema resuelve (sesiones con un agente que reinventan, olvidan y arriesgan), para quién, qué queda fuera y cómo se mide el éxito; y lista todo lo que es, lo que le falta y lo que está por confirmar.

**El detalle.** Pendiente [56](pendientes/hecho/el-estandar-tiene-su-planteamiento.md). Nacen [`prompts/cimiento-planteamiento.md`](prompts/cimiento-planteamiento.md) (las siete épicas quedan enlazadas a él) y [`prompts/cimiento-inventario-funcionalidades.md`](prompts/cimiento-inventario-funcionalidades.md), en revisión del usuario como manda `02·F26`: 22 ítems existentes, 4 por construir (vistas consolidadas, `.docx`, veredicto único, medición de todos los proyectos desde la interfaz) y 3 por confirmar. Lo escribió el agente con lo que el proyecto ya decía, por instrucción del usuario.

## 30.6.0 — 2026-08-22

**MENOR** (dos validadores dejan de dar falsos veredictos; ningún proyecto tiene que cambiar nada).

**Dos mentiras de los validadores, corregidas.** La revisión de instalación decía que faltaban los dieciséis enganches de un proyecto que los tenía bien puestos, solo porque se la corría con la letra de la unidad en minúscula; y el cierre de pendientes reescribía un enlace hacia una ruta con espacio dejándole el espacio literal, con lo que el enlace dejaba de abrir y, peor, ningún validador volvía a verlo. Las dos las reportaron proyectos instalados (`matematica` y `shopnest-mesa`): el estándar se vigila desde afuera.

**El detalle.** Pendientes [72](pendientes/hecho/el-checklist-compara-rutas-no-texto.md) y [71](pendientes/hecho/el-espacio-vuelve-codificado.md). El checklist compara normalizado (`os.path.normcase` en los dos lados; apuntar a otro estándar sigue siendo falta). `cerrar.py` devuelve el espacio como `%20`, y `validar.py estandar` avisa de todo enlace cuyo destino lleve un espacio literal: al estrenarlo encontró nueve en el propio repositorio, invisibles hasta hoy, corregidos en la misma ronda. Cuatro pruebas nuevas.

## 30.5.0 — 2026-08-22

**MENOR** (el instalador cambia cómo da de alta un proyecto; un arreglo de pérdida de datos en la interfaz; `base/` y `plantillas/` no cambian de exigencia).

**El registro de proyectos ya no se vacía solo, y el instalador da de alta directo en Cimiento.** Un proyecto instalado reportó que la lista de proyectos quedaba vacía de la nada y su revisión de instalación lo reprobaba en cada mensaje. La causa estaba en casa: las pruebas de la interfaz exportaban su base de pruebas, vacía, sobre el archivo real. Tres correcciones: ninguna prueba toca ya el registro real; el exportador se niega a escribir cero filas sobre un archivo que tenía filas (y la pantalla lo dice en vez de borrar); y el alta que hace el instalador entra al registro de Cimiento con `manage.py registrar`, regenerando el archivo, en vez de anotar una fila a mano — con eso cierra también la deuda que quedó al cerrar el 75.

**El detalle.** Es el [pendiente 76](pendientes/hecho/el-registro-no-se-vacia-y-el-alta-entra-a-cimiento.md), reportado por `gestion de servicios tecnologicos` y cerrado el mismo día: `core.exportar()` con `RegistroVacio`, `core.registrar()`, el comando `registrar`, `_registrar_en_cimiento` en [`instalar.py`](validadores/instalar.py) (solo contra el registro real: una prueba que redirija el `.md` nunca llega a la base), 10 pruebas de la interfaz en verde y el registro real con sus 10 proyectos después de correrlas. La lección quedó en la señal S-019: toda prueba que escriba, escribe en temporal; todo exportador se niega a vaciar lo que tenía contenido.

## 30.4.0 — 2026-08-22

**MENOR** (cambia la base de datos de la interfaz local; `base/` y `plantillas/` no cambian de exigencia).

**La base de Cimiento es ahora MariaDB, en el puerto 3307.** El registro de proyectos dejó la base de archivo que Django trae por defecto y pasó a un servidor de base de datos de verdad, como cualquier proyecto que el estándar acompaña. Las credenciales viven solo en el `.env` de la interfaz, que no se versiona; el código no conoce ninguna. Lo decidió el usuario: «la DB (Cimiento) debe ser en MariaDB puerto 3307».

**El detalle.** `config/settings/base.py` lee la conexión de las variables `DB_*` del `.env` (listadas sin valor en `.env.example`); nace la base `cimiento` (utf8mb4) y el driver `mysqlclient` entra en `requirements/` con su versión exacta en el lock. Los 10 proyectos se importaron a MariaDB y las 7 pruebas de la interfaz corren contra ella. El archivo `_visor.sqlite3` deja de existir.

## 30.3.0 — 2026-08-21

**MENOR** (la interfaz local gana el registro de proyectos y adopta la estructura estándar; `base/` y `plantillas/` no cambian de exigencia, así que nadie migra nada).

**Los proyectos se administran ahora desde Cimiento, no desde un archivo escrito a mano.** La interfaz tiene una pantalla nueva, Proyectos: registrar, editar, dar de baja (sin borrar la historia) y **medir** — el expediente del ciclo de cada proyecto, calculado en el momento. La lista que antes se editaba a mano (`plantillas/proyectos.md`) pasó a ser un archivo **generado** desde el registro; el instalador y los avisos de cierre lo siguen leyendo igual, y lo que el instalador anote se sube al registro con un clic. Era la dirección que el usuario fijó: «los proyectos deben registrarse, configurarse, consultarse y administrarse desde la propia interfaz».

Y la interfaz misma quedó cumpliendo la estructura que el estándar le exige a cualquier proyecto Django: entorno propio, dependencias declaradas y congeladas (`requirements/` con lock), configuración partida en común y local con sus variables en `.env.example`, las plantillas de todo el proyecto en su carpeta, un paquete con un módulo por carpeta y cada módulo completo (modelos, pruebas, migraciones), y **ningún tercero copiado al repositorio**: Bootstrap, AdminLTE, los iconos y Chart.js se descargan una vez, pineados por versión y huella SHA-256, y el visor sigue funcionando sin internet después de instalado.

**El detalle.** Es el [pendiente 75](pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md), cerrado el mismo día en que nació. Nace `interfaz/proyectos/` (modelo, pantallas, importar/exportar, 7 pruebas junto a las de humo del visor) e `interfaz/descargar_estaticos.py`; `interfaz/requirements/` reemplaza al `requirements.txt` plano y `config/settings/` al `settings.py` único. Los 10 proyectos reales quedaron en el registro con la ida y vuelta al `.md` verificada. Deuda declarada en el cierre: el instalador aún anota sus altas en el `.md` generado (la interfaz las importa); escribirlas directo al registro es mejora futura.

## 30.2.0 — 2026-08-21

**MENOR** (aditivo: un lector nuevo; nadie tiene que cambiar nada).

**Ahora se puede preguntar, con una orden, si un proyecto tiene su expediente completo.** `validar.py expediente` recorre un proyecto y responde lo que antes exigía abrir carpeta por carpeta: qué entregables del ciclo existen (y dónde), cuáles faltan, cuántos espacios por llenar le quedan a cada uno y cuál declaró que no aplica con su porqué. Informa y no detiene: la lista se mira y las decisiones las toma una persona.

Estrenó midiendo un proyecto real: de los trece entregables del expediente tenía tres (el planteamiento, el inventario de funcionalidades y el modelo de datos), y la cadena de ejecución completa: tres épicas, veintiuna historias, veinticinco fases con plan. Ese número — «3 de 13» — es la primera vez que el cumplimiento del expediente se ve de un vistazo.

**El detalle.** Nace [`validadores/expediente.py`](validadores/expediente.py) con seis casos de prueba: encuentra cada entregable por su nombre viva donde viva (con o sin prefijo), distingue completo, en llenado (contando los `«…»` de `13·DOC19`) y no-aplica, y cuenta las estaciones 03 a 11 por su estructura canónica. Lo que falta del frente: el generador de las vistas consolidadas (SRS, matriz, defectos, arquitectura) y el `.docx`, cuya casa natural es la interfaz del [pendiente 75](pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md) — quedó dimensionado en [notas/entregables-del-ciclo-de-vida.md](notas/entregables-del-ciclo-de-vida.md).

## 30.1.0 — 2026-08-21

**MENOR** (aditivo: once moldes nuevos; nadie al día tiene que hacer nada hoy — los usan los trabajos que vienen).

**El expediente del proyecto quedó completo.** A la carpeta del ciclo le entraron los entregables que la ingeniería de software exige y que faltaban: el estudio de factibilidad, el acta de constitución con su plan, el modelo de datos con su diccionario, el diseño de interfaz, el contrato de la API, el manual de instalación, el manual técnico y de operación, las notas de versión, el acta de entrega, la bitácora de operación y el plan de mantenimiento. Cada uno se alimenta en su etapa mientras el trabajo avanza; cuando el proyecto está listo, generar los documentos finales es darle forma a lo que ya está escrito.

Rige la decisión del usuario registrada en la 30.0.0: el ciclo no hace excepciones — todos existen en todo proyecto, la envergadura ajusta la profundidad, y el que no tenga materia declara «No aplica porque...» en vez de omitirse.

**El detalle.** Nacen los moldes 12 a 22 en [`plantillas/ciclo-vida-proyectos/`](plantillas/ciclo-vida-proyectos/README.md); su README explica a qué estación acompaña cada uno y por qué dos entregables no llevan molde a propósito: el manual de usuario **es** el inventario de funcionalidades madurado, y el SRS consolidado, la matriz de trazabilidad, el registro de defectos y el documento de arquitectura son vistas que un generador armará desde lo ya escrito (trabajo dimensionado en [notas/entregables-del-ciclo-de-vida.md](notas/entregables-del-ciclo-de-vida.md), junto al generador `.docx`).

## 30.0.0 — 2026-08-21

**MAYOR** ⚠ obliga a migrar: los moldes del ciclo cambiaron de ruta; un proyecto al día vuelve a correr la instalación y el aviso de desfase se lo dice en su primer mensaje. No quedan redirecciones: las rutas viejas ya no existen.

**Los documentos que todo desarrollo recorre tienen ahora su propia carpeta, y se lee en orden.** Los once moldes del camino obligatorio (el planteamiento, el inventario de funcionalidades, la épica, la historia, la fase, la especificación, los dos planes, el resultado de pruebas, el estado de la fase y el cierre) salieron de la raíz de plantillas, donde estaban revueltos con moldes de configuración y de operación, y viven en una carpeta que los numera por estación: abrirla es ver el ciclo completo, del 01 al 11.

Lo pidió el usuario con una decisión de fondo que quedó registrada: **el ciclo de vida no hace excepciones** — todos sus entregables existen en todo proyecto sin importar la envergadura; lo que la envergadura ajusta es la profundidad, y el que no tenga materia se llena con «No aplica porque...» en vez de omitirse en silencio.

**El detalle.** Nace [`plantillas/ciclo-vida-proyectos/`](plantillas/ciclo-vida-proyectos/README.md) con su README que recorre las once estaciones, cada una con su puerta y su regla. Se movieron y renumeraron los once moldes (la carpeta `planes/` desaparece dentro del ciclo: son las estaciones 07 a 09); el andamio, el instalador y los validadores apuntan a las rutas nuevas, y los 137 documentos que las citaban quedaron al día. La lista canónica de entregables del ciclo (IEEE/ISO), con lo que aún no tiene molde, quedó en [notas/entregables-del-ciclo-de-vida.md](notas/entregables-del-ciclo-de-vida.md) como material del trabajo que sigue: los 13 moldes faltantes y el generador de documentos finales.

## 29.0.0 — 2026-08-21

**MAYOR** ⚠ obliga a migrar: en el próximo encargo de cualquier proyecto al día, las épicas no se derivan hasta que el usuario apruebe el inventario de funcionalidades. Lo ya derivado no se reabre.

**El alcance lo confirma el usuario, no lo asume el agente.** Toda propuesta viene ahora acompañada de un inventario con **todas** las funcionalidades de lo que se va a desarrollar, cada una con su estado (existe, parcial, por construir, por confirmar) y lo no decidido escrito como pregunta. Hasta que el usuario no lo aprueba, no se derivan épicas; y cada épica dice qué ítems del inventario cubre. El inventario no se bota al arrancar: madura con el sistema hasta convertirse en el manual del producto.

Se escribió porque el daño ya ocurrió: en un proyecto real el agente escribió el planteamiento asumiendo el techo del alcance, de ahí salieron tres épicas y 21 historias, y la corrección del usuario llegó seis días después, con todo eso escrito encima. Ninguna regla lo habría preguntado antes. El usuario lo pidió explícito: «la propuesta debe venir acompañada del inventario (...) porque eso es lo que da el punto de partida a las épicas».

**El detalle.** Nace [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) —*el inventario de funcionalidades aprobado es la puerta de las épicas*, que extiende a [`F2`](base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md): la misma puerta, una estación antes— y el molde [`plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), generalizado del inventario real de `shopnest-mesa`. Es el [pendiente 74](pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md), bajado como la fase A de [EP-003 · HU-011](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-011-el-inventario-de-funcionalidades/HU-011-el-inventario-de-funcionalidades.md) con sus tres criterios en Cumple — incluido el veredicto de por qué la conducta del capítulo `01` no cubría este caso. `F26` queda registrada sin validador todavía, con las tres preguntas de [`M19`](base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) respondidas: primero que la puerta demuestre servir a mano.

## 28.2.0 — 2026-08-21

**MENOR** (aditivo: un documento nuevo que viaja con las reglas; nadie tiene que cambiar nada).

**Las reglas ganan su puerta de entrada.** Quien llega a un proyecto sin conocer el estándar tiene ahora un documento que le explica, en lenguaje llano, por qué se trabaja así: los diez pasos que sigue cualquier desarrollo profesional (de entender la necesidad a mantener lo entregado) y las nueve cualidades que un producto necesita para ponerse en producción (seguridad, respaldos probados, pruebas, despliegue reversible y las demás). Cada punto lleva el enlace a la regla o al capítulo que lo exige: la guía explica, la exigencia sigue viviendo en la norma.

La escribió el usuario con el agente en un proyecto real, y guardada allá tenía el defecto de siempre: doctrina transversal en un solo proyecto, invisible para los demás y condenada a divergir si cada uno escribe la suya.

**El detalle.** Nace [`base/guia-de-entrada.md`](base/guia-de-entrada.md), nombrada desde el [README de `base/`](base/README.md) y el mapa del sitio; viaja a los herederos con la carpeta, y al arranque solo le suma su línea de índice (102 bytes medidos; el contenido queda fuera y el consumo va en 69,9 de 90 KB). Es el [pendiente 73](pendientes/hecho/la-guia-de-entrada-es-del-estandar.md), reportado por `matematica`, bajado como la fase A de [EP-001 · HU-014](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-014-la-guia-de-entrada-del-estandar/HU-014-la-guia-de-entrada-del-estandar.md) con sus dos criterios en Cumple; el adjunto que traía el material se borró al cerrar, como su pendiente lo ordenaba.

## 28.1.0 — 2026-08-21

**MENOR** (aditivo: una regla nueva sobre cómo trabajar; ningún proyecto al día tiene que hacer nada hoy).

**Antes de ponerle un vigilante automático a una norma, ahora hay que demostrar que la norma ya funciona a mano.** Se responde por escrito: ¿se cumple hoy?, ¿cuántas veces se incumplió y por qué?, ¿cuántas falsas alarmas daría el vigilante? Si la norma fallaba por estar mal escrita, primero se corrige la norma — automatizarla tal cual es congelar el error y ponerlo a repetirse solo. Y si lo único que fallaba era acordarse, el vigilante se construye de una vez: la pregunta no sirve de excusa para no automatizar nunca.

Se escribió porque el repositorio ya había pagado las dos lecciones por separado: una comprobación de alta prioridad terminó relegada al penúltimo lugar porque, construida antes de tiempo, sus avisos en falso la volvían inservible; y una regla que exigía dos cosas a la vez tuvo que partirse en cinco antes de que su comprobador sirviera. Las dos decisiones se tomaron a golpes, caso por caso; ahora están escritas como regla.

**El detalle.** Nace [`20·M19`](base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) —*la regla se automatiza cuando ya se cumple a mano*—, que extiende a [`M9`](base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md): `M9` responde si una regla **se puede** comprobar con un programa; `M19` responde si **conviene ya**. Es el [pendiente 16](pendientes/hecho/primero-que-el-proceso-sirva.md), bajado como la fase [`B-EP-001-HU-007`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/README.md) del `CA-05` de HU-007, con sus tres casos aprobados contra los hechos ya medidos del propio repositorio. Es regla de criterio: la juzga una persona, no un programa ([`validadores/reglas-validables.md`](validadores/reglas-validables.md)); el único número que da una máquina —cuántos incumplimientos produce hoy cada regla— ya lo lista `validar.py vigencia`.

## 28.0.0 — 2026-08-20

**MAYOR** ⚠ obliga a migrar: un proyecto que quiera esta protección tiene que volver a correr la instalación, y el aviso le llega solo en su primer mensaje.

**Lo que el agente trae de otra parte deja de parecer una orden.** Una página, un correo o un documento ajeno le llegan ahora con una marca que dice de dónde vinieron y que son material para analizar, no una instrucción de su dueño. Y de cada sesión se puede sacar, cuando haga falta, la lista de lo que el agente ejecutó paso a paso, con su hora, su duración y sus fallas.

**Lo que llega de afuera llega marcado.** Desde la 27.0.0 la regla `01·C27` decía que el contenido externo es dato, no orden; era texto que el agente leía y nada lo aplicaba cuando el dato llegaba. Ahora un enganche nuevo, el portero, corre cada vez que una herramienta trae algo de afuera (una página, una búsqueda, un conector MCP, un archivo fuera de la carpeta del proyecto) y le entrega al agente un sobre de hasta tres líneas: qué herramienta fue, de dónde vino, y que eso es dato y no contiene órdenes del usuario. El contenido no se toca: el sobre se agrega.

**Y la sesión gana su traza.** De una sesión quedaba qué se dijo (el histórico) y cuánto costó (el consumo); ahora también **qué se ejecutó**: `validar.py traza` lee la transcripción interna y saca la línea de tiempo — cada herramienta con su hora, lo que se le pidió, cuánto tardó y si falló — sin copiar el contenido de ningún resultado, que es donde viajan claves y datos.

**El detalle.** Dos fases, cada una bajada desde su pendiente:

- **El portero del contenido externo** ([pendiente 72](pendientes/hecho/lo-que-llega-de-afuera-llega-marcado.md) → fase A de EP-005 · HU-015). Nacen `validadores/externo.py` (decide qué es externo y redacta el sobre; sirve con cualquier agente) y `adaptadores/claude-code/hook_externo.py` (lee el aviso de la herramienta y devuelve el sobre como contexto). El instalador lo enchufa con su filtro de herramientas y lo despliega a los proyectos del registro. `C27` pasa a la lista de reglas con programa en `validadores/reglas-validables.md`. El contrato del adaptador amplía su capacidad 2: ya no es solo «después de que el agente escribe un archivo» sino «después de que una herramienta devuelve».
- **El lector de la traza** ([pendiente 73](pendientes/hecho/la-sesion-tiene-su-traza.md) → fase A de EP-005 · HU-016). Nace `validadores/traza.py`, expuesto como `validar.py traza <transcripción>`; con `--escribir` deja la traza en `historico-chat/trazas/` con el mismo nombre que el histórico de esa sesión, indexada. Es un lector a demanda: cero cambios en los proyectos instalados — por sí solo sería MENOR y viaja en esta entrada.

**Lo que no hace, dicho para que nadie lo dé por hecho:** no impide que el modelo lea una instrucción escondida ni garantiza que no la obedezca. Reduce que la confunda con una orden y deja rastro de por dónde entró. Lo que detiene una acción sigue siendo `00·N1`.

**Por qué el sobre se agrega y no reemplaza el resultado.** Agregar contexto está documentado y no depende de la forma en que cada herramienta devuelve; reemplazar el resultado existe, pero la documentación no dice qué herramientas lo aceptan. Se eligió lo que se puede probar.

## 27.2.0 — 2026-08-20

**MENOR** (aditivo: un molde nuevo, dos modos nuevos del andamio, un programa automático nuevo y dos arreglos; los proyectos instalados reciben el aviso de reinstalar).

**Lo mecánico de bajar un defecto por la cadena lo hace ahora un programa.** Cuando hace falta abrir una historia o anotar un pendiente, el andamio deja el archivo y las filas de los índices puestas; cuando un trabajo termina con sus pruebas, el resultado se copia solo a donde el estándar manda repetirlo; y lo que el andamio y los programas del histórico escribían con enlaces mal formados, ya nace bien.

**El detalle.** Cuatro fases, cada una bajada desde su pendiente, y las cuatro salidas de preguntar cómo gastar menos:

- **El andamio no deja enlaces rotos** ([pendiente 67](pendientes/hecho/el-andamio-no-deja-enlaces-rotos.md) → fase C de EP-004 · HU-005). Traslada, al copiar cada plantilla, los enlaces que llegan a la raíz y el marcador de la ruta del estándar. Las siete fases levantadas hoy antes del arreglo se corrigieron a mano; las que vengan nacen bien.
- **La corrida entera vuelve a verde** ([pendiente 68](pendientes/hecho/la-corrida-entera-vuelve-a-verde.md) → fase C de EP-004 · HU-008). `historico.py` y `resumen.py` escriben el texto del enlace con la ruta desde la raíz (`13·DOC14`); se corrigieron los cuatro ya escritos y un resumen del 19 sin la `H-` del molde.
- **El andamio levanta la historia y el pendiente** ([pendiente 69](pendientes/hecho/el-andamio-levanta-la-historia-y-el-pendiente.md) → fase B de EP-007 · HU-003). Dos modos nuevos, `hu` y `pendiente`, con las filas de los índices en los dos sentidos. Nace [`plantillas/pendiente.md`](plantillas/pendiente.md), el molde del pendiente propio del estándar.
- **El veredicto se copia solo** ([pendiente 70](pendientes/hecho/el-veredicto-se-copia-solo.md) → fase C de EP-005 · HU-003). Un enganche nuevo (`hook_veredicto.py`, con su módulo agnóstico `validadores/veredicto.py`) lee el §6 del resultado y lo deja en la fila de la historia y en los dos README; `cerrar.py` deja la fila del backlog en forma de hecho. El `estado-fase.md` sigue siendo del agente.

**Se estrenó sobre sí mismo:** el cierre de estas cuatro fases lo propagó el programa nuevo, y las filas de los cuatro pendientes las dejó `cerrar.py`.

**De paso, y lo atrapó el trinquete de marcas al guardar:** la regla `01·C27` tenía dos rayas en el cuerpo y se cambiaron por paréntesis. No cambia qué exige.

## 27.1.0 — 2026-08-20

**MENOR** (aditivo: dos programas automáticos nuevos y un arreglo del arranque; los proyectos instalados reciben el aviso de reinstalar en su primer mensaje).

**Al abrir este repositorio, el arranque no le entregaba al agente sus propias reglas; ahora sí. Y el agente recibe dos avisos que antes no tenía: cuando avanza un trabajo sin anotar en qué punto va, y cada millón de fichas que la conversación gasta, antes de que termine.** Las tres cosas salieron de comparar el núcleo del agente con la nota de arquitectura y de preguntar por qué una mañana entera se trabajó sin las reglas del flujo cargadas.

**El detalle.** Tres fases, cada una bajada por la cadena desde su pendiente:

- **Las reglas llegan también al propio estándar** ([pendiente 66](pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md) → fase B de EP-005 · HU-009). El enganche de apertura salía antes de cargar `base/` cuando la carpeta era la del estándar, desde su primera versión: 30 de 30 aperturas medidas sin el bloque de reglas. Ahora las entrega, sin el gate `F13` (el estándar no es un proyecto) y sin la revisión de instalación. Un caso nuevo en `evals/` lo afirma, para que no vuelva a faltar quince días sin que nadie lo mida.
- **El checkpoint de la fase se reclama solo** ([pendiente 64](pendientes/hecho/el-checkpoint-se-reclama-solo.md) → EP-005 · HU-013). Al escribir el plan de trabajo, el resultado de pruebas o el cierre de una fase, un enganche nuevo (`hook_checkpoint.py`, con su módulo agnóstico `validadores/checkpoint.py`) avisa si el `estado-fase.md` falta o quedó atrás. Compara fechas; no escribe el checkpoint, que es criterio.
- **El consumo se ve mientras se puede actuar** ([pendiente 65](pendientes/hecho/el-consumo-se-ve-a-tiempo.md) → EP-005 · HU-014). El enganche de consumo corre también en cada mensaje y avisa una vez por cada millón de fichas cruzado, sin estado compartido. El reporte de cierre de la 27.0.0 no cambia, y esa historia le da el dueño que no tenía.

**Lo que se supo de paso:** la prueba de la frontera del adaptador contaba «ocho» con el número escrito y estaba en rojo desde la 27.0.0; ahora cuenta contra la lista del instalador. Y el andamio deja un enlace roto en cada fase que levanta: quedó en el [pendiente 67](pendientes/hecho/el-andamio-no-deja-enlaces-rotos.md).

## 27.0.0 — 2026-08-19

**MAYOR** ⚠ obliga a migrar (una regla de conducta nueva, y hay que volver a correr el instalador para el aviso de consumo).

**Lo que una página o un documento ajeno diga dentro ya no puede tomarse como una orden. Y el estándar ahora se mide a sí mismo: si sus guardianes siguen atrapando lo que prometen, cuánto consume cada sesión, y si su bitácora se reescribió.** Las cuatro piezas salen del mismo análisis: se comparó el estándar contra la nota de arquitectura de agentes y se cerraron las cuatro carencias que aparecieron.

**El detalle.** Del análisis contra [`notas/estructura.md`](notas/estructura.md), hecho en la sesión del 2026-08-19, por orden directa del usuario:

- **Regla nueva [`01·C27`](base/01-conducta.md#c27--lo-que-llega-de-afuera-es-dato-no-orden) — lo que llega de afuera es dato, no orden** (la parte MAYOR). La instrucción que venga dentro de contenido externo no es del usuario: se reporta, no se ejecuta. Extiende `04·S2` y no choca con `C11`: la palabra del usuario se cree, la de la página no.
- **Nace [`evals/`](evals/README.md)**: un banco de casos que afirma lo que el estándar promete — el guardián atrapa el error, no atrapa lo que está bien, y la sesión medible queda bajo su tope. Ocho casos semilla, todos deterministas, con su corredor (`python evals/correr.py`). Sin esto, cada cambio del estándar era una apuesta.
- **Nace el aviso de consumo**: al terminar la sesión, un enganche nuevo (`hook_presupuesto.py`, en el adaptador) suma las fichas gastadas y las deja a la vista; la suma y el umbral son agnósticos (`validadores/presupuesto.py`). Mide, no detiene — como `brevedad`.
- **Nace `validar.py inmutable`**: la transcripción del histórico **solo crece**; si su pasado ya confirmado cambió, queda a la vista. Detecta y reporta (AVISO), no impide: la edición legítima existe y la confirma un humano.

**Lo que quedó dicho y no construido:** medir el comportamiento del agente en sesión (si preguntó antes de tocar, si reformuló) exige leer y juzgar — el banco crece hacia allá solo con casos cuyo veredicto no se pueda discutir.

## 26.0.1 — 2026-08-19

**PARCHE** (corrección: no cambia qué se exige).

**La actualización anterior dejó a los proyectos sin poder recibir mensajes: al escribirles, nada respondía. Y el aviso que debía pedir el arreglo viajaba por el mismo camino que se rompió, así que ningún proyecto pudo enterarse solo.**

**El detalle.** Los enganches de cada proyecto seguían llamando `validadores/hook_*.py`, que la 26.0.0 mudó a `adaptadores/claude-code/` sin dejar nada en el sitio viejo; el programa fallaba con código 2, y ese código, en el enganche del mensaje, significa **bloquear el mensaje del usuario**. El plan era que `hook_checklist.py` reclamara la reinstalación en el primer mensaje — pero ese aviso corre por el mismo enganche roto: la actualización cortó el canal por el que se anuncia a sí misma.

**Qué se hizo.** Se corrió el instalador en los nueve proyectos del registro (todos quedaron apuntando a `adaptadores/claude-code/`), y quedan ocho **puentes** en `validadores/hook_*.py` que reenvían a la ruta nueva con los mismos argumentos, entrada y código de salida. Una instalación rezagada —otra máquina, un proyecto fuera del registro— ya no se bloquea: funciona por el puente hasta que el instalador le reescriba la ruta.

**La lección, para el próximo movimiento:** un archivo que los proyectos llaman por ruta absoluta no se muda sin dejar puente, porque el aviso de desfase viaja por el mismo canal que se rompe.

## 26.0.0 — 2026-08-19

**MAYOR** ⚠ obliga a migrar (todo proyecto instalado tiene que volver a correr el instalador).

**Las reglas son texto y sirven con cualquier herramienta. Lo que las hace cumplir solas, no.** Eran ocho programas que existen porque **esta** herramienta los llama, mezclados con los cincuenta y un programas que funcionarían con cualquiera. Por eso nadie sabía de qué tamaño era la atadura.

Ahora están separados: `adaptadores/claude-code/` es lo que habría que reescribir el día que la herramienta cambie, y `validadores/` es lo que se queda entero.

**Qué hay que hacer.** Volver a correr el instalador en cada proyecto. El aviso de instalación lo reclama solo en el primer mensaje de la siguiente sesión: los avisos automáticos quedaron apuntando a la ubicación vieja, y eso **no falla en silencio** — se reporta.

**El detalle.** Del [pendiente 15](pendientes/hecho/el-estandar-depende-de-una-sola-herramienta.md), sus puntos 2 y 3. Nace también [`adaptadores/contrato.md`](adaptadores/contrato.md).

**El contrato dice qué necesita el estándar de cualquier agente**, sin nombrar ninguno: poder poner texto al arrancar, poder correr un programa cuando se escribe un archivo, cuando el usuario manda un mensaje y cuando el agente termina, y poder cortar un guardado. Cinco cosas.

**Y dice también lo que NO necesita, que es la mitad que se olvida:** no necesita cambiar la respuesta del agente, ni leer cómo razona, ni acceso a la red, ni que la herramienta guarde nada. Todo lo que se guarda son archivos del repositorio. Sin esa lista, quien evalúe una herramienta nueva termina exigiendo de más y descarta opciones que servían.

**Ya se sabe cuánto costaría el cambio, que era el punto:** ocho programas a reescribir, cincuenta y uno que se quedan igual, y ninguna regla que tocar.

**La mudanza pudo dejar la atadura fuera del recuento, y eso habría sido peor que no moverla.** Mirando una sola carpeta, el mapa habría dicho «diez de cincuenta y uno» y habría sonado a mejora, cuando lo único que hubo fue un cambio de sitio. Ahora mira las dos.

**No se hicieron atajos.** Ninguno de los tres criterios de la historia cubría mover código ni escribir el contrato: los tres hablaban del mapa. Se escribieron los dos que faltaban antes de tocar nada.

## 25.2.0 — 2026-08-19

**MENOR** (una lista más para mirar; nada nuevo que cumplir).

**Una regla equivocada se comporta exactamente igual que una correcta.** No se rompe nada: sigue ahí, sigue pasando su revisión de forma, y se sigue obedeciendo. Lo que cambió no fue la regla: fue el mundo que describía.

Ahora se puede preguntar **qué reglas llevan más tiempo sin que nadie se pregunte si todavía sirven**.

**El detalle.** Del [pendiente 14](pendientes/hecho/las-reglas-no-tienen-fecha-de-revision.md). Nace [`validadores/vigencia.py`](validadores/vigencia.py) y las tres preguntas de la revisión quedan escritas en [`base/20-meta-reglas/revision-de-vigencia.md`](base/20-meta-reglas/revision-de-vigencia.md).

**Son dos fechas distintas, y confundirlas era el problema.** El sello que cada regla ya traía dice *«vale mientras el texto de arriba no cambie»*: responde por la forma. La fecha nueva responde por otra cosa — que alguien volvió a preguntarse si el problema que la regla evita todavía existe.

**No hay umbral, y es una decisión.** Un umbral inventado produce una alarma que se aprende a ignorar. La lista se ordena y se muestra; cada cuánto conviene revisar se decide después de mirarla, no antes de tenerla. Por eso nunca detiene nada.

**Al lado de cada regla va cuántos incumplimientos produce hoy, y se lee en las dos direcciones.** Una regla vieja que falla todo el tiempo se revisa primero. Una que **no ha fallado nunca** se mira por el motivo contrario: puede que ya nadie la esté aplicando.

**La fecha arranca ausente en las 245, a propósito.** Ponérsela de una vez a todas habría sido escribir 245 fechas que no responden por ninguna revisión, que es justo el sello vacío que esto viene a evitar.

**Y pedir la lista destapó siete reglas sin sello:** `F4.1` a `F4.5`, `F6` y `F7` nunca recibieron su revisión de forma. Nacieron de partir reglas más grandes y el paso se saltó.

## 25.1.0 — 2026-08-19

**MENOR** (un capítulo opcional más; quien no construya con modelos no cambia nada).

**Un programa corriente se rompe y avisa. Uno que decide con un modelo puede dejar de acertar sin que nada se rompa:** el código igual, las pruebas en verde, ningún error en los registros — y las respuestas ya no sirven, porque cambió la realidad de la que se aprendieron.

Nace el capítulo opcional `22`, para los proyectos que entrenan un modelo, llaman al de un tercero, o dejan que una respuesta automática entre al flujo del negocio.

**El detalle.** Del [pendiente 12](pendientes/hecho/patron-ia.md), con material del diplomado del usuario. Nueve reglas en [`base/22-sistemas-que-aprenden-de-datos.md`](base/22-sistemas-que-aprenden-de-datos.md) y la [ficha del modelo](plantillas/ficha-modelo.md). Se enciende como los demás opcionales: una línea en el `CLAUDE.md` del proyecto.

**Lo que exige, en corto.** Que exista un inventario de qué modelos hay corriendo, antes que cualquier otra cosa. Que cada uno tenga a cargo **una persona con nombre** — un área no lee un aviso ni decide apagar nada. Que el control se gradúe por lo que la decisión puede dañar. Que **sugerir y ejecutar se autoricen por separado**, aunque sea el mismo modelo. Que uno que sigue aprendiendo se vuelva a revisar en un plazo escrito. Que se vigile si **sigue acertando**, no solo si responde. Que se diga de dónde salieron los datos y qué permiten. Que se escriba qué medida se le pidió perseguir y por qué esa. Y que apagarlo deje escrito qué queda decidiendo en su lugar.

**Pidió el número `21` y le tocó el `22`:** el `21` se lo llevó la automatización de procesos hace un día.

**No se le hizo plantilla propia al registro de decisiones.** Aprobar un modelo es una decisión de arquitectura y para eso ya está el `ADR`; un documento más habría sido el mismo contenido con otro nombre.

**Y registrar las letras del capítulo nuevo destapó que faltaban las del anterior.** Las ocho reglas del `21` venían incumpliendo el molde desde que nacieron. Con las dos filas puestas, los incumplimientos del capítulo de meta-reglas bajaron de 35 a 27.

## 25.0.0 — 2026-08-19

**MAYOR** ⚠ obliga a migrar (al guardar, el revisor rechaza el texto con caracteres invisibles nuevos).

**Se estaba limpiando una gotera con la llave abierta.** Se midió cuándo se escribió cada carácter raro del texto del estándar, y el 58 % es posterior al día en que se prohibió escribirlos. Limpiar primero era hacer el trabajo dos veces.

Ahora, al guardar un cambio, se revisa **solo lo que entra en ese guardado** y se rechaza si la cuenta sube. No se exige limpiar lo que ya está: se exige no agregar.

**El detalle.** Del [pendiente 11](pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md). Se agregó `validar.py marcas --preparados` y se enganchó al revisor de guardado que instala [`validadores/instalar.py`](validadores/instalar.py).

**Rechazar todo habría apagado el revisor el primer día.** Seis guardados seguidos traían 425 caracteres de estilo entre todos: un revisor que rechaza siempre se desactiva en una tarde. Así que se reparte:

- **Los invisibles, en cualquier carpeta** — un espacio que no se ve, una raya corta donde va un guion. Nadie los teclea a propósito y se quitan en segundos.
- **Todos, en `base/` y `plantillas/`** — es lo que reciben los proyectos.
- **El resto se cuenta y se dice**, sin rechazar nada.

Probado contra los doce guardados anteriores: ocho habrían pasado sin tocar nada.

**Y se limpiaron 1 212 caracteres**, en 110 archivos de `base/` y `plantillas/`: solo los que tienen un reemplazo y ninguna decisión. La raya larga y el punto medio en prosa **no se tocaron a propósito** — quitarlos es reescribir la frase, y un programa que reescribe frases cambia lo que el estándar dice.

**El sello de una regla ya no vence por tipografía.** El sello responde por lo que la regla exige, y cambiar una raya corta por un guion no cambia ninguna respuesta. Sin esto, esta limpieza habría vencido de golpe el sello de setenta y cuatro reglas — y entonces no se limpia nunca.

**El marcador de relleno `«…»` se dejó fuera de la cuenta**, y encontrarlo evitó un daño: tres revisores reconocen por él una casilla sin llenar. Limpiarlo los habría roto.

## 24.10.0 — 2026-08-18

**MENOR** (una herramienta más para revisar la memoria; nada que cumplir).

**Dos acuerdos opuestos guardados a la vez son peores que no tener ninguno:** dan respuestas seguras y contrarias según cuál se encuentre primero.

Ahora se pueden buscar los pares sospechosamente parecidos, para mirarlos. **No dice que se contradigan** — eso lo decide quien lee.

**El detalle.** Del [pendiente 09](pendientes/hecho/autonomia-sin-ia.md), su ítem 16, **el último de los dieciséis**. Nace [`memoria/parecidas.py`](memoria/parecidas.py).

**El umbral se eligió midiendo, y el resultado fue no devolver nada.** Sobre 114 acuerdos vigentes: con el corte bajo salían seis pares, todos relacionados pero ninguno contrario; con el corte alto, ninguno. **Se eligió el que hoy no devuelve nada** — seis pares que hay que descartar a mano enseñan a no mirar la lista, y el día que aparezca uno de verdad tampoco se mira.

**Y medirlo destapó algo:** la primera versión comparaba el título y daba once pares, todos falsos. Los títulos siguen un molde, así que **dos cosas de temas distintos salen parecidísimas por la forma de la frase**. Comparando el porqué, que es donde está la sustancia, bajaron a seis.

## 24.9.0 — 2026-08-18

**MENOR** (la plantilla del stack pide dos datos más; nada deja de valer).

**La regla más cara de incumplir del estándar dependía de que alguien se acordara.** Dice que antes de algo que no se puede deshacer hay que comprobar que existe una copia — y comprobarlo era una decisión, no un paso.

Ahora hay una forma de correrlo que **hace la copia primero y solo entonces sigue**. Si no hay copia declarada, o si la copia falla, **no corre nada**.

**El detalle.** Del [pendiente 09](pendientes/hecho/autonomia-sin-ia.md), su ítem 15, y hace cumplir [`00·N7`](base/00-nucleo-blindado.md). Nace [`validadores/respaldo.py`](validadores/respaldo.py). La [plantilla del stack](plantillas/stack.md) gana dos filas: cómo se respalda y **cómo se restaura** — la segunda no la usa ningún programa, se declara para que esté escrita antes del susto y no durante.

**El límite va escrito en cada corrida, y es la mitad del trabajo.** Esto cubre lo que se le pasa por la mano; un borrado escrito a mano o desde otra herramienta **no lo ve nadie**. El propio pendiente lo advertía: *«un respaldo automático parcial que se anuncia como total es peor que no tenerlo»*.

**Y no adivina el comando.** Sin declaración no inventa: adivinar cómo se respalda una base ajena sería equivocarse justo antes de lo irreversible.

## 24.8.0 — 2026-08-18

**MENOR** (una herramienta más que arma el esqueleto de un trabajo nuevo).

**Abrir un trabajo nuevo obligaba a copiar cinco documentos a mano, calcular su letra y escribir los enlaces sin equivocarse.** Ahí es donde se cometían los errores que las revisiones detectaban después. Ahora la estructura nace bien en vez de corregirse.

**Y no escribe una sola palabra de contenido**, que es lo que hace que sirva: los espacios por llenar quedan tal cual, para que la revisión siga exigiendo que alguien los llene.

**El detalle.** Del [pendiente 09](pendientes/hecho/autonomia-sin-ia.md), su ítem 12. Nace [`validadores/andamio.py`](validadores/andamio.py); sin `--aplicar` solo dice qué crearía. La advertencia venía en el propio pendiente y era lo más importante que traía — *«un generador que además rellena texto produce documentos que pasan el validador sin decir nada, que es la peor combinación posible»*—, y hay un caso que **falla si algún documento sale sin marcadores**.

**La letra se lee, no se cuenta.** Si existen la `A` y la `C` porque la `B` se renombró, contar cuántas hay daría `C` y **pisaría un trabajo vivo**. Hay un caso con ese hueco exacto.

## 24.7.0 — 2026-08-18

**MENOR** (se puede medir algo que antes no se medía; nada que cumplir).

**Un trabajo que hubo que rehacer y uno que salió bien a la primera se veían igual.** Ahora se distinguen, y con eso se puede saber qué parte del proceso obliga a volver atrás — que es información para cambiar reglas, no para calificar a nadie.

Sobre este repositorio encuentra dos, y son las dos de verdad.

**El detalle.** Del [pendiente 09](pendientes/hecho/autonomia-sin-ia.md), su ítem 10. Nace [`validadores/reaperturas.py`](validadores/reaperturas.py) y el subcomando `validar.py reaperturas`.

**Se deriva de la historia del archivo, no de sus palabras**, y ahí está lo que lo hace fiable: volver a empezar se escribe en prosa y cada quien con las suyas, así que buscar el texto encuentra unas, se pierde otras y cuenta las que solo *hablan* del tema — **cinco archivos lo mencionan y solo dos trabajos se rehicieron**. Lo que no se puede escribir de dos formas es una casilla que estaba marcada y dejó de estarlo.

**Y nunca es una falla.** Volver atrás **es lo correcto** cuando lo que falla es ese trabajo y su documentación decía que estaba hecho: así pasó con los dos que encuentra.

## 24.6.0 — 2026-08-18

**MENOR** (una herramienta más que escribe lo que antes había que acordarse de escribir).

**Cada archivo nuevo obligaba a agregar su línea al índice a mano.** Olvidarlo se descubría después, corriendo la revisión, a veces varios guardados más tarde. Hoy pasó dos veces.

Ahora la línea se escribe sola, con el título del archivo, y queda marcada como pendiente de describir bien.

**El detalle.** Del [pendiente 09](pendientes/hecho/autonomia-sin-ia.md), su ítem 14. Nace [`validadores/indices.py`](validadores/indices.py) y el subcomando `validar.py indices`, que sin `--aplicar` solo dice qué escribiría.

**No regenera el índice entero, y ahí está la decisión.** El pendiente proponía reescribir el bloque completo, y eso destruía trabajo: las líneas que ya están llevan una descripción escrita por alguien que el título del archivo no tiene. Se agrega lo que falta, se avisa de lo que quedó sin describir, y **lo que sobra se reporta y no se borra** — quitar una línea puede ser el error, no el archivo que ya no está.

**Y lo comprobó otro control construido hoy:** al aparecer el archivo nuevo, el mapa de qué está atado a la herramienta lo reportó como pieza sin clasificar. Funcionó a la primera y contra un caso real.

## 24.5.0 — 2026-08-18

**MENOR** (la instalación deja una revisión automática más; nada que hacer en tu proyecto).

**Antes de publicar, ahora corre sola la revisión que hasta hoy dependía de que alguien se acordara.** Enlaces rotos, índices viejos, cosas sin versionar: si algo de eso está mal, el envío se detiene.

Corre al publicar y no en cada guardado, a propósito: en cada guardado costaría minutos y a la semana alguien la apagaría. **Y publicar es lo que no se deshace** — lo guardado se revierte, lo publicado ya lo tiene otro.

**El detalle.** Del [pendiente 09](pendientes/hecho/autonomia-sin-ia.md), su ítem 08. Nace el enganche `pre-push` en [`instalar.py`](validadores/instalar.py), y hoy se notó la falta: se publicaron dieciséis commits seguidos sin que corriera nada solo.

**Lo que detiene y lo que solo informa está separado, y es la distinción que decide si el enganche sobrevive.** La primera versión metía en el bucle que detiene la revisión del cuerpo de reglas contra su propio molde, y **rechazó el envío con cero fallas**: hay reglas con deuda conocida. Un estándar endeudado consigo mismo no puede impedir publicar cualquier otra cosa — así se termina saltando el enganche para todo, que es apagarlo sin decirlo.

**Y de paso se midió el resto del pendiente: diez de sus dieciséis automatizaciones ya estaban construidas.** Quedan cinco, las de complejidad media o alta.

## 24.4.0 — 2026-08-18

**MENOR** (un capítulo nuevo que arranca apagado; ningún proyecto tiene que hacer nada).

**El estándar servía para construir un proceso que corre solo, pero no traía nada propio sobre cómo se construyen.** Ahora sí: ocho reglas para lo que automatiza trabajo repetitivo operando sistemas que no se pueden cambiar ni avisar.

Viene apagado. Se enciende editando una línea del `CLAUDE.md`, como los otros cinco patrones opcionales.

**El detalle.** Cierra el [pendiente 08](pendientes/hecho/patrones-rpa.md) con el capítulo [`21 · Automatización de procesos`](base/21-automatizacion-de-procesos.md): `AU1` a `AU8`, todas con su checklist en cumple.

**No dice «RPA» en ninguna parte, y es a propósito.** [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no admite en la base el nombre de una tecnología, y el pendiente nombraba cuatro motores concretos; la sigla es de la industria y las siglas envejecen. **Lo que no envejece es el problema**, y el problema queda dicho sin sigla.

**Lo que no entró: las plantillas.** `AU7` exige que cada proceso traiga su ficha y se mantenga; **qué campos lleva es del proyecto**, porque depende de qué sistemas toca. Un molde en la base sería adivinar.

## 24.3.1 — 2026-08-18

**PARCHE** (una comprobación deja de acusar de lo que no puede ver).

**Correr las comprobaciones contra un proyecto de verdad destapó que una acusaba en falso.** Decía que a treinta y una tablas les faltaba su migración, y las migraciones estaban ahí. Solo sabe leer dos formatos, y las de ese proyecto eran de un tercero: las saltaba todas y concluía que no existía ninguna.

Ahora, cuando no puede leer las migraciones de un proyecto, **lo dice una vez** y no comprueba lo que no ve.

**El detalle.** Cierra el [pendiente 01](pendientes/hecho/validadores-de-codigo-de-proyecto.md), que pedía justamente esto desde el 2026-08-04: correrlos contra código real. **No se arregló enseñándole el formato nuevo** —eso ataría la base a una tecnología, lo que [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) prohíbe— sino **sabiendo lo que no sabe**. «Faltan» es acusar; «no las veo» es informar, y lo segundo es lo cierto.

**Y el arreglo no apagó nada:** con migraciones legibles, la tabla que de verdad falta se sigue reportando, y en un proyecto sin migraciones de ningún tipo tampoco hay excusa. Los dos casos están escritos.

## 24.3.0 — 2026-08-18

**MENOR** (tres comprobaciones que ya existían pasan a poder correrse).

**Tres comprobaciones estaban escritas, probadas, y no las podía correr nadie.** El backlog las daba por «lo que falta construir» desde hace dos semanas, y lo que faltaba era la puerta: el programa que las lanza ni siquiera las conocía.

Ahora se corren con `validar.py estructura`, `validar.py entidades` y `validar.py cruces`.

**El detalle.** Del [pendiente 01](pendientes/hecho/validadores-de-codigo-de-proyecto.md), que listaba nueve comprobaciones faltantes. **Cinco ya estaban construidas** — [`estructura.py`](validadores/estructura.py) para dónde vive el código y cómo se llama, [`entidades.py`](validadores/entidades.py) para lo que se le exige a una tabla de dominio, [`cruces.py`](validadores/cruces.py) para el cruce entre módulos, [`flujo.py`](validadores/flujo.py) para las puertas del flujo, y [`declaracion.py`](validadores/declaracion.py), que era la precondición de todas—. Tres de ellas no tenían subcomando.

**Es la tercera vez que este repositorio tropieza con lo mismo, y las tres el mismo día:** `cerrar.avisar()` escrita con doce casos y nunca llamada, `metareglas.py` sin subcomando, y estos tres. **Una pieza que no se puede correr figura como cobertura y no cubre nada.**

**Se comportan como deben:** sobre un proyecto que no declaró su convención no inventan nada — dicen qué comprobación se quedó sin correr y por qué. Un validador que exige lo que nadie acordó se termina apagando, y apagado figura como cubierto.

## 24.2.0 — 2026-08-18

**MENOR** (arrancar cuesta la mitad; las reglas llegan igual de completas).

**Más de la mitad de lo que se le entregaba al agente al abrir la sesión no le servía para nada.** Eran los bloques de revisión de cada regla — el registro de que alguien la miró contra el molde y la dio por buena. Eso le sirve a quien mantiene el estándar, no a quien tiene que obedecerlo.

Arrancar pasó de **122,6 KB a 68,7**. Las reglas llegan enteras, con sus ejemplos.

**El detalle.** Lo destapó una prueba, no la lectura: el arranque tenía un techo puesto desde la fase que lo midió, y **saltó al partir las reglas del núcleo**. En vez de subir el techo se miró qué había adentro — **70 de los 122 KB eran sellos**, el 57 por ciento.

El techo baja de 120 a 90 KB, y hay dos casos nuevos: que el sello no viaje, y que **las reglas sí lleguen enteras** — sin el segundo, un recorte de más pasaría por ahorro.

## 24.1.0 — 2026-08-18

**MENOR** (una regla del núcleo dice lo mismo con menos y deja de contradecirse; no cambia lo que exige).

**«¿Y para qué necesita excepciones?»** Lo preguntó el usuario, y la respuesta resultó ser que no las necesita.

La regla que exige aprobación antes de cambiar nada traía una excepción: que un plan ya aprobado se ejecuta seguido, sin volver a preguntar por cada paso. **Eso nunca fue una excepción** — un plan aprobado **ya tiene** esa aprobación. El usuario la dio una vez, para todo lo que el plan dice. Volver a pedirla paso a paso no es más riguroso: es pedir otra vez algo ya concedido.

**El detalle.** [`00·N1`](base/00-nucleo-blindado.md) pasa a **CUMPLE** después de reprobar su fila 16 desde que se midió. El problema no era que la excepción estuviera mal escrita —eso se arregló hoy mismo y no alcanzó—: era que **una regla `[BLINDADA]` con excepción deja de ser inquebrantable por definición**, y la cabecera del capítulo promete lo contrario. El choque era del texto, no de la exigencia.

**El límite sobrevive entero**, que era lo único que había que cuidar: lo irreversible se pide cada vez, aunque el plan lo incluyera. Ahora forma parte de la exigencia en vez de colgar de una excepción.

**Y queda escrito para el capítulo:** una regla `[BLINDADA]` que necesita una excepción probablemente está mal redactada. La de `N1` desapareció sola al decir bien qué cubre la aprobación.

Las reglas publicadas en «no cumple» bajan de 28 a **27**.

## 24.0.0 — 2026-08-18

**MAYOR** (cambia el núcleo: nacen tres reglas blindadas con nombre nuevo. **Si tu proyecto cita `N1`, `N4` o `N6`, hay que mirarlo.**)

**Las tres reglas más importantes del estándar pedían dos cosas cada una, y una regla que pide dos cosas se cumple a medias sin que nada lo note.** En el núcleo eso es exactamente lo que no puede pasar.

Una decía que nada se ejecuta sin permiso *y además* que lo rechazado no se reintenta. Otra, que no se destruye sin autorización *y además* que antes de lo irreversible hay que comprobar que existe una copia. Otra, que una clave no se escribe en el código *y además* que el contenido del proyecto no sale afuera.

**En los tres casos, la segunda mitad es la que se olvida justo cuando la primera se cumplió bien:** con el permiso dado, nadie mira si hay copia.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nacen [`00·N7`](base/00-nucleo-blindado.md) —antes de lo irreversible se comprueba que hay de dónde volver—, [`00·N8`](base/00-nucleo-blindado.md) —el contenido del proyecto no sale sin autorización— y [`00·N9`](base/00-nucleo-blindado.md) —lo que el usuario rechazó no se reintenta de otra forma—.

**`N7` rescata una frase que estaba escondida** dentro de `N4` y ahora es lo primero que se lee: *que la migración se pueda revertir no es lo mismo que poder recuperar lo borrado*. Es la confusión que hace que alguien corra tranquilo algo irreversible.

**`N4` deja de nombrar operaciones concretas.** Enumeraba cuatro comandos de un tipo de almacén, lo que [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no admite en la base y además dejaba fuera todo lo demás. **Lo que se prohíbe es destruir, no cuatro palabras.**

**Lo que sigue sin resolverse, y es del usuario:** `N1` continúa reprobando su checklist, y partirla no lo arregla. Una regla blindada **con excepción escrita** deja de ser inquebrantable por definición, y la cabecera del capítulo promete lo contrario. La excepción es real y necesaria —sin ella un plan aprobado se ejecutaría pidiendo permiso paso a paso—, así que **lo que hay que decidir es si el capítulo admite excepciones**.

Las reglas publicadas en «no cumple» bajan de 30 a **28**.

## 23.26.0 — 2026-08-18

**MAYOR** (nace una regla con nombre nuevo, y otra deja de nombrar la técnica que exigía).

**La regla sobre cómo se prueban los cálculos decía dos cosas, y la segunda es la que evita el engaño.** Una es de dónde salen los casos; la otra, de dónde sale el resultado que se espera. **Se pueden derivar los casos con todo el método y copiar el resultado esperado de lo que el código produce hoy** — y entonces la prueba solo comprueba que el código hace lo que hace: pasa siempre, no falla nunca, y figura como cubierta.

**Y la regla sobre valores que cambian con el tiempo no era larga: era un manual entero metido dentro.** Doce veces el tamaño del molde, con la tabla, la migración, los avisos, la interfaz y las pruebas. Lo que exige cabe en tres líneas.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nace [`08·T8`](base/08-pruebas.md) —el resultado esperado no sale del código que se está probando—, y su propio texto ya decía *«se aplica en dos frentes»*.

[`03·D7`](base/03-datos.md) se reescribió en una exigencia y su manual se fue a [`notas/como-se-guarda-la-historia-de-un-valor.md`](notas/como-se-guarda-la-historia-de-un-valor.md). **También salió del título el nombre de la técnica**: nombrarla ata la regla a una forma de resolverlo, y lo que se exige es el resultado — la nota ya ofrece la alternativa para cuando el volumen no dé.

Las reglas publicadas en «no cumple» bajan de 32 a **30**.

## 23.25.0 — 2026-08-18

**MAYOR** (nacen tres reglas con nombre nuevo, todas del capítulo de conducta).

**Tres reglas sobre cómo trabaja el agente juntaban un error con su contrario, y así una regla sola empuja hacia uno de los dos según cómo se lea.**

Una pedía reformular antes de actuar *y además* decía qué respuesta cuenta como un sí. Otra pedía aplicar sin preguntar lo que el oficio da por sentado *y además* preguntar lo que de verdad decide el dueño. Otra pedía notar cuándo un pedido deja un criterio para la próxima vez *y además* decidir si ese criterio sirve solo aquí o en cualquier proyecto.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nacen [`01·C24`](base/01-conducta.md) —solo la palabra del usuario aprueba—, [`01·C25`](base/01-conducta.md) —lo que es del usuario se pregunta— y [`01·C26`](base/01-conducta.md) —la regla que serviría en otra empresa va a la base común—.

**`C24` es la que se incumple sin mala fe:** el agente pregunta, no le contestan, y toma la falta de objeción por acuerdo. **Se le quitó la lista de palabras afirmativas** —«sí», «dale», «hágale»— porque lo que importa no es cuál palabra sino **de quién** es, y enumerarlas invitaba a buscar la palabra en vez de mirar quién la dijo.

**`C25` y `C14` son dos errores opuestos**, y por eso hacían mal juntas: una combate preguntar de más, la otra decidir de más. La frontera quedó en tres clases —cómo se ve, qué decide el negocio, lo que cuesta caro deshacer— y no en una lista de casos, que se queda corta el día que aparece el que nadie anotó.

**Y `C26` es la que no se nota nunca desde adentro:** una regla escrita en el sitio equivocado funciona igual de bien; el precio lo paga el proyecto siguiente, que la escribe otra vez.

Las reglas publicadas en «no cumple» bajan de 35 a **32**.

## 23.24.1 — 2026-08-18

**PARCHE** (una comprobación deja de reportar de más; nada cambia de lo que se exige).

**El aviso de «este sello venció» pasó de 119 a cero.** No porque se apagara, sino porque el arreglo anterior estaba a medias: comparaba el texto guardado **con su encabezado** contra el actual **sin él**, así que daban distinto siempre. Quedaba igual de ruidoso, pero con más código.

Ahora vence solo el sello de la regla que de verdad cambió.

**El detalle.** La comparación quitaba el encabezado de un lado y no del otro. Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), y con tres casos que lo fijan — incluido el que comprueba que sobre el propio estándar no quede ninguno vencido.

## 23.24.0 — 2026-08-18

**MAYOR** (nacen cuatro reglas con nombre nuevo) · **y una comprobación deja de reportar de más.**

**La regla sobre tablas nuevas pedía tres cosas a la vez** —que el dato no se repita, que quede escrito quién tocó cada fila, y que las relaciones se declaren en el propio almacén— y las tres se cumplen por separado. La de valores configurables pedía dónde guardarlos *y además* cómo compararlos.

**Y una comprobación estaba gritando.** El aviso de «este sello venció» miraba la fecha del **archivo**, así que tocar una regla vencía el sello de todas las de su capítulo: **119 avisos en una sola corrida**. Un validador que reporta ciento diecinueve cosas no lo lee nadie.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). [`03·D1`](base/03-datos.md) se parte en tres —nacen `D10`, quién tocó la fila, y `D11`, la integridad vive en el almacén— y [`03·D4`](base/03-datos.md) en dos, con `D12`: el código decide por el código del catálogo, **no por su identificador**, que es el que cambia entre entornos y hace fallar en producción lo que funcionaba al programar.

**`D11` sostiene a [`03·D9`](base/03-datos.md)**: sin la restricción declarada en el almacén, dos procesos simultáneos insertan el mismo registro por más que la aplicación lo compruebe. Se incumple con la mejor intención — *«ya lo valido yo»*.

**La comprobación del sello ahora pide las dos cosas:** que el archivo se haya tocado después del sello **y** que el cuerpo de esa regla difiera del guardado. Su propio texto ya había anticipado este paso — *«si esto produce demasiado ruido, la huella queda como el paso siguiente, ya con datos»*—, y los datos fueron 119.

Las reglas publicadas en «no cumple» bajan de 37 a **35**.

## 23.23.0 — 2026-08-18

**MAYOR** (nacen cuatro reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Cuatro reglas más separadas, y en las cuatro la mitad que se va es la que se olvida.**

Una pedía que repetir una operación no duplicara su efecto *y además* que dos operaciones simultáneas no se pisaran — que son problemas distintos: el mismo actor dos veces, o dos actores a la vez. Otra pedía que anular revirtiera todo de una vez *y además* que se avisara a quien tenía el dato ya calculado. Otra, que las pruebas corrieran solas *y además* que lo que corre en tu máquina no las reemplace. Y la del plan pedía el visto bueno *y además* dejaba claro que autorizar el arranque de una fase no es aprobar su plan.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nacen [`03·D9`](base/03-datos.md), [`15·IM7`](base/15-registros-inmutables.md), [`09·G11`](base/09-git.md) y [`02·F25`](base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md).

**`02·F25` es la que más se incumple sin querer**, y por eso merecía nombre propio: nadie se salta la aprobación de un plan a propósito — lo que pasa es que **se toma el «arrancá con X» por el permiso de ejecutar**, y el trabajo avanza con la conciencia tranquila. `F4` dice que hace falta un visto bueno; `F25` dice cuál no cuenta.

Las reglas publicadas en «no cumple» bajan de 41 a **37**.

## 23.22.0 — 2026-08-18

**MAYOR** (nacen tres reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Tres reglas más que pedían dos cosas cada una.** Una decía cómo evitar que la entrada del usuario se cuele dentro de una instrucción *y además* qué campos puede tocar un formulario; otra, cómo guardar un archivo privado *y además* qué pasa con él cuando se da de baja a su dueño; otra, que los entornos se parezcan *y además* que lo que hace falta en producción quede escrito.

En los tres casos la segunda mitad es la que se cae sola, sin ruido: se puede tener todo bien parametrizado y aun así dejar que un formulario escriba el campo que vuelve administrador a quien lo manda.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nacen [`04·S16`](base/04-seguridad.md) —solo se asigna lo que está declarado—, [`04·S17`](base/04-seguridad.md) —el archivo sobrevive a la baja de su dueño— y [`11·CFG5`](base/11-configuracion-entornos.md) —lo que producción necesita se escribe antes de aplicarlo—.

**[`14·EST2`](base/14-estructura-codigo.md) no se partió: le sobraba, no le faltaba.** Lo que la hacía parecer dos reglas era un consejo sobre los límites de longitud del motor, que además nombraba tecnología. **No era una exigencia, era una advertencia práctica**, y se fue. Lo que queda es una sola cosa: una convención por tipo de elemento, aplicada igual.

Las reglas publicadas en «no cumple» bajan de 45 a **41**.

## 23.21.0 — 2026-08-18

**MAYOR** (nacen cinco reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Seguimos separando reglas que decían varias cosas a la vez.** Una pedía cuatro cosas distintas sobre la seguridad de las sesiones; otra pedía validar antes de empezar *y además* no dejar el trabajo a la mitad; otra pedía llevar tres estados *y además* anotar quién anuló y por qué.

Cuando una regla pide dos cosas, se cumple la primera y la segunda se cae sin que nada lo note. Ahora cada una se puede señalar por separado.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). [`04·S5`](base/04-seguridad.md) —cuyo título *«CSRF, sesiones y transporte»* **ya las enumeraba**— se parte en cuatro: se queda con el token, y nacen `S13` (la sesión se cierra de verdad), `S14` (el dato sensible no viaja en claro) y `S15` (la contraseña se guarda irreversible y con sal). [`05·E2`](base/05-errores-y-logging.md) se parte y nace `E6` —lo que toca varios registros va en transacción—, y [`15·IM2`](base/15-registros-inmutables.md) se parte y nace `IM6` —anular deja escrito quién, cuándo y por qué—.

**`17·I3` se miró para partirla y se decidió que no**, y conviene saber por qué: sus cuatro puntos —etiqueta, contraste, teclado, color— **no son cuatro exigencias, son la definición de una**. Una interfaz con etiquetas y sin contraste no cumple «la accesibilidad mínima» a medias: no la cumple. **La prueba es si se cumplen por separado**, y acá no.

**Y [`02·F12`](base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) no se toca:** es texto literal del usuario y su propio sello ya decía que se queda reprobada hasta que él decida la vía.

Las reglas publicadas en «no cumple» bajan de 49 a **45**.

## 23.20.0 — 2026-08-18

**MAYOR** (nacen dos reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Tres reglas decían dos cosas cada una, y por eso nadie las cumplía enteras.** Una pedía autorizar cada escritura contra datos reales *y además* contar el borrado lógico como escritura; otra pedía que el mensaje del commit abriera con la idea del usuario *y además* que no llevara firma de herramienta. Cumplir la primera mitad y olvidar la segunda pasaba sin que nada lo notara.

Ahora cada una dice una sola cosa, y se puede señalar cuál se incumplió.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Nacen [`04·S12`](base/04-seguridad.md) —el borrado lógico es una escritura— y [`09·G10`](base/09-git.md) —el commit no se firma con la herramienta—. **Las dos ya venían numeradas dentro del texto que las contenía:** `S11` decía «Regla 1» y «Regla 2», y `G8` abría con «Dos consecuencias». Los identificadores viejos siguen existiendo con la mitad que se quedaron, como manda [`20·M4`](base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md).

**Y partir sirvió para pagar una deuda vieja.** `04·S11` nombraba `SoftDeletes` y `destroy()`, lo que [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) prohíbe en la base, y su sello había decidido no corregirlo porque **el nombre del método era el argumento**: suena a borrar y escribe. Reescribirlo en concepto solo se podía al partir, y así fue. **La lista de reglas que nombran un framework vuelve a cero**, después de once días con una permitida.

**[`12·PR3`](base/12-privacidad-datos.md) no se partió: se reescribió.** No tenía dos exigencias — tenía cuatro remisiones al capítulo de seguridad y nada propio. Lo suyo estaba implícito y ahora está dicho: **el dato personal se trata como sensible aunque nadie lo haya clasificado así**, sin esperar a que el proyecto lo declare.

Las reglas publicadas en «no cumple» bajan de 52 a **49**.

## 23.19.0 — 2026-08-18

**MAYOR** (una regla del núcleo dice ahora algo que antes no decía; conviene releerla).

**Aprobar un plan aprobaba también lo que no se puede deshacer, y eso ya no vale.** La regla decía que un plan aprobado se ejecuta seguido, sin volver a pedir permiso paso a paso. Ahora dice hasta dónde: **lo irreversible se pide aparte cada vez, aunque estuviera escrito en el plan que aprobaste.**

También se escribió entera la excepción de las pruebas: el cambio sin lógica puede ir sin prueba, pero hay que decir en el plan cuál es y por qué, y eso lo aprueba el usuario — no lo decide solo quien escribe.

**El detalle.** [`00·N1`](base/00-nucleo-blindado.md) y [`08·T1`](base/08-pruebas.md) escriben su excepción en la forma que pide [`20·M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), con condición, límite y autorizador. `T1` pasa a **CUMPLE**.

**El cambio de `N1` resolvió un choque que se había creado el mismo día.** El anexo [`acciones-y-riesgo.md`](base/00-identidad-y-rol/acciones-y-riesgo.md) dice que un plan aprobado nunca cubre lo irreversible, y `N1` decía *«se ejecuta continuo»* a secas: las dos afirmaban cosas contrarias, y manda la del núcleo. Hay un caso de prueba que comprueba que sigan de acuerdo.

**Y una corrección del mismo día, que conviene leer.** Al arreglar la excepción se marcó en verde la fila 16 del checklist de `N1`, y **estaba mal**: su sello ya explicaba, desde antes, que el problema no es que la excepción esté mal escrita sino que **existe** — una regla `[BLINDADA]` con excepción deja de ser inquebrantable, que es lo contrario de lo que promete la cabecera del capítulo. Escribirla mejor la hace más explícita, no la hace desaparecer. La fila volvió a ❌ el mismo día.

## 23.18.0 — 2026-08-18

**MENOR** (una regla admite un caso que antes no admitía; nada de lo que ya cumplías deja de valer).

**Enlazar al archivo de al lado obligaba a escribir su dirección completa.** Para nombrar un documento que está en la misma carpeta había que poner una línea de unos 130 caracteres, y eso pasaba en setecientos enlaces — casi todos, documentos de un mismo trabajo citándose entre sí.

Ahora el archivo de la misma carpeta se enlaza por su nombre. El de cualquier otra sigue llevando su dirección entera.

**El detalle.** Es el [pendiente 18](pendientes/hecho/los-enlaces-del-estandar-no-cumplen-doc14.md). [`13·DOC14`](base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) gana su excepción escrita en la forma de [`20·M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), y se le vuelve a aplicar el checklist: pasa de 17 a 18 filas en verde, porque la fila 16 dejó de ser N/A.

**La excepción sale del propio texto de la regla, no de que fueran muchos.** `DOC14` pide la ruta *«para saber dónde vive sin abrirlo»*, y para el vecino ese propósito ya está cumplido. El límite es estrecho a propósito: la misma carpeta y nada más.

**Antes se había intentado al pie de la letra**, y quedó ilegible; se revirtieron 347 archivos. Esa reversión fue la que destapó que el problema no eran los enlaces sino la regla, que no había previsto el caso más común.

## 23.17.1 — 2026-08-18

**PARCHE** (deja de contarse como defecto algo que no lo era; ninguna exigencia cambia).

**La forma en que esta casa nombra sus capítulos estaba contada como si fuera un descuido.** El punto que separa el número del nombre —«09 · Control de versiones»— aparecía como una de las marcas que delatan un texto escrito por una máquina. Eran mil seiscientas, y una de ellas estaba en el índice del propio documento que las prohíbe.

Se conserva, y no como excepción sino como lo que es: la manera en que este proyecto nombra las cosas. En medio de una frase sigue contando.

**El detalle.** Del [pendiente 11](pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md). El [anexo de marcadores](base/00-identidad-y-rol/marcadores-de-ia.md) ya eximía la cita `NN·ID` por ser notación definida, y el separador de encabezado es la misma clase. **El código ya lo tenía decidido y no lo había implementado:** el comentario de [`marcas.py`](validadores/marcas.py) decía *«ni de un `A · B` de encabezado: los dos son notación definida»*, y la expresión regular solo cubría la primera mitad. El recuento baja de 16 477 a **15 485**; el punto medio, de 6 237 a **4 638**. Se exime solo en la línea de un encabezado. 6 casos nuevos.

## 23.17.0 — 2026-08-18

**MENOR** (una regla deja de regir porque otra ya decía lo mismo; no hay nada nuevo que cumplir).

**Dos reglas pedían lo mismo y se remitían la una a la otra en círculo.** Una decía «audita las vulnerabilidades de tus dependencias, el detalle está en el otro capítulo», y el otro capítulo decía «audítalas, ver la primera». Quien las leía daba la vuelta y volvía al principio.

Se queda la del capítulo de dependencias, que es de quien es el tema. La otra deja de regir y su texto se conserva, porque hay trabajo cerrado que la cita.

**El detalle.** [`04·S7`](base/04-seguridad.md) queda `[DEROGADA en 23.17.0 → ver 10·DEP3]` por [`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md), que manda derogar y no borrar. El dueño del tema es el capítulo `10` según [`20·M2`](base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md). **No se pierde ninguna exigencia:** [`10·DEP3`](base/10-dependencias.md) ya pedía las dos cosas y agrega una que `S7` no decía — que quedarse muy atrás vuelve caro e inseguro actualizar después. `DEP3` deja de remitir a `S7`, que era la otra mitad del círculo.

## 23.16.0 — 2026-08-18

**MENOR** (una comprobación más; nada nuevo que cumplir).

**Si mañana dejaras esta herramienta por otra, nadie sabía qué se cae y qué se queda.** Ahora sí: de los 54 programas del estándar, **18 hablan con la herramienta y 36 no** — esos funcionarían igual con cualquier agente, o sin ninguno.

Lo que se caería son los ocho enganches y el instalador que los enchufa. Las reglas, que son texto, se quedan enteras.

**Y el mapa no envejece en silencio**, que es lo que le pasa a todo mapa escrito a mano: si aparece un programa nuevo que no está clasificado, se dice.

**El detalle.** Es el punto 1 del [pendiente 15](pendientes/hecho/el-estandar-depende-de-una-sola-herramienta.md), construido como la fase [`A-EP-005-HU-011`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/A-EP-005-HU-011-donde-termina-el-estandar/README.md) con su plan aprobado. Nace [`validadores/amarre.py`](validadores/amarre.py) y el subcomando `validar.py amarre`, que reporta **por los dos lados**: la pieza que existe y el mapa no nombra, y la que el mapa nombra y ya no existe. El segundo lado no lo pedía la historia — se agregó porque un mapa que promete clasificar algo borrado miente igual que uno incompleto.

**Lo que destapó al construirlo:** el mapa ya tenía el hueco sin necesidad de pieza nueva. Nombraba las 18 amarradas una por una y las libres **solo por su total**, así que **28 piezas no estaban nombradas en ningún lado**. Ahora van las 36 por su nombre: un total no es una clasificación, es la promesa de que alguien clasificó. 12 casos en [`test_el_mapa_del_amarre_no_envejece.py`](validadores/tests/test_el_mapa_del_amarre_no_envejece.py).

## 23.15.0 — 2026-08-18

**MENOR** (una lista nueva que organiza lo que ya se exigía; ninguna regla cambia).

**Aprobar un plan aprobaba por igual cambiar una coma y borrar algo que no se puede recuperar.** Ahora no: hay una lista de lo que el agente puede hacer, ordenada por lo que cuesta deshacer cada cosa.

Lo que se deshace solo se hace y se cuenta después. Lo que cuesta deshacer se anuncia antes, de una en una. **Y lo que no se deshace se pide aparte, cada vez** — aunque estuviera escrito en un plan ya aprobado.

**El detalle.** Es el [pendiente 13](pendientes/hecho/inventario-y-riesgo-de-las-acciones-del-agente.md), construido como la fase [`A-EP-001-HU-012`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/A-EP-001-HU-012-inventario-de-acciones-y-riesgo/README.md) con su plan aprobado. Nace el anexo [`base/00-identidad-y-rol/acciones-y-riesgo.md`](base/00-identidad-y-rol/acciones-y-riesgo.md) —12 clases, 3 🟢 · 4 🟡 · 5 🔴— y su comprobación en `validar.py acciones`. **`N1` a `N6` no cambian letra**, y hay un caso que lo vigila comparando su texto contra lo guardado.

**Tres cosas quedaron nombradas como irreversibles y antes no lo estaban:** borrar un archivo que no está en el control de versiones, correr algo que sale a la red, y escribir fuera del repositorio. Las tres caían en `N1` junto con cambiar una coma.

**Y tres defectos salieron de construirlo, los tres cazados por la máquina.** El que más enseña: el caso que borra una clase a propósito para ver si se reporta **no la reportaba**, porque la búsqueda miraba el archivo entero y el nombre seguía en otra sección. Sin ese caso, «cero huérfanas» habría significado que el programa no busca nada. 23 casos en [`test_las_acciones_tienen_su_riesgo.py`](validadores/tests/test_las_acciones_tienen_su_riesgo.py).

## 23.14.0 — 2026-08-18

**MENOR** (las comprobaciones arrancan donde estás parado; si las corrías desde tu proyecto, ahora sí lo revisan a él).

**Las comprobaciones que dicen revisar tu proyecto estaban revisando otra carpeta.** Si las corrías sin decirles dónde mirar, iban a parar a la carpeta donde vive el estándar — y devolvían un informe que parecía tuyo y no lo era.

Un proyecto lo descubrió al buscar claves sueltas en su código: le salieron dieciocho, todas de archivos que ese proyecto no tiene. Ahora arrancan donde está parado quien las corre.

**El detalle.** Es el [pendiente 63](pendientes/hecho/el-validador-de-secretos-se-revisa-a-si-mismo.md), reportado por `rni-dp`. El defecto no era el recorrido sino el valor por defecto de `--raiz`, que caía en `RAIZ` —la carpeta del propio estándar, calculada desde `__file__`—. **Cambian los 22 subcomandos que dicen «carpeta del proyecto»**; los que revisan el estándar siguen apuntando a `RAIZ`. No era solo `secretos`: los otros veintiuno tenían lo mismo y nadie lo había notado, porque casi siempre se corren desde el estándar y ahí las dos raíces coinciden.

**Y una exención, con cuidado:** las claves falsas de `test_la_clave_no_llega_al_historico.py` existen para comprobar que el detector detecta, así que se saltan. **Se nombran una por una y no por carpeta** — exceptuar `tests/` entero dejaría ciego al detector sobre lo que se escriba ahí mañana. Un caso de prueba fija que una clave de verdad sigue saliendo. 8 casos nuevos.

## 23.13.2 — 2026-08-18

**PARCHE** (se escribe una decisión que ya estaba tomada; nada cambia de comportamiento).

**Una conversación que sigue pasada la medianoche queda guardada con la fecha del día en que empezó, y nadie había escrito si eso está bien.** Está bien, y ahora se dice: el archivo es de una conversación, no de un día.

Partirla en dos rompería la forma de encontrarla, así que no se parte. Cada mensaje lleva su hora real, de modo que lo que pasó después de las doce se sabe leyendo. El resumen sí se guarda en el día en que pasaron las cosas, y esa diferencia es a propósito.

**El detalle.** Es el punto 3 del [pendiente 33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), preguntado el 2026-08-06 y sin contestar desde entonces. **La decisión ya la tomaba la máquina:** `hook_historico.py` busca la sesión por su marca `<!-- sesion: id -->`, nunca por fecha, así que partirla dejaría media conversación sin marca y la siguiente sesión no la encontraría. Faltaba escribirlo, y quedó en [`plantillas/historico-chat.md`](plantillas/historico-chat.md) y en el README de la carpeta. El caso real está a la vista: una sesión con 91 turnos de un día y 27 del siguiente.

## 23.13.1 — 2026-08-18

**PARCHE** (una comprobación más y dos correcciones de forma; nada nuevo que cumplir).

**Una regla podía declararse intocable sin estar en el capítulo de lo intocable, y nadie lo miraba.** No es que contradijera a las de arriba: es que se las saltaba, quedando por encima sin haber pasado por donde se pasa. Ahora se comprueba.

**El detalle.** Del punto 8 del [pendiente 33](pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), preguntado el 2026-08-07 y sin contestar desde entonces. `validar.py metareglas` reporta cualquier regla con la marca `[BLINDADA]` fuera de [`base/00-nucleo-blindado.md`](base/00-nucleo-blindado.md) — es la única mitad de [`20·M1`](base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) que un programa puede juzgar; que un nivel no contradiga al de arriba exige leer las dos reglas. Hoy da cero.

**Y el detalle que decide si el control sirve**, que ya estaba escrito en el resumen de aquel día: la palabra aparece en prosa en seis archivos, así que se ancla al **encabezado**. *«Un validador que reporta de más se termina apagando, y un control apagado es peor que ninguno porque figura como cubierto.»* Hay un caso de prueba dedicado a eso.

También del mismo punto: el plan de la fase `A-EP-001-HU-001` declara su origen en la forma que pide `13·DOC12`, y la tabla del [`CLAUDE.md`](CLAUDE.md) §3 ganó la fila de `anatomia/`.

## 23.13.0 — 2026-08-18

**MENOR** (una comprobación más que se puede correr; no cambia nada de lo que se exige).

**Pedir «menos es más» siete veces en tres días no hizo que las respuestas se acortaran.** Cada vez se anotaba el caso, y anotarlo no cambiaba nada: al final el registro era el sustituto de cumplir.

Lo que faltaba no era otro recordatorio, era un número. Ahora se puede medir cuánto ocupa lo que el agente contesta, y mirarlo al cerrar la sesión. **No detiene nada y no dice qué respuesta estuvo mal** — decir cuál palabra sobra sigue siendo cosa de quien lee.

**El detalle.** Es el [pendiente 58](pendientes/hecho/nada-hace-cumplir-id9.md), reportado por `shopnest-mesa`, con su salida 3: medir y no bloquear. Nace [`validadores/brevedad.py`](validadores/brevedad.py) y el subcomando `validar.py brevedad`, que lee la transcripción que ya escribe el enganche del histórico y reporta **la mediana por sesión** — no el máximo, porque una respuesta larga suele estar justificada y lo que señala un problema es que la mitad lo sean. Las otras dos salidas se descartaron con motivo: rebotar la respuesta obliga a leer la versión larga primero, e inyectar la regla en cada mensaje es lo que ya falló siete veces.

**Y hay un motivo que no estaba en el pendiente:** [`reglas-validables.md`](validadores/reglas-validables.md) ya declaraba que `ID9` no se puede comprobar con un programa. Un enganche que rebotara estaría afirmando lo contrario; uno que cuenta hace justo lo que esa declaración permite. Por eso la declaración quedó ahí y no en el cuerpo de la regla: meterla dentro la habría hecho más larga, **incumpliendo `ID9` al escribir cómo se comprueba `ID9`**. 21 casos en [`test_la_brevedad_se_mide.py`](validadores/tests/test_la_brevedad_se_mide.py).

## 23.12.2 — 2026-08-18

**PARCHE** (cuatro reglas dicen lo mismo en menos palabras; nada de lo que exigen cambia).

**Cuatro reglas venían con su explicación pegada y no se leían.** Una usaba mil doscientos caracteres para decir algo que cabe en cuatro líneas. Ahora la regla dice qué hay que hacer, y el detalle —qué carpetas quedan fuera, por qué autorizar un archivo no autoriza a su carpeta— vive aparte, enlazado.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), las cuatro que fallaban **solo** la fila 10: [`04·S9`](base/04-seguridad.md) 1 278 → 290 —su inventario de rutas se fue a [`notas/rutas-fuera-del-proyecto.md`](notas/rutas-fuera-del-proyecto.md)—, [`04·S10`](base/04-seguridad.md) 1 029 → 307, [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) 564 → 309 y [`05·E4`](base/05-errores-y-logging.md) 419 → 282. Las cuatro pasaron a **CUMPLE**: las reglas reprobadas bajan de 58 a **54**.

**Dos cosas que salieron de hacerlo.** `S10` no necesitó anexo: sus cinco viñetas eran la misma exigencia dicha cinco veces, más una lista de comandos concretos que por [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no debía estar en la base. Y `E4` tampoco: sus cuatro viñetas explicaban cuándo usar cada nivel de registro con un ejemplo, y el nombre del nivel ya lo dice.

## 23.12.1 — 2026-08-18

**PARCHE** (dos reglas dicen lo mismo en menos palabras; no cambia nada de lo que exigen).

**Dos reglas sobre datos venían con su explicación pegada y no se leían.** Una medía casi dos mil caracteres para decir algo que cabe en cinco líneas. Ahora la regla dice qué hay que hacer, y el porqué —por qué la gente se equivoca y qué se rompe cuando lo hace— vive aparte, enlazado.

**El detalle.** Del [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). [`03·D8`](base/03-datos.md) pasó de 1 962 a 292 caracteres —su porqué quedó en [`notas/pertenencia-y-autoria.md`](notas/pertenencia-y-autoria.md)— y [`03·D5`](base/03-datos.md) de 640 a 304, ganando además su excepción escrita en la forma que pide [`20·M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md). Las dos pasaron a **CUMPLE**: las reglas reprobadas bajan de 60 a 58.

**Y un efecto que conviene saber antes de tocar otra:** cambiarle el título a una regla le mueve el ancla, y las citas a esa ancla quedan rotas **sin que `validar.py estandar` diga nada**. Lo destapó `citas.py` al querer reescribir dos capítulos que citaban a `D8` por su título viejo.

## 23.12.0 — 2026-08-18

**MENOR** (la instalación deja una carpeta más; ningún proyecto tiene que hacer nada).

**Cuando el estándar corregía algo que un proyecto había reportado, el aviso de vuelta llegaba a uno de nueve.** Los otros ocho no tenían dónde recibirlo, y nadie se enteraba de que se había perdido.

Ahora la instalación deja puesta la carpeta del backlog, y los proyectos que ya estaban la reciben la próxima vez que se pongan al día. Y si aun así un aviso no puede llegar, se dice a quién no llegó en vez de callarlo.

**El detalle.** Es el [pendiente 61](pendientes/hecho/el-aviso-de-vuelta-llega-a-uno-de-nueve.md), con sus tres decisiones tomadas por el usuario. `pendientes/` entró a `CARPETAS_BASE` de [`instalar.py`](validadores/instalar.py) y a [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), a la que se le volvió a aplicar el checklist. `cerrar.avisar()` devuelve ahora dos listas —lo entregado y lo que no— y `cerrar.py` imprime la segunda con el motivo. **No se le inventa la carpeta a ningún repositorio ajeno**, que era la decisión de fondo: lo que cambió es que el silencio se acabó. 9 casos nuevos en [`test_aviso_de_vuelta.py`](validadores/tests/test_aviso_de_vuelta.py).

## 23.11.2 — 2026-08-18

**PARCHE** (cambia una palabra; nada de lo que se exige cambia).

**El estándar usaba una palabra del oficio que nunca definió.** Llamaba «corrida» a ejecutar las pruebas, y quien no es del gremio no sabía si eso es una prueba, un grupo de pruebas o un día entero de trabajo. De eso dependía cómo se llena una columna del informe de pruebas.

Ahora dice «ejecución». El verbo se queda: *«las pruebas se corren»* se entiende bien y no se tocó.

**El detalle.** Es el [pendiente 26](pendientes/hecho/corrida-y-ejecucion-en-el-estandar.md), decidido por el usuario. Cambian ocho archivos de `base/` y `plantillas/`, incluida la entrada «Alcance de corrida» del [glosario](base/glosario.md) y el texto de [`02·F5`](base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), a la que se le volvió a aplicar el checklist porque editar una regla anula su sello — la fila 4 sigue en ❌ por el mismo motivo de antes, ajeno a la redacción. Queda a propósito *«la numeración corrida entre sesiones»* de [`plantillas/sesion.md`](plantillas/sesion.md): ahí la palabra significa otra cosa.

## 23.11.1 — 2026-08-18

**PARCHE** (se arregla un defecto de la instalación; no cambia nada de lo que se exige).

**Poner al día un proyecto pedía hacerlo dos veces, y dejaba una anotación de más.** La instalación escribía su constancia y, en la misma corrida, decía que faltaba escribirla. Al correrla otra vez —como el propio mensaje pedía— escribía una segunda constancia, vacía, siete segundos después de la primera.

La causa era cómo se ordenaban esas anotaciones: se comparaban como texto, y así la versión «23.10.0» quedaba antes que la «23.5.0», porque el uno va antes que el cinco. Leyendo la vieja como la última salían las dos cosas a la vez. Ahora se comparan como números.

**El detalle.** Es el [pendiente 62](pendientes/hecho/el-instalador-pide-una-segunda-pasada.md), reportado por `shopnest-mesa` al subir del `23.5.0` al `23.11.0` el mismo día. `versiones.registros()` ordenaba por `(fecha, sufijo)` y dejaba la versión fuera del criterio; con los dos registros del mismo día empataban y el desempate caía en el orden alfabético del nombre. De ahí salían los dos síntomas: el checklist leía la versión vieja como «última» y pedía el registro, y `registrar_version` creía que la versión había subido y escribía otro.

Se reabrió la fase [`A-EP-007-HU-006`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/README.md) en vez de abrir una nueva, con su ciclo 3 y 15 casos en [`test_el_registro_de_version_no_se_duplica.py`](validadores/tests/test_el_registro_de_version_no_se_duplica.py).

**Por qué pasó las pruebas la primera vez:** el caso que lo cubría montaba **un** solo registro, y con uno no hay orden que equivocar. El caso estaba bien escrito; el montaje no alcanzaba.

## 23.11.0 — 2026-08-18

**MENOR** (una regla nueva sobre cómo trabajar; ningún proyecto tiene que cambiar nada).

**Trabajar con dos ventanas abiertas sobre lo mismo hacía perder trabajo.** Cada una anotaba el número de la versión cuando empezaba, no cuando terminaba, y como las dos empezaban con el mismo número las dos escribían el mismo. Pasó cuatro veces en tres archivos distintos, y una de esas veces se perdió una anotación entera.

Ahora la norma es mirar el dato justo antes de escribirlo, no al empezar. Eso quita de encima la pregunta de si hay alguien más trabajando: si se mira en el momento, no hace falta saberlo.

**El detalle.** Nace [`20·M18`](base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md) —*lo compartido se lee un instante antes de escribirlo*—, que extiende a [`M10`](base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): `M10` ya pedía que el cambio, su entrada y la subida fueran en el mismo movimiento, pero no decía **cuándo** se lee lo que se va a escribir. Es el [pendiente 22](pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), cerrado como la fase [`A-EP-002-HU-006`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/README.md) con sus dos criterios en cumple. La comprobación es [`validadores/numeracion.py`](validadores/numeracion.py), dentro de `validar.py versionado`, con 19 casos.

**Lo que destapó la simulación:** el cruce se rompe de dos maneras y solo una deja rastro. Si al resolver el choque se conservan las dos entradas queda un número repetido, que se ve; si se conserva una, **falta una entrada y no se ve**. Por eso el registro tiene dos `15.4.0` —marcadas, no renumeradas: un proyecto pudo haberla adoptado— y por eso la regla vale más que su validador, que solo llega después.

## 23.10.0 — 2026-08-18

**PARCHE** — se anotó que una regla ya existente cubría un caso que parecía sin resolver. **Ninguna regla cambió de texto.**

La duda era: cuando lo que se construye no es un programa sino un documento, ¿hay que escribir además un papel aparte que explique qué se va a hacer? Resulta que el estándar ya lo contestaba, y hacía meses: **lo que la historia dice que hay que lograr es ese papel.** Nadie lo había buscado.

Se intentó agregarlo como regla nueva y salió mal: lo escrito chocaba con otra regla del mismo capítulo. Se devolvió todo a como estaba.

**El detalle.** Es el [pendiente 20](pendientes/hecho/cuando-la-historia-hace-de-especificacion.md), cerrado citando [`02·F19`](base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) —*«la redacción del CA es la especificación funcional»*, desde la v3.1.0— en vez de escribir nada. La frase que se había agregado a [`02·F2`](base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) chocaba con [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), que prohíbe fusionar eslabones de la cadena; `F2` volvió a su texto y a su sello originales. Lo destapó una pregunta del usuario, no una comprobación — y de ahí salió la fase [`A-EP-005-HU-010`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo/), que hace llegar las reglas relacionadas al escribir.

## 23.9.0 — 2026-08-18

**MENOR** — las entradas de este archivo empiezan ahora explicando, en dos frases y sin palabras raras, qué cambió y por qué. Los nombres de archivo y las referencias internas siguen estando, pero más abajo.

Se cambió porque se le mostró una entrada vieja a quien no había seguido el trabajo y no entendió nada. No era una entrada mala: se revisaron las 83 y **ninguna** se entendía sin conocer el proyecto por dentro. Setenta y cuatro empezaban nombrando un archivo.

Las 83 anteriores se quedan como están. Reescribirlas es otro trabajo y no corre prisa; lo que corría prisa era que la próxima naciera legible.

**El detalle.** Nace [`20·M17`](base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), con su checklist en CUMPLE, y `validar.py metareglas` avisa cuando la entrada de la versión vigente abre con un identificador de regla, una ruta o jerga de la casa. Sale del `CA-03` de [EP-002 · HU-002](documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/HU-002-registro-de-cambios.md), que exige justamente eso y nunca se había comprobado con un lector de verdad.

---

## 23.8.0 — 2026-08-18

**MENOR** — los nombres de los roles estaban en inglés y ahora están en español: Explorer pasa a Explorador, Designer a Diseñador, y así con trece. La palabra «spec» pasa a «especificación».

Se cambió porque el estándar exige escribir en español todo lo que tenga traducción usada, y estos nombres se habían quedado sin traducir. Un proyecto al día no tiene que hacer nada: lo que cambia es cómo se llaman las cosas.

**El detalle.** Lo pide [`01·C20`](base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica), y eran **211 apariciones en 39 archivos**.

| Antes | Ahora |
|---|---|
| Explorer · Proposer · Designer | Explorador · Proponente · Diseñador |
| Épica Writer · HU Writer · Spec Writer | Escritor de épica · de historia · de especificación |
| Task Planner · Implementer · Verifier | Planificador de tareas · Implementador · Verificador |
| Reviewer · Orchestrator · Researcher | Crítico · Orquestador · Investigador |
| spec | especificación |

**Cuatro archivos cambiaron de nombre**, con sus citas arrastradas por `cerrar.mover`: `02·F2`, `13·DOC3`, `13·DOC6` y la plantilla de especificación de módulo. [`00·ID6`](base/00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md) se reselló, porque editar el texto de una regla anula su checklist.

**Queda uno a propósito:** la carpeta `skills/generar-spec-modulo/`. El nombre de una skill es cómo se la invoca, así que renombrarla cambia comportamiento y no solo texto.

---

## 23.7.5 — 2026-08-18

**PARCHE** — diez reglas que solo sobraban de largo caben ahora en el molde. **Ninguna cambia lo que exige.**

### Diez de una sola pasada, y por qué se podían hacer juntas

De las 70 reglas en NO CUMPLE, **quince fallan solo la fila 10** —el cuerpo de cuatro líneas de [`20·M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)— y diez de esas son puro exceso de explicación: no hay que partirlas, ni derogarlas, ni decidir nada.

**Es el único trabajo grande del [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) que no depende de una decisión.**

| Regla | Antes | Después |
|---|---:|---:|
| [`01·C13`](base/01-conducta.md#c13--preguntas-de-análisis-van-en-chat-abierto-no-en-formulario-cerrado) | 802 | **306** |
| [`09·G9`](base/09-git.md#g9--la-historia-de-usuario-es-la-unidad-del-commit) | 552 | **319** |
| [`01·C19`](base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) | 533 | **317** |
| `01·C12` · `01·C11` | 462 · 461 | **269** · **278** |
| [`04·S1`](base/04-seguridad.md#s1--autorización-en-cada-acción-sensible) · `04·S2` | 437 · 349 | **311** · **295** |
| `09·G7` · `17·I1` · `03·D3` | 421 · 395 · 378 | **270** · **293** · **306** |

Reglas en NO CUMPLE: **70 → 60**.

### Lo que sobra casi siempre es el porqué, y la regla ya lo decía

En **ocho de las diez** lo que se fue era razonamiento — por qué sobre-verificar molesta, por qué el formulario cerrado empobrece la respuesta, por qué lo que no se versiona se pierde. La fila 10 lo dice ella misma: *si no cabe, o son dos reglas o se está contando el porqué, que va a `notas/`*. **El diagnóstico acertó ocho de diez veces.**

### El bloque de ejemplo era espacio gratis y nadie lo usaba

La fila 10 mide **solo el cuerpo**. Un ejemplo largo no cuesta nada; una enumeración en el cuerpo cuesta todo. Y aun así las reglas más largas tenían ejemplos cortos — `01·C12` llevaba tres ejemplos de adjetivo **en el cuerpo** teniendo su bloque justo debajo.

**La forma de acortar sin perder nada estaba disponible desde el principio.**

### Nada se perdió, y se comprobó punto por punto

Los tres puntos de `D3`, los tres de `S1`, los cuatro de `S2`, los tres estados de `I1`, los tres criterios de `C13`. **Y ninguna excepción se tocó** — es lo único de una regla que no se puede resumir sin cambiar qué permite.

**Cada sello dice de cuánto a cuánto y qué texto salió**, para que quien lea dentro de un año sepa si lo que falta se perdió o se movió.

### Lo que **no** se tocó, de las quince

`03·D8`, `04·S9` y `04·S10` tienen dentro **un procedimiento**, no una explicación: es el caso de anexo. `05·E4` ya tenía decidido que su escala se va a un anexo, y `02·F13` se reescribió hace días.

**`04·S9` tiene además un motivo propio:** es **el único modelo de excepción completa del cuerpo** —condición, límite y autorizador—, y acortarla de paso entre otras nueve es la forma de perderlo.

**Y queda una deuda dicha:** el porqué que se sacó **no se escribió en `notas/`**. No se perdió —los sellos dicen qué salió de cada regla— pero no está donde `M5` manda.

Fase: [`E-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/E-EP-001-HU-009-las-que-solo-sobraban-de-largo/).

---

## 23.7.4 — 2026-08-18

**PARCHE** — dos reglas enlazaban a su vecina **y además la copiaban**. Se quedan con lo suyo; **ninguna exigencia desaparece del cuerpo**.

### El defecto se leía como diligencia

[`20·M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) pide que lo que ya dice otra regla esté **enlazado en vez de copiado**. [`07·Q7`](base/07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) y [`12·PR4`](base/12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes) hacían las dos cosas: **el enlace estaba puesto** y el texto repetido debajo.

Por eso duraron. Un enlace delante de un texto repetido se lee como cuidado, no como duplicación: **cumplían la mitad que se ve.**

| Regla | Se fue | Quedó |
|---|---|---|
| `07·Q7` | el criterio de alcance, que es [`01·C3`](base/01-conducta.md#c3--quédate-en-tu-tarea) | `C3` como motivo enlazado, y decirlo para su tarea |
| `12·PR4` | lo de logs, que es [`05·E5`](base/05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles) | pantallas, reportes y mensajes a terceros |

### La forma correcta ya estaba escrita en otra regla del mismo cuerpo

[`14·EST3`](base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `01·C3` **el mismo criterio de alcance** que `Q7`, y estaba en CUMPLE: la nombra entre paréntesis como el **motivo** y todo lo demás es suyo. `Q7` reformulaba el criterio entero antes de enlazarlo.

**Faltaba leerlas juntas.** El análisis del 2026-08-07 ya las había nombrado en la misma línea.

### Tres capas del mismo criterio, y solo una aportaba

[`00·N6`](base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada) (blindada) → `05·E5` → `12·PR4`, cada una reformulando a la anterior. La única parte que no dice ninguna otra regla es **la mitad de pantallas y reportes de `PR4`** — `E5` habla de logs. Es lo que la salvó de derogarse.

**Y su ejemplo se quedaba ilustrando lo que la regla dejó de decir:** era de logs. Un ejemplo así es peor que ninguno, porque manda a buscar la exigencia donde ya no está. Se cambió con ella. `PR4` además **declara ahora `depende de 05·E5`**, en una de las tres formas de [`20·M7`](base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md): la relación existía y no estaba dicha.

### Lo que **no** hace

**La categoría queda a medias, y se dice.** Siguen repitiendo `12·PR3` —que no exige nada propio—, `01·C16` —cuyo arreglo pasa por normalizar el bloque `Encadenamiento` en cuatro reglas a la vez— y [`04·S7`](base/04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas), cuyos dos sellos prescriben **derogarla** en favor de [`10·DEP3`](base/10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día).

**Las tres necesitan una decisión, no una redacción.** Derogar obliga a adoptarlo ([`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) en todos los proyectos.

Reglas en NO CUMPLE: **72 → 70**. Fase: [`D-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/D-EP-001-HU-009-enlazar-en-vez-de-repetir/).

---

## 23.7.3 — 2026-08-18

**PARCHE** — cuatro reglas nombraban un stack, un dominio o una herramienta. Se dicen en concepto; **ninguna cambia lo que exige**.

### Quien heredaba el estándar leía reglas escritas para el stack de otro

[`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) manda que la base no nombre lenguaje, framework, motor, herramienta ni dominio real. Cuatro reglas lo hacían:

| Regla | Decía |
|---|---|
| [`01·C10`](base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) | `SQLite`, `MariaDB`, `React`, `Django` y «este ERP» |
| [`01·C15`](base/01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa) | «el módulo Aportes», de un proyecto real |
| [`01·C16`](base/01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo) | Las órdenes de lectura y edición del agente, y dos del control de versiones |
| [`04·S10`](base/04-seguridad.md#s10--no-mates-procesos-globales--solo-pid-exacto-y-estrictamente-necesario) | `node` y `php` |

**No rompe nada, y por eso duraba:** un proyecto lee la regla, la entiende a medias y la aplica peor.

### `C10` no pasaba la pregunta que ella misma manda hacerse

Es la regla que enseña a decidir si algo es transversal o local, y **su criterio para decidirlo nombraba dos frameworks**: *«¿esta regla tendría sentido en un proyecto React + Django de otra empresa?»*. Ahora pregunta por otra empresa, otro lenguaje y otro negocio.

### La cuarta la encontró el programa, no una lectura

`S10` no estaba en la lista, y su sello explica por qué: **sí había argumentado la fila 5** —para defender `killall`, `pkill` y `taskkill`— y **al hacerlo la dio por revisada**. Los dos intérpretes estaban tres líneas más arriba.

**Un argumento sobre una fila no es una revisión de la fila.** Quien lee el sello ve que alguien la miró; no ve qué parte miró.

Y el detector callaba la mitad: `node` no estaba en su lista, así que de los dos nombres solo reportaba `php`. Ahora conoce `node`, `deno`, `bun`, `dotnet` y `softdeletes` — **solo lo que se le escapó de verdad**, porque una lista inflada por precaución empieza a reportar de más y una comprobación que reporta de más se apaga.

### Lo que se conserva, y por qué se escribió en una prueba

**`killall`, `pkill` y `taskkill` se quedan.** No son producto ni framework: son cómo se llama la misma acción en cada sistema, y quitarlos deja a `S10` sin decir qué prohíbe.

**Tienen su caso de prueba, y es el que más pesa de los nueve.** Un criterio que solo vive en un sello se pierde; uno que vive en una prueba se defiende solo — sin él, la próxima pasada los borra creyendo que mejora.

**Y [`04·S11`](base/04-seguridad.md#s11--escritura-contra-el-almacén-productivo-requiere-autorización-por-operación) sigue nombrando `SoftDeletes`**, también a propósito: ahí el nombre del método **es el argumento** —suena a borrar y escribe—, así que reescribirlo es parte de partir la regla. La prueba contra `base/` no exige cero: exige exactamente esa lista.

### El costo, dicho

`C10` pasó de 1724 a 1780 caracteres. **Escribir en concepto es más largo que nombrar la herramienta**, y es por eso que el nombre propio sobrevive: se lee más fácil y convence más. El ejemplo con código real de `03·D8` duró cuatro meses.

Fase: [`C-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/C-EP-001-HU-009-las-tres-reglas-con-nombre-propio/).

---

## 23.7.2 — 2026-08-18

**PARCHE** — dieciséis sellos de checklist decían dos cosas contrarias. Se corrige la descripción del veredicto; **ninguna regla cambia de texto**.

### La tabla decía una cosa y su propio párrafo, otra

Cada bloque de checklist tiene dos mitades: una tabla de veinte casillas y un texto que explica qué falla. **En cinco reglas no coincidían** — el texto reprobaba una fila que la tabla mostraba en ✅.

**Pesa porque la tabla es lo que se lee.** Nadie recorre veinte filas de prosa: se mira el renglón de emoticones y se sigue. Cuando las dos mitades se contradicen, gana la que se ve, que era la falsa.

**El defecto no era de juicio, era de transcripción.** En cuatro de los cinco se corrió **una casilla del bloque `C`** — siete seguidas, sin encabezado por columna, y contar de memoria hasta la séptima falla. Es exactamente lo que un programa hace sin equivocarse y una persona no.

**Y en los tres del capítulo `01` la fila que se perdió fue siempre la 5:** la que dice que la base no nombra tecnología. Escrita en el texto las tres veces, y las tres veces sin llegar a la tabla.

### Diez resúmenes que no cuadraban con su tabla, y un sello apilado

La línea de totales de diez sellos decía una cuenta y su tabla tenía otra — **nueve por el mismo lado**, una N/A de más y un ✅ de menos. Se recalcularon desde la tabla, que es lo que alguien puede verificar casilla por casilla.

Y [`20·M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) llevaba **dos bloques de checklist superpuestos** desde el 2026-08-07, el de la `v2.1.0` encima del de la `v2.2.0`: quien leía de arriba abajo se quedaba con el viejo, que además tenía mal la cuenta. Un sello se reemplaza, no se apila. Es la regla que dice que ninguna regla nace fuera del procedimiento.

### Tres comprobaciones para que no vuelva

`validar.py metareglas` reporta ahora el sello cuyo texto reprueba una fila que su tabla da por buena, el resumen que no cuadra con su tabla, y la regla con dos sellos.

**Se escribieron antes de corregir nada, a propósito.** Al revés se habrían estrenado sobre un cuerpo ya limpio: cero hallazgos y ninguna forma de saber si sirven. Así, los cinco los encontró la comprobación — y el falso positivo también.

**Lo difícil no era encontrar: era no inventar.** La primera corrida reportó seis, y el sexto estaba bien: un sello en CUMPLE que cuenta qué reprobaba **antes** de corregirlo. Un CUMPLE ya no se compara contra su prosa; lo que sí se le exige es que su tabla no traiga ni un ❌. La mitad de los quince casos son de silencio, porque una comprobación que reporta de más se apaga a la semana.

### Lo que esto **no** hace

**No arregla ninguna regla.** Las 72 en NO CUMPLE siguen siendo 72, y [`01·C10`](base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) sigue nombrando tecnologías concretas. Lo que cambió es que ahora su tabla lo dice. Eso es el [19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

Fase: [`B-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/B-EP-001-HU-009-el-sello-no-se-contradice/).

---

## 23.7.1 — 2026-08-18

**PARCHE** — el aviso de vuelta de la 23.7.0 estaba escrito y probado, y **el comando no lo llamaba**.

### Lo que la 23.7.0 afirmaba y no era

La entrada de abajo dice *«el aviso lo escribe `cerrar.py` al cerrar»*. La función existía, tenía sus doce casos y todos pasaban — pero `main()` nunca la invocaba. **Cerrar un pendiente no avisaba a nadie**, que es exactamente el defecto que [`02·F24`](base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md) vino a cerrar.

**Lo destapó correr el comando de verdad**, no una prueba. Las pruebas llamaban a `avisar()` directamente, así que verificaban la pieza sin verificar que estuviera conectada.

### Y al conectarlo salieron dos más

- **El estándar se mandaba un aviso a sí mismo.** Está en su propio registro, y la comparación de rutas era por texto: el registro escribe `c:\` y el comando `C:\`. Ahora se compara con `normcase`.
- **El archivo se llamaba `algo.md.md`.** El destino ya traía su extensión.

Los tres tienen su caso ahora, y los dos nuevos comprueban **lo que se vio fallar**, no lo que debería pasar.

### Lo que dejó el primer envío real

Llegó a **un** proyecto de nueve, aunque la ficha decía «a todos»: los otros ocho no tienen carpeta `pendientes/` y a un proyecto que no lleva backlog **no se le inventa**. Queda anotado en el [61](pendientes/hecho/el-aviso-de-vuelta-llega-a-uno-de-nueve.md), porque lo que falta no es el aviso — es que ocho proyectos no tienen dónde escribir un pendiente.

---

## 23.7.0 — 2026-08-18

**MENOR** — el defecto del estándar se reporta, y al corregirlo el estándar avisa de vuelta. Aditivo: un proyecto al día no tiene que hacer nada.

### La regla que faltaba: `02·F24`

Nace [`02·F24`](base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md). Un proyecto que encuentra un defecto del estándar tenía tres caminos y **ninguno escrito**: parcharlo por su cuenta —y pisar a los demás—, anotarlo solo en su repositorio —donde el estándar nunca lo ve— o no hacer nada. Los tres pasaron en `shopnest-mesa` el mismo fin de semana, y ninguno incumplió nada, porque la regla no existía.

**Va al capítulo `02` y no a la épica de instalación:** lo que gobierna es un paso del flujo —qué hace el agente cuando lo que hay que arreglar no es suyo—; la instalación es por dónde viaja el aviso, no de qué trata la regla.

**Y cierra el choque con [`02·F20`](base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md):** `F20` manda parar y proponer, y no decía a dónde va lo propuesto cuando es del estándar. Ahora `F20` para y `F24` dice a dónde.

### El paso que nadie hacía era el sexto

Los siete pasos estaban dictados desde el 2026-08-16. Los cinco primeros se venían haciendo por criterio de cada sesión; **el aviso de vuelta no lo hacía nadie**, y sin él el séptimo —el pendiente del proyecto queda abierto hasta confirmar— deja pendientes abiertos para siempre: nadie vuelve a mirar el repositorio ajeno.

Ahora lo escribe [`validadores/cerrar.py`](validadores/cerrar.py) al cerrar, porque **el aviso es parte de cerrar**: un programa aparte abre la puerta a cerrar sin avisar, que es justo el defecto.

**Escribe un pendiente y nada más — nunca toca código**, y hay una prueba que compara la raíz del proyecto antes y después. Escribir en el repositorio de otro es bastante delicado como para que el alcance sea de una línea. Es idempotente, va solo a proyectos del registro, y al que no lleva backlog no se le inventa la carpeta.

### Dos plantillas, cada una nombrando a la otra

[pendiente-reportado](plantillas/pendiente-reportado.md) —el del estándar— y [pendiente-de-seguimiento](plantillas/pendiente-de-seguimiento.md) —el del proyecto, que **no se cierra al reportar**. Se nombran entre sí a propósito: uno sin el otro es exactamente la mitad que falló los dos días de agosto que originaron esto.

### Y se comprueba por programa

`validar.py pendientes` reporta el pendiente que dice venir de un proyecto sin nombrarlo — casilla vacía o con el molde `«…»` todavía puesto. **Los 34 del backlog pasan sin tocar ninguno**, que es la señal de que la regla describe lo que ya se hacía bien en vez de inventar una exigencia.

Fase: [`A-EP-007-HU-008`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/) · pendiente [36](pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md).

---

## 23.6.0 — 2026-08-18

**MENOR** — el enganche que recuerda escribir la señal, y su molde recortado. Aditivo.

### El recordatorio llega en el turno, no al cerrar

Nace [`validadores/hook_senales.py`](validadores/hook_senales.py), conectado a `UserPromptSubmit`. Al cerrar la sesión no sirve: **un chat no tiene final** y nadie sabe cuál fue el último mensaje hasta mucho después.

**Lo difícil no era avisar: era que no se volviera ruido**, que es lo que pasa con un aviso en cada turno. Tres condiciones lo evitan, y las tres tienen prueba: una vez por sesión, solo si el proyecto lleva señales, y **nunca escribe una señal** — reconocer qué merece serlo es criterio del agente.

La marca de «ya avisé» vive dentro del propio archivo, en un comentario invisible al leerlo. Un temporal se borraría al reiniciar y el aviso volvería.

### El molde de la señal pasa de siete campos a cuatro

**Qué pasó · por qué importa · qué se decidió · dónde queda.** Siete campos se llenan las dos primeras veces, y a la tercera la señal no se escribe — que es peor que escribirla incompleta.

Nada se pierde: la fecha y el autor los guarda el control de versiones.

### La plantilla dice qué es señal y qué es pendiente

Lo que se aprendió va a las señales; lo que falta hacer, a `pendientes/`. **Los dos salen del mismo momento y por eso se confunden**, y una misma conversación suele dejar las dos.

## 23.5.0 — 2026-08-18

**MENOR** — una regla nueva de conducta. Aditiva: ningún proyecto al día tiene que hacer nada.

### `01·C23` · Busca en el repositorio antes de preguntar

Antes de pedirle una decisión al usuario se busca si ya la dejó escrita, **en este orden**: la historia y su §9 · la épica · el resumen de sesión · el histórico · la memoria. De lo más específico a lo más general, parando en cuanto se encuentra.

Si está, se sigue **citando dónde** —o se muestra, si contradice lo pedido—. Si no, se pregunta **diciendo dónde se buscó**.

- **De dónde sale:** el 2026-08-14 el agente preguntó en qué orden trabajar dos historias y ofreció tres opciones. La respuesta estaba en la §9 de una de ellas. **La pregunta tenía premisa falsa:** cualquiera de las tres respuestas habría contradicho algo ya decidido.
- **No reduce las preguntas, cambia cuáles.** Preguntar lo que de verdad no está decidido es lo que evita adivinar.
- **Extiende [`01·C7`](base/01-conducta.md#c7--ante-dos-lecturas-pregunta)**, que manda preguntar ante dos lecturas y **da por hecho que el dato no está**.
- **Validable a medias, y así queda registrada:** que el agente haya buscado no lo puede ver ningún programa; que la respuesta traiga su cita, sí — y esa mitad queda pendiente.

**El orden no salió de una preferencia:** salió de dónde el estándar ya manda escribir cada cosa. Una decisión sobre una historia vive en la historia antes que en el histórico.

**Dos cosas las destapó el plan de pruebas, no la lectura.** La primera redacción no cubría el `CA-03` —mostrar la contradicción— y no cabía en el molde: 368 caracteres para 320. Se corrigió la regla, no el criterio, y el porqué del orden se fue a la historia.

## 23.4.0 — 2026-08-18

**MENOR** — cuatro comprobaciones nuevas, una herramienta que mueve sin romper, y un procedimiento que se va a su capítulo. Aditivo: ningún proyecto al día tiene que hacer nada.

### Ningún validador termina en silencio

**Treinta y tres de los cuarenta y cinco programas de `validadores/` salían con código 0 sin imprimir nada.** Un módulo que calla no es que falte: **afirma** — sale igual que cuando ha mirado todo y está en orden. Una fase se lo creyó y escribió «cero enlaces rotos» sobre veinte.

Ahora cada uno muere diciendo por dónde se corre, con su subcomando exacto, y sale con **código 2**: ni 0 ni 1, para que «no comprobé nada» no se confunda ni con «todo bien» ni con «hay fallas».

- **`validar.py metareglas`**, que faltaba. Es el único programa que comprueba once de las veinte filas del [checklist del estándar](base/20-meta-reglas/checklist.md) —entre ellas la 5, que `M3` necesita, y la 15, que impide que una regla normal mande sobre una `[BLINDADA]`— y no tenía por dónde correrse desde el 2026-08-14.
- La prueba que lo protege **lee los módulos del disco, no una lista**, así que el programa número 46 entra solo. Uno de sus casos comprueba que la lista no esté vacía: un barrido sobre cero archivos pasaría diciendo lo mismo que uno sobre cuarenta.

### Un sello de checklist vencido se reporta

Cada bloque de checklist cierra con «vale mientras el texto de arriba no cambie», y **nada lo comprobaba**. Una regla podía editarse y seguir mostrando un CUMPLE aplicado contra otro texto, otra versión y otro día. Es peor que no tener sello: el que no lo tiene al menos no engaña.

- Se compara **la fecha del sello contra la del último cambio**, y la fecha sale del control de versiones y no del disco: la del sistema de archivos cambia con un `clone`, un `checkout` o un antivirus, y daría vencidos falsos en cada máquina nueva. Sin dato **no se inventa un vencimiento**.
- Sale como **aviso**. Que un sello caducó no es que la regla esté mal escrita: es que hay que volver a mirarla.
- **Son 36 de 73.** Casi la mitad de las reglas selladas. Ese número no se sabía.

### Los enlaces y las citas dejan de reportar lo que no es

Cinco falsos positivos en `base/`, resueltos **sin tocar una línea de `base/`** — torcer el texto para callar al validador era la salida mala.

- Un enlace escrito entre comillas invertidas es una **muestra**, no un enlace: `comun.enlaces()` ya no mira ahí, igual que cualquier lector de Markdown.
- Un identificador en una **columna de ejemplos** —«Lo que sale mal»— muestra, no cita.
- La **segunda mención** del mismo archivo no pide enlace si la primera lo lleva.
- El **ancla al mismo archivo** es la forma correcta de citar a una vecina.
- Un enlace con `%20` se decodifica antes de buscarlo en disco.

**Y el reparador obedece al validador.** Medido antes de arreglarlo, `citas.py --aplicar` habría **escrito** esos cinco errores en `base/`. Si el validador no lo reporta, el reparador no lo toca.

### La carpeta del día nace con su línea en el índice

El enganche del resumen creaba la carpeta y el archivo, y no anotaba ninguno de los dos índices. Un resumen que no está en el índice es un resumen que nadie va a abrir — el defecto que el resumen existe para arreglar.

Se cerró por los dos caminos, porque hacen falta los dos: el enganche **escribe** la línea, y un validador **rompe** si falta. El enganche solo cubre lo que nazca de aquí en adelante.

**El enganche sigue sin escribir hallazgos:** poner el nombre de una carpeta en una lista no interpreta nada.

### Mover un documento ya no rompe sus citas

Nace [`validadores/cerrar.py`](validadores/cerrar.py). **No busca texto:** resuelve cada enlace contra el disco y compara rutas absolutas, así que da igual cuántos `../` lleve delante.

- Cerrar un pendiente a mano dejaba **58 enlaces rotos en 39 archivos**. Se midió al mover el 53.
- Recalcula **las dos direcciones**: lo que cita al archivo y lo que el archivo cita. Mover un documento lo baja un nivel y sus propios `../` quedan cortos.
- `mover()` sirve para cualquier `.md`, no solo para un pendiente.

### El registro de versión ya no dice que falta escribirse

El apartado «Qué quedó pendiente» se calculaba **antes** de escribir el archivo, así que el registro recién nacido se listaba a sí mismo como faltante. Ahora se calcula después: la foto se toma con el trabajo terminado.

Cuesta escribir el archivo dos veces. Es el precio de que diga la verdad.

### `base/13-documentacion/retrodocumentacion.md`

**Un procedimiento no es un molde:** no se copia ni se llena, se lee y se sigue. Estaba en `plantillas/` y pasa a vivir junto a la regla que lo exige, donde ya estaba `render-local-de-md.md`. Sus citas se arrastraron con él, y sus enlaces pasaron de `«RUTA-ESTANDAR»` a rutas relativas: `plantillas/` se copia dentro de los proyectos y `base/` no.

Nace [`plantillas/README.md`](plantillas/README.md), que dice que ahí viven **dos** cosas —modelos que llena una persona y fuentes con las que el instalador genera— y trae la pregunta que las separa. Con eso, un archivo sin marcas `«…»` deja de necesitar una lista de excepciones escrita a mano.

### Reglas puestas al día

- **`02·F13`** tiene su checklist aplicado otra vez. Decía «pendiente de aplicar» desde el 2026-08-08, una forma que el validador no reconocía: figuraba como aviso cuando era una regla publicada sin sello válido. **Reprueba la fila 10** —631 caracteres para un molde de 320— y así queda escrito.
- **`14·EST3`** reprobaba la misma fila por **tres caracteres**. Se recortó el porqué y quedó en CUMPLE. No cambia qué exige.
- **`14·EST1` y `14·EST3`** quedan selladas en CUMPLE; **`14·EST2` en NO CUMPLE**, y su bloque dice por qué: son tres reglas metidas en una, y por eso ni el título puede ser imperativo ni el cuerpo cabe.
- **El capítulo `15` entero**: `IM1`, `IM4` e `IM5` en CUMPLE; `IM2` e `IM3` en NO CUMPLE. `IM2` pasa a llamarse *Guarda los tres estados y la trazabilidad de quien anula* — el título anterior nombraba un tema sin decir ninguna norma. No cambia qué exige.
- **El capítulo `11` entero**: `CFG1`, `CFG2` y `CFG4` en CUMPLE; `CFG3` en NO CUMPLE — son tres exigencias en una. A `CFG4` se le agregó el ejemplo INCORRECTO/CORRECTO que le faltaba: la bandera que se enciende al liberar y nadie quita.
- **El capítulo `12` entero**: `PR1`, `PR2` y `PR5` en CUMPLE; `PR3` y `PR4` en NO CUMPLE. `PR5` pasa a llamarse *Define cuánto se conservan y qué pasa después* y `PR2` gana su ejemplo. **`PR3` es la grave: no exige nada propio** — sus cuatro frases remiten al capítulo `04`, así que quien la cumple no hace nada distinto de cumplir aquel. Es un índice con forma de regla.
- **El capítulo `10` entero**: `DEP1`, `DEP2`, `DEP4` y `DEP5` en CUMPLE; `DEP3` en NO CUMPLE por repetir `04·S7`. **El arreglo está en el otro capítulo:** `DEP3` es el dueño correcto —una vulnerabilidad de una dependencia es asunto de dependencias— y lo que toca es derogar `S7`. `DEP3` y `DEP5` ganan el ejemplo que les faltaba.
- **El capítulo `05` entero**: `E1`, `E3` y `E5` en CUMPLE; `E2` y `E4` en NO CUMPLE. `E2` son dos exigencias y **la mitad que sobra ya se cita desde fuera** —`15·IM3` y el `13` apuntan acá para la transacción—, así que al partirla hay que llevar esas citas. `E4` no cabe: su escala de cuatro niveles es una tabla de referencia dentro de una regla.
- **El capítulo `06` entero, y es el primero que queda sin una sola regla reprobada:** `R1` a `R6`, las seis en CUMPLE. Sirve de referencia de qué aspecto tiene un capítulo al día.
- **El capítulo `07` entero**: `Q1` a `Q6` en CUMPLE; `Q7` en NO CUMPLE por reformular `01·C3` en vez de enlazarla. `Q6` gana el ejemplo que le faltaba.
- **El capítulo `08` entero**: `T2`, `T3`, `T5` y `T6` en CUMPLE; `T1`, `T4` y `T7` en NO CUMPLE. **`T7` es la regla más larga del cuerpo: 1645 caracteres para un molde de 320**, y ella misma declara que cubre «dos frentes». **`T1` es la más delicada:** su excepción deja al agente autorizándose a sí mismo a no probar.
- **El capítulo `17` entero**: `I2`, `I4`, `I5` e `I6` en CUMPLE; `I1` e `I3` en NO CUMPLE. **`I6` se llamaba «Adaptable»** —una sola palabra, que ni ordena ni enuncia nada— y pasa a *Funciona en los tamaños de pantalla que el proyecto soporta*. `I5` e `I6` ganan el ejemplo que les faltaba.
- **El capítulo `03` entero, y es el peor del cuerpo:** siete de sus ocho reglas reprueban. Solo `D2` cabe en el molde. **`D7` mide 3839 caracteres —doce veces el molde y la regla más larga del estándar—** y es un manual de ocho pasos con encabezado de regla. `D8` traía en su ejemplo el código de un stack y una entidad reales, contra `M3`: reescrito en pseudocódigo agnóstico.
- **El capítulo `04` entero, y es el que más reprueba:** diez de sus once reglas. Solo `S8` pasa. `S4` pasa a llamarse *Guarda los secretos fuera del código y rota el que se expuso*. **`04·S9` resultó ser el modelo de excepción del estándar** —la única cuya excepción declara condición, límite y autorizador—, y eso es justo lo que les falta a `08·T1`, `03·D4` y `03·D5`.
- **El capítulo `09` entero**: `G1` a `G5` en CUMPLE; `G6` a `G9` en NO CUMPLE. `G3` pasa a llamarse *Deja fuera del control de versiones los secretos y lo generado* y `G4` gana su ejemplo. **El corte que el análisis proponía para `G8` reservaba el número `G9`, y ese número ya está ocupado** por una regla que nació después: la mitad que salga se lleva `G10`.
- **El núcleo blindado, las seis:** `N2`, `N3` y `N5` en CUMPLE; `N1`, `N4` y `N6` en NO CUMPLE. **`N1` es lo más serio de la pasada: una regla `[BLINDADA]` con una excepción escrita**, cuando la cabecera del capítulo promete que nada las desactiva. El arreglo es de forma —eso no es excepción sino el alcance de la autorización— y no se toca acá: el núcleo cambia con decisión del usuario.
- **Los capítulos `18` y `19` enteros**, los dos `opt-in` de DevOps: catorce reglas, **y ninguna tiene un solo ejemplo INCORRECTO/CORRECTO**. Nacieron juntos y se escribieron de corrido. Se anota como un trabajo y no como catorce: el capítulo es la unidad, y hoy ningún proyecto los tiene encendidos.
- **El capítulo `01` y `20·M15`, los últimos que faltaban. Las 200 reglas del cuerpo tienen ya su bloque de checklist**, y **`01·C14` traía la peor cita del estándar**: atribuía a `01·C1` un texto que `C1` no dice. Es el único hallazgo de la pasada falso de contenido y no de forma. Corregida.
- **Las reglas sin sello bajan de 121 a 0**; las publicadas en NO CUMPLE suben de 7 a 72. Ese número sube porque ahora todas dicen la verdad: **el sello ya no es el problema, lo es lo que el sello dice.**

### `citas.py` no pedía enlace dos veces… salvo en el mismo renglón

La regla que nació con el pendiente 55 —la segunda mención no pide enlace si la primera lo lleva— miraba solo las **líneas anteriores**. Dos menciones en el mismo renglón se le escapaban, y el reparador quería enlazar la segunda.

Ahora mira el tramo de línea que queda a la izquierda, incluidos los enlaces que ya venían escritos. Se descubrió sellando `07·Q4`. Ese segundo número **sube porque ahora dicen la verdad**: antes no tenían bloque. El que mide el avance es el primero.

### La fila 10 medía mal, y castigaba a las reglas que citan bien

`M5` da cuatro líneas —320 caracteres— y `M15` exige que **toda** cita lleve su enlace. El conteo cobraba el marcado completo: cada enlace costaba unos cincuenta caracteres que nadie lee.

**Dos reglas del estándar tirando en direcciones contrarias, y perdía la que se cumplía.**

- De las **108** reglas que se pasaban del límite, **27 se pasaban solo por eso**. `ID3` contaba 561 y son 265.
- Ahora se mide el cuerpo **leído**: `[texto](destino)` cuenta como `texto`. Las que se pasan bajan de 108 a **78**, y ninguna de las 30 rescatadas hubo que tocarla.
- **No relaja la fila:** la regla que de verdad no cabe sigue sin caber, y hay una prueba que lo fija.
- Conviene volver a mirar cualquier lista de «reglas largas» hecha antes de esta fecha.

## 23.3.0 — 2026-08-17

**MENOR** — dos comprobaciones nuevas que cuentan lo que antes se contaba a mano. Aditivo: ningún proyecto al día tiene que hacer nada.

### La numeración de pendientes se comprueba sola

Nace [`validadores/pendientes.py`](validadores/pendientes.py) con su subcomando `pendientes`, de la fase [`A-EP-004-HU-018`](documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/A-EP-004-HU-018-el-numero-de-pendiente-libre/). Dice el próximo número libre, avisa del repetido y cruza la carpeta con su índice.

- **Al construirlo apareció que la carpeta no es la fuente de la numeración.** Al cerrarse, un pendiente se mueve a `hecho/` y **pierde su número**: `02-vigencia…md` pasa a `vigencia-y-poda-de-memoria.md`. Mirando los archivos, el 02 parece libre — y no lo está. **Quince de los cincuenta y cinco números tomados existen solo en el índice**, en su fila tachada.
- Sin ese hallazgo, el validador habría entregado el 02 al siguiente pendiente y roto en silencio toda cita al 02 anterior. Un validador equivocado es peor que ninguno, porque se le cree.
- El número que entrega es **el siguiente al mayor, no el primer hueco**: los huecos son historia, y reutilizarlos haría que «el 02» apuntara a dos cosas según cuándo se leyera.

### La corrida de fases dice cuántas HU hay y cuántas están completas

`validar.py fases` cierra con una línea nueva: `HU: 68 en total · 25 completas · 43 incompletas (F12.2)`. Sale de la fase [`A-EP-004-HU-017`](documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase/).

- **Una HU cuenta completa cuando todas sus fases tienen los cinco documentos**, no cuando alguna los tiene. Con dos fases y una a medias la historia no está terminada, y contarla completa escondería justo el trabajo que falta.
- **La línea va después de los hallazgos y aparece aunque no haya ninguno:** es el resumen de cuánto falta, no un incumplimiento más.
- **Cruza con el [pendiente 48](pendientes/48-inventario-hu.md)**, que lleva la misma cuenta a mano. Hay una prueba que compara los tres números: si se separan, una de las dos está mal y la suite lo dice.
- Los tres bordes quedan definidos y escritos en [`validadores/docs/fases.md`](validadores/docs/fases.md): árbol sin `epicas/` calla, épica sin HU no aporta, y carpeta `HU-` sin su `.md` **cuenta como incompleta** — existe como trabajo aunque le falte el papel.

## 23.2.1 — 2026-08-17

**PARCHE** — el enganche del resumen prepara su salida, como los otros cinco. No cambia qué se exige.

`hook_resumen.py` era **el único** de los seis enganches que no llamaba a `preparar_salida()`. Su texto lleva acentos y comillas angulares, así que salía en la página de códigos de la consola: quien lo leyera recibía mojibake, y con la salida en una tubería no se podía ni decodificar — dos pruebas del camino real llevaban tiempo en rojo por eso.

- **Es el pendiente [45](pendientes/hecho/instalar-prepara-su-propia-salida.md) otra vez, en otro archivo.** Allá `instalar()` se moría al imprimir una flecha porque solo `main()` preparaba la consola. Mismo descuido, misma clase de síntoma.
- **Nace la prueba que impide que se repita:** `TodoEnganchePreparaSuSalida` recorre los seis y falla si alguno no lo hace, para que la lista no quede coja cuando nazca el séptimo.
- Salió al ejecutar las fases del pendiente [48](pendientes/48-inventario-hu.md).

## 23.2.0 — 2026-08-16

**MENOR** — plantilla nueva. No cambia qué se exige: `02·F12.2` ya pedía la fase, y esto es el molde del tablero que muestra cuáles la tienen.

Nace [`plantillas/inventario-hu.md`](plantillas/inventario-hu.md), el inventario de historias de usuario: **una fila por HU y una casilla por documento** de la fase (`plan_trabajo`, `plan_pruebas`, `resultado_pruebas`, `estado-fase`, `funcionalidad_implementada`).

- **Sale de un caso real.** En este repositorio, **52 de las 66 HU** no tienen su fase completa: 49 sin ninguna carpeta de fase y 3 a medias. El inventario quedó en el pendiente [48](pendientes/48-inventario-hu.md).
- **Lleva todas las HU, también las completas.** Un tablero que solo anota lo que falta no deja decir cuántas hay ni de dónde salió el número.
- **Los dos contadores se corrigen juntos.** Al cerrar una fila, `Completas` sube uno e `Incompletas` baja uno en la misma edición; si se pierde la cuenta, se recuenta mirando la tabla.
- **Separa construcción de retrodocumentación**, que es casi todo lo que falta acá: el código existe y lo que no existe es el documento que diga con qué plan se hizo y qué salió — el mismo hallazgo del pendiente [38](pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md).

## 23.1.1 — 2026-08-16

**PARCHE** — ninguna regla del estándar queda fuera del registro de lo validable. No cambia qué se exige ni el texto de ninguna regla.

El validador de meta-reglas reportaba **33 reglas sin clasificar**, incluidos los capítulos `18` y `19` completos. Bajaron a cero en la fase [`A-EP-001-HU-009-clasificar-las-que-faltan`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/).

- **Quince ya estaban clasificadas**, y el problema era cómo: el registro decía `C1–C17` y el programa busca cada identificador literal. **Un documento que alimenta a un programa se escribe como el programa lee.**
- **Los capítulos `18` y `19` no aparecían ni una vez**, ni para decir que no se validan. Ser opt-in no exime: `20·M9` no exceptúa a las reglas opcionales.
- **`20·M15` y `02·F12` ya estaban construidas** y no figuraban entre los validadores hechos.
- La lista de validables **creció** de ~12 a ~22: clasificar de más como «no validable» era el camino cómodo.

**El [pendiente 19](pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) no cierra:** siguen las siete publicadas en «no cumple» —que necesitan una decisión de quien define el estándar— y las 121 sin bloque de checklist.

## 23.1.0 — 2026-08-16

**MENOR** — una fase ya no puede tener dos veredictos distintos sin que se note. Aditivo: no cambia ningún molde.

El veredicto de una fase se escribe **dos veces a mano** —en el §6 del `resultado_pruebas` y en el `estado-fase`— y nada comprobaba que dijeran lo mismo. Ya habían dejado de decirlo: en `A-EP-003-HU-010` el resultado decía «No cumple» y el estado-fase seguía diciendo «aprobada». El `estado-fase` es el que se mira para pasar la puerta de verificación. Se construyó en la fase [`A-EP-004-HU-014-comparar-los-dos-veredictos`](documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/A-EP-004-HU-014-comparar-los-dos-veredictos/).

- **`veredicto()` en [`validadores/fases.py`](validadores/fases.py)** compara tres cosas: el concepto, las exigencias en «No» del §5 con la fase dada por cumplida, y el conteo de criterios. Comparar solo el concepto dejaría medio archivo verificado.
- **Dos límites a propósito:** si falta uno de los dos documentos calla —una fase a medio escribir no es una contradicción—, y «Cumple, con una salvedad» no contradice a «Cumple».
- **Cuatro casos de prueba nuevos.** El repositorio pasa de 32 a 36.

**La decisión que faltaba, tomada y escrita:** compara un programa, y el `estado-fase` sigue escribiendo su veredicto. La otra salida —que lo enlace en vez de copiarlo— obligaría a reescribir todas las fases cerradas; si algún día se hace, esta comprobación se retira.

## 23.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar — la revisión de la instalación deja de decir «completo» con la cadena vacía.

`02·F0` exige `planteamiento → épica → HU → especificación → plan → código`, y la revisión no miraba ninguno de los tres primeros: un proyecto podía tener código commiteado, `prompts/` sin un solo archivo y ninguna épica, con el arranque diciendo **«13 de 13, instalación completa»**. Pasó en `shopnest-mesa`, y lo notó el usuario preguntando. Se construyó en la fase [`A-EP-007-HU-007-la-revision-ve-la-cadena`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/A-EP-007-HU-007-la-revision-ve-la-cadena/).

- **La lista de componentes pasa de 13 a 14**, con el punto `cadena` en [`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md): al menos un planteamiento en `prompts/`, y una épica si ya hay código en `proyectos/`.
- **Es el único punto que el instalador no instala**, y su columna lo dice. El planteamiento lo escribe el agente con lo que el usuario quiere; dejar la plantilla cruda sería peor, porque parecería un planteamiento y la revisión lo daría por cumplido.
- **La épica solo se exige si ya hay código.** A un proyecto recién instalado no se le pide: el ruido se deja de leer.
- **Tres casos de prueba nuevos.** El repositorio pasa de 29 a 32.

**Qué tiene que hacer un proyecto al día:** correr el instalador una vez —la huella del stack cambió— y escribir su planteamiento si no lo tiene. Hasta entonces dirá «13 de 14», que es el punto.

## 22.1.0 — 2026-08-16

**MENOR** — un programa comprueba que cada regla de negocio diga de dónde baja. Aditivo: lo que obliga ya lo declaró la 22.0.0.

La 22.0.0 fijó el molde; esta escribe el programa que lo mira. Se construyó en la fase [`A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen`](documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen/).

- **`reglas_sin_origen()` en [`validadores/plantillas.py`](validadores/plantillas.py)** marca como **falla** cada regla del §4 sin identificador de procedencia. Es falla y no aviso: una regla sin fuente ya llegó hasta un criterio de aceptación en un proyecto real, y lo que avisa se ignora.
- **Un `spec.md` ahora se reconoce.** Antes no se comparaba contra ninguna plantilla —el programa no sabía cuál le tocaba—, así que el documento más importante de un módulo era invisible para el validador de forma. Sin esto, la comprobación nueva no se habría disparado nunca.
- **Tres casos de prueba nuevos**, con las dos reglas reales del caso que lo destapó. El repositorio pasa de 26 a 29 pruebas.

**Lo primero que encontró fue deuda propia:** las dos especificaciones de este repositorio traen **31 reglas de negocio sin origen**. No se apagó la comprobación para que el número diera cero; quedaron en el [pendiente 47](pendientes/hecho/el-origen-de-las-reglas-de-negocio.md).

## 22.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar — toda regla de negocio dice de dónde baja.

El §4 del modelo de especificación pedía `«Regla — por qué existe.»`: **el porqué, nunca el de dónde**. Una regla de negocio no se inventa en la especificación de un módulo —baja de un requisito, de una historia o de una decisión—, pero como nadie lo preguntaba, una regla con buena justificación y ninguna procedencia entraba sin resistencia. En `shopnest-mesa` una así bajó sola a una decisión, una fila de trazabilidad, dos escenarios de prueba y un criterio de aceptación; tardó un día en verse, y solo porque alguien preguntó de dónde salía. Se construyó en la fase [`A-EP-003-HU-004-el-origen-de-la-regla-de-negocio`](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/A-EP-003-HU-004-el-origen-de-la-regla-de-negocio/).

- **El molde pasa a ser** `«Regla — de dónde baja (el identificador del requisito, la historia o la decisión) — por qué existe.»`, en [`plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md`](plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md).
- **Se pide un identificador, no una frase.** «Lo pidió el cliente» no se puede seguir hasta ninguna parte.
- **La regla sin procedencia no se escribe ahí:** se sube a la historia que corresponda y baja desde allá.

**Qué tiene que hacer un proyecto al día:** escribir la procedencia en cada regla de negocio que agregue de acá en adelante. **No** hay que reescribir las especificaciones ya escritas: quedan selladas con su versión, les falta un dato y no quedan inválidas.

## 21.3.1 — 2026-08-16

**PARCHE** — el programa que comprueba la `F22` queda retrodocumentado y bajo prueba. No cambia qué se exige ni una línea de producción.

El 2026-08-16 se escribió [`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) y, en la misma sesión, el programa que la comprueba — sin épica, sin historia y sin fase. El repositorio que escribe la regla, incumpliéndola mientras la escribe. Se retrodocumentó en la fase [`A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22`](documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22/).

- **Los tres criterios de la HU-015 quedaron con evidencia de una corrida real**, en [`validadores/tests/test_version_derogaciones.py`](validadores/tests/test_version_derogaciones.py): el proyecto atrasado con fases falla y la falla nombra la regla, lo ya adoptado no se vuelve a cobrar, sin fases no se cobra, y los límites callan en vez de romper. El repositorio pasa de 22 a 26 pruebas.
- **Los casos corren contra las derogaciones reales del estándar.** Si cambia la marca del encabezado que [`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) exige, la prueba lo dice en vez de pasar contra un dato inventado.
- **Lo que le faltaba al trabajo sin cadena no era documentación, era prueba.** `validadores/docs/version.md` ya explicaba las tres funciones con ejemplos; lo que nadie había escrito era con qué se comprobaban.

## 21.3.0 — 2026-08-16

**MENOR** — renombrar una sesión deja coherente el resumen que arrastra. Aditivo: ningún proyecto tiene que hacer nada.

`historico.py --renombrar` movía el resumen de la sesión a su nombre nuevo, pero adentro el enlace de vuelta a la transcripción se quedaba apuntando al nombre viejo. Es el propio estándar el que pide nombrar la sesión, y el comando que ofrecía para hacerlo dejaba el repositorio con un enlace roto. Lo reportó `shopnest-mesa` y le pasó tres veces a esta casa el mismo día. Se construyó en la fase [`B-EP-005-HU-008-renombrar-deja-el-resumen-coherente`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/).

- **`_reenlazar()` corrige el enlace de adentro del resumen**, texto y destino: un enlace que abre pero se anuncia con el nombre viejo también miente ([`13·DOC14`](base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md)). Se reemplaza el par exacto, así que un resumen que nombre otras sesiones las conserva intactas.
- **Nace la primera suite de pruebas de `historico.py`** — [`validadores/tests/test_historico_renombrar.py`](validadores/tests/test_historico_renombrar.py), tres casos: el normal, el que nombra otra sesión y el de una sesión sin resumen. El repositorio pasa de 19 a 22 pruebas.
- **La HU-008 gana su `CA-04`.** Su `RN-06` pedía el arrastre desde el principio y ningún criterio lo medía, así que no había de dónde derivar el plan ([`02·F18`](base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).
- **`validadores/docs/historico.md`** documenta `renombrar()`, `_mover_resumen()` y `_reenlazar()`, que no estaban.

## 21.2.1 — 2026-08-16

**PARCHE** — el instalador se moría al imprimir si nadie le había preparado la consola. No cambia qué se exige.

`validadores/instalar.py` escribe su avance con tildes y con una flecha `→`, y la consola de Windows tal como arranca no admite esos caracteres: al llegarle uno, el programa **se muere ahí mismo**, no instalando sino escribiendo en pantalla. Para eso existe `preparar_salida()`, pero solo la llamaba `main()` — o sea únicamente al correrlo desde la línea de comandos. Un programa que llamara a `instalar()` como biblioteca lo mataba. Se construyó en la fase [`B-EP-007-HU-001-prepara-su-propia-salida`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/).

- **`instalar()` prepara su propia salida al entrar.** Delegarlo en quien lo llame era pedirle al de afuera que conociera las tripas del de adentro.
- **Su prueba comprueba que se pone roja sin el arreglo**, que no es un lujo: el primer caso instalaba en carpeta vacía y **pasaba en verde con el defecto puesto**, porque esa corrida nunca imprime una flecha. Ahora instala, sube la versión para que los sellos queden viejos, y comprueba que la corrida medida sí imprimió una `→`.
- **Se quitó el rodeo** que la [21.2.0](#2120--2026-08-16) había puesto en su propia prueba para esquivar esto.

**Qué hacer para quedar al día:** nada. El programa vive en el estándar y los proyectos lo llaman por su dirección.

## 21.2.0 — 2026-08-16

**MENOR** — el instalador repara lo que ya estaba instalado, y registra la versión aunque no cambie ninguna plantilla. No cambia qué se exige.

**Lo que la [21.1.0](#2110--2026-08-16) arregló no llegaba a los proyectos ya instalados, y el registro de versión se quedaba atrás para siempre.** Dos defectos que reportó `shopnest-mesa` y que resultaron ser el mismo: el instalador decide si hay trabajo mirando una huella, y cuando la huella no cambia se queda quieto aunque el proyecto sí esté mal. Se cerraron juntos en la fase [`A-EP-007-HU-006-poner-al-dia-lo-ya-instalado`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/).

- **Toda copia que ya existe pasa por `_reparar_marcadores`.** Rellena en el sitio los huecos que quedaron crudos de una instalación anterior y no reescribe nada más. Sin bandera: reinstalar repara. Antes, «al día» se medía contra la plantilla central, así que una copia podía estar al día y mal escrita a la vez.
- **Lo que llena el proyecto no se toca.** `_rellenar` solo conoce los huecos que el instalador sabe calcular; `«motor»` o `«manual / pipeline»` salen intactos, y un caso de prueba cuenta los huecos antes y después para comprobarlo.
- **Subir de versión es por sí solo motivo de registro.** Antes el instalador decía «nada que registrar» y la revisión decía «falta el registro»: el proyecto se quedaba en 12 de 13 para siempre, con el aviso de instalación incompleta sonando en cada mensaje y sin más salida que editar a mano un archivo que dice que no se edita a mano. A la carpeta del propio estándar no se le escribe registro: lleva este `CHANGELOG`.
- **Se corrigió el texto de ayuda de la fila `versiones`** en [`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md), que mandaba hacer lo que el instalador ya había hecho.
- **Su prueba:** [`validadores/tests/test_instalar_reparar.py`](validadores/tests/test_instalar_reparar.py), seis casos. Los cinco automáticos corren contra una copia desechable del estándar, para poder editarle una plantilla y subirle la versión sin tocar el de verdad ([`00·N4`](base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

**Qué hacer para quedar al día:** correr el instalador una vez. Repara la copia y escribe el registro que falte, sin banderas y sin editar nada a mano. Es lo que la [21.1.0](#2110--2026-08-16) decía que no se podía.

## 21.1.1 — 2026-08-16

**PARCHE** — el revisor de enlaces daba un veredicto distinto según desde dónde se lo corriera. No cambia qué se exige.

**Un enlace bueno salía roto dentro de un proyecto.** [`validadores/enlaces.py`](validadores/enlaces.py) resolvía `«RUTA-ESTANDAR»` contra la carpeta que estaba revisando, dando por hecho que esa carpeta era el estándar. No lo es: los enganches corren el programa desde el estándar y le pasan el proyecto como `--raiz`, así que iba a buscar `«proyecto»/base/…`, una carpeta que ningún proyecto tiene — las reglas no se copian, se enganchan por su dirección completa. Dentro de un proyecto el marcador **no se resolvía bien nunca**, ni cuando estaba bien puesto.

Es la otra mitad de lo que dejó la [20.0.1](#2001--2026-08-16), y se construyó en la fase [`A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar`](documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar/).

- **El marcador se resuelve contra la carpeta donde vive el estándar.** Corriendo sobre el propio estándar las dos coinciden, así que acá no cambia nada: se comprobó comparando la salida antes y después, y son idénticas.
- **Se queda aunque la [21.1.0](#2110--2026-08-16) haga que dejen de llegar marcadores.** Aquella quita la causa; esta es la red para el que se escape mañana.
- **Su prueba:** [`validadores/tests/test_enlaces_marcador.py`](validadores/tests/test_enlaces_marcador.py). Comprueba que la misma cita da el mismo veredicto desde dos carpetas distintas, y que lo que no resuelve se sigue reportando — un arreglo que callara sería peor que el defecto.

**Qué hacer para quedar al día:** nada. El programa vive en el estándar y los proyectos lo llaman por su dirección, así que ya corren esta versión.

## 21.1.0 — 2026-08-16

**MENOR** — arregla la instalación y suma la prueba que faltaba. No cambia qué se exige.

**Tres de los cuatro sitios donde el instalador copia no llenaban los huecos.** Solo el del `CLAUDE.md` pasaba el texto por `_rellenar()`; el del stack, el de la memoria y el de los cuatro archivos de `.agente/` escribían la plantilla cruda. Así, `«RUTA-ESTANDAR»` llegaba intacto al proyecto y la cita a la regla no abría. Lo reportó `shopnest-mesa`, mirando el enlace a [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) de su `.agente/stack-instalacion.md`.

Es la deuda que dejó cerrar la [20.0.1](#2001--2026-08-16) sin fase ni plan de pruebas — el caso que motivó [`02·F23`](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md). Esta vez sí hubo fase: [`A-EP-007-HU-001-rellenar-los-marcadores-al-copiar`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/).

- **Los tres puntos de copia de [`validadores/instalar.py`](validadores/instalar.py) rellenan.** Se verificó que el sello no se ve afectado: la huella sale del stack central, no del texto copiado.
- **Nace la primera prueba del repositorio**, [`validadores/tests/test_instalar_marcadores.py`](validadores/tests/test_instalar_marcadores.py). Se corre con `python -m unittest discover -s validadores/tests` y usa la biblioteca estándar: sin internet y sin instalar nada.
- **Qué comprueba, y qué no.** Solo los marcadores que `_rellenos()` sabe llenar. Los otros huecos —a qué se dedica el negocio, quién usa el sistema— llegan vacíos **a propósito**: los contesta el proyecto, y borrarlos sería inventar la respuesta.
- **Se comprobó que la prueba no es vacía:** con el defecto reintroducido se pone roja y nombra cada marcador.

**Qué hacer para quedar al día:** los proyectos **nuevos** nacen bien desde ya. Los que ya estaban instalados **no se arreglan reinstalando**, y son dos motivos distintos:

- Los cuatro archivos de `.agente/` no se pisan una vez creados, porque los llena el proyecto.
- El `stack-instalacion.md` sí se pisaría, pero la huella se calcula del stack central y no del archivo copiado: como la plantilla no cambió, el instalador dice «ya estaba al día» y no reescribe. Lo comprobó `shopnest-mesa` el mismo día, y quedó como [pendiente 42](pendientes/hecho/el-arreglo-del-40-no-llegaba-a-lo-ya-instalado.md).

Mientras el 42 no cierre, un proyecto viejo se repara a mano: reemplazar `«RUTA-ESTANDAR»` por la ruta del estándar, o borrar el archivo y reinstalar si todavía nadie lo había llenado.

## 21.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (cambia por dónde entra al trabajo lo que dice el backlog).

**Un pendiente se estaba ejecutando como si fuera un plan.** El backlog dice qué falta y por qué, y eso se leía como permiso para editar directo: se cambiaba el código, se subía la versión y se marcaba hecho. Sin fase no hay plan de pruebas, y sin plan de pruebas nadie escribe qué había que comprobar. Se vio el mismo día en la [20.0.1](#2001--2026-08-16): los enlaces de las plantillas se arreglaron sin fase, y la única prueba que importaba —instalar en un proyecto y hacer clic— no la corrió nadie. El defecto salió del proyecto que lo sufrió, no del estándar que lo produjo.

- **[`02·F23`](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)**: el pendiente se baja a historia de usuario de su épica y se construye como fase de esa historia. El archivo del backlog no es el plan.
- **Extiende a [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)**, y hereda su excepción: el pendiente que solo pide decidir algo o leer no es desarrollo y no abre fase.
- **Dos procedimientos decían lo contrario y quedan corregidos.** Los nueve pasos de [`20 · base.md`](base/20-meta-reglas/base.md) y el §2 del [`CLAUDE.md`](CLAUDE.md) del estándar describían cambiar una regla como *buscar → enrutar → escribir → versionar*. Eso sigue siendo cómo queda **escrita** la regla; no reemplaza la cadena.
- **Validable, falta el validador**, y así queda en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): un programa puede comprobar que el pendiente cerrado nombre su HU y su fase, pero antes hay que fijar dónde se escribe esa referencia.

**Qué hacer para quedar al día:** el pendiente que ya esté en curso se termina como venía; el siguiente que se abra entra por su HU. Lo cerrado no se reabre — salvo lo que quedó sin probar, que se retrodocumenta con su fase.

## 20.0.1 — 2026-08-16

**PARCHE** — arregla enlaces que nacían rotos. No cambia qué se exige.

**Cada proyecto nacía con las citas a las reglas rotas.** Las plantillas citan sus reglas con enlace, como pide [`20·M15`](base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md), y el destino era relativo: `../base/…`. Dentro de este repositorio abre. Pero la plantilla no se queda acá: el instalador la copia dentro de un proyecto, y allá `../base/` es la carpeta que está **encima** del proyecto — nunca el estándar. Lo reportó `shopnest-mesa`, donde `hook_md.py` quedaba siempre en rojo por catorce enlaces muertos; un aviso que siempre suena se deja de leer, y por eso se perdieron fallas reales durante media sesión.

- **Los 91 enlaces de las 22 plantillas pasan a `«RUTA-ESTANDAR»/base/…`.** El marcador ya existía y lo resuelve [`instalar.py · _rellenos()`](validadores/instalar.py) contra la carpeta donde corre el estándar. No está escrito a mano en ningún lado: si el estándar se muda, basta reinstalar desde la carpeta nueva.
- **[`validadores/enlaces.py`](validadores/enlaces.py) aprende el marcador.** Sin esto el arreglo rompía la comprobación acá: 87 enlaces daban por rotos porque el marcador solo se llena al instalar. Ahora, sin llenar, se resuelve contra la raíz del repositorio.
- **El límite:** la ruta que entra al archivo es la de la máquina donde se instaló, y los documentos generados sí se versionan. En otra máquina ese enlace no abre. No empeora nada —hoy no abre en ninguna—, pero tampoco lo resuelve del todo.

**Qué hacer para quedar al día:** volver a correr la instalación, y los enlaces quedan apuntando al estándar de esta máquina.

## 20.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (cambia cómo se entrega todo lo que el agente escribe).

**Explicar más largo no es explicar mejor.** El usuario lo cortó otra vez con dos palabras —*"menos es más"*— después de un reporte de cinco bloques y tres listas. [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) ya pedía que el texto se entienda sin saber del tema, pero eso no alcanza: un texto puede entenderse perfecto y no leerse por largo, y lo que no se lee no comunicó nada.

- **[`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)**: se entrega en la menor extensión con la que se entienda — la conclusión primero, y nada que no cambie lo que el lector va a decidir o a hacer.
- **Qué se recorta y qué no.** Sobra el repaso de lo ya dicho, la justificación que nadie pidió y el recuento paso a paso. El dato exacto nunca. Lo que no cabe corto va al archivo del repositorio que le corresponde, y en el mensaje queda su enlace.
- **Extiende a `ID7`, no la repite.** Aquella se ocupa de que se entienda; esta, de que se lea.
- **No es validable**, y así queda registrado en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): contar renglones es fácil, pero decidir cuál sobra exige entender qué cambia la decisión del que lee.

**Qué hacer para quedar al día:** nada en los archivos del proyecto; cambia cómo se escribe de acá en adelante.

## 19.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (todo proyecto con una derogación sin adoptar tiene que ponerse al día antes de su próxima fase).

**Derogar una regla no llegaba a los proyectos.** El estándar es central, así que al derogar una regla todo proyecto deja de leerla ese mismo día — pero ninguno se pone al día solo: cada uno declara su versión en su `CLAUDE.md` y ahí se queda. [`validadores/version.py`](validadores/version.py) reportaba ese desfase como **aviso**, sin límite escrito de hasta cuándo se podía sostener. Un proyecto podía quedarse tres versiones atrás para siempre y ningún reporte lo llamaba incumplimiento.

- **[`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)**: ninguna fase se abre ni se cierra mientras el proyecto declare una versión anterior a la que derogó una regla que ese proyecto cumplía.
- **Adoptar no es cambiar el número.** Lo único que se abre es la fase que adopta la derogación, una por cada HU que implementaba la regla derogada ([`02·F12`](base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)); ahí se aplica la regla que la reemplazó, y al cerrarla se sube la versión declarada. Sin eso, subir el número deja el trabajo viejo tal como estaba y la regla nueva sin aplicar.
- **El amarre es la fase, no la sesión.** Abrir y cerrar una fase ya son momentos donde alguien revisa y firma, así que la comprobación se cuelga de una parada que ya existe en vez de inventar otra. Fuera de esos dos momentos el desfase se reporta pero no detiene nada: un proyecto que solo hace el trabajo que [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) exceptúa queda marcado, no bloqueado.
- **Dos textos decían lo contrario y se corrigieron:** la nota de retroactividad de [`base/20-meta-reglas/base.md`](base/20-meta-reglas/base.md) y [`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md), que daban el desfase de versión como informativo siempre.
- **Ya la comprueba un programa.** [`version.py`](validadores/version.py) suma `derogaciones()`, `sin_adoptar()` y `validar_fase()`, y [`flujo.py`](validadores/flujo.py) —el que recorre las fases— la cobra donde hay fases. Las reglas jubiladas se leen de la marca `[DEROGADA en X.Y.Z → ver ID]` del título de cada regla, que es dato exacto; el `CHANGELOG.md` es prosa y nombrar ahí la palabra "derogación" no jubila nada. Queda un filtro fino sin hacer, anotado en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): si la regla derogada era una `*opt-in*` que el proyecto nunca encendió, hoy igual se le cuenta.

**Qué hacer para quedar al día:** mirar si entre la versión declarada y la vigente hay alguna derogación; si la hay, abrir una fase por cada HU que implementaba la regla derogada, aplicar ahí la regla que la reemplazó, y al cerrarla subir la versión declarada en el `CLAUDE.md` del proyecto.

## 18.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (cambia el nombre de una plantilla y de una ruta del proyecto).

**"Brief" se dice planteamiento.** La palabra estaba en inglés y nombraba el largo del documento, no su contenido: traducida literal queda "breve", que no dice nada de lo que hay que entender. El usuario lo destapó con un caso: alguien lee *"el brief responde qué se necesita y qué no se negocia"*, no sabe qué es, va al glosario y lo que encuentra no lo saca del apuro.

- **`plantillas/brief.md` pasa a [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](plantillas/ciclo-vida-proyectos/01-planteamiento.md)**, y el `brief.md` de la raíz a [`planteamiento.md`](planteamiento.md).
- **La ruta del proyecto pasa de `prompts/<slug>-brief.md` a `prompts/<slug>-planteamiento.md`.**
- **La palabra cambia en la zona normativa**: `base/`, `plantillas/`, `skills/`, `anatomia/` y el validador de plantillas. 30 ocurrencias.
- **Los enlaces que apuntaban al archivo viejo se corrigieron en todo el repositorio**, incluidos los de fases ya cerradas: un enlace roto no le sirve a nadie. El texto de esos registros no se tocó.

**Qué hacer para quedar al día:** renombrar `prompts/<slug>-brief.md` a `prompts/<slug>-planteamiento.md`.

**Lo que queda pendiente:** la palabra sigue escrita en `documentacion/`, `pendientes/`, `analisis/` e `historico-chat/`, que son registros de otras sesiones y de fases cerradas.

## 17.0.2 — 2026-08-16

**PARCHE** (redacción; no cambia qué se exige).

**Un glosario es un mini diccionario, y varias entradas no lo eran.** Lo destapó el usuario con un caso: alguien lee *"el brief responde qué se necesita y qué no se negocia"*, no sabe qué es un brief, va al glosario y encuentra *"el primer papel"*. No se entiende, y entonces el glosario no sirvió para lo que existe.

- **La prueba que ahora pasan las 72 entradas:** reemplazar la palabra por su definición y que la frase siga teniendo sentido. *"El **documento donde se escribe qué se necesita, antes de que exista una solución** responde qué se necesita y qué no se negocia."*
- **Cada definición empieza diciendo qué clase de cosa es** —el documento, la lista, la acción, el conjunto, el apunte— y sigue con qué hace. Antes 48 de 72 arrancaban en el aire: *"el primer papel"*, *"qué se va a hacer"*, *"lo que se escribe"*.
- **Ninguna pasa de 115 caracteres.**
- **Se quitó el anuncio del idioma, no la explicación.** *"En inglés quiere decir breve"* empieza informando algo que ya se ve: que la palabra está en inglés. Se recortó ese arranque en seis entradas y quedó solo lo que explica el nombre. Donde el idioma no es obvio se conserva: *postmortem* en latín, *meta* como "sobre", *retro* como "hacia atrás", y el inglés *hook* detrás de enganche.

La definición de **brief** es literal del usuario y no se toca.

## 17.0.1 — 2026-08-16

**PARCHE** (redacción; no cambia qué se exige).

**La columna "Qué quiere decir el nombre" estaba escrita en español de ninguna parte.** [`00·ID8`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) lo nombra en su sección 5: el español neutro, del que nadie reconoce de dónde es, delata que lo armó una máquina. Las 27 celdas llenas de [`base/glosario.md`](base/glosario.md) se reescribieron como se habla acá.

- *"Lo que se halla trabajando"* pasa a *"lo que uno se encuentra trabajando, sin andarlo buscando"*.
- *"Como la señal de una carretera"* pasa a *"como una señal de tránsito"*.
- *"Línea de montaje"* pasa a *"línea de ensamble"*; *"antes de salir"*, a *"antes de arrancar"*.
- *"Blindada contra cambios"*, que repetía la palabra, pasa a *"como un carro blindado: por más que le den, no cede"*.
- Se quitaron las comillas de las traducciones: *"En inglés, «pila»"* pasa a *"en inglés quiere decir pila"*.

## 17.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (todo proyecto al día tiene que escribir su glosario).

**Las palabras del negocio no estaban definidas en ninguna parte.** El estándar ya tiene su glosario desde la 15.3.0, pero eso define las palabras del estándar. Las del negocio de cada proyecto —cómo se llama acá un cliente, qué cuenta como pedido, qué es un cierre— seguían en la cabeza de quien las usaba, y dos documentos del mismo proyecto podían llamarle distinto a la misma cosa sin que nadie lo notara.

- **[`13·DOC23`](base/13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md)**: todo proyecto mantiene el glosario de sus términos, cada uno en una línea entendible por quien no conoce el dominio, actualizado en el mismo cambio que introduce el término.
- **La sección Glosario de [`plantillas/dominio.md`](plantillas/dominio.md)** deja de ser un espacio en blanco y dice qué entra, qué no, y cuándo se actualiza. Existía desde antes; lo que faltaba era la regla que obligara a llenarla.
- **Qué entra y qué no.** La palabra que el negocio ya trae va acá. El concepto de la base que en este proyecto se llama de otro modo va en `mapeo-nombres.md`, que sigue siendo otra cosa.
- **Validable a medias**, y así queda registrado: un programa puede ver si el glosario existe y si tiene entradas; si la definición se entiende, no.

**Qué hacer para quedar al día:** llenar la sección Glosario de `dominio.md` con las palabras del negocio que ya usan las especificaciones del proyecto.

## 16.0.0 — 2026-08-15

**MAYOR** ⚠ obliga a migrar (un plan de pruebas en curso con pasos de dos acciones hay que partirlo).

**Un paso de dos acciones pierde la mitad de lo que salió.** El plan de una fase decía *«tomar la lista de origen **y** contar cuántos términos tiene»* en una sola fila, con un solo renglón de resultado esperado. Al ejecutar quedó anotado el conteo y se perdió de dónde había salido la lista, que era lo que había que comprobar. El caso quedó en "aprobado" con la mitad sin registro, y eso no se vio hasta bajar el resultado a la forma nueva de [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md).

- **[`plantillas/ciclo-vida-proyectos/08-plan-pruebas.md`](plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)** §6: **un paso, una acción**. Cada fila lleva un solo verbo y un solo resultado esperado, con su ejemplo INCORRECTO/CORRECTO.
- **Se aplicó al plan que lo destapó**, [la fase A de EP-003 · HU-010](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/plan_pruebas.md), versión 1.1: seis pasos partidos o reescritos en CP-001, CP-002, CP-004, CP-005, CP-007 y CP-008. Ningún caso cambia lo que comprueba.
- **El resultado de esa fase pasa de «aprobada con una prueba pendiente» a «No cumple».** No es un cambio de criterio: la plantilla no admite estado intermedio y `RNF-01` no tiene caso ejecutado. Con los pasos partidos se ve además que 15 de los 33 no dejaron registro de qué salió.
- **La regla «se arranca desde cero» destapó dos pasos dados por supuestos** en el mismo plan (versión 1.2): CP-004 no decía cómo se eligen las tres entradas de muestra, y CP-006 no decía que hay que conseguir a alguien que no haya escrito el glosario — que era justo lo que tenía el caso bloqueado, sin que apareciera en ninguna fila.
- **La sección 2 de [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) pedía lo mismo dos veces** —un bloque por pareja `CA`–`CP` arriba y un «Detalle de `CP-00N`» abajo—, y quien leyera no sabía cuál mandaba. Queda un solo bloque, con sus tres partes y **cuatro reglas que dicen qué es "detallado"**: un paso por cada fila del plan, se arranca desde cero, ningún paso queda vacío, y está detallado cuando alguien que no estuvo puede repetir la prueba sin preguntar nada.

## 15.4.3 — 2026-08-15

**PARCHE** (se documenta y se prueba algo que ya corría; nadie tiene que hacer nada nuevo).

**El reparto de las reglas al abrir la sesión no estaba escrito en ninguna parte, y nadie lo probaba.** [`validadores/cargador.py`](validadores/cargador.py) manda completos los capítulos que empiezan por `00-` y `01-` y del resto manda el índice, desde la versión 5.0.0. Esa decisión solo vivía en un comentario del programa: una línea cambiada dejaba al agente sin identidad y nada avisaba.

- **[`documentacion/automatismos/spec.md`](documentacion/automatismos/spec.md)** gana la sección 4.1 con siete reglas de negocio: qué llega completo, qué llega en índice, por qué se decide por la ruta y no por el nombre del archivo, qué pasa cuando el arranque está detenido y por qué no se puede cargar todo.
- **Diez pruebas nuevas** en la clase `RepartoDeLasReglas`, y se comprobó que cazan el defecto: con el reparto roto a propósito, el capítulo de conducta deja de llegar y la prueba lo detecta.
- **Medido y escrito:** 73 KB de 369 KB, y 0,21 s el enganche que los entrega.
- **El [pendiente 25](pendientes/hecho/las-reglas-de-como-se-escribe-si-llegaban-puestas.md) se cierra por falso.** Decía que `ID8` se incumplió porque llegaba como línea de índice; llegaba completa. La causa se había deducido en vez de verificarse, y esa es la parte que no se puede repetir.

## 15.4.2 — 2026-08-15

**PARCHE** (deja escrita la pregunta que la sección ya venía respondiendo; no exige nada nuevo).

**La sección de identificación no decía qué se responde ahí.** Arrancaba directo en la tabla, así que se llenaba como un trámite. Ahora abre con su pregunta: **¿qué se está probando?**

- **[`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md)**: una línea al abrir la sección 0.
- **«Corrida» pasa a «ejecución»** en esa plantilla, y la sección 1 dice qué es: correr las pruebas de principio a fin. «Corrida» era jerga y no estaba en el [glosario](base/glosario.md) como término propio.
- **Las secciones 1 y 2 también abren con su pregunta**, y la 2 pide explicar qué problema resuelve cada pareja `CA`–`CP`, con su ejemplo: el problema, las condiciones, los pasos con lo que salió, y cómo se verificó que la pareja cumple.

## 15.4.1 — 2026-08-15

**PARCHE** (le da forma a lo que pidió la 15.4.0; no exige nada nuevo).

**El detalle de un caso quedó en tres partes, no en cinco.** Al aplicarlo a los diecisiete casos de una fase se vio que dos sobraban: los pasos esperados y los que se siguieron son los mismos pasos, así que van en una sola tabla de tres columnas —qué hacer, qué tiene que pasar y qué salió—, y el desvío se lee en la fila. El veredicto tampoco se repite en el detalle: ya vive en la tabla de casos ejecutados.

- **[`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md)**: las tres partes, con el ejemplo en esa forma.

## 15.4.0 — 2026-08-14

**MENOR** (el instalador deja una carpeta más; nadie tiene que hacer nada nuevo).

**El enganche que sostenía el resumen de la sesión no creaba el resumen.** La fase que lo construyó cerró el mismo día con sus tres criterios en "cumple", y el programa no hacía lo que esos criterios piden: los dos resúmenes que había en el repositorio los había escrito el agente a mano. Se reabrió la fase [`A-EP-005-HU-008`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md) en vez de abrir una nueva: lo que fallaba era ese trabajo, y su documentación decía que estaba hecho.

- **El archivo nace en el primer mensaje de la sesión, no al abrir.** Al abrir, la transcripción todavía no existe, y de su nombre sale el del resumen. Los dos modos del enganche lo aseguran: la sesión que se retoma lo tiene desde el arranque y la nueva en el primer turno.
- **`instalar.py` deja puesta `historico-chat/resumenes/` con su índice.** Sin ella el enganche quedaba mudo en todo proyecto que hereda el estándar, y crearla era un paso a mano que nadie había documentado.
- **El encabezado del resumen ya no enlaza `plantillas/sesion.md`.** Esa carpeta es del estándar y no viaja al proyecto: ahí el enlace nacía roto. Enlaza el índice del histórico, que el instalador sí deja en todos.
- **La corrida 2 de las pruebas dispara el enganche como orden del sistema**, con el JSON que le manda Claude Code, sobre un proyecto que arma el instalador. Ninguna precondición se monta a mano: eso fue lo que dejó pasar el defecto. La fase no se declara cumplida hasta que el archivo aparezca solo en una sesión real.
- **[`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md)**: el detalle de un caso pasa a tener cinco partes fijas — el problema que resuelve, la precondición, qué hacer para que cumpla, con qué reprueba y los pasos que se siguieron de verdad. Con el detalle a medias un caso puede pasar habiendo probado otra cosa, y eso fue lo que pasó. Queda escrito que si lo ejecutado no son los pasos de "para que cumpla", el caso no cumple, aunque haya salido bien.

## 15.4.0 — 2026-08-15  ·  ⚠ **número repetido**

> **Este número está usado dos veces**, y la de arriba es del día anterior. Lo dejaron dos sesiones abiertas a la vez sobre el mismo repositorio, que es lo que describe el [pendiente 22](pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).
>
> **No se renumera a propósito.** Un proyecto pudo haber adoptado «15.4.0», y cambiarle el número ahora le movería el piso sin que se entere. Queda marcado, que es lo honesto: quien adoptó esa versión tiene **las dos cosas**, la de arriba y esta.
>
> Desde la v23.11.0 esto no puede volver a pasar sin que se diga: `validar.py versionado` lo reporta.

**MENOR** (una sección más en una plantilla; ningún brief ya escrito deja de valer).

**El brief no decía cómo se llama el proyecto.** La plantilla tenía el nombre solo en el título, y ese título nombra el módulo o la épica. Un proyecto entero no tenía dónde decir cómo se llama, y el nombre es lo primero que heredan todos los documentos que salen de ahí.

- **Sección 0, Identificación**, en [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](plantillas/ciclo-vida-proyectos/01-planteamiento.md): nombre del proyecto, qué cubre el encargo y fecha.
- El [`planteamiento.md`](planteamiento.md) de este repositorio la estrena: el proyecto se llama **Cimiento**.

## 15.3.0 — 2026-08-14

**MENOR** (nace un documento de consulta; nadie queda obligado a nada nuevo).

**Las reglas usaban palabras que no estaban definidas en ningún lado.** Para saber qué es una especificación había que encontrar la regla que la exige; para saber qué es una señal, otra; para saber qué es una fase, un capítulo entero. El caso que lo destapó: el usuario preguntó qué significaba "spec", y la respuesta tomó tres intentos y terminó cambiando una regla.

- **[`base/glosario.md`](base/glosario.md)**: 72 términos en cuatro grupos (la cadena de trabajo, las reglas, lo que comprueba y lo que se guarda). Cada uno en una línea, con quién lo escribe, dónde vive y qué regla lo manda. Es un anexo, no una regla: no exige nada y por eso no lleva checklist.
- **Una columna dice qué quiere decir el nombre**, no solo qué es la cosa: por qué a una fase le decimos estación, de dónde sale bitácora, qué significa brief. Sin eso, un término se puede leer y seguir sin entender por qué se llama así.
- **Cada entrada enlaza a su regla y no copia su texto.** Dos copias de la misma norma se desincronizan, y manda la que nadie relee.
- **Se alcanza desde las tres puertas de entrada**: [`README.md`](README.md), [`base/README.md`](base/README.md) y [`anatomia/mapa-del-sitio.md`](anatomia/mapa-del-sitio.md).
- **Queda el inventario de lo que sigue en otro idioma**: 10 términos que se quedan con su motivo escrito y 12 que faltan traducir, con el archivo donde vive cada uno. Renombrarlos es trabajo aparte, porque rompe las citas.

Cierra la parte del glosario del [pendiente 21](pendientes/hecho/los-nombres-de-rol-en-espanol.md), que nace del hallazgo H-8 del 2026-08-14. La parte de los roles queda abierta.

## 15.2.0 — 2026-08-14

**MENOR** (una columna más en una plantilla; no invalida los resultados ya escritos).

**Un caso de prueba aprobado no decía con qué se probó.** El plan dice qué **tipo** de dato usar; el resultado decía solo "aprobado". Con eso nadie puede repetir la prueba, y un caso que no se puede repetir no es una prueba: es un recuerdo.

- **Columna nueva `Con qué se probó`** en [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md), con el ejemplo real: el archivo, el valor o el comando que se corrió.
- Su ejemplo lo deja claro: no vale *"un usuario sin permiso"*, vale *"`qa.consulta` sobre `/facturas/42/anular`"*.

## 15.1.0 — 2026-08-14

**MENOR** (dos enganches nuevos; nadie queda obligado a nada que no estuviera ya exigido).

**El resumen de la sesión dependía de que alguien se acordara.** Desde la 14.0.0 [`13·DOC22`](base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) lo exige, el modelo existe y el índice lo enlaza. Faltaba el programa. Es la misma lección de la transcripción, que solo empezó a escribirse siempre cuando la escribió un programa.

- **[`validadores/resumen.py`](validadores/resumen.py) y [`validadores/hook_resumen.py`](validadores/hook_resumen.py)**: el archivo se crea al abrir la sesión, con el modelo puesto y sin hallazgos.
- **Avisa qué falta**, una vez por cada cosa y máximo dos: que no haya ningún hallazgo, y que nadie haya dicho si la sesión se puede cerrar. La marca del aviso vive dentro del propio resumen.
- **Muestra lo que sigue abierto del propósito** que la sesión declara, y nada de otros temas. Una sesión abierta para un tema no tiene por qué ver los hallazgos de otro: eso es ruido, y el ruido se deja de leer.
- **El resumen se mueve con la transcripción** al ponerle el tema a la sesión. Los dos se llaman igual, así que renombrar solo uno dejaba el índice apuntando a un archivo que no está.
- **Lo que el enganche no hace:** escribir hallazgos ni interpretarlos. Reconocer uno es criterio, y el criterio no lo tiene un programa. Lo que sí puede es que el hueco se vea.

**Qué tiene que hacer un proyecto al día.** Correr el instalador para recibir los dos enganches. Un proyecto sin carpeta de resúmenes no se ve afectado.

## 15.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (una regla nueva que exige algo a todo proyecto al día).

**Un pendiente se estaba usando como permiso.** El repositorio tenía anotado que 354 enlaces no cumplen [`13·DOC14`](base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), y los documentos escritos ese mismo día sumaban 122 incumplimientos nuevos de la misma familia. La deuda dejaba de ser deuda y pasaba a ser costumbre.

- **[`02·F21`](base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md)**: desde que un incumplimiento queda registrado en un pendiente, un hallazgo o una señal, lo que se escriba de ahí en adelante nace cumpliendo. El pendiente guarda lo viejo y se limpia aparte; no autoriza a producir más.
- El usuario lo dijo así: *"yo antes escribía sin ortografía, pero a partir de que aprendí ya escribo con ortografía, no importa el contexto"*.

**Qué tiene que hacer un proyecto al día.** Nada hacia atrás: sus pendientes siguen como están. Lo que cambia es de aquí en adelante, y el costo de cumplirla es cero cuando el incumplimiento ya se conoce.

## 14.0.1 — 2026-08-14

**PARCHE** (enlaces; no cambia qué se exige).

**Las plantillas citaban reglas por su ID y sin enlace**, contra [`20·M15`](base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md), que exige que toda cita lleve el enlace al sitio donde vive la regla. Peor: muchas citaban sin el prefijo del capítulo —`F4`, `DOC5`, `C19`—, y así ni siquiera se sabía dónde buscar.

- **122 citas enlazadas en 23 plantillas**, cada una con su capítulo y su ruta.
- **El modelo del resumen de sesión lo deja escrito**: toda regla que se nombre va enlazada, en cualquier campo del hallazgo.

## 14.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (una regla nueva que exige algo a todo proyecto al día).

**Lo que una sesión dejaba se perdía dentro de su propia transcripción.** La transcripción prueba lo que se dijo, y por eso es larga: nadie la relee. Una sesión produjo cinco aprendizajes y nueve pendientes que hubo que ir a rescatar leyendo el chat. El molde para escribir lo que quedó existía desde la 12.2.0, pero nada lo exigía y nada lo enlazaba, así que dependía de que alguien se acordara.

- **[`13·DOC22`](base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)**: cada sesión deja su resumen en un documento aparte, escrito **en el momento en que aparece cada hallazgo**, no al cerrar. Un chat no tiene final, y lo que se deja para el final no se escribe.
- **El resumen se encuentra desde donde se busca.** El índice del histórico enlaza, en la misma línea de cada sesión, su transcripción y su resumen. [`validadores/historico.py`](validadores/historico.py) escribe ese enlace al ponerle nombre a la sesión, y solo si el resumen ya existe: un enlace roto en el índice es peor que no tenerlo.
- **Un hallazgo se nombra `AAAA-MM-DD · tema · H-N`.** Cada resumen numera los suyos desde `H-1`, así que el número solo no identifica nada. La numeración corrida entre sesiones se descartó: obligaría a un contador único, y dos sesiones abiertas a la vez lo rompen, que es justo lo que ya pasó con la versión.
- **El hallazgo que se hereda no se copia.** La sesión que retoma uno abierto lo nombra en su «viene de» y trabaja sobre el original. Dos copias del mismo hallazgo terminan diciendo cosas distintas, y manda la que nadie está mirando.
- **Cuál de los dos documentos abrir** queda escrito en [`historico-chat/resumenes/README.md`](historico-chat/resumenes/README.md): se arranca siempre por el resumen, y la transcripción se abre cuando el resumen no alcanza.
- **Toda regla que el resumen nombre va enlazada.** [`20·M15`](base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) ya lo exigía y el modelo no lo decía, así que los resúmenes citaban por ID y quien los leía tenía que salir a buscar.

**Qué tiene que hacer un proyecto al día.** Correr el instalador para recibir el modelo, y crear la carpeta de resúmenes la primera vez que la use. Lo ya escrito no se rehace y una sesión vieja sin resumen no se reabre: la norma aplica al trabajo en curso y al que viene.

## 13.1.0 — 2026-08-14

**MENOR** (dos precisiones en tres plantillas; no invalida nada escrito).

**Un veredicto de pruebas que decía "cumple con observaciones" no dice nada.** Si el carro vuelve del taller sin frenos, no está arreglado: "cumple con observaciones" era la forma amable de decir que no cumple, y quien lo lee después no sabe si podía cerrar la fase o no.

- **Los requisitos no funcionales de una HU van numerados `RNF-0N`** en [`plantillas/ciclo-vida-proyectos/04-HU.md`](plantillas/ciclo-vida-proyectos/04-HU.md), igual que los criterios de aceptación. Sin número no se pueden citar desde el plan ni desde las pruebas, y terminaban verificándose de vista.
- **Y cuentan como exigencia propia.** En [`plantillas/ciclo-vida-proyectos/08-plan-pruebas.md`](plantillas/ciclo-vida-proyectos/08-plan-pruebas.md) y [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) cada `RNF-0N` lleva su fila en la matriz y en el veredicto, y la cobertura suma criterios y requisitos por separado. En la fase donde salió esto, tres requisitos venían contados como uno solo: la cobertura decía 4 de 4 cuando era 6 de 6.
- **El veredicto pasa a ser binario** en [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) y en [`plantillas/ciclo-vida-proyectos/10-estado-fase.md`](plantillas/ciclo-vida-proyectos/10-estado-fase.md): cumple o no cumple. Lo que falte hace que sea no cumple. Los defectos ya tienen su tabla, con severidad y con quién los aceptó.
- **Cada `CP-00N` se escribe como enlace a su caso, y cada `CA-0N` o `RNF-0N` como enlace a su exigencia en la HU**, en el plan de trabajo, el plan de pruebas, el resultado y el documento de cierre. Un identificador suelto obliga a buscarlo a mano, y así es como se termina juzgando un caso sin haber leído lo que exigía. Salió de una fase real: el caso decía "los que se declaró" sin decir dónde, y quien ejecutaba acababa decidiendo la lista.

## 13.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (tres reglas nuevas que exigen algo a todo proyecto al día).

**Los huecos de un modelo se marcaban de tres formas distintas, y ninguna estaba escrita.** Al contarlo archivo por archivo: 25 de 30 plantillas usaban `«…»`, once convivían con `[texto]` y dos con `<texto>`. La convención se cumplía porque alguien se acordaba, no porque estuviera en ninguna regla. Un documento entregado a medias dejaba sus huecos confundidos con el texto, y nadie los veía al aprobarlo.

- **[`13·DOC19`](base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)**: los espacios por llenar se marcan `«…»`, la misma marca en todos los modelos. Deja escrito además qué **no** es un hueco: la sintaxis de un comando que se copia y se pega la llena quien lo corre.
- **[`13·DOC20`](base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md)**: un documento que conserva una sola marca no está terminado, y no se presenta como tal.
- **[`13·DOC21`](base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md)**: la sección que no aplica se escribe `N/A`. Dejarla marcada la vuelve un hueco; borrarla hace creer que el modelo nunca la pidió.
- **179 huecos convertidos** en 13 plantillas, sin tocar enlaces, casillas ni bloques de guía. Tres archivos de `plantillas/` quedaron sin marca a propósito: `historico-chat.md`, `memoria.md` y `retrodocumentacion.md` no son modelos que alguien llene, y así queda escrito.
- **Por qué esa marca y no otra**, con las cuatro descartadas y el motivo de cada una: [`notas/marca-del-espacio-por-llenar.md`](notas/marca-del-espacio-por-llenar.md).

**Qué tiene que hacer un proyecto al día.** Correr el instalador para recibir las plantillas nuevas. Los documentos que ya llenó no se tocan: un documento terminado no es un modelo.

## 12.4.0 — 2026-08-14

**MENOR** (precisa un campo que ya existía; no invalida los resúmenes ya escritos).

**Un problema partido en dos historias no dejaba ver cuál va primero.** Las épicas están cortadas por tipo de entregable: el documento modelo cae en una y el programa que lo llena, en otra. Un hallazgo que dispara las dos queda repartido, y entrando por cualquiera de las dos épicas el orden no se ve. Pasó con el resumen de sesión: su modelo es de EP-003 y su enganche de EP-005, y hubo que deducir a mano que el enganche va después porque escribe el archivo con el modelo adentro.

- **El campo `Dispara` de [`plantillas/sesion.md`](plantillas/sesion.md) numera las historias** en el orden en que se resuelven, y cada una dice por qué va ahí.
- **También nombra lo que las bloquea aunque el hallazgo no lo haya disparado.** Una historia vieja en backlog puede estar deteniendo a una nueva, y eso solo se ve desde acá.
- **Por qué en el hallazgo y no en la épica:** el hallazgo es el único sitio donde el problema está entero. Recortar las épicas por problema costaría rehacer las 54 historias ya colgadas.

## 12.3.0 — 2026-08-14

**MENOR** (aditivo: un campo nuevo en una plantilla; no invalida los resúmenes ya escritos).

**Una sesión que va a resolver un hallazgo no decía cuál.** El resumen de sesión guardaba de dónde nace cada hallazgo y dónde se cierra, pero no de dónde nace **la sesión**. Cuando alguien abre una sesión con un hallazgo en la mano ("trabajemos en H-4"), ese origen no quedaba escrito en ninguna parte: se perdía en la transcripción, que es justo lo que el resumen viene a evitar.

- **Campo nuevo `Viene de`** en [`plantillas/sesion.md`](plantillas/sesion.md), al principio del resumen: la fecha, el tema y el número del hallazgo que se fue a resolver, o `—` si es trabajo nuevo.
- **Es el enlace hacia adelante.** El de vuelta ya existía: el `cerrado en` del hallazgo apunta a la sesión que lo cerró. Con los dos, un hallazgo que se arrastra tres sesiones se sigue en cualquier dirección; con uno solo, no.
- Si la sesión atiende más de un hallazgo, se nombran todos.

## 12.2.0 — 2026-08-14

**MENOR** (aditivo: una plantilla nueva; no cambia nada de lo escrito).

**Lo que una sesión deja se quedaba en la transcripción.** Una sesión entera produjo cinco aprendizajes y nueve pendientes, y ninguno tenía dónde escribirse: había que releer la conversación para encontrarlos. La transcripción guarda **lo que se dijo**; faltaba el molde de **lo que quedó**.

- **Nueva plantilla [`plantillas/sesion.md`](plantillas/sesion.md)**: cuatro campos por hallazgo — qué pasó, por qué importa, qué se decidió y dónde queda.
- **No es un resumen de cierre.** Se llena en el momento en que aparece el hallazgo. Es la misma lección de la transcripción de sesiones: lo que se deja para el final no se escribe nunca, porque un chat no tiene final.
- **Cada hallazgo termina en uno de cuatro sitios**, y la plantilla lo dice: señal, pendiente, regla o memoria del usuario. Lo que no cabe en ninguno era conversación, y ya está en la transcripción.
- **Falta el enganche** que lo recuerde en el momento. Mientras dependa de que el agente se acuerde, se va a olvidar, y eso queda anotado como pendiente.

## 12.1.0 — 2026-08-14

**MENOR** (precisa el alcance de una regla que ya existía; no invalida nada escrito).

**"Responde corto" se cumplía en los reportes y no en las explicaciones.** [`01·C5`](base/01-conducta.md#c5--responde-corto) pedía respuestas cortas, y el agente las daba al reportar trabajo. Al explicar un concepto hacía lo contrario: párrafos, tablas y opciones para responder una pregunta de una línea. El usuario lo cortó tres veces en la misma sesión, la última con *"explicar algo no es extenderse en prosa y que no se entienda nada, explicar es poder decir algo en pocas palabras pero que se entienda"*.

- **`C5` dice ahora que la explicación también va corta**, y que si no cabe en dos o tres frases el asunto todavía no se entendió: se piensa más, no se escribe más.
- **Queda fijado qué significa "menos es más"** dicho por el usuario: lo anterior fue largo y no se entendió, y se responde otra vez más corto. Antes era una señal que el agente podía leer como un comentario de estilo.
- **El ejemplo es el de la sesión**: tres párrafos y una tabla para explicar qué es una especificación, contra una sola frase.
- La regla trae su bloque de checklist, que antes no tenía.

## 12.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (desde ahora, un comando rechazado no cancela lo que el usuario pidió: el agente corrige el comando y vuelve a intentar).

**Un rechazo se leía como "olvídelo todo".** El usuario aprobó un renombrado, rechazó el comando con que el agente iba a hacerlo, y el agente dio el encargo por cancelado y respondió con una explicación. Hubo que pedirlo tres veces. [`01·C1`](base/01-conducta.md#c1--avisa-antes-de-tocar) y [`01·C17`](base/01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación) dicen qué cuenta como **aprobación**; ninguna decía qué significa un **no** al comando, y el agente lo resolvió a su criterio, que es lo que las reglas existen para impedir.

- **Nace [`01·C22`](base/01-conducta.md#c22--ante-un-comando-rechazado-corrige-el-comando--la-orden-sigue-en-pie)**: lo que el usuario rechaza es **cómo** el agente iba a hacerlo, no lo que pidió. El agente corrige la llamada y reintenta, o pregunta en una línea qué cambiarle; la orden solo la retira el usuario, diciéndolo. Extiende `C17`.
- **Nace en `base/` y no en la memoria del agente.** Es conducta de cualquier agente, no preferencia de un usuario: `base/` es la línea de comportamiento y la memoria se construye encima ([`01·C19`](base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto), [`20·M13`](base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)). Escribirla en la memoria era conducta sin versionar.
- **Sin validador.** Lo que se exige pasa después del rechazo y no queda en ningún archivo ([`20·M9`](base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)). Queda anotada como no validable.
- **Retroactividad.** No reabre nada. Aplica a los rechazos que lleguen desde ahora.

## 11.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (desde ahora, el agente no arranca con un pedido al que le falte un dato: pregunta por ese dato y espera).

**El pedido incompleto se completaba adivinando.** [`01·C7`](base/01-conducta.md#c7--ante-dos-lecturas-pregunta) y [`01·C17`](base/01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación) cubrían el pedido que admite **dos lecturas**, pero no el que no trae el dato: *"arregle eso"* no tiene dos lecturas, no tiene ninguna. El agente deducía a qué apuntaba "eso" por el contexto, acertaba a veces, y el trabajo quedaba a medias o en el archivo equivocado.

- **Nace [`01·C21`](base/01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar)**: un pedido de trabajo declara **sobre qué**, **qué quiere**, **qué debe quedar hecho** y **qué no se toca**; el que solo pide información declara los dos primeros. Si falta alguno, el agente pregunta por ese y no toca nada mientras espera. Extiende `C7`.
- **[`plantillas/CLAUDE.md.plantilla`](plantillas/CLAUDE.md.plantilla) gana el punto 6**, con los cuatro campos y un ejemplo de cada uno. Llega solo a cada proyecto por [`01·C18`](base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central), que es aditivo: nadie copia nada a mano.
- **Sin validador.** Lo que se exige pasa en el chat y ningún script lo lee ([`20·M9`](base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)). Queda anotada como no validable.
- **Retroactividad.** No reabre nada. Aplica a los mensajes que lleguen desde ahora.

## 10.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (desde ahora, el documento que use una palabra de otro idioma la traduce o la explica la primera vez).

**El estándar escribía en inglés y exigía escribir en español.** [`01·C8`](base/01-conducta.md#c8--habla-el-idioma-del-proyecto) manda que todo lo que ve el usuario vaya en el idioma del proyecto, y el propio estándar usaba "spec" en 53 archivos. Quien lee "falta la spec" no sabe qué documento le piden ni dónde ponerlo, que es justo lo que [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) vino a evitar.

- **Nace [`01·C20`](base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica)**: el término de otro idioma se traduce, y el que no tenga traducción usada se explica la primera vez que aparece. Extiende `C8`, que fijaba el idioma pero no decía qué hacer con las palabras que no lo tienen.
- **"spec" pasa a "especificación"** en el texto de `base/`, `plantillas/`, `validadores/` y `documentacion/`: 162 cambios. **Los nombres de archivo y las rutas no se tocan** — `spec.md`, `plantilla-especificacion-modulo.md` y el archivo de `F2` siguen igual, así que ningún proyecto tiene que renombrar nada. Fue decisión del usuario, para que el cambio no obligara a mover archivos.
- **Los identificadores no cambian.** `F2` sigue siendo `F2`; lo que cambió es su título, que ahora dice *"Sin especificación acordada no hay código"*.
- **Se anula el checklist de las reglas cuyo texto se tocó** ([`20·M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md)): `F2`, `F7`, `DOC3`, `DOC6`, `DOC11`, `DOC12`, `DOC13` y las cuatro `F4.x` derogadas. Cambió una palabra y no lo que exigen, pero las filas 8 a 11 se juzgan sobre el texto. Se vuelven a aplicar en la fase que las toque.
- **Retroactividad.** Un documento ya escrito y aceptado no se reabre para traducirle las palabras. Aplica a lo que se escriba desde ahora.

## 9.2.0 — 2026-08-14

**MENOR** (aditivo: una columna nueva en la tabla de deuda del cierre).

**La deuda se anotaba sin decir de dónde salía.** Se registraba qué quedó pendiente y a dónde se traslada, pero no por qué apareció. Y no todas las deudas dicen lo mismo: una que sale de no haber visto lo que se iba a romper señala que la línea base de [`02·F17`](base/02-flujo-de-trabajo/base.md) se hizo floja; una que se decidió por tiempo, o que la produjo el propio plan al diferir algo, no señala nada malo. Sin separarlas, no se puede saber si el análisis previo se está haciendo bien.

- **[`plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md`](plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) §6 gana la columna `Origen`**, con cuatro valores: *no previsto*, *atajo decidido*, *cambio del entorno* y *diferido por el plan*. Cada uno con qué pasó y qué significa.
- **Para qué sirve.** Un análisis bueno no elimina la deuda: convierte la **descubierta** en **declarada**. Si fase tras fase se repite *"no previsto"*, el problema no es la deuda: es que la línea base se está haciendo por encima. Antes eso no se veía en ningún lado.
- **Retroactividad.** Las fases cerradas no se reabren para clasificar su deuda.

## 9.1.0 — 2026-08-14

**MENOR** (aditivo: una subsección nueva en el cierre y una en el estado de fase; el plan de trabajo pierde una columna y una sección que ya vivían mejor en otro lado).

**Nada verificaba que el plan de trabajo se hubiera cumplido.** El `resultado_pruebas` que trajo [`9.0.0`](#900--2026-08-13) comprueba que **el resultado sirve**. Pero que **se haya hecho lo que se dijo que se iba a hacer** no lo revisaba nadie: el avance se marcaba con una casilla dentro del propio plan, que es autorreporte y encima pisa el documento aprobado, y el `funcionalidad_implementada` trazaba solo contra la spec. Una fase podía pasar todas las pruebas y haber dejado tres tareas sin tocar, o haber tocado archivos que el plan no declaraba, sin que quedara rastro.

- **[`plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md`](plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) §2 pasa a tener dos trazabilidades**, porque responden preguntas distintas: **§2.1 spec → implementación** (qué había que lograr) y **§2.2 plan de trabajo → ejecución** (qué se iba a hacer para lograrlo). La §2.2 va tarea por tarea, con su identificador copiado del plan, y suma dos cosas que antes no se preguntaban: las **tareas que no se hicieron** y los **archivos tocados que el plan no declaraba** ([`02·F8`](base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). "Ninguno" es la respuesta esperada; que quede escrito cuando no lo es permite ver si el plan se amplía sobre la marcha y por qué.
- **[`plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`](plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) pierde la columna `Estado` de §3 y el §13 de cierre.** Marcar avance ahí pisaba el plan aprobado y dejaba sin contra qué comparar, el mismo defecto que `9.0.0` corrigió en el plan de pruebas. El cierre ya vivía completo en el `funcionalidad_implementada`, duplicado.
- **[`plantillas/ciclo-vida-proyectos/10-estado-fase.md`](plantillas/ciclo-vida-proyectos/10-estado-fase.md) gana §1.2 · Avance de las tareas del plan**, que es donde va el seguimiento **en vivo** mientras la fase corre. Queda la cadena completa: el plan dice qué se va a hacer, el estado dice por dónde va, el cierre dice qué se hizo.
- **Retroactividad.** Las fases cerradas no se reabren. Los planes ya aprobados conservan su columna de estado; el cambio aplica a los que se escriban desde acá.

## 9.0.0 — 2026-08-13

**MAYOR** ⚠ obliga a migrar (toda fase que se abra desde ahora produce un quinto documento; el plan de pruebas deja de ser donde se anotan los resultados).

**El plan de pruebas se aprobaba antes y se sobreescribía después.** La plantilla traía la tabla de ejecución dentro de cada caso y el resumen de la corrida en §12: el mismo archivo que el usuario aprueba **antes** de probar terminaba pisado con lo que pasó **después**. Tres consecuencias: se pierde la línea base aprobada, así que no hay contra qué comparar lo que se acordó probar; no queda un veredicto formal de si la fase cumple; y el documento de cierre tenía que redactar de memoria la sección "qué se probó". Además la plantilla decía apoyarse en ISO/IEC/IEEE 29119-3, que separa el plan del registro de ejecución, y la nuestra los juntaba.

- **Nueva plantilla [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md)**, el `resultado_pruebas.md` de la fase. Registra qué se ejecutó, con qué resultado, qué defectos salieron, y sobre todo el **veredicto por criterio de aceptación** y el **veredicto de la fase**. Se crea **junto con los dos planes**, no cuando se corre la primera prueba: el formato puesto desde el principio se ve, se revisa y no se olvida. Lo que no se ha corrido se escribe **"no ejecutado"**, nunca en blanco ni como aprobado, y el veredicto arranca en *"todavía no se ejecutó"*, que no es lo mismo que "no cumple". Los ciclos de reprueba se apilan sin pisar el anterior, porque saber que algo falló y después pasó vale más que ver solo el resultado final.
- **[`02·F12.13`](base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) suma el quinto documento al árbol de la fase.** El cambio a `F12` lo **decidió el usuario el 2026-08-13**; esa regla está congelada como texto suyo y el agente no la ajusta por cuenta propia.
- **El resultado se arma desde el plan, no desde lo que se hizo.** La lista de casos, su criterio y su prioridad **se copian** del `plan_pruebas`; un caso que esté en uno y no en el otro es defecto de trazabilidad y se arregla antes de dar veredicto. Y §5.1 pone frente a frente **cada meta que el plan fijó** (cobertura, casos críticos ejecutados, métricas propias, criterios de salida) contra lo que dio de verdad: sin eso, el plan podía exigir el 100% de los críticos y el resultado no decirlo nunca.
- **[`plantillas/ciclo-vida-proyectos/08-plan-pruebas.md`](plantillas/ciclo-vida-proyectos/08-plan-pruebas.md) deja de recibir resultados.** Se le quitan la tabla de ejecución por caso y el resumen de corrida; en su lugar apunta al documento nuevo. El plan define **qué se va a medir**; el resultado dice **cuánto dio**.
- **[`plantillas/ciclo-vida-proyectos/10-estado-fase.md`](plantillas/ciclo-vida-proyectos/10-estado-fase.md) gana §1.1 · Veredicto de las pruebas**, que se **copia** del resultado y no se escribe de memoria. Es de donde sale el estado de la estación de verificación, y con un criterio en "No" la fase no cierra.
- **[`plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md`](plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) §3 pasa a resumir del resultado**, no a redactarlo: si dice algo que el resultado no respalda, manda el resultado.
- **[`plantillas/ciclo-vida-proyectos/04-HU.md`](plantillas/ciclo-vida-proyectos/04-HU.md)** suma la columna de resultado a la tabla de fases y la fila correspondiente a la tabla de qué documento responde qué.
- **[`base/02`](base/02-flujo-de-trabajo/base.md)**: `F4` aclara que lo que se aprueba son los dos planes y que el plan aprobado no se modifica para anotarle resultados; la etapa 7 de `F15` cierra ahora con el `resultado_pruebas` escrito, no con un conteo verde reportado de palabra.
- **[`validadores/fases.py`](validadores/fases.py)** incluye `resultado_pruebas.md` entre los documentos que espera de una fase. Sigue siendo **aviso**, no falla: una fase recién abierta todavía no lo tiene, y eso no es incumplimiento.
- **Retroactividad.** Las fases ya cerradas no se reabren para producirlo. Aplica a las que se abran desde esta versión.

## 8.2.0 — 2026-08-13

**MENOR** (aditivo: una sección nueva en la plantilla de HU; no invalida ninguna HU ya escrita).

**La cadena de trazabilidad se cortaba en la HU.** El brief lista sus épicas, la épica lista sus HU y cada HU nombra su épica ([`13·DOC16`](base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md)). De ahí para abajo el hilo se perdía: la HU no nombraba las fases que la implementan ni sus planes, así que desde el requisito no había cómo llegar a la ejecución. Se llegaba al revés —la fase sí declara qué CA cubre— y un enlace de una sola vía no se mantiene: cuando la fase se mueve o se divide, nadie actualiza el otro lado porque el otro lado no existe.

- **[`plantillas/ciclo-vida-proyectos/04-HU.md`](plantillas/ciclo-vida-proyectos/04-HU.md) gana la sección `8 · Fases que la implementan`**: una fila por fase con los CA que cubre, sus dos planes y su estado. Las secciones siguientes corren de número.
- **Se completa a medida**, igual que la lista de épicas del brief y la de HU de la épica. Una HU recién escrita la tiene vacía, y eso es correcto: las fases se definen después.
- **Además, una tabla de qué documento responde qué** (el requisito, el plan, las pruebas, el estado, el cierre), para no ir a buscar al documento equivocado. Es el mismo problema que resolvió [`8.1.0`](#810--2026-08-13) en los dos planes, visto desde arriba.
- **Retroactividad.** Una HU ya escrita y aceptada no se reabre por esto; la sección se agrega cuando se le definan fases.

## 8.1.0 — 2026-08-13

**MENOR** (aditivo: dos secciones nuevas en dos plantillas; no invalida ningún plan ya escrito).

**Un documento terminado no decía qué era.** El propósito de cada plantilla vivía dentro de la caja de instrucciones, y esa caja la plantilla manda borrar al llenarla. Resultado: el `plan_trabajo` y el `plan_pruebas` de una fase quedaban sin una sola línea que explicara para qué existe cada uno. Quien los abre meses después tiene que deducirlo del contenido, y quien tiene que aprobarlos no sabe qué está aprobando.

- **[`plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`](plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) y [`plantillas/ciclo-vida-proyectos/08-plan-pruebas.md`](plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)** ganan una línea fija bajo el título: **para qué sirve** el documento, y dónde vive lo que no le toca a él. Va fuera de la caja de instrucciones y **sobrevive al llenado**.
- **Una línea, no dos.** La primera versión traía además un apartado *"qué no es"*. Se descartó: si el "para qué sirve" está bien escrito, ya excluye lo demás, y la negación repetía en forma de contraposición lo que la [lista de marcadores](base/00-identidad-y-rol/marcadores-de-ia.md) señala como adorno. Lo que sí valía era decir **dónde vive lo otro**, y eso se dice en positivo, dentro de la misma línea.
- **La caja de instrucciones lo dice explícito**: se borra ella, no la línea de arriba.
- **Retroactividad.** Un plan ya escrito y aprobado no se reabre por esto. Las dos líneas se agregan al escribir el siguiente.
- Como las plantillas cambiaron de huella, su copia local en cada proyecto queda marcada vieja hasta la próxima corrida del instalador; el texto local no se pisa.

## 8.0.1 — 2026-08-13

**PARCHE** (no cambia qué se exige: la narrativa ya tenía que estar; ahora se ve).

- **[`plantillas/ciclo-vida-proyectos/04-HU.md`](plantillas/ciclo-vida-proyectos/04-HU.md) §2 · Narrativa.** Las tres líneas (`Como`, `Quiero`, `Para`) pasan a lista. Sin el guion, Markdown junta los tres renglones en un solo párrafo corrido y la narrativa, que es lo primero que alguien lee de una HU, queda ilegible. Se agrega la nota que dice por qué van como lista, para que nadie las vuelva a dejar sueltas.
- Como la plantilla cambió de huella, la copia local del catálogo de cada proyecto queda marcada vieja hasta la próxima corrida del instalador; el texto local no se pisa.

## 8.0.0 — 2026-08-12

**MAYOR** ⚠ obliga a migrar (todo catálogo de proyecto con reglas `P` ya escritas tiene que agregarles su respaldo; la que no lo tenga se queda sin respaldo hasta que se cree la regla de base que le falta).

**Las reglas de un proyecto dejan de nacer sueltas.** Hasta ahora la capa 3 podía escribir cualquier regla `P` sin más justificación que "lo acordó el equipo": la plantilla del catálogo lo admitía de frente, con un campo que aceptaba *"regla nueva, no cubierta por la base"*. Un catálogo así crece hasta volverse un estándar paralelo, con la diferencia de que ese no pasa por checklist, no se versiona y nadie lo audita.

- **Nueva [`20·M16 · Toda regla de proyecto nombra la regla de base que concreta`](base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)** (extiende [`M1`](base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)). Cada `P` declara, con su enlace, la regla de `base/` cuyo criterio concreta o endurece. Si ningún criterio la cubre, la regla de base se escribe primero, agnóstica y por el procedimiento completo ([`M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md)); hasta entonces la `P` no se publica.
- **El respaldo es del criterio, no del detalle**, y por eso la regla no choca con [`M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md). La base dice **qué hay que decidir** (`06·R4`: lo caro y estable se cachea, con invalidación clara); la `P` dice **con qué valor se decide aquí** (el catálogo, 10 minutos). Sin esa separación la regla se trancaba: una `P` de stack no puede subir a `base/`, y sin respaldo tampoco podría existir. El desarrollo, con la tabla de las dos mitades, queda en [`base.md`](base/20-meta-reglas/base.md).
- **Qué pasa con lo que no encaja.** Si al quitarle el detalle del proyecto no queda nada que le sirva a otro, no era una regla: era una decisión de configuración, y va donde va la configuración.
- **[`plantillas/reglas-proyecto.md`](plantillas/reglas-proyecto.md) cambia de forma.** El campo *Relación con la base* pasa a llamarse **Respaldo**, es obligatorio y lleva enlace; desaparece la salida *"regla nueva, no cubierta por la base"*. Se suma la sección *Ninguna `P` se sostiene sola*. Como la plantilla cambió de huella, el catálogo de cada proyecto queda marcado viejo hasta la próxima corrida del instalador; el texto local no se pisa.
- **[`20·M16` queda registrada como validable](validadores/reglas-validables.md)**, y no en seco: el catálogo vive en el proyecto. El script comprueba que cada `P` trae su respaldo y que el ID citado existe en `base/`; que el criterio citado sea de verdad el que la `P` concreta lo decide quien lee.
- **[`13·DOC10`](base/13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md) no se toca.** Esa regla exige registrar y numerar la regla propia, que es otra exigencia; el respaldo es de dónde sale, y son dos cosas que se cumplen por separado ([`M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)).

## 7.0.0 — 2026-08-10

**MAYOR** ⚠ obliga a migrar (todo documento que se entregue desde ahora se relee contra la lista de marcadores; un proyecto al día tiene que empezar a hacerlo).

**Lo que el agente entrega deja de leerse como escrito por una máquina.** Hasta ahora el estándar solo pedía que el texto se entendiera ([`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)), y un documento puede entenderse perfecto y venir lleno de muletillas, rayas largas y secciones todas del mismo tamaño. Eso lo nota cualquiera que lo lea, y en un entregable pesa.

- **Nueva [`00·ID8 · Escribe sin las marcas que delatan generación automática`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md)** (extiende `ID7`). Alcanza a documentación, manuales, informes y a cualquier texto que una persona vaya a leer como trabajo terminado. Ningún documento se entrega sin releerlo contra la lista.
- **Nuevo anexo del capítulo [`marcadores-de-ia.md`](base/00-identidad-y-rol/marcadores-de-ia.md)**, la lista cerrada: 62 marcas en ocho secciones, cada una con qué se escribe en su lugar. Van ordenadas de la más fácil de ver a la más difícil de disimular: palabras y muletillas, puntuación y tipografía, marcas invisibles, estructura, el español que no es de acá, contenido y tono, metadatos del archivo, y el contraste con lo escrito antes. Va como anexo y no dentro de la regla porque el cuerpo de una regla son cuatro líneas ([`20·M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)), y vive en `base/` porque es lo único que heredan los proyectos.
- **Dos secciones que no venían en la guía de origen.** *Marcas invisibles* (espacio duro, caracteres de ancho cero, guion suave, `…` como carácter único): no se ven leyendo, sobreviven a cualquier reescritura y son las únicas que un script cuenta sin equivocarse. Y *El español que no es de acá*: el léxico de España, el `vosotros`, el pretérito compuesto donde va el simple y el español neutro sin acento de ninguna parte, que en Colombia salta a la primera lectura.
- **Qué no cuenta como marca.** La notación que el propio estándar define (la cita `NN·ID`, los `[BLINDADA]` y `*opt-in*`, los bloques `INCORRECTO / CORRECTO`, los ✅ ❌ de la tabla del checklist), la flecha dentro de una notación, la sección fija que pide una plantilla, los bloques de código y la salida de herramientas. Y el límite: la lista quita adorno, nunca precisión. Si quitar una marca vuelve el texto confuso, manda `ID7`.
- **Lo que la lista no cubre, dicho en la lista.** La norma del español —ortografía, gramática, sintaxis, variedad del país— no está en el estándar: [`01·C8`](base/01-conducta.md#c8--habla-el-idioma-del-proyecto) fija el idioma y nada más. Escribir bien y no sonar a máquina son dos exigencias distintas, y la primera todavía no tiene regla.
- **[`00·ID8` queda registrada como validable parcial**](validadores/reglas-validables.md): un script puede contar las marcas de palabra y tipografía; que el documento suene o no a máquina lo decide quien lo lee.
- **Lo que esto deja pendiente.** El texto que ya está escrito —`base/`, `plantillas/`, los README del repositorio— usa la raya larga como inciso por todas partes. La norma nueva no reabre lo cerrado, así que rige para lo que se escriba desde ahora; limpiar lo anterior es un trabajo aparte que todavía no se hizo.

## 6.1.0 — 2026-08-09

**MENOR** (aditivo: nada de lo que ya se cumplía deja de cumplirse).

**Cada sesión pide su nombre mientras todavía hay con quién acordarlo.** El enganche crea el archivo como `AAAA-MM-DD-sesion.md` porque al abrir el chat nadie sabe de qué va a tratar, y ponerle el tema después quedaba en que el agente se acordara — que es justo lo que el estándar no da por hecho. En el histórico de este repositorio se veía el resultado: ocho sesiones quedaron llamándose "sesión del AAAA-MM-DD", y esa línea del índice es lo único que la siguiente sesión ve de ellas.

- **[`validadores/historico.py`](validadores/historico.py) — `aviso_de_nombre`.** Cuando el archivo todavía tiene el nombre genérico y la sesión ya tuvo una respuesta, devuelve el recordatorio de proponerle al usuario nombre y resumen. [`hook_historico.py`](validadores/hook_historico.py) lo escribe en su salida del `UserPromptSubmit`, que Claude Code le entrega al agente en ese mismo turno. **Se pide una sola vez**: queda la marca `<!-- nombre: preguntado -->` en el archivo. No se pide en el primer mensaje —ahí el tema todavía no existe— y **nada se renombra solo**: el nombre lo aprueba el usuario.
- **`--renombrar`, el comando que hace el cambio completo.** `python validadores/historico.py --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"` mueve el archivo, corrige su título y arregla la línea del índice — las tres cosas. Renombrar a mano dejaba el índice apuntando a un archivo que ya no está. La fecha sale del nombre viejo y no del reloj: una sesión que se nombra al otro día sigue siendo la del día que ocurrió. Las tildes se conservan en el título y en el índice, y se quitan del nombre del archivo, que viaja en enlaces y rutas.
- **El mismo nombre en la sesión de Claude Code.** El recordatorio trae también la línea `/rename <tema>` para que el usuario la pegue: pone ese nombre en la pestaña, en la barra del prompt y en `/resume`. La pega él porque `/rename` es un comando del usuario — el agente no lo puede ejecutar y ningún enganche fija el título de la sesión. Lo que se automatiza es que los dos nombres salgan de la misma propuesta, en el mismo momento.
- **[`plantillas/historico-chat.md`](plantillas/historico-chat.md)** documenta las tres cosas en *Qué hace el agente aquí*. Como la plantilla cambió de huella, el `historico-chat/README.md` de cada proyecto queda marcado viejo hasta la próxima corrida del instalador; el texto local no se pisa.

## 6.0.0 — 2026-08-08

**MAYOR** ⚠ obliga a migrar (`00·ID2` queda derogada: lo que se escriba desde ahora sigue `00·ID7`, y quien cite `ID2` tiene que citar `ID7`).

**Todo lo que el agente escribe se entiende sin saber del tema.** Hasta ahora la norma decía lo contrario: [`00·ID2`](base/00-identidad-y-rol/reglas/ID2-escribe-en-registro-tecnico-sin-adornos.md) pedía escribir *"para quien lee código: preciso, técnico"*, y el "que hasta un niño lo entienda" quedaba reservado a la pantalla del producto ([`17·I4`](base/17-interfaz.md#i4--texto-para-el-usuario-no-jerga)). El resultado se veía en la práctica: documentación correcta que solo entiende quien ya sabe. Ahora el estándar es uno solo, y las reglas mismas entran en él.

- **Nueva [`00·ID7 · Escribe para que lo entienda quien no sabe del tema`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)** (deroga `ID2`). Alcanza a todo lo que el agente produce —respuestas, documentación, manuales, mensajes y las reglas del propio estándar—: palabras de todos los días, ideas directas, párrafos cortos, y el término técnico que no se pueda evitar explicado en sencillo la primera vez. Cada cosa se explica diciendo **qué hace**, **para qué sirve** y **qué resultado deja**. El ejemplo se agrega solo si aclara. Antes de dar un texto por terminado se relee comprobando que se entiende sin conocimiento previo.
- **La claridad no se compra con imprecisión.** Se cambia la palabra difícil por la fácil, nunca el dato exacto por uno vago: la documentación técnica también sigue la regla, sin perder lo que la hace exacta.
- **[`00·ID2`](base/00-identidad-y-rol/reglas/ID2-escribe-en-registro-tecnico-sin-adornos.md) queda `[DEROGADA]`**, con su texto intacto y la nota de qué la reemplaza ([`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)). Lo único suyo que sobrevive —sin relleno ni fórmulas de cortesía— lo conserva `ID7`.
- **[`17·I4`](base/17-interfaz.md#i4--texto-para-el-usuario-no-jerga) deja de ser "lo contrario"** de cómo escribe el agente: pasa a ser el mismo estándar llevado a la pantalla del producto, donde además no asoman siglas ni códigos internos.
- **La higiene de [`20 · Meta-reglas`](base/20-meta-reglas/base.md) se alinea:** el lenguaje de una regla ya no es "técnico", es imperativo, corto y en palabras de todos los días.

## 5.0.0 — 2026-08-08

**MAYOR** ⚠ obliga a migrar (`02·F13` cambia de exigencia: el agente ya no se detiene a esperar que el usuario cree la estructura, la crea él).

**El `CLAUDE.md` pasa a ser el setup del agente, y la instalación se hace sola.** Instalar un proyecto pedía siete pasos a mano —copiar la plantilla, reemplazar cada `«…»`, crear `proyectos/`, editar el `.gitignore`, poner los 4 archivos de `.agente/`, anotar el proyecto en el registro central y fijar la versión adoptada— y hasta que alguien los hiciera, el proyecto trabajaba **sin reglas**. Ahora los pone el instalador: una línea deja el entorno completo, operativo y comprobado.

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

- **[`plantillas/CLAUDE.md.plantilla`](plantillas/CLAUDE.md.plantilla) — sin el recuadro de pasos manuales.** Se abría con *"BORRAR ESTE RECUADRO"* y cuatro instrucciones para el usuario; ese recuadro **era** el proceso de instalación, y era lo que fallaba. En su lugar, la sección **Instalación** con la única línea que hay que correr, qué deja puesto y qué no decide. Los marcadores (`«RUTA-ESTANDAR»`, `«NOMBRE-PROYECTO»`, `«SLUG-PROYECTO»`, `«VERSION-ESTANDAR»`) los llena el instalador; los opt-in `15`–`19` traen su valor por defecto (`no`) en vez de un `«sí / no»` que dejaba el archivo reprobando hasta que alguien lo editara. Nueva sección **2.5** (el código del usuario) y arranque de sesión reordenado: instalar es el paso 1.
- **[`validadores/instalar.py`](validadores/instalar.py) instala el proyecto entero**, no solo los enganches: estructura base (`proyectos/`, `documentacion/`, `prompts/`), `CLAUDE.md` generado desde la plantilla con las rutas de la máquina, `.gitignore`, los 4 archivos de `.agente/`, la fila en el registro central — y al terminar corre el checklist y reporta lo que quedó. Sobre un proyecto ya instalado no duplica ni pisa nada; sobre uno con el `CLAUDE.md` viejo, llena los marcadores que queden (incluidos los de plantillas anteriores) y agrega solo las secciones que la plantilla sumó.
- **[`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) deja de ser un muro.** Pasa de *"Detente si el proyecto no tiene su estructura base"* a *"Deja la estructura base puesta antes de trabajar"*: crear una carpeta que la norma exige no es una decisión del usuario, es la norma. Lo que sigue siendo suyo —y la regla lo dice más fuerte que antes— es **qué va dentro de `proyectos/`**: el agente crea la carpeta vacía y **nunca** mueve, reorganiza ni acomoda código que ya exista. Se retiran el mensaje de orientación y el bloqueo del arranque. El resultado del checklist de la regla queda **anulado**: se vuelve a aplicar en el próximo repaso del capítulo.
- **[`01·C18`](base/01-conducta.md) se aplica sola.** Pedía *"avisa al usuario y ofrece aplicarlos"* y *"jamás en silencio"*: una pregunta cuya única respuesta útil es "sí", que mientras no se contestaba dejaba el `CLAUDE.md` viejo. Ahora el instalador aplica lo aditivo y **dice qué agregó** — en su salida y en el registro de `documentacion/versiones/`. Sigue sin pisar, reordenar ni borrar lo escrito.
- **[`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md)** cambia la columna *"Cómo se instala"* por *"Qué hace el instalador"*: los 13 componentes se instalan con la misma línea. Ninguna fila le pide nada al usuario.
- Un `«…»` dentro de una frase deja de contar como marcador sin llenar: es cómo se nombra a un marcador, no un hueco.
- **El propio estándar queda fuera** de la configuración de proyecto: no es un proyecto que use el agente, es donde viven las reglas. Recibe los enganches, el histórico y la memoria; no `proyectos/`, ni `.agente/`, ni un `.gitignore` que borraría su `CLAUDE.md` del repositorio.

## 4.0.0 — 2026-08-08

**MAYOR** ⚠ obliga a migrar (dos reglas del capítulo `02` quedan derogadas: quien cite `02·F6` o `02·F7` tiene que citar `13·DOC1` y `13·DOC3`).

**`13 · Documentación` se somete al checklist.** Era el único capítulo grande que nunca había pasado por [`M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md): 16 reglas, 30 KB, cero bloques de checklist. La auditoría de [`analisis/base-2026-08-07-cumplimiento-meta-reglas.md`](analisis/base-2026-08-07-cumplimiento-meta-reglas.md) §5.14 lo había medido — **1 cumplía, 5 al borde y 10 no**. Ahora son **18 reglas, las 18 CUMPLE**, cada una con su resultado escrito y su motivo.

- `base/13-documentacion.md` → `base/13-documentacion/base.md` + `reglas/`, el mismo molde que `00-identidad-y-rol/`, `02-flujo-de-trabajo/` y `20-meta-reglas/`. El índice del capítulo dice qué exige cada regla en una línea; el cuerpo de cada una pasó de párrafos a una a cuatro líneas.
- **Dos reglas nuevas, ninguna exigencia nueva.** [`DOC17`](base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md) (un `README.md` por nivel del árbol) vivía dentro de `DOC15`, y `DOC16` ya la citaba como si fuera regla propia. [`DOC18`](base/13-documentacion/reglas/DOC18-actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad.md) (actualizar el mapa al cerrar) era la segunda mitad de `DOC9`, que pedía dos cosas cumplibles por separado — lo anunciaba su propio título. Quien las citaba dentro de la regla vieja ahora las cita por su ID.
- **`DOC14` deja de nombrar herramientas.** Era la regla más larga del capítulo (58 líneas): nombraba visor de repositorio, editor, código de error y "route", y traía **rutas reales de un cliente** en los ejemplos — `M3` de frente. Los ejemplos son ficticios y el montaje del render local salió a [`base/13-documentacion/render-local-de-md.md`](base/13-documentacion/render-local-de-md.md), anexo del capítulo: es infraestructura del proyecto, no regla de redacción de enlaces.
- **`DOC5` describe el backend en concepto**, no con un motor, una herramienta y una carpeta concretos. Cuál se usa lo declara la capa 3, que es donde `M3` lo manda.
- **`DOC10` deja de depender hacia arriba.** Citaba `P28` —una regla del catálogo de **un proyecto**— desde capa 2, que [`M7`](base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) prohíbe, y cerraba con una enumeración congelada de IDs citables que ya estaba vieja; lo que garantiza que toda regla se pueda citar es `M4`.
- **`DOC3` y `DOC11` dejan de repetirse.** `DOC11` se declaraba *"extiende DOC3"* y a continuación copiaba entera su tabla. El principio queda en `DOC3`, la tabla solo en `DOC11`.
- **`DOC12` completa su excepción** —tenía condición, le faltaban límite y autorizador ([`M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md))— y **`DOC4` gana el ejemplo** que no tenía.
- Los procedimientos y formatos que ocupaban el cuerpo de `DOC6`, `DOC8`, `DOC12` y `DOC13` viven donde corresponde: `plantillas/`. Nueva: [`plantillas/retrodocumentacion.md`](base/13-documentacion/retrodocumentacion.md), los seis pasos de `DOC6`.

**Se consolidan los dos duplicados.** [`02·F6`](base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md) y [`02·F7`](base/02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md) exigían lo mismo que `DOC1` y `DOC3` —el ejemplo de `F7` era idéntico palabra por palabra— y las cuatro reprobaban por eso. Quedan **derogadas** ([`M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)): marca en el encabezado, texto original conservado debajo, ID no reutilizado. Con eso, `DOC1` y `DOC3` pasan a CUMPLE y el capítulo `13` queda **18 de 18**.

**Qué hay que hacer en un proyecto:** cambiar `02·F6` por `13·DOC1` y `02·F7` por `13·DOC3` donde se los cite —specs, planes, fases abiertas—. Las fases ya cerradas no se reabren: quedan selladas con la versión bajo la que cerraron.

Las citas del resto del estándar se reenlazaron solas a los archivos de destino (`validadores/citas.py`).

## 3.1.1 — 2026-08-07

**PARCHE** ⚠ **corrige una pérdida de datos.** Quien tenga 3.0.0 o 3.1.0 instalado debe actualizar antes de abrir otra sesión.

**La migración borraba memoria real.** `recuerdos.migrar()` borraba el archivo del almacén de la herramienta cuando era idéntico a uno del repositorio, con el argumento de que no se perdía nada. El argumento se cae cuando el almacén es un *junction* a `historico-chat/memory/`: origen y destino son **el mismo archivo**, compararlo consigo mismo da idéntico siempre, y el borrado se llevaba el único ejemplar. Pasó en un proyecto real, dos veces — una desde el instalador y otra desde el enganche, que corre solo en cada arranque y en cada edición.

- **Ya no se borra nada, nunca.** Todo lo que hay en el almacén se mueve; si el nombre está ocupado, entra como `<nombre>-local.md` y decide el usuario. Un enganche que corre solo no puede tener permiso de destruir: se equivoca una vez y se lleva la memoria entera sin que nadie lo pida.
- **El almacén enlazado pasa a ser una forma válida de cumplir `01·C19`.** Si es un *junction* o un enlace simbólico a la carpeta del repositorio, la herramienta ya escribe dentro del repositorio: no hay nada que mover, el checklist da por cumplido y el instalador **no toca la carpeta**. Se compara por identidad en disco (`os.path.samefile`), no por el texto de la ruta — dos rutas distintas pueden ser el mismo sitio.
- Cinturón además de eso: mover un archivo sobre sí mismo se detecta y se salta.

Lo escrito antes no se recupera solo: si la carpeta quedó vacía, se restaura del último commit (`git checkout -- historico-chat/memory/`).

Detrás: 2 pruebas nuevas —el duplicado idéntico que ya no se borra y el almacén enlazado que no se toca— y una verificación contra un *junction* de Windows de verdad, no simulado (206 en total).

## 3.1.0 — 2026-08-07

**MENOR** (aditivo: la sesión nueva arranca sabiendo qué pasó en las anteriores; ningún proyecto tiene que hacer nada más que reinstalar).

**Un chat nuevo empieza en blanco: lo que no se le inyecta, no existe para él.** El histórico se venía escribiendo desde `2.0.0`, pero nadie lo leía — la sesión siguiente no sabía siquiera que existía. Y la memoria acababa de mudarse al repositorio (`3.0.0`), donde la herramienta ya no la carga sola. Las dos cosas se resuelven igual: al abrir la sesión se inyecta el **índice**, no el contenido.

- `validadores/hook_sesion.py` — además de las reglas base, carga el índice de la memoria (`historico-chat/memory/memory.md`) y el del histórico (las últimas 40 sesiones, con el tema de cada una), con la orden de abrir con `Read` la que haga falta. Las transcripciones enteras no van: son la conversación completa y llenarían la ventana con lo que casi nunca se necesita.
- **Las dos se cargan también en el propio estándar.** Ahí no hay instalación que revisar —el enganche salía sin hacer nada—, pero la memoria y el histórico sí son los del usuario.
- `validadores/historico.py` — `sesiones()` y `contexto()` leen el índice del `README.md`; la línea de la sesión se comprueba **en cada mensaje** y no solo al crear el archivo: si al crearlo no había índice, esa sesión quedaba invisible para siempre.
- `validadores/enlaces.py` — `historico-chat/` entra en las carpetas con índice obligatorio. Una sesión sin su línea pasa a ser **falla**, no descuido; una línea que apunta a un archivo renombrado, aviso.
- `plantillas/historico-chat.md` — nueva sección: el índice es lo que lee la próxima sesión, y renombrar el archivo sin corregir la línea lo rompe.

Detrás: 6 pruebas nuevas (205 en total).

## 3.0.0 — 2026-08-07

**MAYOR** ⚠ obliga a migrar (la memoria del agente pasa al repositorio; un proyecto al día tiene que reinstalar para mover la suya).

**La memoria del agente deja de vivir en la herramienta.** Claude Code guardaba lo que el agente debe recordar entre sesiones en `~/.claude/projects/<ruta-del-proyecto>/memory/`, fuera del proyecto. Ahí no se ve en `git`, no se puede revisar en un cambio, no se versiona y no viaja a otra máquina: al clonar el proyecto en otro equipo, la memoria se queda atrás y nadie se entera. Ahora va en `historico-chat/memory/` del proyecto, y el almacén local queda **vacío** — sin copia ni puntero, porque dos versiones del mismo recuerdo terminan diciendo cosas distintas y la que manda es la que nadie puede leer.

- `base/01-conducta.md` · **`C19`** (nueva) — la memoria se escribe en `historico-chat/memory/`, un archivo por recuerdo; el almacén de la herramienta queda vacío. Vive en `01` y no en `13` por lo mismo que `C18`: el capítulo se carga literal en cada sesión, así que rige aunque el proyecto todavía no tenga la carpeta.
- `plantillas/memoria.md` (nueva) — el índice que se instala como `historico-chat/memory/memory.md`: la norma, la forma de cada recuerdo (qué se pide · por qué · cómo se aplica) y la tabla. Es documento heredado con sello; **no se pisa**, lo llena el proyecto.
- `plantillas/CLAUDE.md.plantilla` · **§2.4** (nueva) — la cuarta carpeta del proyecto, con su regla de versionado. El paso 6 la nombra entre lo que deja instalado.
- `plantillas/stack-instalacion.md` — componente **`recuerdos`**: la carpeta con su índice **y** el almacén local vacío. Las dos mitades son la misma exigencia: tener la carpeta y dejar los recuerdos afuera es no tener memoria.

Detrás, para que no dependa de que el agente se acuerde:

- `validadores/recuerdos.py` (nuevo) — resuelve dónde guarda la herramienta la memoria de cada proyecto (reemplaza por `-` todo lo que no sea letra o dígito de la ruta) y la **mueve**. Un archivo idéntico al que ya está en el repositorio se borra; uno con el nombre ocupado entra como `<nombre>-local.md` y se avisa — nada se pisa. La comparación de nombres ignora mayúsculas: en Windows `MEMORY.md` y `memory.md` son el mismo archivo.
- `validadores/hook_recuerdos.py` (nuevo) — enganche en `SessionStart` (recoge lo que quedó de sesiones anteriores) y en `PostToolUse`·`Write|Edit` (recoge el recuerdo en el momento en que se escribió; si no, pasaría toda la sesión en la carpeta equivocada y el agente lo daría por guardado). Es el único enganche que **sí** corre en el propio estándar: ahí vive la memoria del usuario.
- `validadores/instalar.py` — `instalar_recuerdos()`: crea la carpeta con el índice sellado y vacía el almacén local en la misma corrida.
- `validadores/checklist.py` · `versiones.py` — el componente `recuerdos` reprueba si falta la carpeta, si el índice quedó viejo o si algo sigue en el almacén local.

**Qué hay que hacer en un proyecto ya instalado:** correr `python validadores/instalar.py "<proyecto>" --aplicar`. Crea la carpeta y mueve lo que hubiera. Lo que entre como `-local` lo decide el usuario.

## 2.5.0 — 2026-08-07

**MENOR** (las diecinueve reglas del flujo pasan por el molde y por el checklist; ninguna cambia qué exige).

**El capítulo 02 se somete al estándar, como ya hizo el 20.** `M14` dice que ninguna regla nace fuera del procedimiento y que su cierre es el checklist. Se aplicó a `F0`–`F13`. **Resultado: 9 cumplen, 10 no** — y las diez reprueban por cosas que solo el usuario puede decidir.

**La regla se separó de su explicación.** Cada archivo de `reglas/` conserva **solo la exigencia**: encabezado, cuerpo de una a cuatro líneas, dependencia declarada, excepción con sus tres partes y ejemplo. Todo lo que desarrollaba, ilustraba o justificaba —la tabla de once etapas, la construcción de la línea base, la casuística de migración, el protocolo de `F8`, el mensaje de orientación de `F13`— pasó a `base.md`, a una sección `### F<n>` por regla. `F4.3`, que era la regla más larga del catálogo con 78 líneas, quedó en cinco.

- **`F0` toma el texto corregido que `estructura-regla.md` ya publicaba** desde la v2.2.0 sin que nadie lo aplicara. Convivían dos versiones de la misma regla y ninguna decía cuál mandaba.
- **Los títulos que contaban ahora mandan** (`M5`): `F0 · Recorre la cadena completa, sin saltar eslabones` · `F3 · Ejecuta seguido el plan aprobado` · `F5 · Corre solo las suites que la fase toca` · `F7 · No cierres una fase con trazabilidad incompleta` · `F9 · No subdividas ni renegocies un plan ya aprobado` · `F13 · Detente si el proyecto no tiene su estructura base`, entre otros. **Ningún ID cambió** (`M4`); los archivos se renombraron detrás del título.
- **`F13` pierde la marca inventada** `[GATE DE ARRANQUE · PRECONDICIÓN]`, que el propio `estructura-regla.md` usaba como anti-ejemplo literal. Que corra primero lo dice el capítulo, no una etiqueta.
- **Ocho excepciones que decían cuándo no aplican pero no hasta dónde ni quién autoriza** quedaron completas (`M8`): `F0`, `F2`, `F4`, `F4.2`, `F4.4`, `F9`, `F10`, `F11`.
- **Se rompió el ciclo de dependencias `F4.4 ↔ F4.5`** y la duplicación `F3`/`F9`, que ahora es `extiende 02·F3` (`M7`). El texto que `F5`, `F6` y `F7` copiaban de `08·T5`, `13·DOC1` y `13·DOC3` —ejemplo incluido, palabra por palabra— se reemplazó por el enlace (`M5`).

**Las diez que reprueban, y por qué.** No son defectos de redacción: son decisiones de catálogo, y el catálogo lo decide el usuario.

| Reglas | Fila | Qué falta decidir |
|---|---|---|
| `F4.1`–`F4.5` | 6 | el sub-ID decimal no lo contempla `M4`: legalizarlo o promoverlas a `F14`… |
| `F4`, `F4.3`, `F4.5` | 8 · 9 | llevan dos exigencias que se cumplen por separado; partirlas crea IDs nuevos |
| `F5`, `F6`, `F7` | 2 · 4 | el dueño del tema es `08` y `13`; derogarlas a favor de `T5`, `DOC1` y `DOC3` es `M11` |
| `F12` | 8 · 9 · 10 | su texto está **congelado por decisión del usuario** y el agente no lo reescribe |

Cada una lo dice en su propio archivo, con la marca *"regla vigente y reprobada"* que ya usa `M4`: siguen rigiendo (`M10` — un cambio de norma no reabre lo cerrado), pero no son conformes hasta que se resuelva.

## 2.4.0 — 2026-08-07

**MENOR** (el capítulo 02 pasa a carpeta; ninguna regla cambia qué exige ni qué ID tiene).

**`02 · Flujo de trabajo` se muda a su carpeta.** Era el archivo más grande del estándar —46 KB, catorce reglas y cinco subpartes en un solo `.md`— y ya tenía dos reglas viviendo aparte (`F12/`, `F13/`), así que el capítulo se leía en dos sitios a la vez. Ahora sigue el mismo molde que `00-identidad-y-rol/` y `20-meta-reglas/`: `base.md` es el índice y cada regla tiene su archivo en `reglas/`.

- `base/02-flujo-de-trabajo.md` → `base/02-flujo-de-trabajo/base.md`. Queda como índice: la tabla de las catorce reglas con qué exige cada una, y la secuencia del flujo. De 494 líneas a 36.
- `base/02-flujo-de-trabajo/reglas/` — **una regla, un archivo `<ID>-<título>.md`**, igual que `ID1`–`ID6` y `M1`–`M15`: `F0`–`F13`, más las cinco partes `F4.1`–`F4.5`, con el texto sin reescribir. Sin subcarpetas: `F12/` y `F13/` colgaban del capítulo y eran las únicas reglas fuera del sitio de las reglas.
- `base/02-flujo-de-trabajo/estructura-base.md` — el anexo de `F13` (el árbol obligatorio) pasa a la raíz del capítulo, donde `20-meta-reglas/` ya tiene los suyos (`checklist.md`, `estructura-regla.md`).
- **Las citas se reenlazaron al archivo de destino**, no a un ancla del índice: `02·F5` ahora abre la regla `F5`, no un encabezado dentro de un archivo de 46 KB. Aplica `M15`.

**Efecto en el arranque:** el cargador inyecta el índice de los capítulos temáticos, no su texto. Antes el índice de `02` era una línea de 46 KB; ahora son quince líneas que dicen de qué trata cada regla, y el agente lee **solo la que va a tocar**. El gate `F13` se sigue cargando literal — cambió su ruta (`validadores/cargador.py`).

Lo que **no** cambió: ningún ID, ningún texto de regla, ninguna exigencia. `F12` conserva intacto el texto literal del usuario.

## 2.3.0 — 2026-08-07

**MENOR** (aditivo: una regla nueva y un validador; ningún proyecto que herede el estándar tiene que hacer nada).

**Toda cita a otra regla lleva su enlace.** Citar por ID —`M5`, `09·G6`— obliga a quien lee a salir a buscar: abrir el capítulo, encontrar el encabezado. Con 206 citas repartidas en 43 archivos eso es fricción suficiente para que nadie compruebe nada, y una cita que nadie sigue es una dependencia que nadie verifica.

- `base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md` — la regla. Extiende `M4`, que fija el ID y la forma `NN·ID`.
- **Las 206 citas de `base/` quedan enlazadas**, al archivo y al ancla del encabezado. Las que viven en su propio archivo enlazan al archivo, sin ancla: un ancla de más se rompe al renombrar el título.
- **De paso se normalizaron tres formatos que convivían** — `` `04·S4` ``, `` `00` · N3 `` y `` `00`·N3 `` — a la única forma que `M4` admite. No es un cambio de norma: es aplicar la que ya estaba escrita.

Lo cercado no se tocó: ahí las citas son el molde que alguien va a copiar, no citas a nadie.

Detrás: `validadores/citas.py` (nuevo) — indexa dónde vive cada regla leyendo `base/`, enlaza y valida. Entra en `validar.py estandar`, así que una cita suelta o un enlace a una regla inexistente se reportan solos. 11 pruebas nuevas (191 en total).

## 2.2.0 — 2026-08-07

**MENOR** (las catorce meta-reglas pasan a archivo propio y se les aplica el checklist; ninguna cambia qué exige).

**El capítulo 20 se somete a sí mismo.** `M14` dice que ninguna regla nace fuera del procedimiento y que su cierre es el checklist en `CUMPLE`. Se aplicó a `M1`–`M14`. **Resultado: 10 cumplen, 4 no** — y las cuatro reprueban la misma fila, la 17, que exige decisión del usuario.

**La regla se separó de su explicación.** Cada archivo de `reglas/` conserva **solo la exigencia**: encabezado, cuerpo de una a cuatro líneas, ejemplo y checklist. Lo que desarrollaba, ilustraba o justificaba la regla —tablas, listas de apoyo, el porqué— vuelve a `base.md`, a una sección `### M<n>` por regla, enlazada desde el cuerpo. Con eso las filas 9 (una sola exigencia) y 10 (de una a cuatro líneas) pasan a verde en `M2`, `M5`, `M7` y `M12`, que antes las reprobaban.

**Efecto que conviene tener presente:** varias piezas movidas **mandan**, no solo explican — los tipos MAYOR/MENOR/PARCHE de `M10`, las dos prohibiciones de `M7` (sin ciclos, nunca hacia arriba), las tres aclaraciones de `M8`, el orden de búsqueda de `M12`, la tabla de destinos de `M13`. Siguen siendo texto del capítulo y el agente las lee igual, pero **ya no son texto de una regla citable por ID**. Si alguna debe poder citarse, se promueve a regla propia (`M15`…) — es decisión del usuario.

- `base/20-meta-reglas/reglas/` — las catorce, una por archivo, con el texto sin reescribir. `base.md` queda como capítulo e índice (de 204 líneas a 60).
- Se añadió el ejemplo INCORRECTO/CORRECTO que faltaba en nueve (`M2`, `M4`, `M5`, `M7`, `M9`, `M10`, `M11`, `M12`, `M13`) y el enlace de `M5` a su propio anexo `estructura-regla.md`, que no tenía — rompía la fuente única que `M2` exige.
- `validadores/reglas-validables.md` — las catorce clasificadas (`M9`). Siete se validan **en seco** sobre el propio estándar (`M3`, `M4`, `M5`, `M7`, `M9`, `M10`, `M14`): son las más rentables del catálogo y hoy no existe ninguna.
- `validadores/cargador.py` — el índice listaba las reglas nuevas como "(sin título)": un archivo de una sola regla no lleva `H1`, su encabezado es el `##` de la regla. Ahora lo usa como respaldo.
- `base/00-identidad-y-rol/reglas/` — corregida la aritmética de los seis sellos: eran `17 ✅ · 3 N/A`, no `16 ✅ · 4 N/A`.

**Las cuatro que no cumplen** quedan marcadas en su propio archivo, vigentes y reprobadas (`M10`: un cambio de norma no reabre lo cerrado). Las cuatro reprueban **solo la fila 17** — no choca con ninguna regla vigente:

| Regla | Con qué choca |
|---|---|
| `M2` | no contempla que el preámbulo comparta el número `00` con el núcleo |
| `M4` | no contempla los sub-ID decimales que el catálogo ya usa (`F4.1`–`F4.5`, `F12.1`–`F12.13`) |
| `M7` | el catálogo usa una cuarta forma de dependencia —el bloque `Encadenamiento`— 22 veces |
| `M8` | dice que las `[BLINDADA]` no admiten excepción, y `00·N1` es blindada y tiene una escrita |

Ninguna se puede cerrar sin decidir qué gana: o la meta-regla absorbe la práctica, o la práctica se corrige. Es del usuario.

## 2.1.0 — 2026-08-07

**MENOR** (aditivo: una regla nueva; ningún proyecto que herede el estándar tiene que hacer nada).

**`20·M14` · Ninguna regla nace fuera del procedimiento.** El capítulo tenía trece meta-reglas que gobernaban **cada pieza** de la creación de una regla —dónde va, qué ID lleva, qué forma tiene, cómo se versiona— pero ninguna gobernaba **el acto completo**. El procedimiento de nueve pasos existía como *sección*, sin identificador: no se podía citar desde un commit ni desde una spec, ni exigir por ID. `M14` cierra ese hueco.

Su cierre es el checklist en `CUMPLE`: sin eso la regla no se publica, se corrige o se retira.

- `base/20-meta-reglas/base.md` — la regla, con su checklist aplicado al pie. Se aplicó a sí misma: sería incoherente que la regla que exige el checklist naciera sin él.
- `validadores/reglas-validables.md` — `M14` clasificada (`M9`) como validable parcial: que la regla haya recorrido el procedimiento no lo decide un script, pero su cierre sí — la fila 19 ya la comprueba `version.py`, y la presencia del bloque de checklist es mecánica.

Queda anotado que las otras trece `M` siguen sin evaluar, igual que el resto del catálogo.

## 2.0.0 — 2026-08-07

**MAYOR** · `⚠ obliga a migrar`. Un proyecto al día tiene que correr el instalador **una vez**.

Nada de lo que un proyecto hereda del estándar puede quedarse viejo. Antes se intentaba detectar comparando títulos de sección y fechas de archivo, y las dos cosas fallan: un paso nuevo **dentro** de una sección que ya existía no cambia ningún título, y la fecha miente en cuanto alguien clona el repositorio o edita el archivo por cualquier motivo.

- **El sello.** `CLAUDE.md`, `historico-chat/README.md` y `.agente/stack-instalacion.md` llevan al final `<!-- huella: … · estandar X.Y.Z -->` con la huella de **la plantilla contra la que se sincronizaron** —no la del archivo local, que cada proyecto llena con lo suyo—. Cualquier cambio de la plantilla rompe la coincidencia, venga por dentro o por fuera del documento.
- **Quedar viejo reprueba.** Era AVISO y el componente pasaba igual: un proyecto con el `CLAUDE.md` viejo figuraba como instalación completa.
- **El registro.** Cada actualización deja un `.md` en `documentacion/versiones/`: desde cuándo el proyecto usa esa versión, qué componentes se actualizaron con su huella antes y después, qué aplicó el instalador y qué quedó pendiente. Va en `documentacion/` y no en `.agente/` porque `.agente/` está en el `.gitignore`, y saber bajo qué versión cerró cada fase tiene que poder mirarse desde cualquier copia del repositorio. Componente nuevo del stack: `versiones`.
- **El número de versión deja de reprobar.** Al proyecto no le interesan todos los cambios del estándar, solo los que tiene que aplicar: que declare `1.8.0` con el central en `2.0.0` no obliga a nada por sí solo, y dejarlo en rojo por eso es ruido que enseña a ignorar la alerta. El desfase se informa al margen; `version` ahora solo exige que la versión adoptada esté **declarada**, porque sin ella no hay con qué sellar una fase cerrada.

**Cómo se migra** — la línea de siempre, la del paso 6:

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

Deja los sellos puestos y escribe el primer registro. Hasta que se corra, `claude-md`, `historico` y `stack-instalacion` salen en rojo: no porque el proyecto esté mal, sino porque todavía no declara contra qué versión se sincronizó.

Detrás: `validadores/versiones.py` (nuevo — sellos, comparación y registro), `checklist.py`, `instalar.py`, `validar.py versiones` para verlo a mano, y 19 pruebas nuevas (180 en total).

## 1.6.0 — 2026-08-07

**MENOR.** Ningún proyecto que herede el estándar tiene que hacer nada: la exigencia nueva recae sobre quien escribe reglas **del estándar**.

**El checklist respondido queda dentro del capítulo, en dos piezas.** En 1.5.0 la sección decía lo contrario —que no se persistía copia por regla, para no inflar `base/`—. Se cambia por una razón que pesa más: **que una auditoría posterior no vuelva a analizar lo ya verificado**. La regla cuyo sello dice `CUMPLE` contra la versión vigente se salta; el trabajo se concentra en las que no lo traen o lo traen anulado. Sin esto, cada auditoría reevalúa el catálogo entero desde cero.

Dos piezas, y cada una donde sirve:

1. **El instrumento — `base/20-meta-reglas/checklist.md`, archivo nuevo.** El checklist **es estándar**, así que vive con las meta-reglas, al lado de su `base.md` y como fuente única (`M2`): las 20 filas con su meta-regla y su criterio de aprobado, cómo se decide el resultado, el molde de cómo se aplica, la regla de caducidad, y qué filas puede decidir un script (once) y cuáles piden leer la regla (nueve).
2. **La evaluación — dentro de cada regla.** Al final de su archivo, como `###`: el veredicto, contra qué versión y en qué fecha, el resultado por bloque, las `N/A` justificadas, y **el enlace al instrumento** — para que quien abra una regla suelta sepa de dónde sale esa evaluación. No repite las 20 filas (`M5`).

- `base/20-meta-reglas/base.md` — la sección del checklist queda en resumen + enlace, como ya hacen `F12` y `F13` con sus fuentes únicas.
- `base/00-identidad-y-rol/reglas/` — las seis reglas quedan evaluadas: 16 ✅ · 0 ❌ · 4 N/A · **CUMPLE**.
- `base/00-identidad-y-rol/base.md` — el capítulo lo dice y enlaza el instrumento.

**Backlog que esto abre:** las otras 164 reglas de `base/` quedan **sin sellar**. No es incumplimiento retroactivo —`M10` dice que un cambio de norma no reabre lo cerrado— pero sí es la cola de trabajo: hasta que una regla se selle, sigue entrando en cada auditoría. Se salda por capítulos, no de una vez.

## 1.5.1 — 2026-08-07

**PARCHE** (redacción y una justificación que había quedado falsa; no cambia qué se exige).

Se aplicó el checklist recién agregado a las seis reglas de `00 · Identidad y rol`. **En la primera pasada ninguna cumplía.** El resultado quedó dentro de cada regla, en [`base/00-identidad-y-rol/reglas/`](base/00-identidad-y-rol/reglas/).

- `base/20-meta-reglas/base.md` — la tabla de `M1` describía el preámbulo como *"No: describe, no exige"*. Desde que el capítulo tiene reglas (`ID1`–`ID6`, v1.4.0) esa frase era falsa, y las seis reglas chocaban con `M1` — la fila 17 del checklist. La columna es **¿Se ajusta?**: la respuesta sigue siendo **No** y la precedencia no cambia; lo que se corrigió es la justificación, que ahora dice *"un proyecto no redefine quién es el agente ni el molde de las reglas"*.
- `base/00-identidad-y-rol/reglas/` — `ID1` y `ID6` repetían texto de `01·C14` y de `20·M1` además de enlazarlo (fila 11, `M5` sin texto prestado): ahora difieren en vez de reformular. `ID1`–`ID4` pasaron de tercera persona descriptiva a presente imperativo, que es lo que pide `M5`. `ID5` gana el enlace a `00·N2`, de donde sale que la autorización sea de un solo uso.

Sigue disponible, y es decisión pendiente del usuario, la otra vía para el choque: que el capítulo deje de ser preámbulo y pase a **capa 2**. Eso sí movería la precedencia, y por eso no se tomó por cuenta propia.

## 1.5.0 — 2026-08-07

**MENOR** (aditivo: agrega una comprobación, no cambia ninguna exigencia existente).

- `base/20-meta-reglas/base.md` — sección nueva **«Checklist de la regla — qué cumple y qué no»**, entre el procedimiento de alta y la higiene del conjunto. Veinte filas agrupadas en cinco bloques (dónde va · cómo se identifica · cómo está escrita · cómo se relaciona · qué obliga fuera de su texto), cada una con su meta-regla y su criterio de aprobado, y un resultado al final que dice **CUMPLE** o **NO CUMPLE**.

El criterio de resultado es binario a propósito: una sola fila en ❌ y la regla no se publica. No hay "cumple parcial" — una regla a medias es la que después nadie sabe si rige. Solo cuatro filas admiten `N/A` (ejemplo, dependencias, ciclos y excepción), y siempre con motivo escrito.

Por qué ahí y no en `estructura-regla.md`: el checklist verifica `M1`–`M13` completas, y el anexo solo desarrolla `M5`. Además no cabía dentro de `M5`, que exige cuerpo de una a cuatro líneas.

La sección deja anotado cuáles de las veinte filas puede decidir un script solo (once) y cuáles piden leer la regla (nueve). Esa división es la especificación del validador de meta-reglas que falta.

## 1.4.0 — 2026-08-07

**MENOR** (aditivo: reglas nuevas en un capítulo que no las tenía; nada de lo que ya se cumplía deja de valer).

El capítulo del preámbulo se ajusta al capítulo 20: deja de ser prosa y pasa a tener reglas con identificador.

- `base/00-identidad-y-rol/reglas/` — seis reglas nuevas, **una por archivo**, nombradas `<PREFIJO><n>-<título>`: `ID1` criterio de desarrollador senior · `ID2` registro técnico sin adornos · `ID3` qué cuenta como entregado · `ID4` el ciclo completo de entender a documentar · `ID5` el borde del rol (seis cosas fuera por definición) · `ID6` los roles por etapa no cambian la precedencia.
- `base/00-identidad-y-rol/base.md` — pasa a ser el capítulo con el índice enlazado a las seis. El texto que antes era prosa suelta queda repartido en las reglas; lo que ya decía otro capítulo se enlaza en vez de repetirse (`20·M5`).
- `base/20-meta-reglas/estructura-regla.md` — el prefijo **`ID`** se registra en la tabla de letras ocupadas, como exige `M4` antes de estrenar un prefijo.
- `validadores/reglas-validables.md` — `ID1`–`ID6` clasificadas (criterio humano, `M9`). `ID3` se anota como caso parcial: sus cuatro condiciones ya se validan por separado; lo que no se valida es la conjunción.

Con esto queda cerrada la primera mitad del hallazgo **H-22** del informe de `analisis/`: el capítulo que `02·F0` citaba como fuente de reglas ya tiene reglas citables. Sigue abierto que el número `00` esté compartido con el núcleo.

## 1.3.1 — 2026-08-07

**PARCHE** (no cambia qué se exige; solo dónde vive el texto).

- `base/00-identidad-y-rol.md` pasa a `base/00-identidad-y-rol/base.md`. El capítulo del preámbulo queda con carpeta propia, como `20-meta-reglas/`, para poder crecer con anexos sin inflar el archivo que se carga en cada turno. El texto no cambió.

Detrás: `validadores/cargador.py` decidía qué se carga **literal en todos los turnos** por el nombre del archivo (`00-`, `01-`). Con el capítulo en carpeta, el nombre pasa a ser `base.md` y la identidad del agente habría caído al índice — es decir, el agente arrancaría sin saber quién es. Ahora la comprobación mira el **primer tramo de la ruta**, así que un capítulo del núcleo carga igual viva en archivo suelto o en carpeta.

## 1.3.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). El histórico de sesiones deja de depender de que el agente se acuerde de escribirlo:

- Plantilla nueva: `historico-chat.md` — el `README.md` de la carpeta `historico-chat/` de cada proyecto.
- `CLAUDE.md.plantilla`: punto **2.3** (la carpeta, quién la escribe, se versiona, y cómo excluirla si el chat maneja datos sensibles) y punto **6** ampliado: el instalador es el camino por el que **toda** herramienta nueva del estándar llega al proyecto, sin pasos manuales. Si algo exige configurar a mano, es defecto del estándar.

Detrás: `validadores/hook_historico.py` (enganches `UserPromptSubmit` y `Stop`) e `instalar.py`, que los deja puestos y crea la carpeta. Un proyecto al día no tiene que hacer nada: los recibe la próxima vez que corra el paso 6.

Y el **stack de instalación**: la lista de todo lo que un proyecto debe tener para que el agente esté completo.

- Plantilla nueva: `stack-instalacion.md` — los 11 componentes, qué es cada uno y cómo se instala. Se copia a `./.agente/` de cada proyecto, sellada con la huella del original: si el estándar agrega un componente, la copia deja de coincidir y eso se reporta como actualización pendiente.
- `CLAUDE.md.plantilla`: punto **2.1** (los dos archivos que el estándar escribe en `.agente/` y no se editan a mano) y paso **8** — mientras exista `.agente/INSTALACION-INCOMPLETA.md`, el agente no está completo y debe decir qué falta en cada respuesta. No bloquea: el único gate sigue siendo `F13`.

Detrás: `validadores/checklist.py` (la comprobación de cada componente; la lista se lee de la plantilla, no se duplica en código), `hook_checklist.py` en `UserPromptSubmit`, y `validar.py checklist --raiz` para verlo a mano.

## 1.2.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Un capítulo de **preámbulo**:

- `00 · Meta-reglas` — la regla de reglas: jerarquía de cuatro niveles, organización por dominio con fuente única, orden determinista de desempate ante conflicto, formato canónico de una regla, ID estable, dependencias declaradas (`extiende` / `depende de` / `deroga`), excepciones escritas dentro de la regla, criterio de validable, versionamiento obligatorio, derogación en vez de borrado, y procedimiento para agregar una regla sin duplicar ni contradecir.

No cambia ninguna regla existente: **formaliza** las convenciones que la base ya usaba de hecho y cubre lo que no estaba escrito (desempate, dependencias, derogación, anti-duplicación).

## 1.1.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Dos capítulos **opt-in** de dominio DevOps:

- `18 · Despliegue e infraestructura` — despliegue como artefacto versionado, IaC, build-una-vez, config por entorno fuera del artefacto, release reversible, checklist de despliegue, health/readiness, y correr contra producción gateado por el usuario. Extiende `09·G6`.
- `19 · Observabilidad y operación` — logs estructurados, señales doradas + trazas, SLO/alertas como código sobre síntomas, runbooks, postmortem sin culpa. Extiende `05`.

Plantillas nuevas: `checklist-despliegue.md`, `postmortem.md`. Toggles en `CLAUDE.md.plantilla §5.1`.

## 1.0.0 — 2026-08-06

Primera versión sellada del estándar. Línea base: núcleo blindado (`00`), conducta y flujo (`01`–`02`), buenas prácticas (`03`–`17`), plantillas de capa 3, memoria por señales con vigencia y ciclo de deuda, y la capa de validadores automáticos + hooks.

A partir de aquí, cada cambio de `base/` o `plantillas/` suma una entrada con su tipo.
