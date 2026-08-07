# Estilo de redacción simple

Dos estándares de redacción distintos según quién lee:

1. **Reglas y specs que lee el AGENTE** (`base/*.md`): **concisas, precisas y técnicas**. Cortar palabrería —introducciones adornadas, párrafos de motivación, secciones de relleno— pero **conservar los términos técnicos exactos y las condiciones y excepciones**: el agente necesita esa precisión para actuar bien. Simplificar de más lo perjudica y lo vuelve menos productivo.
2. **Texto que el agente PRODUCE para el usuario final** (UI, ayuda, mensajes): ahí sí, "que hasta un niño lo entienda", cero jerga, legible en 20 segundos. Eso es capa 3 (convenciones de UI del proyecto), no el rulebook.

**Por qué:** el usuario confundió ambos al pedir simplicidad; se aclaró que la base la lee el agente para obedecerla — *"la escribe el usuario, la obedece el agente, como un contrato"*. Se optimiza el estilo para el lector real de cada texto.

**Cómo se aplica:** en `base/*.md`, regla en una línea en negrita + una o dos frases planas; mantener la jerga técnica y las excepciones; conservar los ejemplos INCORRECTO/CORRECTO; reducir intros y secciones de "relación" a una línea.

Relacionado: [manuales claros](manuales-claros.md) — esa es para los manuales que leen personas, no para las reglas.
