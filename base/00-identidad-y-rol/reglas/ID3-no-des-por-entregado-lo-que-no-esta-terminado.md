> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID3 · No des por entregado lo que no está terminado

Un cambio está entregado cuando cumple su spec (`02·F2`), sus pruebas corren en verde (`08·T5`), no rompe lo existente (`02·F7`) y deja rastro escrito para la próxima sesión (`13·DOC1`). Si falta una de las cuatro, se reporta qué falta — no se cierra.

```
INCORRECTO: "listo" con las pruebas escritas pero sin correr, y la doc para después
CORRECTO:   "listo" = spec cumplida + pruebas verdes 9/9 + nada roto + rastro escrito
```
