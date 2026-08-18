# Pendiente · «Corrida» es jerga y no está definida

**Estado:** abierto · anotado 2026-08-15 · nace del hallazgo H-2 del [2026-08-15 · la-plantilla-del-resultado-de-pruebas](../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md).

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-010 — Glosario de la terminología](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md) — «corrida» es una entrada que le falta al glosario; va con el 21 |

## El problema

El estándar llama «corrida» a ejecutar las pruebas, y en ninguna parte dice qué es. Quien no es del oficio no sabe si una corrida es un caso, una suite o un día entero de pruebas — y de eso depende cómo se llena la columna **Ciclo** del resultado de pruebas.

En el [glosario](../base/glosario.md) la palabra solo aparece dentro de «alcance de corrida». Como término propio no existe, así que el glosario no la resuelve.

## Qué falta

**Decidir una de dos, y aplicarla completa.**

| Salida | Qué implica |
|---|---|
| Reemplazar «corrida» por «ejecución» en todo el estándar | Es lo que ya se hizo en [plantillas/planes/resultados.md](../plantillas/planes/resultados.md); falta el resto |
| Dejar la palabra y definirla en el glosario | Menos trabajo, pero sigue siendo jerga, y [`00·ID7`](../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) pide que se entienda sin saber del tema |

**Dónde sigue apareciendo:**

- [base/02-flujo-de-trabajo](../base/02-flujo-de-trabajo/base.md), incluida la regla [`F5`](../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) y su nombre «alcance de corrida»
- [base/08-pruebas.md](../base/08-pruebas.md)
- [base/glosario.md](../base/glosario.md)
- [base/20-meta-reglas/estructura-regla.md](../base/20-meta-reglas/estructura-regla.md)
- [plantillas/planes/pruebas.md](../plantillas/planes/pruebas.md), §3.5 y §12.2
- [plantillas/funcionalidad-implementada.md](../plantillas/funcionalidad-implementada.md)

## El límite

Cambiar la palabra en `F5` cambia el nombre de un concepto que otras reglas citan, «alcance de corrida». Si se cambia, se cambia en el glosario y en las citas a la vez, o quedan dos nombres para lo mismo — que es peor que la jerga.

**No urge:** no bloquea nada y no rompe nada. Va después de lo que sí tiene una fase esperando.
