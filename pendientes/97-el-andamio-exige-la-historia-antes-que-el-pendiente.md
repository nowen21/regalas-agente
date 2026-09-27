# Pendiente · El andamio exige la historia antes que el pendiente

**Estado:** abierto, anotado el 2026-09-27.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente. La épica candidata es la que tenga `andamio.py` y el flujo de pendientes a su cargo |
| **De dónde sale** | La sesión del 2026-09-27: al crear el [pendiente 96](96-la-norma-del-espanol-de-colombia-no-tiene-regla.md), el agente creó primero el esqueleto de una HU porque el andamio no lo dejaba de otra forma. El usuario lo corrigió |
| **Proyecto de origen** | El estándar mismo |

## El problema

El orden que fijó el usuario el 2026-09-27 es este:

```
hallazgo → pendiente → HU → fase
```

- El **hallazgo** puede ser del propio agente o de otro proyecto.
- La **HU** siempre sabe de qué épica es hija: no hay HU sueltas.

**`andamio.py` obliga al orden contrario.** En [andamio.py:281-282](../validadores/andamio.py#L281-L282), `crear_pendiente` falla con «no existe la historia» si la HU que recibe `--hu` no está creada. Para anotar un pendiente hay que inventarle antes su historia.

**Y el orden completo no está escrito en ninguna regla:**

- [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) arranca en el planteamiento y no nombra el hallazgo ni el pendiente.
- [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) cubre pendiente → HU → fase.
- El tramo hallazgo → pendiente no lo cubre nadie.
- La sección «Ningún pendiente vive suelto» del [índice](README.md) pide que cada pendiente declare su historia, y no dice que la historia puede quedar por asignar mientras el pendiente se aprueba.

## Por qué importa

**Dice algo falso**, por eso va como `P1`: la herramienta hace cumplir un orden que la regla no pide. Cobró el 2026-09-27. El agente siguió a la herramienta y no a `F23`, y creó una HU vacía para un pendiente que el usuario todavía no había aprobado.

Una HU creada antes del pendiente se escribe sin que nadie haya aprobado qué falta, así que termina fijando el alcance antes de tiempo.

## Qué falta

1. **`andamio.py pendiente` sin `--hu` obligatorio.** Sin historia, la ficha dice «Por asignar» y el pendiente no entra al mapa de historias hasta tenerla. Con `--hu`, sigue como hoy.
2. **El orden, escrito donde se lee.** Hay dos salidas:
   - **Precisar `F23`** para que nombre el tramo hallazgo → pendiente y diga que la HU nace de la épica que le corresponde. Es más barato y deja el orden junto a la regla que ya lo cubre a medias.
   - **Una regla nueva del capítulo 02.** Solo hace falta si precisar `F23` le mete una segunda exigencia (`M5`).

   Conviene la primera.
3. **La sección «Ningún pendiente vive suelto»** aclara que «Por asignar» vale mientras el pendiente no esté aprobado.

## El límite

No cambia cuándo un pendiente se construye: sigue sin construirse sin su HU y su fase (`F23`). Solo cambia cuándo se puede **anotar**.

## Cómo se sabrá que cerró

- `python validadores/andamio.py pendiente prueba` sin `--hu` simula la creación sin error.
- `F23` o la regla nueva nombran el orden hallazgo → pendiente → HU → fase, con su checklist en **CUMPLE**.
- `python validadores/validar.py metareglas` sigue en verde.
