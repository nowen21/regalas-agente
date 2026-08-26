# A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Retro-documenta.** El criterio existe y se aplicó a las 188 reglas: está en [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) —«si un script puede decir sí o no sin opinar, es validable; si dos personas pueden discutir, se queda en el documento»— y `20·M9` obliga a declararlo.

**Lo que la fase destapa.** El criterio **vive en `validadores/`, no en `base/`**. Un proyecto que hereda recibe la obligación de clasificar y no el criterio con que se decide.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-001 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Una duda: si el criterio entra al cuerpo de `M9` o si `M9` lo enlaza.
