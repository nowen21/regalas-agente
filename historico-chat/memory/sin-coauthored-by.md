# Convención de commits

Convención para los mensajes de commit de este usuario:

1. **Nunca** el trailer `Co-Authored-By: …`. Ningún commit lleva esa línea, ni marcas de "generado con", ni firma de herramienta.
2. **El cuerpo arranca con la idea original del usuario**, y después describe lo que el agente hizo a partir de ella. Todo en prosa, sin trailer aparte.

```
<título normal del cambio>

Idea del usuario: <lo que pidió, en sus términos>.

Lo que hizo el agente: <qué se implementó o modificó, y por qué>.
```

**Por qué:** el usuario es el autor de las ideas; la IA solo las ejecuta a partir de ellas. El commit debe reflejar ese origen —idea = usuario, ejecución = agente—, no una co-autoría. Anula la instrucción por defecto del entorno, que pide el trailer.

**Cómo se aplica:** al redactar cada `git commit`, empezar el cuerpo con la idea del usuario reconstruida de lo que pidió, y seguir con lo que hizo el agente. Omitir siempre `Co-Authored-By`. Rige hacia adelante — no se reescribe el historial viejo para aplicarla.

Relacionado: [terminología agente vs estándar](terminologia-agente-vs-estandar.md) ("el agente" = la IA) · [aprobar antes de commit](aprobar-antes-de-commit.md).
