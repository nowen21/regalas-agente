# D-EP-001-HU-009-enlazar-en-vez-de-repetir

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada exigencia |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: el [pendiente 19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que **sigue abierto** — su categoría *«dejar de repetir al vecino»*.

**Por qué el defecto duraba:** las dos reglas **enlazaban** a la vecina. El enlace estaba puesto, visible y correcto — y aun así reprobaban, porque la fila 11 no pide enlazar sino **enlazar en vez de copiar**. Un enlace delante de un texto repetido se lee como diligencia.

**Y la forma correcta ya estaba escrita en el propio cuerpo:** [`14·EST3`](../../../../../base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `01·C3` el mismo criterio que `07·Q7` y estaba en CUMPLE. Faltaba leerlas juntas.

**Se cierran dos de cinco.** Las otras tres —`12·PR3`, `01·C16` y `04·S7`— no son un cambio de redacción: dos piden decidir si una regla deja de existir.

**Estado:** estación 8 de las once, en la [v23.7.4](../../../../../CHANGELOG.md). Veredicto **Cumple**, 7 de 7 casos.
