# A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Mitad retro-documentación, mitad construcción.** Los puntos existen: la tabla de estaciones del [director](../../../../../skills/sdd-orchestrator/SKILL.md) dice cuáles aprueba el usuario, `01·C17` dice que solo su palabra afirmativa cuenta y `00·N2` que la autorización es de un solo uso.

**Lo que la fase destapa.** La lista **no vive en `base/`**: vive dentro de un procedimiento. Un proyecto que hereda recibe las reglas sueltas y no la lista, así que no puede leer de un lado qué falta aprobar. Llevarla a `base/` sube versión, y es la duda 1.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md` — la fila de HU-008 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Dos dudas bloquean el CA-01.
