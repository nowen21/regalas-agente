# A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Construcción, y es la mitad que le falta a una regla blindada.** `00·N6` prohíbe que una clave quede escrita, y **ningún programa enmascara**: [`secretos.py`](../../../../../validadores/secretos.py) detecta las que ya están en el código, y la transcripción copia tal cual lo que el usuario pega.

**Por esto el CA-02 de [EP-001 · HU-003](../../../EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md) quedó cumplido a medias.**

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Una duda bloquea la marca con que se tapa.
