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

**Qué se midió.** Se enrutaron los 33 archivos de [pendientes/README.md/](../../../pendientes/README.md) contra las 68 historias del árbol de épicas. **Veintisiete cabían** en una historia que ya existía. **Seis no cabían en ninguna**, y hubo que escribirlas:

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

**Por qué importa.** Esto es el [pendiente 22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) pasando en vivo, y hoy se resolvió a mano leyendo horas de modificación. **Nada lo impide ni lo avisa.** El día que las dos sesiones toquen el mismo archivo, una pisa a la otra en silencio.

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

### H-18 · El aviso equivocado se deja de leer, y el silencio no deja rastro

**Qué se construyó.** El enganche ya distingue un resumen **vacío** de uno que **no puede leer**: dos avisos, dos marcas propias, y el segundo dice **cuántos** hallazgos hay que renumerar. Fase [`C-EP-005-HU-008`](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible/), sin cambio de versión — no toca `base/` ni `plantillas/`.

**Por qué el número importa.** Un aviso que se puede desmentir de un vistazo se deja de leer: quien ve «este resumen sigue vacío» con quince hallazgos en pantalla concluye que el programa se equivocó, y sigue. Y es la reacción correcta ante algo que afirma lo falso. **El programa no se equivocaba al mirar — se equivocaba al nombrar lo que vio.**

**El defecto se tapaba a sí mismo por tres caminos, y ninguno deja rastro:** el resumen se contaba como vacío; la comprobación del cierre **nunca corría**, porque necesita encontrar un hallazgo antes de mirar; y el aviso se marca como ya dado, así que se ve una vez y calla para siempre.

**Dos marcas y no una**, con caso propio: con una sola, avisar de un caso apagaría el otro **para siempre**, y el aviso no se recupera.

**Y los tres se renumeraron después de escribir la comprobación**, para que se estrenara sobre los archivos que estaban mal — igual que en la fase `B` del sello. Es la tercera vez hoy que ese orden es lo que hace que la comprobación sirva.

### H-19 · Enlazar no es lo mismo que enlazar en vez de copiar

**Qué se cerró.** Dos reglas —[`07·Q7`](../../../base/07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) y [`12·PR4`](../../../base/12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes)— que enlazaban a su vecina **y además la copiaban**. Fase [`D-EP-001-HU-009`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/D-EP-001-HU-009-enlazar-en-vez-de-repetir/), v23.7.4. **Las 72 en NO CUMPLE pasan a 70.**

**Por qué duraban, y es lo que hay que recordar.** Las dos tenían el enlace puesto, visible y correcto. La fila 11 no pide enlazar: pide **enlazar en vez de copiar**. Un enlace delante de un texto repetido **se lee como diligencia**, así que cumplían la mitad que se ve y sobrevivieron a varias lecturas.

**La forma correcta ya estaba escrita, en otra regla del mismo cuerpo.** `14·EST3` toma de `01·C3` el mismo criterio de alcance que `Q7` y estaba en CUMPLE: la nombra entre paréntesis como el motivo y todo lo demás es suyo. Faltaba leerlas juntas — es la tercera vez hoy que **la respuesta estaba en el repositorio y el trabajo era encontrarla**, no inventarla.

**Y un detalle que se repite:** el ejemplo de `PR4` era de logs, y al irse esa mitad quedó ilustrando lo que la regla ya no dice. **Peor que no tener ninguno**, porque manda a buscar la exigencia donde no está.

**Lo que no se hizo, y por qué.** Quedan tres de la categoría: `12·PR3`, `01·C16` y `04·S7`. **Ninguna es redacción** — dos piden decidir si una regla deja de existir, y derogar obliga a adoptarlo en todos los proyectos instalados.

### H-20 · El sitio para acortar sin perder nada estaba desde el principio

**Qué se cerró.** Diez reglas cuyo único defecto era el largo. Fase [`E-EP-001-HU-009`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/E-EP-001-HU-009-las-que-solo-sobraban-de-largo/), v23.7.5. **Las 70 en NO CUMPLE pasan a 60**, y ninguna cambia lo que exige.

**Lo que más enseña.** La fila 10 mide **solo el cuerpo** de la regla: el bloque INCORRECTO/CORRECTO no cuenta. Así que un ejemplo largo sale gratis y una enumeración en el cuerpo cuesta todo — **y aun así las reglas más largas tenían ejemplos cortos**. `01·C12` llevaba tres ejemplos de adjetivo arriba teniendo su bloque justo debajo, vacío de contenido.

