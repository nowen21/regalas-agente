# Memoria del agente — cómo se trabaja en este repo

Lo que el agente debe recordar entre sesiones se escribe **aquí**, en el repo. Su memoria local (`~/.claude/projects/<proyecto>/memory/`) solo **apunta** a estos archivos: allá queda una línea, acá el texto completo.

**Por qué acá y no solo allá:** la memoria local no se ve en git, no se puede revisar, no se versiona y no viaja a otra máquina. Esto sí.

**Un archivo por recuerdo**, con el mismo nombre que su puntero en la memoria local. Cada uno lleva la misma forma: **qué se pide**, **por qué** y **cómo se aplica**.

No es norma (`20·M13`): la norma vive en `base/`. Esto es preferencia del usuario sobre cómo trabajar.

---

## Índice

| Recuerdo | De qué se trata |
|---|---|
| [Aprobar antes de commit](aprobar-antes-de-commit.md) | No hay commit ni push hasta que el usuario lea el cambio y lo apruebe; "sí" al cambio no es "sí" al commit. |
| [Estilo de redacción simple](estilo-redaccion-simple.md) | Las reglas que lee el agente son técnicas y precisas; "que un niño lo entienda" es solo para la UI del usuario final. |
| [Fixtures sin secretos literales](fixtures-sin-secretos-literales.md) | En tests y ejemplos, los tokens se arman en runtime: GitHub bloquea el push si ve un secreto con forma real. |
| [Histórico de sesiones](historico-chat.md) | Cada sesión se transcribe literal en `historico-chat/`, con marca de tiempo del reloj del sistema. |
| [Las reglas son la decisión del usuario](reglas-son-decision-del-usuario.md) | Una regla escrita se cumple tal cual; no se pondera, no se reinterpreta, no se propone cambiarla al incumplirla. |
| [Manuales claros](manuales-claros.md) | Tercera persona, sin etiquetar al lector por rol, paso a paso literal, el camino más simple. |
| [Pendientes en el repo](pendiente-patrones-devops.md) | El backlog del estándar vive en `pendientes/`, versionado; la memoria es solo el puntero. |
| [Respuestas cortas](respuestas-cortas.md) | Conclusión primero y pocas líneas; los detalles van en los archivos, no en el chat. |
| [Terminología: agente vs estándar](terminologia-agente-vs-estandar.md) | "El agente" es la IA; "el estándar" son las reglas centralizadas. No se intercambian. |
| [Toda herramienta se autoinstala](herramienta-se-autoinstala.md) | Llega sola a cada proyecto vía `instalar.py`; exigir configuración manual es defecto del estándar. |
| [Todo multiproyecto](todo-multiproyecto.md) | Lo que se construya sirve a cualquier proyecto: universal de raíz, o universal por detección de stack. |
| [Trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) | Mientras se trabaja un tema, todo va dentro de su carpeta; replicar al resto lo indica el usuario. |
| [Una pregunta no es una instrucción](pregunta-no-es-instruccion.md) | Si el usuario pregunta, se responde en el chat y no se edita nada. |
| [Convención de commits](sin-coauthored-by.md) | El cuerpo arranca con la idea del usuario y sigue con lo que hizo el agente; nunca `Co-Authored-By`. |
