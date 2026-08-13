# El proyecto sabe qué versión del agente usa y qué le falta aplicar

Lo que pidió el usuario, con sus palabras. Rescatado de las sesiones del histórico.

## De [2026-08-06-sesion-3.md](../historico-chat/2026-08-06-sesion-3.md) · 2026-08-06 18:23:03

La idea es que desde el agente exista una plantilla con el **stack de instalación**, para que posteriormente sea copiada al directorio **`.agente`** del proyecto. Además, desde los proyectos también debe ser posible detectar si existen actualizaciones del stack de instalación, del propio agente o de cualquiera de sus componentes, de manera que puedan identificarse y aplicarse cuando corresponda.

## De [2026-08-06-sesion-5.md](../historico-chat/2026-08-06-sesion-5.md) · 2026-08-07 10:21:21

Sí, constrúyalo. Nada de lo que utilice el proyecto debe quedar desactualizado. Cuando exista una nueva versión del agente, y esa versión afecte alguno de los componentes que utiliza el proyecto, se deberá realizar la actualización correspondiente.
Toda actualización deberá quedar documentada dentro del proyecto en la carpeta **`.agente/versiones`**, de manera que se pueda identificar a partir de qué momento el proyecto comenzó a utilizar la nueva versión.
En esa documentación debe quedar registrado, como mínimo, qué versión se instaló, qué cambios se aplicaron, qué componentes fueron actualizados y cualquier información relevante relacionada con la actualización.

## De [2026-08-06-sesion-5.md](../historico-chat/2026-08-06-sesion-5.md) · 2026-08-07 11:33:26

Pero entonces la forma de alertar a los proyectos no es la adecuada, porque al proyecto no le interesa conocer todos los cambios del agente, sino únicamente aquellos que debe actualizar o aplicar.

## De [2026-08-06-sesion-5.md](../historico-chat/2026-08-06-sesion-5.md) · 2026-08-07 09:53:50

pero también debe haber algo que valide que CLAUDE.md está actualizado no puede haber nada viejo en el proyecto del agente
