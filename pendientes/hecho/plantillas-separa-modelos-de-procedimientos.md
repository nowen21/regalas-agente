# Pendiente · La carpeta de plantillas mezcla modelos con procedimientos

**Estado:** **cerrado** el 2026-08-17. Anotado el 2026-08-14 · nace del hallazgo H-7 del [2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido](../../historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md).

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-006 — Procedimientos por rol](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-006-procedimientos-por-rol/HU-006-procedimientos-por-rol.md) — lo que está mal ubicado es un procedimiento, no un modelo |

## El problema

`plantillas/` dice, por su nombre, que todo lo de adentro es un modelo que alguien llena. Al aplicar [`13·DOC19`](../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), cuatro de sus treinta archivos quedaron sin una sola marca, y hubo que declararlos como excepción en una lista escrita a mano.

**Al mirar el instalador, tres de los cuatro resultaron estar bien donde están.** No son modelos, pero tampoco están fuera de sitio:

| Archivo | Qué es | Veredicto |
|---|---|---|
| [`plantillas/historico-chat.md`](../../plantillas/historico-chat.md) | La fuente con la que [`validadores/instalar.py`](../../validadores/instalar.py) **genera** el `historico-chat/README.md` de cada proyecto | Se queda. No lo llena una persona, lo llena un programa |
| [`plantillas/memoria.md`](../../plantillas/memoria.md) | Lo mismo, para `historico-chat/memory/memory.md` | Se queda |
| [`plantillas/prompts/prompt-base-usuario.md`](../../plantillas/prompts/prompt-base-usuario.md) | El molde con que el usuario pide trabajo. Se llena escribiendo el pedido | Se queda: ya está separado en su subcarpeta |
| [`plantillas/retrodocumentacion.md`](../../base/13-documentacion/retrodocumentacion.md) | El procedimiento de seis pasos de [`13·DOC6`](../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md). Se lee y se sigue | **Está mal ubicado** |

## Qué falta

**1. Mover `retrodocumentacion.md` al capítulo 13**, al lado de la regla que lo exige, como ya está [`render-local-de-md.md`](../../base/13-documentacion/render-local-de-md.md). Ese capítulo ya tiene el precedente: el anexo que no es regla vive junto a su regla.

**2. Escribir en el índice de `plantillas/` que ahí viven dos cosas:** los modelos que alguien llena a mano, y las fuentes con las que el instalador genera archivos. Con eso, un archivo sin marca deja de necesitar una lista de excepciones: se sabe por qué categoría no la lleva.

## El límite

Mover el procedimiento cambia una ruta que puede estar citada. Antes de moverlo se buscan las citas y se corrigen en el mismo cambio, o quedan enlaces rotos.

## Lo que este pendiente ya no dice

La primera versión proponía una subcarpeta `plantillas/procedimientos/` o mover los cuatro a `base/`. Las dos sobran: tres de los cuatro tienen su motivo, y el cuarto tiene un sitio que ya existe.

---

# Cómo cerró — 2026-08-17

**1 · El procedimiento se movió al capítulo 13.** `retrodocumentacion.md` vive ahora en [base/13-documentacion/retrodocumentacion.md](../../base/13-documentacion/retrodocumentacion.md), al lado de la regla que lo exige, siguiendo el precedente de [base/13-documentacion/render-local-de-md.md](../../base/13-documentacion/render-local-de-md.md).

**El límite que este pendiente ponía se respetó, y con herramienta en vez de a mano.** Decía: «antes de moverlo se buscan las citas y se corrigen en el mismo cambio, o quedan enlaces rotos». Eran **12 enlaces en 12 archivos**, y los arrastró [validadores/cerrar.py](../../validadores/cerrar.py) —la pieza que nació para el [54](cerrar-un-pendiente-arrastra-sus-citas.md)—, que para esto se generalizó: `mover()` sirve para cualquier `.md`, no solo para un pendiente.

**Y una que el pendiente no había previsto:** el archivo citaba con `«RUTA-ESTANDAR»` porque vivía en `plantillas/`, que **sí** se copia dentro de los proyectos. En `base/` no se copia, así que sus tres citas pasaron a rutas relativas. Moverlo entre carpetas no es solo cambiarlo de sitio: cambia con qué convención se escriben sus enlaces.

**2 · El índice de `plantillas/` dice qué vive ahí.** No existía. Ahora está en [plantillas/README.md](../../plantillas/README.md), con las dos categorías —modelo y fuente de generación—, cuáles son las tres fuentes, y la pregunta que las separa.

Con eso, un archivo sin marcas deja de necesitar una lista de excepciones: se sabe por qué categoría no las lleva. Que era el punto — **una lista de excepciones escrita a mano envejece sin que nadie la mire.**
