# Pendiente · La guía del desarrollo profesional es doctrina del estándar, no de un proyecto

**Estado:** abierto · anotado 2026-08-21.

| | |
|---|---|
| **Historia de usuario** | EP-001 (cuerpo de reglas heredable): es contenido que debe heredarse a todos los proyectos; la HU concreta la asigna el estándar |
| **Proyecto de origen** | **matematica** · `C:\wamp64\www\proyectos\personales\matematica` |
| **Su pendiente de seguimiento** | `pendientes/02-esperando-que-el-estandar-adopte-la-guia-del-desarrollo.md` del proyecto: queda **abierto allá** hasta que este se resuelva |
| **A quién avisar al cerrar** | a **todos los instalados**: la lista está en [../plantillas/proyectos.md](../../plantillas/proyectos.md) |

## El problema

En el proyecto matematica quedó escrita, a pedido del usuario, una guía que resume dos cosas que rigen a **cualquier** proyecto, no a ese en particular:

1. **Los 10 pasos del ciclo de desarrollo** (entender la necesidad, analizar el contexto, delimitar alcance, descomponer en unidades con criterios de aceptación, planificar con aprobación previa, implementar, probar contra los criterios, documentar y cerrar, entregar, mantener). Es, en lenguaje llano, la cadena `02·F0` con sus estaciones.
2. **Las cualidades del producto para producción** (seguridad, manejo de errores, datos protegidos y respaldos probados, pruebas automatizadas, reproducibilidad, observabilidad, rendimiento bajo carga real, despliegue repetible y reversible, documentación de operación). Es, en lenguaje llano, el mapa de los capítulos `03` a `12` y de los patrones opt-in `15` a `19`.

El archivo vive en `documentacion/guia-desarrollo-profesional.md` del proyecto de origen. En la misma sesión quedó registrada la señal **S-262** (decision, scope organizacion): la división del trabajo entre lo que el estándar hace cumplir solo y lo que decide el usuario.

Doctrina transversal guardada en un solo proyecto es el mismo defecto que la memoria local: los demás proyectos no la ven, y si cada uno escribe su propia versión, divergen.

## Cómo se reproduce

1. Abrir `C:\wamp64\www\proyectos\personales\matematica\documentacion\guia-desarrollo-profesional.md` (sesiones del 2026-08-20 y 21, estándar v28.0.0): la guía existe y su contenido no menciona nada exclusivo de ese proyecto salvo la tabla de correspondencia final.
2. Buscar en el estándar un documento equivalente y heredable (en `base/`, `anatomia/` o `plantillas/`): no existe uno que presente el ciclo completo y las cualidades de producción en lenguaje de entrada, para quien llega sin conocer las reglas.

## Por qué importa

No bloquea nada. El daño es lento: cada proyecto nuevo que quiera "la explicación de por qué trabajamos así" la reescribirá a su modo, y las versiones divergirán del texto normativo. Además el usuario fijó la línea (S-262 y este pedido): lo que rige a todos los proyectos vive en el estándar, y los proyectos lo consumen, no lo copian.

## Qué falta

Que el estándar adopte la guía como contenido propio y heredable. Dos salidas:

1. **Documento doctrinal en el estándar** (por ejemplo en `anatomia/` o como documento de entrada de `base/`), escrito desde el estándar: los 10 pasos enlazando cada uno a su regla (`02·F0` y compañía) y las cualidades enlazando a sus capítulos y patrones opt-in. Los proyectos lo referencian; la copia local de matematica se reemplaza por un puntero. Es la salida que conviene: un solo texto, con dueño.
2. Convertirla en plantilla (`plantillas/`) que el instalador copie a cada proyecto. Se descarta la recomendación: multiplica copias que envejecen, que es justo el defecto que este pendiente reporta.

La redacción de partida está **adjunta a este pendiente**: `73-adjunto-guia-desarrollo-profesional.md` (borrado al cerrar, como acá se ordenó), copia literal de la guía del proyecto de origen para no depender de aquel repositorio. El estándar decide qué toma, qué corrige y por dónde la mete a su propio flujo (esto no nace como regla: `20·M14` manda su procedimiento si algo de aquí debe volverse norma). El adjunto se borra al cerrar.

## El límite

Este pendiente no pide crear reglas nuevas ni validadores: pide un documento heredable. Si al escribirlo el estándar decide que algo debe ser regla, eso sigue su propio procedimiento aparte. Tampoco cubre la señal S-262, que ya quedó registrada en la memoria central y no necesita más.

## Cómo se sabrá que cerró

El estándar tiene el documento publicado y enlazado desde su README o su anatomía; en el proyecto matematica se puede reemplazar `documentacion/guia-desarrollo-profesional.md` por una referencia al documento central sin perder contenido (comparando que los 10 pasos y las 9 cualidades estén cubiertos allá). Entonces el pendiente de seguimiento de matematica se cierra.