**El sitio donde poner lo que sobraba llevaba ahí todo el tiempo, y nadie lo estaba usando.**

**Y el diagnóstico ya estaba escrito.** `20·M5` dice en la propia fila 10: *si no cabe, o son dos reglas o se está contando el porqué, que va a `notas/`*. Acertó **ocho de diez veces**. Es la cuarta vez hoy que la respuesta estaba en el repositorio.

**La medición fue el trabajo, no el trámite.** La primera reescritura dejó **cinco de las diez todavía pasadas**, y `09·G9` necesitó tres pasadas. Escribir corto no sale a la primera, y firmar un sello sobre un largo estimado ya costó cinco correcciones en esta misma historia.

**Deuda dicha:** el porqué que se sacó no se escribió en `notas/`. Está en los sellos —cada uno dice qué salió— pero no donde `M5` manda.

### H-21 · Una regla que tenía razón, aplicada donde no había mirado

**Qué pasó.** El [pendiente 18](../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md) contaba 354 enlaces que incumplen `13·DOC14`; hoy eran **1031**. Se construyó la reparación por programa, se aplicó a los 1031 — **y se revirtió entera.**

**Por qué.** `DOC14` pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*. Para el archivo de **la misma carpeta** ese propósito ya está cumplido, y la regla no distingue el caso. Aplicada literal, la tabla de contenidos de una fase quedaba con celdas de **132 caracteres para decir `plan_trabajo.md`**.

**Y son 747 de los 1031.** Tres de cada cuatro.

**Lo que hay que recordar:** una regla puede tener razón en el caso para el que se escribió y volverse contraproducente en el que no se miró — **y eso solo se ve aplicándola**. El validador llevaba días contando 1031 sin que nadie viera que eran dos poblaciones distintas.

**Se arreglaron los 284 de entre carpetas**, que son los que la regla resuelve de verdad, sin romper un solo enlace: el destino no se toca nunca.

**Y los casos encontraron dos defectos antes de tocar el repositorio:** la exclusión de `prompts/` se contaba contra la raíz equivocada —en el repositorio real las dos coinciden, así que habría funcionado hasta el día que no— y el texto entre comillas invertidas no lo ve nadie.

**Dónde queda.** La fase [`B-EP-004-HU-005`](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive/), sin cambio de versión. **La decisión sobre el vecino es del usuario**, y hasta que se tome el número no baja de 747.

### H-22 · Dieciséis mil marcas, y una fase que esperaba lo que ya estaba escrito

