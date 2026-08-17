# Hecho · Un solo veredicto por fase

Origen: pendiente 28, abierto el 2026-08-15 y cerrado el 2026-08-16, versión **23.1.0**.

| | |
|---|---|
| **De dónde salía** | El hallazgo H-7 del [2026-08-15 · la plantilla del resultado de pruebas](../../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md) |
| **Dónde se construyó** | Fase [`A-EP-004-HU-014-comparar-los-dos-veredictos`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/A-EP-004-HU-014-comparar-los-dos-veredictos/) |
| **Lo destapó** | El [pendiente 27](el-veredicto-de-la-fase-a-de-hu-010.md), que era el caso |

## Qué pasaba

El veredicto de una fase se escribe **dos veces a mano**: en el §6 del `resultado_pruebas.md` y en el `estado-fase.md`. Nada comprobaba que dijeran lo mismo.

Y ya no lo decían. En la fase `A-EP-003-HU-010`, el resultado decía **No cumple** y el estado-fase seguía diciendo «aprobada con una prueba pendiente».

**Por qué importaba:** el `estado-fase` es lo que se mira para pasar la puerta de verificación. Si dice que cumple, la fase pasa sin que nadie abra el resultado — que es donde está la verdad.

## La decisión que faltaba

El pendiente dejaba dos salidas y ninguna elegida. Se tomó la primera, y queda escrito el porqué:

| Salida | Qué pasó con ella |
|---|---|
| **Un programa compara los dos y avisa si difieren** | **Elegida.** No cambia ningún documento ni ningún molde, no obliga a migrar las fases ya escritas y cabe entera en EP-004 |
| El `estado-fase` no escribe el veredicto: lo enlaza | Descartada por ahora. Quita la copia de raíz, pero cambia el molde del `estado-fase`, obliga a reescribir todas las fases cerradas y cambia lo que lee la puerta de verificación |

**Si algún día se hace la segunda, esta comprobación sobra y se retira.** Queda dicho para que nadie tenga que deducirlo.

## Cómo cerró

`veredicto()` en [`validadores/fases.py`](../../validadores/fases.py) compara tres cosas, y no solo el concepto — el propio pendiente advertía que comparar medio archivo deja medio verificado:

1. **El concepto.** Si difieren, falla, y el hallazgo dice los dos valores y recuerda cuál mira la puerta.
2. **Las exigencias en «No».** Si el §5 del resultado tiene un criterio o un requisito en «No» y el `estado-fase` da la fase por cumplida, se nombra esa exigencia.
3. **El conteo de criterios.** Si los dos cuentan distinto, se dicen los dos números.

**Dos límites, a propósito:** si falta uno de los dos documentos calla —una fase a medio escribir no es una contradicción—, y una salvedad al lado del concepto («Cumple, con una salvedad») tampoco lo es.

## Lo que hay que saber para leer su resultado

**No encontró ninguna contradicción en este repositorio, y eso no es una buena noticia por sí sola:** el único caso conocido se corrigió unas horas antes, al cerrar el 27. La comprobación llegó tarde a su propio caso.

Su valor no es lo que encuentra hoy: es que la próxima no dependa de que alguien reescriba un resultado de pruebas y note la diferencia — que fue exactamente como se encontró esta.

## Cómo se supo que cerró

Una fase de mentira con los dos veredictos distintos se reporta; con los dos iguales, no. Está automatizado en [`validadores/tests/test_fases_veredicto.py`](../../validadores/tests/test_fases_veredicto.py), con un caso dedicado a lo que **no** hay que reportar.
