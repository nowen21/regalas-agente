<!-- sesion: ddf03218-0c9d-4ac4-924b-8aac7f6ba82b -->
<!-- nombre: preguntado -->

# 2026-08-14 — Molde para pedir en la sesion

## Conversación

### 1 · Usuario — 2026-08-14 11:25:41
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\prompts\prompt-base-usuario.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> haga un análisis de lo que está en este archivo: plantillas/prompts/prompt-base-usuario.md ahí mismo después de lo que ya hay. No haya que cambiar nada del enunciado

### 2 · Usuario — 2026-08-14 11:27:05
> le estoy dan la ruta del archivo no entiendo que hace revisando otros archivos?

**Agente** — 2026-08-14 11:28:18
<!-- agente: 6ffbb09c-a2c0-4512-b539-158336baba7b -->

Tiene razón — leí de más. Al análisis, con lo que dice el archivo.

Análisis escrito en [prompt-base-usuario.md](plantillas/prompts/prompt-base-usuario.md), debajo del enunciado, que quedó intacto.

Lo que sale del análisis:

- **Lo claro:** el que escribe es el usuario, es dentro del chat, y busca dos cosas distintas — que no falte nada y que no se pueda entender de dos formas.
- **Lo que falta decidir (5 puntos):** si aplica a todo mensaje o solo a los que piden trabajo, si es obligatorio, cuáles son los campos, qué hace el agente cuando falta uno, y dónde vive el molde.
- **El punto crítico:** lo que evita las malas interpretaciones no son más campos, sino que el agente pregunte por lo que falta en vez de suponerlo.
- **Ubicación:** el pedido está en `plantillas/`, pero es un prompt del usuario, no un molde.

No construí la estructura todavía — eso depende de las cinco decisiones.

### 3 · Usuario — 2026-08-14 11:30:47
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\prompts\prompt-base-usuario.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> si la idea es que el agente me obligue a escribirle todo en prompts

**Agente** — 2026-08-14 11:31:05
<!-- agente: d7621d4e-2165-406f-96c6-c03b76d00d4e -->

Entiendo la pregunta como que sí: el molde sería obligatorio, y el agente no arranca hasta que el pedido esté completo. Eso responde el punto 3 del análisis (obligatorio, no ayuda opcional).

Lo que se cae de esa decisión, y es lo que queda por resolver:

- **¿Todo mensaje, o solo los que piden trabajo?** Si aplica a todo, preguntar "¿qué hace este archivo?" obligaría a llenar un molde. Lo razonable: obliga solo cuando el mensaje pide ejecutar algo.
- **¿Dónde se llena?** Dos lecturas distintas de "en prompts":
  1. En el chat mismo, con el molde de campos.
  2. Cada pedido queda como archivo en `prompts/`, y el chat solo lo señala.
- **Qué hace el agente si falta un campo:** con la regla obligatoria, no asume — pregunta solo por lo que falta y espera.

Dígame cuál de las dos lecturas de "en prompts" es, y con eso armo la estructura.

Aparte: esta sesión la guardo como `2026-08-14-molde-para-pedir-en-la-sesion.md` — el análisis del prompt base del usuario y el molde obligatorio de pedidos, ¿va?

### 4 · Usuario — 2026-08-14 11:35:20
> si

**Agente** — 2026-08-14 11:35:48
<!-- agente: ecd32e7c-56fa-497d-a083-b7c5ee3a39f1 -->

Sesión renombrada a [2026-08-14-molde-para-pedir-en-la-sesion.md](historico-chat/2026-08-14-molde-para-pedir-en-la-sesion.md), con su línea en el índice. Para que la pestaña muestre lo mismo, pegue usted:

```
/rename molde-para-pedir-en-la-sesion
```

Queda pendiente la otra pregunta, que es la que decide cómo se construye el molde — ¿cuál de las dos?

1. **En el chat.** Usted escribe el pedido en el mensaje siguiendo los campos del molde. No se crea ningún archivo.
2. **En `prompts/`.** Cada pedido queda como archivo en esa carpeta y el chat solo lo señala; el agente lee el archivo.

