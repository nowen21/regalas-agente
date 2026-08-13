### Regla: Toda regla de proyecto debe estar respaldada por una regla del agente

Toda regla que se cree dentro de `reglas-proyecto` de cualquier proyecto debe estar basada en una **regla previamente definida en las reglas del agente**.

Si la regla que se necesita para el proyecto **no existe en las reglas del agente**, primero se debe crear dicha regla siguiendo estrictamente el **estándar establecido para la creación de reglas del agente**. Una vez creada y validada la regla del agente, se podrá crear la regla correspondiente dentro de `reglas-proyecto`.

De esta manera, ninguna regla de proyecto podrá existir de forma aislada ni establecer criterios que no estén contemplados en el estándar general del agente.

Esta misma condición aplica a **todas las reglas que se creen, modifiquen o incorporen posteriormente en `reglas-proyecto` de cada proyecto**: siempre deberán tener como fundamento una regla del agente.

**Principio obligatorio:**

> Si una regla de proyecto no tiene una regla equivalente que la respalde en las reglas del agente, primero debe crearse la regla del agente aplicando su estándar correspondiente.
