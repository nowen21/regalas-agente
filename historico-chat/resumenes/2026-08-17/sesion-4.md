# 2026-08-17 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-17-sesion-4.md](../../2026-08-17-sesion-4.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «[sesión 3](sesion-3.md)» — allá se ejecutaron 25 de las 51 fases aprobadas y quedaron 26 detenidas por 42 dudas del usuario. Acá se pidió resolver los pendientes, y el pedido se volvió otro: **que ninguno quede suelto**.

---

## Hallazgos de esta sesión

### H-1 · El pedido cambió al mirar el backlog, y el cambio fue el hallazgo

**Qué pasó.** Se pidió «resolver los pendientes». Al triar los 30 abiertos, el agente los separó en tres montones —los que solo esperan una decisión, los que se construyen, los de limpieza— y propuso empezar por el más urgente. El usuario cortó eso con una sola línea:

> *«todos los pendientes deben estar dentro de una HU, nada puede estar suelto»*

**Por qué importa.** El triaje del agente era por urgencia; el del usuario es por **cadena**. Son preguntas distintas y la segunda va primero: da igual cuál pendiente sea el más urgente si al construirlo se salta la historia. [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) ya lo decía —un pendiente se baja a historia y se construye como fase—, pero lo decía **para el momento de construir**. El usuario lo corrió al momento de **abrir**.

**Dónde queda.** En el trabajo entero de esta sesión, y en las `RN-06` a `RN-08` de [EP-004 · HU-016](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md).

### H-2 · Seis pendientes no tenían ninguna historia que los recibiera

**Qué se midió.** Se enrutaron los 33 archivos de [pendientes/](../../../pendientes/README.md) contra las 68 historias del árbol de épicas. **Veintisiete cabían** en una historia que ya existía. **Seis no cabían en ninguna**, y hubo que escribirlas:

| Historia nueva | Recibe |
|---|---|
| [EP-001 · HU-011 — Buscar antes de preguntar](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md) | el 24, que ya la traía redactada adentro |
| [EP-001 · HU-012 — Inventario de acciones y riesgo](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md) | el 13 |
| [EP-001 · HU-013 — Capítulos opt-in de dominio](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) | el 08 y el 12 |
| [EP-005 · HU-011 — Dónde termina el estándar](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) | el 15 |
| [EP-005 · HU-012 — Hacer cumplir lo que solo se recuerda](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) | el 58 |
| [EP-007 · HU-008 — El proyecto reporta al estándar](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) | el 36 |

**Por qué importa.** Seis es la medida del hueco. No es que faltaran seis documentos: es que **seis pendientes se iban a construir sin que nadie hubiera escrito cuándo se dan por aceptados**. El 36 y el 58 son los peores del grupo, porque los dos son defectos reportados por un proyecto real y llevaban días esperando.

**Y hay una lectura al revés que también sirve:** las 16 automatizaciones del [09](../../../pendientes/09-autonomia-sin-ia.md) cupieron **todas** en historias que ya existían. Ese tema estaba bien repartido desde el principio, y ahora se puede demostrar.

**Dónde queda.** Las seis escritas con el molde completo, en su épica y en los dos índices.

### H-3 · El campo que la HU-016 pedía ya existía a medias, y en el sitio equivocado

**Qué se encontró.** [EP-004 · HU-016](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) decía desde el 2026-08-16 que faltaba «una pieza antes del programa: un sitio fijo donde el pendiente declare su fase». Al enrutar se vio que el [52](../../../pendientes/hecho/el-sello-del-checklist-se-comprueba.md) ya traía una fila `Historia que lo recibiría` y ningún otro la tenía. Un solo archivo de 33 con el campo, y con otro nombre.

**Por qué importa.** Es el patrón que este repositorio ya conoce: **una buena costumbre de un solo archivo no es una convención**. Mientras viva en uno solo, el programa que la lea no encuentra nada que leer, y quien escriba el siguiente pendiente no la va a copiar porque no la va a ver.

**Dónde queda.** El campo quedó fijo y con un solo nombre —`Historia de usuario`— en la ficha de cabecera de los **33** archivos. La tarea de la HU-016 que pedía fijarlo está marcada como hecha.

### H-4 · El script de enrutamiento metió la fila dentro de la tabla equivocada, en tres archivos

**Qué pasó.** El programa que escribió las 33 filas buscaba «la primera tabla de las 15 primeras líneas». En el [18](../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md), el [19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) y el [23](../../../pendientes/hecho/plantillas-separa-modelos-de-procedimientos.md) esa tabla no era la ficha: era una tabla de contenido. La fila quedó entre los datos.

