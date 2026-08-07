# El defecto que el agente detecta, lo corrige

Cuando el agente encuentra algo mal —un enlace roto, una cita a una regla derogada, un dato desactualizado— y ya lo reportó como defecto, lo **arregla**. No pregunta "¿lo corrijo?".

**Por qué:** el usuario lo cortó así — *"si está mal para qué me pide permiso para corregir?"*. Preguntar por algo que el propio agente acaba de declarar incorrecto no le da control: le devuelve una decisión que ya está tomada por los hechos. Si está mal, está mal.

**Cómo se aplica:** decir qué estaba mal y que se corrigió, en la misma respuesta. La pregunta se reserva para lo que de verdad es una decisión —qué versión se deja, si se deroga o se parte una regla, qué entra en el commit—, no para ejecutar una corrección evidente.

**Lo que sigue necesitando permiso:** el `commit` y el `push` ([aprobar antes de commit](aprobar-antes-de-commit.md)), y editar cuando el usuario solo preguntó algo ([una pregunta no es una instrucción](pregunta-no-es-instruccion.md)). Corregir un defecto que el agente detectó no es ninguna de las dos.

Relacionado: [una pregunta no es una instrucción](pregunta-no-es-instruccion.md) · [aprobar antes de commit](aprobar-antes-de-commit.md) · [respuestas cortas](respuestas-cortas.md).
