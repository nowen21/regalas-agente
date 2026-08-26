# B-EP-006-HU-007-marcar-deja-fecha-y-referencia

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Corrige un defecto.** Reemplazar una señal imprime «S-001 marcada reemplazada por S-002» y **no guarda ni el `--by` ni la fecha**. Archivar tampoco deja fecha. De una señal marcada no se sabe **cuándo** ni **por cuál**.

**El dato existe, se muestra y se pierde al cerrar la consola** — que es literalmente lo que [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) manda evitar, incumplido por el programa que implementa esa misma regla.

**Sin migración:** las tres columnas que hacen falta ya existen. Y las señales marcadas antes del cambio **se quedan sin fecha**: rellenarlas con hoy sería inventar cuándo se marcaron.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md`, que salen de ejecutar.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
