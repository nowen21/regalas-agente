# Pendiente · La carpeta del día nace sin su línea en el índice

**Estado:** abierto · anotado 2026-08-15 · nace de la sesión [historico-chat/2026-08-15-los-resumenes-que-faltan.md](../historico-chat/2026-08-15-los-resumenes-que-faltan.md).

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-008 — Enganche del resumen](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) — la línea del índice la tiene que escribir ese enganche, que es el que crea la carpeta |

## El problema

[`historico-chat/resumenes/README.md`](../historico-chat/resumenes/README.md) cierra con la lista de días que hay. Hoy nombra solo el 2026-08-14. El 2026-08-15 tiene su carpeta y dos resúmenes dentro, y no aparece.

Pasó lo mismo que el índice de transcripciones evita: [`validadores/historico.py`](../validadores/historico.py) agrega la línea al crear el archivo, así que ahí no se olvida. En los resúmenes, [`validadores/hook_resumen.py`](../validadores/hook_resumen.py) crea la carpeta del día y el archivo con el modelo puesto, pero no toca ninguno de los dos índices: ni el del día ni el de días.

Un resumen que no está en el índice es un resumen que nadie va a abrir. Es exactamente el defecto que el resumen existe para arreglar.

## Qué falta

**1. Que el enganche escriba las dos líneas.** Al crear la carpeta del día: su `README.md` con la tabla de sesiones, y la línea del día en el índice de arriba. Al crear el resumen: su fila en el `README.md` del día, aunque diga «sin escribir todavía».

**2. O que un validador lo compruebe.** Si se prefiere no hacerlo automático, entonces que falte la línea tiene que romper algo: un validador que compare las carpetas de `resumenes/` contra el índice, y los archivos de cada día contra el `README.md` de ese día.

**3. Poner al día lo que ya falta.** La línea del 2026-08-15 en el índice de días.

## El límite

El enganche **no escribe hallazgos** y esto no lo cambia: escribir una línea de índice con el nombre del archivo no es interpretar nada. Reconocer un hallazgo sigue siendo criterio (`13·DOC22`).

**Va con el [31](hecho/los-resumenes-de-las-sesiones-viejas.md), antes de escribirlo:** si no, cada uno de los 33 resúmenes nace fuera del índice y hay que volver a pasar por todos.
