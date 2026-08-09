# `reglas-validables.md`

La revisión, regla por regla, de cuáles se pueden comprobar con un programa y cuáles no.

## Qué es

Es un documento, no código: nadie lo llama y no se ejecuta.

Recorre las reglas de `base/` una por una y las reparte en tres grupos, con un solo criterio:

> Si un programa puede responder **sí o no sin opinar** → se puede comprobar sola.
> Si dos personas pueden discutir si se cumplió → se queda escrita, y la interpreta el agente.

Lleva la fecha 2026-08-05 y es una foto de ese momento: cada vez que se agrega o se cambia una regla, hay que volver a mirarlo.

## Qué contiene

| Parte | De qué trata |
|---|---|
| Criterio | Cómo se decide, y el aviso de que muchas reglas necesitan un proyecto con código de verdad para poder comprobarse. |
| Conteo | El resumen: alrededor de 50 reglas ya convertidas en validador, unas 9 que se podrían y todavía no están, y unas 93 que necesitan que las juzgue una persona. |
| Actualizaciones | Notas que anotan los cambios posteriores a esa fecha: qué reglas se sumaron y a cuáles les cambió el título sin cambiarles el código. |
| Ya son validadores | La tabla que dice qué archivo comprueba cada regla y qué mira exactamente. |
| Se podrían y faltan | Las que se podrían comprobar solas pero todavía no, con el motivo. |
| No se pueden | Las que necesitan que las juzgue una persona. |

## Con qué se relaciona

Es el documento que explica por qué existe cada archivo de `validadores/`. Su tabla de «ya son validadores» es el revés de la tabla del `README.md`: aquella va de la regla al archivo, esta va del archivo a la regla.

Cuando se crea un validador nuevo, esa regla pasa del grupo «se podrían y faltan» al grupo «ya son validadores».

De acá salen las tareas del pendiente `01 · validadores de código de proyecto`.

## Cómo se lee

No se ejecuta. Se abre en `validadores/reglas-validables.md`.