**Por qué importa.** Ningún validador lo habría visto: el enlace resuelve, la tabla sigue siendo tabla y el conteo daba 33 de 33. **Lo destapó una comprobación escrita a propósito** —que la fila estuviera precedida por el encabezado vacío `| | |`—, no la corrida de siempre. Una comprobación que se escribe para dudar del propio trabajo encuentra lo que las otras no buscan.

**Dónde queda.** Los tres archivos revertidos y rehechos. La regla del programa quedó siendo «encabezado sin nombres de columna», que es lo que distingue la ficha de una tabla cualquiera.

### H-5 · El nombre de la HU-016 se quedó corto y no se cambia

**Qué se decidió.** La historia se llama «el pendiente **cerrado** nombra su fase» y desde hoy cubre también al abierto. Renombrar la carpeta habría dejado rotos todos los enlaces que la citan.

**Por qué importa.** Eso es exactamente el [pendiente 54](../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md) —cerrar un pendiente dejó 12 enlaces huérfanos en un solo día—, y no tenía ningún sentido reproducirlo dentro del trabajo que lo enruta. **El nombre queda; el alcance lo dicen las `RN` y los `CA`**, que es el mismo criterio con que [`20·M11`](../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) prohíbe renumerar una regla.

**Dónde queda.** Escrito dentro de la propia historia y en su `README`, para que nadie lo «arregle» después.

### H-6 · Lo que esta sesión **no** hizo, y por qué

**Ningún pendiente se cerró.** El pedido inicial era resolverlos; el segundo fue enrutarlos, y eso es lo que se hizo. Los 30 siguen abiertos.

**No se tocó `base/` ni `plantillas/`**, así que no hubo entrada de `CHANGELOG` ni subida de `VERSION`: lo que cambió es `documentacion/` y `pendientes/`, y [`20·M10`](../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) pide versión cuando cambia lo que se le exige a un proyecto. Acá no cambió.

**La regla no está escrita todavía.** «Todo pendiente nombra su historia» vive hoy en las `RN` de una HU, no en `base/`. La fase que construye la comprobación quedó abierta —hallazgo 7— y espera aprobación; la que escribiría el texto **no se puede abrir**, porque no hay historia que la reciba —hallazgo 8—.

**Lo que quedó comprobado:** `validar.py estandar` da **0 fallas** con los mismos 5 avisos conocidos —los falsos positivos del [55](../../../pendientes/hecho/los-enlaces-de-ejemplo-no-son-enlaces.md)—, y las 36 pruebas del repositorio pasan.

### H-7 · La HU ya existía, así que la fase es la `B` — y no está detenida, al revés que la `A`

**Qué pasó.** Al ir a construir la comprobación, `EP-004 · HU-016` ya tenía fase `A` —una de los 51 planes, abierta y sin aprobar—. El usuario lo zanjó en una línea: *«si ya existe la HU se crea otra fase»*. Quedó abierta [`B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia`](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/README.md), con sus dos planes y su estado, en la estación 4.

**Lo que se supo al escribirla.** La `A` está detenida por dos dudas, y **el enrutamiento de hoy contestó una**: «¿dónde se declara, una línea fija o una sección?» ya no es una opinión — es la fila `Historia de usuario` de la ficha, medida en 33 archivos. Eso **destraba la duda 27** del [pendiente 59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). Cerrarla formalmente es de la fase `A`; se reporta y no se aprovecha desde la `B`.

**Y un plan que quedó viejo.** La fase `A` declara en su §2.1 que **crea** `validadores/pendientes.py`. El archivo ya existe —156 líneas, escrito para HU-018 y commiteado ayer—. Se reporta, no se corrige desde acá.

### H-8 · Se fue a cambiar `02·F23` y no hubo dónde bajarlo

**Qué se buscó.** La fase `B` construye el programa que comprueba, pero el texto de [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) no dice «desde que se abre». Hacer fallar por algo que la regla no exige es peor que no comprobarlo, así que había que escribir la frase. **No hubo dónde:** ninguna historia declara el capítulo `02` como su módulo. El `00` y el `01` tienen la suya; el `02`, no.

**Por qué importa.** El `02` es el capítulo de la cadena —`F0`, `F12`, `F15`, `F23`— y el más citado del repositorio. Si ningún sitio lo recibe, **todo cambio del `02` se ha venido haciendo sin cadena, incluida la regla que exige la cadena**. `F22` y `F23` nacieron en agosto y ninguna tuvo historia propia.

