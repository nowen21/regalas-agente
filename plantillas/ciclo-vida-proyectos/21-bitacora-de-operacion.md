# Bitácora de operación   `[CAPA 3]`

**Para qué sirve este documento.** Es el registro de lo que le pasa al sistema en producción, en orden: despliegues, respaldos, incidentes, mantenimientos. Cuando algo falle, la primera pregunta será «¿qué cambió antes?», y la respuesta debe estar acá y no en la memoria de alguien.

> Plantilla. Se escribe **en el momento** en que el evento ocurre, el más reciente arriba; nunca se reescribe lo anotado (si algo se corrigió después, se anota la corrección como evento nuevo). Mientras no haya producción, existe con su primera línea: «No aplica todavía porque «el porqué»». Reemplaza los `«…»` y borra esta caja.

## El registro

> Tipos de evento: **despliegue**, **respaldo**, **restauración**, **incidente**, **mantenimiento**, **cambio de configuración**. Un incidente con causa y corrección de fondo amerita además su [postmortem](../postmortem.md), y acá queda el enlace.

| Fecha y hora | Tipo | Qué pasó | Qué se hizo | Quién |
|---|---|---|---|---|
| «AAAA-MM-DD HH:MM» | «…» | «…» | «…» | «…» |

## Lo que la bitácora alimenta

- Un **incidente** repetido dos veces gana su fila en el [manual de operación](18-manual-tecnico-y-de-operacion.md) («cuando algo falla»), para que la tercera vez tenga remedio escrito.
- Un **despliegue** apunta a su versión en las [notas de versión](19-notas-de-version.md).
- Una **restauración** actualiza la fecha de última prueba en el manual de operación.
