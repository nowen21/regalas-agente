# A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Construcción.** El disparo existe —[`hook_md.py`](../../../../../validadores/hook_md.py) corre con cada escritura— y lo que hace es comprobar enlaces. Al escribir un plan de trabajo, el capítulo que lo rige **no llega**: llega su índice al abrir la sesión, y hay que acordarse de abrirlo.

**El límite es el costo:** el arranque ya pesa unos 73 KB, medidos en la fase A de [HU-009](../../HU-009-lo-que-rige-cada-frase-llega-puesto/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/README.md). Repetir capítulos en cada escritura haría la sesión inutilizable.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md` — los dos salen de ejecutar, y la fase todavía no se aprobó. la fila de HU-010 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Dos dudas: qué capítulo rige cada documento, y si llega completo o solo la regla.
