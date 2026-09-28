# Pendiente · «qué falta, en una línea»

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Modelo del pendiente propio del estándar: lo que esta casa encontró que le falta a sí misma. El que reporta un proyecto tiene el suyo, [plantillas/pendiente-reportado.md](pendiente-reportado.md). Lo levanta el andamio (`python validadores/andamio.py pendiente <slug>`). Sin `--hu`, la historia queda «Por asignar» hasta que el pendiente se apruebe; con `--hu <épica>/<HU>`, el andamio la rellena. El resto queda con sus marcadores. Al llenarlo se reemplazan los `«…»` y se borran esta caja y las notas como ella.

**Estado:** abierto, anotado el «AAAA-MM-DD».

| | |
|---|---|
| **Historia de usuario** | «HISTORIA». «Por qué esa y no otra» |
| **De dónde sale** | «el hallazgo, la sesión o el proyecto que lo destapó, con su enlace» |
| **Proyecto de origen** | El estándar mismo |

## El problema

> Es el hallazgo que abre el pendiente.

«Qué se encontró, con el detalle que necesita quien va a corregirlo y no vio el caso. Con rutas y líneas, verificadas.»

## Por qué importa

> Es el daño que hace dejarlo como está.

«Qué se rompe o qué se pierde. Si no bloquea nada, decirlo, y decir entonces qué daño hace, porque casi siempre hay uno más lento.»

## Qué falta

> Es el trabajo que cierra el pendiente.

«Qué debe construirse o corregirse. Si hay más de una salida, las dos con su costo y cuál conviene.»

## El límite

> Marca hasta dónde llega el pendiente.

«Lo que este pendiente **no** cubre, para que nadie lo dé por cerrado de más.»

## Cómo se sabrá que cerró

> Es la prueba que da el pendiente por cerrado.

«La comprobación concreta que alguien puede correr para verificarlo. No «cuando esté arreglado».»
