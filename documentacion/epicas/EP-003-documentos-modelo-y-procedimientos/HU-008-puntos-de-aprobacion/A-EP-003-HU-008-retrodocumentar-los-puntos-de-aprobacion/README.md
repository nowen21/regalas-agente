# A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Mitad retro-documentación, mitad construcción.** Los puntos existen: la tabla de estaciones del [director](../../../../../skills/sdd-orchestrator/SKILL.md) dice cuáles aprueba el usuario, `01·C17` dice que solo su palabra afirmativa cuenta y `00·N2` que la autorización es de un solo uso.

**Lo que la fase destapa.** La lista **no vive en `base/`**: vive dentro de un procedimiento. Un proyecto que hereda recibe las reglas sueltas y no la lista, así que no puede leer de un lado qué falta aprobar. Llevarla a `base/` sube versión, y es la duda 1.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-008 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Dos dudas bloquean el CA-01.
