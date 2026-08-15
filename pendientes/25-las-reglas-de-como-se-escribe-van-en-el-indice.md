# Pendiente · Las reglas de cómo se escribe llegan en el índice, no puestas

**Estado:** abierto · anotado 2026-08-14 · nace del hallazgo H-6 del [2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido](../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

## El problema

[`validadores/cargador.py`](../validadores/cargador.py) reparte `base/` en dos:

- **Literal**, con el texto completo: `base/00-nucleo-blindado.md` y lo que cuelga del núcleo.
- **En índice**, una línea con la ruta, el tamaño y el título: todo lo demás.

El reparto tiene sentido para las reglas que se consultan cuando el tema lo pide. No lo tiene para las que gobiernan **cada frase que se escribe**.

El 2026-08-14 se vio en la práctica: todo lo que se escribió en la sesión incumplía [`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), la regla que prohíbe las marcas de generación automática. No fue descuido: esa regla llegaba como una línea de índice, y nada obligaba a abrirla. El agente escribía el estándar sin haber leído la parte del estándar que dice cómo se escribe.

## Qué falta

**Que vayan literales también los capítulos que gobiernan cómo se escribe cada respuesta:** [`base/00-identidad-y-rol/`](../base/00-identidad-y-rol/base.md) y [`base/01-conducta.md`](../base/01-conducta.md), con sus anexos, incluida la lista de [marcadores de generación automática](../base/00-identidad-y-rol/marcadores-de-ia.md).

Se descartaron las otras dos salidas:

| Salida | Por qué no |
|---|---|
| Cargar `base/` entero literal | Son 188 reglas: no caben, y lo que no cabe se recorta solo |
| Dejarlo como está y confiar en el `CLAUDE.md` | Es depender de que alguien se acuerde de abrir el archivo, que es la falla que este repositorio ya conoce |

## El límite

Hay que medir cuánto crece el arranque: el núcleo ya va literal, y estos dos capítulos con sus anexos pesan más. Si no cabe, se decide qué parte del capítulo `01` va puesta y qué parte queda en el índice, pero la lista de marcadores va completa: es la que se relee antes de entregar.

## Lo que ya se hizo

El `CLAUDE.md` de este repositorio ganó su paso 0, que manda cargar y obedecer `base/` al abrir la sesión, igual que se lo exige a cualquier proyecto que hereda. Eso tapa el hueco a medias: dice que hay que cargarlo, pero quien lo cumple sigue siendo el agente y no el programa.
