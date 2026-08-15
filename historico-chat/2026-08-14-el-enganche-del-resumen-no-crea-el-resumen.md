<!-- sesion: d7222a74-bf92-4c55-8afc-784dbe785e43 -->
<!-- nombre: preguntado -->

# 2026-08-14 — El enganche del resumen no crea el resumen

## Conversación

### 1 · Usuario — 2026-08-14 22:47:56
> lo que se hizo acá ya se puede replicar a cualquier proyecto:
> H-4 · No había dónde escribir lo aprendido
>
> ?

**Agente** — 2026-08-14 22:49:58
<!-- agente: 909db2ed-186a-4096-aabe-df2066591d83 -->

No del todo. Lo verifiqué en el instalador:

**Sí viaja:**
- Las reglas (`DOC19` a `DOC22`, `F21`) están en `base/`, que es lo que hereda cualquier proyecto.
- El enganche está registrado en [validadores/instalar.py:200](validadores/instalar.py#L200), así que `instalar.py` lo escribe solo en el `settings.json` del proyecto, apuntando al estándar.

**No arranca solo:**
1. `resumen.py` no hace nada si no existe la carpeta `historico-chat/resumenes/` ([resumen.py:86](validadores/resumen.py#L86)), y **nadie la crea**: el instalador no la pone. En un proyecto nuevo el enganche queda mudo hasta que alguien cree la carpeta a mano. Eso es configuración manual, que según su propia regla es defecto del estándar.
2. El resumen que genera enlaza a `../../../plantillas/sesion.md` ([resumen.py:121](validadores/resumen.py#L121)). En un proyecto heredero esa ruta no existe: el enlace nace roto.

Con esos dos arreglados, sí se replica a cualquier proyecto sin tocar nada.

### 2 · Usuario — 2026-08-14 22:52:19
> osea que al abrir la sesión tampo se está teniendo en cuenta?

**Agente** — 2026-08-14 22:52:40
<!-- agente: 4555684c-b284-415b-8f3d-d31a3e0f7f44 -->

Correcto, y es peor que lo anterior: falla **acá mismo**, no solo en un proyecto heredero.

La cadena: `hook_resumen --modo inicio` busca la transcripción por la marca de sesión ([hook_resumen.py:52](validadores/hook_resumen.py#L52)), pero en `SessionStart` esa transcripción todavía no existe: la crea `hook_historico` en el primer mensaje del usuario. Sin transcripción devuelve vacío y no crea nada ([hook_resumen.py:53-54](validadores/hook_resumen.py#L53-L54)).

Y el modo `aviso` tampoco lo salva: si el resumen no está, se sale ([hook_resumen.py:82](validadores/hook_resumen.py#L82)). O sea, nadie lo crea nunca.

La prueba está en esta sesión: la transcripción es [2026-08-14-sesion-7.md](historico-chat/2026-08-14-sesion-7.md) y en `resumenes/2026-08-14/` no hay archivo suyo.

Son tres huecos, no dos, y este es el que deja el enganche inservible.

Esta sesión la guardo como `2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md`, sobre por qué lo de H-4 todavía no se replica ni funciona acá. ¿Va?

### 3 · Usuario — 2026-08-14 22:57:14
> pero entonces que fué lo que se hizo acá: h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido, osea que no se logró el objetivo?

### 4 · Usuario — 2026-08-14 22:57:30
> o cuál era el objetivo?

**Agente** — 2026-08-14 22:58:09
<!-- agente: 99c68532-9290-4001-931f-e7691cc267ed -->

El objetivo era el hallazgo H-4 de la sesión anterior: que lo aprendido en una sesión tuviera **dónde** quedar escrito, y que quedara ahí **sin que nadie tuviera que acordarse**.

Lo que sí quedó hecho, en tres fases y cinco reglas nuevas (12.2.0 a 15.2.0):

| Se logró | Dónde |
|---|---|
| El sitio: un resumen por sesión, en carpeta por día, enlazado desde el índice | [`13·DOC22`](base/13-documentacion/reglas/DOC22-deja-en-su-propio-documento-lo-que-la-sesion-dejo.md), [plantillas/sesion.md](plantillas/sesion.md) |
| El modelo: qué campos lleva un hallazgo, de dónde viene la sesión, en qué orden se resuelven sus historias | mismo archivo |
| La marca del espacio por llenar, pareja en las 30 plantillas | [`DOC19`](base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) a [`DOC21`](base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) |
| Que lo ya identificado como mal no se repita en lo nuevo | [`02·F21`](base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) |

Lo que **no** se logró es justo la mitad que le daba sentido: que no dependa de la memoria. El enganche existe y está instalado, pero nunca crea nada, por lo que vimos hace un momento. Los dos resúmenes que hay en el repositorio los escribí yo a mano, no el programa.

Y hay algo peor que el defecto: la prueba lo dio por bueno. El caso llamó a la función `crear` con la transcripción ya en la mano ([resultado_pruebas.md:42](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/resultado_pruebas.md#L42)), en vez de disparar el evento real de apertura de sesión. Probó la pieza, no el enganche.

Resumen: el "dónde escribir" está resuelto. El "sin acordarse" está escrito pero no funciona.

### 5 · Usuario — 2026-08-14 22:59:53
> y por qué no se logró esto:
>
> "Lo que no se logró es justo la mitad que le daba sentido: que no dependa de la memoria"
> no era parte de ese H
> ?

**Agente** — 2026-08-14 23:00:31
<!-- agente: debe559f-d9ec-4c2f-adf9-782ade8a529d -->

Sí era parte, y de forma literal: [CA-01 · "El archivo nace solo"](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) dice *"Dado que se abre una sesión... existe el archivo de esa sesión"*. Y el caso [CP-001](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/plan_pruebas.md) también estaba bien escrito: *"Correr el enganche de `SessionStart`"*.

No falló el criterio ni el plan. Falló la ejecución, por tres cosas encadenadas:

1. **No corrí el enganche, corrí la pieza.** El resultado dice *"se pidió crear el resumen de una sesión llamada `maracuya.md`"*: le entregué la transcripción ya hecha a la función. En una sesión real esa transcripción todavía no existe al abrir, porque la escribe otro enganche después. Probé el paso 2 dando por cierto el paso 1.
2. **La precondición del caso escondía el otro hueco.** Dice *"proyecto de prueba con carpeta de resúmenes"*. Se la puse yo a mano, así que nunca apareció que nadie crea esa carpeta.
3. **El criterio transversal convirtió el hueco en característica.** *"Un proyecto sin carpeta de resúmenes no se ve afectado"* quedó marcado como cumplido. Leído así, el enganche mudo en un proyecto nuevo no es defecto: es lo esperado.

En una línea: di por probado el disparador habiéndolo reemplazado por una llamada directa, y las precondiciones que yo mismo escribí me montaron el mundo donde eso funciona.

### 6 · Usuario — 2026-08-14 23:01:39
> no entiendo si hace o no?

**Agente** — 2026-08-14 23:01:45
<!-- agente: ce4c25e1-b332-4c44-8a91-e9cc522d8e3b -->

No hace.

El programa existe, está instalado y corre. Pero no crea el resumen: en esta sesión no lo creó, y en ninguna otra tampoco. Los dos resúmenes que hay en el repositorio los escribí yo a mano.

### 7 · Usuario — 2026-08-14 23:02:27
> en entonces retome esa sesión  en esta

### 8 · Usuario — 2026-08-14 23:06:45
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\historico-chat\2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> como se llama la sesión donde se solucionó es te H: H-4 · No había dónde escribir lo aprendido

**Agente** — 2026-08-14 23:06:52
<!-- agente: 9df5b2de-eb23-47db-9e3b-906112ae7ef5 -->

`2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido`

- Transcripción: [historico-chat/2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](historico-chat/2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md)
- Resumen: [resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md)

El H-4 nació en otra: `2026-08-14-hu-de-la-comprobacion-automatica`, y ahí figura como cerrado en la primera.

### 9 · Usuario — 2026-08-14 23:07:46
> esta es la que tiene que retomar para ver que salió mal :
>
>  historico-chat/2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md

**Agente** — 2026-08-14 23:08:26
<!-- agente: 647d8e0d-754d-4c97-9f76-ce292dd86cc7 -->

Retomada. Esto es lo que salió mal, y está en la propia transcripción:

**1. La prueba nunca disparó el enganche.** En el mensaje 144 usted reclamó que el resultado no decía el paso a paso, y al escribirlo quedó a la vista ([línea 1780](historico-chat/2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md#L1780)):

| # | Qué se ejecutó | Qué salió |
|---|---|---|
| 1 | `crear(raiz, "2026-08-14-maracuya.md")` en un proyecto temporal | Apareció `resumenes/2026-08-14/maracuya.md` |

El caso pedía *"correr el enganche de `SessionStart`"*. Lo que corrí fue la función, con la transcripción ya inventada. Su exigencia destapó la evidencia, yo la escribí, y aun así puse cumple.

**2. La fase entera se ejecutó y se cerró de un golpe.** Mensaje 140, *"hágale"*; trece minutos después, *"H-4 quedó cerrado"*, catorce casos en verde. En medio no hubo una sola sesión real donde mirar si el archivo aparecía.

**3. Lo presenté como mérito.** [Línea 1732](historico-chat/2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md#L1732): *"esta fase fue la única que no necesitó ampliar el plan"*. En las otras dos hubo que ampliarlo porque la realidad contradijo el plan. Acá no contradijo nada porque nunca la consulté.

**4. Es el mismo defecto que usted ya había cazado ese día.** En CP-002 me dijo *"usted no está para aceptar sus propios criterios"*. Cuatro horas después escribí la precondición *"proyecto de prueba con carpeta de resúmenes"* y el criterio transversal *"un proyecto sin carpeta no se ve afectado"*: yo mismo armé el mundo donde el programa funciona, y ahí lo probé.

Lo que sigue, si me lo autoriza: reabrir H-4 en el resumen donde nació y abrir la fase B de EP-005 · HU-008, con la prueba corriendo el evento real y no la función.

### 10 · Usuario — 2026-08-14 23:09:03
> osea las pruebas volvieron a quedar mal?

**Agente** — 2026-08-14 23:09:47
<!-- agente: 35e9c642-d445-4cbf-b9dd-1a778dbede31 -->

Sí, y no es un caso: son seis de nueve.

Todos parten del mismo supuesto falso, que el archivo del resumen ya existe. Como el enganche nunca lo crea, ninguno de esos estados ocurre en la realidad.

| Caso | Qué se probó | Vale |
|---|---|---|
| CP-001, CP-002 | `crear()` con una transcripción inventada, en vez del evento de apertura | No |
| CP-004, CP-005, CP-007 | El aviso sobre un resumen que yo puse a mano. Sin ese archivo el aviso se sale callado ([hook_resumen.py:82](validadores/hook_resumen.py#L82)) | No |
| CP-006 | El propósito leído de ese mismo archivo puesto a mano | No |
| CP-003 | El renombrado, con la orden real | Sí |
| CP-008 | La medición del arranque, sobre este repositorio | Sí |
| CP-009 | Que no estorbe donde no hay carpeta | Sí |

O sea, `CA-01`, `CA-02` y `CA-03` quedaron en cumple sin estar probados. Los tres criterios de la HU.

Lo único que sí quedó verificado es que el programa no estorba y que es rápido.

### 11 · Usuario — 2026-08-14 23:11:35
> es que por eso yo le ponía el ejemplo de la receta de arroz

**Agente** — 2026-08-14 23:11:48
<!-- agente: f2a0f474-646b-4901-813e-8d9a4c151abc -->

Exacto, y ahí estaba la respuesta: usted dijo que el resultado de pruebas es probar el arroz que salió.

Lo que hice fue cocinar un arroz aparte, en mi olla, con mi agua, y probar ese. El de la estufa real nunca lo destapé. Y como el mío salió bien, escribí que la receta funciona.

Peor: la olla también la fabriqué yo. La precondición *"proyecto de prueba con carpeta de resúmenes"* es agua que en la cocina real nadie sirve.

Eso da la regla que falta, y no la tiene [`base/08-pruebas.md`](base/08-pruebas.md): la prueba dispara el evento real por donde el usuario lo va a disparar, no llama por dentro a la pieza. Si el caso dice "al abrir la sesión", se abre una sesión.

¿La escribo como regla nueva del capítulo 08, y con ella reabro H-4 y la fase B de HU-008?

### 12 · Usuario — 2026-08-14 23:12:38
> qué regla a escribir?

**Agente** — 2026-08-14 23:13:18
<!-- agente: ad4d6ba7-7086-456e-aeb5-fa184c73d80a -->

Esta, en el capítulo [`08 · pruebas`](base/08-pruebas.md), que hoy no la tiene. El vecino más cercano es `T2` ("prueba el comportamiento, no la implementación"), y habla de qué se verifica, no de por dónde se entra:

> ## T8 · Dispara la prueba por el mismo camino de la realidad
>
> El caso se ejecuta por la entrada real que lo dispara (el evento, el comando, la petición), nunca llamando por dentro a la función que esa entrada invoca. Llamar la pieza prueba la pieza: el camino queda sin probar, y ahí es donde falla.
>
> ```
> INCORRECTO: el caso dice "al abrir la sesión" y la prueba llama crear(raiz, "2026-08-14-tema.md")
> CORRECTO:   el caso dice "al abrir la sesión" y la prueba corre el enganche de SessionStart
> ```

Hay una segunda, hermana pero distinta, y por eso no la meto en la misma (el checklist reprueba el "y además"):

> ## T9 · El estado inicial del caso lo arma el sistema, no el que prueba
>
> Las precondiciones se producen corriendo el flujo que las produce. Una precondición puesta a mano puede describir un estado que el sistema nunca alcanza, y entonces la prueba pasa sobre un mundo que no existe.

La segunda es la que habría cazado el otro hueco: la carpeta `resumenes/` que yo creé a mano y que en un proyecto nuevo nadie crea.

Ninguna de las dos arregla el enganche. Eso es la fase B de HU-008.

¿Escribo las dos, o solo la `T8`?

### 13 · Usuario — 2026-08-14 23:14:42
> no necesito es solución a lo que quedó mal

### 14 · Usuario — 2026-08-14 23:16:35
> no haga pruebas con supuestos por es que le pedí el paso a paso de lo que hizo

**Agente** — 2026-08-14 23:21:14
<!-- agente: f4e9c6c7-3c82-4f28-87b1-91e555d9b8d5 -->

Entendido: la prueba corre lo real, y el resultado dice paso a paso lo que se ejecutó y lo que salió. Nada de precondiciones que yo mismo monte.

Voy con eso puesto. Primero el resumen de esta sesión, que es lo que la sesión anterior demostró que se pierde si se deja para después.

Fase abierta, detenida esperando su aprobación: [B-A-EP-005-HU-008-el-enganche-crea-el-resumen](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-A-EP-005-HU-008-el-enganche-crea-el-resumen/README.md).

**La solución, en cuatro cambios** ([plan de trabajo](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-A-EP-005-HU-008-el-enganche-crea-el-resumen/plan_trabajo.md), 10 tareas, 10 h):

1. El archivo se asegura en los dos modos, no solo al abrir. Al abrir la transcripción no existe; en el primer mensaje del usuario sí.
2. El instalador deja puesta la carpeta `historico-chat/resumenes/`, como ya deja el histórico y la memoria.
3. El encabezado deja de enlazar `plantillas/`, que no viaja al proyecto.
4. Se anula en la fase A el veredicto de los seis casos que no probaron lo que decían.

**El [plan de pruebas](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-A-EP-005-HU-008-el-enganche-crea-el-resumen/plan_pruebas.md)** arranca con tres condiciones que un caso tiene que cumplir para valer, aunque pase:

- Se corre el enganche como orden del sistema, con el mismo JSON que le manda Claude Code.
- El proyecto de prueba se arma corriendo el instalador, y la transcripción la escribe el otro enganche. El que prueba no crea nada del flujo.
- El resultado escribe la orden literal y su salida, paso a paso.

Y hay un caso que no se puede automatizar: mañana, en este repositorio, el archivo tiene que aparecer solo. Eso queda como criterio de salida.

Antes de eso dejé el rastro: H-4 reabierto en [el resumen donde nació](historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md), y [el resumen de esta sesión](historico-chat/resumenes/2026-08-14/el-enganche-del-resumen-no-crea-el-resumen.md) con sus tres hallazgos.

¿Apruebo y ejecuto?

### 15 · Usuario — 2026-08-14 23:24:59
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\historico-chat\resumenes\2026-08-14\h-8-la-traduccion-quedo-a-medias.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> si

### 16 · Usuario — 2026-08-14 23:30:49
> no me interesa que cree una nueva fase se tiene que reabrir la fase que se cerró

### 17 · Usuario — 2026-08-14 23:37:23
> hagamos un ejemplo con lo que dice CP-001 y CA-01 que es lo ese debe validar en resusultado_pruebas. Agréguelos ahi textual en: Detalle de CP-001

### 18 · Usuario — 2026-08-14 23:40:22
> no agregue cosas que van en: CP-001 no está todo eso que agregó

**Agente** — 2026-08-14 23:41:59
<!-- agente: fbdc96cc-a711-4b22-aa4c-5a2d9dbee363 -->

Ajustado. En **Detalle de CP-001** quedan solo tres cosas: `CA-01` textual, `CP-001` textual como está en el plan, y lo que se ejecutó al lado. El veredicto es una línea.

Lo demás que había escrito ahí era análisis mío, y no es de ese caso.

**Estado de lo ejecutado**, con la fase A reabierta y sin fase B:

| Qué | Dónde |
|---|---|
| El archivo nace en el primer mensaje, no al abrir | [hook_resumen.py](validadores/hook_resumen.py) |
| El instalador deja `historico-chat/resumenes/` | [instalar.py](validadores/instalar.py) |
| El encabezado ya no enlaza `plantillas/` | [resumen.py](validadores/resumen.py) |
| Corrida 2: 10 casos que disparan el enganche como orden del sistema | [pruebas.py](validadores/pruebas.py) |
| La fase vuelve a la estación 8, con su ampliación y los tres defectos nuevos | [la fase A](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md) |

Pruebas: los 10 casos nuevos en verde, y la corrida a mano paso por paso quedó escrita. La suite completa, 236 casos con una falla que no es de acá: viene de `base/09-git.md` y `base/glosario.md`, que los está escribiendo otra sesión. `validar.py estandar` en 0 fallas.

**La fase no la doy por cumplida.** Falta CP-018: que en una sesión nueva de este repositorio el archivo aparezca solo. Eso se ve mañana al abrir, no lo puedo simular. Y falta el commit, que usted autoriza aparte.

### 19 · Usuario — 2026-08-14 23:43:27
> agregue también: Cómo validarlo

**Agente** — 2026-08-14 23:43:43
<!-- agente: 9aa6df6c-bd87-4d23-9125-f947b67c9c58 -->

Agregado, textual como está en la HU.

El bloque de **Detalle de CP-001** queda ahora con cuatro partes:

1. `CA-01`, el escenario en gherkin.
2. Su **cómo validarlo**, los tres pasos y el "aprobado cuando".
3. `CP-001` del plan de pruebas, con precondiciones y pasos.
4. Lo que se ejecutó de verdad, al lado, y el veredicto en una línea.

Leído así se ve solo el desvío: el paso 1 pedía abrir una sesión, y lo que se corrió fue la función.

### 20 · Usuario — 2026-08-14 23:46:34
> según:  CA-01 y CP-001 cuál es el problema que resuelve

**Agente** — 2026-08-14 23:46:42
<!-- agente: 8b7aa44e-845f-493c-90be-32abe2fdf693 -->

El problema es que **lo que se deja para el final no se escribe**.

- **CA-01** lo dice en su "aprobado cuando": *"el hueco se ve, en vez de no existir"*. Mientras el archivo no exista, escribir el resumen depende de que alguien se acuerde, y un chat no tiene cierre donde acordarse.
- **CP-001** lo aterriza en tres comprobaciones: que el archivo esté al abrir, que esté **vacío** con el modelo puesto (el hueco a la vista, no un texto que parezca trabajo hecho), y que al correr otra vez no pise lo ya escrito.

Es la misma lección de la transcripción: se escribió siempre solo desde que la escribe un programa.

### 21 · Usuario — 2026-08-14 23:47:10
> eso no fue lo que le pedí

**Agente** — 2026-08-14 23:47:18
<!-- agente: bdc8128e-a61c-4779-8994-21098fdf31a5 -->

No. Dígame cuál de las dos:

1. Que escriba en el **Detalle de CP-001** cuál es el problema que ese criterio y ese caso resuelven, para que el documento lo diga.
2. Otra cosa, y le erré a las dos.

### 22 · Usuario — 2026-08-14 23:48:04
> cual es el problema que pretenden resolver?

**Agente** — 2026-08-14 23:48:22
<!-- agente: 2de73ea7-5648-4544-9071-9dbffc534e56 -->

Está escrito en la HU, y es lo que CA-01 y CP-001 vienen a cubrir.

**[HU-008 §2](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md), textual:**

> - **Como** quien retoma el trabajo días después
> - **Quiero** que el resumen de la sesión exista aunque nadie se acuerde de escribirlo
> - **Para** no depender de la memoria del agente para saber qué quedó

**§3, el problema:**

> El modelo del resumen y su carpeta ya existen. Llenarlos depende de que el agente se acuerde, y esa es exactamente la forma en que se pierde: un chat no tiene final, así que lo que se deja para el cierre no se escribe.

De ahí sale `RN-01`: *"el archivo del resumen se crea solo al abrir la sesión, con el modelo puesto"*. `CA-01` es esa regla convertida en criterio, y `CP-001` es cómo se comprueba.

### 23 · Usuario — 2026-08-14 23:49:34
> no lo que hace la hu sino lo que 
>
> CA-01 y CP-001 pretenden resolver la pareja resulven una parte de la HU

**Agente** — 2026-08-14 23:49:43
<!-- agente: 939e609c-0ebf-4349-82d7-1d58168cd69d -->

La pareja cubre **una sola** de las tres partes de la HU: que el archivo exista.

| Parte de la HU | Quién la cubre |
|---|---|
| Que el hueco exista, con el modelo puesto y vacío | **CA-01 · CP-001** |
| Que avise qué le falta mientras se trabaja | CA-02 · CP-004 |
| Que muestre lo abierto del propósito | CA-03 · CP-006 |

O sea: `CA-01` y `CP-001` no resuelven que el resumen se llene ni que alguien se entere de que está vacío. Solo que **nunca falte el archivo** donde escribir, y que al nacer no traiga nada escrito que parezca trabajo hecho.

Llenarlo sigue siendo criterio, y eso la HU lo deja fuera de alcance.

### 24 · Usuario — 2026-08-14 23:50:11
> le estoy preguntando solo por esto: CA-01 · CP-001 no estoy siendo claro?

**Agente** — 2026-08-14 23:50:15
<!-- agente: 58466a40-abc0-4e2f-8510-8d12092cab5c -->

Que el archivo del resumen nunca falte: nace solo, vacío y con el modelo puesto.

### 25 · Usuario — 2026-08-14 23:51:32
> listo si eso es lo que resulven esas dos cuál es el paso a paso de la prueba para que se cumpla y cual es el paso a paso para que no se cumpla

**Agente** — 2026-08-14 23:51:50
<!-- agente: a0152ae0-3129-4fb3-ad10-f93ff24a0b6d -->

**Para que cumpla** — cada paso es una orden, y lo que sale se mira en el disco:

| # | Qué se ejecuta | Qué tiene que salir |
|---|---|---|
| 1 | `git init` y `instalar.py <proyecto> --aplicar` | Existe `historico-chat/resumenes/` |
| 2 | `hook_resumen.py --modo inicio`, con `{"session_id":"s1","cwd":"<proyecto>"}` | Sale con 0 |
| 3 | `hook_historico.py --modo usuario`, mismo `session_id` | Aparece la transcripción del día |
| 4 | `hook_resumen.py --modo aviso`, mismo `session_id` | Aparece `resumenes/<hoy>/<mismo nombre>.md` |
| 5 | Abrir ese archivo | Trae el modelo y **ningún** hallazgo |
| 6 | Repetir el paso 4 sobre un resumen con un hallazgo escrito | No lo pisa, y el índice del día no gana otra línea |

**Para que no cumpla** — cualquiera de estas tres, y basta una:

| # | Qué se ejecuta | Con qué sale reprobado |
|---|---|---|
| 1 | Los pasos 1 a 4 completos | Después del paso 4 no hay archivo en la carpeta del día |
| 2 | Los pasos 1 a 4 completos | El archivo aparece **con un hallazgo adentro** que nadie escribió |
| 3 | El paso 4 sobre un resumen que ya tiene un hallazgo | El texto se pisa, o el índice queda con la línea dos veces |

El paso 1 de esa segunda tabla es exactamente lo que pasaba antes: la cadena llegaba hasta el final y el archivo no existía.

¿Los escribo así, las dos tablas, en el Detalle de CP-001?

### 26 · Usuario — 2026-08-14 23:53:16
> pero explique en plabras sencillas cada paso no con código

**Agente** — 2026-08-14 23:53:25
<!-- agente: c1f0b5d3-367f-4a59-a5e1-56e3edf8f0d5 -->

**Para que cumpla:**

| # | Qué se hace | Qué tiene que pasar |
|---|---|---|
| 1 | Se instala el estándar en una carpeta nueva y vacía | Queda creada la carpeta donde viven los resúmenes |
| 2 | Se abre una sesión | No pasa nada todavía, y nada se rompe |
| 3 | Se escribe el primer mensaje | Aparece el archivo donde se copia la conversación |
| 4 | Se mira la carpeta de los resúmenes | Ahí está el archivo de esa sesión, con el mismo nombre |
| 5 | Se abre ese archivo | Trae el formulario en blanco: los espacios por llenar y ningún hallazgo escrito |
| 6 | Se escribe algo adentro y se sigue trabajando | Lo escrito sigue ahí, y en la lista del día la sesión aparece una sola vez |

**Para que no cumpla**, basta con una de estas tres:

| # | Qué se hace | Con qué queda reprobado |
|---|---|---|
| 1 | Se abre la sesión y se escribe el primer mensaje | En la carpeta de los resúmenes no hay ningún archivo |
| 2 | Se abre el archivo recién creado | Trae un hallazgo escrito que nadie escribió |
| 3 | Se escribe algo adentro y se sigue trabajando | Lo escrito se borró, o la sesión quedó dos veces en la lista del día |

La primera de la segunda tabla es lo que venía pasando: se hacía todo y el archivo no aparecía nunca.

### 27 · Usuario — 2026-08-14 23:54:04
> agregue eso a qué se ejecutó

**Agente** — 2026-08-14 23:54:36
<!-- agente: 2fe4adaf-e41d-4d7c-b406-e1e10aff5c18 -->

Agregado en **Detalle de CP-001**, en palabras y sin código. El bloque quedó así:

1. `CA-01` y su "cómo validarlo", textuales.
2. `CP-001` del plan, textual.
3. **Qué había que ver para darlo por cumplido** — los seis pasos.
4. **Y para darlo por reprobado** — las tres formas, con una basta.
5. **Qué se ejecutó de verdad** — los tres pasos que sí se corrieron.
6. El veredicto: anulado, porque nunca se abrió una sesión.

Leído seguido, la tabla de reprobados y lo que se ejecutó dicen lo mismo: el paso 1 nunca se hizo.

### 28 · Usuario — 2026-08-14 23:57:13
> si ve como es que se hace? es contar todo lo que se hizo para llegar a la verdad

**Agente** — 2026-08-14 23:57:26
<!-- agente: 845c69a9-1a33-4257-ac6b-614747e5d82f -->

Sí. Y lo que lo destapó fue escribirlo: mientras el detalle decía "se creó el resumen y apareció", la trampa no se veía. Contando el paso 1 tal como fue —que no se abrió ninguna sesión— el caso se cae solo.

Dos cosas quedan para que esto no dependa de que yo me acuerde:

1. Los otros ocho casos de esta fase siguen con el detalle a medias: dicen qué salió, no qué había que ver ni con qué habrían reprobado.
2. La plantilla [planes/resultados.md](plantillas/planes/resultados.md) hoy pide el paso a paso, pero no pide las otras tres: el criterio y el caso textuales, la tabla de cuándo reprueba, y que esté en palabras.

¿Voy por las dos, o primero por la plantilla?

### 29 · Usuario — 2026-08-14 23:58:03
> según lo que hicimos faltan pasos?

**Agente** — 2026-08-14 23:58:14
<!-- agente: e4a951c3-309f-48de-b7ea-dada1abde326 -->

Sí, falta uno. `CA-01` pide en su "cómo validarlo" un tercer paso que en mi tabla no está:

> 3. Abrir una segunda sesión el mismo día. Resultado esperado: aparece su propio archivo, sin pisar el anterior.

Mi tabla salta de "se abre el archivo" a "se escribe algo adentro", y nunca abre la segunda sesión.

Y al revés: mi paso 1, instalar el estándar, no es un paso de `CP-001`. Sale de su precondición, así que ahí está de más como paso.

¿Los corrijo? Quedaría con la segunda sesión adentro y con la instalación puesta como precondición, no como paso.

### 30 · Usuario — 2026-08-14 23:58:46
> corrija

**Agente** — 2026-08-14 23:59:07
<!-- agente: 36db51b1-f4a7-49d6-839f-8d0256f3ac3e -->

Corregido. Ahora la instalación va como precondición, no como paso, y entró la segunda sesión del mismo día que pedía `CA-01`.

- Cumple: 4 pasos.
- Reprueba: 4 formas, con una basta.

Los dos quedan uno a uno: cada paso de la primera tabla tiene su forma de fallar en la segunda.

### 31 · Usuario — 2026-08-14 23:59:43
> escriba el paso a paso en infinitivo

**Agente** — 2026-08-15 00:00:00
<!-- agente: 5014c486-c0ab-4404-849b-e54f05fce2e9 -->

Listo. Las dos tablas quedan en infinitivo: *abrir*, *escribir*, *seguir*. La columna se llama ahora **Qué hacer**.

La tercera tabla, la de lo que se ejecutó, la dejé en pasado a propósito: esa no dice qué hacer, dice qué pasó.

### 32 · Usuario — 2026-08-15 00:04:31
> ya entedió lo que quiero?

**Agente** — 2026-08-15 00:04:40
<!-- agente: 51102d88-b4d3-4d3d-b0cf-18ddda7d3fed -->

Sí. Que el resultado de pruebas se pueda juzgar sin creerme nada:

1. **El criterio y el caso, textuales**, para no tener que ir a buscarlos ni fiarse de mi resumen.
2. **Qué hacer para que cumpla**, paso a paso, en infinitivo y en palabras que entienda cualquiera.
3. **Qué hacer para que reprube**, uno a uno con lo anterior. Si no se puede decir cómo falla, no se puede decir que pasa.
4. **Qué se ejecutó de verdad.** Si no coincide con el punto 2, no cumple, aunque el programa haya salido bien.

Y que eso no se quede en este caso: va en los otros ocho y en la plantilla, o vuelve a pasar.

### 33 · Usuario — 2026-08-15 00:08:55
> lo que necesito que diga es lo siguiente: el problema que resuelven CA-01 y CP-001 es: Que el archivo del resumen nunca falte: nace solo, vacío y con el modelo puesto.
> y los pasos que se siguieron para comprobar esas solución son los siguientes:
> enumerar pasos. soy claro?

**Agente** — 2026-08-15 00:09:30
<!-- agente: 9bf594af-103d-4671-b279-d1c7fa3023ab -->

Claro. Queda con esa frase al principio y los pasos numerados debajo.

Hecho. **Detalle de CP-001** abre ahora con la frase:

> El problema que resuelven CA-01 y CP-001 es: que el archivo del resumen nunca falte. Nace solo, vacío y con el modelo puesto.

Y los pasos seguidos quedan numerados, cada uno con lo que salió. Agregué un cuarto que faltaba decir: la segunda sesión del mismo día no se abrió, se dejó para otro caso.

Debajo sigue el veredicto: anulado, porque el paso 1 nunca abrió una sesión.

### 34 · Usuario — 2026-08-15 00:10:46
> ya puede quitar la literalidad de:CA-01 y CP-001 era solo para realizar el ejercicio

**Agente** — 2026-08-15 00:11:43
<!-- agente: 78920ecb-d09c-43b6-ac9a-e5d6fe8d866d -->

Quitada la literalidad. El bloque quedó en cinco partes, con `CA-01` y `CP-001` solo enlazados:

1. El problema que resuelven.
2. La precondición.
3. Qué hacer para que cumpla.
4. Qué hacer para que reprube.
5. Los pasos que se siguieron, y el veredicto.

Falta llevarlo a los otros ocho casos de esta fase y a la plantilla, para que no dependa de que yo lo repita. ¿Sigo por ahí?

### 35 · Usuario — 2026-08-15 00:12:03
> pero la precondición no es un paso?

**Agente** — 2026-08-15 00:12:13
<!-- agente: b9656d08-4d30-4163-aa4c-db4e3a17286d -->

Sí, cuando hay que hacer algo para llegar a ella. Y acá hay que hacerlo: instalar el estándar en la carpeta.

Precondición es lo que ya es cierto sin hacer nada. Si alguien tiene que ejecutar algo, es un paso, y dejarlo fuera de la lista es justo donde se escondió la trampa: la precondición decía *"proyecto de prueba con carpeta de resúmenes"* y esa carpeta la puse yo a mano, sin que quedara escrito que alguien la había puesto.

Lo paso a ser el paso 1 y corro la numeración. ¿Va?

### 36 · Usuario — 2026-08-15 00:12:45
> de cual estándard habla?

**Agente** — 2026-08-15 00:12:51
<!-- agente: 62bfa05b-fce9-42c6-a103-83fd484ce4fc -->

De este repositorio: el agente. Lo que se instala es `base/`, los enganches y la configuración, y lo hace [validadores/instalar.py](validadores/instalar.py) sobre una carpeta cualquiera.

En el documento la palabra queda vaga, tiene razón. Lo escribo así en el paso 1: *"instalar el agente en una carpeta nueva y vacía, con `validadores/instalar.py`"*.

### 37 · Usuario — 2026-08-15 00:13:30
> cómo se llama el agente?

**Agente** — 2026-08-15 00:13:42
<!-- agente: d47a8f8c-bb0b-445d-a77d-42da641fc9d9 -->

**Cimiento.** Usted le puso ese nombre ayer, y está en la memoria: [terminologia-agente-vs-estandar.md](historico-chat/memory/terminologia-agente-vs-estandar.md).

Entonces el paso 1 queda: *"instalar Cimiento en una carpeta nueva y vacía"*.

### 38 · Usuario — 2026-08-15 00:14:56
> A parte de la terminología debe estar en el brief del proyecto o en dónde?

**Agente** — 2026-08-15 00:15:38
<!-- agente: f849c814-8a14-4e7c-a3ed-563af6c2ec5c -->

En el [brief.md](brief.md), que hoy se titula *"Brief del agente"* y nunca dice cómo se llama. Ahí es donde se declara qué es el producto, así que el nombre es de ese documento.

Y en un sitio más, porque la palabra viaja: [`base/00-identidad-y-rol`](base/00-identidad-y-rol/base.md) es el capítulo que dice **quién** trabaja, y es lo que cada proyecto hereda. Si el nombre no está ahí, en un proyecto instalado nadie sabe cómo se llama lo que tiene corriendo.

La memoria no es el sitio: sirve para que yo lo trate así en esta sesión, no para que el proyecto lo sepa. Hoy el nombre solo vive ahí, y por eso no aparece en ningún documento.

Hay un tercero que no toco: el glosario, que lo está escribiendo otra sesión ahora mismo.

Son dos cambios de una línea. ¿Los hago?

### 39 · Usuario — 2026-08-15 00:33:33
> sigamos con esto:
> El problema que resuelven.
> La precondición.
> Qué hacer para que cumpla.
> Qué hacer para que reprube.
> Los pasos que se siguieron, y el veredicto.

### 40 · Usuario — 2026-08-15 06:35:47
> siga

**Agente** — 2026-08-15 06:38:11
<!-- agente: 5af21958-219f-4fd1-a233-d5eb0ea234e8 -->

Al día. Lo que quedó en esta pasada:

| Qué | Dónde |
|---|---|
| Los ocho casos de la corrida 2, con las cinco partes | [resultado_pruebas.md](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/resultado_pruebas.md) |
| Los cinco casos anulados de la corrida 1, cada uno diciendo cuál lo reemplaza | mismo archivo |
| Las cinco partes exigidas en el molde, para que se replique | [plantillas/planes/resultados.md](plantillas/planes/resultados.md) |
| Los tres hallazgos de la sesión, con su decisión y dónde quedó | [el resumen](historico-chat/resumenes/2026-08-14/el-enganche-del-resumen-no-crea-el-resumen.md) |
| Versión **15.4.0** con su entrada | [CHANGELOG.md](CHANGELOG.md) |

En el molde quedó escrito lo que faltaba decir: **si lo que se ejecutó no son los pasos de "para que cumpla", el caso no cumple, aunque haya salido bien.**

Pruebas: 236 casos con una falla que no es de acá, la de las citas de `base/09-git.md` y `base/glosario.md`, que los está escribiendo otra sesión. `validar.py estandar` en 0 fallas. Enlaces del resultado y del resumen, sin roturas.

Falta el commit, que usted autoriza aparte. Y quedan dos cosas menores sin hacer: los tres casos de la corrida 1 que siguen en pie (`CP-003`, `CP-008`, `CP-009`) todavía tienen el detalle viejo, y el nombre Cimiento sigue sin estar en el [brief](brief.md).

### 41 · Usuario — 2026-08-15 06:41:30
> entonces en dónde quedamos?

**Agente** — 2026-08-15 06:41:39
<!-- agente: 5233fbcd-1485-4275-bfa1-3f7c69b16c59 -->

El propósito era arreglar lo que la sesión de H-4 dejó mal: el enganche no creaba el resumen.

**Hecho y probado:**

| Qué | Estado |
|---|---|
| El archivo nace en el primer mensaje, no al abrir | Corregido |
| El instalador deja la carpeta de resúmenes en cualquier proyecto | Corregido |
| El encabezado ya no enlaza a algo que no viaja | Corregido |
| Las pruebas disparan el enganche, no llaman la función | 10 casos nuevos, en verde |
| La fase A reabierta, con su ampliación, su corrida 2 y sus tres defectos | Escrito |
| El molde exige las cinco partes en cada caso | Escrito |

**Falta, en orden:**

1. **El commit.** Nada de esto está guardado.
2. **La única prueba que no puedo simular:** que al abrir la próxima sesión el archivo aparezca solo. Hasta eso, la fase no cierra y H-1 sigue abierto.
3. Dos cosas menores: tres casos viejos con el detalle a la antigua, y el nombre Cimiento fuera del brief.

¿Hago el commit?

### 42 · Usuario — 2026-08-15 06:42:37
> si haga el commit
