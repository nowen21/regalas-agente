# A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Retro-documenta.** [`hook_md.py`](../../../../../validadores/hook_md.py) corre con cada escritura y, si el archivo es un documento, comprueba los enlaces. Esta sesión lo vio actuar: al escribir un plan con un enlace roto, el aviso llegó de inmediato.

**Lo que la fase tiene que responder** es el CA-03: hoy el enganche devuelve el detalle y no distingue entre detener y avisar, como sí hace la línea de comandos.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
