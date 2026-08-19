# Decidir es del usuario, recomendar es del agente

**Qué se pide.** Cuando el trabajo llega a una bifurcación que el usuario tiene que resolver —dos o tres salidas posibles, y ninguna se deduce de lo que ya está escrito—, el agente **escribe las opciones en el mensaje del chat** y espera. No las decide por su cuenta, ni siquiera declarando el supuesto y siguiendo. Tampoco las pone en el formulario de preguntas de la herramienta: van en el texto de la respuesta.

Recomendar sí, y con el motivo en una línea. Elegir no.

**Por qué.** Una decisión tomada por el agente se pierde: no queda en el chat como decisión, queda enterrada en un plan que el usuario aprueba sin haber elegido. Y el formulario obliga a contestar ahí mismo, en el momento en que la herramienta lo pone, en vez de dejar la pregunta escrita para leerla con calma junto al resto del mensaje.

**Cómo se aplica.**

1. Se listan las opciones en una tabla o una lista corta, con lo que deja cada una.
2. Se marca cuál se recomienda y por qué, en una línea.
3. Se para. No se escribe código ni documentos que dependan de esa decisión.

Es distinto de [[corregir-el-defecto-que-uno-mismo-detecta]]: aquello vale mientras el agente ejecuta algo **ya autorizado**, y ahí sí arregla sin preguntar. Acá no hay autorización todavía, porque justamente falta la decisión. Se apoya en [[pregunta-no-es-instruccion]] y en [[reglas-son-decision-del-usuario]].

Sesión del 2026-08-16: el agente ofreció dos decisiones en el formulario, el usuario lo paró; el agente entonces las tomó él mismo, y el usuario lo paró otra vez — «no señor, no decida usted, no está autorizado a decidir usted».

Sesión del 2026-08-18: volvió a pasar. El agente puso las dos decisiones del pendiente 61 en el formulario — *«no me obligue a responder las preguntas póngalas en la pantalla»*. **Es la segunda vez, y el recuerdo ya lo decía:** no faltó escribirlo, faltó leerlo antes de preguntar.
