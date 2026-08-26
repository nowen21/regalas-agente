# B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada criterio de aceptación |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |

**Corrige un defecto.** Un `.md` que no se puede decodificar **tumba la corrida entera** con una traza de Python, y se lleva por delante todos los hallazgos ya encontrados. Es el peor momento posible para caerse: cuando ya hay trabajo hecho que reportar.

**La causa está en tres líneas** que usan casi todos los validadores: la lectura común abre sin red. Hoy todos se caen igual.

**Hay un préstamo que cerrar:** el validador de pendientes, nacido el mismo día, tiene su propia lectura porque la común no le servía. Que vuelva a usarla es la prueba de que el arreglo sirve de verdad.

**Lo que falta de la fase:** `resultado_pruebas.md` y `funcionalidad_implementada.md`, que salen de ejecutar.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
