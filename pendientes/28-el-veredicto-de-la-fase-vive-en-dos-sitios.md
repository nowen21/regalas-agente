# Pendiente · El veredicto de la fase vive en dos sitios

**Estado:** abierto · anotado 2026-08-15 · nace del hallazgo H-7 del [2026-08-15 · la-plantilla-del-resultado-de-pruebas](../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md).

## El problema

El veredicto de una fase se escribe dos veces a mano: en la sección 6 del `resultado_pruebas.md` y en el `estado-fase.md`. Nada comprueba que digan lo mismo.

Y ya no lo dicen. En la fase A de EP-003 · HU-010, el [resultado](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md) dice **No cumple** y el [estado-fase](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/estado-fase.md) sigue diciendo «aprobada con una prueba pendiente».

**Por qué importa:** el `estado-fase` es lo que se mira para pasar la puerta de verificación. Si dice que cumple, la fase pasa sin que nadie abra el resultado — que es donde está la verdad.

## Qué falta

**La historia que dispara:**

> **EP-004 · [HU-014](../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) — un solo veredicto por fase**
> - **Como** quien revisa una fase
> - **Quiero** que el concepto del `resultado_pruebas` y el del `estado-fase` no puedan decir cosas distintas
> - **Para** no pasar una puerta de verificación con un veredicto viejo
> - **Contexto:** hoy el veredicto se escribe a mano en los dos archivos y nada comprueba que coincidan. Esta sesión dejó un caso donde ya no coinciden. Si no se hace, la puerta de verificación se apoya en el archivo que nadie actualizó.

Y antes de programarla, decidir cuál de las dos salidas:

| Salida | Qué implica |
|---|---|
| Un programa compara los dos y avisa si difieren | No cambia ningún documento; es la que cabe en EP-004 |
| El `estado-fase` no escribe el veredicto: lo enlaza | Quita la copia de raíz, pero cambia el molde del `estado-fase` y lo que la puerta de verificación lee |

## El límite

No es solo el veredicto: el `estado-fase` también repite el conteo de casos. Si se compara, se comparan los dos, o queda medio archivo verificado y medio no.

**Va después del [pendiente 27](27-la-fase-a-de-hu-010-cerro-sin-cumplir.md):** primero hay que saber cuál es el veredicto bueno de esa fase.
