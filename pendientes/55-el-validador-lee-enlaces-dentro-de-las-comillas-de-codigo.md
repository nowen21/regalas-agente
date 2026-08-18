# Pendiente · El validador lee como enlace lo que está entre comillas de código

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-005 — Comprobar los enlaces y las citas a reglas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) — es un falso positivo de ese mismo validador, contra su RN-01 y su RN-04 |
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

## No es solo `enlaces.py`: `citas.py` tiene el mismo hueco — medido el 2026-08-17

Al correr la suite completa mientras se ejecutaban las fases del [48](48-inventario-hu.md), `Citas.test_no_queda_ninguna_cita_suelta_en_base` reportó **cinco citas sueltas en `base/`**. Se revisaron una por una y **las cinco son falsos positivos**:

| Dónde | Qué reporta | Qué es de verdad |
|---|---|---|
| [`base/glosario.md:68`](../base/glosario.md) | `C20` y `F12` sin enlace | Ejemplos dentro de la prosa: «el código corto de una regla, **como `C20` o `F12`**» |
| [`base/20-meta-reglas/estructura-regla.md:57`](../base/20-meta-reglas/estructura-regla.md) | `G9` sin enlace | Ejemplo de lo que **no** hay que hacer: «ponerle `G9` a una regla del capítulo de pruebas». **`G9` no existe** |
| [`base/00-identidad-y-rol/reglas/ID9-…`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)`:32` | `ID7` sin enlace | Segunda mención en el mismo párrafo; la primera **sí** lleva enlace |
| [`base/09-git.md:107`](../base/09-git.md) | `G1` mal apuntada | **Sí** lleva enlace, a un ancla del mismo archivo — que es lo correcto |

**Lo que esto agrega al pendiente:** el hueco no está solo en `enlaces.py`. `citas.py` no distingue una **cita** de un **identificador nombrado como ejemplo**, y no hay forma de distinguirlos sin mirar el contexto. Cuatro de los cinco casos son eso.

**Lo que se hizo el 2026-08-17, y lo que no.** No se editó `base/`: está bien escrito, y torcerlo para callar al validador es la salida mala que este pendiente ya describe. La prueba quedó marcada como fallo esperado, con los cinco casos explicados en su propio texto, para que avise sola cuando este pendiente cierre.

## Qué falta

Que `enlaces.py` no busque enlaces dentro de un bloque de código ni de un tramo entre comillas invertidas. Es lo mismo que ya hacen los lectores de Markdown.

Y que `citas.py` no cuente como cita un identificador que aparece **como ejemplo**. Al cerrarlo, quitarle el `expectedFailure` a `Citas.test_no_queda_ninguna_cita_suelta_en_base`.

**Conviene hacerlo junto con el punto 1 del 33** —el `unquote` de los enlaces con espacios—: mismo archivo, misma clase de falso positivo, y una sola fase.

## Cómo se sabrá que cerró

Un documento que muestre un enlace de ejemplo entre comillas de código no produce ningún hallazgo.
