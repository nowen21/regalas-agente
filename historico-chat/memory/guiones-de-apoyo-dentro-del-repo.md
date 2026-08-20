# Los guiones de apoyo van dentro del repositorio

Cuando el agente necesita un guion intermedio para generar o editar archivos, ese guion se escribe **dentro del repositorio** (en una carpeta temporal ignorada por git) o no se escribe: nunca en la carpeta temporal que la herramienta ofrece fuera del proyecto.

**Por qué:** el 2026-08-20 el agente dejó seis guiones en `AppData\Local\Temp\claude\...\scratchpad` y el usuario preguntó por qué consultaba esa ruta si todo lo del proyecto va en el proyecto. La regla [`04·S9`](../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) ya lo dice: el agente escribe solo dentro de la carpeta del proyecto. La autorización genérica de la herramienta no reemplaza la regla del estándar.

**Cómo se aplica:** si un comando largo no cabe en la consola, el guion va a una carpeta temporal del repositorio y se borra al terminar. Leer lo que la herramienta guarda por fuera (su transcripción, lo que inyectó cada enganche) sí vale, porque es leer; lo que no se hace es escribir allá.

Relacionado: [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) · [histórico de sesiones](historico-chat.md).
