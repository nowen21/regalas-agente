# A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Retro-documenta.** La clasificación existe y está completa: las 33 reglas sin clasificar bajaron a cero el 2026-08-16.

**Lo que la fase destapa.** Lo que vigila esa completitud es [`metareglas.py`](../../../../../validadores/metareglas.py), que **no se puede correr**. La fase lleva la comprobación a la suite, que sí corre, y agrega el caso que costó una sesión: el registro decía «C1–C17» y el programa no lee rangos.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md` — la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
