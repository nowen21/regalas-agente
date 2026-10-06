# Pendiente: el enganche del análisis espera al histórico con un reloj

| | |
|---|---|
| **De dónde sale** | [H-2 · El enganche del análisis espera al histórico con un reloj](../../sesion-2.md), en el resumen de la sesión del 2026-10-05, que salió de «Dónde más puede pasar» del [análisis 1 del pendiente 124](../124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |

## El problema

`AnalisisEnCurso.esperar`, en [analisis_en_curso.py](../../../../../proyectos/cimiento/core/enganches/analisis_en_curso.py), revisa cada 0,25 segundos, hasta 5 segundos, si el histórico ya anotó el turno, porque los dos enganches corren con el mismo evento y no se avisan entre sí.

## Por qué importa

Es una espera por reloj donde lo acordado para Cimiento es actuar por evento (acuerdo 4 del análisis 1 del pendiente 124). Si el histórico tarda más de 5 segundos, el análisis sigue sin el turno; si tarda menos, cada mensaje igual pierde tiempo preguntando.
