# Pendiente · «qué se encontró, en una línea»

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Modelo del pendiente que un proyecto le reporta al estándar (`02·F24`). Se copia en `pendientes/` **del estándar**, no del proyecto. Su gemelo, el que queda en el proyecto, es [plantillas/pendiente-de-seguimiento.md](pendiente-de-seguimiento.md), y los dos se escriben en la misma sesión: uno sin el otro es la mitad que ya falló dos veces. Al llenarlo se reemplazan los `«…»` y se borran esta caja y las notas de cada sección.

**Estado:** abierto, anotado el «AAAA-MM-DD».

| | |
|---|---|
| **Historia de usuario** | «EP-00N · HU-00N — título» — «por qué esa y no otra» |
| **Proyecto de origen** | **«Nombre del proyecto»** · `«ruta»` |
| **Su pendiente de seguimiento** | `«ruta del pendiente allá»` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a «el proyecto de origen» / a **todos los instalados**, si la corrección los rige a todos — la lista está en [plantillas/proyectos.md](proyectos.md) |

> El proyecto de origen es obligatorio. Sin él nadie sabe a quién avisarle al cerrar, y ese proyecto se queda esperando para siempre. `validar.py pendientes` lo comprueba.

## El problema

> Describe el defecto del estándar tal como se encontró.

«Qué se encontró, con el detalle que necesita quien va a corregirlo y no vio el caso.»

## Cómo se reproduce

> Son los pasos para ver el defecto con los propios ojos.

«Los pasos, con el proyecto y la fecha. Sin esto, quien corrija tiene que creer en vez de comprobar.»

## Por qué importa

> Es el daño que hace el defecto mientras siga abierto.

«Qué se rompe o qué se pierde. Si no bloquea nada, decirlo, y decir entonces qué daño hace, porque casi siempre hay uno más lento.»

## Qué falta

> Es la corrección que se le pide al estándar.

«Qué debe corregirse. Si hay más de una salida, las dos con su costo y cuál conviene.»

## El límite

> Marca hasta dónde llega este pendiente. Si no hay nada que excluir, se escribe «Ninguno».

«Lo que este pendiente **no** cubre, para que nadie lo dé por cerrado de más.»

## Cómo se sabrá que cerró

> Es la prueba que da por corregido el defecto.

«La comprobación concreta que alguien puede correr para verificarlo, no «cuando esté arreglado».»