### 5 · Usuario — 2026-08-14 11:39:02
> ¿Aplica a todo lo que escriba el usuario, o solo a los mensajes que piden trabajo? 
> que propone solo responda
>
> Una pregunta de dos palabras no debería obligar a llenar un molde.
> pero si debería obligar a que sea más específico para evitar ambigüedades

**Agente** — 2026-08-14 11:39:22
<!-- agente: 6045046c-4879-498f-89f1-2d88b1cc20ab -->

Propongo **dos niveles**, no un molde único.

**Nivel 1 — mínimo, aplica a todo mensaje, incluso a una pregunta de dos palabras.** Tres cosas que caben en una sola frase:

| Campo | Qué es | Sin él pasa que… |
|---|---|---|
| **Sobre qué** | El archivo, carpeta, regla o tema, con su nombre. No "eso", "ahí", "lo anterior" | el agente lo busca por contexto y le acierta a veces |
| **Qué quiere que pase** | `solo responda` · `opine` · `hágalo` | una pregunta se lee como orden, o al revés |
| **Límite, si lo hay** | "sin tocar nada", "solo en esa carpeta" | el agente se estira más de la cuenta |

Ejemplo: `¿qué hace?` → `¿qué hace validadores/enlaces.py? solo responda`. Es la misma pregunta corta, ya sin ambigüedad. Usted acaba de usar el campo 2 al escribir "que propone solo responda".

**Nivel 2 — solo cuando el mensaje pide trabajo.** Suma cuatro campos al nivel 1:

- **Qué se quiere lograr** (el resultado, no el paso)
- **Dónde sí y dónde no** se puede tocar
- **Cómo se sabe que quedó bien**
- **Qué no hacer** (lo que ya se descartó)

**Cómo se hace cumplir**, que es lo que le da fuerza: el agente no completa el campo que falta suponiendo. Si falta algo del nivel 1, pregunta en una línea y no toca nada. Si falta algo del nivel 2, escribe en una frase lo que entendió y espera el sí.

### 6 · Usuario — 2026-08-14 11:42:21
> escriba eso en forma más clara debajo de la pregunta. Recueda: menos es más

**Agente** — 2026-08-14 11:42:42
<!-- agente: d141b524-9bbd-4d3a-9b89-d6081c90335b -->

Quedó en [prompt-base-usuario.md](plantillas/prompts/prompt-base-usuario.md), dentro del punto 3, justo debajo de la tabla de preguntas.

### 7 · Usuario — 2026-08-14 11:43:29
> no le dije que por fuera le dije debajo de la pregunta

**Agente** — 2026-08-14 11:43:57
<!-- agente: 5827f7c7-69bf-4dc5-87ec-1a91ef414ffc -->

La propuesta quedó pegada debajo de su pregunta: saqué esa fila de la tabla, la puse como pregunta con la respuesta abajo, y las otras cuatro pendientes bajaron a "Lo que sigue sin decidir".

### 8 · Usuario — 2026-08-14 11:44:17
> no me cambie el formato de lo que ya tenemos

**Agente** — 2026-08-14 11:44:48
<!-- agente: 3fb1fe57-ad26-4ba1-aec5-6b1e910861d7 -->

La tabla volvió a su forma original, con sus cinco filas y los mismos encabezados. La propuesta quedó dentro de la celda de la primera pregunta, debajo del texto de esa pregunta.

### 9 · Usuario — 2026-08-14 11:47:18
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\prompts\prompt-base-usuario.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> el nivel 2 es muy extenso y no se hace entender

**Agente** — 2026-08-14 11:47:35
<!-- agente: 9ad37ec7-e25a-454d-89f8-364787ced223 -->

El nivel 2 quedó con cuatro campos apilados y la regla del agente pegada al final. Lo dejaría en dos campos, y la regla aparte porque vale para los dos niveles:

> - **Nivel 2, solo si pide trabajo** — agregue dos cosas: **qué debe quedar hecho** y **qué no se toca**.
>
> Si falta algo, el agente no lo rellena: pregunta y espera.

Los otros dos que tenía —"cómo se sabe que quedó bien" y "qué no hacer"— caben dentro de esos dos, y sacarlos hace el molde corto de verdad. ¿Lo dejo así?

