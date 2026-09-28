# Pendiente · andamio.py impone un orden de trabajo incorrecto

**Estado:** abierto, anotado el 2026-09-27. Aprobado el mismo día y bajado a historia.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-022 · andamio.py impone un orden de trabajo incorrecto](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-022-andamio-impone-un-orden-de-trabajo-incorrecto/HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md) |
| **De dónde sale** | La sesión del 2026-09-27: para crear el [pendiente 96](96-el-agente-no-conserva-el-espanol-colombiano.md), el agente creó primero el esqueleto de una HU, porque el andamio no lo dejaba de otra forma. El usuario lo corrigió |
| **Proyecto de origen** | El estándar mismo |

## El problema

`andamio.py` impone un orden de trabajo distinto del que fijó el usuario el 2026-09-27: hallazgo, pendiente, HU y fase. En [andamio.py:286-287](../validadores/andamio.py#L286-L287), `crear_pendiente` exige que la HU exista antes de registrar el pendiente, así que obliga a crear la HU antes de que el pendiente se apruebe.

Ese orden tampoco está escrito en ninguna regla: [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) arranca en el planteamiento y [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) cubre de pendiente a fase, pero ninguna nombra el tramo de hallazgo a pendiente.

## Por qué importa

La herramienta hace cumplir un orden que la regla no pide, y por eso va como `P1`. Ya pasó el 2026-09-27: el agente siguió a la herramienta y no a `F23`, y creó una HU vacía para un pendiente que el usuario no había aprobado. Una HU creada antes de su pendiente fija el alcance antes de que alguien apruebe qué falta.

## Qué falta

1. `andamio.py pendiente` con `--hu` opcional: sin historia, la ficha dice «Por asignar» y el pendiente entra al mapa de historias cuando la tenga.
2. El orden escrito en una regla. Hay dos salidas:
   - Precisar `F23` para que nombre el tramo de hallazgo a pendiente y diga que la HU nace de su épica. Es la más barata, y conviene.
   - Una regla nueva del capítulo 02, solo si precisar `F23` le agrega una segunda exigencia (`M5`).
3. La sección «Ningún pendiente vive suelto» dice que «Por asignar» vale mientras el pendiente no esté aprobado.

## El límite

No cambia cuándo se construye un pendiente: sigue necesitando su HU y su fase (`F23`). Solo cambia cuándo se puede anotar.

## Cómo se sabrá que cerró

- `python validadores/andamio.py pendiente prueba` sin `--hu` simula la creación sin error.
- `F23`, o la regla nueva, nombra el orden hallazgo, pendiente, HU y fase, con su checklist en CUMPLE.
- `python validadores/validar.py metareglas` sigue sin fallas.
