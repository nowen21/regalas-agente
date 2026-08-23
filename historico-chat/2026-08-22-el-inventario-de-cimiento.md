<!-- sesion: d350bf4a-be4f-4d22-828e-5b1d54ae3e94 -->
<!-- nombre: preguntado -->

# 2026-08-22 — El inventario de cimiento

## Conversación

### 1 · Usuario — 2026-08-22 15:14:46
> después del planteamiento qué sigue?

**Agente** — 2026-08-22 15:15:36
<!-- agente: 83cb5648-2255-41fd-a063-9d3372a84339 -->

Después del **planteamiento** (`prompts/<slug>-planteamiento.md`) no sigue la épica: sigue la **puerta**.

**1 · Inventario de funcionalidades** — [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)

Se escribe desde [`plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md): cada ítem con su estado, y lo que no esté decidido marcado «por confirmar». **El usuario lo aprueba o corrige el alcance ahí.** Sin ese OK no se deriva ninguna épica — esa regla nació justo porque en `shopnest-mesa` el alcance se asumió en el planteamiento y la corrección llegó con 3 épicas y 21 historias ya escritas encima.

**2 · Épicas** — [`13·DOC16`](base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md), citando qué ítems del inventario cubre cada una. La que no baje de ningún ítem no arranca.

**3 · Historias de usuario** — [`13·DOC15`](base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), la épica descompuesta con sus criterios de aceptación.

**4 · Fase** — recién acá se ejecuta: especificación ([`02·F2`](base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)) → línea base verificada → `plan_trabajo` + `plan_pruebas` → **pausa y aprobación explícita** → código → pruebas → cierre → commit ([`02·F15`](base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)).

La cadena completa la manda [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) y ningún eslabón se salta por chico que sea el trabajo. El mapa macro con las once etapas está en [base/02-flujo-de-trabajo/base.md](base/02-flujo-de-trabajo/base.md), y las plantillas van numeradas en ese mismo orden (`01-planteamiento` → `02-inventario` → `03-epica` → `04-HU` → `05-fase`).

Si me dices de qué planteamiento hablas, te armo el inventario desde la plantilla para que lo apruebes.

### 2 · Usuario — 2026-08-22 15:24:48
> listo empecemosa llenar ese inventario

**Agente** — 2026-08-22 15:26:14
<!-- agente: b8d08e27-ad99-4718-ab46-b93b39c7f9ec -->

El inventario de **Cimiento** ya existe y está en **EN REVISIÓN DEL USUARIO**: [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md), acompañando a [prompts/cimiento-planteamiento.md](prompts/cimiento-planteamiento.md). Empiezo por ahí — si te referías a otro proyecto, corrígeme y lo armo desde cero.

Cómo está hoy:

| Grupo | Existe | Parcial | Por construir | Por confirmar |
|---|:--:|:--:|:--:|:--:|
| 1 · Cuerpo de reglas | 5 | 0 | 0 | 1 |
| 2 · Ciclo de vida y entregables | 3 | 0 | 2 | 0 |
| 3 · Comprobación automática | 4 | 0 | 1 | 0 |
| 4 · Memoria entre sesiones | 5 | 0 | 0 | 0 |
| 5 · Instalación y administración | 5 | 0 | 1 | 0 |
| **Total** | **22** | **0** | **4** | **1** |

Lo que falta para que pase de «en revisión» a **APROBADO** son tres preguntas. Son las que abren la puerta de las épicas ([`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)), así que van primero. Te las hago en el chat, no en formulario ([`01·C13`](base/01-conducta.md#c13--preguntas-de-análisis-van-en-chat-abierto-no-en-formulario-cerrado)):

**P-1 · Los capítulos opt-in de RPA y de IA (`21`, `22` ya existen; hablo de los pendientes 08 y 12): ¿se escriben ahora, o cuando aparezca un proyecto que los estrene?**
Mi propuesta es esperar al proyecto. Un capítulo escrito sin caso real se llena de lo que uno se imagina, y después toca desarmarlo — es exactamente lo que pasó con `18` y `19`, que hoy están sin ejemplos.

**P-2 · ¿Entra en el horizonte un segundo agente real que use el estándar?**
El contrato del adaptador ya lo prevé, o sea que el costo está medido y no se pierde nada por dejarlo dormido. Mi propuesta: no por ahora.

**P-3 · ¿La interfaz debe volverse tablero de todos los proyectos — cumplimiento de un vistazo y alertas — o se queda en registro?**
Es la evolución natural del ítem 5.6 («la interfaz mide todos los proyectos de una vez»). Mi propuesta: sí, pero después de 5.6, no en vez de.

Y una cuarta, que es tuya y no está escrita como pregunta: **¿falta alguna funcionalidad en las 27 filas?** El inventario lo escribí yo con lo que el proyecto tiene construido; si algo que quieres de Cimiento no aparece ahí, ahora es cuando entra — después ya no baja a épica.

Contéstame las que tengas claras y voy marcando el documento; las que queden abiertas bloquean solo sus ítems, no el resto.

---

Aparte, dos cosas de higiene de la sesión:

Esta sesión la guardo como `2026-08-22-el-inventario-de-cimiento.md` — de qué se trató: se aprueba el inventario de funcionalidades de Cimiento para abrir la puerta de las épicas. ¿Va? Si sí, corro el renombrado y tú pegas `/rename el-inventario-de-cimiento`.

### 3 · Usuario — 2026-08-22 15:26:41
> si

**Agente** — 2026-08-22 15:27:10
<!-- agente: dbf86f18-408b-4222-a57b-f2e1439da4e0 -->

Renombrada: [historico-chat/2026-08-22-el-inventario-de-cimiento.md](historico-chat/2026-08-22-el-inventario-de-cimiento.md), con su línea del índice corregida. Pégame esta línea para que la pestaña y `/resume` digan lo mismo — es comando tuyo, yo no puedo escribirlo:

```
/rename el-inventario-de-cimiento
```

Ahora, lo otro: ese «si» lo tomo **solo** para el renombrado. No lo cuento como aprobación del alcance, porque asumir un alcance con un sí corto es justo el error que [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) existe para evitar — en `shopnest-mesa` costó 3 épicas y 21 historias escritas encima de un alcance supuesto.

Si tu intención era decir «sí a las tres propuestas», dímelo con esa palabra y marco el inventario así:

- **P-1** → los capítulos de RPA y de IA esperan a que haya proyecto que los estrene. El ítem 1.6 pasa de «Por confirmar» a **Por construir (aplazado)**.
- **P-2** → no entra un segundo agente por ahora. El ítem 6.2 queda **descartado por ahora**, con el contrato del adaptador intacto.
- **P-3** → la interfaz sí será tablero, **después** de 5.6. El ítem 6.3 pasa a **Por construir**, dependiente de 5.6.

Y sigue viva la cuarta, que es la que no puedo contestar yo: **¿falta alguna funcionalidad en las 27 filas?** Si no falta ninguna, con eso el inventario queda **APROBADO** y ya se pueden derivar las historias de los cuatro ítems «por construir» (2.4, 2.5, 3.5, 5.6) a sus épicas.

### 4 · Usuario — 2026-08-22 15:27:30
> suba todo

### 5 · Usuario — 2026-08-22 15:28:36
> en qué quedamos al establecer el inventario?

**Agente** — 2026-08-22 15:28:53
<!-- agente: 5412b6da-8722-4fe2-8f87-d730d5d14dce -->

Nada quedó escrito todavía. El inventario sigue exactamente como estaba: [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md), **EN REVISIÓN DEL USUARIO**, con las tres preguntas sin contestar.

Lo único que se hizo en la sesión fue el renombrado del histórico. Tu «si» lo tomé solo para eso, y sobre «suba todo» arranqué a preparar un commit — ahí me detuviste.

Donde quedamos, en concreto:

| Pregunta | Estado | Mi propuesta, sin aplicar |
|---|---|---|
| **P-1** · capítulos RPA e IA | sin contestar | esperar a que haya proyecto que los estrene (ítem 1.6 → Por construir, aplazado) |
| **P-2** · segundo agente | sin contestar | no por ahora (ítem 6.2 → descartado por ahora) |
| **P-3** · interfaz como tablero | sin contestar | sí, después de 5.6 (ítem 6.3 → Por construir) |
| **¿Falta alguna funcionalidad?** | sin contestar | no la puedo contestar yo |

Y una duda que me frena: **«suba todo» — ¿te referías a subir el repo a git, o a aplicar las tres decisiones al inventario?** Lo leí como git y por eso fui a mirar el estado del repositorio. Si era lo segundo, dímelo y en un minuto dejo el documento marcado con las tres, más la cuenta actualizada y el estado en **APROBADO** — sabiendo que eso abre la puerta para derivar las historias de los cuatro ítems «por construir» (2.4, 2.5, 3.5, 5.6).

### 6 · Usuario — 2026-08-22 15:34:52
> P-1: si existen proyectos de hecho quedan 10 configurados
> P-2: NO
> P-3: SI

**Agente** — 2026-08-22 15:38:47
<!-- agente: 9cee01f1-4217-48c5-b30c-f48054327db3 -->

Antes de marcar nada, verifiqué P-1 contra el repo — y ahí hay una corrección que hacerte.

Listo. Marqué el inventario — [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md).

**P-1 · tu respuesta me hizo verificar, y la pregunta no tenía objeto.** Los dos capítulos ya están escritos hace días: [`21 · Automatización de procesos`](base/21-automatizacion-de-procesos.md) con ocho reglas (`AU1`-`AU8`) y [`22 · Sistemas que aprenden de datos`](base/22-sistemas-que-aprenden-de-datos.md) con nueve (`IA1`-`IA9`), de los pendientes [08](pendientes/hecho/patrones-rpa.md) (cerrado el 18) y [12](pendientes/hecho/patron-ia.md) (cerrado el 19). La fila 1.6 la escribí mal: el mismo documento ya los contaba como «Existe» en la fila 1.3 y se contradecía. Corregida a **Existe**; el grupo 1 queda 6 de 6.

Y confirmé lo de los 10: son exactamente 10 en el registro — AgroSystem, Aspectos legales, dp_card, este repo, Gestión de Servicios Tecnológicos, LocalHub, matematica, Proyecto de grado, RNI y shopnest-mesa.

**P-2 · NO** → ítem 6.2 **descartado por ahora**. El contrato del adaptador queda intacto, sin construir nada encima.

**P-3 · SÍ** → ítem 6.3 **Por construir**, detrás del 5.6. Sin la medición de todos los proyectos de una vez, el tablero no tendría qué mostrar.

Tus tres respuestas quedaron además en §0 como decisiones de alcance con fecha, para que nadie las vuelva a preguntar.

Los hallazgos los escribí en [historico-chat/resumenes/2026-08-22/el-inventario-de-cimiento.md](historico-chat/resumenes/2026-08-22/el-inventario-de-cimiento.md), con las dos historias que dispara P-3 ya redactadas en orden.

---

El inventario sigue en **EN REVISIÓN** por una sola cosa, y es la que no puedo contestar yo:

**¿Falta alguna funcionalidad en las 27 filas?** Si no falta ninguna, dime «aprobado» y lo paso a **APROBADO**; ahí se abre la puerta para derivar las historias de los cinco ítems por construir (2.4, 2.5, 3.5, 5.6 y 6.3).

Sobre el «suba todo» de antes: no commiteé nada. Cuando el inventario quede aprobado te muestro qué entra al commit y me lo apruebas aparte.

### 7 · Usuario — 2026-08-22 15:40:14
> si quiero agregar que el inventario se maneje desde la interfaz en dónde va?

**Agente** — 2026-08-22 15:41:18
<!-- agente: 1ea3771d-3766-4b29-8da4-a2869cbad7d3 -->

Va en el inventario mismo, como fila nueva — no en `pendientes/` ni en una regla. Es una funcionalidad de Cimiento que todavía no existe, y el inventario es justo el documento donde el alcance se declara antes de bajar a épica ([`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).

**Dónde exactamente: §5 «Instalación y administración de proyectos», como fila 5.7, estado «Por construir».** Ahí es donde ya viven 5.4 (el registro de proyectos en la interfaz), 5.5 y 5.6 — todas las que dicen «esto se maneja desde la interfaz». Y encaja con la decisión 1 de §0, que es tuya del 21: *«los proyectos se administran desde su interfaz, no desde archivos a mano»*.

**No va en §6.** Esa sección es de candidatos esperando tu confirmación; esto lo estás decidiendo tú ahora, así que entra como alcance comprometido, no como pregunta.

Ahora, dos cosas que encontré al ir a ubicarla y que cambian el tamaño de lo que estás pidiendo:

**1 · Ninguna de las siete épicas cubre la interfaz.** Miré [documentacion/epicas/README.md](documentacion/epicas/README.md): EP-007 es el instalador («que todo llegue a un proyecto con una línea»), no la aplicación Django. O sea que 5.4, 5.5, 5.6 y esta nueva 5.7 hoy **no tienen dónde bajar**. Mi propuesta es abrir **EP-008 · La interfaz de Cimiento** y que las cuatro cuelguen de ahí; forzarlas dentro de EP-007 mezcla dos cosas distintas y después no se sabe qué se está construyendo.

**2 · Necesito saber el borde, porque cambia si son dos filas o veinte.** ¿Es **solo el inventario** el que se maneja desde la interfaz, o es el primero de una familia — que **todos los entregables del ciclo** (los 22 moldes: planteamiento, épica, HU, fase, especificación, planes…) se administren ahí y dejen de escribirse a mano?

- Si es **solo el inventario**: una fila 5.7 y una historia. Chico y claro.
- Si es **todo el ciclo**: eso no es una fila en §5, es un **grupo nuevo** en el inventario y probablemente la épica más grande del proyecto. Y hay que decidir algo espinoso: si el documento vive en la base o sigue siendo el `.md` del repo y la interfaz solo lo edita — porque hoy todo el estándar (validadores, enganches, trazabilidad) lee archivos.

Dime cuál de las dos y escribo la fila —o el grupo— en el inventario de una vez.

### 8 · Usuario — 2026-08-22 15:42:10
> pero en cual de todos los puntos?

**Agente** — 2026-08-22 15:42:34
<!-- agente: 50b12d9e-71ad-4159-9c71-ddedf5b00174 -->

El inventario tiene ocho puntos. Estos:

| Punto | De qué trata | ¿Va ahí? |
|---|---|---|
| **0** | Lo que ya decidiste, con tus palabras | No — ahí van decisiones, no funcionalidades |
| **1** | El cuerpo de reglas | No — la interfaz no es una regla |
| **2** | El ciclo de vida y sus entregables | No — ahí está *qué* es el inventario, no *desde dónde* se maneja |
| **3** | La comprobación automática | No |
| **4** | La memoria entre sesiones | No |
| **5** | **Instalación y administración de proyectos** | **Sí — acá** |
| **6** | Proyección (ya contestada) | No — eso era para candidatos sin decidir |
| **7** | Preguntas abiertas | No |
| **8** | Qué pasa cuando apruebes | No — es el cierre |

**Punto 5**, después de la última fila que hay hoy, que es la 5.6. O sea que la fila nueva queda como **5.7**:

```
| 5.6 | La interfaz mide todos los proyectos de una vez y muestra el veredicto de cada uno | Por construir |
| 5.7 | El inventario de funcionalidades se administra desde la interfaz, no editando el .md a mano | Por construir |
```

Y la cuenta del punto 5 pasa de «5 existen, 1 por construir, de 6» a **«5 existen, 2 por construir, de 7»**.

Por qué el 5 y no el 2: el punto 2 responde *qué documentos tiene el ciclo* — ahí el inventario ya está, en la fila 2.1. Lo que quieres agregar no es otro documento, es **desde dónde se opera**, y esa familia entera vive en el 5: la 5.4 dice «el registro de proyectos en la interfaz», la 5.5 «el instalador escribe en el registro», la 5.6 «la interfaz mide». La tuya es la siguiente de esa lista.

¿La escribo así, con ese texto, o la redactas tú? Y sigue viva la pregunta de antes, que decide si es una fila o un grupo entero: **¿solo el inventario, o todos los entregables del ciclo se manejan desde la interfaz?**

### 9 · Usuario — 2026-08-22 15:43:57
> no se debe colocar lo que ya se decidió el inventario es todo lo que el proyecto debe tener sin importar si ya está hecho

### 10 · Usuario — 2026-08-22 15:44:27
> cuando se hagan las pruebas es que se sabe si ya se hizo

**Agente** — 2026-08-22 15:45:44
<!-- agente: cee8ada9-4b4f-4359-8ddc-fdb41d77b2b0 -->

Entendido, y es una corrección de fondo — no de dónde va la fila.

Tienes razón, y lo que corrigiste tumba dos cosas que hice hoy.

**Lo que entendí, en una línea cada una:**

1. El inventario es **todo lo que el proyecto debe tener** — completo. No se poda una fila porque ya esté construida, ni porque ya se haya decidido, ni porque ya se mencione en otra parte. Yo estaba usando «eso ya existe» y «eso ya está decidido» como criterio para dejar filas por fuera, y eso convierte el inventario en una lista de pendientes. Como el documento madura hasta ser el manual del producto, el manual habría nacido con huecos justo en lo que sí está construido.

2. **«Existe» no lo dice el agente: lo dice la prueba.** Yo marqué 22 filas como «Existe» porque leí el repo. Eso es una opinión, no evidencia. Hasta que corra la prueba, el estado honesto es *sin verificar* — que no es lo mismo que *no existe*.

Quedó escrito como **S-022** en [documentacion/senales.md](documentacion/senales.md), con tus dos frases.

**Qué invalida de lo de hoy:**

- Las 22 filas «Existe» del inventario quedan sin respaldo. Incluida la 1.6 que «corregí» hace un rato — cambié un error por otro: pasé de «Por confirmar» a «Existe», y sigue siendo afirmación mía.
- Mi argumento de recién para ubicar la fila («en el punto 2 el inventario ya está, en la fila 2.1») era exactamente el criterio equivocado. La fila 5.7 entra igual, esté o no cubierta en otro lado.

**Lo que propongo hacer, y necesito que elijas:**

La columna «Estado» hoy mezcla los dos ejes que acabas de separar. Mi propuesta es partirla en dos:

| # | Funcionalidad | Debe tener | Verificado |
|---|---|---|---|
| 5.7 | El inventario se administra desde la interfaz | Sí | Sin verificar |
| 3.1 | `validar.py` con sus subcomandos | Sí | ✅ `plan_pruebas` de la fase X, 2026-08-… |

«Debe tener» es tuyo y no cambia. «Verificado» solo se llena con la prueba que lo respalda y su fecha — sin prueba, dice *sin verificar*, y ahí se ve de un vistazo cuánto del producto está afirmado y cuánto demostrado.

Dos preguntas para arrancar:

**a) ¿Te sirve ese formato de dos columnas, o lo prefieres de otra forma?**

**b) Esto cambia la plantilla [`02-inventario-funcionalidades.md`](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) y la regla [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md), o sea que es cambio del estándar y va por la cadena: pendiente → historia → fase, con su `CHANGELOG` y su `VERSION`.** ¿Abro el pendiente ahora, o primero arreglamos el inventario de Cimiento y el estándar después?

### 11 · Usuario — 2026-08-22 15:49:24
> a. otro para que explique de qué se trata
> b. si, el documento se debe desarrollar aplicando 00 ID9
>
> no hay que abrir pendiente, se debe corregir de una

**Agente** — 2026-08-22 15:56:13
<!-- agente: 41eafe06-410e-48fb-9b75-804b92de560f -->

Corregido de una, sin pendiente. Cuatro archivos:

**El molde** — [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md). Ahora encabeza con las dos leyes que dijiste, y la tabla queda así:

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|

«De qué se trata» es la columna que pediste, escrita a quien va a usar el producto y en la menor extensión con la que se entienda ([`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)). «Verificado» reemplaza al estado que afirmaba el agente: solo lo llena la prueba corrida, con su fecha, y sin prueba dice **Sin verificar**.

**El inventario de Cimiento** — [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md). Reescrito: **30 filas, las 30 sin verificar.** Ya no hay ninguna «Existe» dicha por mí. Creció de 27 a 30 porque entró todo lo que yo había dejado por fuera: los dos capítulos de dominio como filas propias (1.6 y 1.7), tu 5.7 del inventario desde la interfaz, y el tablero como 5.8, que bajó de proyección a producto porque contestaste que sí.

**La señal** — S-022 en [documentacion/senales.md](documentacion/senales.md), con tus dos frases textuales.

**La versión** — **32.0.0 MAYOR**, ⚠ obliga a migrar: un proyecto que ya tenga inventario escrito lo rehace. [CHANGELOG.md](CHANGELOG.md).

**No toqué [`02·F26`](base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md).** Sigue diciendo lo mismo y sigue siendo cierto: el inventario aprobado es la puerta. Lo que estaba mal era el molde, no la puerta. Si quieres que la regla también nombre de dónde sale el estado, dímelo — pero eso anula su checklist sellado y hay que volver a aplicarle las 20 filas.

Dos cosas quedan abiertas:

**P-4, la tuya sin contestar:** ¿desde la interfaz se administra **solo el inventario** (fila 5.7 y ya), o **todos los entregables del ciclo**? Si es lo segundo es un grupo nuevo, y hay que decidir si el documento vive en la base o sigue siendo el archivo del repositorio con la interfaz encima — hoy todo el estándar lee archivos.

**Una falla que no es mía:** `validar.py estandar` está en rojo por un enlace roto en [historico-chat/resumenes/indice-tematico.md](historico-chat/resumenes/indice-tematico.md#L553) — apunta a `sesion-3.md`, que otra sesión renombró. Detiene el `push` de cualquiera. No lo toqué por ser trabajo de otra sesión. ¿Lo arreglo?

### 12 · Usuario — 2026-08-22 15:58:57
> esto: "0. Lo que el usuario ya definió" no debe estar porque eso lo definen las pruebas

### 13 · Usuario — 2026-08-22 16:01:52
> p-4: todo el ciclo de vida
> aplique el nuevo inventario

**Agente** — 2026-08-22 16:05:20
<!-- agente: 12f31797-51c1-43b4-90e9-49c3c2bac1ff -->

Ahora el inventario de Cimiento con el molde nuevo y P-4 aplicada.

Aplicado. El inventario nuevo está en [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md): **34 filas, las 34 sin verificar.**

**Fuera «0. Lo que el usuario ya definió»**, del molde y del documento. Es la segunda de las tres leyes ahora: *acá no va lo que ya se decidió*. Antes de borrar comprobé que no se perdiera nada — las ocho decisiones ya estaban en el [planteamiento](prompts/cimiento-planteamiento.md): los diez proyectos en la línea 24, la administración desde la interfaz en la 30, «el ciclo no hace excepciones» en la 32, MariaDB 3307 y Django en la 67, el tablero en la 77. Copiarlas dejaba dos versiones de la misma decisión sin saber cuál manda.

**P-4 · todo el ciclo de vida** → grupo 6 nuevo, cinco filas:

| # | Funcionalidad |
|---|---|
| 6.1 | Cada documento del ciclo nace desde la interfaz |
| 6.2 | Los documentos se llenan y se corrigen ahí |
| 6.3 | El inventario se administra desde la interfaz |
| 6.4 | La interfaz no deja saltar eslabones |
| 6.5 | El expediente se consulta desde la interfaz |

La versión sigue en **32.0.0**: la entrada del CHANGELOG todavía no se ha publicado, así que la completé en vez de subir otra.

Queda una pregunta que no puedo contestar yo, y es la que decide el diseño:

**P-5 · Con todo el ciclo en la interfaz, ¿dónde vive cada documento?** Hoy el comprobador, los frenos de git y la trazabilidad **leen archivos**. Si los documentos pasan a la base, esos tres se quedan sin qué leer. Mi propuesta es repetir lo que ya funcionó con el registro de proyectos: **la base manda y el archivo se genera desde ella** — la interfaz administra y los comprobadores siguen leyendo lo de siempre.

Y sigue abierto lo de antes: los grupos 5 y 6 son 12 filas que **ninguna de las siete épicas cubre** (EP-007 es el instalador, no la aplicación). Piden una épica nueva de la interfaz.

Todo quedó en el resumen de la sesión, con las historias que dispara: [historico-chat/resumenes/2026-08-22/el-inventario-de-cimiento.md](historico-chat/resumenes/2026-08-22/el-inventario-de-cimiento.md).

### 14 · Usuario — 2026-08-22 16:06:28
> vuelvo y le digo no debe hacer rerencia a nada de lo que ya está no deben haber fechas ni nada de eso que el usuario etc...

### 15 · Usuario — 2026-08-22 16:08:38
> mire esto: Estado: EN REVISIÓN DEL USUARIO (2026-08-22). Este inventario es el punto de partida de las épicas: ninguna épica se deriva hasta que el usuario lo apruebe. Lo que diga «por confirmar» es una pregunta, no una decisión.
>
> el documento debe quedar como si no hubiera nada desarrollado pero se debe utilizar la información que ya se tiene para llenarlo

**Agente** — 2026-08-22 16:10:26
<!-- agente: 7faa2808-6b1d-4c6c-8afd-09a4f822ef05 -->

Hecho, en el molde y en el documento. Ninguno tiene ya una sola fecha.

**Lo que salió del inventario de Cimiento:**

- La fecha del estado. Ahora es solo `**Estado: EN REVISIÓN DEL USUARIO.**`
- El «por qué existe» y la mención a que Cimiento no tenía inventario.
- Las cuatro preguntas contestadas con su respuesta y su fecha. Queda **una sola pregunta**, la que sigue viva, renumerada `P-1`: dónde vive cada documento con todo el ciclo en la interfaz.
- La proyección con el segundo agente descartado. Una candidata que se descarta se borra, no se archiva.
- La firma del final, que decía quién lo escribió, cuándo y cuántas veces se reescribió.
- «las siete épicas existentes no cubren la interfaz» del cierre. Eso es estado de hoy, no producto.

**La ley 2 del molde es ahora la que dijiste:** *este documento no lleva historia — ni fechas, ni quién decidió qué, ni qué se preguntó y se contestó*. Y con ella la consecuencia operativa: una pregunta contestada deja de ser pregunta, sube a fila del producto o se va.

**Lo que quedó:** 34 filas en seis grupos, todas **Sin verificar**, llenadas con lo que ya se sabe del proyecto. Se lee como si nada estuviera construido, que es lo que pediste.

Lo que saqué no se perdió: las decisiones estaban ya en el [planteamiento](prompts/cimiento-planteamiento.md), y el rastro de qué se preguntó y qué se contestó está en el [resumen de la sesión](historico-chat/resumenes/2026-08-22/el-inventario-de-cimiento.md) y en la señal S-022.

El documento: [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md). El molde: [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md).

### 16 · Usuario — 2026-08-22 16:13:56
> esto: "EN REVISIÓN DEL USUARIO" no tiene por qué ir
> la pregunta es qué aporta esto: "Estado: EN REVISIÓN DEL USUARIO. Este inventario es el punto de partida de las épicas: ninguna épica se deriva hasta que el usuario lo apruebe. Lo que diga «por confirmar» es una pregunta, no una decisión."? 00 ID9 debe se tan claro que si un niño lo lee lo entiende

**Agente** — 2026-08-22 16:15:12
<!-- agente: 22c30cea-5a2b-480f-abc6-2436076436f9 -->

**No aportaba nada.** Era el documento hablando de sí mismo: en qué estado está, qué regla lo rige, cómo interpretar una casilla. Quien abre la lista quiere saber qué hace Cimiento, y esa línea no se lo decía.

Ahora arranca así:

> Esta es la lista completa de lo que Cimiento debe hacer. Cada fila dice qué es, para qué sirve y si ya se probó.

Y debajo, «Cómo se lee», tres puntos en el idioma de quien lo va a usar:

- **Están todas: las hechas y las que faltan.** Esta lista no dice qué falta: dice qué es Cimiento.
- **No dice cuándo ni quién.** Eso se guarda en el planteamiento y en el histórico.
- **«Sin verificar» quiere decir que nadie lo ha probado todavía.** No quiere decir que falte. Esa casilla solo la cambia una prueba corrida.

Lo mismo en el molde, para que ningún proyecto vuelva a heredar ese encabezado.

Tres cosas que salieron con él, y por qué:

- **«Estado: EN REVISIÓN DEL USUARIO»** — es un dato de trámite, no del producto. Y hoy lo llevaría la interfaz, no el texto.
- **«el punto de partida de las épicas»** — «épica» no la entiende quien va a usar Cimiento. La regla existe y se cumple igual sin anunciarla dentro del documento que rige.
- **«"por confirmar" es una pregunta, no una decisión»** — explicaba una etiqueta que ya no aparece en ninguna fila.

También cambié el cierre: «Qué pasa cuando **el usuario** apruebe» → «Qué pasa cuando **esto** se apruebe».

Está en [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md) y en [el molde](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), y lo anoté en la entrada 32.0.0 del [CHANGELOG](CHANGELOG.md), que todavía no se ha publicado.

### 17 · Usuario — 2026-08-22 16:16:17
> eso que dije debe quedar tambipen en la plantilla para que se replique en otros proyectos

**Agente** — 2026-08-22 16:18:41
<!-- agente: e4a4454d-2fb3-4d20-89cc-9356be0b8e43 -->

Ya está en el molde — es lo que se replica: [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md). Le agregué lo que faltaba de lo que dijiste.

**En la caja de instrucciones** (la que cada proyecto borra al llenarlo):

> **Se llena con todo lo que ya se sabe del proyecto, pero se escribe como si nada estuviera construido:** sin fechas, sin estado de trámite, sin decir qué se preguntó y qué se contestó.
> Lo que quede acá se replica a todo proyecto que herede el estándar, así que lo que sobre, sobra en todos.

**En el cuerpo, la prueba de que una fila está bien escrita:**

> **Un niño la lee y entiende qué hace el producto.** Si hay que saber del proyecto para entenderla, está escrita para adentro y hay que rehacerla.

Ahí cité [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) junto a [`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md): ID9 pide pocas palabras, ID7 pide que las entienda quien no sabe del tema. La prueba del niño es la de ID7, y es la que faltaba nombrar.

Después la apliqué al inventario de Cimiento y tres filas no la pasaban:

| Fila | Decía | Dice |
|---|---|---|
| 1.2 | «cada proyecto ajusta lo suyo en su **capa 3**» | «cada proyecto aprieta o afloja las suyas» |
| 2.4 | «requisitos, **trazabilidad**, defectos, arquitectura» | «qué se pidió, qué lo cumple, qué falló y cómo está montado el sistema» |
| 3.1 | «**citas sin destino**, fases incompletas, **secretos** escritos» | «referencias a algo que no existe, trabajos a medio cerrar, contraseñas escritas donde no van» |

El comprobador sigue en 0 marcas nuevas. La única falla del repositorio sigue siendo el enlace roto del índice temático, que es de otra sesión y no he tocado.

### 18 · Usuario — 2026-08-22 16:34:33
> toda la plantilla debe quedar para que se resuelva de tal manera que si un niño la lee el inventario lo entienda

**Agente** — 2026-08-22 16:36:48
<!-- agente: 5c5494d2-ae99-488e-83ce-eadfebee3447 -->

Reescrito el molde entero, no solo la columna: [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md).

Lo que salió, que era lo que obligaba a saber del proyecto para entenderlo:

| Decía | Dice |
|---|---|
| «Proyección: por confirmar con el usuario» | «Lo que todavía no se sabe si entra» |
| «no se derivan **épicas**» | «no se parte el trabajo en bloques» |
| «los **ítems** aprobados bajan a **requisitos**» | «cada fila baja a trabajo con su nombre y su número» |
| «Nada de esta sección está decidido; cada fila es una pregunta… sobre el **alcance**» | «Nada de acá está decidido: la duda es si entra o no al producto» |
| «cuántas verificadas, cuántas fallidas» | «cuántas probadas bien, cuántas probadas mal, cuántas sin probar» |
| «bloquea solo los **ítems** que la citan» | «detiene solo las filas que la nombran» |
| «El planteamiento de la propuesta se revisa» | «El papel donde se pidió el proyecto se revisa» |

La exigencia queda escrita en la caja del molde, para que ningún proyecto la pierda:

> **La prueba de que quedó bien escrita: un niño la lee y entiende qué hace el producto.** Vale para el documento entero, no solo para la tabla. Si para entender algo hay que saber del proyecto, está escrito para adentro y se rehace.

Con [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) citado al lado de [`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md): pocas palabras, y ninguna que haya que ir a buscar.

Un arreglo que salió de paso: las tres secciones fijas perdieron el número. Antes eran «2. Proyección», «3. Preguntas», «4. Qué pasa», y un proyecto con seis grupos las numera 7, 8 y 9 — el comprobador las reportaba como secciones faltantes en todos. Ahora coinciden.

Queda pendiente de tu lado la única pregunta viva del inventario de Cimiento, **P-1**: con todo el ciclo en la interfaz, ¿cada documento vive en la base, o sigue siendo el archivo del repositorio y la interfaz lo edita?

### 19 · Usuario — 2026-08-22 17:15:27
> en la db

**Agente** — 2026-08-22 17:16:41
<!-- agente: 009dce53-2bcb-4a63-9bd8-0c86a081a039 -->

**En la base.** Aplicado, y con eso el inventario se queda **sin preguntas abiertas**: la sección entera desapareció, que es lo que manda la regla — una pregunta contestada sube a fila o se va.

Subieron dos filas al grupo 6:

| # | Funcionalidad | De qué se trata |
|---|---|---|
| 6.6 | Los documentos viven en la base | Lo que se escribe queda guardado en la base de datos, y esa es la versión que manda. |
| 6.7 | Las comprobaciones siguen viendo lo que se escribe | Con los documentos en la base, el comprobador, los frenos y el expediente siguen revisando igual. |

La 6.7 no es un adorno: es la exigencia que tu decisión abre. Hoy el comprobador, los frenos de git y el expediente **leen archivos**, y si el documento pasa a la base se quedan sin qué leer. Escribí **qué** tiene que seguir pasando, no **cómo** — si la interfaz deja una copia en el repositorio o si los comprobadores aprenden a leer la base es decisión del plan, no del inventario.

**El inventario queda en 36 filas, seis grupos, todas sin verificar.** [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md)

Lo que falta para cerrarlo es tuyo: **¿lo apruebas?** Con el sí, las 36 filas bajan a trabajo. Y ahí aparece lo que vengo señalando: los grupos 5 y 6 son **14 filas de interfaz que ninguna de las siete épicas cubre** — EP-007 es el instalador, no la aplicación. Piden una épica nueva.

Sin commitear nada todavía. Cuando digas, te muestro qué entra y lo apruebas aparte.

### 20 · Usuario — 2026-08-22 17:18:26
> comite

**Agente** — 2026-08-22 17:20:55
<!-- agente: 7d962406-d993-4e76-9979-4eab5ffdfdf6 -->

Freno antes de commitear, porque lo que hay preparado no es lo nuestro.

**Hay 193 archivos en el área de preparación, y solo 7 son de esta conversación.** El resto lo puso otra sesión que sigue trabajando en este mismo repositorio ahora mismo: publicó la versión **32.0.1** encima de mi 32.0.0 mientras hablábamos.

El propio comprobador lo dice:

```
[AVISO] este commit mezcla archivos de 2 sesiones (cf3e0d35: 26 · d350bf4a: 2)
```

Lo mío son estos siete:

- [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md)
- [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md)
- [documentacion/senales.md](documentacion/senales.md) — la señal S-022
- `CHANGELOG.md` y `VERSION`
- la transcripción y el resumen de la sesión, más su línea en el índice del día

Tres caminos, y la diferencia importa:

**1 · Solo lo mío.** Se puede commitear por ruta sin tocar lo que la otra sesión tiene preparado. El pero: `CHANGELOG.md` y `VERSION` ya traen la entrada 32.0.1 de ella, y no los puedo dejar por fuera porque el freno del commit exige que todo cambio de `plantillas/` venga con su entrada y su versión. Resultado: mi commit arrastra su entrada, y esa entrada apunta a un pendiente y a una fase que todavía no están en el repositorio. Enlaces rotos hasta que ella cierre.

**2 · Todo.** Un solo commit con las tres sesiones del día. Queda coherente y sin enlaces rotos, pero mete 186 archivos que no has revisado hoy y que no salieron de esta conversación.

**3 · Esperar** a que la otra sesión cierre su commit, y commitear lo mío encima. Es lo más limpio: cada commit dice lo que hizo su sesión y nada queda roto en el camino.

**Recomiendo la 3**, y si no quieres esperar, la 1. La 2 es la que hace que dentro de un mes nadie pueda leer qué cambió y por qué.

¿Cuál?

### 21 · Usuario — 2026-08-22 18:16:28
> suba todo

**Agente** — 2026-08-22 18:21:33
<!-- agente: c61afe8a-5727-4a8b-9264-b89abbabfe66 -->

Subido. Tres commits en `main`, todos publicados en `origin`.

| Commit | Qué lleva |
|---|---|
| `5383047` | El molde del inventario y el inventario de Cimiento. Versión **32.1.0** |
| `6b20e85` | El enlace roto que detenía la publicación, y la apertura de la entrada del registro |
| `b906f6b` | El cierre del resumen de la sesión |

**El problema de la mezcla se resolvió solo.** Mientras te preguntaba cuál de los tres caminos, la otra sesión commiteó lo suyo — los 188 archivos y la versión 32.0.1. Así que cuando fui a commitear ya solo quedaba lo mío, y quedó en un commit limpio. La opción 3 que te recomendaba pasó sin que nadie esperara.

**Dos frenos me pararon en el camino**, y los dos eran reales:

- El guardián de versión rechazó el commit: mi 32.0.0 ya se había ido con el commit de la otra sesión, así que lo que quedaba sin publicar necesitaba entrada propia. De ahí salió la **32.1.0**, que registra la prueba del niño y las secciones sin número.
- La batería previa al `push` encontró el enlace roto del índice temático. Lo arreglé, aunque venga de otra sesión: detenía la publicación del repositorio entero y tú habías pedido subir.

**Lo que queda sin hacer, y lo dejé escrito sin marcar en el resumen:**

- Los hallazgos H-2 y H-5 no tienen archivo en [pendientes/](pendientes/).
- Las tres historias que disparan, y la épica de la interfaz, están descritas en el resumen pero no creadas. Ahí caen las 14 filas de los grupos 5 y 6 del inventario, que hoy no tienen dónde bajar.

Eso es lo siguiente, cuando quieras.

### 22 · Usuario — 2026-08-22 18:25:34
> de qué se trata esta sesión?

**Agente** — 2026-08-22 18:25:50
<!-- agente: e0dc1d3b-2312-4fbd-8d21-b0dff1284ed2 -->

Se guardó como [2026-08-22-el-inventario-de-cimiento.md](historico-chat/2026-08-22-el-inventario-de-cimiento.md).

**Empezó como una pregunta de procedimiento** — qué sigue después del planteamiento — y la respuesta era el inventario de funcionalidades, la puerta que hay que cruzar antes de derivar épicas. Fuimos a llenar el de Cimiento.

**Terminó cambiando el molde para todos los proyectos**, porque el que había estaba mal en cuatro cosas, y las cuatro las corregiste tú:

1. **Yo dejaba filas por fuera** porque «eso ya existe». El inventario es todo lo que el producto debe tener, esté construido o no.
2. **Yo marcaba 22 filas como «Existe»** por haber leído el código. Eso lo dice la prueba, no el agente. Ahora la columna se llama «Verificado» y solo la llena una prueba corrida.
3. **El documento arrastraba historia** — fechas, estado de trámite, quién decidió qué, las preguntas ya contestadas. Se lee como si nada estuviera construido, aunque se llene con lo que ya se sabe.
4. **Estaba escrito para adentro.** Ahora la prueba es que un niño lo lea y entienda qué hace el producto, y vale para el documento entero.

**Tres decisiones tuyas de alcance:** no entra un segundo agente; la interfaz sí será tablero de todos los proyectos; y todo el ciclo de vida se administra desde la interfaz, con los documentos viviendo **en la base**.

**Lo que quedó:** el inventario de Cimiento con 36 filas en seis grupos, todas sin verificar y sin preguntas abiertas. El molde reescrito, versión 32.1.0. La señal S-022. Todo comiteado y publicado.

**Lo que no:** las 14 filas de interfaz no tienen épica donde bajar, y dos hallazgos siguen sin su archivo en `pendientes/`.

Está en [el resumen](historico-chat/resumenes/2026-08-22/el-inventario-de-cimiento.md), hallazgo por hallazgo.

### 23 · Usuario — 2026-08-22 18:27:10
> si un niño lee las funcionalidades sabe de qué se trata?

**Agente** — 2026-08-22 18:27:58
<!-- agente: 1c28ce82-538e-43a3-b0b5-1519d560cd35 -->

No. Lo probé fila por fila y **21 de las 36 no pasan.**

Las palabras que un niño no tiene cómo entender, y que obligan a saber del proyecto:

| Fila | La palabra que la hunde |
|---|---|
| 1.1 | «prompt», «relajar» |
| 1.3 | «registros inmutables», «despliegue», «observabilidad» |
| 1.4 | «se versiona», «se deroga» |
| 1.6 | «cola de trabajo», «credenciales», «bot» |
| 2.1 | «planteamiento, épica, historia, fase, especificación» — la cadena entera |
| 2.2 | «moldes del ciclo» |
| 2.5 | «repositorio», «.docx» |
| 3.2 | «git», «confirmar y subir» |
| 3.3 | «enganches», «el histórico» |
| 3.4, 6.5 | «expediente» |
| 3.5, 5.6 | «veredicto», «cumplimiento» |
| 4.5 | «traza» |
| 5.2 | «desfase» |
| 5.5 | «altas» |
| 6.4 | «épica», «fase», «eslabones» |

Y la columna del nombre está peor que la de la descripción: «Núcleo blindado», «El canal de defectos», «Las señales», «El veredicto único» no le dicen nada a nadie de fuera.

Así se vería el grupo 1 arreglado:

| # | Funcionalidad | De qué se trata |
|---|---|---|
| 1.1 | Las reglas que no se pueden desobedecer | Un puñado de reglas que nadie puede saltarse, ni el dueño del proyecto ni quien le dé órdenes al programa. Si otra regla las contradice, mandan estas. |
| 1.2 | Las reglas de cómo se trabaja | Cómo se escribe el programa, cómo se guardan los datos, cómo se prueba lo hecho y cómo se anota lo que se hizo. Sirven sin importar con qué esté construido, y cada proyecto puede exigir más o menos. |
| 1.3 | Reglas extra que se encienden si se necesitan | Un proyecto puede activar reglas que otros no necesitan: guardar cosas que nunca se borran, publicar el programa para que la gente lo use, o vigilarlo mientras funciona. |
| 1.4 | Las reglas para escribir reglas | Cómo se crea una regla nueva, dónde se guarda, cómo se le pone número y cómo se retira cuando deja de servir. |
| 1.5 | La explicación para el que llega nuevo | Todo el camino de un proyecto contado en palabras normales, para alguien que no sabe nada del tema. |
| 1.6 | Reglas para los programas que hacen tareas solos | Lo que hay que cuidar cuando un programa hace solo lo que haría una persona: que no se rompa si la pantalla cambia, que las tareas esperen en fila, que se distinga «esto no se puede hacer» de «esto se dañó», y que las contraseñas no queden escritas adentro. |
| 1.7 | Reglas para los programas que aprenden | Lo que hay que cuidar cuando un programa aprende de los datos y decide cosas: tener la lista de los que están funcionando, que cada uno tenga un responsable con nombre y apellido, vigilar más los que pueden hacer más daño, y revisarlos cada cierto tiempo. |

¿Ese es el tono? Si sí, rehago los otros cinco grupos igual. Si te parece que se fue demasiado largo, lo aprieto: la prueba del niño pide que entienda, y `00·ID9` pide que sea corto — cuando chocan, mandas tú.

### 24 · Usuario — 2026-08-22 18:29:51
> si y eso debe quedar en la plantilla para que aplique a los demás proyectos

**Agente** — 2026-08-22 18:34:42
<!-- agente: f630f9f7-a5ae-436e-b003-8e96379d6fc7 -->

Hecho y publicado. **Las 36 filas reescritas**, y los seis nombres de grupo también:

| Antes | Ahora |
|---|---|
| El cuerpo de reglas | Las reglas |
| El ciclo de vida y sus entregables | Los pasos de todo proyecto y los papeles que deja |
| La comprobación automática | Lo que se revisa solo |
| La memoria entre sesiones | Lo que se recuerda de una vez para otra |
| Instalación y administración de proyectos | Poner esto a andar en cada proyecto |
| El ciclo de vida se administra desde la interfaz | Trabajar el proyecto desde la pantalla |

**En el molde quedó lo que se replica** — [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md):

La prueba cubre ahora **las tres cosas**: el nombre del grupo, el nombre de la funcionalidad y su descripción. Antes decía «el documento entero» y yo lo había leído como «la descripción». Y va con el ejemplo, que es lo que de verdad transmite el tono:

```
INCORRECTO: | 1.1 | Núcleo blindado | Las reglas que ningún proyecto, prompt ni
                    instrucción puede relajar |
CORRECTO:   | 1.1 | Las reglas que no se pueden desobedecer | Un puñado de reglas
                    que nadie puede saltarse, ni el dueño del proyecto ni quien
                    le dé órdenes al programa |
```

Versión **32.1.1**, commit `ce794ed`, publicado.

Lo anoté como hallazgo H-6 en el resumen, y vale la pena decirlo así: **la exigencia se escribió hace una hora y el documento que la estrenaba no la cumplía.** Una regla que su propio primer caso incumple no es una regla. La encontraste preguntando, no leyendo el molde.

Las palabras que se fueron, por si sirven de lista para otros documentos: «núcleo blindado», «expediente», «desfase», «traza», «veredicto», «altas», «enganches», «prompt», «git», «épica», «fase», «eslabones».

**Agente** — 2026-08-22 18:38:05
<!-- agente: 2f117b8f-9f2d-44ed-8537-45044d5b5170 -->

No. Son tres cosas distintas, y el estándar las separa a propósito:

| | Qué agrupa | Dónde vive |
|---|---|---|
| **Grupo del inventario** | Lo que se entiende junto **al leerlo** | El inventario, y nada más |
| **Épica** | Necesidad: historias que entregan un valor parecido | [`13·DOC16`](base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) |
| **Módulo** | Unidad **técnica**: dominio propio, con su prefijo de rutas o su especificación aparte | [`13·DOC13`](base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) |

El grupo del inventario es el más blando de los tres: existe para que la lista se pueda leer, no para mandar sobre el código. Por eso el molde dice «un grupo por cada parte del producto que se entienda sola», y no «un grupo por módulo».

En Cimiento se ve claro que no coinciden:

- **Grupos 1 y 2** (las reglas, los pasos y los papeles) no son código: son texto. No hay módulo detrás.
- **Grupo 3** (lo que se revisa solo) sí cae casi entero en [validadores/](validadores/).
- **Grupo 4** (lo que se recuerda) está repartido entre [historico-chat/](historico-chat/) y los enganches, que viven en dos sitios distintos.
- **Grupos 5 y 6** (instalar, y trabajar desde la pantalla) caen los dos en [interfaz/](interfaz/) más el instalador. Dos grupos, un módulo.

O sea: dos grupos sin módulo, uno que calza, uno repartido y dos que comparten.

Y de paso, algo que salió al mirar: **Cimiento no tiene catálogo de módulos.** Existe la hoja para hacerlo, [plantillas/catalogo-modulos.md](plantillas/catalogo-modulos.md), pero el proyecto no la llenó nunca, y `13·DOC13` lo exige antes de cerrar la unidad que crea un módulo. Es un hueco real, aparte del que ya sabíamos de la épica de la interfaz. ¿Lo anoto como pendiente?

### 25 · Usuario — 2026-08-22 18:39:16
> Es cierto que un niño lo debe entender pero tampoco tan infantil: "Un puñado de reglas que nadie puede saltarse, ni el dueño del proyecto ni quien le dé órdenes al programa. Si otra regla las contradice, mandan estas."

**Agente** — 2026-08-22 18:44:51
<!-- agente: b42d2274-f202-488b-b033-d96a6aff8d92 -->

Tienes razón: me pasé al otro lado. Claro no es infantil.

Corregido. El ejemplo que señalaste ahora dice:

> **Las reglas que no se pueden desobedecer** — Las reglas que ninguna otra puede contradecir. No las levanta el dueño del proyecto ni una instrucción dada al asistente: si algo choca con ellas, ellas mandan.

Se fue el «un puñado de», el rodeo de «quien le dé órdenes al programa» y la explicación de más. Dice lo mismo, directo.

**El tono quedó escrito en el molde**, para que no dependa de quién lo llene:

> **Claro no es infantil:** se usan palabras comunes y frases cortas, no se rodea lo que se quiere decir ni se explica de más. Se dice qué hace, en el tono con que se le explica algo a un adulto que no es del oficio.

Las otras que sonaban a cuento y ya no:

| Antes | Ahora |
|---|---|
| «las **mañas** de quien manda» | «sus preferencias de trabajo» |
| «ni cuando el trabajo es **chiquito**» | «por pequeño que sea el trabajo» |
| «una sola **nota** por proyecto» | «una sola calificación por proyecto» |
| «qué **papeles** tiene el proyecto» | «qué documentos tiene el proyecto» |
| «qué órdenes ejecutó el **ayudante**» | «qué ejecutó el asistente, orden por orden» |
| «una **hoja** lista para cada papel» | «un formato listo para cada documento» |

Y corregí el ejemplo del molde, que era el peor caso: el «CORRECTO» que yo había puesto era justo la versión infantil que acabas de señalar. Un molde que enseña con un mal ejemplo enseña mal a todos los proyectos.

Versión **32.1.2**, commit `b34efb6`, publicado.

Dos cosas que debo decirte:

**El commit volvió a llevar archivos de otra sesión** — `validadores/enmascarar.py`, `version.py` y dos pruebas nuevas. Sigo usando «subir todo» como me dijiste, pero cada vez que lo hago se mezcla otra vez.

**Sigue sin responder lo de antes:** ¿anoto como pendiente el catálogo de módulos que Cimiento no tiene, y la épica de la interfaz donde caen las 14 filas de los grupos 5 y 6?

### 26 · Usuario — 2026-08-22 18:45:54
> pero para qué pendiente si estamos trabajando sobre ese documento?

**Agente** — 2026-08-22 18:47:15
<!-- agente: ab06300c-7e38-4eab-80af-169b59d09448 -->

Tienes razón. Ninguna de las dos era un pendiente, y por razones distintas.

Ninguna era pendiente, y por razones distintas.

**El catálogo de módulos era una fila del inventario.** Es algo que el producto debe tener, o sea que por la ley 1 va en la lista aunque no exista. Ya está escrita, la **2.6**:

> **La lista de las partes del proyecto** — En qué partes está dividido el proyecto por dentro, para qué sirve cada una y dónde está, para que quien llegue después no tenga que adivinarlo.

El grupo 2 queda en 6 filas, y el inventario en **37**.

**La épica no era nada.** Es el paso siguiente del camino, y ya está escrito en el cierre del documento: cuando apruebes, las 37 filas bajan a trabajo. No hay que anotar en ninguna parte que después viene lo que sigue.

Lo que me corregiste vale para más que hoy, así que lo dejé como señal **S-023**: ante un hueco hay tres destinos, y se elige por lo que el hueco **es**.

- Si el producto debe tenerlo → **fila del inventario**, aunque no exista todavía.
- Si es el paso siguiente de un camino ya escrito → **nada**, se hace cuando toque.
- Solo lo que hay que hacer y no cabe en el trabajo de hoy → **pendiente**.

Yo tiraba todo al tercero, que es el más caro: convierte un renglón de dos minutos en un trámite de tres pasos, y lo saca del sitio donde alguien lo iba a buscar.

Cambié dos archivos: [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md) y [documentacion/senales.md](documentacion/senales.md). Nada de `plantillas/` ni `base/`, así que no hay versión que subir.

¿Lo commiteo?

### 27 · Usuario — 2026-08-22 18:53:21
> Esto es lo que se busca en el inventario crear una plantilla destinada a definir el **inventario de funcionalidades que debe tener un proyecto antes de iniciar su desarrollo**.
>
> Diseña esta plantilla para que permita identificar, organizar y documentar de manera estructurada todas las funcionalidades que el sistema debe implementar.
>
> La plantilla debe permitir, como mínimo:
>
> * Identificar cada funcionalidad de forma única.
> * Definir el nombre y la descripción de la funcionalidad.
> * Establecer el objetivo o propósito de la funcionalidad.
> * Clasificarla por módulo, proceso o componente del sistema.
> * Definir los actores o roles que interactúan con ella.
> * Especificar las entradas y salidas esperadas.
> * Documentar las reglas de negocio asociadas.
> * Identificar dependencias con otras funcionalidades.
> * Definir las condiciones o criterios que debe cumplir para considerarse terminada.
> * Establecer prioridad y estado.
> * Identificar si requiere componentes de frontend, backend, base de datos, integraciones externas u otros elementos técnicos.
> * Permitir registrar observaciones, restricciones y consideraciones especiales.
>
> La plantilla debe estar diseñada para que el agente pueda utilizarla como **fuente de verdad del alcance funcional del proyecto**, permitiéndole posteriormente verificar qué funcionalidades están definidas, cuáles faltan por desarrollar y cuáles ya fueron implementadas.
>
> Además, debe diferenciar claramente entre:
>
> 1. **Funcionalidades obligatorias:** necesarias para que el sistema cumpla su propósito.
> 2. **Funcionalidades complementarias:** aportan valor, pero no son indispensables para la operación inicial.
> 3. **Funcionalidades futuras:** identificadas, pero fuera del alcance actual.
>
> El resultado debe ser una plantilla genérica y reutilizable para diferentes tipos de proyectos de software, evitando asumir un lenguaje, framework, arquitectura o tecnología específica.
>
> La plantilla debe estar estructurada de manera que pueda ser interpretada tanto por un desarrollador como por el agente, y debe servir posteriormente para generar planes de trabajo, historias de usuario, tareas de desarrollo, pruebas y documentación.

**Agente** — 2026-08-22 18:56:12
<!-- agente: 8bee7a78-9a8d-40c0-9422-108362b60d6f -->

Esto reemplaza el molde que teníamos: pasa de una tabla resumen a una ficha por funcionalidad. Lo escribo completo.

Listo el molde nuevo: [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md). Versión **33.0.0**, mayor, porque cambia la estructura de un documento que ya existe en los proyectos.

**Cada funcionalidad pasó de una fila a una ficha de catorce campos:**

| Campo | Cubre lo que pediste |
|---|---|
| ID `F-001` | Identificación única, y no se reutiliza aunque se descarte |
| Nombre y «De qué se trata» | Nombre y descripción |
| **Para qué sirve** | Objetivo. Si no se puede escribir, la funcionalidad no está justificada |
| **Parte del sistema** | Módulo, proceso o componente |
| **Quién la usa** | Actores y roles, con qué hace cada uno |
| **Qué recibe** / **Qué entrega** | Entradas y salidas |
| **Reglas que debe respetar** | Reglas de negocio, numeradas `RN-1` |
| **Depende de** | Dependencias, por ID |
| **Terminada cuando** | Criterios de terminación, numerados `CA-1`, cada uno respondible con sí o no |
| **Qué necesita construirse** | Pantalla, lógica de servidor, almacenamiento, conexión externa, tarea automática |
| **Prioridad** y **Estado** | Alta/Media/Baja · Definida, En desarrollo, Implementada, Descartada |
| **Lo que hay que tener en cuenta** | Observaciones, restricciones, casos raros |

Arriba queda un **resumen** de una línea por funcionalidad, para verlas todas juntas sin leer 37 fichas.

**Las tres clases** están escritas como tabla: obligatoria, complementaria, futura. Y separé algo que se confundía: «futura» es *decidida y para después*; «no se sabe si entra» es *una pregunta*, y esa sigue en su propia sección.

**Tres decisiones que tomé y conviene que revises:**

**1 · Estado y Verificado quedaron como dos casillas.** Pediste estado, y hace tres horas dijiste que si algo está hecho lo dicen las pruebas. Las dos cosas caben si no se mezclan: «Estado» es lo que alguien dice que va pasando; «Verificado» solo lo llena una prueba corrida. Una funcionalidad puede estar **implementada y sin verificar**, y eso quiere decir que se construyó y nadie lo ha demostrado. Si prefieres una sola casilla, se quita.

**2 · «Terminada cuando» baja tal cual a la historia.** Lo dejé escrito en el cierre: esos criterios se vuelven los criterios de aceptación y de ahí salen las pruebas, sin inventarlos aparte. Es lo que hace que la lista sirva para generar el trabajo y no solo para aprobarlo.

**3 · Sin tecnología, y lo dice explícito:** «necesita pantalla» sí, «necesita React» no. Eso vive en la ficha de tecnología del proyecto.

Ahora, lo que esto deja roto: **el inventario de Cimiento ya no coincide con su molde.** Son 37 funcionalidades a las que hay que escribirles quién las usa, qué reciben, qué entregan, sus reglas y sus criterios de terminación. Puedo llenarlo con lo que sé del repositorio, pero varias fichas van a quedar con preguntas para ti.

¿Lo migro ahora, o lo dejamos y commiteo primero el molde?

### 28 · Usuario — 2026-08-22 18:56:50
> ahora aplique ese nuevo formato a lo que ya tenemos

### 29 · Usuario — 2026-08-22 18:58:38
> siga

**Agente** — 2026-08-22 19:05:24
<!-- agente: 77134d54-7c70-4937-8c46-1a95699467f3 -->

Aplicado. [prompts/cimiento-inventario-funcionalidades.md](prompts/cimiento-inventario-funcionalidades.md): **37 fichas completas, 787 líneas.**

**Arriba, el resumen** — una línea por funcionalidad, con las siete columnas: ID, nombre, clase, parte del sistema, prioridad, estado y verificado. Ahí se ve todo junto sin leer las fichas.

**Abajo, las 37 fichas** con los catorce campos. Ejemplo de cómo quedó una:

> **F-015 · Los frenos al guardar**
> **Depende de** F-014
> **Reglas que debe respetar** — `RN-1` Lo que detiene es una falla, no un aviso. `RN-2` El freno de las marcas falla cuando la cuenta sube, no cuando es distinta de cero. `RN-3` Un cambio de lo que viaja a los proyectos no pasa sin su entrada en el registro y su versión.
> **Terminada cuando** — `CA-1` Guardar algo con una falla se detiene y se dice cuál. `CA-2` Publicar corre la batería completa. `CA-3` Los frenos se instalan solos.
> **Lo que hay que tener en cuenta** — Un freno que se salta a menudo deja de ser freno. Si estorba, el problema es la revisión, no el freno.

**Las cuentas:** 26 obligatorias, 11 complementarias, 0 futuras. Implementadas: 0. Verificadas: 0. Las 37 en «Definida», porque ninguna ha pasado por una fase con su plan y sus pruebas.

**Siete partes del sistema** salieron al clasificarlas: cuerpo de reglas, documentos del ciclo, comprobador, enganches, memoria, instalador e interfaz. Eso responde tu pregunta de antes: los grupos no eran módulos, y ahora la parte es una columna propia. Ojo con esto: **esas siete las deduje mirando el repositorio, no de un documento** — la lista de partes es la funcionalidad F-013, que aún no existe.

**Las reglas de negocio salieron mejor de lo que esperaba**, porque muchas ya estaban aprendidas a golpes. F-027 lleva «lo que se genera hacia afuera nunca vacía lo que tenía contenido», que viene de las tres veces que se perdió el contenido. F-022 lleva «una preferencia con alternativa se cumple por la alternativa más cómoda».

**Cuatro preguntas quedaron abiertas**, y cada una detiene solo su funcionalidad:

| Pregunta | Detiene |
|---|---|
| Cómo siguen viendo los documentos las revisiones cuando estén en la base | F-037 |
| Qué documentos entran al paquete de entrega | F-012 |
| Cómo pesa cada parte en la calificación única | F-018 |
| A partir de cuándo un proyecto «se quedó atrás» | F-030 |

La primera es la de fondo: o la base genera una copia en archivos, como ya se hace con la lista de proyectos, y nada de lo que hoy funciona se toca; o las revisiones aprenden a leer la base, que es más limpio y cuesta más. Mi propuesta es la primera.

Sin commitear. ¿Lo subo?

### 30 · Usuario — 2026-08-22 19:05:54
> defina funcionalidad

### 31 · Usuario — 2026-08-22 19:06:10
> defina

**Agente** — 2026-08-22 19:06:43
<!-- agente: 1a88806f-65c3-46bd-8074-b7e177597136 -->

**Una funcionalidad es algo que el producto hace.** Recibe algo, hace algo con eso y entrega un resultado que alguien puede ver.

Se reconoce por tres señas, y tienen que darse las tres:

1. **Tiene quién la use** — una persona con un rol, otro sistema, o el propio producto actuando solo.
2. **Tiene entrada y salida** — algo la dispara y algo queda distinto después.
3. **Se puede comprobar** — hay una forma de responder con sí o no si funcionó.

Lo que **no** es funcionalidad, aunque el producto lo tenga:

| No es | Qué es | Ejemplo |
|---|---|---|
| Un texto que el producto entrega | Un entregable | Una guía, un manual, un cuerpo de reglas |
| Una cualidad del producto | Un requisito de calidad | Que sea rápido, que sea seguro |
| Una parte de cómo está armado | Un componente | Una tabla, una carpeta, un módulo |
| Algo que se decidió | Una restricción | Que corra sin internet |

---

Ahora, aplicando eso al inventario que acabo de escribir: **nueve de las 37 no son funcionalidades.**

F-001, F-002, F-003, F-004, F-006 y F-007 son cuerpos de reglas. F-005 es una guía. F-009 son formatos. F-013 es una lista. Todas son **texto que Cimiento entrega**, no algo que Cimiento haga. No tienen quién las use en el sentido de la definición: se leen.

Y ahí hay un choque real que no puedo resolver yo:

**La mitad del valor de Cimiento es contenido, no comportamiento.** Las reglas *son* el producto. Si el inventario solo admite funcionalidades estrictas, esas nueve filas se caen — y eso contradice la primera ley, que dice que la lista tiene todo lo que el producto debe tener.

Dos salidas:

**A · Ampliar el documento a dos tipos.** Cada fila declara si es **funcionalidad** (algo que el producto hace) o **entregable** (algo que el producto entrega para leer). Los campos cambian según el tipo: un entregable no tiene «qué recibe» ni «qué entrega», tiene «quién lo lee» y «qué debe contener». El inventario sigue completo y cada fila se juzga con la vara que le corresponde.

**B · Reescribir las nueve como la acción que las usa.** «Las reglas que no se pueden desobedecer» pasa a ser «cargar y hacer cumplir las reglas en cada sesión», que sí tiene entrada, salida y comprobación. El texto de las reglas queda como insumo, no como fila.

**Recomiendo A.** La B suena más limpia pero esconde el producto detrás del mecanismo que lo carga, y un manual armado desde ahí no diría qué reglas hay. Además la A sirve a cualquier proyecto que entregue documentación, que son todos.

¿Cuál? Y sea cual sea, la definición que acabo de darte debería quedar en el glosario del estándar, que hoy no la tiene: define «funcionalidad implementada» pero nunca «funcionalidad».
