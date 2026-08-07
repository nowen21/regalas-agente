# No tocar el trabajo de otras sesiones

Al commitear, montar **solo lo que hizo esta sesión**. El trabajo que aparece en el árbol y lo hizo otra sesión no se commitea, aunque el usuario diga "suba" y aunque esté terminado y en verde. Cada sesión sube lo suyo.

**Por qué:** el que versiona tiene que ser el que hizo el cambio. Cuando una sesión commitea el trabajo de otra, las entradas del `CHANGELOG` de ambas caen en el mismo movimiento y **ningún commit corresponde ya a un salto de versión** — que es justo lo que `M10` pide al exigir versionar "en el mismo movimiento". Pasó el 2026-08-07: un commit terminó registrando seis versiones (1.3.1 → 2.0.0) escritas por dos sesiones en paralelo, y el historial dejó de decir qué cambio trajo qué versión. Además, describir en el mensaje un trabajo que no se hizo obliga a reconstruirlo del `CHANGELOG`, que es adivinar.

**Cómo se aplica:** antes de `git add`, comparar el árbol contra lo que se tocó en esta sesión. Lo ajeno se deja quieto y **se dice**: "esto lo está trabajando otra sesión, no lo subo". Si el usuario insiste en subirlo, es su decisión, pero se avisa primero de que el versionado queda mezclado. Nunca montar carpetas enteras (`git add validadores/`) sin mirar qué arrastran.

Relacionado: [aprobar antes de commit](aprobar-antes-de-commit.md) · [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) — mismo principio: el alcance de lo que se toca lo fija el usuario, no la conveniencia del momento.
