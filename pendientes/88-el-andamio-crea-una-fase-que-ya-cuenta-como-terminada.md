# Pendiente · El andamio crea los cinco documentos vacíos, y con eso una fase recién abierta ya cuenta como terminada

**Estado:** abierto, anotado el 2026-08-27.

| | |
|---|---|
| **Historia de usuario** | Por crear. Sale de este pendiente cuando se apruebe |
| **De dónde sale** | La señal `S-053`, que cobró **tres veces el mismo día** |
| **Proyecto de origen** | El estándar mismo |

## El problema

El inventario de historias cuenta una fase como terminada cuando **existen sus cinco documentos**. No mira si dicen algo.

El andamio que abre una fase crea los cinco de una vez, con el molde adentro. **Así que una fase recién abierta, sin una línea de trabajo hecha, ya cuenta como terminada.**

Se midió: cuatro fases figuraban completas y su `estado-fase` decía **«Ejecutada y cerrada»**. Su documento de cierre era el molde en blanco, con **31 marcadores sin reemplazar cada uno** — todavía decía `«2-4 líneas en lenguaje claro»` y `AAAA-MM-DD`.

## Cobró tres veces en un día

| Cuándo | Qué pasó |
|---|---|
| Al buscar fases con criterios en rojo | Cuatro figuraban cerradas y eran moldes en blanco |
| Al crear la `HU-021` para arreglar el conteo | **La historia contaba como terminada** antes de escribir una línea |
| Al crear su fase `B` | Volvió a meter esa misma historia entre las que «no dicen si cumplen», y **movió la base de una medición en curso** |

**La tercera es la que más enseña.** La fase que se abrió para arreglar el conteo le agregó un caso al conteo, y por poco se atribuye la diferencia a un error de cuenta anterior. Lo salvó que el plan exigía un número exacto (`S-056`).

## Por qué importa

Es el mismo defecto del inventario a mano, **un nivel más adentro**. Antes el número se copiaba y se desfasaba; ahora se calcula bien y **cuenta lo que no debe**.

Y el sesgo va siempre en la misma dirección: **optimista**. Abrir trabajo hace que el avance se vea mejor.

## Qué falta

**La medida que lo destapa ya existe y funciona:** contar los marcadores del molde que quedaron sin reemplazar. Se probó sobre el árbol real y **separa sin falsos positivos** cuatro documentos con 31 marcadores de doce con cinco a siete, que son comillas angulares de prosa normal.

Lo que falta es decidir dónde entra:

1. **Que el inventario no cuente un documento que sigue siendo el molde.** Es lo más directo, y usa la medida que ya se probó.
2. **Que el andamio no cree los cinco documentos de entrada**, sino cada uno al llegar su estación. Evita el problema en vez de detectarlo, pero cambia cómo se trabaja hoy.
3. **Que un validador avise** cuando un documento con muchos marcadores conviva con un `estado-fase` que dice «cerrada». No lo arregla, lo hace visible.

**La 1 y la 3 no se estorban.** La 2 es la que hay que discutir, porque toca el hábito.

## El límite

Este pendiente **no** cubre:

- **Los cuatro cierres que estaban en blanco.** Se escribieron el 2026-08-27. Eso tapó los casos, no la causa.
- **Las 15 historias que no dicen si cumplen.** Esas de verdad no lo dicen, y se resuelven escribiendo su veredicto.
- **Que nadie reporte el campo `Estado` faltante.** Es otra deuda, anotada en su fase (`S-050`).

## Cómo se sabrá que cerró

Que abrir una fase nueva con el andamio **no mueva** el número de historias terminadas, y que se pueda comprobar corriendo el inventario antes y después de abrirla.
