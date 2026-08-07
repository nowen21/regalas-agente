# Terminología: agente vs estándar

Decisión de nomenclatura para este repo y todos sus documentos:

- **El agente** = la IA que hace el trabajo = **Claude Code**. Son lo mismo. Se usa como app de escritorio, comando de terminal o extensión del editor (el editor a secas **no** es el agente).
- **El estándar** = el conjunto de reglas centralizadas (`base/` + `plantillas/`) que el agente sigue. Se instala una vez en una carpeta central y sirve para todos los proyectos. **No** se copia dentro de cada proyecto.

Frase modelo: *"el agente lee el estándar desde la carpeta central"*. Nunca decir "el agente está centralizado" — lo centralizado es el estándar.

**Por qué:** el usuario lo eligió al detectar que el manual mezclaba ambos sentidos de "agente" y confundía. Coincide con las reglas base, que dicen "el agente hace X" refiriéndose a la IA.

**Cómo se aplica:** en manual, README, plantillas y toda comunicación, usar "el agente" solo para la IA y "el estándar" para las reglas centralizadas.
