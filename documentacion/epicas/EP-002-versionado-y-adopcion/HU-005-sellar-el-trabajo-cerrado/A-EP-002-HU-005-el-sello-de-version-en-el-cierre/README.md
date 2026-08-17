# A-EP-002-HU-005-el-sello-de-version-en-el-cierre

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Mitad retro-documentación, mitad construcción.** La regla existe: la retroactividad está escrita en la cabecera del [`CHANGELOG`](../../../../../CHANGELOG.md) y el aviso de desfase la repite. Lo que **no existe** es el campo: ningún modelo de cierre pide bajo qué versión cerró la fase, así que el sello se escribe cuando alguien se acuerda.

**Toca `plantillas/`,** y eso sube versión — MAYOR si el validador lo exige, MENOR si solo avisa. Es la duda 2 del plan, y la decide el usuario.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Dos dudas bloquean el CA-01.
