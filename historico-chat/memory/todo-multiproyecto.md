# Todo multiproyecto

Todo lo que se construya en el estándar —validadores, reglas, plantillas, enganches— debe ser **multiproyecto y agnóstico del stack**. Nunca diseñar algo "solo para un framework".

**Por qué:** el estándar es una capa central que **cualquier** proyecto hereda. Algo atado a un stack rompe el propósito. Probar contra un proyecto real es válido, pero el diseño no puede depender de él.

**Cómo se aplica:** algo queda universal por una de dos vías, y hay que decidir cuál antes de construirlo:

1. **Universal de raíz** — el chequeo es idéntico en todo repo (rama git, patrones de secreto, presencia de lockfile).
2. **Universal por detección de stack** — el chequeo existe en todos pero cambia de forma (migraciones, linter, pruebas, N+1): se detecta el ecosistema o se lee el stack declarado en `.agente/`, y se aplica la convención que corresponda.

Si no encaja en ninguna de las dos, no es apto para el estándar: es capa 3.

Relacionado: [fixtures sin secretos literales](fixtures-sin-secretos-literales.md) · [toda herramienta se autoinstala](herramienta-se-autoinstala.md).
