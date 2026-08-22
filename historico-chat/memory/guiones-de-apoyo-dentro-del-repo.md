# Los guiones de apoyo van dentro del repositorio, y se quedan

Cuando el agente necesita un guion intermedio para generar o editar archivos, ese guion se escribe **dentro del repositorio**, en `historico-chat/scripts/AAAA-MM-DD/`, y **se queda ahí versionado**. Nunca en la carpeta temporal que la herramienta ofrece fuera del proyecto.

**Por qué:** el 2026-08-20 el agente dejó seis guiones en `AppData\Local\Temp\claude\...\scratchpad` y el usuario preguntó por qué consultaba esa ruta si todo lo del proyecto va en el proyecto. La regla [`04·S9`](../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) ya lo dice: el agente escribe solo dentro de la carpeta del proyecto. La autorización genérica de la herramienta no reemplaza la regla del estándar.

**Y el 2026-08-22 el usuario lo precisó, porque el recuerdo se estaba cumpliendo a medias:** *«nada se debe escribir por fuera, todo debe quedar en historico-chat»*. No alcanza con que el guion viva en una carpeta temporal del repositorio y se borre: **el resultado quedaba versionado y el cómo se perdía**. A la pregunta «¿con qué se recortaron esas treinta reglas?» no había respuesta en ninguna parte.

**Cómo se aplica:**

- El guion se escribe en `historico-chat/scripts/AAAA-MM-DD/`, con un nombre que diga qué hace.
- La carpeta del día lleva su `README.md` diciendo qué hizo cada uno. El de la carpeta madre explica qué son y qué no.
- **No se borran, y no se vuelven a correr**: se guardan para leerlos. Casi todos escriben sobre texto que ya cambió.
- Si un guion sirve dos veces, deja de ser de un solo uso y baja a `validadores/` por la cadena, con su contrato y sus pruebas.
- Leer lo que la herramienta guarda por fuera (su transcripción, lo que inyectó cada enganche) sí vale, porque es leer. Lo que no se hace es **escribir** allá.

Relacionado: [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) · [histórico de sesiones](historico-chat.md).
