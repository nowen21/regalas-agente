# Plantillas

## Reglas de redacción

Toda plantilla y todo documento generado a partir de una plantilla deben redactarse siguiendo estas reglas. Cada modelo incluye estas reglas en su propia caja de reglas (la parte 3 de [cómo está hecho un modelo](#cómo-está-hecho-un-modelo)).


| Regla | Qué exige |
|---|---|
| [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
| [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
| [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
| [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

## Qué hay en esta carpeta

Los moldes del estándar. Los del ciclo de vida están en [plantillas/ciclo-vida-proyectos/README.md](ciclo-vida-proyectos/README.md), numerados en el orden en que todo desarrollo los recorre. En esta raíz quedan los de configuración del proyecto, operación, transversales y fuentes de generación.

Aunque la carpeta se llame «plantillas», no todo lo que hay acá se llena a mano. Al aplicar [`13·DOC19`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), que pide marcar con `«…»` cada espacio por llenar, cuatro archivos quedaron sin marcas y hubo que listarlos a mano como excepción. Una lista así envejece sin que nadie la mire. Por eso acá se dice qué categorías hay, y un archivo sin marcas se explica solo.

## Las dos categorías

| Categoría | Quién la llena | ¿Lleva marcas `«…»`? |
|---|---|---|
| **Modelo** | Una persona, copiándolo y completándolo | Sí, una en cada espacio por llenar |
| **Fuente de generación** | Un programa, como el andamio o [validadores/instalar.py](«RUTA-ESTANDAR»/validadores/instalar.py) | No: no hay a quién marcarle dónde escribir |

Casi todas son modelos. Estas son las fuentes de generación, y conviene conocerlas antes de «arreglarles» las marcas que les faltan:

| Archivo | Con qué se genera |
|---|---|
| [plantillas/pendiente.md](pendiente.md) | El pendiente propio del estándar; lo levanta el andamio |
| [plantillas/candidatas-a-regla.md](candidatas-a-regla.md) | El barrido de lo que el usuario pidió dos veces, que `20·M20` exige al cerrar una versión |
| [plantillas/historico-chat.md](historico-chat.md) | El `historico-chat/README.md` de cada proyecto |
| [plantillas/memoria.md](memoria.md) | El `historico-chat/memory/memory.md` de cada proyecto |
| [plantillas/CLAUDE.md.plantilla](CLAUDE.md.plantilla) | El `CLAUDE.md` del proyecto |

## Cómo está hecho un modelo

El modelo de todas es [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](ciclo-vida-proyectos/07-plan-trabajo.md). Las demás se ajustaron a él en las versiones 38.0.4 y 38.0.5. Una plantilla nueva se arma igual, y la que se aparte se corrige.

### Las partes, en orden

| # | Parte | Qué lleva | Al llenarla |
|---|---|---|---|
| 1 | **Título** | Un `#` con el identificador y el nombre del documento, separados por ` · `: `# Plan de Trabajo · Fase «A-EP01-HU03-Descripción»` | Se llena |
| 2 | **Para qué sirve este documento** | Un párrafo de entrada que dice qué es el documento, para qué sirve, qué se busca con él y cómo se usa | Se queda, para que quien lo abra un año después sepa qué está leyendo |
| 3 | **Caja de reglas de redacción** | La tabla de [reglas de redacción](#reglas-de-redacción), con la frase «Esta nota se borra al llenarla». Va debajo del párrafo de la parte 2 o, si no lo hay, debajo del título | Se borra |
| 4 | **Caja de uso** | Qué es el documento, qué reglas cumple y dónde se guarda. Cierra con «Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta» | Se borra |
| 5 | **Nota de definición** | Debajo de cada `##` y de cada `###`, una nota `>` que dice qué es la sección, qué se escribe y cómo, con un ejemplo que el agente pueda seguir al llenarla.<br><br>La nota dice también qué no va en la sección, para que el agente no la llene con datos que le tocan a otra.<br><br>Si la sección puede no aplicar, la nota dice qué se escribe en ese caso: «Ninguno» o «No aplica: «motivo»» | Se borra |
| 6 | **Espacios por llenar** | La marca `«…»`, con lo que va adentro dicho en ella ([`13·DOC19`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)) | Se reemplazan |
| 7 | **Citas a reglas** | Toda regla nombrada va enlazada ([`20·M15`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md)). Si la plantilla ya usa `«RUTA-ESTANDAR»`, sus enlaces también; si no, la ruta es relativa a `base/` | Se quedan |

### La plantilla misma cumple las reglas de redacción

- Sin raya larga en el título, los encabezados ni la prosa: se usa el punto medio.
- Sin emojis, sin separadores `---` entre secciones, sin negrita sobre frases enteras, sin flechas en la prosa y sin palabras enteras en mayúscula.
- Tres puntos seguidos (`...`) fuera de las marcas, no los puntos suspensivos de un solo carácter.
- Cada cosa se dice una vez: el texto por llenar no repite lo que ya dijo la nota.

### Al llenarla

- La sección que no aplica se escribe `N/A`; no se borra ni se deja con su marca ([`13·DOC21`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md)). Solo se borra la que el modelo marca *(opcional)*.
- Un documento con una sola marca `«…»` sin reemplazar no está terminado ([`13·DOC20`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md)).

### Lo que queda por fuera

- Los encabezados que lee un programa no llevan nota de definición, como el `## S-000` de [plantillas/senales.md](senales.md).
- Los archivos que el agente no redacta no llevan la caja de reglas: los índices, la transcripción del enganche, el prompt del usuario, las guías de etapa del CVDS y el registro de proyectos.

## Lo que no es ninguna de las dos, y por eso no está acá

Un procedimiento no es un molde. No se copia ni se llena: se lee y se sigue, y vive junto a la regla que lo exige.

[plantillas/«RUTA-ESTANDAR»/base/13-documentacion/retrodocumentacion.md](«RUTA-ESTANDAR»/base/13-documentacion/retrodocumentacion.md), con los seis pasos de [`13·DOC6`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), estuvo acá hasta el 2026-08-17 y se movió por eso. El capítulo 13 ya tenía el precedente: [plantillas/«RUTA-ESTANDAR»/base/13-documentacion/render-local-de-md.md](«RUTA-ESTANDAR»/base/13-documentacion/render-local-de-md.md) es un anexo que no es regla y vive al lado de la suya.

[plantillas/prompts/](prompts/) sí se queda, en su subcarpeta: el molde con que el usuario pide trabajo se llena escribiendo el pedido, así que es un modelo, solo que lo llena el usuario y no el agente.

## La pregunta que separa

Antes de dejar un archivo acá, se pregunta si alguien lo copia y lo completa:

- Sí: es un modelo, va acá y lleva sus marcas.
- No, lo llena un programa: es una fuente de generación, va acá y no lleva marcas.
- No, se lee y se sigue: es un procedimiento, y va junto a la regla que lo exige.
