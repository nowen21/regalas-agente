# Pendiente · «Corrida» es jerga y no está definida

**Estado:** cerrado 2026-08-18 · anotado 2026-08-15 · nace del hallazgo H-2 del [2026-08-15 · la-plantilla-del-resultado-de-pruebas](../../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md).

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-010 — Glosario de la terminología](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md) — «corrida» es una entrada que le falta al glosario; va con el 21 |

## El problema

El estándar llama «corrida» a ejecutar las pruebas, y en ninguna parte dice qué es. Quien no es del oficio no sabe si una corrida es un caso, una suite o un día entero de pruebas — y de eso depende cómo se llena la columna **Ciclo** del resultado de pruebas.

En el [glosario](../../base/glosario.md) la palabra solo aparece dentro de «alcance de corrida». Como término propio no existe, así que el glosario no la resuelve.

## Qué falta

**Decidir una de dos, y aplicarla completa.**

| Salida | Qué implica |
|---|---|
| Reemplazar «corrida» por «ejecución» en todo el estándar | Es lo que ya se hizo en [../plantillas/planes/resultados.md](../../plantillas/planes/resultados.md); falta el resto |
| Dejar la palabra y definirla en el glosario | Menos trabajo, pero sigue siendo jerga, y [`00·ID7`](../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) pide que se entienda sin saber del tema |

**Dónde sigue apareciendo:**

- [../base/02-flujo-de-trabajo/base.md](../../base/02-flujo-de-trabajo/base.md), incluida la regla [`F5`](../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) y su nombre «alcance de corrida»
- [../base/08-pruebas.md](../../base/08-pruebas.md)
- [../base/glosario.md](../../base/glosario.md)
- [../base/20-meta-reglas/estructura-regla.md](../../base/20-meta-reglas/estructura-regla.md)
- [../plantillas/planes/pruebas.md](../../plantillas/planes/pruebas.md), §3.5 y §12.2
- [../plantillas/funcionalidad-implementada.md](../../plantillas/funcionalidad-implementada.md)

## El límite

Cambiar la palabra en `F5` cambia el nombre de un concepto que otras reglas citan, «alcance de corrida». Si se cambia, se cambia en el glosario y en las citas a la vez, o quedan dos nombres para lo mismo — que es peor que la jerga.

**No urge:** no bloquea nada y no rompe nada. Va después de lo que sí tiene una fase esperando.


---

# Cómo cerró — 2026-08-18

**El usuario eligió la primera salida: «corrida» sale del estándar.** Quedó «ejecución» en los ocho archivos que se heredan.

## No fue un reemplazo a ciegas

**El verbo se queda.** *«Las pruebas se corren»*, *«correr la suite»* se entienden sin saber del oficio, y `00·ID7` no pide cambiar eso. Lo que era jerga es el **sustantivo**: nadie definía qué es una corrida, y de eso dependía cómo se llena la columna **Ciclo** del resultado de pruebas.

Y quedó una a propósito: *«la numeración **corrida** entre sesiones»*, en [`plantillas/sesion.md`](../../plantillas/sesion.md). Es otro sentido de la palabra —seguida, consecutiva— y cambiarlo habría dicho otra cosa.

| Dónde | Qué decía | Qué dice |
|---|---|---|
| [`base/glosario.md`](../../base/glosario.md) | Alcance de corrida | **Alcance de ejecución** |
| [`02·F5`](../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) | la corrida que cierra una fase · la corrida global | la **ejecución** que cierra una fase · la **ejecución** global |
| [`base/02-flujo-de-trabajo/base.md`](../../base/02-flujo-de-trabajo/base.md) | fuera de la corrida | fuera de la **ejecución** |
| [`base/08-pruebas.md`](../../base/08-pruebas.md) | se crea y destruye por corrida | se crea y destruye por **ejecución** |
| [`base/20-meta-reglas/estructura-regla.md`](../../base/20-meta-reglas/estructura-regla.md) | una migración de una sola corrida | una sola **ejecución** |
| [`plantillas/planes/pruebas.md`](../../plantillas/planes/pruebas.md) | Alcance de la corrida automatizada | Alcance de la **ejecución** automatizada |
| [`plantillas/funcionalidad-implementada.md`](../../plantillas/funcionalidad-implementada.md) | Suites corridas | Suites **ejecutadas** |
| [`plantillas/planes/resultados.md`](../../plantillas/planes/resultados.md) | tres corridas | tres **ejecuciones** |

## El sello de `F5` se volvió a aplicar

Cambiarle el texto a una regla **anula** su resultado del checklist, aunque el cambio sea de una palabra. Se volvió a aplicar el 2026-08-18: **la fila 4 sigue en ❌ por el mismo motivo de antes**, que es de quién es el tema *pruebas* y no tiene nada que ver con la redacción.

## Lo que no se tocó

La palabra sigue viva en comentarios y docstrings de [`validadores/`](../../validadores/), que no se hereda. No estorba a nadie que use el estándar; si alguna vez estorba, es un renglón.
