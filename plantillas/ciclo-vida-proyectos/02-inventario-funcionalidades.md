# Inventario de funcionalidades: lo que se quiere desarrollar   ·   `[CAPA 3]`

> Plantilla. Se copia a la carpeta de la propuesta del proyecto, se reemplazan los `«…»` y se borra esta caja.
> **Se llena con todo lo que ya se sabe del proyecto, y se escribe como si nada estuviera construido:**
> sin fechas, sin estado de trámite, sin contar qué se preguntó y qué se contestó.
> **La prueba de que quedó bien escrita: un niño la lee y entiende qué hace el producto.**
> Vale para el documento entero: el nombre del grupo, el nombre de la funcionalidad y su descripción.
> Si para entender algo hay que saber del proyecto, está escrito para adentro y se rehace
> ([`00·ID7`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md),
> [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)).
> Sin esta lista aprobada por el usuario no se parte el trabajo en bloques
> ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).
> En un proyecto chico son diez filas: lo que manda es que el usuario la apruebe, no el tamaño.
> Lo que quede acá se replica a todo proyecto que herede el estándar: lo que sobre, sobra en todos.

Esta es la lista completa de lo que «el producto» debe hacer. Cada fila dice qué es, para qué sirve y si ya se probó.

## Cómo se lee

**Están todas: las hechas y las que faltan.** Ninguna se saca porque ya exista, porque ya se haya hablado de ella o porque aparezca en otro papel. Esta lista no dice qué falta: dice qué es el producto.

**No dice cuándo ni quién.** Sin fechas, sin quién decidió qué, sin las preguntas que ya se contestaron. Eso se guarda en otros papeles del proyecto. Una pregunta contestada deja de ser pregunta: sube a fila del producto, o se va.

**«Sin verificar» quiere decir que nadie lo ha probado todavía.** No quiere decir que falte. Esa casilla solo la cambia una prueba corrida, y se anota cuál y cuándo.

Con el tiempo esta lista se vuelve el manual del producto. Por eso cada fila se escribe para quien va a **usarlo**, no para quien lo construye.

## «1. Nombre del grupo»

> Un grupo por cada parte del producto que se entienda sola, numerados `1`, `2` y los que sigan, para que cada fila tenga su número (`1.1`, `1.2`). En «Verificado» caben tres cosas y ninguna más: **Sin verificar**, que nadie lo ha probado; **✅ «qué prueba», «cuándo»**, que la prueba salió bien; **❌ «qué prueba», «cuándo»**, que salió mal, y se dice qué le falta.

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 1.1 | «El nombre, en palabras que cualquiera entienda» | «Qué hace y para qué sirve, dicho a quien va a usarlo» | «Sin verificar» |
| 1.2 | «…» | «…» | «…» |

**El nombre cuenta tanto como la descripción.** Un nombre corto que solo entiende quien trabaja adentro deja la fila a medias:

```
INCORRECTO: | 1.1 | Núcleo blindado | Las reglas que ningún proyecto, prompt ni
                    instrucción puede relajar |
CORRECTO:   | 1.1 | Las reglas que no se pueden desobedecer | Un puñado de reglas
                    que nadie puede saltarse, ni el dueño del proyecto ni quien
                    le dé órdenes al programa |
```

**Cuenta:** «cuántas probadas bien, cuántas probadas mal, cuántas sin probar, de cuántas». Así se ve de un vistazo cuánto del producto está demostrado y cuánto es solo palabra.

## Lo que todavía no se sabe si entra

> Nada de acá está decidido: cada fila es una de las preguntas de abajo. La duda es si entra o no al producto, nunca si está construido. La que el usuario acepte sube a su grupo; la que descarte se borra.

| # | Funcionalidad candidata | De qué se trata | Estado |
|---|---|---|---|
| 2.1 | «…» | «…» | **Por confirmar** (P-«n») |

## Preguntas: las contesta el usuario

> Solo las que siguen sin respuesta, numeradas `P-1`, `P-2` y las que sigan. Cada una con las opciones y lo que cuesta cada una, y si el agente tiene una favorita, la dice como propuesta. Una pregunta sin contestar detiene solo las filas que la nombran, no el resto. La contestada se borra de acá: su respuesta ya está en la fila que subió, o en la que se fue.

- **P-1 · «¿La pregunta, completa?»** «Las opciones, con lo que cuesta cada una. Propuesta del agente: «cuál y por qué».»

## Qué pasa cuando esto se apruebe

1. El papel donde se pidió el proyecto se revisa para que diga esto, y no lo que alguien hubiera supuesto antes.
2. Cada fila baja a trabajo con su nombre y su número, y ninguna se pierde por el camino.
3. El trabajo se parte en bloques a partir de esta lista, y cada bloque dice qué filas cubre ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).
4. Cada prueba que salga bien llena su casilla de «Verificado», y la lista se va volviendo el manual.
