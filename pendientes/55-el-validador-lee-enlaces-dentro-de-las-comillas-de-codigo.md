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
| [`base/20-meta-reglas/estructura-regla.md:57`](../base/20-meta-reglas/estructura-regla.md) | `G9` sin enlace | Ejemplo de lo que **no** hay que hacer: «ponerle `G9` a una regla del capítulo de pruebas». ~~**`G9` no existe**~~ — **corregido el 2026-08-17: sí existe**, es [`base/09-git.md`](../base/09-git.md) *La historia de usuario es la unidad del commit*. Sigue siendo falso positivo, pero por ser ejemplo y no por no existir |
| [`base/00-identidad-y-rol/reglas/ID9-…`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)`:32` | `ID7` sin enlace | Segunda mención en el mismo párrafo; la primera **sí** lleva enlace |
| [`base/09-git.md:107`](../base/09-git.md) | `G1` mal apuntada | **Sí** lleva enlace, a un ancla del mismo archivo — que es lo correcto |

**Lo que esto agrega al pendiente:** el hueco no está solo en `enlaces.py`. `citas.py` no distingue una **cita** de un **identificador nombrado como ejemplo**, y no hay forma de distinguirlos sin mirar el contexto. Cuatro de los cinco casos son eso.

**Lo que se hizo el 2026-08-17, y lo que no.** No se editó `base/`: está bien escrito, y torcerlo para callar al validador es la salida mala que este pendiente ya describe. La prueba quedó marcada como fallo esperado, con los cinco casos explicados en su propio texto, para que avise sola cuando este pendiente cierre.

## Y es peor: el reparador **escribiría** el error — medido el 2026-08-17

Lo de arriba es que el validador **reporta** de más. Al cerrar el [53](hecho/ningun-validador-termina-en-silencio.md) se corrió `citas.py` en simulación, que es su modo por omisión, y esto es lo que haría:

```
$ python validadores/citas.py
213 reglas indexadas en base/

  1 reparadas                  base/09-git.md
  2 enlazadas                  base/glosario.md
  1 enlazadas                  base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md
  1 enlazadas                  base/20-meta-reglas/estructura-regla.md

4 enlazadas · 1 reparadas · 4 archivos (simulado; agrega --aplicar)
```

**Las cinco están mal, y son exactamente los cinco falsos positivos de este pendiente.** Con `--aplicar`, `citas.py` enlazaría los cuatro identificadores que son ejemplos y «repararía» el enlace de `G1`, que apunta a un ancla del mismo archivo y está bien como está.

Eso convierte el daño en otra cosa. Este pendiente decía que el validador enseña a **ignorar** sus hallazgos; el reparador los **escribe en `base/`**. Y lo haría en una sola corrida, sin que nadie revisara las cinco.

**Al cerrar este pendiente hay que comprobar las dos mitades:** que `enlaces.py` y `citas.py` no reporten los cinco, y que `citas.py --aplicar` no los toque.

### El caso de `G1` es distinto de los otros cuatro, y se arregla aparte

Los cuatro de la tabla son **ejemplos** y no hay forma de distinguirlos sin mirar el contexto. El quinto no:

```
Concreta a [`G1`](#g1--commits-atómicos-un-solo-propósito), que pide un propósito por commit
```

Es un enlace a un ancla **del mismo archivo**, que es lo correcto, y `citas.py` lo da por mal apuntado porque compara contra la ruta completa. **Ese sí es determinista**: si la regla citada vive en el archivo donde está la cita, el ancla suelta vale. No necesita ninguna convención nueva, y se puede arreglar sin decidir nada.

Lo mismo pasa con la segunda mención de `ID7` dentro del mismo párrafo, donde la primera **sí** lleva su enlace: exigir el enlace dos veces en tres líneas es ruido, y también se puede decidir sin convención.

**Quedan tres, no cinco**, y esos tres sí necesitan que alguien decida cómo se marca un identificador nombrado como ejemplo.

## Qué falta

Que `enlaces.py` no busque enlaces dentro de un bloque de código ni de un tramo entre comillas invertidas. Es lo mismo que ya hacen los lectores de Markdown.

Que `citas.py` acepte el ancla del mismo archivo y no exija el enlace en la segunda mención del mismo párrafo. **Esas dos son deterministas y no esperan a nadie.**

Y que `citas.py` no cuente como cita un identificador que aparece **como ejemplo**. Al cerrarlo, quitarle el `expectedFailure` a `Citas.test_no_queda_ninguna_cita_suelta_en_base`.

**Conviene hacerlo junto con el punto 1 del 33** —el `unquote` de los enlaces con espacios—: mismo archivo, misma clase de falso positivo, y una sola fase.

## Cómo se sabrá que cerró

Un documento que muestre un enlace de ejemplo entre comillas de código no produce ningún hallazgo.
