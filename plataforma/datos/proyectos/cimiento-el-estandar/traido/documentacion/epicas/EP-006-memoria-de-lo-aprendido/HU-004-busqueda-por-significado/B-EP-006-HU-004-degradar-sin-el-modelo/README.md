# B-EP-006-HU-004-degradar-sin-el-modelo

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Corrige el defecto más grave que dejó la sesión del 2026-08-17.** Con las librerías instaladas y **el modelo ausente**, la búsqueda se cae entera — también la parte por palabra, que no necesita ni modelo ni red. Le pasa a cualquier máquina nueva, a una con la caché borrada, o a un despliegue sin red la primera vez.

**La causa:** `disponible()` comprueba que `numpy` y `model2vec` **importen**, no que el modelo cargue. Y no se ve nunca donde se desarrolla, porque ahí el modelo ya está descargado.

**De paso cierra el transversal de privacidad**, que la fase A dejó en «No»: cargar el modelo abre una conexión al repositorio remoto. El contenido de las señales no viaja, y conectarse es conectarse.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md`, que salen de ejecutar.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