**Dónde queda.** El [pendiente 60](../../../pendientes/60-nadie-es-dueno-del-texto-del-capitulo-02.md), enrutado a `EP-001 · HU-007`. Es hermano del [47](../../../pendientes/47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md) y del [56](../../../pendientes/56-el-estandar-no-tiene-planteamiento.md): los tres son el mismo hueco a distinta altura.

### H-9 · Dos sesiones sobre el mismo árbol, y una falla que no es de nadie de acá

**Qué pasó.** Al commitear se vio que otra sesión está trabajando en el mismo directorio: sus archivos se tocaron a las 20:14 y 20:21, los de esta a las 20:22, y ya había commiteado a `main`. Se separó archivo por archivo mirando las horas de modificación, y el commit `1c36481` llevó **solo** lo de esta sesión: 58 archivos, dejando fuera seis fases nuevas y cuatro transcripciones suyas.

**Y hay una falla que no es de esta sesión.** `validar.py estandar` reporta un enlace roto en `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas`, que es una de las carpetas sin rastrear de la otra sesión. No se tocó.

**Por qué importa.** Esto es el [pendiente 22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) pasando en vivo, y hoy se resolvió a mano leyendo horas de modificación. **Nada lo impide ni lo avisa.** El día que las dos sesiones toquen el mismo archivo, una pisa a la otra en silencio.

### H-10 · El paso que nadie hacía era el sexto, y hay tres cierres que lo prueban

**Qué se midió.** El [pendiente 36](../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md) traía siete pasos dictados por el usuario para reportar un defecto del estándar sin tocarlo. Los cinco primeros se venían haciendo por criterio de cada sesión. **El sexto —avisarle al proyecto cuando la corrección esté— no lo hacía nadie.**

**Por qué importa.** Sin el aviso, el séptimo paso —el pendiente del proyecto queda abierto hasta confirmar— deja pendientes abiertos **para siempre**: nadie vuelve a mirar el repositorio ajeno. Y no es una hipótesis. Al construirlo aparecieron **tres cierres anteriores que se fueron sin aviso**: dos los espera `shopnest-mesa` y uno `dp`, y ninguno de los dos proyectos lo sabe.

**No se mandan hacia atrás.** Inventar hoy un aviso sobre una corrección de hace dos días es escribir una fecha falsa. Se anota quiénes son y quién los espera, en la §3 del [resultado_pruebas](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/resultado_pruebas.md).

**Y la señal de que la regla no inventa nada:** los 34 pendientes del backlog pasan la comprobación nueva **sin tocar ninguno**. Una regla que hay que salir a acomodarle el repositorio para que pase está describiendo otra cosa.

**Dónde queda.** [`02·F24`](../../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md), las dos plantillas, el aviso en `cerrar.py`, y la versión **23.7.0**.

### H-11 · El inventario decía 74 y su tabla listaba 68

**Qué pasó.** Al cerrar el 36 falló una prueba: la cuenta del programa daba `(74, 33, 41)` y el [48](../../../pendientes/48-inventario-hu.md) tenía escrito `(74, 32, 42)`. Al ir a corregirlo se vio lo otro: **las seis historias nuevas de ayer contaban en el encabezado pero no tenían fila en la tabla.**

**Por qué importa.** El encabezado se actualizó a mano al crearlas; la tabla no. Un inventario al que hay que creerle el encabezado porque su propia tabla no lo respalda **no sirve de inventario** — y las dos únicas de las seis que ya están construidas eran invisibles justo en el documento que existe para que nada quede invisible.

**Lo que lo destapó fue la prueba que compara las dos cuentas**, no una lectura. Es la razón por la que esa prueba existe.

**Dónde queda.** Las seis filas puestas, con lo que cada una tiene hoy en disco. 74 filas y 74 en el encabezado.

### H-12 · Siete pendientes decían «cerrado» y seguían en la carpeta de abiertos

**Qué se midió.** Al buscar qué construir después del 36 se revisó el estado escrito dentro de cada archivo, y **siete de los abiertos ya decían «cerrado»**: el 23, el 32, el 36, el 46, el 52, el 54 y el 55. Su trabajo estaba hecho y commiteado; lo que faltaba era mover el archivo.

