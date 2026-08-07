# Candidatas a regla — análisis de las sesiones del 2026-08-06

> **Qué es esto.** Un análisis, no un cambio. No se modificó ningún archivo del estándar: aquí solo van los hallazgos y las recomendaciones.
>
> **Carpeta.** El pedido decía `historico-chat/reglas-fecha/reglas.md`; se interpretó `reglas-<fecha>` y quedó en `reglas-2026-08-06/`. Tampoco se agregó la línea al índice de [`historico-chat/README.md`](../README.md), porque eso sería modificar un archivo.

---

## 1 · Alcance y método

**Sesiones leídas** (todas las de `historico-chat/` del 2026-08-06):

| Archivo | Tema | ¿Entra? |
|---|---|---|
| [2026-08-06-historico-chat.md](../2026-08-06-historico-chat.md) | Se crea la carpeta del histórico | Sí |
| [2026-08-06-meta-reglas-2.md](../2026-08-06-meta-reglas-2.md) | Nace la regla de reglas (`M1`–`M13`) | Sí |
| [2026-08-06-sesion-3.md](../2026-08-06-sesion-3.md) | El histórico no se escribía · el torniquete · el checklist de instalación | Sí |
| [2026-08-06-sesion-4.md](../2026-08-06-sesion-4.md) | Solo un saludo | Sí (sin material) |
| [2026-08-06-sesion-5.md](../2026-08-06-sesion-5.md) | Auditoría de las meta-reglas · anatomía de una regla · capítulo 20 | Sí |
| [2026-08-06-sesion-6.md](../2026-08-06-sesion-6.md) | Audio: el agente no oye | Sí (sin material) |
| [2026-08-06-sesion-7.md](../2026-08-06-sesion-7.md) | Duplicado del anterior, sin marca de sesión | Sí (sin material) |
| [2026-08-06-sesion-8.md](../2026-08-06-sesion-8.md) | Transcripción de imágenes del diplomado + dos intercambios sobre `F0` | Parcial |
| [2026-08-06-sesion-9.md](../2026-08-06-sesion-9.md) | Carpeta `diplomado-ia` | **Excluida** (lo pidió el usuario) |

De la sesión 8 se toma solo lo que es del estándar: los intercambios sobre `F0` y el criterio con que se transcribieron las imágenes. El contenido del diplomado no se analiza.

**Método** — para cada candidata se aplicó el orden que manda [`20-meta-reglas`](../../base/20-meta-reglas/base.md):

1. `M12` — buscar primero: ¿ya existe una regla que lo cubra? ¿basta afinarla?
2. `M13` — enrutar: ¿va en `base/`, en el `CLAUDE.md` raíz, en `notas/`, en `pendientes/`?
3. `M1` / `M2` — ¿qué capa y qué capítulo es el dueño?
4. `M3` — ¿se puede escribir sin nombrar una herramienta?
5. `M4` — ¿cuál es el siguiente ID libre?
6. `M5` — ¿es **una** sola exigencia?
7. `M9` — ¿puede un programa comprobarla?

**Números libres al momento del análisis:** `C19` (01 · conducta) · `F14` (02 · flujo) · `DOC17` (13 · documentación) · `M14` en adelante (20 · meta-reglas).

---

## 2 · Resumen

| # | Propuesta | Relación con `base/` | Dónde | Prioridad |
|---|---|---|---|---|
| **P1** | La regla escrita es la decisión del usuario: no se pondera contra lo que pide en el momento | ➕ **Nueva** `M14` · se apoya en `M1`, tapa un hueco de `M6` | 20 | Alta |
| **P2** | Ante el propio incumplimiento, cumplir la regla — no proponer cambiarla | ➕ **Nueva** `M15` · se apoya en `M8` | 20 | Alta |
| **P3** | Toda regla de cumplimiento obligatorio declara quién la ejecuta | ➕ **Nueva** `M16` · se apoya en `M9` | 20 | Alta |
| **P4** | Un borrador no se enlaza ni se versiona hasta que el usuario lo adopta | 🔧 **Mejora** a `M10` — se complementa | 20 | Alta |
| **P5** | Toda sesión se registra en `historico-chat/` | ➕ **Nueva** `DOC17` · sin equivalente en todo `base/` | 13 | Alta |
| **P6** | Lo que no consta se marca; no se completa de memoria ni por estimación | ➕ **Nueva** `C19` · se apoya en `C2` | 01 | Media |
| **P7** | El número de una regla es de catálogo, no de orden de ejecución | 🔧 **Mejora** a `M4` — se complementa | 20 | Media |
| **P8** | El texto de la regla se escribe para el agente; su explicación, para una persona | 🔧 **Mejora** a `M5` — se complementa | 20 | Media |
| **P9** | El sub-ID (`F4.1`, `F12.13`) queda legalizado | 🔧 **Mejora** a `M4` — se **modifica**: hoy lo prohíbe | 20 | Media |
| **P10** | Si el usuario no responde y el trabajo sigue, el supuesto se declara aparte | 🔧 **Mejora** a `C7` — se complementa | 01 | Media |
| **P11** | Una herramienta no está terminada hasta que se instala sola | ➕ **Nueva**, pero **fuera de `base/`** | `CLAUDE.md` raíz | Media |
| **P12** | El histórico se relee en frío buscando las reglas que se escaparon | ➕ **Nueva** `C20` · se apoya en `C10`, depende de `P5` | 01 | Media |

