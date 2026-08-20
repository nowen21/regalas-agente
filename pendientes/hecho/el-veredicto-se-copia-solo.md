# Pendiente · Las filas de estado y los enlaces de vuelta los escribe el agente a mano en cada cierre

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-003 — Disparar las comprobaciones al escribir un archivo](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md) — es el mismo momento: al escribir el resultado o el cierre de una fase, el programa puede completar lo que de ellos se deriva |
| **De dónde sale** | La pregunta del usuario del 2026-08-20: cómo hacer que Cimiento haga más y gaste menos. Quedó en el [resumen](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

Al cerrar una fase, el veredicto se copia a mano en cuatro sitios: el `estado-fase.md` §1.1, la fila del §8 de la historia, el `README.md` de la fase y el de la historia. Lo mismo con el estado de la historia («Ready» → «Hecha») y con la fila del backlog cuando el pendiente cierra. Hoy `fases.py` comprueba **después** que esas copias no se contradigan (HU-014 de EP-004); no las escribe.

El 2026-08-20, cerrar tres fases fueron doce de esas copias, y el programa que ya sabe el veredicto (lo lee del `resultado_pruebas.md` §6) las miró sin escribirlas.

## Por qué importa

Cada copia a mano es una contradicción esperando, y es lo que el validador de veredictos nació para atrapar. Un programa que la escribe no se contradice. Y es trabajo del agente que no es criterio: el veredicto ya está decidido en el resultado.

## Qué falta

Un enganche que, al escribir el `resultado_pruebas.md` de una fase, lea su §6 y ponga al día la fila del §8 de la historia y los `README.md` de la fase y la historia; y `cerrar.py`, que ya arrastra las citas, que deje además la fila del backlog en la forma «hecho». El `estado-fase.md` no: ese es el checkpoint y lo escribe el agente (pendiente 64, ya cerrado).

## El límite

No decide el veredicto ni lo interpreta: copia lo que el resultado dice, donde el estándar manda que se repita.

## Cómo se sabrá que cerró

Escribir un `resultado_pruebas.md` con veredicto «Cumple» deja la fila del §8 de la historia y los dos README diciendo lo mismo, sin que el agente los toque, y `validar.py fases` no reporta veredictos que no coinciden.
