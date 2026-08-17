# A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Retro-documenta.** Los dos programas existen y corren: [`secretos.py`](../../../../../validadores/secretos.py) busca claves incrustadas y [`versionado.py`](../../../../../validadores/versionado.py) revisa qué está versionado.

**Lo que la fase pone en primer plano** es el CA-03: que un ejemplo no se confunda con una clave. Un detector con falsos positivos se apaga, y entonces no detecta nada.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
