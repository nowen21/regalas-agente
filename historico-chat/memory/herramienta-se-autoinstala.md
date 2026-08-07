# Toda herramienta se autoinstala

Una herramienta del estándar —enganche, validador, carpeta que el proyecto necesite— no está terminada hasta que **se instala sola** en cualquier proyecto que use el agente. El camino es `validadores/instalar.py`, que corre el paso 6 de `plantillas/CLAUDE.md.plantilla` en cada sesión y es idempotente.

Entregar el mecanismo y decir "ahora hay que agregarlo a mano en cada proyecto" es entregarlo a medias.

**Por qué:** las reglas y los validadores viajan solos desde la carpeta central, pero lo que vive **dentro** del proyecto (enganches en `.claude/settings.json`, carpetas como `historico-chat/`) no llega si nadie lo instala. Si exige configuración manual, es defecto del estándar, no tarea del proyecto.

**Cómo se aplica:** al crear una herramienta, cerrar el círculo en el mismo trabajo — agregarla a `HOOKS_CLAUDE` (o a la instalación que corresponda) en `instalar.py`, crear en el proyecto lo que necesite para funcionar, y dejarlo escrito en `CLAUDE.md.plantilla` para que el agente de ese proyecto sepa qué queda instalado. Tocar `plantillas/` obliga a versionar: `CHANGELOG.md` + `VERSION`.

Relacionado: [todo multiproyecto](todo-multiproyecto.md) · [las reglas son la decisión del usuario](reglas-son-decision-del-usuario.md).
