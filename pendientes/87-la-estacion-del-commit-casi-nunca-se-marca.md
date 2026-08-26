# Pendiente · La estación del commit casi nunca se marca, porque ocurre después de que el agente termina

**Estado:** abierto, anotado el 2026-08-25.

| | |
|---|---|
| **Historia de usuario** | Por crear. Sale de este pendiente cuando se apruebe |
| **De dónde sale** | La plataforma, al calcular el estado de este repositorio, dijo que tenía **41 fases abiertas**. Al mirarlas, 23 estaban cerradas de hecho |
| **Proyecto de origen** | El estándar mismo |

## El problema

La plataforma calculó el estado de este repositorio y dijo: **41 de 128 fases siguen abiertas**. Al mirar una por una, el reparto era este:

| Estación | Cuántas | Qué significa de verdad |
|---|---|---|
| **8 · cierre documental** | **23** | **Están cerradas.** Su documento de cierre está escrito y guardado en git |
| 4 · pausa y presentación | 7 | Esperando aprobación de sus planes |
| 6 · ejecución continua | 7 | Construcción a medias |
| 7 · pruebas | 2 | Construidas, sin veredicto escrito |
| 8, con su hash anotado | 1 | Cerrada, contada mal por otro motivo |

**23 de 41 no eran trabajo pendiente: eran marcas pendientes.** Se comprobó contra `git log`: los 23 documentos de cierre están guardados en el repositorio, con su commit y su fecha.

## Por qué pasa

La estación 9 del ciclo es **«commit único»**, y el commit ocurre **después** de que el agente termina de escribir. En ese momento el agente ya reportó, el usuario aprueba, se commitea, y **nadie vuelve al `estado-fase.md` a marcar la casilla**.

No es descuido: es la forma del ciclo. La última estación es la única que se cumple fuera del momento en que se está escribiendo el documento que la registra.

## Por qué importa

**Cualquier medición sobre el estado del proyecto sale falsa.** Hoy son 41 abiertas donde hay 17. Un 58% de error en el único número que dice cuánto trabajo hay colgando.

Y el daño crece: cada fase que se cierre de aquí en adelante suma otra marca sin poner, así que el número se aleja cada mes.

**No lo arregla haber corregido las 23.** Eso se hizo el 2026-08-25, leyendo el historial. Si no cambia nada más, el año que viene habrá otras veintitantas.

## Qué falta

Hay tres salidas, y conviene decidir cuál antes de construir:

1. **Que el hash lo ponga un programa.** Un enganche de después del commit que busque la fase de esa rama y le escriba el hash y la estación. Es lo único que no depende de que alguien se acuerde.
2. **Que la estación 9 no exista como casilla por marcar.** Si el commit es lo último y no hay nada después, la fase podría darse por cerrada al pasar la estación 8, y el hash quedaría como dato que se anota si se puede.
3. **Que un validador avise.** Un programa que compare: fases en estación 8 cuyo cierre ya está en git. Eso no lo arregla, pero lo hace visible cada vez.

**La 1 y la 3 no se estorban.** La 1 evita el problema; la 3 lo detecta si la 1 falla.

## El límite

Este pendiente **no** cubre:

- **Las 17 fases que sí tienen trabajo pendiente.** Esas son trabajo, no marcas.
- **Las 5 fases cuya estación no se deja leer.** Es otro problema, y también lo destapó la plataforma.
- **Corregir las 23**, que ya se hizo el 2026-08-25 con el hash verificado en el historial.

## Cómo se sabrá que cerró

Que la plataforma calcule el estado de este repositorio dos meses después de cerrar una fase, y el número de fases abiertas coincida con las que de verdad tienen trabajo pendiente, sin que nadie lo haya corregido a mano.
