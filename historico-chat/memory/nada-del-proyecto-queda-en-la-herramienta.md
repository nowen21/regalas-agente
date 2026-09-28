# Nada del agente ni del proyecto queda por fuera de ellos

Todo lo que pertenece al agente o al proyecto vive **dentro** del agente o del proyecto, no en el almacén de Claude Code. Si alguien necesita ese contenido, lo encuentra por un **enlace** que lleva al sitio del repositorio donde está. Vale para todo: reglas, memoria, guiones, lo que entregan los enganches y cualquier cosa que venga después.

**Por qué:** el 2026-09-28 se vio que el enganche de arranque le pasaba al agente 79,7 KB de reglas. Claude Code lo guardó en `~/.claude/projects/<proyecto>/<id-de-sesión>/tool-results/` y al agente le mostró solo 2 KB. Las reglas del proyecto terminaron en un archivo de la herramienta que nadie versiona ni revisa, y el agente trabajó sin ellas. El usuario lo dijo así: *«nada debe quedar por fuera del agente o del proyecto. Si se necesita alguna información, debe existir un enlace que lleve al lugar donde está el contenido […] Eso debe aplicar para todo»*.

**Cómo se aplica:**

- Lo que un enganche le entrega al agente es corto y trae enlaces a los archivos del repositorio. No copia el contenido: las reglas ya están en `base/`, y el enganche dice dónde.
- Si la herramienta guarda algo por su cuenta fuera del repositorio, eso es una falla que hay que arreglar en su origen. Leer esa copia no la arregla.
- Extiende lo que ya exigen [`01·C19`](../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) para la memoria y [`04·S9`](../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) para lo que escribe el agente. Esas dos cubren lo que hace el agente. Esta cubre también lo que hace la herramienta.

Relacionado: [los guiones de apoyo van dentro del repositorio](guiones-de-apoyo-dentro-del-repo.md) · [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md).
