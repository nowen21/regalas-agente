# Aprobar antes de commit

Nunca ejecutar `git commit` ni `git push` por iniciativa propia. El flujo es: **el agente hace el cambio en los archivos → el usuario lo lee → el usuario aprueba → recién ahí se hace commit/push.**

**Por qué:** el usuario quiere revisar cada cambio antes de que entre al historial. *"Yo primero leo y luego apruebo."* Un "sí" a hacer un cambio NO es un "sí" a commitearlo.

**Cómo se aplica:** tras editar, presentar o resumir el cambio y **esperar aprobación explícita** ("sube", "commit", "ya, apruébalo") antes de tocar git. No encadenar el commit en la misma acción que produjo el cambio.

Relacionado: [convención de commits](sin-coauthored-by.md) (formato del mensaje una vez aprobado) · [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) (aprobar el cambio y aprobar su propagación son permisos distintos).
