# Bitácora de operación   `[CAPA 3]`

**Para qué sirve este documento.** Es el registro de lo que le pasa al sistema en producción, en orden: despliegues, respaldos, incidentes, mantenimientos. Cuando algo falle, la primera pregunta será «¿qué cambió antes?», y la respuesta debe estar acá y no en la memoria de alguien.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Plantilla. Se escribe **en el momento** en que el evento ocurre, el más reciente arriba. Lo anotado no se reescribe: si algo se corrigió después, la corrección se anota como evento nuevo. Mientras no haya producción, existe con su primera línea: «No aplica todavía porque «el porqué»».
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta.

## El registro

> Tiene una fila por cada evento del sistema en producción. Los tipos de evento son despliegue, respaldo, restauración, incidente, mantenimiento y cambio de configuración. Un incidente con causa y corrección de fondo amerita además su [postmortem](../postmortem.md), y acá queda el enlace.

| Fecha y hora | Tipo | Qué pasó | Qué se hizo | Quién |
|---|---|---|---|---|
| «AAAA-MM-DD HH:MM» | «…» | «…» | «…» | «…» |

## Lo que la bitácora alimenta

> Dice qué otros documentos se actualizan a partir de lo que se anota acá.

- Un **incidente** repetido dos veces gana su fila en el [manual de operación](18-manual-tecnico-y-de-operacion.md) («cuando algo falla»), para que la tercera vez tenga remedio escrito.
- Un **despliegue** apunta a su versión en las [notas de versión](19-notas-de-version.md).
- Una **restauración** actualiza la fecha de última prueba en el manual de operación.
