# Pendiente · La sesión no tiene traza paso a paso

**Estado:** abierto, anotado el 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-016 — La traza de la sesión, paso a paso](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-016-la-traza-de-la-sesion-paso-a-paso/HU-016-la-traza-de-la-sesion-paso-a-paso.md). Lee la misma transcripción que [HU-014](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md) (el consumo) y deja un archivo en `historico-chat/` como [HU-001](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md): es de esta épica |
| **De dónde sale** | La sesión del 2026-08-20 ([resumen](../../historico-chat/resumenes/2026-08-20/sesion-5.md), H-6), al comparar el bloque `observability/` de [../notas/estructura.md](../../notas/estructura.md) con Cimiento |
| **Proyecto de origen** | El estándar mismo |

## El problema

De una sesión se conserva **qué se dijo** (la transcripción de `historico-chat/`) y **cuánto costó** (`hook_presupuesto.py`). No se conserva **qué hizo el agente paso a paso**: qué herramienta llamó, con qué, a qué hora, cuánto tardó y si falló. Esa información existe en la transcripción interna de la herramienta (bloques `tool_use` y `tool_result`, con hora y con `is_error`), pero nadie la lee: es un archivo de un megabyte de líneas JSON.

## Por qué importa

Cuando algo salga mal en un proyecto heredero (un archivo que apareció cambiado, un comando que no debió correr) habrá que reconstruir **cómo** pasó. Hoy eso es leer la transcripción entera a mano. Con nueve proyectos instalados es cuestión de semanas, no de años. Y para el propio estándar es la medida que falta junto al consumo: cuántos pasos cuesta una fase, cuáles fallan, cuál es el lento.

No bloquea nada. Pierde lo que no se mide.

## Qué falta

Un **lector**, no un enganche: `validadores/traza.py` que, dada la transcripción de una sesión, saque la línea de tiempo (orden, hora, herramienta, resumen de lo que se le pidió, duración, ok o error) y un cierre con los totales; `validar.py traza` lo expone, y con `--escribir` la deja en `historico-chat/trazas/` con el mismo nombre que el histórico de esa sesión. Cero cambios en los proyectos instalados: se corre cuando hace falta.

No copia el contenido de los resultados: ahí es donde pueden ir claves y datos. Solo la entrada, recortada, y el estado.

## El límite

No mide lo que la herramienta no registra (el razonamiento, lo que el agente leyó sin llamar a una herramienta). No reemplaza al histórico: este dice qué se habló; la traza, qué se ejecutó. Y no es un enganche: si algún día conviene escribirla sola al cerrar, es otra historia.

## Cómo se sabrá que cerró

`python validadores/validar.py traza <transcripción>` imprime la línea de tiempo de una sesión real con sus totales; con `--escribir` aparece `historico-chat/trazas/<sesión>.md` indexado; y la suite tiene el caso de una transcripción sintética con un paso fallido y uno sin respuesta.
