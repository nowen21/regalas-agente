# B-EP-006-HU-003-la-busqueda-dice-donde-esta

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Corrige un defecto.** La fase [`A`](../A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/resultado_pruebas.md) ejecutó su plan completo y cerró en **No cumple**: la búsqueda encuentra y **no dice dónde está lo que encontró**. El CA-01 se da por aprobado «cuando el resultado alcanza para abrir lo que se encontró», y no alcanza.

**Son dos arreglos de una línea cada uno**, los dos en `cmd_search`: agregar `where_` a lo que imprime, y cerrar la conexión en el camino sin resultados. Los dos tienen **su prueba ya escrita**, en rojo esperado desde la fase A — esta fase las destapa.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md`, que salen de ejecutar.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
