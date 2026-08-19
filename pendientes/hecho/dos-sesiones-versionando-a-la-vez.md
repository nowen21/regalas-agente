# Pendiente · Dos sesiones versionando a la vez

**Estado:** cerrado 2026-08-18 · anotado 2026-08-14 · nace del hallazgo H-9 de [2026-08-14](../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

| | |
|---|---|
| **Historia de usuario** | [EP-002 · HU-006 — Quién manda sobre la versión](../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md) — dos sesiones numerando a la vez es el caso que esa historia tiene que resolver |

## El problema

El 2026-08-14 hubo dos sesiones abiertas sobre el mismo repositorio. Una escribió la versión 10.0.0 mientras la otra subía la 9.0.0, la 9.1.0 y la 9.2.0. Al final del día la versión iba en 12.2.0 con dos numeraciones vivas y entradas del registro escritas por las dos.

`VERSION` y `CHANGELOG.md` son un archivo único cada uno, y ninguna sesión sabe qué está haciendo la otra. La regla de que cada sesión sube solo lo suyo se rompe justo ahí: para guardar lo propio hay que arrastrar lo ajeno.

## Qué falta

Decidir quién manda sobre la versión y escribirlo. Tres opciones sobre la mesa:

**1. La versión se sube al guardar el cambio, no al editarlo.** El número lo pone quien commitea, con lo que haya en ese momento.

**2. Cada sesión escribe su entrada del registro en un archivo aparte** y se juntan al guardar. El registro deja de ser un archivo que dos sesiones editan.

**3. Una sola sesión a la vez toca el estándar.** Es lo más simple y lo más incómodo.

## No es solo la versión: es cualquier archivo que dos sesiones editen

**Ampliado el 2026-08-16**, después de que volviera a pasar en otro archivo.

Mientras una sesión reescribía [`pendientes/README.md`](../README.md) para ponerle la columna de prioridad, otra sesión le agregó los pendientes 37 y 38. La escritura falló, hubo que releer el archivo, incorporar lo ajeno y volver a escribir — que es exactamente lo que este pendiente describe: *«para guardar lo propio hay que arrastrar lo ajeno»*.

La diferencia con el caso del 2026-08-14: acá **no se perdió nada, porque la herramienta avisó** antes de sobrescribir. Con `VERSION` no avisó nadie y quedaron dos numeraciones vivas.

Eso cambia el alcance de lo que hay que decidir. `VERSION` y `CHANGELOG.md` son los que más duelen, pero el problema es de **cualquier archivo único que dos sesiones toquen a la vez**: este README, los índices del histórico, `plantillas/proyectos.md`. Las tres opciones de arriba se evalúan contra eso, no solo contra la versión.

**Sin decidir:** si el acuerdo cubre cualquier archivo compartido o se deja acotado a la versión.

## Tercer caso: casi cuesta el mismo trabajo hecho dos veces

**Ampliado el 2026-08-16**, esa misma tarde, desde el proyecto `rni-dp`.

Una sesión de otro proyecto repasó esta cola para decidir con qué seguir, propuso arrancar por el [pendiente 40](el-instalador-rellena-los-marcadores.md) —el único `P0`— y el usuario aprobó. Al ir a tocar `instalar.py` resultó que **otra sesión ya lo había ejecutado entero**: las tres funciones rellenando, la prueba escrita y corrida, y la fase `A-EP-007-HU-001` en la estación 9. Nada estaba commiteado; vivía solo en el árbol de trabajo.

En el rato que duró esa conversación también cambió lo que se había leído al empezar: había dos archivos numerados 40 y se reportaron como defecto; media hora después la otra sesión los había fundido y el sobrante ya no existía.

Lo único que evitó el choque fue mirar la hora de modificación de los archivos y el `git status` **antes** de editar. No hubo aviso de ninguna herramienta, porque no hubo escritura: el trabajo duplicado se habría descubierto al commitear.

**Sube el costo del problema.** Los dos casos anteriores eran arreglables —dos numeraciones vivas, una escritura que hubo que rehacer—. Este es trabajo entero hecho por segunda vez, y el árbol de trabajo sin commitear lo hace invisible para cualquiera que mire el historial.

**Sin decidir, además:** cómo se entera una sesión de que otra está viva sobre el mismo repositorio. Hoy solo lo dicen las fechas de los archivos, y solo si a alguien se le ocurre mirarlas.

## El límite

Esto no lo resuelve un validador: puede detectar el cruce, no evitarlo. Lo que hace falta primero es el acuerdo.

---

## Tercer caso: el número del pendiente, 2026-08-16

No fue el `CHANGELOG` esta vez. Dos sesiones abiertas a la vez crearon **tres pendientes con el número 48**: una escribió `48-el-sello-del-checklist-caduca-con-el-texto.md` y la otra `48-hu-incompletas-ep-001-cuerpo-de-reglas.md` y `48-hu-incompletas-ep-006-memoria.md`.

Se resolvió a mano —la primera cedió el número y se corrió al `52`—, y eso es justo lo que este pendiente dice que no debería hacer falta. **Amplía el alcance:** lo que dos sesiones se pisan no es solo la versión; es cualquier numeración que se calcule mirando lo que ya existe.


---

# Cómo cerró — 2026-08-18

**Se eligió la salida 1, y se escribió en su forma general:** [`20·M18`](../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md) — *lo compartido se lee un instante antes de escribirlo*.

No quedó acotada a `VERSION` porque los cuatro casos de arriba son **el mismo defecto en archivos distintos**: la versión, el registro, el número del pendiente y un índice. Una regla que solo nombrara la versión dejaría fuera a los otros tres, que ya se rompieron.

## Las tres salidas, y por qué esta

| Salida | Qué costaba |
|---|---|
| **1 · el número se pone al guardar** | ✅ **elegida** — no cambia la forma de nada |
| 2 · cada sesión escribe su entrada aparte | cambia el registro para todos los proyectos que ya lo heredaron |
| 3 · una sola sesión a la vez | prohíbe algo que la propia historia declara normal y no negociable |

## Lo que contesta la pregunta que quedaba sin decidir

El pendiente terminaba con *«cómo se entera una sesión de que otra está viva»*. **La regla quita la pregunta de encima:** releyendo al escribir no hace falta enterarse. Lo que hay que saber se lee cuando se va a usar.

## Y lo que la ejecución destapó

**El cruce se rompe de dos maneras, no de una.** Al simularlo con dos copias, la corrida sin la regla no terminó con un número repetido: terminó con **una entrada del registro perdida** — la de la segunda sesión, borrada al resolver el choque.

| Cómo se resuelve el choque | Qué queda | ¿Se ve? |
|---|---|---|
| Se conserva una de las dos entradas | falta una entrada | ❌ no |
| Se conservan las dos con el mismo número | número repetido | ✅ sí |

**El repositorio tiene la segunda:** dos entradas para la `15.4.0`, del 14 y del 15 de agosto. La primera **no se puede contar**, porque perderse es justamente no dejar rastro.

Eso es lo que hace que la regla valga más que su validador: es lo único que actúa **antes** del choque.

## Dónde quedó

- La regla: [`20·M18`](../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md)
- La comprobación: [`validadores/numeracion.py`](../../validadores/numeracion.py), dentro de `validar.py versionado` — 19 casos
- La fase: [`A-EP-002-HU-006`](../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/README.md), con los dos criterios en cumple
- La `15.4.0` repetida: **marcada en el registro, no renumerada** — un proyecto pudo haberla adoptado
