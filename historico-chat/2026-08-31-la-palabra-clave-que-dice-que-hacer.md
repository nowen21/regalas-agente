<!-- sesion: f6dbc715-b0ac-488e-9a51-c495f3004132 -->
<!-- nombre: preguntado -->

# 2026-08-31 — La palabra clave que dice que hacer

## Conversación

### 1 · Usuario — 2026-08-31 08:25:41
> <ide_opened_file>The user opened the file Untitled-1 in the IDE. This may or may not be related to the current task.</ide_opened_file>
> levante a localhub en el puerto 8002

**Agente** — 2026-08-31 08:29:14
<!-- agente: 865f987b-7c1b-40ea-966d-daf09dde8b34 -->

LocalHub está arriba en <http://127.0.0.1:8002/> — responde 200 y ya abrió el navegador.

- Comando: `.venv\Scripts\python.exe manage.py start --port 8002` en `C:\DesarrollosClaude\personales\localhub\proyectos\localhub`
- Corriendo en segundo plano (ID `bw4cc81vs`), con el autorreload de Django activo.
- Al arrancar reindexó los workspaces 2, 8 y 9 (3636, 270 y 1250 nodos), sin archivos ilegibles.

Cuando quiera bajarlo, dígame y detengo el proceso.

### 2 · Usuario — 2026-09-26 19:26:46
> cuál es la regla que debe indicarse una plabra clave para que el agente sepa qué debe hacer?

**Agente** — 2026-09-26 19:28:58
<!-- agente: 070435b0-c0ca-49f4-bd67-33177277e31c -->

