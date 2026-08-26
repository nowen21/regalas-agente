# C-EP-001-HU-009-las-tres-reglas-con-nombre-propio

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada exigencia |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: el [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que **sigue abierto**. Es el segundo punto de su lista de por dónde seguir: las reglas que nombran un stack, un dominio o una herramienta, y que hacen que **cualquier proyecto que herede el estándar lea reglas escritas para el stack de otro**.

**Eran tres según el pendiente. Eran cuatro:** la cuarta —[`04·S10`](../../../../../base/04-seguridad.md#s10--no-mates-procesos-globales--solo-pid-exacto-y-estrictamente-necesario)— la encontró el programa, no una lectura, y el motivo está en su propio sello viejo: había argumentado esa fila para defender otros tres nombres, y con eso la dio por revisada.

**Lo que más pesa de esta fase no es lo que se quitó, sino lo que se conserva:** `killall`, `pkill` y `taskkill` se quedan, con caso de prueba propio, para que la próxima pasada no los borre creyendo que mejora.

**Estado:** estación 8 de las once, en la [v23.7.3](../../../../../CHANGELOG.md). Veredicto **Cumple**, 9 de 9 casos.
