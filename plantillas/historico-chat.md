# Histórico de sesiones

Qué se habló con el agente en cada sesión. Sirve para retomar el trabajo sin releer el chat y para saber por qué quedó algo como quedó: **el chat se borra; el repositorio no.**

Un archivo por sesión, `AAAA-MM-DD-tema.md`. Si hay más de una sesión el mismo día, se sufija `-2`, `-3`.

## Quién lo escribe

Lo escribe el programa, no el agente. Dos enganches de Claude Code, instalados por `validadores/instalar.py` del estándar:

| Enganche | Cuándo | Qué anota |
|---|---|---|
| `UserPromptSubmit` | al enviar el mensaje | el mensaje del usuario, literal |
| `Stop` | al terminar la respuesta | la respuesta del agente, leída del transcript |

La hora sale del reloj de la máquina en ese instante — no de la memoria del agente.

> Está así a propósito. Mientras registrar la sesión dependa de que el agente se acuerde, no se cumple siempre: una instrucción escrita **informa**, un enganche **ejecuta**.

## Cómo está armado cada archivo

- La primera línea lleva `<!-- sesion: <id> -->`. La sesión se busca por esa marca, **no por el nombre**: el archivo se puede renombrar para ponerle el tema real sin que la sesión se parta en dos.
- **La sesión que cruza la medianoche se queda entera, con la fecha del día en que empezó.** No se parte: el archivo es de una conversación, no de un día, y la marca de sesión es una sola. Cada turno lleva su hora real, así que lo que pasó después de las doce se sabe leyendo, no por el nombre del archivo. **El resumen sí va al día en que pasaron las cosas** — son dos documentos con dos criterios, y es a propósito.
- Los mensajes entran antes de `## Abierto`, que cierra el archivo.
- Cada respuesta lleva `<!-- agente: <uuid> -->`, que evita que se duplique si el enganche vuelve a correr.
- No se guarda el razonamiento interno del agente ni la salida cruda de las herramientas: esto es la conversación, no la máquina por dentro.

## El índice es lo que lee la próxima sesión

Un chat nuevo arranca sin memoria de los anteriores. Al abrir la sesión, el enganche le inyecta al agente **este índice** —no las transcripciones, que son la conversación entera— para que sepa qué se habló antes y pueda abrir con `Read` la sesión que le sirva.

Por eso cada sesión que se crea queda anotada aquí: la línea la pone el enganche al crear el archivo y la vuelve a comprobar en cada mensaje. Una sesión sin su línea es una sesión que la siguiente no va a encontrar, y el validador de índices la reporta como falla.

## Qué hace el agente aquí

- **Ponerle tema al nombre.** El enganche crea `AAAA-MM-DD-sesion.md` porque al abrir el chat todavía no se sabe de qué se va a tratar. Apenas hay una respuesta el tema ya está claro, y el propio enganche se lo recuerda al agente —**una sola vez** en la sesión, no en cada mensaje—: propone nombre y resumen en una línea y espera. El nombre lo aprueba el usuario; nada se renombra solo.
- **Renombrar con el comando, no a mano.** Cuando el usuario aprueba:

  ```sh
  python "<estándar>/validadores/historico.py" --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"
  ```

  El recordatorio del enganche trae esa línea con la ruta ya puesta. Cambia el nombre del archivo, su título y la línea del índice — **las tres cosas**. Renombrar a mano deja el índice apuntando a un archivo que ya no está, y esa línea es por donde la próxima sesión llega a esta.
- **El mismo nombre en la sesión de Claude Code.** Junto con el comando, el agente le pasa al usuario la línea `/rename <tema>`, que le pone ese nombre a la sesión: es lo que se ve en la pestaña, en la barra del prompt y en `/resume`. La pega el usuario — `/rename` es un comando suyo y el agente no lo puede ejecutar. Así el archivo del histórico y la sesión abierta se llaman igual.
- **Decir de qué se trató.** La línea del índice nace como "sesión del AAAA-MM-DD"; el `--resumen` la reemplaza por el tema real. Es lo único que la próxima sesión ve de esta.
- **Mantener `## Abierto`**: lo que quedó sin cerrar, o "nada".
- **No copiar a mano lo que el enganche ya escribió.** Si falta algo, se agrega; no se reescribe encima.

## Forma

```markdown
<!-- sesion: 0000-0000 -->

# AAAA-MM-DD — Tema

## Conversación

### 1 · Usuario — AAAA-MM-DD HH:MM:SS
> La pregunta, literal.

**Agente** — AAAA-MM-DD HH:MM:SS

La respuesta, tal como se dio.

## Abierto
- Lo que quedó sin cerrar, o "nada".
```

## Índice

- (una línea por sesión; el enganche agrega la suya al crear el archivo)
