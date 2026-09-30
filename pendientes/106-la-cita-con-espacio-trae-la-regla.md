# Pendiente · La cita «00 id9» trae la regla

**Estado:** abierto. Espera la aprobación del usuario.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente. Responde a EP-005 · HU-023 · CA-09 |
| **De dónde sale** | [H-12 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

El usuario corrige con «00 id9», con espacio y en minúscula. [validadores/recuperar.py](../validadores/recuperar.py) solo reconoce la forma `00·ID9`, así que la regla citada no llega. Visto en vivo el 2026-09-29: con «00 id9» no llegó; con «00·ID9» sí.

## Por qué importa

Es la forma en que el usuario pide cumplir una regla, y el agente responde sin su texto.

## Qué falta

Que el recuperador reconozca la cita con espacio o con punto medio, en mayúscula o en minúscula, cuando el capítulo y el identificador existen.

## El límite

- No cambia cómo se eligen las reglas por la palabra de `01·C28`.

## Cómo se sabrá que cerró

- «00 id9», «00·id9» y «00·ID9» traen el texto de `00·ID9`.
- «00 zz9», que no existe, no trae nada.
