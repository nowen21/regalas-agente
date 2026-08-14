crea la estructura de como el usuario le debe pedir o escirbir las cosas cuando escribe en la sesión para que no queden cosas sueltas y con malas interpretaciones

---

# Análisis del enunciado

## 1. Qué pide, en una frase

Un molde fijo para que **el usuario** escriba lo que pide dentro del chat, de modo que no quede nada sin decir ni nada que se pueda entender de dos formas.

## 2. Lo que el enunciado sí deja claro

| Punto | Qué dice |
|---|---|
| **Quién escribe** | El usuario. Es un formato de **entrada**, no de respuesta del agente. |
| **Cuándo** | "cuando escribe en la sesión": en el chat mismo, mientras se conversa. No es un documento que se prepare aparte antes de empezar. |
| **Para qué** | Dos objetivos distintos: que **no falte información** ("cosas sueltas") y que **lo dicho tenga una sola lectura** ("malas interpretaciones"). |
| **Qué se entrega** | Una **estructura**: algo reusable, que sirva para cualquier pedido, no la respuesta a un pedido puntual. |

## 3. Lo que no dice y hay que decidir antes de construirlo

| Falta definir | Pregunta que abre |
|---|---|
| **Alcance por tipo de mensaje** | ¿Aplica a todo lo que escriba el usuario, o solo a los mensajes que piden trabajo? Una pregunta de dos palabras no debería obligar a llenar un molde, pero sí a ser específica.<br><br>**Propuesta: dos niveles.**<br>• **Nivel 1, todo mensaje:** sobre qué (el archivo o el tema con su nombre, no "eso" ni "ahí"), qué quiere (`solo responda`, `opine`, `hágalo`) y el límite si lo hay. Ejemplo: `¿qué hace?` → `¿qué hace validadores/enlaces.py? solo responda`.<br>• **Nivel 2, solo si pide trabajo:** agregue dos cosas: **qué debe quedar hecho** y **qué no se toca**.<br><br>Si falta algo, el agente no lo rellena: pregunta y espera. |
| **Obligatorio u opcional** | ¿El agente puede exigir que se complete un mensaje que no cumple el molde, o el molde es solo una ayuda para escribir?<br><br>**Propuesta: todo debe tener un propósito.** Un molde que no se exige no cambia nada, y entonces sobra. Si existe, se exige, y eso tiene dos caras:<br>• **Hacia el agente:** el molde obliga. Si falta un campo, no arranca; pregunta por ese campo y espera.<br>• **Hacia el molde:** cada campo existe solo si evita una ambigüedad concreta. El campo que no evita nada se quita, aunque suene completo.<br><br>La segunda cara protege de la primera: como es obligatorio, cada campo de más se vuelve una traba en cada mensaje. |
| **Los campos** | El enunciado no nombra ninguno. Hay que proponerlos: qué se quiere, para qué, sobre qué archivos o carpetas, qué no se debe tocar, cómo se sabe que quedó bien.<br><br>**Propuesta: cuatro campos.** Entra el que evita una ambigüedad que los otros no cubren.<br>• **Sobre qué:** el archivo, la carpeta o el tema, con nombre. Sin él, el agente adivina a qué apuntan "eso", "ahí", "lo anterior".<br>• **Qué quiere:** `solo responda`, `opine` o `hágalo`. Sin él, una pregunta se ejecuta o una orden se queda en respuesta.<br>• **Qué debe quedar hecho:** el resultado en una frase. Sin él, el agente entrega otra cosa y las dos partes creen tener razón.<br>• **Qué no se toca:** archivos, carpetas o decisiones ya cerradas. Sin él, el trabajo se estira más allá de lo pedido.<br><br>El nivel 1 pide los dos primeros; el nivel 2 agrega los dos últimos. "Qué no se toca" es el límite opcional del nivel 1, así que son cuatro campos y no cinco.<br><br>**Los dos que salen:** *para qué* casi siempre repite "qué debe quedar hecho", y se escribe dentro de ese campo cuando el pedido no se explica solo. *Cómo se sabe que quedó bien* es ese mismo campo, si el resultado se escribe como algo que se puede mirar y comprobar; dos campos para lo mismo hacen que se llene uno y quede vacío el otro. |
| **Qué hace el agente si falta un campo** | ¿Pregunta, asume y avisa, o se detiene? Este es el punto que de verdad evita las "malas interpretaciones": sin él, el molde es apenas una sugerencia de redacción.<br><br>**Propuesta: se detiene.** Si no tiene lo que necesita para trabajar no avanza, porque las cosas quedan a medias.<br>• **No asume, ni asume y avisa.** Avisar después de haber trabajado ya dejó el trabajo a medias.<br>• **Pregunta solo por el campo que falta**, en una línea y nombrándolo. No repite el molde completo ni manda un formulario para llenar ([`01·C13`](../../base/01-conducta.md#c13--preguntas-de-analisis-van-en-chat-abierto-no-en-formulario-cerrado)).<br>• **Mientras espera no toca nada.**<br>• **Si la falta aparece con el trabajo ya empezado**, para ahí, dice qué lleva hecho y qué necesita saber para seguir. |
| **Dónde queda escrito** | ¿Como plantilla que el usuario copia, como regla del estándar que obliga al agente a pedirla, o las dos cosas?<br><br>**Propuesta: las dos, pero no pesan igual.**<br>• **La regla es lo que manda.** Va en [`base/01-conducta.md`](../../base/01-conducta.md) como una `C` nueva, porque es conducta del agente frente al mensaje del usuario: si falta un campo, se detiene y pregunta. Sin esto, el molde es un consejo que nadie cumple.<br>• **La plantilla es apoyo.** Los cuatro campos caben en una frase, y nadie copia un archivo para escribir en el chat. Sirve un recordatorio corto en `plantillas/prompts/`, con los campos y dos ejemplos, para pegar cuando el pedido es grande. Que llegue a cada proyecto lo hace `instalar.py`, no el usuario.<br><br>**Dos cosas que se caen de esto:** la versión es **MAYOR**, porque obliga a un proyecto al día a algo nuevo, que el agente deje de arrancar con pedidos incompletos; y la regla va **sin validador**, porque lo que se exige pasa en el chat y ningún script lee el chat ([`20·M9`](../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)). |

## 4. Tensión de fondo

El pedido tiene dos fuerzas que empujan en sentidos contrarios:

- **Que sea completo** pide más campos: entre más se declare, menos se adivina.
- **Que sirva en un chat** pide menos: el usuario escribe rápido y corto, y un molde largo se abandona a la tercera vez.

El molde solo funciona si es corto. Lo que lo hace efectivo no es la cantidad de campos, sino que el agente **pregunte por el campo que falta en vez de suponerlo**.

## 5. Detalle de ubicación

El archivo está en `plantillas/prompts/`, que es donde viven los moldes. Lo guardado acá todavía no es un molde: es el pedido del usuario con sus palabras. Vale revisar si el pedido debe quedar en `prompts/` y dejar en `plantillas/` solo la estructura que salga de él.

## 6. Qué sigue

Resueltas las cinco decisiones del punto 3, la estructura quedó construida en la versión **11.0.0**:

- La regla [`01·C21`](../../base/01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar), que es la que obliga.
- El punto 6 de [`plantillas/CLAUDE.md.plantilla`](../CLAUDE.md.plantilla), con los cuatro campos y un ejemplo de cada uno, que llega solo a cada proyecto.
