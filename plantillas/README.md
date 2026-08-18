# Plantillas

Los moldes del estándar. El nombre de la carpeta dice «plantillas» y eso hace pensar que todo lo de adentro es un documento que alguien llena a mano. **No lo es**, y confundirlos cuesta: al aplicar [`13·DOC19`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) —cada espacio por llenar lleva su marca `«…»`— cuatro archivos quedaron sin una sola marca y hubo que declararlos como excepción en una lista escrita a mano.

**Una lista de excepciones escrita a mano envejece sin que nadie la mire.** Lo que hacía falta no era la lista: era decir qué categorías viven acá, para que un archivo sin marcas se explique solo.

## Las dos categorías

| Categoría | Quién la llena | ¿Lleva marcas `«…»`? |
|---|---|---|
| **Modelo** | Una persona, copiándolo y completándolo | **Sí.** Cada espacio por llenar lleva la suya |
| **Fuente de generación** | Un programa — [validadores/instalar.py](«RUTA-ESTANDAR»/validadores/instalar.py) | **No**, y no es un descuido: no hay nadie a quien marcarle dónde escribir |

Son casi todos modelos. Las fuentes de generación son estas, y conviene saber cuáles son antes de «arreglarles» las marcas que les faltan:

| Archivo | Con qué se genera |
|---|---|
| [plantillas/historico-chat.md](historico-chat.md) | El `historico-chat/README.md` de cada proyecto |
| [plantillas/memoria.md](memoria.md) | El `historico-chat/memory/memory.md` de cada proyecto |
| [plantillas/CLAUDE.md.plantilla](CLAUDE.md.plantilla) | El `CLAUDE.md` del proyecto |

## Lo que no es ninguna de las dos, y por eso no está acá

**Un procedimiento no es un molde.** No se copia ni se llena: se lee y se sigue. Vive junto a la regla que lo exige, no acá.

[plantillas/«RUTA-ESTANDAR»/base/13-documentacion/retrodocumentacion.md](«RUTA-ESTANDAR»/base/13-documentacion/retrodocumentacion.md) —los seis pasos de [`13·DOC6`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)— estuvo acá hasta el 2026-08-17 y se movió por eso. El capítulo 13 ya tenía el precedente: [plantillas/«RUTA-ESTANDAR»/base/13-documentacion/render-local-de-md.md](«RUTA-ESTANDAR»/base/13-documentacion/render-local-de-md.md) es un anexo que no es regla y vive al lado de la suya.

**[plantillas/prompts/](prompts/) sí se queda**, en su subcarpeta: el molde con que el usuario pide trabajo se llena escribiendo el pedido, así que es un modelo — solo que lo llena el usuario y no el agente.

## La pregunta que separa

Antes de dejar un archivo acá:

> **¿Alguien lo copia y lo completa?**
> Sí → es un modelo, va acá y lleva sus marcas.
> No, lo llena un programa → es una fuente de generación, va acá y no lleva marcas.
> No, se lee y se sigue → es un procedimiento, y va junto a la regla que lo exige.
