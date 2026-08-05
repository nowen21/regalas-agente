# Pendiente · Vigencia y poda de la memoria

**Estado:** abierto · anotado 2026-08-04.

Definir **qué pasa con una señal cuando pasa el tiempo**. Hoy `memoria/senales.db` solo crece: `supersede` existe, pero depende de que alguien recuerde marcar la señal vieja. Una decisión que quedó obsoleta **sin que nadie la marcara** sigue apareciendo en `search` con el mismo peso que una de ayer.

## El riesgo real

El daño es **silencioso**. El agente le cree a la memoria: no tiene forma de saber que la señal S-014 describe una arquitectura que se cambió hace ocho meses. Sin política de caducidad, la pieza más valiosa del estándar se degrada sola de activo a ruido — y cuanto más se usa, más rápido.

## Qué cubriría

- **Marca de vigencia** — cada señal con fecha de última revisión, no solo de creación. Una señal no revisada en N meses se muestra atenuada o marcada como "sin verificar".
- **Revisión periódica** — ritual (o comando) que lista las señales más viejas de un scope y pide confirmar / reemplazar / cerrar. Barato si se hace seguido.
- **Ranking por recencia en `search`** — hoy FTS5 ordena por relevancia léxica pura. Empatar en palabras y desempatar por fecha evita que lo viejo tape lo nuevo.
- **Detección de contradicciones** — dos señales activas del mismo scope que se contradicen: hoy conviven y nadie avisa.
- **Poda con criterio** — qué se archiva y qué nunca se borra. Las señales de tipo `decision` y `restriccion` son historia (no se borran); `gotcha` y `error-resuelto` de un módulo que ya no existe, sí.

## Decisión pendiente

Archivar ≠ borrar. Definir si la señal caduca pasa a `estado='archivada'` (sigue en la tabla, fuera de `search`) o a una tabla aparte. Preferible lo primero: una sola tabla, una sola consulta.

## Relación con otros pendientes

- Depende del mismo esquema que el [03 · ciclo de vida de pendientes](03-ciclo-de-vida-de-pendientes.md) — conviene diseñar los dos cambios de `estado` juntos, en una sola migración. Por eso van seguidos.
- La [05 · memoria semántica](05-memoria-semantica.md) **agrava** este problema: la búsqueda semántica encuentra más señales viejas que la léxica, no menos. Por eso este va antes.