**Por qué importa.** Marcar el estado y no mover el archivo es **la mitad del cierre**, y la mitad que falta es la que se ve: el conteo del [README](../../../pendientes/README.md) decía 30 abiertos cuando eran 28, y quien abriera la carpeta iba a leer siete temas como trabajo por hacer. Envejece solo, sin que nadie se equivoque en nada.

**Y no se podía hacer a mano.** Mover los siete arrastró **142 enlaces en 51 archivos**. Antes de que existiera [`cerrar.py`](../../../validadores/cerrar.py) —del [54](../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md), cerrado hace un día— esto era exactamente lo que hacía que nadie los moviera.

**Dónde queda.** Los siete en [`pendientes/hecho/`](../../../pendientes/hecho/), con el nombre de cómo cerraron y no del problema. Ninguno roto: `validar.py estandar` sin incumplimientos.

### H-13 · El aviso de vuelta estaba escrito, probado, y desconectado

**Qué pasó.** La versión 23.7.0 se publicó diciendo que `cerrar.py` manda el aviso al cerrar. La función estaba, con doce casos, todos pasando. **`main()` no la llamaba.** Cerrar un pendiente no avisaba a nadie — el defecto exacto que [`02·F24`](../../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md) acababa de venir a cerrar.

**Por qué ninguna prueba lo vio.** Las doce llamaban a `avisar()` **directamente**. Verificaban que la pieza funciona, no que esté conectada. Es un punto ciego con forma: cuanto mejor está probada una función aislada, más convincente se ve el módulo que no la usa.

**Lo destapó correr el comando de verdad.** Y al conectarlo salieron dos defectos más, los dos solo visibles fuera del laboratorio:

- **El estándar se mandaba un aviso a sí mismo.** Está en su propio registro y las rutas se comparaban por texto: el registro escribe `c:\` y el comando `C:\`. En las pruebas los proyectos de mentira nacían con la misma caja, así que nunca se vio.
- **El archivo salía `algo.md.md`.** El destino ya traía extensión.

**Dónde queda.** La 23.7.1, con un caso por cada uno — escritos sobre **lo que se vio fallar**, no sobre lo que debería pasar.

### H-14 · «Avisar a todos» llegó a uno de nueve

**Qué se midió.** La ficha del 36 decía avisar a **todos** los proyectos instalados. El aviso llegó a **shopnest-mesa** y a nadie más: los otros ocho **no tienen carpeta `pendientes/`**, y a un proyecto que no lleva backlog no se le inventa.

**La decisión de no inventarla sigue siendo la correcta** — escribir en el repositorio de otro tiene que tener el alcance de una línea. Lo que falla está más arriba: el instalador no la deja puesta, así que **ocho proyectos no tienen dónde escribir un pendiente**, ni suyo ni de nadie. El aviso no lo causó; lo hizo visible.

**Y es el 36 un nivel más abajo:** allá el estándar no avisaba; acá avisa y el aviso **se cae sin ruido**. Nadie se entera de que se perdió.

**Dónde queda.** El [61](../../../pendientes/61-el-aviso-de-vuelta-llega-a-uno-de-nueve.md), con las tres decisiones que hacen falta y cuál de ellas importa.

### H-15 · Cinco sellos del estándar decían dos cosas contrarias

**Qué se midió.** Cada bloque de checklist tiene dos mitades: una tabla de veinte casillas y un texto que explica qué falla. **En cinco reglas no coincidían** — el texto reprobaba una fila que la tabla mostraba en ✅. Más diez resúmenes que no cuadraban con su propia tabla, y una regla con **dos sellos apilados**.

**Por qué importa.** La tabla es lo que se lee: nadie recorre veinte filas de prosa, se mira el renglón de emoticones y se sigue. Cuando las dos mitades se contradicen, **gana la que se ve**, que era la falsa.

**Y el defecto no era de juicio.** En cuatro de los cinco se corrió **una casilla del bloque `C`** — siete seguidas, sin encabezado por columna. Nadie evaluó mal la regla: se equivocaron al transcribirlo, que es exactamente lo que un programa hace sin fallar.

**El detalle que más dice:** en los tres sellos del capítulo `01` la fila perdida fue siempre la **5**, la que dice que la base no nombra tecnología. Escrita en el texto las tres veces, y las tres veces sin llegar a la tabla. Es la fila que más incomoda del checklist, y es la que se cayó.

**Lo difícil fue no inventar.** La primera corrida reportó seis; el sexto estaba bien —un CUMPLE que cuenta qué reprobaba **antes** de corregirlo—. La mitad de los quince casos son de silencio: una comprobación que reporta de más se apaga a la semana, y apagada no encuentra nada.

**Dónde queda.** La fase [`B-EP-001-HU-009`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/B-EP-001-HU-009-el-sello-no-se-contradice/) y la v23.7.2. **No baja el 19 —las 72 siguen siendo 72—: lo vuelve confiable**, porque cualquier lista sacada de esos sellos habría estado mal contada.

### H-16 · Este resumen no existía para el programa que lo cuenta

**Qué pasó.** El enganche avisó *«el resumen de esta sesión sigue vacío»* teniendo quince hallazgos escritos. No era un defecto del enganche: **los hallazgos estaban escritos como `### 1 ·` y el programa busca `### H-1 ·`**, que es lo que dice [`plantillas/sesion.md`](../../../plantillas/sesion.md).

