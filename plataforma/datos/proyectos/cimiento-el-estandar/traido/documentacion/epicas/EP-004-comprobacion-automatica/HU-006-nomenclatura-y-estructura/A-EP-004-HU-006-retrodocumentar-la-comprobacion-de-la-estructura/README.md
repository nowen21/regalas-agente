# A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Retro-documenta.** El programa existe y corre a diario: [`fases.py`](../../../../../validadores/fases.py) comprueba nueve partes de `02·F12`. Falta la prueba atada a estos tres criterios y la declaración de qué parte de la regla **no** comprueba nadie, porque pide criterio.

**Y deja la línea base:** hoy la corrida da 0 fallas y 54 avisos. Sin ese número escrito, mañana no se puede decir si bajaron.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
