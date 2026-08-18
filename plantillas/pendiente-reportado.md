# Pendiente · «qué se encontró, en una línea»

> **Modelo del pendiente que un proyecto le reporta al estándar** (`02·F24`). Se copia en `pendientes/` **del estándar**, no del proyecto. Su gemelo —el que queda en el proyecto— es [plantillas/pendiente-de-seguimiento.md](pendiente-de-seguimiento.md), y los dos se escriben **en la misma sesión**: uno sin el otro es la mitad que ya falló dos veces. Reemplaza los `«…»` y borra esta caja.

**Estado:** abierto · anotado «AAAA-MM-DD».

| | |
|---|---|
| **Historia de usuario** | «EP-00N · HU-00N — título» — «por qué esa y no otra» |
| **Proyecto de origen** | **«Nombre del proyecto»** · `«ruta»` |
| **Su pendiente de seguimiento** | `«ruta del pendiente allá»` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a «el proyecto de origen» / a **todos los instalados**, si la corrección los rige a todos — la lista está en [plantillas/proyectos.md](proyectos.md) |

> **El proyecto de origen no es opcional.** Sin él nadie sabe a quién avisarle al cerrar, y ese proyecto se queda esperando para siempre. `validar.py pendientes` lo comprueba.

## El problema

«Qué se encontró, con el detalle que necesita quien va a corregirlo y no vio el caso.»

## Cómo se reproduce

«Los pasos, con el proyecto y la fecha. Sin esto, quien corrija tiene que creer en vez de comprobar.»

## Por qué importa

«Qué se rompe o qué se pierde. Si no bloquea nada, decirlo — y decir entonces qué daño hace, porque casi siempre hay uno más lento.»

## Qué falta

«Qué debe corregirse. Si hay más de una salida, las dos con su costo y cuál conviene.»

## El límite

«Lo que este pendiente **no** cubre, para que nadie lo dé por cerrado de más.»

## Cómo se sabrá que cerró

«La comprobación concreta que alguien puede correr para verificarlo — no "cuando esté arreglado".»
