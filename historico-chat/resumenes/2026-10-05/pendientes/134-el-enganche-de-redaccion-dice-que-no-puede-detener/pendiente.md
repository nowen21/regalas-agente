# Pendiente: el enganche de redacción dice que no puede detener

| | |
|---|---|
| **De dónde sale** | [H-2 · El enganche de redacción dice que no puede detener](../../reglas-de-cada-turno-sin-tokens.md), en el resumen de la sesión del 2026-10-05 |

## El problema

La descripción de [hook_redaccion.py](../../../../../adaptadores/claude-code/hook_redaccion.py) dice que mide y no detiene porque, cuando corre, «el texto ya salió: no hay nada que bloquear». El motivo real es otro: el usuario decidió el 2026-08-31 que `00·ID9` se mide sin detener ([EP-005·HU-012](../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md), RN-05). Un enganche `Stop` sí puede devolver `decision: block`.

## Por qué importa

Quien lea el comentario cree que detener es imposible y no sabe que fue una decisión del usuario, ni dónde quedó escrita.

## Qué se corrige

Solo el comentario: que dé el motivo real y enlace la HU-012. El comportamiento no cambia. Detener o no detener lo decide el usuario, y hoy está decidido.