### 10 · Usuario — 2026-08-14 11:47:56
> si

**Agente** — 2026-08-14 11:48:07
<!-- agente: 62ce9eb2-d4ed-41fd-941f-ba4a04f7166a -->

Nivel 2 quedó en dos campos, y la regla del agente salió a su propia línea porque aplica a los dos niveles.

### 11 · Usuario — 2026-08-14 11:50:57
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\prompts\prompt-base-usuario.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> los niveles que queden en una lista

**Agente** — 2026-08-14 11:51:16
<!-- agente: 8b4c4ade-d06d-4486-b8be-f8059041ce86 -->

Los dos niveles quedaron como lista, con viñeta `•` y salto `<br>`: dentro de una celda de tabla el guion de markdown no arma lista, rompe la fila. También volví a dejar el nivel 2 en dos campos, que es lo que usted había aprobado.

### 12 · Usuario — 2026-08-14 11:52:09
> recuerde que esto:  —  no hace parte del estándard

**Agente** — 2026-08-14 11:52:46
<!-- agente: e8278a46-c38c-4e15-b809-3694420bb58f -->

Corregido en todo el archivo. La raya larga es marcador de generación automática ([`00·ID8`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), sección 2 de [marcadores-de-ia.md](base/00-identidad-y-rol/marcadores-de-ia.md)), y en su lugar van dos puntos, coma o paréntesis.

Aproveché y quité el punto medio que separaba `solo responda · opine · hágalo`, que está en la misma lista de marcadores. La flecha del ejemplo se queda: como notación `antes → después` el propio anexo la permite.

### 13 · Usuario — 2026-08-14 11:54:20
> ¿El agente puede exigir que se complete un mensaje que no cumple el molde, o el molde es solo una ayuda para escribir?
>
> Todo debe tener un propósito

**Agente** — 2026-08-14 11:54:32
<!-- agente: 637c5e56-73bc-45dd-8efb-05ec48d697dc -->

Lo leo así: un molde que no se exige no cambia nada, y entonces sobra. Si existe, se exige.

Eso tiene dos caras, y las dos salen de "todo debe tener un propósito":

- **Hacia el agente:** el molde obliga. Si falta un campo, no arranca; pregunta por ese campo y espera.
- **Hacia el molde:** cada campo existe solo si evita una ambigüedad concreta. El campo que no evita nada se quita, aunque suene completo.

La segunda cara es la que protege de la primera: como es obligatorio, cada campo de más se convierte en una traba en cada mensaje.

¿Lo escribo así debajo de esa pregunta, en su celda?

### 14 · Usuario — 2026-08-14 11:55:49
> si

**Agente** — 2026-08-14 11:56:00
<!-- agente: f007e584-f987-4c7c-abdc-22a1373de883 -->

Escrito en la celda de esa pregunta, con el mismo formato que la anterior: viñetas `•` y salto `<br>`, sin raya larga.

Quedan tres preguntas del punto 3: los campos, qué hace el agente cuando falta uno, y dónde queda escrito el molde.

### 15 · Usuario — 2026-08-14 11:56:17
> El enunciado no nombra ninguno. Hay que proponerlos: qué se quiere, para qué, sobre qué archivos o carpetas, qué no se debe tocar, cómo se sabe que quedó bien.
>
> propongalos

**Agente** — 2026-08-14 11:56:42
<!-- agente: 6cb2a725-4ce7-4368-a8d4-b3f3f82d3eec -->

Aplico la prueba de propósito a los cinco candidatos: entra el campo que evita una ambigüedad que los otros no cubren.

**Quedan cuatro.**

| Campo | Lo que escribe el usuario | Sin él pasa que |
|---|---|---|
| **Sobre qué** | el archivo, la carpeta o el tema, con nombre | el agente adivina el referente de "eso", "ahí", "lo anterior" |
| **Qué quiere** | `solo responda`, `opine` o `hágalo` | una pregunta se ejecuta, o una orden se queda en respuesta |
| **Qué debe quedar hecho** | el resultado, en una frase | el agente entrega otra cosa y las dos partes creen tener razón |
| **Qué no se toca** | archivos, carpetas o decisiones cerradas | el trabajo se estira más allá de lo pedido |

