# A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Retro-documenta.** [`memoria/memoria.py`](../../../../../memoria/memoria.py) busca con el índice de texto completo que la base ya trae, sin instalar nada, y a propósito ignora los acentos.

**Lo que la fase agrega es la prueba dura:** que el índice esté sincronizado. Un índice desincronizado responde igual — responde mal, y eso es peor que no responder.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
