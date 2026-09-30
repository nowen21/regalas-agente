# El registro del proceso no cuenta como trabajo por guardar

**Qué se pide.** Para decidir si algo falta por guardar, o si una sesión se puede cerrar, cuenta solo el trabajo: el código, las reglas y los documentos de la cadena. La transcripción de la sesión en `historico-chat/` y la anotación del commit en el `estado-fase.md` no cuentan: los escriben solos los enganches después de cada mensaje y de cada commit, y entran en el commit siguiente.

**Por qué.** Lo pidió el usuario el 2026-09-30: *«Esos dos archivos hacen parte del histórico y se modifican después del commit o push. Si nos quedamos revisándolos constantemente, entraríamos en un ciclo infinito. Debemos centrarnos en lo que realmente importa»*. El agente había propuesto guardarlos varias veces, y cada commit los volvía a dejar sin guardar.

**Cómo se aplica.**

- No se propone un commit solo para esos archivos, ni se los nombra como algo que falta.
- Cuando entran en un commit de trabajo, van sin comentario aparte.
- Antes de decir que algo falta por guardar, se revisa con `git status` qué es trabajo y qué es registro (`01·C2`).

Relacionado: [aprobar antes de commit](aprobar-antes-de-commit.md) · [histórico de sesiones](historico-chat.md).
