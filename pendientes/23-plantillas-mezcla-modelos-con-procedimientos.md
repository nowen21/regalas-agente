# Pendiente · La carpeta de plantillas mezcla modelos con procedimientos

**Estado:** abierto · anotado 2026-08-14 · nace del hallazgo H-7 del [2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido](../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-006 — Procedimientos por rol](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-006-procedimientos-por-rol/HU-006-procedimientos-por-rol.md) — lo que está mal ubicado es un procedimiento, no un modelo |

## El problema

`plantillas/` dice, por su nombre, que todo lo de adentro es un modelo que alguien llena. Al aplicar [`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), cuatro de sus treinta archivos quedaron sin una sola marca, y hubo que declararlos como excepción en una lista escrita a mano.

**Al mirar el instalador, tres de los cuatro resultaron estar bien donde están.** No son modelos, pero tampoco están fuera de sitio:

| Archivo | Qué es | Veredicto |
|---|---|---|
| [`plantillas/historico-chat.md`](../plantillas/historico-chat.md) | La fuente con la que [`validadores/instalar.py`](../validadores/instalar.py) **genera** el `historico-chat/README.md` de cada proyecto | Se queda. No lo llena una persona, lo llena un programa |
| [`plantillas/memoria.md`](../plantillas/memoria.md) | Lo mismo, para `historico-chat/memory/memory.md` | Se queda |
| [`plantillas/prompts/prompt-base-usuario.md`](../plantillas/prompts/prompt-base-usuario.md) | El molde con que el usuario pide trabajo. Se llena escribiendo el pedido | Se queda: ya está separado en su subcarpeta |
| [`plantillas/retrodocumentacion.md`](../plantillas/retrodocumentacion.md) | El procedimiento de seis pasos de [`13·DOC6`](../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md). Se lee y se sigue | **Está mal ubicado** |

## Qué falta

**1. Mover `retrodocumentacion.md` al capítulo 13**, al lado de la regla que lo exige, como ya está [`render-local-de-md.md`](../base/13-documentacion/render-local-de-md.md). Ese capítulo ya tiene el precedente: el anexo que no es regla vive junto a su regla.

**2. Escribir en el índice de `plantillas/` que ahí viven dos cosas:** los modelos que alguien llena a mano, y las fuentes con las que el instalador genera archivos. Con eso, un archivo sin marca deja de necesitar una lista de excepciones: se sabe por qué categoría no la lleva.

## El límite

Mover el procedimiento cambia una ruta que puede estar citada. Antes de moverlo se buscan las citas y se corrigen en el mismo cambio, o quedan enlaces rotos.

## Lo que este pendiente ya no dice

La primera versión proponía una subcarpeta `plantillas/procedimientos/` o mover los cuatro a `base/`. Las dos sobran: tres de los cuatro tienen su motivo, y el cuarto tiene un sitio que ya existe.
