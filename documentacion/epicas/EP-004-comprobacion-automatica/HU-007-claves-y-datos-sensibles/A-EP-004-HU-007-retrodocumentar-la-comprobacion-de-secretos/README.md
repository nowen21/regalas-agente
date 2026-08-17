# A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Retro-documenta.** Los dos programas existen y corren: [`secretos.py`](../../../../../validadores/secretos.py) busca claves incrustadas y [`versionado.py`](../../../../../validadores/versionado.py) revisa qué está versionado.

**Lo que la fase pone en primer plano** es el CA-03: que un ejemplo no se confunda con una clave. Un detector con falsos positivos se apaga, y entonces no detecta nada.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md` — la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Sin dudas pendientes.
