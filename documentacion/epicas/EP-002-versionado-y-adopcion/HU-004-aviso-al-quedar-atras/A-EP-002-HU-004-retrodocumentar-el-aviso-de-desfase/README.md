# A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Retro-documenta.** El aviso sale solo al abrir la sesión: lo entrega [`hook_sesion.py`](../../../../../validadores/hook_sesion.py) y lo decide [`version.py`](../../../../../validadores/version.py). Falta la prueba de sus tres estados.

**Lo que la fase destapa.** El mensaje dice qué versión declara el proyecto y cuál es la vigente, y **no dice qué cambió entre las dos**, que es la tercera parte de la RN-02. Completarlo cambia lo que el usuario ve en cada apertura, así que se propone y no se hace de oficio.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md` — la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. La duda no bloquea las pruebas.