**Qué se midió.** Nace [`validadores/marcas.py`](../../../validadores/marcas.py), el primer programa que comprueba si el estándar cumple su propia [`00·ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md). Era el paso 1 del [pendiente 11](../../../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) —*contar antes de tocar*— y lo que lo tenía trabado desde el 2026-08-10.

**16 477 marcas en 820 archivos** fuera del histórico; **4 491 en `base/` y `plantillas/`**, que es lo que viaja a los proyectos. Las dos que pesan: raya larga 7 286, punto medio 6 237.

**La fase estaba detenida por una duda que su propio origen contestaba.** Llevaba desde ayer en la estación 6 esperando saber si la comprobación aplica a todo el repositorio o solo a lo que se entrega — y el pendiente 11 lo decía en su paso 3 desde hace ocho días: *«No tocar el histórico»*. **Es el primer caso encontrado de [`01·C23`](../../../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar)**, la regla que se escribió ayer.

**Lo incómodo del número.** Buena parte de esas 16 477 se escribieron **después** de que la marca quedara registrada, y [`02·F21`](../../../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) dice que desde ahí lo nuevo nace cumpliendo. No pasó — **y este resumen está escrito con las mismas marcas que acaba de contar.** El recuento no separa lo viejo de lo nuevo, y sin eso limpiar hoy es rehacer el trabajo el mes que viene.

**Y una decisión que se dejó a la vista en vez de esconderla:** el `·` de `09 · Control de versiones` y de los títulos de fase **se cuenta como marca**, porque el anexo llama marca a adornar títulos con él. Si el estándar quiere conservar esa forma, se escribe la excepción; no se hace un descuento callado en el programa.

### H-23 · Los trece roles en inglés, en español

Cerrado el [pendiente 21](../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md), v23.8.0. **211 apariciones en 39 archivos**, y cuatro archivos renombrados —`02·F2`, `13·DOC3`, `13·DOC6` y la plantilla de especificación— con sus citas arrastradas.

**Lo que costó no fue traducir: fue el orden.** Primero el texto, después los nombres de archivo, y al final las referencias que `mover` no resuelve porque llevan el marcador `«RUTA-ESTANDAR»` — esas quedaron rotas hasta que se arreglaron a mano.

**`00·ID6` se reselló**: editar el texto de una regla anula su checklist, aunque el cambio sea de idioma.

**Queda la carpeta `skills/generar-spec-modulo/` a propósito.** El nombre de una skill es cómo se la invoca: renombrarla cambia comportamiento, no solo texto.

### H-24 · La instrucción escrita habría borrado dieciséis mensajes

Cerrado el [pendiente 29](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md). La transcripción del 2026-08-15 pasó de 57 bloques a 48.

**El pendiente decía quitar los 25 bloques que no llevan la marca del enganche.** Al medir, solo **9 estaban repetidos palabra por palabra**; los otros **16 son mensajes que el usuario escribió de verdad**, sin gemelo en ninguna parte.

> **La instrucción se apoyaba en un supuesto que nadie comprobó:** que la marca del enganche estuviera siempre. Faltaba en la mitad del archivo. Y era un archivo que no se puede reconstruir.

**Queda sin saber por qué faltan esas 16 marcas.** O el enganche no las escribió ese día, o las escribió sin ellas — y si fue un defecto suyo, puede repetirse.

### H-25 · El origen de las reglas estaba a tres líneas de donde se busca

Del [pendiente 47](../../../pendientes/47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md): las reglas de negocio de esta casa no decían de dónde bajan. **Eran 57, no las 31 contadas el 2026-08-16.**

**No hubo que inventar ninguna procedencia.** Cada `### 4.N` de las dos especificaciones ya declaraba en qué fase se escribió, con su enlace. Lo que faltaba era **bajarlo de la sección a la regla**, que es donde el programa lo busca y donde lo lee quien abre por la mitad.

**Ninguna se borró, y esa era la tercera salida del pendiente** — *«alguna seguramente no la pidió nadie»*. Que una regla tenga procedencia no la vuelve necesaria; borrar una vigente quita algo del estándar. Es lo único que queda del 47, y es decisión suya.

### H-26 · Tres de las 42 dudas ya estaban contestadas en el repositorio

De las 42 que detienen 26 fases ([59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md)), **tres tenían su respuesta escrita**:

- **La 16** —qué reglas candidatas no entraron— está en [el análisis del 2026-08-13](../../../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md), con las 22 fichas y su salida. Diecisiete no entraron.
- **La 21** —si la comprobación de marcas cubre todo el repositorio— la contestaba el pendiente 11 desde el 2026-08-10, y **hoy se construyó justamente así**.
- **La 18** no está contestada, pero el pendiente 20 ya trae las dos salidas evaluadas: hay que elegir, no pensarla de cero.

**Quedan 39.**

**Es la segunda vez hoy que una fase espera algo que ya estaba escrito**, y la tercera que la respuesta está en el repositorio y el trabajo era encontrarla. [`01·C23`](../../../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar) se escribió ayer y va acumulando casos más rápido de lo que se aplica.

**Y una que vale la pena decir:** ese mismo análisis tiene una ficha llamada **«menos es más»**, evaluada el 2026-08-13 y marcada *«ya está cubierta»* por `01·C5` y `00·ID7`. Hoy volvió a aparecer, con razón — porque estar cubierta no es lo mismo que cumplirse.

### H-27 · Cuatro dudas más las contesta el programa que ya corre

Siguiendo con las 42 del [59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md): **cuatro no hay que decidirlas, hay que mirarlas.**

- **23** — la corrida completa **no** incluye linter, pruebas ni audit: son subcomandos aparte. Se decidió al construirlo.
- **31 y 33** — dos fases preguntan si esperan a la corrida completa de `EP-004·HU-008`. **No esperan: está construida** y corre desde su fase `A`.
- **38** — un subcomando con dos modos, y `validar.py metareglas --catalogo` ya funciona así.

**De 42 a 35.** Siete contestadas hoy sin que el usuario tuviera que responder ninguna.

**Y dos que parecían contestadas y no lo están:** la 26 y la 27, sobre el pendiente cerrado que nombra su fase. **Solo uno de los 35 archivos de `hecho/` lleva la fila fija**, y ningún programa la comprueba. Ahí la convención no existe todavía — que es distinto de que falte decidirla.

### H-28 · De 42 dudas a 33, sin que el usuario contestara ninguna

Última pasada sobre el [59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). **Dos más las resuelve el propio cuerpo de reglas:**

- **25** — dónde vive el registro de conteos: [`09·G3`](../../../base/09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado) deja fuera lo generado, y un conteo lo es.
- **40** — qué cuenta como publicar: `09·G7` nombra confirmar y publicar como dos actos, y el despliegue es del capítulo `18`, que es opt-in y está apagado.

**De 42 a 33.** Nueve contestadas: tres estaban escritas en el repositorio, cuatro las resuelve el programa que ya corre, y dos, el cuerpo de reglas.

> **Ninguna de las nueve era una decisión pendiente.** Estaban escritas como preguntas porque quien redactó el plan de cada fase no fue a buscar la respuesta — y eso detuvo veintiséis fases durante un día.

**Y hay que decir el límite:** las 33 que quedan sí son decisiones. Buscar más no las va a contestar.

### H-29 · Las 42 dudas, decididas

El usuario pidió resolver las 33 que quedaban, y están escritas en el [59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) con su motivo cada una.

**Casi ninguna hizo falta inventarla.** El grupo A lo resuelve la fila 1 del checklist; el B, una sola regla —**detiene lo que se comprueba sin criterio, avisa lo que necesita juicio**— con toda la evidencia de esta sesión del mismo lado; el resto sale de reglas que ya existen.

**Las tres decisiones que más cambian algo:**

- **La 18** — la historia hace de especificación cuando el entregable no es código, en vez de abrirle una excepción a `F2`. **Una excepción es la puerta que después nadie cierra**, y `08·T1` es el ejemplo vivo.
- **La 36** — la versión se sube al guardar, no al editar. La otra salida —una sola sesión a la vez— ya se incumplió dos veces esta semana, y una regla que la práctica salta no es una regla.
- **La 30** — una clave en una transcripción vieja se enmascara, no se borra el bloque. Borrar pierde lo dicho, que es lo que hoy casi pasó con el pendiente 29.

**Cuatro van con propuesta y no con decisión** —qué proyectos, qué encargo, quién lee—: hacen falta datos que no están en ningún archivo.

**Y el pendiente sigue abierto a propósito.** Decidir no es ejecutar: las 26 fases siguen detenidas hasta que cada una lleve su respuesta a la §2.7 de su plan.

### H-30 · Las 26 fases dejan de estar detenidas

La decisión de cada duda quedó escrita **en la §2.7 del plan de su fase**, no solo en el [59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md): 26 planes y 25 estados al día.

**Estaba en el sitio equivocado y ese era medio problema.** Una decisión que vive en el pendiente obliga a que alguien la vaya a buscar; escrita en el plan de la fase, la lee quien la vaya a ejecutar, que es quien la necesita.

**Ninguna arrancó.** Decidir no es ejecutar, y los estados lo dicen: pasan de «detenida por la duda» a «lista para arrancar».

### H-31 · El registro de cambios estaba escrito para adentro, las 83 entradas

**Qué pasó.** Se le mostró al usuario la entrada de la `15.2.0` para ejecutar el `CA-03` de [EP-002 · HU-002](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/HU-002-registro-de-cambios.md), que exige que se entienda sin haber seguido el trabajo. Respondió **«no entendí nada»**.

**No era una entrada mala: eran todas.** De las 83, **74 citan una ruta de archivo, 43 un identificador de regla, y ninguna tiene menos de tres marcas de jerga.**

**Por qué duró meses.** El criterio estaba escrito desde el principio, pero **solo se puede comprobar con una persona** — y quien escribe la entrada ya sabe de qué habla, así que releerla uno mismo no comprueba nada. **Un criterio que necesita un lector sobrevive sin cumplirse hasta que alguien trae el lector.**

**Dónde queda.** Nace [`20·M17`](../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md) —la entrada abre con qué cambió y por qué, y el detalle va debajo— con su comprobación y diez casos. **Su primer hallazgo fue la entrada escrita unas horas antes**, por quien acababa de medir el problema.

**Las 83 viejas se quedan** (`20·M10`), y queda una pregunta más grande: si el registro estaba escrito para adentro, es probable que otros documentos también.

### H-32 · La clave ya no llega al histórico

Ejecutada la primera de las 26 fases desbloqueadas, y **la que tenía daño vivo**: hasta hoy una clave pegada en el chat quedaba escrita en claro en la transcripción, **que se versiona**. De ahí no se borra.

Nace [`validadores/enmascarar.py`](../../../validadores/enmascarar.py), y el enganche del histórico lo llama **antes** de escribir — no después. Un enmascarado que corre sobre el archivo ya escrito llega tarde: el valor estuvo en disco, y si hubo un guardado en medio quedó en el historial para siempre.

**La mitad del trabajo fue no tapar de más.** El molde —`tu-clave`, `changeme`— se queda, porque taparlo vuelve ilegible un ejemplo; y `password: os.environ["X"]` también, con un motivo más fuerte: **es la forma correcta**, y taparla enseñaría lo contrario de lo que el estándar pide.

**Y se reconoce con lo que `secretos.py` ya sabía.** Una lista nueva serían dos listas que se separan.

**Lo que queda:** las 47 transcripciones ya escritas no se revisaron, y el enmascarado solo cubre el histórico. Un resumen o un plan escritos a mano pueden llevar una clave y nadie los mira.

### H-33 · Decir dónde vive lo que la regla exige, en vez de abrirle otra excepción

Cerrado el [pendiente 20](../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md), v23.10.0. `02·F2` dice ahora que **cuando el entregable no es código, la especificación es la historia con sus criterios de aceptación.**

**Los dos caminos del pendiente parecían equivalentes y no lo son:**

> **Una excepción dice cuándo la regla no rige. Esto dice dónde vive lo que la regla exige.**

Con el camino elegido `F2` sigue exigiendo lo mismo en todos los casos; lo único que cambia es de qué está hecha la especificación.

**Y pesa que `F2` ya tenía una excepción.** Abrirle la segunda a una regla que ya trae una es la puerta que después nadie cierra — `08·T1` es el ejemplo vivo, con su excepción que deja al agente autorizándose a sí mismo a no probar.

**Lo que ordena:** dos fases de este repositorio se habían abierto declarando que no tienen especificación aparte, y hasta hoy era un incumplimiento silencioso.

### H-34 · Al escribir una regla llegan las que se relacionan con ella

**Sale de un defecto de esta misma sesión.** Se escribió una frase en `02·F2` que chocaba con `02·F0` —la regla que `F2` cita en su propio texto— y la fila 17 del checklist, *«no choca con ninguna regla vigente»*, se selló en verde sin mirar.

**El usuario lo reformuló y ahí cambió todo:** no es un problema de cargar contexto, es de **buscar lo que se relaciona**. Con eso, el criterio de aceptación de la historia —*«llega completo el capítulo»*— resultó ser la forma cara de resolverlo.

**Dos razones medidas para cambiarlo:**

- El capítulo `02` pesa **98 KB**, y mandarlo entero **obliga a encontrar la relación uno mismo**, que es exactamente lo que falla.
- **Solo trae a los vecinos del mismo capítulo.** De las cinco reglas que dependen de `02·F2`, **tres viven en otros** — `00·ID3`, `00·ID5` y `13·DOC3`.

**El criterio se devolvió antes de tocar nada.** Por `02·F19` la redacción del CA es la especificación, así que una decisión tomada en un pendiente no podía cambiarla de costado — y eso fue lo que el usuario exigió.

**Y no hizo falta base de datos.** La respuesta estaba en el repositorio: `citas.py` sabe dónde vive cada regla, `metareglas.py` lee las dependencias, y `M15` obliga a que toda cita lleve enlace. **Quién cita a quién ya estaba escrito; faltaba preguntarlo.**

**El límite quedó en un caso de prueba:** una relación que nadie declaró no se encuentra. Eso hace que `M7` y `M15` dejen de ser trámite — son lo que hace la consulta posible.

### H-35 · El 20 se cierra sin escribir nada: `F19` ya lo decía

`02·F2` volvió a su texto original. La frase que le agregué chocaba con `02·F0`, y además **no hacía falta**: [`02·F19`](../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) dice desde la v3.1.0 que *«la redacción del CA es la especificación funcional»*.

**El [pendiente 20](../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md) preguntaba algo contestado en su propio capítulo, dos reglas más abajo.**

**Lo que ordena hacia atrás:** las dos fases que se abrieron declarando que no tienen especificación aparte **no estaban incumpliendo nada**. `F19` ya las cubría; faltaba que alguien lo mirara.

**Y lo que dejó equivocarse:** la fase `A-EP-005-HU-010`. Al tocar `F2` ahora `F0` sale tercera en la lista de relacionadas — el choque que hoy costó cuatro vueltas se ve en la primera.

---

### H-36 · El cruce de dos sesiones se rompe de dos maneras, y solo una deja rastro

**El [pendiente 22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) quedó cerrado** con [`20·M18`](../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md) — *lo compartido se lee un instante antes de escribirlo*. Se simuló con dos copias del repositorio, y el resultado sin la regla no fue el que se esperaba.

| Cómo se resuelve el choque | Qué queda | ¿Se ve? |
|---|---|---|
| Se conservan las dos entradas con el mismo número | número repetido | ✅ sí |
| Se conserva una de las dos | **falta una entrada** | ❌ no |

**El registro tiene la segunda:** dos entradas para la `15.4.0`, del 14 y del 15 de agosto. **La primera no se puede contar**, porque perderse es justamente no dejar rastro — y `validar.py versionado` daba por limpia la corrida en que se perdió una.

**Eso es lo que hace que la regla valga más que su validador:** es lo único que actúa antes del choque. La comprobación llega después y ve la mitad de los casos.

**La `15.4.0` no se renumera.** Un proyecto pudo haberla adoptado, y cambiarle el número ahora le movería el piso sin que se entere. Queda marcada en su propio título, y el validador la reporta como aviso en vez de falla.

### H-37 · Se estaba abriendo un pendiente en medio de cerrarlos, y la decisión ya estaba tomada

**Lo cazó el usuario:** *«porque en la solución de pendientes está creando pendientes?»*.

Al cerrar el 22 aparté sus ampliaciones —el número de un pendiente, los índices compartidos, enterarse de que hay otra sesión viva— a un pendiente 63 nuevo, alegando que construir más de lo que el criterio pide es lo que `02·F20` manda proponer.

**Y estaba mal por dos razones.** La primera: abrir un pendiente mientras se cierran deja la cola donde estaba. La segunda, peor: **el alcance ya lo había decidido el usuario hoy** —*«cualquier archivo único compartido»*, la duda 2 de esa misma fase—. Invocar `F20` era desandar una decisión tomada.

`M18` se escribió en su forma general. Los cuatro casos del pendiente son el mismo defecto en archivos distintos, y acotarla a `VERSION` habría dejado fuera tres roturas que ya ocurrieron. **De paso contesta la pregunta que el pendiente daba por sin decidir:** releyendo al escribir no hace falta enterarse de que hay otra sesión viva.

### H-38 · `cerrar.py` desordenaba el texto de los enlaces que arreglaba

Al mover un pendiente a `hecho/` reescribía el **destino** de cada enlace que lo citaba y dejaba el **texto** diciendo dónde vivía antes — que es lo que `13·DOC14` prohíbe.

**No se veía al cerrar, sino dos cierres después**, cuando la suite lo reportaba lejos de lo que lo causó. Ahora repara las dos partes en el mismo paso, compartiendo el arreglo con el reparador para que no puedan divergir.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ quedan **23** abiertos, cada uno con su historia declarada |
| Toda historia disparada está escrita en su épica | ☑ las seis nuevas, con su fila en la épica y en los dos índices |
| Lo que se hizo está aprobado y guardado | ☐ **falta el commit del 22 y de la 23.11.0**, que se pide aparte |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

**Lo que sigue, cuando se retome:** aprobar y ejecutar la fase `B-EP-004-HU-016`. Sin ella el enrutamiento de hoy es un estado que nada sostiene. Y decidir el [pendiente 60](../../../pendientes/60-nadie-es-dueno-del-texto-del-capitulo-02.md), que es lo único que permite escribir el texto de la regla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
