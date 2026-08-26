# A-EP-001-HU-008-retrodocumentar-la-derogacion

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Por qué esta fase casi no construye.** La derogación existe y ya se usó ocho veces —`F4.1` a `F4.5`, `F6`, `F7` e `ID2`—: [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) la exige, la marca está en la lista cerrada y `validar.py version` las lee para decir qué falta adoptar. Lo que no existe es prueba de que sigan ahí: si mañana alguien borra una, nada avisa. Lo único que la fase agrega son dos pruebas a la suite.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. La fila de HU-008 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes: las ocho derogaciones están verificadas.
