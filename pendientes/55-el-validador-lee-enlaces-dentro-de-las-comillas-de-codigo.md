# Pendiente · El validador lee como enlace lo que está entre comillas de código

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-6 del [resumen de la sesión 7](../historico-chat/resumenes/2026-08-16/sesion-7.md) |
| **Misma familia que** | El punto 1 del [33](33-defectos-que-destaparon-los-resumenes-viejos.md), donde da por rotos los enlaces con espacios |

## El problema

Un plan de pruebas escribió, entre comillas invertidas, **el texto que la prueba tenía que encontrar**:

```
| 1 | Comprobar el estado inicial | Dice `[historico-chat/2026-01-02-sesion.md](../../2026-01-02-sesion.md)` |
```

Eso no es un enlace: es una muestra de lo que el caso comprueba. `enlaces.py` lo leyó como enlace y lo reportó roto, dos veces.

## Por qué importa

Deja dos salidas, y las dos son malas: **redactar torcido** para que el validador no se queje —que fue lo que se hizo—, o **aprender a ignorar** sus hallazgos. Lo segundo se contagia al resto de lo que reporta, incluido lo que sí es cierto.

## Qué falta

Que `enlaces.py` no busque enlaces dentro de un bloque de código ni de un tramo entre comillas invertidas. Es lo mismo que ya hacen los lectores de Markdown.

**Conviene hacerlo junto con el punto 1 del 33** —el `unquote` de los enlaces con espacios—: mismo archivo, misma clase de falso positivo, y una sola fase.

## Cómo se sabrá que cerró

Un documento que muestre un enlace de ejemplo entre comillas de código no produce ningún hallazgo.
