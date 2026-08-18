# Pendiente · Las reglas de cómo se escribe llegan en el índice, no puestas

**Estado:** **cerrado el 2026-08-15, por falso.** Anotado el 2026-08-14 · nace del hallazgo H-6 del [2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido](../../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

> ## Lo que pedía ya estaba hecho
>
> Verificado el 2026-08-15 corriendo el programa: [`validadores/cargador.py`](../../validadores/cargador.py) manda completos **todos** los capítulos que empiezan por `00-` y por `01-`, desde la versión 5.0.0. Son 73 KB de 369 KB. [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) llegaba completa.
>
> **Entonces el diagnóstico era falso.** `ID8` no se incumplió por no llegar: llegó, y se incumplió igual. Escribirlo como "llegaba en el índice" dio por cerrada una causa que nadie había mirado, y esa es la parte que hay que no repetir: **la causa se verifica corriendo el programa, no se deduce**.
>
> **Lo que sí falta, y vive en otro sitio:** el capítulo [`02 · flujo de trabajo`](../../base/02-flujo-de-trabajo/base.md) llega como índice, y ahí está lo que gobierna cada movimiento de una fase. Eso es [EP-005 · HU-010](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md).
>
> **Y lo que este pendiente nunca vio:** que la regla llegue no alcanza. Comprobar lo entregado es [EP-004 · HU-013](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md).
>
> El reparto quedó documentado y probado en la [fase A de EP-005 · HU-009](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/README.md).
>
> Lo de abajo queda tal cual, sin corregir: es lo que se creyó, y sirve para no volver a creerlo.

## El problema

[`validadores/cargador.py`](../../validadores/cargador.py) reparte `base/` en dos:

- **Literal**, con el texto completo: `base/00-nucleo-blindado.md` y lo que cuelga del núcleo.
- **En índice**, una línea con la ruta, el tamaño y el título: todo lo demás.

El reparto tiene sentido para las reglas que se consultan cuando el tema lo pide. No lo tiene para las que gobiernan **cada frase que se escribe**.

El 2026-08-14 se vio en la práctica: todo lo que se escribió en la sesión incumplía [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), la regla que prohíbe las marcas de generación automática. No fue descuido: esa regla llegaba como una línea de índice, y nada obligaba a abrirla. El agente escribía el estándar sin haber leído la parte del estándar que dice cómo se escribe.

## Qué falta

**Que vayan literales también los capítulos que gobiernan cómo se escribe cada respuesta:** [`base/00-identidad-y-rol/`](../../base/00-identidad-y-rol/base.md) y [`base/01-conducta.md`](../../base/01-conducta.md), con sus anexos, incluida la lista de [marcadores de generación automática](../../base/00-identidad-y-rol/marcadores-de-ia.md).

Se descartaron las otras dos salidas:

| Salida | Por qué no |
|---|---|
| Cargar `base/` entero literal | Son 188 reglas: no caben, y lo que no cabe se recorta solo |
| Dejarlo como está y confiar en el `CLAUDE.md` | Es depender de que alguien se acuerde de abrir el archivo, que es la falla que este repositorio ya conoce |

## El límite

Hay que medir cuánto crece el arranque: el núcleo ya va literal, y estos dos capítulos con sus anexos pesan más. Si no cabe, se decide qué parte del capítulo `01` va puesta y qué parte queda en el índice, pero la lista de marcadores va completa: es la que se relee antes de entregar.

## Lo que ya se hizo

El `CLAUDE.md` de este repositorio ganó su paso 0, que manda cargar y obedecer `base/` al abrir la sesión, igual que se lo exige a cualquier proyecto que hereda. Eso tapa el hueco a medias: dice que hay que cargarlo, pero quien lo cumple sigue siendo el agente y no el programa.