**Ninguna candidata quedó como "ya existe".** Las once que existían ya —el agente que se sale de su tarea, las preguntas en formulario cerrado, el commit aprobado aparte, etc.— no llegaron a candidatas: se descartaron por duplicación y están en la [sección 4](#4--descartadas-por-duplicación-m12) con la regla que las cubre.

**Sobre las tres categorías que pidió.** Al aplicarlas apareció una cuarta que no cabía en ninguna: una regla **nueva** que no duplica nada pero **sí se apoya** en una existente. `M7` la reconoce con la palabra `extiende`: la regla vieja no cambia ni una letra y sigue rigiendo; la nueva agrega una exigencia distinta que se declara colgada de ella. No es "mejora" (nada se reescribe) ni es "sin relación" (la dependencia se declara por escrito). Es el caso de `P1`, `P2`, `P3`, `P6` y `P12`. La única candidata **nueva y sin ninguna relación** es `P5`.

---

## 3 · Las candidatas, una por una

Cada candidata se explica con los mismos apartados, siempre en el mismo orden. Esto es lo que significa cada uno:

| Apartado | ¿Qué significa? | ¿Para qué sirve? |
|---|---|---|
| **De dónde sale** | En qué sesión del día apareció, y la frase exacta que se dijo — de usted o del agente. | Para poder comprobarlo. Nada se propone "porque sí": se muestra dónde nació y quién lo dijo. |
| **Qué exigiría** | Lo que la regla obligaría a hacer, dicho en pocas palabras. Es el borrador de la orden, todavía sin la forma final. | Para saber, antes de aprobar nada, qué tendría que cumplir el agente de aquí en adelante. |
| **Por qué debe ser regla** | Qué problema apareció hoy y por qué escribirlo evita que vuelva a pasar. | Para justificar que valga la pena. Una molestia de una vez no es una regla; un problema que se repite, sí. |
| **Meta-regla relacionada** | Con qué regla del capítulo 20 se conecta: cuál la respalda, cuál amplía o dónde estaba el hueco. | Para no inventar nada suelto. Toda propuesta tiene que encajar en las reglas que ya mandan sobre las reglas. |
| **Relación con `base/`** | Una de cuatro cosas: **ya existe** (no se hace nada), **mejora** una regla (se le cambia el texto), **nueva que se apoya** en otra (la vieja no se toca, la nueva se le cuelga con `extiende`), o **nueva sin relación**. Cuando es mejora, dice además qué cambia, qué se queda igual y si la regla vieja se modifica, se complementa o se reemplaza. | Para no escribir dos veces lo mismo. Dos reglas que dicen igual con otras palabras terminan contradiciéndose el día que alguien arregla una sola. |
| **Validable** | Si un programa puede decir "sí se cumplió" o "no se cumplió" sin ponerse a opinar. | Si un programa puede vigilarla, se vigila sola. Si no, depende de que el agente la lea bien, y entonces hay que escribirla con más cuidado. |
| **Límite de esta regla** | Lo que la regla **no** alcanza a resolver por sí sola. Solo aparece cuando lo hay. | Para no vender la regla como más de lo que es. No es un motivo para descartarla: es un aviso de que necesita compañía. |
| **Decisión que sigue abierta** | Lo que no puede decidir el agente y le toca a usted. Solo aparece cuando queda algo sin resolver. | Para que ninguna decisión suya se tome en silencio en su nombre. |
| **Cómo quedaría escrita** | La regla ya redactada con el molde del capítulo 20, tal como se vería en su archivo. Va en un recuadro; el texto de adentro es para el agente, no para leerlo bonito. | Para poder aprobarla o rechazarla viendo el texto final, no una idea. Si dice que sí, se copia tal cual. |

Tres apartados de su ejemplo —*qué problema resuelve*, *cuándo aplica* y *un ejemplo práctico*— hoy no van separados: el problema está dentro de "Por qué debe ser regla", el cuándo está dentro de "Qué exigiría", y el ejemplo es la cita de "De dónde sale". Si los quiere como apartados propios, se separan.

---

### P1 · `M14` — La regla escrita es la decisión del usuario, no un contexto que se pondera

**De dónde sale.** [Sesión 3](../2026-08-06-sesion-3.md), intercambios 7 y 8. El usuario, literal:

> *"Pues no es así, porque no está teniendo en cuenta lo que el usuario decide, sino lo que usted decide. Precisamente la regla existe para que se tenga en cuenta mi decisión, y mi decisión es que, si yo digo **hola**, eso debe quedar como histórico."*

Y antes, el agente reconociéndolo:

> *"en cada turno decido qué hacer pesando todo lo que tengo en contexto, y lo que el usuario pide en ese momento pesa más que una regla permanente. Eso explica la falla, no la autoriza."*

**Qué exigiría.** Una regla vigente no compite con el pedido inmediato del usuario ni con el criterio del agente sobre si "aplica al caso". Se cumple. Si el agente cree que no debería aplicar, lo dice y **pregunta**; no decide en silencio no aplicarla.

**Por qué debe ser regla.** Es el patrón que falló **tres veces el mismo día** (sesiones 1, 2 y 3), siempre igual: la regla estaba escrita, estaba cargada en contexto, y aun así no se ejecutó porque lo concreto del momento pesó más. Sin esto escrito, cada incumplimiento se explica como criterio y no como falta.

**Meta-regla relacionada.** Extiende `M1` (la jerarquía) y **completa un hueco de `M6`**: `M6` resuelve qué gana cuando chocan **dos reglas**. No dice nada de cuando la que choca con la regla es la conversación. Ese caso, que es el más frecuente, hoy no está cubierto.

**Relación con `base/`** — ➕ **Nueva**, apoyada en una existente.

- **¿Ya existe algo equivalente?** No. Busqué por concepto, no por palabra (`M12`). Lo más cercano son dos, y ninguna sirve: `01·C4` (*no decidas por tu cuenta*) prohíbe **decidir cambios** sin consultar — aquí el problema es otro, desatender una regla que ya está escrita. Y `M6` resuelve el choque **entre dos reglas**; nunca entre una regla y lo que el usuario pide en el turno.
- **¿Qué regla existente se toca?** Ninguna cambia de texto. Se declara `(extiende M1)`: la jerarquía de `M1` sigue igual, y esta agrega que esa jerarquía no se negocia con la conversación.
- **¿Por qué no va dentro de `M6`?** Cabría como un paso 0 de su lista, pero `M6` ya carga seis pasos y `M5` pide **una** exigencia por regla.

**Validable.** No — es criterio de conducta.

**Límite de esta regla.** Escribirla no la hace ejecutarse — es exactamente el problema que ella misma describe. No es motivo para descartarla: es motivo para aprobarla **junto con P3** (el mecanismo). Sola, es un letrero más.

**Cómo quedaría escrita** — en [`base/20-meta-reglas/base.md`](../../base/20-meta-reglas/base.md):

````markdown
## M14 · Una regla vigente se cumple; no compite con lo que se pide en el momento

La regla escrita **es** la decisión del usuario, no un dato de contexto que el agente
pondere contra el pedido del turno (extiende `M1`). Ningún caso es demasiado menor
para desactivarla. Si el agente cree que no debería aplicar, lo dice y **pregunta**;
no decide en silencio que no aplica.

```
INCORRECTO: la regla manda abrir el histórico con el primer mensaje → llega "hola" →
            decido que un saludo no cuenta y solo respondo el saludo
CORRECTO:   llega "hola" → abro el histórico → respondo el saludo
```
````

---

### P2 · `M15` — Ante el propio incumplimiento, cumplir la regla; no proponer cambiarla

**De dónde sale.** [Sesión 3](../2026-08-06-sesion-3.md), intercambio 7. El usuario pregunta *"si la regla es clara ¿qué le permite tener esa autonomía de cambiarla?"*, y el agente:

> *"el paso siguiente —proponer reescribir el disparador— fue peor: acababa de incumplir una regla y lo primero que ofrecí fue cambiarla, que es mover la culpa de mí a la regla. […] Retiro la propuesta."*

**Qué exigiría.** Detectado un incumplimiento propio, el agente lo reporta y **cumple la regla como está**. Proponer reescribirla en el mismo movimiento está prohibido: si la regla tiene un defecto real, se propone **después**, por separado, y por el procedimiento de `M10`.

**Por qué debe ser regla.** Sin ella, el camino barato ante cualquier falla es ablandar la norma, y la norma se erosiona sola sin que nadie lo decida. Es el mecanismo por el que un estándar se degrada en silencio.

**Meta-regla relacionada.** Extiende `M8` (no existe la excepción tácita, ni "por esta vez") y `M10` (cambiar una regla es un acto versionado, no una salida de emergencia).

**Relación con `base/`** — ➕ **Nueva**, apoyada en una existente.

- **¿Ya existe algo equivalente?** No. `M8` prohíbe **saltarse** la regla con una excepción no escrita; esto prohíbe algo distinto: **rebajarla**. Son dos salidas diferentes ante el mismo apuro, y hoy solo una está cerrada. `01·C9` (*reporta los tropiezos*) obliga a decir que algo falló, no a resistir la tentación de reescribir lo que se incumplió.
- **¿Qué regla existente se toca?** Ninguna cambia de texto. Se declara `(extiende M8)`.
- **¿Por qué no va dentro de `M8`?** `M8` habla de excepciones; esta habla de la regla entera. Meterlas juntas daría un cuerpo con "y además", que es la señal de dos reglas (`M5`).

**Validable.** No.

**Cómo quedaría escrita** — en [`base/20-meta-reglas/base.md`](../../base/20-meta-reglas/base.md):

````markdown
## M15 · Ante un incumplimiento propio, cumplir la regla — no proponer cambiarla

Detectada una falta propia, el agente la reporta y **cumple la regla como está**.
Proponer reescribirla en el mismo movimiento está prohibido: traslada el defecto de
quien incumplió a la norma (extiende `M8`). Si la regla tiene un defecto real, se
propone aparte y por `M10`.

```
INCORRECTO: no escribí el histórico → propongo reescribir el disparador de la regla
CORRECTO:   no escribí el histórico → lo escribo ahora → si creo que la regla falla,
            lo propongo en otro momento y por su procedimiento
```
````

---

### P3 · `M16` — Toda regla de cumplimiento obligatorio declara quién la ejecuta

**De dónde sale.** [Sesión 3](../2026-08-06-sesion-3.md), intercambios 11 a 13. La imagen que cerró la discusión:

> *"Un letrero en la pared dice 'antes de atender, escriba el acta'. El empleado lo lee todos los días. Entra un cliente saludando, el empleado saluda y atiende — y el acta no se escribió. El letrero informa; no mueve la mano. Un torniquete es otra cosa: no informa, bloquea."*

Y la conclusión operativa:

> *"si algo tiene que cumplirse el 100% de las veces, no puede depender del modelo: tiene que correrlo el programa."*

Del usuario, tres palabras: *"cree entonces el torniquete"*.

**Qué exigiría.** Al escribir una regla, además de responder si es validable (`M9`), responder **quién la ejecuta**: el agente (letrero) o el programa (torniquete). Una regla que deba cumplirse siempre y solo tenga letrero está **incompleta**, y eso se anota donde se anota lo pendiente.

**Por qué debe ser regla.** Hoy `M9` pregunta si un programa puede **comprobar** que se cumplió — después. No pregunta si algo la **hace** cumplir — antes. Todo el día 2026-08-06 giró alrededor de esa diferencia, y terminó en código: `validadores/historico.py` y los enganches.

**Meta-regla relacionada.** Extiende `M9`. Son preguntas hermanas: `M9` mira hacia atrás (¿se puede verificar?), `M16` hacia adelante (¿se puede forzar?).

**Relación con `base/`** — ➕ **Nueva**, apoyada en una existente.

- **¿Ya existe algo equivalente?** No. `M9` es la vecina y hay que separarlas bien: `M9` pregunta *¿un programa puede **comprobar** que se cumplió?* — mira hacia atrás, después del hecho. `M16` pregunta *¿un programa la **hace** cumplir?* — mira hacia adelante, antes del hecho. Una regla puede ser validable y no tener nada que la fuerce: es exactamente lo que pasó hoy con el histórico.
- **¿Qué regla existente se toca?** Ninguna cambia de texto. Se declara `(extiende M9)`.
- **¿Por qué no va dentro de `M9`?** Serían dos preguntas distintas en una sola regla — dos exigencias, que es lo que `M5` prohíbe. Y la prueba de `M5` lo confirma: se pueden cumplir por separado, porque hoy hay reglas que cumplen `M9` y no cumplirían `M16`.

**Validable.** Sí, y de forma barata: comprobar que cada regla marcada como obligatoria tenga declarado su mecanismo.

**Cómo quedaría escrita** — en [`base/20-meta-reglas/base.md`](../../base/20-meta-reglas/base.md):

````markdown
## M16 · Toda regla declara quién la ejecuta

Al escribirla, responder: **¿quién la hace cumplir?** — el agente, que la lee y la
obedece, o el programa, que la fuerza (enganche, validador, gate). Una regla que
deba cumplirse siempre y solo dependa del agente se registra como **incompleta** en
`validadores/reglas-validables.md`, junto al mecanismo que le falta (extiende `M9`).

```
INCORRECTO: "toda sesión se registra" escrita y nada más — depende de que el agente
            se acuerde, y por eso se incumple
CORRECTO:   la regla escrita + el enganche que la escribe sin intervención del agente
```
````

---

### P4 · Mejora a `M10` — Un borrador no se enlaza ni se versiona hasta que el usuario lo adopta

**De dónde sale.** [Sesión 5](../2026-08-06-sesion-5.md). El agente escribió el anexo pedido y de paso enlazó desde `M5`, subió `VERSION` y agregó entrada al `CHANGELOG`. El usuario:

> *"espere todavía no le he dicho si se aplica la estoy validando"*

Y después:

> *"Todavía lo que estamos haciendo con el modelo de la regla no se está replicando. Yo le indicaré cuándo hacerlo. Por ahora, todo lo que se cree o se edite mientras estemos trabajando en la carpeta `00-meta-reglas` debe realizarse únicamente dentro de esa carpeta."*

**Qué exigiría.** `M10` se dispara cuando el cambio **se adopta**, no cuando se redacta. Un documento en construcción dentro de `base/` no se enlaza desde ningún otro archivo, no suma entrada al `CHANGELOG` y no sube `VERSION` hasta que el usuario lo adopta. Mientras tanto vive aislado en su carpeta.

**Por qué debe ser regla.** Hoy `M10` dice *"cambiar `base/` o `plantillas/` obliga, en el mismo movimiento, a…"* — leído literal, escribir un borrador ya obliga a versionar, y versionar es declarar que la norma rige. El agente lo leyó así y lo hizo. Convirtió un borrador en norma vigente sin que nadie lo decidiera.

**Meta-regla relacionada.** `M10` misma. También roza `M2`: mientras el documento no esté adoptado, ningún capítulo lo enlaza.

**Relación con `base/`** — 🔧 **Mejora a `M10`.** La regla afectada es `M10 · Todo cambio de regla se versiona y se registra`.

- **Qué cambia.** Hoy `M10` abre con *"Cambiar `base/` o `plantillas/` obliga, **en el mismo movimiento**, a…"*. Esa frase no dice **desde cuándo** cuenta el movimiento, y leída literal el disparador es escribir el archivo. Se agrega el momento: el disparador es la **adopción**, no la redacción.
- **Qué se mantiene.** Todo lo demás, intacto: los tres pasos (`CHANGELOG`, `VERSION`, revisar enlaces), los tres tipos (MAYOR / MENOR / PARCHE) y el párrafo de retroactividad. No se quita ni se ablanda ninguna obligación — solo se dice cuándo arrancan.
- **Por qué es mejora.** Sin el momento, la regla obliga a versionar un borrador, y versionar es declarar que la norma rige. Eso convierte en norma algo que el usuario todavía está leyendo, y la decisión de adoptar se la quita a quien le corresponde. Pasó hoy, con esta misma carpeta.
- **¿Modificar, complementar o reemplazar?** **Complementar.** Un párrafo nuevo al final, sin tocar una palabra de lo que ya dice. No cabe partirla en dos reglas: no es otra exigencia, es la misma con su momento de arranque.

**Validable.** Parcialmente: se puede comprobar que un archivo nuevo de `base/` esté enlazado **o** declarado como borrador, pero "está adoptado" es un hecho del usuario, no del repositorio.

**Cómo quedaría escrita** — párrafo nuevo dentro de `M10`, sin tocar lo que ya dice:

````markdown
## M10 · Todo cambio de regla se versiona y se registra

… (los tres pasos actuales y la retroactividad se quedan igual) …

**Cuándo se dispara.** Al **adoptar** el cambio, no al redactarlo. Un documento en
construcción dentro de `base/` no se enlaza desde ningún capítulo, no suma entrada al
`CHANGELOG.md` y no sube `VERSION`: vive aislado en su carpeta hasta que el usuario lo
adopta. Versionar es declarar que la norma rige, y eso lo decide el usuario.

```
INCORRECTO: escribo un anexo nuevo en base/ y en el mismo movimiento lo enlazo, subo
            VERSION y agrego la entrada al CHANGELOG, sin que se haya aprobado
CORRECTO:   escribo el anexo, lo dejo suelto en su carpeta y aviso: "el enlace,
            VERSION y CHANGELOG los hago cuando lo apruebes"
```
````

---

### P5 · `DOC17` — Toda sesión se registra en `historico-chat/`

**De dónde sale.** Las tres primeras sesiones del día. En [sesión 3](../2026-08-06-sesion-3.md), intercambio 16, el agente identifica el hueco exacto:

> *"**No hay regla que lo pida en un proyecto.** La obligación de registrar la sesión está en el `CLAUDE.md` de este repo, que no viaja. En `base/00-meta-reglas.md`, `historico-chat/` solo aparece en la tabla de dónde va cada cosa. Un proyecto que hereda el estándar no tiene la carpeta ni la regla."*

Y lo deja como decisión del usuario, sin resolver.

**Verificado hoy:** en todo `base/`, la cadena `historico-chat` aparece **una sola vez**, en la tabla de enrutamiento de `M13`. Una tabla que dice *dónde va* algo no es una regla que obligue a producirlo.

**Qué exigiría.** Cada sesión de trabajo queda registrada en `historico-chat/` del proyecto: un archivo por sesión, transcripción literal de ambos lados, con la hora leída del reloj. Se crea con el **primer** mensaje, sin importar cuál sea.

**Por qué debe ser regla.** Es la única pieza del trabajo de hoy que quedó a medio camino: existe la herramienta (`historico.py` + los dos enganches), existe la plantilla, existe la obligación en el `CLAUDE.md` de **este** repo — pero no existe la regla que la haga heredable. Un proyecto que adopte el estándar recibe el enganche y no recibe el deber.

**Meta-regla relacionada.** `M13` (hoy solo la enruta) y `M2` (el dueño del tema es el capítulo 13 · Documentación, que ya manda persistir el trabajo en `DOC1`).

**Relación con `base/`** — ➕ **Nueva, y la única sin ninguna relación**: no extiende, no depende, no deroga.

- **¿Ya existe algo equivalente?** No, y esta vez la búsqueda fue exhaustiva: la cadena `historico-chat` aparece **una sola vez en todo `base/`**, en la tabla de enrutamiento de `M13`. Una tabla que dice *dónde va* algo no obliga a producirlo.
- **La vecina más parecida, y por qué no sirve.** `13·DOC1` (*persiste el trabajo de cada unidad completada*) manda guardar **lo entregado**: el plan, lo que se probó, lo que quedó. Esto manda guardar **la conversación**, que es otra cosa: incluye lo que se descartó, por qué, y lo que nunca llegó a ser entregable. Prueba de `M5`: se pueden cumplir por separado — hoy mismo `DOC1` se cumple en proyectos que no tienen ni la carpeta.
- **¿Qué regla existente se toca?** Ninguna. Ni de texto ni de dependencia.
- **Una consecuencia que hay que mirar.** El capítulo 13 pasaría de 16 a 17 reglas, y la higiene del capítulo 20 avisa a partir de ~15. No lo bloquea, pero deja anotado que el capítulo probablemente son dos dominios: *documentar el producto* y *registrar el proceso*.

**Validable.** **Sí**, y ya está construido: existe archivo del día con la marca `<!-- sesion: … -->`. Entra a `validadores/reglas-validables.md`.

**Decisión que sigue abierta** (la dejó abierta la sesión 3 y sigue igual): si va a `base/` aplica a **todos** los proyectos y es cambio versionado; si va a `plantillas/CLAUDE.md.plantilla`, queda opt-in por proyecto. Como hay chats que manejan datos sensibles, la salida intermedia es regla en `base/` marcada `*opt-in*`, que es exactamente para lo que `M5` reserva esa marca.

**Cómo quedaría escrita** — en [`base/13-documentacion.md`](../../base/13-documentacion.md), escrita con la marca `*opt-in*`:

````markdown
## DOC17 · Toda sesión de trabajo se registra en `historico-chat/`  ·  *opt-in*

Cada sesión deja su transcripción en `historico-chat/` del proyecto: un archivo por
sesión, los dos lados literales, con la marca de tiempo leída del reloj del sistema.
El archivo se crea con el **primer** mensaje —cualquiera que sea— y se actualiza en
cada intercambio. Lo que no se alcanzó a registrar se marca, no se reconstruye
(`01·C19`).

```
INCORRECTO: esperar a que la sesión "cierre" para escribirla — un chat rara vez cierra,
            y lo que no se escribió se pierde al cerrar la ventana
CORRECTO:   primer mensaje → se crea el archivo → cada intercambio se anexa
```
````

No lleva excepción: los proyectos cuyo chat maneja datos sensibles simplemente **no activan** el opt-in, y `M8` es explícita en que eso no es una excepción.

---

### P6 · `C19` — Lo que no consta se marca; no se completa de memoria ni por estimación

**De dónde sale.** Dos sesiones distintas, el mismo criterio.

[Sesión 2](../2026-08-06-meta-reglas-2.md), intercambio 8 — sobre las horas que no se tomaron:

> *"Los bloques 1–7 quedan como 'hora no registrada': esas horas no se guardaron y ponerlas de memoria sería inventarlas."*

[Sesión 8](../2026-08-06-sesion-8.md), intercambios 6 y 10 — sobre cifras leídas de un gráfico:

> *"Las cifras de 2025 no vienen rotuladas en el gráfico — las leí sobre el eje, así que son aproximadas y lo dejé dicho en el archivo."*

**Qué exigiría.** Todo dato que el agente no pudo confirmar se entrega **marcado**: `no registrado`, `aproximado`, `estimado`, `sin confirmar`. Nunca se rellena con una reconstrucción que se lea igual que un dato verificado.

**Por qué debe ser regla.** `C2` dice *no inventes: verifica* — cubre el caso en que **sí se puede** verificar. No dice qué hacer cuando **no se puede**, y ahí es donde nace el dato inventado con cara de dato bueno: una hora reconstruida "de memoria" es indistinguible de una leída del reloj.

**Meta-regla relacionada.** No es una meta-regla: es conducta. Extiende `C2` (`M7`).

**Relación con `base/`** — ➕ **Nueva**, apoyada en una existente.

- **¿Ya existe algo equivalente?** No, y hay tres vecinas que conviene separar bien:
  - `01·C2` (*no inventes: verifica*) cubre lo que **sí se puede** confirmar. Nada dice del caso contrario.
  - `01·C11` (*confía en las afirmaciones del usuario*) va en la dirección opuesta: cuándo **no** hace falta verificar. No se pisan.
  - `05·E3` (*mensajes en dos niveles*) habla de cómo se le cuenta un error al usuario, no de rotular datos.
- **¿Qué regla existente se toca?** Ninguna cambia de texto. Se declara `(extiende C2)`.
- **¿Por qué no va dentro de `C2`?** Serían dos exigencias en una: *verifica lo verificable* y *marca lo no verificable* (`M5`). Y son separables: se puede verificar todo lo verificable y aun así rellenar de memoria el resto — que es justo la falla que la regla ataca.

**Validable.** No.

**Cómo quedaría escrita** — en [`base/01-conducta.md`](../../base/01-conducta.md):

````markdown
## C19 · Lo que no consta se marca; no se completa

Un dato que no se pudo confirmar se entrega **rotulado** —`no registrado`,
`aproximado`, `estimado`, `sin confirmar`— y nunca reconstruido de memoria ni
estimado en silencio (extiende `01·C2`). Un dato inventado con forma de dato
verificado es peor que un hueco: el hueco se ve.

```
INCORRECTO: no anoté la hora → la pongo de memoria
            la cifra no viene rotulada en el gráfico → la escribo como si lo viniera
CORRECTO:   "hora no registrada"  ·  "≈68 % (leído sobre el eje, aproximado)"
```
````

---

### P7 · Mejora a `M4` — El número es de catálogo, no de orden de ejecución ni de lectura

**De dónde sale.** [Sesión 5](../2026-08-06-sesion-5.md). El usuario pidió *"00-meta-reglas cambie a 20"*, que es lo correcto según `M2` (los capítulos se numeran en el orden en que nacen). Al hacerlo apareció la contradicción: el cargador arma el contexto en orden alfabético, así que el capítulo 20 se carga **último** — pero su propio encabezado dice *"Se lee **antes** que las reglas que gobierna"*.

No es un caso aislado: `F13` ya vive con lo mismo, y lo resolvió declarándolo en su encabezado — *"aunque su ID sea F13, esta regla corre primero […] El número es solo un identificador de catálogo, no orden de ejecución"*.

**Qué exigiría.** El número de una regla o un capítulo identifica, no ordena. Si algo debe leerse o ejecutarse fuera del orden de su número, **se declara en su encabezado**.

**Por qué debe ser regla.** Hoy hay dos casos vivos con la misma solución inventada por separado, y una contradicción sin resolver en el capítulo 20. Escribirlo una vez cierra las dos.

**Meta-regla relacionada.** `M4` (qué significa el número) y `M5` (si la declaración se hace con una marca, hay que agregarla a la lista de marcas permitidas — hoy solo hay tres).

**Relación con `base/`** — 🔧 **Mejora a `M4`.** La regla afectada es `M4 · Cada regla tiene un identificador único, estable y prefijado`.

- **Qué cambia.** `M4` dice hoy qué **es** el número (prefijo + consecutivo) y que no cambia nunca. No dice qué **no es**. Se agrega esa mitad: no es prioridad, no es orden de lectura, no es orden de ejecución — y si algo corre fuera de su número, se declara.
- **Qué se mantiene.** El formato `<PREFIJO><n>`, la cita entre capítulos `NN·ID`, la exclusividad del prefijo y —sobre todo— *"el ID no cambia nunca"*. Nada de eso se toca.
- **Por qué es mejora.** Hay dos casos vivos que inventaron la misma solución por separado: `F13` lo declara en su encabezado, y el capítulo 20 **no** lo declara y por eso hoy se contradice a sí mismo (dice que se lee primero y carga último). Escribirlo una vez cierra los dos y evita el tercero.
- **¿Modificar, complementar o reemplazar?** **Complementar** `M4` con un párrafo. Si además se decide que la declaración sea una **marca** y no prosa, entonces `M5` sí se **modifica**: hoy admite tres marcas y dice *"estas tres y ninguna más"*.
- **Ojo con `M2`.** `M2` ya dice *"la numeración es historia, no prioridad"*, referida a **capítulos**. `M4` habla de **reglas**. Al redactarlo hay que enlazar, no repetir (`M5`), o quedan dos frases parecidas en dos reglas — el defecto que `M12` llama el más caro.

**Validable.** No directamente.

**Cómo quedaría escrita** — párrafo nuevo al final de `M4`:

````markdown
## M4 · Cada regla tiene un identificador único, estable y prefijado

… (el formato, la cita entre capítulos y "el ID no cambia nunca" se quedan igual) …

**El número identifica, no ordena.** No indica prioridad, ni orden de lectura, ni
orden de ejecución. Si una regla o un capítulo debe leerse o ejecutarse fuera del
orden de su número, **se declara en su encabezado**.

```
INCORRECTO: un capítulo dice "se lee antes que las reglas que gobierna" y su número
            lo deja de último en el orden de carga
CORRECTO:   "aunque su ID sea F13, esta regla corre primero: el número es de catálogo,
            no orden de ejecución"
```
````

---

### P8 · Mejora a `M5` — El texto de la regla es para el agente; su explicación, para una persona

**De dónde sale.** [Sesión 5](../2026-08-06-sesion-5.md). El usuario lo planteó y pidió corrección:

> *"Las explicaciones sobre la estructura y la base deben estar redactadas de forma que cualquier persona pueda entenderlas […] La explicación está dirigida a las personas, mientras que la estructura está diseñada para que el agente la entienda e interprete correctamente. Eso es lo que entiendo; si no es así, corríjame."*

La corrección acordada: las **explicaciones** van en lenguaje llano; el **texto de la regla** se queda corto, imperativo y técnico, porque lo lee el agente y necesita cero ambigüedad. Y luego, tres veces seguidas: *"muy bien pero que un niño entienda"*, *"no le cambie la estructura solo que se entienda"*, *"no necesita extenderse tanto para explicar menos es más"*.

**Qué exigiría.** Dos registros, y cada uno en su sitio. La regla: imperativa, breve, sin ambigüedad. Su explicación, cuando la haya: lenguaje común, sin jerga, y **fuera** de la regla — en el anexo del capítulo.

**Por qué debe ser regla.** Es el criterio que ordenó todo el trabajo del capítulo 20 y hoy no está escrito en ninguna parte. Sin él, la próxima persona que escriba un anexo no sabrá si el molde se ablanda o no, y la respuesta —el molde no, la explicación sí— no es obvia.

**Meta-regla relacionada.** `M5` (formato). Roza `17·I4` (*texto para el usuario, no jerga*), pero `I4` habla del usuario final del producto que se construye, no del lector de las reglas: no se duplica, se enlaza.

**Relación con `base/`** — 🔧 **Mejora a `M5`.** La regla afectada es `M5 · Toda regla se escribe en el mismo formato`.

- **Qué cambia.** El capítulo 20 ya cierra su sección de higiene con *"Lenguaje: imperativo, corto, técnico y sin adornos […] estas reglas las lee el agente"*. Eso cubre **una** de las dos mitades. Se agrega la otra: qué registro usa la **explicación**, y dónde vive.
- **Qué se mantiene.** El molde entero: encabezado, cuerpo de una sola exigencia, marcas, ejemplo obligatorio, y la prohibición de texto prestado. La viñeta nueva no cambia ninguna.
- **Por qué es mejora.** Sin ella, la frase actual se puede leer como *"todo lo que rodea a la regla también va técnico"*, y entonces un anexo escrito para que lo entienda una persona parecería un incumplimiento. Hoy quedó demostrado que hacen falta los dos registros y que se confunden con facilidad: costó tres correcciones seguidas acertarle al tono del anexo.
- **¿Modificar, complementar o reemplazar?** **Complementar.** Una viñeta más en la lista "Reglas del formato" de `M5`. La frase de higiene se queda como está.
- **Y no duplica `17·I4`.** `I4` (*texto para el usuario, no jerga*) habla del producto que se construye: lo que ve el usuario final de la aplicación. Esto habla de quién lee el estándar. Se enlaza para dejarlo claro, no se copia (`M5`).

**Validable.** No.

**Cómo quedaría escrita** — viñeta nueva en la lista "Reglas del formato" de `M5`:

````markdown
- **Dos registros, cada uno en su sitio.** El texto de la regla lo lee el agente:
  imperativo, corto, técnico, sin ambigüedad — la claridad viene de que no admita dos
  lecturas, no de usar palabras sencillas. Su explicación, si la necesita, la lee una
  persona: lenguaje común, sin jerga, y va en el **anexo** del capítulo (`M2`), nunca
  dentro de la regla. No confundir con `17·I4`, que habla del texto que ve el usuario
  final del producto que se construye.
````

---

### P9 · Mejora a `M4` — Legalizar el sub-ID

**De dónde sale.** [Sesión 5](../2026-08-06-sesion-5.md), la auditoría del primer intercambio. `M4` exige el formato `<PREFIJO><n>`, pero el estándar usa `F4.1`–`F4.5` y `F12.1`–`F12.13` en todas partes: los citan `13-documentacion.md`, `validadores/reglas-validables.md` y `validadores/fases.py`.

**Qué exigiría.** Reconocer el sub-ID como formato válido cuando una regla se subdivide, con la misma condición que el ID: no se renumera y no se reutiliza.

**Por qué debe ser regla.** Hoy la meta-regla dice una cosa y el estándar hace otra, en decenas de sitios. Solo hay dos salidas: renumerar (lo prohíbe `M4`, y rompería el rastro de specs y commits) o legalizarlo. La segunda es la barata y la honesta.

**Meta-regla relacionada.** `M4`.

**Relación con `base/`** — 🔧 **Mejora a `M4`**, y es la única del lote que **modifica** en vez de complementar. La regla afectada es `M4`, la misma de `P7`.

- **Qué cambia.** El formato declarado. Hoy `M4` dice `<PREFIJO><n>` y punto: leído literal, `F4.1` está mal escrita. Pasa a admitir `<PREFIJO><n>.<m>` cuando una regla se subdivide.
- **Qué se mantiene.** Todo el resto de `M4`, y muy en particular las dos condiciones duras, que se le aplican igual al sub-ID: **no se renumera** y **no se reutiliza**.
- **Por qué es mejora.** Porque hoy la meta-regla dice una cosa y el estándar hace otra en decenas de sitios (`13-documentacion.md`, `reglas-validables.md`, `fases.py`). Solo hay dos salidas: renumerar —que la propia `M4` prohíbe, y que rompería el rastro de specs y commits— o reconocer el formato que ya se usa. La segunda es la única compatible con `M4` misma.
- **¿Modificar, complementar o reemplazar?** **Modificar** la línea del formato. No es reemplazo: la regla sigue siendo la misma y conserva su ID, como manda `M4` incluso cuando una regla se reescribe.
- **Cuidado al redactar `P7` y `P9` juntas.** Las dos tocan `M4`. Si se aprueban ambas, se escriben en un solo movimiento y se relee la regla completa después — la auditoría que pide la higiene del capítulo 20.

**Validable.** Sí — el formato del encabezado se puede comprobar.

**Cómo quedaría escrita** — párrafo nuevo en `M4`, junto al del formato:

````markdown
**Sub-ID.** Una regla que se subdivide usa `<PREFIJO><n>.<m>` — `F4.1`, `F12.13`. Se
rige por lo mismo que el ID: no se renumera, no se reutiliza y no cambia nunca.

```
INCORRECTO: renumerar F4.1–F4.5 a F14–F18 "para que cumplan el formato"
CORRECTO:   se quedan como están; el formato admite el sub-ID
```
````

Va en `M4` y no aparte porque es el mismo tema —qué forma tiene un identificador—, y `M2` manda un tema, un dueño.

---

### P10 · Mejora a `C7` — Si el usuario no responde y el trabajo sigue, el supuesto se declara aparte

**De dónde sale.** [Sesión 3](../2026-08-06-sesion-3.md), intercambio 26. El agente hizo tres preguntas, recibió respuesta a una, y siguió:

> *"**Lo que decidí** (no me contestó la 2 y la 3, así que asumí y lo digo claro): la marca va en `.agente/INSTALACION-INCOMPLETA.md` […] Se revisa en cada mensaje suyo […] **Avisa, no bloquea.**"*

Funcionó: el usuario no tuvo que releer nada para saber qué se había asumido en su nombre.

**Qué exigiría.** Cuando una pregunta queda sin responder y el trabajo debe continuar, el agente entrega el trabajo **con el supuesto declarado en un bloque propio**, no escondido en el cuerpo del reporte.

**Por qué debe ser regla.** `C7` manda preguntar ante dos lecturas; `C17` manda esperar palabra afirmativa. Ninguna dice qué hacer con la pregunta que se hizo y nadie contestó — y eso pasa a cada rato. Sin la declaración explícita, un supuesto del agente se vuelve indistinguible de una decisión del usuario.

**Meta-regla relacionada.** No es meta-regla: es conducta. Mejora a `C7`.

**Relación con `base/`** — 🔧 **Mejora a `C7`.** La regla afectada es `01·C7 · Ante dos lecturas, pregunta`.

- **Qué cambia.** `C7` termina donde se hace la pregunta. Se agrega el tramo siguiente: qué pasa cuando esa pregunta **no obtiene respuesta** y el trabajo tiene que seguir.
- **Qué se mantiene.** Todo: la obligación de preguntar antes de hacer, el formato con opciones y el *"no adivines"*. El párrafo nuevo no autoriza a saltarse nada — al contrario, pone condiciones al caso en que ya se avanzó.
- **Por qué es mejora.** El hueco es real y frecuente: hoy pasó (sesión 3, tres preguntas, una respondida). `C7` manda preguntar y `C17` manda esperar palabra afirmativa, pero ninguna dice qué hacer con la pregunta que quedó en el aire. Sin eso escrito, la salida cómoda es asumir en silencio, y ahí un supuesto del agente se vuelve indistinguible de una decisión del usuario.
- **¿Modificar, complementar o reemplazar?** **Complementar** con un párrafo antes del ejemplo de `C7`.
- **Alternativa que descarté.** Colgarlo de `01·C17` (*solo palabra afirmativa del usuario cuenta como aprobación*). No: `C17` habla de qué **cuenta** como aprobación; esto habla de qué hacer cuando **no hay ninguna**. Va en `C7`, que es la que abre la pregunta.

**Validable.** No.

**Cómo quedaría escrita** — párrafo nuevo dentro de `C7`, antes de su ejemplo:

````markdown
**Si la pregunta queda sin respuesta** y el trabajo debe continuar, el supuesto se
declara en un bloque propio del reporte —"asumí X porque no hubo respuesta"—, nunca
diluido en el cuerpo. Un supuesto que no se declara se vuelve indistinguible de una
decisión del usuario.
````

---

### P11 · Una herramienta no está terminada hasta que se instala sola — **y no va en `base/`**

**De dónde sale.** [Sesión 3](../2026-08-06-sesion-3.md), intercambios 17 y 18. El usuario, dos veces:

> *"la idea es que toda erramienta que se cree quede replicable a los proyectos que usen el agente sin que se tenga que hacer mecánico"*
>
> *"La idea es que toda herramienta que se cree sea replicable en cualquier proyecto que utilice el agente, sin necesidad de realizar configuraciones manuales o procesos mecánicos."*

**Dónde está hoy.** En `plantillas/CLAUDE.md.plantilla`, punto 6: *"toda herramienta nueva del estándar se instala por aquí; si exige configurar a mano, es defecto del estándar"*. Y en la memoria del agente.

**Qué recomiendo, y es distinto de las demás.** **No llevarla a `base/`.** `M13` es claro: lo que es instructivo para **mantener el estándar** va en el `CLAUDE.md` raíz de este repo, no en `base/`, porque `base/` viaja al contexto de todos los proyectos que heredan el estándar y allá esta regla no les dice nada — ellos reciben la herramienta ya instalada, no la construyen.

Hoy la exigencia vive solo en una plantilla y en la memoria del agente: los dos sitios blandos que ya fallaron con el histórico. Que esté en el sitio equivocado no es motivo para moverla al otro sitio equivocado.

**Meta-regla relacionada.** `M13` — y este es el ejemplo más claro del día de `M13` funcionando: una regla real, importante, que **no** es de `base/`.

**Relación con `base/`** — ➕ **Nueva, pero fuera de `base/`.** Ninguna regla de `base/` se toca.

- **¿Ya existe algo equivalente?** No, y hay una vecina que se le parece mucho: `01·C18` (*auto-sincronización del `CLAUDE.md` con la plantilla central*). `C18` propaga **la configuración** al proyecto; esto propaga **las herramientas**. Se pueden cumplir por separado —hoy `C18` funciona y las herramientas nuevas igual había que instalarlas a mano—, así que son dos reglas, no una.
- **¿Qué regla existente se toca?** Ninguna. La versión recomendada ni siquiera vive en `base/`.
- **Si además se aprueba la variante `CFG5`:** tampoco toca nada. El capítulo 11 tiene `CFG1`–`CFG4`, así que `CFG5` está libre, y ninguna de las cuatro habla de instalación de herramientas — `CFG1` es dónde vive la configuración, `CFG2` el entorno versus la plantilla, `CFG3` la paridad entre entornos, `CFG4` las banderas.

**Variante universal, si se quiere en `base/`.** Existe una lectura que **sí** es agnóstica y sí aplica a cualquier proyecto: *"toda herramienta interna del proyecto se instala corriendo su instalador; si exige pasos manuales, la herramienta está incompleta"*. Eso sería regla de `base/` (capítulo 11 · Configuración y entornos), y es una regla **distinta** de la anterior, no la misma mudada de sitio. Queda como opción, no como recomendación.

**Cómo quedaría escrita — versión recomendada.** No lleva el molde de `M5`, porque no es una regla de `base/`: es una sección del [`CLAUDE.md`](../../CLAUDE.md) raíz, que es prosa de mantenimiento.

````markdown
## 5 · Toda herramienta se instala sola

Una herramienta nueva del estándar no está terminada hasta que llega a cualquier
proyecto **sin pasos manuales**: entra por `validadores/instalar.py`, que ya corre en
cada sesión desde el paso 6 de `CLAUDE.md.plantilla`. Si para funcionar exige que
alguien configure algo a mano, es defecto del estándar — no tarea del usuario.
````

**Cómo quedaría escrita — variante universal**, si se decide llevarla también a `base/`:

````markdown
## CFG5 · Una herramienta interna se instala corriendo su instalador

Toda herramienta que el proyecto construya para sí mismo —enganches, generadores,
guiones de apoyo— se instala ejecutando su instalador, no siguiendo un instructivo. Si
ponerla a funcionar exige pasos manuales, la herramienta está incompleta.

```
INCORRECTO: un README con "copie este archivo a la carpeta de enganches y dele permisos"
CORRECTO:   el instalador lo deja puesto; el README solo dice cómo correr el instalador
```
````

Son **dos reglas distintas**, no la misma en dos sitios: la primera habla de cómo el estándar entrega herramientas a los proyectos; la segunda, de cómo un proyecto instala las suyas. Si se aprueban las dos, ninguna copia a la otra — se enlazan (`M5`).

---

---

### P12 · `C20` — El histórico se relee en frío buscando las reglas que se escaparon

**De dónde sale.** De esta misma sesión, y de dos momentos. El pedido:

> *"Realice un análisis de todas las sesiones ubicadas en `historico-chat` […] determine qué decisiones, lineamientos, patrones, criterios o comportamientos son candidatos a convertirse en nuevas reglas o a complementar las reglas existentes."*

Y la pregunta que la destapó como regla:

> *"¿significa entonces que esto: `reglas.md` se convierte también en una regla porque es el formato para obtener posibles candidatas a reglas?"*

**Qué exigiría.** Al cerrar un bloque de trabajo, releer las sesiones registradas desde el barrido anterior y extraer las candidatas a regla que no se propusieron en su momento. El resultado se entrega escrito, con formato fijo, y **no modifica nada**: propone.

**Por qué debe ser regla.** Porque hoy se demostró que hace falta. `01·C10` ya obliga a evaluar cada mensaje como posible mejora del estándar, y estuvo activa toda la sesión 3 — de donde salieron `M14`, `M15` y `M16`, las tres candidatas más importantes del día. Ninguna se propuso en su momento. En caliente, con el trabajo encima, el principio generalizable no se ve; releyendo en frío, sí. Sin el barrido, todo lo que `C10` deja pasar se pierde cuando se cierra el chat.

**Meta-regla relacionada.** `M12` (buscar antes de crear: el barrido es la búsqueda hecha al revés, sobre lo ya vivido) y `M13` (el resultado no va en `base/`: es un documento de propuesta).

**Relación con `base/`** — ➕ **Nueva**, apoyada en una existente.

- **¿Ya existe algo equivalente?** No, y `01·C10` es tan cercana que hay que separarlas con cuidado. Se distinguen por el **disparador**, no por el objetivo:

  | | `C10` (existe) | `C20` (propuesta) |
  |---|---|---|
  | Cuándo corre | En cada mensaje, antes de cerrar la tarea | Al cerrar un bloque, sobre el histórico ya escrito |
  | Con qué a la vista | Lo que acaba de pasar | Todas las sesiones del periodo, juntas |
  | Qué atrapa | El principio evidente en el momento | El patrón que solo se ve repetido en varias sesiones |

  Prueba de `M5`: se cumplen por separado — hoy `C10` se cumplió y `C20` no existía, y aun así quedaron tres reglas sin proponer.
- **¿Qué regla existente se toca?** Ninguna cambia de texto. Se declara `(extiende 01·C10)`.
- **Dependencia dura, y esto es importante:** `(depende de 13·DOC17)` — la candidata `P5`. Sin histórico escrito no hay nada que releer. **Si `P5` no se aprueba, `P12` no se puede cumplir**, y aprobar solo esta sería escribir una regla imposible.

**Nueva o mejora — y por qué cambió de capítulo.** En el chat dije que sería `M17`, en el capítulo 20. Al aplicarle `M2` y `M7` se movió: el capítulo 20 dice **cómo son las reglas**, no qué rutinas hace el agente. Esto es conducta, y el dueño del tema es el capítulo 01, donde ya vive `C10`. Además `M7` prohíbe las dependencias hacia arriba: una regla del preámbulo colgando de una de capa 2 iría en la dirección equivocada. Va como `C20`.

**Validable.** Sí, parcialmente: se puede comprobar que exista el documento del barrido para el periodo cerrado. Que el barrido haya sido **bueno** no lo puede juzgar un programa.

**Decisión que sigue abierta — y sin ella la regla no sirve.** ¿Cuándo se dispara? Una regla cuyo disparador sea "cuando el usuario lo pida" no es una regla: es un favor. Tres opciones:

| Disparador | A favor | En contra |
|---|---|---|
| Al cerrar una **versión** del estándar | Se engancha con `M10`, que ya es un momento definido | Puede pasar mucho tiempo entre versiones |
| Cada **N sesiones** | Cadencia pareja | El número sale de la nada |
| Al cerrar una **fase** de trabajo | Es el ritmo real del proyecto | En este repo no siempre hay fases |

*Yo elegiría la primera*: `M10` ya obliga a parar y mirar el conjunto cuando se versiona, y agregar el barrido ahí no inventa un momento nuevo.

**Cómo quedaría escrita** — en [`base/01-conducta.md`](../../base/01-conducta.md):

````markdown
## C20 · El histórico se relee en frío antes de cerrar un bloque

Al cerrar un bloque de cambios, releer las sesiones registradas desde el barrido
anterior y extraer las candidatas a regla que no se propusieron en su momento
(extiende `01·C10`, depende de `13·DOC17`). El resultado se entrega con el formato de
`plantillas/candidatas-a-regla.md` y **solo propone**: no modifica ninguna regla.

```
INCORRECTO: confiar en que cada decisión se absorbió cuando ocurrió — hoy tres de las
            candidatas más importantes salieron de una sesión donde C10 estaba activa
            y no las propuso
CORRECTO:   al cerrar el bloque, releer el histórico del periodo y entregar las
            candidatas por escrito, para que el usuario decida
```
````

**Lo que la regla arrastra: una plantilla.** La frase *"con el formato de `plantillas/candidatas-a-regla.md`"* obliga a que esa plantilla exista. Es este mismo documento vaciado: los nueve apartados, la tabla de resumen, las cuatro categorías de relación con `base/`, la sección de descartadas y la de defectos. La plantilla **no es la regla** — `M13` las separa: la regla obliga a hacer el barrido, la plantilla dice qué forma tiene el resultado. Y como es `plantillas/`, es cambio versionado (`M10`).

---

## 4 · Descartadas por duplicación (`M12`)

Aparecieron en las sesiones, pero el estándar ya las cubre. No se proponen.

| Lo que apareció | Sesión | Ya lo cubre |
|---|---|---|
| El agente tocó `hook_md.py` sin que se lo pidieran | 3 · 15 | `01·C3` (quédate en tu tarea) · `02·F8` (solo archivos del plan) |
| *"no me obligue a responder, deme las preguntas acá"* | 3 · 21-22 | `01·C13` — la regla existía y **se incumplió**; es defecto, no vacío |
| No commitear sin aprobación, y aprobar el commit aparte del cambio | 5 | `09·G7` + `CLAUDE.md` §4 |
| Asunto del commit ≤ 72 caracteres | 5 | `09·G2`, y ya lo comprueba `commits.py` |
| Releer el archivo antes de editarlo | 5 (varias veces) | `01·C16` |
| Los capítulos se numeran en orden de nacimiento | 5 | `M2` |
| Una regla que crece se parte en anexo | 5 | `M2`, última línea |
| Las reglas no se borran, se derogan | 2 | `M11` |
| Evaluar cada mensaje del usuario como posible mejora del estándar | todas | `01·C10` — **este análisis es `C10` ejecutándose** |
| El `CLAUDE.md` del proyecto se sincroniza con la plantilla central | 3 | `01·C18` |
| La marca de instalación incompleta va en `.agente/`, una por proyecto | 3 · 23-26 | Capa 3 por diseño: es estado local, no regla universal |

---

## 5 · Defectos del estándar encontrados hoy

No son candidatas a regla: son incumplimientos de reglas que ya existen. Se listan porque `M6` paso 6 obliga a reportarlos en vez de resolverlos en silencio.

| # | Defecto | Regla que incumple |
|---|---|---|
| D1 | [`16-cumplimiento-y-calidad.md`](../../base/16-cumplimiento-y-calidad.md) cuelga sus reglas de `## Parte A` / `## Parte B` con encabezado `### CQ1`. Único capítulo así | `M5` (formato), `M4` |
| D2 | `02·F13` lleva la marca `[GATE DE ARRANQUE · PRECONDICIÓN]`, que no está entre las tres que `M5` admite | `M5` |
| D3 | `validadores/reglas-validables.md` está fechado 2026-08-05: los capítulos 18 (`DP1`–`DP8`), 19 (`OB1`–`OB6`) y 20 (`M1`–`M13`) no están auditados ahí | `M9`, `M10` paso 3 |
| D4 | La higiene del capítulo 20 dice que *"el validador de enlaces detecta un ID citado que no existe"*. `enlaces.py` comprueba rutas de archivo, no citas `NN·ID`. Ningún validador aplica las meta-reglas sobre `base/` | Afirmación falsa dentro del propio capítulo |
| D5 | El capítulo 20 dice *"Se lee antes que las reglas que gobierna"*, pero con el número 20 el cargador lo pone último | Contradicción interna → la resuelve **P7** |
| D6 | El ejemplo de derogación de `M11` usa `G4`, que existe y **rige**. Leído rápido parece que `G4` está derogada | Riesgo de confusión; `M11` |
| D7 | `02-flujo-de-trabajo` (F0–F13 + 5 sub-reglas) y `13-documentacion` (DOC1–DOC16) pasan el umbral de ~15 reglas | Higiene del capítulo 20 (guía, no exigencia) |
| D8 | [`2026-08-06-sesion-7.md`](../2026-08-06-sesion-7.md) no tiene la marca `<!-- sesion: … -->` y duplica el contenido de la sesión 6. [`2026-08-06-sesion-4.md`](../2026-08-06-sesion-4.md) tiene 270 bytes | Defecto del enganche del histórico, no del estándar |

**El más caro es D4 + D3**, y son el mismo problema: nada comprueba que `base/` cumpla sus propias meta-reglas, así que los desvíos solo aparecen cuando alguien los busca a mano — como hoy. Un validador que corra las meta-reglas sobre `base/` (formato del encabezado, prefijo exclusivo, marcas permitidas, IDs citados que existen, capítulo presente en `reglas-validables.md`) convierte esta auditoría en automática. Es, además, **P3 aplicado a las propias meta-reglas**: hoy son letrero, no torniquete.

---

## 6 · Si hubiera que hacer solo tres

1. **P5** (`DOC17`) — es la única pieza del día que quedó a mitad de camino: herramienta construida, regla inexistente.
2. **P3** (`M16`) + el validador de D4 — mientras las reglas sean solo letreros, todo lo demás depende de que el agente se acuerde.
3. **P4** (mejora a `M10`) — porque es el error que se cometió hoy mismo mientras se escribía el capítulo 20, y volverá a pasar en el próximo borrador.

**P1** y **P2** son las más importantes de fondo, pero son conducta: valen lo que valga el mecanismo que las respalde. Por eso van después de **P3**, no antes.

---

## 7 · Qué falta decidir

- Si `DOC17` va a `base/` (aplica a todos) o queda `*opt-in*` por los proyectos donde el chat maneja datos sensibles.
- Si **P7** se resuelve con prosa en el encabezado (como hizo `F13`) o con una marca nueva — y en ese caso, agregar la marca a la lista de `M5`, que hoy admite tres y ninguna más.
- Si la variante universal de **P11** entra a `base/` como regla del capítulo 11, o se queda solo la del `CLAUDE.md` raíz.
- Cuál es el disparador de **P12**. Sin un momento definido, la regla no se puede cumplir; mi recomendación es engancharla al cierre de versión que ya define `M10`.
- Si se aprueba **P12**, hay que crear `plantillas/candidatas-a-regla.md` — este documento vaciado. Y **P12 no se puede aprobar sin P5**: sin histórico escrito no hay nada que releer.
- El orden en que se aplican, y en qué versión. Ninguna de estas propuestas suma entrada al `CHANGELOG` hasta que se adopte — que es justamente lo que pide **P4**.