**Cuánto había.** Tres resúmenes, los tres del 2026-08-17, con **29 hallazgos invisibles** entre los tres. Los otros 44 del histórico sí siguen el molde.

**Por qué importa más de lo que parece.** No es solo que no se cuenten. La comprobación de *«¿se puede cerrar la sesión?»* **necesita encontrar un hallazgo antes de mirar el cierre**, así que en esos tres nunca corrió. Y el aviso de «sigue vacío» se marca a sí mismo como ya dado: se ve **una vez** y después calla para siempre. Un resumen escrito con la numeración equivocada queda mudo y nadie se entera.

**Lo destapó el enganche diciendo algo que parecía falso.** Es lo que hay que aprender: un aviso que contradice lo que uno ve suele estar leyendo otra cosa, no equivocándose.

**Dónde queda.** Los tres reescritos, 29 hallazgos legibles. **Falta la comprobación**: que un resumen con `### N ·` y sin ningún `H-` se reporte, en vez de contarse como vacío.

### H-17 · La regla que enseña a no nombrar frameworks nombraba dos

**Qué se midió.** Cuatro reglas de `base/` nombraban un stack, un dominio real o una herramienta del agente. El pendiente 19 decía **tres**; la cuarta la encontró el programa.

**Por qué importa.** Es el defecto que **daña a quien hereda, no a quien escribe**: un proyecto que instala el estándar lee reglas redactadas para el stack de otro. No rompe nada — se lee, se entiende a medias y se aplica peor. Por eso duraba.

**Y la peor es `01·C10`:** es justamente la regla que enseña a decidir si algo es transversal o local, y su criterio para decidirlo era *«¿tendría sentido en un proyecto React + Django de otra empresa?»*. **La pregunta que le pedía al agente hacerse era la que ella misma no pasaba.**

**Cómo se le pasó la cuarta.** El sello de `04·S10` **sí había argumentado la fila 5** —para defender `killall`, `pkill` y `taskkill`, que es lo llamativo— y al hacerlo la dio por revisada. Los dos intérpretes estaban tres líneas más arriba.

> **Un argumento sobre una fila no es una revisión de la fila.** Quien lee el sello ve que alguien la miró; no ve qué parte miró. Es lo mismo que la fase `B` encontró en las tablas, un nivel más adentro.

**Lo que más pesa no es lo que se quitó.** Tres nombres se conservan —`killall`, `pkill`, `taskkill`—, y se les escribió **un caso de prueba** en vez de dejarlo en el sello: un criterio que solo vive en un sello se pierde, y la próxima pasada los borra creyendo que mejora.

**Dónde queda.** La fase [`C-EP-001-HU-009`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/C-EP-001-HU-009-las-tres-reglas-con-nombre-propio/) y la v23.7.3. **Las 72 siguen siendo 72** —las cuatro reprobaban otras filas también—, pero el daño a quien hereda baja a cero.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ los 30 siguen abiertos, cada uno con su historia declarada |
| Toda historia disparada está escrita en su épica | ☑ las seis nuevas, con su fila en la épica y en los dos índices |
| Lo que se hizo está aprobado y guardado | ☑ commit `1c36481` · **falta** el de la fase B y el pendiente 60 |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

**Lo que sigue, cuando se retome:** aprobar y ejecutar la fase `B-EP-004-HU-016`. Sin ella el enrutamiento de hoy es un estado que nada sostiene. Y decidir el [pendiente 60](../../../pendientes/60-nadie-es-dueno-del-texto-del-capitulo-02.md), que es lo único que permite escribir el texto de la regla.

<!-- aviso: resumen sin hallazgos -->
