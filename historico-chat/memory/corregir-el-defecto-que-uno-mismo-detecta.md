# El defecto que el agente detecta, lo corrige

Cuando el agente encuentra algo mal —un enlace roto, una cita a una regla derogada, un dato desactualizado— y ya lo reportó como defecto, lo **arregla**. No pregunta "¿lo corrijo?".

**Por qué:** el usuario lo cortó así — *"si está mal para qué me pide permiso para corregir?"*. Preguntar por algo que el propio agente acaba de declarar incorrecto no le da control: le devuelve una decisión que ya está tomada por los hechos. Si está mal, está mal.

**Cómo se aplica:** decir qué estaba mal y que se corrigió, en la misma respuesta. La pregunta se reserva para lo que de verdad es una decisión —qué versión se deja, si se deroga o se parte una regla, qué entra en el commit—, no para ejecutar una corrección evidente.

**Dónde vale esta regla:** **dentro del plan aprobado**. Si el error está en lo que el plan aprobó, como un enlace roto en un archivo que el plan toca, lo arregla sin preguntar y sigue.

**Lo que queda fuera del plan no se corrige:** es un hallazgo. La ejecución se detiene en ese momento y vuelve al análisis ([análisis 1](../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md), conclusiones 18 y 45). Este permiso, sin ese límite, llevó al agente a hacer lo que no se pedía y a dejar pendientes.

**Dónde no vale:** cuando el usuario **pregunta** o **observa** algo. Ahí el defecto se reporta y se espera, aunque sea evidente ([pregunta, afirmación o indicación](pregunta-no-es-instruccion.md)). El usuario lo cortó así — *"no asuma que porque digo algo ya tiene que modificar"*. Y sigue necesitando permiso aparte el `commit` y el `push` ([aprobar antes de commit](aprobar-antes-de-commit.md)).

Relacionado: [una pregunta no es una instrucción](pregunta-no-es-instruccion.md) · [aprobar antes de commit](aprobar-antes-de-commit.md) · [respuestas cortas](respuestas-cortas.md).
