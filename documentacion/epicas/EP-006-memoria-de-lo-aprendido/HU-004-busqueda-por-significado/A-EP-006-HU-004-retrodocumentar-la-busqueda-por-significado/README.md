# A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Retro-documenta.** [`memoria/semantica.py`](../../../../../memoria/semantica.py) busca por significado, calcula los vectores **en la máquina** y se degrada solo si sus dependencias no están.

**Las dos mitades que la fase prueba** son las que sostienen el diseño: que sin el modelo la memoria siga sirviendo, y que el contenido de las señales no salga de la máquina — que es una regla blindada y hoy solo está escrita en un comentario.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md` — la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
