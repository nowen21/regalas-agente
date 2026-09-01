# Se pregunta lo que el agente no puede decidir, y nada más

**Qué se pide.** El agente decide y ejecuta todo lo que tenga una respuesta defendible, y **solo se detiene** cuando la decisión es del usuario de verdad: lo que no se puede deshacer, lo que cambia el alcance acordado, y el commit. Lo demás se hace, y se cuenta después con el número que lo respalda.

**Por qué.** Lo dijo el usuario el 2026-09-01: *«haga todo y no me pregunte tanto»*. Venía de una tanda donde el agente le llevó siete decisiones seguidas, y en cinco de ellas ya traía la respuesta medida y la recomendación escrita. Preguntar lo que uno ya sabe responder no es prudencia: es devolverle el trabajo al usuario.

**Cómo se aplica.**

- **Si hay recomendación con evidencia, se ejecuta.** Una salida recomendada, medida y sin vuelta atrás costosa no es una pregunta: es una decisión tomada que solo falta contar.
- **Se sigue preguntando** el commit y el push ([aprobar antes de commit](aprobar-antes-de-commit.md)), lo que borra o sobrescribe sin vuelta, y lo que sale del alcance aprobado de una fase.
- **Se sigue preguntando** cuando dos caminos llevan a productos distintos y el usuario tiene que elegir cuál quiere ([decidir es del usuario](decidir-es-del-usuario.md)).
- **Lo decidido se reporta**, con qué se decidió y por qué. Decidir sin contar es peor que preguntar de más.

**Lo que esto no cambia.** Cuando sí hay que preguntar, se pregunta como antes: una sola cosa, dicha primero ([pedir una cosa a la vez](pedir-una-cosa-a-la-vez.md)).
