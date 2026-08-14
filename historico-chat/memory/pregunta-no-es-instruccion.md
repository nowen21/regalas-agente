# Pregunta, afirmación o indicación: hay que distinguirlas

Antes de tocar un archivo, el agente clasifica el mensaje del usuario en uno de tres y actúa según eso. El nombre del archivo dice "una pregunta no es una instrucción", que es el caso más frecuente, pero la regla cubre los tres.

| Qué llegó | Cómo se reconoce | Qué hace el agente |
|---|---|---|
| **Pregunta** | Pide información o el juicio del agente. *"¿el agente maneja machine learning?"*, *"¿de qué se trata este documento?"*, *"¿en dónde se verifica esto?"* | Responde **solo en el chat**. No toca ningún archivo, ni siquiera si al responder descubre algo mal |
| **Afirmación u observación** | Señala algo sin pedir acción. *"no entiendo por qué hay esto"*, *"estos documentos no explican cuál es su propósito"*, *"pero no está el formato dentro de la fase"* | Explica, **dice qué haría** para arreglarlo y **espera**. Detectar un defecto no autoriza a tocarlo |
| **Indicación** | Pide ejecutar. Verbo en imperativo, o un sí a algo que el agente propuso. *"cree las épicas"*, *"corrija"*, *"suba"*, *"commité"*, *"si entonces modificar la plantilla"* | Ejecuta |

**Cuando dude, no toca.** Explica y pregunta en una línea. Es más barato preguntar que deshacer.

**Mientras se discute un diseño, ningún comentario es una orden de aplicar.** El usuario piensa en voz alta y va corrigiendo el rumbo frase por frase; si el agente edita en cada una, el archivo cambia de forma cinco veces y hay que devolverlo. Se analiza el asunto completo, se propone, y se toca cuando el usuario cierra la discusión. Lo dijo así el 2026-08-14: *"por eso le dije que lo devolviera, porque quería analizar las cosas, porque no es hacer las cosas por hacer"*.

**El rechazo de un comando no está acá.** Que rechazar la llamada no retire la orden es conducta de cualquier agente, no preferencia de este usuario: vive en [`01·C22`](../../base/01-conducta.md#c22--ante-un-comando-rechazado-corrige-el-comando--la-orden-sigue-en-pie).

**Por qué:** el usuario lo señaló varias veces, y la última fue explícita — *"no asuma que porque digo algo ya tiene que modificar"*. Cada edición no pedida le agrega trabajo de revisión y le quita el control de qué se toca y cuándo. Entender no es autorizar.

**Cómo se aplica:** releer el mensaje y ubicar el verbo antes de abrir un archivo. Una condicional también manda: *"si en la plantilla no está hay que corregirlo"* es indicación, no observación. Si ya se editó por error, se avisa y se pregunta cuál versión se deja; y si el usuario pide devolverlo, se devuelve y se comprueba que el archivo quedó igual que en el commit.

**El límite con la regla de corregir el defecto detectado.** Esa regla ([corregir el defecto detectado](corregir-el-defecto-que-uno-mismo-detecta.md)) vale **mientras el agente ejecuta algo ya autorizado**: si está escribiendo lo que le pidieron y encuentra un enlace roto, lo arregla sin preguntar. No vale para convertir una pregunta o una observación en permiso de edición.

Relacionado: [corregir el defecto detectado](corregir-el-defecto-que-uno-mismo-detecta.md) · [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) · [aprobar antes de commit](aprobar-antes-de-commit.md).
