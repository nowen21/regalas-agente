# Pendiente: la palabra clave no se reconoce en plural

| | |
|---|---|
| **De dónde sale** | [H-3 · La palabra clave no se reconoce en plural](../../reglas-de-cada-turno-sin-tokens.md), en el resumen de la sesión del 2026-10-05 |

## El problema

El usuario escribió «preguntas las pruebas están automatizadas...» y [recuperar.py](../../../../../proyectos/cimiento/core/herramientas/recuperar.py) (`trae_palabra_clave`) respondió que el mensaje no abría con una palabra de `01·C28`. La comparación es exacta: «preguntas» no coincide con «Pregunta».

## Por qué importa

El agente queda obligado a no responder un pedido cuya intención es clara, o a saltarse la regla, como pasó en esa sesión. Cada caso cuesta un mensaje más. Toca la misma lista que el [pendiente 131](../../../2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/pendiente.md), y conviene tratarlos juntos.
