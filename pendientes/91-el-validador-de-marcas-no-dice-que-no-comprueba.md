# Pendiente · El validador de marcas dice «cero» sobre lo que no mira

**Estado:** abierto, anotado el 2026-08-30.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-024](../documentacion/epicas/EP-004-comprobacion-automatica/HU-024-el-validador-dice-que-no-comprueba/HU-024-el-validador-dice-que-no-comprueba.md), aprobada el 2026-08-30 |
| **De dónde sale** | El hallazgo `H-3` de la sesión [2026-08-28 · plantilla-manual-instalacion](../historico-chat/resumenes/2026-08-28/plantilla-manual-instalacion.md), y el agente volvió a caer en él el mismo día |
| **Proyecto de origen** | El estándar mismo |

## El problema

[`validadores/marcas.py`](../validadores/marcas.py) cuenta las marcas de las secciones 2 y 3 del anexo [`marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md): la raya larga, el punto medio, los caracteres invisibles. De la sección 4 en adelante hace falta leer, y el propio anexo lo dice.

**La salida no distingue las dos cosas.** Cuando el programa no encuentra nada imprime:

```
0 en 0 archivos
```

Y eso se lee como «el documento cumple `00·ID8`», que es más de lo que el programa comprobó.

Hay un segundo filo, y es el que hizo daño: **el subcomando `validar.py marcas` solo recorre `base/` y `plantillas/`.** Sobre `documentacion/` devuelve cero porque no mira, no porque esté limpio.

**Pasó de verdad el 2026-08-30.** El agente corrió `validar.py marcas`, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de veinticinco documentos nuevos. El enganche del commit, que sí lee lo que entra al índice, encontró trece avisos en esos mismos archivos. La afirmación falsa quedó publicada, y hubo que corregirla en el commit siguiente.

## Por qué importa

No bloquea nada, y ese es el problema: **un cero que se lee como aprobado enseña a no volver a mirar.** Cada documento que pasa con ese cero acumula deuda de `00·ID8` que nadie ve hasta que alguien lo lee entero, y para entonces son cientos de archivos.

El daño concreto ya medido: un mensaje de commit publicado afirmando algo falso sobre la calidad de veinticinco documentos.

## Qué falta

Dos cosas, y la primera sola no alcanza:

1. **Que la salida diga qué no comprobó.** Al terminar, nombrar las secciones del anexo que el programa no cuenta y que piden lectura. Cuesta poco.
2. **Que `validar.py marcas` diga sobre qué recorrió.** O que amplíe su alcance a `documentacion/`, o que imprima qué carpetas miró. Hoy no dice ninguna de las dos, y por eso su cero se confunde con el del árbol entero.

La segunda salida es la que evita el caso que ya ocurrió. Ampliar el alcance es más trabajo y produciría ruido de entrada, porque `documentacion/` arrastra deuda vieja; decir qué se recorrió cuesta una línea y cierra el engaño.

## El límite

Esto **no** convierte el validador en comprobación completa de `00·ID8`. Las secciones 4 a 8 del anexo se leen, y seguirán leyéndose. Lo que se pide es que el programa deje de sugerir lo contrario.

## Cómo se sabrá que cerró

Correr `python validadores/validar.py marcas` sobre un árbol limpio y que la salida nombre, con sus palabras, qué carpetas recorrió y qué secciones del anexo no cuenta. Y que un documento de `documentacion/` con una raya larga en prosa no pueda pasar por ese comando sin que quede dicho que ahí no se miró.