**Cómo se reparten:** nivel 1 pide los dos primeros. Nivel 2 agrega los dos últimos. "Qué no se toca" es el mismo campo que en el nivel 1 aparecía como límite opcional, así que no son cinco campos sino cuatro.

**Los dos que salen:**

- **Para qué.** Casi siempre repite "qué debe quedar hecho". Se escribe solo cuando el pedido no se explica por sí mismo, y ahí cabe dentro de ese campo.
- **Cómo se sabe que quedó bien.** Es el mismo campo que "qué debe quedar hecho", si este se escribe como algo que se puede mirar y comprobar. Dos campos para lo mismo hacen que se llene uno y se deje vacío el otro.

¿Lo escribo así en la celda de esa pregunta?

### 16 · Usuario — 2026-08-14 11:57:16
> si

**Agente** — 2026-08-14 11:57:29
<!-- agente: 73520014-04d0-46a7-8e05-93a9cee20dd6 -->

Listo, en la celda de "Los campos".

Quedan dos preguntas: qué hace el agente cuando falta un campo, y dónde queda escrito el molde.

### 17 · Usuario — 2026-08-14 11:58:40
> ¿Pregunta, asume y avisa, o se detiene? Este es el punto que de verdad evita las "malas interpretaciones": sin él, el molde es apenas una sugerencia de redacción.
>
> sino tiene lo que necesita para trabajar no puede avanzar porque las cosas van a quedar a medias

**Agente** — 2026-08-14 11:58:53
<!-- agente: d7a3af39-1eec-4fec-9db1-8cdd18025f3d -->

Entonces se detiene. Así lo escribiría:

