# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-14-molde-para-pedir-en-la-sesion.md](../../2026-08-14-molde-para-pedir-en-la-sesion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Sale de un archivo del propio usuario: el molde con que le pide trabajo al agente.

**Propósito:** que un pedido traiga lo que el agente necesita para trabajar, y que no se avance sin eso.

---

## Hallazgos de esta sesión

### H-1 · Se le dio una ruta y el agente se puso a leer el proyecto

- **Qué pasó:** *«le estoy dando la ruta del archivo, no entiendo qué hace revisando otros archivos»*. Y más adelante, otra vez: *«¿qué es lo que está construyendo, que veo que está leyendo una cantidad de archivos?»*.
- **Por qué importa:** cada archivo que el agente abre sin necesidad gasta contexto y tiempo, y desplaza el pedido real. Cuando la instrucción trae la ruta, la ruta **es** el alcance.
- **Qué lo soluciona:** leer lo que se nombró, y preguntar antes de ampliar.
- **Qué se decidió:** el agente se limitó al archivo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [trabajo confinado a la carpeta](../../memory/trabajo-confinado-a-la-carpeta.md).
- **Nace en:** 2026-08-14 · molde para pedir en la sesión.
- **Cerrado en:** 2026-08-14 · molde para pedir en la sesión.
- **Con qué se retoma:** —.

### H-2 · Un molde que aplica a todo obliga a llenar un formulario para preguntar la hora

- **Qué pasó:** al analizar el molde apareció la primera pregunta de fondo: si aplica a **todo** lo que escribe el usuario o solo a lo que pide trabajo. El propio agente lo dijo: *«una pregunta de dos palabras no debería obligar a llenar un molde»*.
- **Por qué importa:** un molde que estorba se abandona. Y el estándar ya distingue los tres modos —pregunta, observación, indicación—: el molde solo tiene sentido en el tercero.
- **Qué lo soluciona:** niveles. El molde completo para lo que pide trabajo, y nada para lo demás.
- **Qué se decidió:** quedaron los niveles, y el usuario los mandó poner en lista porque el intermedio *«es muy extenso y no se hace entender»*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/prompts](../../../plantillas/prompts/).
- **Nace en:** 2026-08-14 · molde para pedir en la sesión.
- **Cerrado en:** 2026-08-14 · molde para pedir en la sesión.
- **Con qué se retoma:** —.

### H-3 · Sin lo que necesita, el agente no avanza

- **Qué pasó:** la pregunta que el agente marcó como la que de verdad evita las malas interpretaciones: cuando el pedido no trae lo necesario, ¿pregunta, asume y avisa, o se detiene? El usuario respondió sin dudar: *«si no tiene lo que necesita para trabajar no puede avanzar, porque las cosas van a quedar a medias»*.
- **Por qué importa:** sin esa respuesta el molde es apenas una sugerencia de redacción. Con ella, es una condición para empezar.
- **Qué lo soluciona:** que el agente pida lo que falta y espere, en vez de suponerlo.
- **Qué se decidió:** el molde exige, no sugiere. Es la misma frase con la que cerró la otra sesión del día: *nada se debe construir sobre un supuesto*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/prompts/](../../../plantillas/prompts/), y la memoria [pregunta, afirmación o indicación](../../memory/pregunta-no-es-instruccion.md).
- **Nace en:** 2026-08-14 · molde para pedir en la sesión.
- **Cerrado en:** 2026-08-14 · molde para pedir en la sesión.
- **Con qué se retoma:** —.

### H-4 · El molde no nombraba ningún propósito

- **Qué pasó:** el usuario lo señaló en tres palabras — *«todo debe tener un propósito»*— y el agente encontró que el enunciado no nombraba ninguno. Los propuso: qué se quiere, para qué, sobre qué archivos o carpetas, qué no se debe tocar, y cómo se sabe que quedó bien.
- **Por qué importa:** los dos últimos son los que faltan casi siempre. **Qué no tocar** es lo que evita que el agente amplíe el alcance por su cuenta, y **cómo se sabe que quedó bien** es lo único que permite cerrar sin discutir.
- **Qué lo soluciona:** que el molde los pida por nombre.
- **Qué se decidió:** quedaron los cinco.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/prompts/](../../../plantillas/prompts/).
- **Nace en:** 2026-08-14 · molde para pedir en la sesión.
- **Cerrado en:** 2026-08-14 · molde para pedir en la sesión.
- **Con qué se retoma:** —.

### H-5 · Plantilla, regla, o las dos

- **Qué pasó:** la última pregunta de forma: si el molde es una plantilla que el usuario copia, una regla que obliga al agente a pedirla, o las dos cosas. El usuario zanjó el alcance: *«la idea es que cada proyecto lo tenga»*.
- **Por qué importa:** una plantilla sola se queda en este repositorio. Para que llegue a cada proyecto tiene que viajar por donde viaja todo: el instalador.
- **Qué lo soluciona:** las dos cosas — la plantilla que se copia y la exigencia que la pide.
- **Qué se decidió:** así quedó, y se commiteó.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/prompts/](../../../plantillas/prompts/).
- **Nace en:** 2026-08-14 · molde para pedir en la sesión.
- **Cerrado en:** 2026-08-14 · molde para pedir en la sesión.
- **Con qué se retoma:** —.

### H-6 · La raya larga no es del estándar

- **Qué pasó:** en mitad del trabajo, el usuario corrigió el texto que el agente estaba escribiendo: *«recuerde que esto: — no hace parte del estándar»*.
- **Por qué importa:** es `00·ID8` aplicándose dos días después de haberse escrito, sobre un documento nuevo. La regla existe, y aun así hubo que recordarla.
- **Qué lo soluciona:** el validador mecánico que `ID8` declaró como parte comprobable y que todavía no existe.
- **Qué se decidió:** se corrigió el texto.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, ya está anotado.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md](../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md), que es el mismo trabajo.
- **Nace en:** 2026-08-14 · molde para pedir en la sesión.
- **Cerrado en:** —.
- **Con qué se retoma:** mientras no exista el validador, `ID8` depende de que alguien la recuerde en cada texto.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 a H-5 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-6 en el [11](../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commiteado y subido a pedido del usuario |
