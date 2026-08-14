# Terminología: agente vs estándar vs Claude

Decisión de nomenclatura para este repo y todos sus documentos. Son **tres** cosas distintas y no se intercambian:

- **El agente** = lo que construye este repositorio: los programas que se instalan en cada proyecto con `instalar.py` (validadores, enganches, memoria, métricas) más el texto que los guía (reglas, plantillas, skills). Tiene dos mitades: la determinista corre sola; la de criterio es papel hasta que alguien la aplica ([`anatomia/componentes-del-agente.md`](../../anatomia/componentes-del-agente.md)).
- **El estándar** = la parte del agente que es norma: `base/` + `plantillas/`. Vive en una carpeta central y **no** se copia dentro de cada proyecto.
- **Claude** (o Claude Code) = la IA que opera el agente leyendo el estándar. Se usa como app de escritorio, comando de terminal o extensión del editor. **No es el agente**: el agente no incluye a la IA, la IA lo usa.

Frases modelo: *"el agente se instala en el proyecto"*, *"Claude trabaja con base al estándar"*, *"el agente lee el estándar desde la carpeta central"*. Nunca decir *"el agente es Claude"*, *"se instala Claude en el proyecto"* ni *"el agente está centralizado"* — lo centralizado es el estándar.

**El agente aprende escribiendo, no entrenando.** Lo que sabe está en sus archivos —reglas, notas, memoria, pendientes— y llegó ahí porque alguien lo escribió después de vivirlo en un proyecto real. Eso **no** es machine learning: no hay modelo que ajuste sus números solos con los datos, y la carpeta no llama a ninguna API. La única pieza con un modelo es `memoria/semantica.py`, y tampoco aprende: usa uno ya entrenado, local y fijo, solo para comparar textos parecidos.

**Por qué:** el usuario lo eligió al detectar que el manual mezclaba los sentidos de "agente" y confundía. El 2026-08-13 lo corrigió otra vez, porque este mismo archivo decía "el agente = Claude Code" y eso llevó a responder que el agente maneja machine learning. Quien es machine learning es Claude, que no es el agente.

**Cómo se aplica:** en manual, README, plantillas y toda comunicación, usar "el agente" solo para lo que este repo construye e instala, "el estándar" para `base/` + `plantillas/`, y "Claude" para la IA que lo opera.
