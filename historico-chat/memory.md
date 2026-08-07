# Memoria del agente — cómo se trabaja en este repo

Lo que el agente debe recordar entre sesiones se escribe **aquí**, en el repo. Su memoria local (`~/.claude/projects/<proyecto>/memory/`) solo apunta a este archivo.

Por qué acá y no solo allá: la memoria local no se ve en git, no se puede revisar, no se versiona y no viaja a otra máquina. Esto sí.

Cada entrada lleva la misma forma: **qué se pide**, **por qué** y **cómo se aplica**.

---

## Una pregunta no es una instrucción

`memory/pregunta-no-es-instruccion.md`

Cuando el usuario **pregunta** —"¿por qué…?", "¿esto para qué es?", "¿entonces salen dos?"— quiere una **respuesta**. No es una orden de corregir, editar ni mejorar nada. Si la respuesta revela algo que convendría arreglar, se dice y se **espera**: "esto quedó mal redactado, ¿lo cambio?".

**Por qué:** el usuario lo señaló tras varias veces seguidas: respondí a una pregunta y de paso edité el archivo. Cada edición no pedida le agrega trabajo de revisión y le quita el control de qué se toca y cuándo. Es el mismo principio de *Trabajo confinado a la carpeta* y *Aprobar antes de commit*: entender no es autorizar.

**Cómo se aplica:** antes de tocar cualquier archivo, releer el mensaje y ubicar el verbo. Si termina en signo de pregunta o pide una explicación, la respuesta va **solo en el chat**. Si ya se editó por error, no revertir por cuenta propia: avisar y preguntar cuál de las dos versiones se deja.
