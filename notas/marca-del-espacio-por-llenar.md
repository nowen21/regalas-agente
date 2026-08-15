# Por qué la marca del espacio por llenar es `«…»`

Nota de diseño de [`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md). La regla dice qué se exige; acá queda por qué se eligió esa marca y no otra, para que nadie lo vuelva a discutir desde cero.

## El problema

Un modelo es un esqueleto con huecos. Quien lo llena a medias entrega un documento donde los huecos que quedaron se confunden con el texto, y nadie los ve al aprobarlo.

Hacía falta una marca que cumpliera dos cosas a la vez, y las dos son necesarias:

1. **Que se note al leer**, sin ir a buscarla.
2. **Que un programa la encuentre** sin confundirla con texto normal.

## Las candidatas

| Marca | Por qué se descartó |
|---|---|
| `[texto]` | Choca con los enlaces de markdown, que son `[texto](ruta)`, y con las casillas `- [ ]`. Un programa que la busque tiene que distinguir tres usos del mismo corchete |
| `<texto>` | Choca con las etiquetas de markdown y de HTML, y sobre todo con la sintaxis de los comandos que las propias plantillas traen adentro, como `--tema "<tema>"` |
| `{{texto}}` | Es la sintaxis de los motores de plantillas. Un documento que la use se rompe si alguien lo pasa por uno de ellos, y además lee como código |
| `XXX` | Se lee como texto normal, no se distingue de una palabra en mayúsculas, y no dice qué va en ese hueco |
| `«texto»` | **La elegida** |

## Por qué ganó `«…»`

Tres motivos, en orden de peso:

**Ya se usa.** Al contar el 2026-08-14, la marca estaba en 25 de los 30 archivos de `plantillas/`. Elegir cualquier otra costaba cambiar 25 archivos en vez de 5, y sin ganar nada a cambio.

**No choca con nada.** Las comillas angulares no son sintaxis de markdown, ni de HTML, ni de ningún motor de plantillas, ni de la línea de comandos. Un programa que las busque no tiene que desambiguar.

**Se ven.** En un texto en español no aparecen casi nunca, así que el ojo las encuentra sin buscarlas.

## El caso límite que obligó a escribir una segunda regla

Dentro de varias plantillas hay comandos que el usuario copia y pega, con su propia sintaxis:

```
python validadores/historico.py --renombrar "<archivo>" --tema "<tema>"
```

Ese `<tema>` **parece** un hueco por llenar y no lo es: lo llena quien corre el comando, no quien usa la plantilla. Si la regla no lo dijera, el programa que cuente las marcas reportaría de más, y el riesgo que la épica quería evitar es exactamente ese: que nadie confíe en la herramienta porque avisa de lo que no es.

Por eso la regla deja escrito qué se marca: lo que llena quien usa el modelo, y nada más.

## Los cuatro archivos que quedaron sin marca, y por qué

Esta es **la lista declarada**: los archivos de `plantillas/` que no llevan ninguna marca. Un archivo sin marca que no esté acá es un defecto, no una excepción.

| Archivo | Qué es en realidad |
|---|---|
| [`plantillas/retrodocumentacion.md`](../plantillas/retrodocumentacion.md) | El procedimiento de seis pasos para retro-documentar un módulo. Se lee y se sigue; no se llena |
| [`plantillas/historico-chat.md`](../plantillas/historico-chat.md) | La explicación de cómo se escribe el histórico. Los `<archivo>` que trae están dentro de comandos que el usuario copia, y por la regla no son huecos |
| [`plantillas/memoria.md`](../plantillas/memoria.md) | La explicación de dónde vive la memoria del agente. Su único `<nombre>` está dentro de una frase que describe qué hace un programa |
| [`plantillas/prompts/prompt-base-usuario.md`](../plantillas/prompts/prompt-base-usuario.md) | El molde con que el usuario le pide trabajo al agente. Se llena escribiendo el pedido, no reemplazando huecos |

Que estén en la carpeta de plantillas no los vuelve modelos. Si alguna vez alguno pasa a tener huecos, los marca como los demás.

## Lo que esta nota no decide

Cuántos huecos lleva cada modelo, ni qué pide cada uno. Eso es de cada plantilla.
