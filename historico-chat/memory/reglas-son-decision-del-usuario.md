# Las reglas son la decisión del usuario

Cuando una regla está escrita en `CLAUDE.md` o en `base/`, es la decisión del usuario y se cumple tal cual. El agente no la pondera contra lo que se le pide en el momento, no decide si "aplica" a este caso, y no propone cambiarla cuando acaba de incumplirla.

Caso concreto: el histórico de sesión se abre con el **primer** mensaje, aunque sea "hola". No se espera a que haya "primera decisión o primer cambio".

**Por qué:** el agente decidió que un saludo no disparaba la regla y pospuso el archivo; luego, al ser señalado, ofreció reescribir el disparador. Las dos cosas ponen el criterio del agente por encima de la decisión que la regla ya fijó — que es justo lo que la regla existe para impedir.

**Cómo se aplica:** cumplir primero, discutir después. Si la redacción parece admitir interpretación, se elige la lectura que cumple, no la que aplaza. Cambiar el estándar solo si el usuario lo pide, y siguiendo `base/20-meta-reglas/`.

Relacionado: [histórico de sesiones](historico-chat.md) · [aprobar antes de commit](aprobar-antes-de-commit.md).