- **No asume, ni asume y avisa.** Avisar después de haber trabajado deja el trabajo a medias, que es justo lo que se quiere evitar.
- **Pregunta solo por el campo que falta**, en una línea y nombrándolo. No repite el molde completo ni manda un formulario para llenar ([`01·C13`](base/01-conducta.md#c13--preguntas-de-analisis-van-en-chat-abierto-no-en-formulario-cerrado)).
- **Mientras espera no toca nada.**
- **Si la falta aparece con el trabajo ya empezado**, para en ese punto, dice qué lleva hecho y qué necesita saber para seguir.

¿Lo escribo así en la celda?

### 18 · Usuario — 2026-08-14 11:59:01
> si

**Agente** — 2026-08-14 11:59:14
<!-- agente: 4197c3cb-3b75-454e-bd1f-0139cfe18a64 -->

Escrito. El enlace a `01·C13` va relativo desde `plantillas/prompts/`, para que abra desde el archivo.

Queda una pregunta: dónde queda escrito el molde.

### 19 · Usuario — 2026-08-14 12:00:46
> ¿Como plantilla que el usuario copia, como regla del estándar que obliga al agente a pedirla, o las dos cosas?
>
> que propone?

**Agente** — 2026-08-14 12:01:05
<!-- agente: bc6036da-d237-49c8-b120-bdfd88b579a8 -->

**Las dos, pero no pesan igual.**

- **La regla es lo que manda.** Va en [`base/01-conducta.md`](base/01-conducta.md) como una `C` nueva, porque es conducta del agente frente al mensaje del usuario: si falta un campo, se detiene y pregunta. Sin esto, el molde es un consejo que nadie cumple.
- **La plantilla es solo apoyo.** Los cuatro campos caben en una frase, y nadie va a copiar un archivo para escribir en el chat. Serviría un recordatorio corto en `plantillas/prompts/`, con los campos y dos ejemplos, para pegar cuando el pedido es grande. Que llegue a cada proyecto lo hace `instalar.py`, no el usuario.

**Dos cosas que se caen de esto:**

- **Versión MAYOR.** Obliga a un proyecto al día a algo nuevo: el agente deja de arrancar con pedidos incompletos.
- **Sin validador.** Lo que se exige pasa en el chat, y ningún script lee el chat ([`20·M9`](base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable-y-como.md)). Se cumple o no se cumple en el momento.

¿Lo escribo así en la celda? Con eso quedan resueltas las cinco preguntas del punto 3 y se puede construir la estructura.

### 20 · Usuario — 2026-08-14 12:04:27
> si

**Agente** — 2026-08-14 12:04:39
<!-- agente: 27d81aa2-6924-4b4e-bbd3-de37c9d9bace -->

Con eso el punto 3 queda con las cinco preguntas resueltas: alcance en dos niveles, molde obligatorio, cuatro campos, el agente se detiene cuando falta uno, y la regla vive en `base/01` con un recordatorio en `plantillas/prompts/`.

El punto 6 del análisis dice que la estructura se construye cuando estén resueltas esas decisiones. Ya lo están. ¿La construyo?

### 21 · Usuario — 2026-08-14 12:05:13
> si

### 22 · Usuario — 2026-08-14 12:07:39
> qué es lo que está construyendo que veo que está leyendo una cantidad de archivos?

**Agente** — 2026-08-14 12:07:52
<!-- agente: 4f7fefc2-07a6-490c-872c-25fdcba32c74 -->

Todavía no he escrito nada. Estaba juntando lo que el propio estándar exige antes de crear una regla, que es lo que usted aprobó construir:

| Leí | Para qué |
|---|---|
| `base/01-conducta.md` | ver hasta qué número van las `C` y no chocar con `C7` y `C17`, que ya hablan de ambigüedad |
| `20/estructura-regla.md` y `20/checklist.md` | el molde de la regla y las 20 filas que hay que responderle |
| `validadores/reglas-validables.md` | anotarla como no validable |
| `CHANGELOG.md` y `VERSION` | la entrada nueva y subir a 11.0.0 |
| `validadores/instalar.py` | comprobar que la plantilla de apoyo llegue sola a cada proyecto |

Lo último trajo un hallazgo: **el instalador no copia la carpeta `plantillas/` completa**, solo archivos que tiene listados. Una tarjeta suelta en `plantillas/prompts/` no llegaría a ningún proyecto, y quedaría como un segundo texto que dice lo mismo que la regla.

Dos salidas:

1. **Solo la regla.** El molde vive en `01·C21`, que viaja con `base/` y siempre está al día.
2. **Regla más tarjeta en `CLAUDE.md.plantilla`**, que sí se sincroniza sola en cada proyecto ([`01·C18`](base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central)). El usuario la ve en su `CLAUDE.md` sin copiar nada.

¿Cuál hago?

### 23 · Usuario — 2026-08-14 12:10:49
> 2. la idea es que cada proyecto lo tenga

**Agente** — 2026-08-14 12:13:13
<!-- agente: ea417a75-2932-444c-b18c-403e780e04f9 -->

Estructura construida, en cinco archivos:

| Archivo | Qué quedó |
|---|---|
| [base/01-conducta.md](base/01-conducta.md) | La regla `C21`, "Pide el dato que falte antes de arrancar", con su ejemplo y el checklist de 20 filas aplicado: **CUMPLE**, 19 ✅ y 1 N/A |
| [plantillas/CLAUDE.md.plantilla](plantillas/CLAUDE.md.plantilla) | Punto 6, con los cuatro campos y un ejemplo de cada uno. Llega solo a cada proyecto por `C18`, que agrega las secciones nuevas sin pisar lo escrito |
| [validadores/reglas-validables.md](validadores/reglas-validables.md) | `C21` anotada como no validable, con el motivo |
| [CHANGELOG.md](CHANGELOG.md) | Entrada 11.0.0, MAYOR |
| [VERSION](VERSION) | 10.0.0 pasa a 11.0.0 |

El validador del estándar da **0 fallas**. Los dos avisos que salen son de `base/09-git.md` y `estructura-regla.md`, de otro trabajo, y no los toqué.

Dos cosas de las que decidimos y conviene tener presentes:

- La regla dice que el pedido que solo pide información declara **dos** campos, no cuatro. Sin eso, preguntar algo corto obligaría a llenar el molde entero.
- `base/09-git.md` aparece modificado en git, pero es de otra sesión.

Falta su aprobación para commitear. ¿Reviso algo antes?

### 24 · Usuario — 2026-08-14 12:44:35
> comite
