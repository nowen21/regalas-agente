# Pendiente: el Resumen del gasto tarda cerca de 1,5 s y se vuelve a pedir con cada mensaje

| | |
|---|---|
| **De dónde sale** | H-33 de la [sesión del 2026-10-06](../../../2026-10-06/sesion.md) |

## El problema

En la pantalla del gasto, la pestaña Resumen (`/gasto/pestana/resumen/`) tardó entre 1,5 y 1,8 s el 2026-10-08, medida con Chrome sin ventana. Las otras cuatro pestañas tardan entre 0,2 y 0,6 s. El Resumen arma las dos gráficas, los candidatos a automatizar y dónde se gasta más (`GastoDelPeriodo.pestana("resumen")`, en `proyectos/cimiento/core/consumo/tablero.py`).

Cada vez que el vigilante guarda algo, Cimiento avisa a la pantalla y la pestaña abierta se vuelve a pedir. Mientras el agente trabaja eso pasa con cada mensaje y con cada llamada: el Resumen se recalcula una y otra vez. Desde la fase `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto`, ese refresco ya no tapa la pestaña que se escoge, pero el costo sigue.

## Por qué importa

La pantalla responde lento justo cuando más se usa, mientras se trabaja, y la base hace el mismo cálculo pesado muchas veces por minuto.
