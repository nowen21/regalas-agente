# Pendiente · El validador de la F22 se escribió sin su fase

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-3 del [resumen del 2026-08-16](../historico-chat/resumenes/2026-08-16/sesion.md) |
| **Historia que lo recoge** | [EP-004 · HU-015](../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

El 2026-08-16 se escribió [`02·F22`](../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) y, en la misma sesión, el programa que la comprueba: `derogaciones`, `sin_adoptar` y `validar_fase` en [`validadores/version.py`](../validadores/version.py), llamados desde [`validadores/flujo.py`](../validadores/flujo.py).

Eso es desarrollo, y [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) pide recorrer `planteamiento → épica → HU → especificación → plan → código`, sin atajos por tamaño. No hubo HU ni fase: el código existe y su cadena no.

**Lo que lo hace grave:** es el mismo repositorio que escribe la regla, incumpliéndola mientras la escribe. Y sin fase no hay plan aprobado ni cierre, así que el código quedó sin el registro que dice por qué es como es.

## Qué falta

Retrodocumentar el trabajo como fase de EP-004, con la plantilla que ya existe para eso ([`plantillas/retrodocumentacion.md`](../plantillas/retrodocumentacion.md)):

1. La fase de la [HU-015](../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md), con su plan de trabajo.
2. Su resultado de pruebas: las tres comprobaciones ya se corrieron a mano contra proyectos de mentira, y ese resultado hay que escribirlo.
3. Su cierre y su estado de fase.

## Qué revisar además

Esta no es la primera vez. Vale la pena mirar cuánto trabajo del propio estándar se hizo sin cadena, porque la regla que lo prohíbe se aplica también acá: el [`CLAUDE.md`](../CLAUDE.md) del repositorio manda obedecer `base/` antes de tocar nada.

## Cómo se sabe que cerró

La fase existe con su plan, su resultado de pruebas y su cierre, y la HU-015 la nombra en su sección 8.