La regla es **`01·C28` — «Sin la palabra que diga qué se espera, el agente no actúa»**, en [base/01-conducta.md:899](base/01-conducta.md#L899).

Lo que exige, en una línea: cada pedido abre con una palabra de la lista, y esa palabra fija el **máximo** que el agente puede hacer, no el mínimo. Sin ella no se toca nada: se responde con la lista y se espera.

La lista no está en la regla —son dieciocho palabras, no caben en el cuerpo— sino en su anexo [base/01-conducta/palabras-clave.md](base/01-conducta/palabras-clave.md), agrupadas por lo que autorizan:

| Grupo | Palabras |
|---|---|
| No tocan nada | pregunta · explique · analicemos · revise · proponga · busque · compare · verifique |
| Cambian el proyecto | hágalo/aplique · corrija · escriba/redacte · suba · recuerde · registre · revierta |
| Mandan sobre el trabajo | apruebo · continúe · pare |

Tres límites que el anexo deja escritos: una palabra parecida no cuenta («arregle» no es «corrija»), la palabra es techo y no piso (con `revise` se reporta aunque el arreglo sea de un renglón), y ninguna palabra autoriza actuar por adelantado.

De dónde viene: la HU [HU-036 · El pedido dice qué se espera](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/HU-036-el-pedido-dice-que-se-espera.md), fase `A-EP-001-HU-036`. Dos cosas de esa fase siguen abiertas: el commit (estación 9) y tres de los cinco casos de prueba, que quedaron sin verificar porque hay que correrlos en una sesión nueva. No es comprobable por programa, y así está declarado en `validadores/reglas-validables.md`.

Aparte: esta sesión la guardo como `2026-08-31-la-palabra-clave-que-dice-que-hacer.md` — se levantó LocalHub en el 8002 y se consultó la regla `01·C28`, ¿va?

### 3 · Usuario — 2026-10-06 13:29:42
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\01-conducta\palabras-clave.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> pregunta ya se puede cerrar esta sesión?

**Agente** — 2026-10-06 13:31:02
<!-- agente: 29c61572-8e3f-480e-99c7-2b96f1c30c81 -->

No todavía. El molde de [resumenes/2026-08-31/sesion.md](historico-chat/resumenes/2026-08-31/sesion.md) tiene cuatro casillas para cerrar y las cuatro están sin marcar.

Qué falta, concretamente:

1. **El resumen dice «Nada todavía»** y la sesión sí dejó cosas: se levantó LocalHub en el 8002 y se ubicó la regla `01·C28` con su anexo. Mientras eso no esté escrito, cerrar lo pierde.
2. **La sesión no tiene nombre.** Sigue guardada como `2026-08-31-sesion.md`, que no dice de qué trata. Se propuso `2026-08-31-la-palabra-clave-que-dice-que-hacer` y usted no ha dicho si va.
3. **Hay 46 archivos sin guardar** en el árbol de trabajo. La mayoría viene de antes de esta sesión, pero la casilla «lo que se hizo está aprobado y guardado» los cuenta igual.

Fuera de esta sesión queda abierto lo de la fase `A-EP-001-HU-036`: está en estación 9 esperando el commit, y tres de sus cinco casos de prueba siguen sin correr porque hay que hacerlo en una sesión nueva. Esa sesión nueva podría ser la próxima.

Lo más corto para dejarlo cerrable es escribir el resumen y renombrar la sesión. Dígame con cuál palabra sigo: `escriba` el resumen, `hágalo` para el renombre, o las dos.

### 4 · Usuario — 2026-10-06 14:41:19
> pregunta: que se debe hacer?

**Agente** — 2026-10-06 14:41:56
<!-- agente: 11c36d7a-2d9d-4fff-a5fe-8f22b7dd9cb8 -->

Cuatro pasos, en este orden.

**1. Escribir los hallazgos en el resumen.** Hoy quedaron dos: LocalHub levantado en el 8002, y la ubicación de la regla `01·C28` con su anexo de dieciocho palabras. Ninguno abre pendiente: los dos se resuelven con la decisión escrita en el campo de dónde queda. El molde está en `plantillas/sesion.md`.

**2. Renombrar la sesión.** Dos cosas, o el índice apunta a un archivo que ya no está:

```
python "C:/Ing. Jose/ia/agente/validadores/historico.py" --renombrar "C:/Ing. Jose/ia/agente/historico-chat/2026-08-31-sesion.md" --tema "la-palabra-clave-que-dice-que-hacer" --resumen "se levantó LocalHub en el 8002 y se ubicó la regla 01·C28"
```

Y la otra la escribe el usuario, porque el agente no puede: `/rename la-palabra-clave-que-dice-que-hacer`.

**3. Decidir qué pasa con los 46 archivos sin guardar.** Es lo único que no se resuelve en un minuto. Vienen de trabajo anterior y mezclan tres cosas distintas: la plataforma, el acceso por grupos y la documentación de fases. Hay que revisarlos y repartirlos en commits por tema, o dejarlos quietos y anotar en el resumen que quedan así a propósito. Las dos salidas cierran la casilla; lo que no la cierra es no decidir.

**4. Marcar las cuatro casillas** del resumen y cerrar.

Fuera de esto, para la sesión siguiente queda la fase `A-EP-001-HU-036`: su commit, y los tres casos de prueba que no se pueden correr acá porque el agente que escribió la regla ya sabe lo que ella le exige.

El paso 3 es el que decide si la sesión cierra hoy. Los otros tres son mecánicos.

### 5 · Usuario — 2026-10-06 14:45:39
> pregunta: qué le escribo?

**Agente** — 2026-10-06 14:46:04
<!-- agente: eaacc959-c916-426b-81be-85000bb729ac -->

Según `01·C28`, la palabra va al empezar y alcanza para todo el pedido. Tres opciones, según qué se quiera que pase.

**Para los pasos 1 y 2, que son mecánicos:**

```
hágalo: escriba el resumen de hoy con los dos hallazgos y corra el renombre de la sesión
```

Después de eso falta pegar `/rename la-palabra-clave-que-dice-que-hacer`, que es comando del usuario y el agente no lo puede escribir.

**Para el paso 3, mirar sin tocar:**

```
revise los 46 archivos sin guardar y proponga cómo repartirlos en commits por tema
```

Con `revise` se reporta y no se corrige, aunque algo se vea claro. Sirve para decidir con el mapa en la mano.

**Para el paso 3, si ya está decidido dejarlos quietos:**

```
registre en el resumen que los 46 archivos quedan sin guardar a propósito
```

Lo más corto para cerrar hoy es la primera, y después la tercera. La segunda abre otra tanda de trabajo, porque repartir 46 archivos en commits por tema no es de un renglón.

### 6 · Usuario — 2026-10-06 14:46:59
> hagalo

**Agente** — 2026-10-06 14:53:37
<!-- agente: d73c6bae-a10e-4ca2-9390-a80d539bf0f8 -->

Hecho. Dos archivos y dos índices.

**La sesión ya tiene nombre.** La transcripción quedó como [2026-08-31-la-palabra-clave-que-dice-que-hacer.md](historico-chat/2026-08-31-la-palabra-clave-que-dice-que-hacer.md), con su línea en [historico-chat/README.md:199](historico-chat/README.md#L199) y el enlace al resumen al final de esa línea.

**El resumen está escrito**, en [resumenes/2026-08-31/la-palabra-clave-que-dice-que-hacer.md](historico-chat/resumenes/2026-08-31/la-palabra-clave-que-dice-que-hacer.md), y dice **nada**.

Esa es la corrección: antes hablé de «dos hallazgos», y contra el molde de [plantillas/sesion.md](plantillas/sesion.md) ninguno de los dos lo es. Un hallazgo necesita su pendiente y tiene que caer en uno de los cuatro destinos. Levantar LocalHub es una operación que se repite leyendo el README de ese proyecto, y ubicar `01·C28` fue responder por algo que ya estaba escrito. El molde cierra diciendo justo esto: si la sesión no dejó nada, se escribe «nada», que es un dato y no un olvido. Las dos cosas quedaron igual nombradas en el resumen, para que nadie tenga que releer la transcripción.

También quedó anotado, sin contarlo como hallazgo, que la fase `A-EP-001-HU-036` sigue en estación 9: el commit sin hacer y tres de cinco pruebas sin correr. Eso ya vivía en su `estado-fase.md`.

**Un tropiezo, porque vale saberlo.** El renombre no mueve solo la transcripción: mueve también el resumen de esa sesión, para que los dos se llamen igual. El resumen se escribió primero como `sesion.md` y quedó por fuera del nombre nuevo, así que hubo que llevarlo al archivo correcto. En adelante, primero el renombre y después el resumen.

Falta lo que el agente no puede hacer ni decidir:

- Pegar `/rename la-palabra-clave-que-dice-que-hacer`, para que la pestaña y `/resume` queden con el mismo nombre.
- Los 46 archivos sin guardar. Es la cuarta casilla del resumen, la única sin marcar.

### 7 · Usuario — 2026-10-06 16:19:18
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\01-conducta\palabras-clave.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> ¿que sige?

**Agente** — 2026-10-06 16:19:25
<!-- agente: f096f0ae-e910-4d07-8eed-48a61b26da55 -->

Falta la palabra de `01·C28`: el mensaje no dice qué se espera. Para esto serviría `pregunta`, `proponga` o `liste`.

Y un aviso que vale la pena: el enganche sigue diciendo que el resumen está vacío, aunque ya quedó escrito. Dice «nada» a propósito, y el enganche lee eso como un olvido. Eso sí es un hallazgo, y con la palabra se registra.

### 8 · Usuario — 2026-10-06 16:21:31
> pregunta como hago para indicarle a la regla que lo que vaya entre ¿? también es una pregunta

**Agente** — 2026-10-06 16:24:10
<!-- agente: b7a46a4d-6ce2-41f0-b42d-a182c98a764e -->

Por la lista no se puede, y ya hay una fila que lo intentó.

En [base/01-conducta/palabras-clave.md:26](base/01-conducta/palabras-clave.md#L26) alguien escribió la fila `| **¿La pregunta que se haga?** | Responder lo que se pregunta |`. El programa la lee como si «¿La pregunta que se haga?» fuera una palabra literal, así que nunca coincide con nada. Esa fila no hace nada hoy, y es la que aparece en el aviso del enganche entre las palabras válidas.

**Por qué.** Quien decide es [recuperar.py](proyectos/cimiento/core/herramientas/recuperar.py). La expresión `_FRASE` de la [línea 54](proyectos/cimiento/core/herramientas/recuperar.py#L54) se come el `¿` de apertura y se queda con la primera palabra en minúscula. De «¿qué sigue?» saca `que`, que no está en la lista. Y `_FILA_PALABRA` solo sabe capturar palabras en negrita, así que la lista no tiene cómo expresar «cualquier cosa entre signos».

**Qué habría que cambiar.** Tres cosas, y en este orden:

1. En `recuperar.py`, que una frase que abra con `¿` y cierre con `?` valga como la palabra «Pregunta». Toca los tres métodos que hoy dependen de `palabras_de_inicio`: `trae_palabra_clave` ([167](proyectos/cimiento/core/herramientas/recuperar.py#L167)), `palabra_clave` ([151](proyectos/cimiento/core/herramientas/recuperar.py#L151)) y `tareas_del_mensaje`.
2. En el anexo, reemplazar esa fila por una frase en prosa que diga la forma, porque no es una palabra y la tabla de palabras no es su lugar. El anexo ya tiene la sección «Lo que la lista no admite», que es donde encaja.
3. Las pruebas, en `proyectos/cimiento/core/herramientas/`, junto a las de `Respondo`, que es el caso más parecido.

**Una decisión que hay que tomar antes.** En la práctica casi nadie escribe el `¿` de apertura: lo normal es «que sigue?». Si solo cuenta la forma completa `¿…?`, el caso que más se repite sigue fallando. Y si cuenta el `?` final solo, entonces cualquier frase que termine en pregunta autoriza la clase que no toca nada, que es lo mismo que autoriza «Pregunta». El riesgo es bajo, pero es una decisión distinta y conviene dejarla escrita.

**Lo que esto pide.** Es un cambio de comportamiento, así que por `02·F0` va por la cadena: pendiente, historia y fase con su plan. El capítulo que lo recibe es el `01`, y el recuperador viene de `EP-005` y `EP-025` según sus propios comentarios.

Con `registre` queda el pendiente escrito y de ahí sale la historia.

### 9 · Usuario — 2026-10-06 16:30:12
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\01-conducta\palabras-clave.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> ok

**Agente** — 2026-10-06 16:30:28
<!-- agente: 5afc663e-0633-4d61-8f4d-84bba49603c8 -->

«ok» no dice qué se espera, y `01·C28` pide la palabra.

Para lo que quedó abierto sirve una de estas:

- `registre` el pendiente de la pregunta entre signos y el del aviso que lee «nada» como resumen vacío.
- `revise` los 46 archivos sin guardar y proponga cómo repartirlos.
- `pare`, si la sesión queda así.

### 10 · Usuario — 2026-10-06 16:31:00
> analicemos: le regla que si dice

**Agente** — 2026-10-06 16:31:12
<!-- agente: c1121b32-b831-4fd7-a599-2ee2669177c6 -->

El mensaje quedó cortado: «le regla que si dice». La palabra está clara, `analicemos` autoriza estudiar y dar una lectura, pero falta el tema.

Dos lecturas posibles:

- **Qué dice hoy `01·C28`**, el texto de la regla contra lo que el programa hace de verdad.
- **Qué debería decir** para que la pregunta entre signos cuente.

¿Cuál de las dos, o era otra cosa?

### 11 · Usuario — 2026-10-06 16:31:45
> respondo: lea la regla que si dice ok

**Agente** — 2026-10-06 16:33:46
<!-- agente: 8995b1bb-a9d6-4a15-908b-6a0bf197c548 -->

La regla sí dice `ok` ahora. El anexo quedó editado y todavía sin guardar: entraron `Liste` y `OK`, y salió la fila `¿La pregunta que se haga?`, que era la que no servía.

**El programa ya lo reconoce, sin tocar código.** `_FILA_PALABRA` lee cualquier fila con la palabra en negrita, y la detección baja el mensaje a minúsculas sin tildes. De «ok» saca `ok`, y coincide. Eso explica el aviso de hace dos turnos: cuando llegó «ok» la fila todavía no estaba.

**Lo que conviene revisar de la celda.** `OK` quedó en el grupo de las que no tocan nada, que es su lugar. Pero las otras nueve de ese grupo dicen un verbo: responder, mirar, comparar. `OK` dice «Se entiende la explicación», que describe al usuario y no lo que queda autorizado. Leída al pie de la letra, no autoriza nada, y eso es justo lo correcto. Vale la pena que lo diga: «nada, es acuse de recibo». Así el agente no la lee como permiso para seguir con lo que venía, que es lo que haría `Continúe`.

**Dos cosas quedan desalineadas.** El sello del checklist de `C28`, en [base/01-conducta.md:1040](base/01-conducta.md#L1040), dice «en el anexo, las dieciocho palabras», y hoy son veintiuna filas, veintitrés formas contando `aplique` y `redacte`. Y `20·M10` pide entrada en `CHANGELOG.md` y subir `VERSION`: agregar palabras a la lista es aditivo, así que sería **MENOR**.

**Lo que no cambia.** El cuerpo de la regla no se tocó, así que el sello del checklist sigue vigente: ese sello se anula cuando cambia el texto de la regla, no su anexo.

Y queda abierto lo de antes: la pregunta entre signos sigue sin funcionar, porque `¿…?` no es una palabra y la tabla solo sabe de palabras. Esa necesita código.

### 12 · Usuario — 2026-10-06 16:35:53
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\01-conducta\palabras-clave.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> ok

**Agente** — 2026-10-06 16:36:06
<!-- agente: 31984815-e130-4bd6-9ca7-b1331c4318b7 -->

`OK` ya está en la lista, y el aviso del enganche no apareció: la fila nueva funciona.

Lo que autoriza es nada, así que el análisis queda ahí y no se toca nada.

Lo que sigue abierto, cuando haya con qué seguir:

- El anexo y `01-conducta.md` están editados sin guardar, y falta la entrada en `CHANGELOG.md` con versión **MENOR**.
- El sello de `C28` todavía dice «dieciocho palabras».
- La celda de `OK` describe al usuario y no lo que queda autorizado.
- La pregunta entre `¿?` sigue necesitando código.

### 13 · Usuario — 2026-10-06 16:38:07
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\01-conducta.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> ok

**Agente** — 2026-10-06 16:38:17
<!-- agente: 0ea56237-a839-4b72-95c0-114d759bcd22 -->

Entendido. Nada que hacer con `ok`, así que acá queda, en espera de la palabra que diga qué sigue.

### 14 · Usuario — 2026-10-06 16:39:21
> Revice ya corregí la regla para que no diga el número

**Agente** — 2026-10-06 16:39:38
<!-- agente: c4597222-6902-4294-98e3-e11e7eec9b8c -->

Llegó como «Revice», con c, y la lista solo tiene `Revise`. El anexo dice que una palabra parecida no cuenta, así que acá no se hace nada.

Con `revise` escrito así, se mira la regla y se reporta lo que haya.

### 15 · Usuario — 2026-10-06 16:39:54
> revise

**Agente** — 2026-10-06 16:41:26
<!-- agente: fbb67c93-080f-41f7-ad0d-6632e7abdb7c -->

Revisado. El cambio quedó bien.

**Lo corregido.** En [base/01-conducta.md:1040](base/01-conducta.md#L1040) el sello de `C28` ya dice «en el anexo, las palabras y qué autoriza cada una», sin el número. Es el único lugar del cuerpo de reglas que lo traía.

**Lo que encontré, en orden de lo que cuesta.**

1. **Falta la versión.** `VERSION` sigue en `56.1.0` y `CHANGELOG.md` no tiene entrada. Agregar `Liste` y `OK` es aditivo, así que por `20·M10` va **MENOR**, o sea `56.2.0`. Es lo único que un validador va a reclamar después.
2. **La celda de `OK` sigue describiendo al usuario:** «Se entiende la explicación». Las otras del grupo dicen qué queda autorizado. Conviene «nada, es acuse de recibo».
3. **El número sigue en cinco documentos de la fase `A-EP-001-HU-036`**, en su plan, su estado y su funcionalidad implementada. Eso **no se toca**: son el acta de lo que se decidió el 2026-08-24, cuando sí eran dieciocho. Lo anoto para que no se vuelva una cacería.
4. **Un cambio que viene colado** en el mismo archivo, línea 818: el resultado del checklist de otra regla pasó de `19 ✅, 0 ❌, 1 N/A` a `19 ✅ · 0 ❌ · 1 N/A`. Queda igual al resto de la casa, así que está bien, pero es de otra regla y no de esta. Si el commit se arma por tema, va aparte.

**Lo que corrí.** `validar.py versionado` da cero fallas, con un aviso viejo y ya reconocido sobre dos entradas de la 15.4.0. `validar.py estandar` da cero incumplimientos.

Nada se tocó: `revise` reporta y no corrige.

### 16 · Usuario — 2026-10-06 16:44:32
> Hágalo cambie la versión

**Agente** — 2026-10-06 16:47:41
<!-- agente: 319c4f17-6607-4d5b-84ca-2b0ec76e296a -->

Hecho.

- `VERSION` pasó de `56.1.0` a **`56.2.0`**.
- `CHANGELOG.md` abre con la entrada `## 56.2.0 — 2026-10-06`, **MENOR**, con las dos filas nuevas, la fila muerta que salió, y el sello que dejó de contar palabras.
- `validar.py versionado`: cero fallas, con el aviso viejo de las dos entradas de la 15.4.0.

**Por qué MENOR y no PARCHE.** Agregar `Liste` y `OK` es aditivo: ningún proyecto al día tiene que hacer nada. El sello que dejó de decir el número habría sido PARCHE solo, y el grado más alto manda.

**Lo que quedó por fuera de la entrada, a propósito.** Los dos totales de sello que pasaron de coma a punto medio, en [base/01-conducta.md:818](base/01-conducta.md#L818) y en `M10`, son de la fase `B-EP-001-HU-041`, y su propio plan de trabajo decidió «sin versión nueva» porque el sello no es el texto de la regla. Meterlos acá los versionaría contra lo que esa fase ya resolvió.

**Un dato que corregir.** El resumen de la sesión dice «46 archivos sin guardar», y ese número ya no sirve: el árbol cambió de forma desde que lo conté, `plataforma/` ahora es `proyectos/cimiento/`. Con `corrija` lo dejo sin número, diciendo solo que el árbol tiene cambios sin guardar.

### 17 · Usuario — 2026-10-06 16:48:13
> pregunta ya se puede cerrar esta sesión?

**Agente** — 2026-10-06 16:48:50
<!-- agente: 69b41358-d0ef-49b4-8c03-18b21e2edd25 -->

No todavía, y ahora falta más que antes.

**El resumen quedó mentiroso.** Dice «nada» y ya no es cierto: desde entonces la sesión cambió la lista de palabras de `01·C28`, subió la versión a `56.2.0` y escribió su entrada. También dice «46 archivos», y hoy el árbol tiene 67 con otra forma.

**Hay un hallazgo de verdad.** La fila `¿La pregunta que se haga?` estuvo en el anexo sin funcionar nunca, porque el programa la leía como una palabra literal. Eso no se recupera leyendo el código, así que es señal, y de ahí sale un pendiente: que la pregunta entre signos cuente, lo cual pide código en el recuperador.

**Y hay un hueco de cadena.** Las filas `Liste` y `OK` entraron al anexo editando el archivo a mano, sin pendiente, sin historia y sin fase. `02·F0` pide la cadena para todo cambio de comportamiento, y `01·C28` es comportamiento. La versión ya quedó registrada, pero el eslabón que la justifica no existe.

**Nada está guardado.** El último commit es `3e8a525`, de otra sesión.

Lo que cierra esto, en orden: `corrija` el resumen con lo que la sesión sí dejó, `registre` la señal y el pendiente, y `suba` lo de la lista de palabras con su versión. Los 67 archivos son otra cosa y no caben en un commit.

### 18 · Usuario — 2026-10-06 16:52:27
> respondo no asuma el hallazgo porque solo hice fue una pregunta la cual ya la descarté

**Agente** — 2026-10-06 16:52:49
<!-- agente: 897dfc60-716d-4b27-b19c-8f7931e34359 -->

Entendido: eso se descarta, no hay señal ni pendiente por ahí.

Con eso, para cerrar quedan dos cosas:

- **El resumen.** Dice «nada» y «46 archivos», y las dos cosas ya no son ciertas: la sesión subió la versión a `56.2.0` con su entrada en el registro. Con `corrija` queda al día.
- **Guardar.** Sin commit están `VERSION`, `CHANGELOG.md`, `base/01-conducta.md`, el anexo de palabras, el histórico renombrado y el resumen. Es la cuarta casilla.

Los otros 61 archivos del árbol son de trabajo anterior y no son de esta sesión.

Queda sin decidir si las filas `Liste` y `OK` necesitan su eslabón de cadena, o si entran como ajuste de la lista sin fase. Eso lo decide quien manda sobre el estándar, no el agente.

### 19 · Usuario — 2026-10-06 16:54:06
> pregunta qué sigue?

**Agente** — 2026-10-06 16:54:17
<!-- agente: 9b26f18e-4b75-4dca-b07c-2b3d75b02b16 -->

Dos pasos, y el segundo necesita una decisión.

**1. Corregir el resumen.** Reemplazar «nada» por lo que la sesión sí dejó: la lista de palabras creció con `Liste` y `OK`, salió la fila que no servía, y la versión quedó en `56.2.0` con su entrada. Y quitar el «46 archivos», que ya no cuadra.

```
corrija el resumen de la sesión
```

**2. Guardar.** Son seis archivos de este tema: `VERSION`, `CHANGELOG.md`, `base/01-conducta.md`, `base/01-conducta/palabras-clave.md`, el histórico renombrado y su resumen.

```
suba lo de la lista de palabras
```

Antes de eso falta decidir si las filas `Liste` y `OK` llevan su eslabón de cadena o entran como ajuste de la lista. De eso depende si el commit va solo o con su fase.

Y un dato aparte: LocalHub en el 8002 se cayó cuando terminó el proceso de la sesión anterior. Si se necesita, se vuelve a levantar.

### 20 · Usuario — 2026-10-06 16:55:31
> corrija el resumen de la sesión

**Agente** — 2026-10-06 16:56:34
<!-- agente: adc68993-eb81-4108-abd7-86e5969de82a -->

Corregido.

**Lo que cambió el resumen.** Ya no dice «nada»: tiene el hallazgo `H-1`, con qué pasó, por qué importa y dónde quedó, que son el anexo, el sello de `01·C28` y la entrada `56.2.0`. El número de archivos salió.

**Lo descartado quedó escrito como descartado.** La pregunta entre signos aparece en una línea aparte, diciendo que se revisó y que se descartó en la misma sesión, para que nadie la reabra creyendo que se olvidó. No deja pendiente.

**Las casillas.** Las dos primeras quedaron marcadas. Las otras dos no:

- La tercera espera la decisión de si `Liste` y `OK` llevan su eslabón de cadena.
- La cuarta espera el commit de los seis archivos del tema.

**La línea del índice del día** también quedó al día, con lo que la sesión dejó en vez de «sin escribir todavía».

`validar.py sesiones` y `validar.py indices` dan cero incumplimientos.

### 21 · Usuario — 2026-10-06 16:57:29
> suba lo de la lista de palabras
