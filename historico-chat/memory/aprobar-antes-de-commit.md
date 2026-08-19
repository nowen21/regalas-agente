# Aprobar antes de commit

Nunca ejecutar `git commit` ni `git push` por iniciativa propia. El flujo es: **el agente hace el cambio en los archivos → el usuario lo lee → el usuario aprueba → recién ahí se hace commit/push.**

**Por qué:** el usuario quiere revisar cada cambio antes de que entre al historial. *"Yo primero leo y luego apruebo."* Un "sí" a hacer un cambio NO es un "sí" a commitearlo.

**Cómo se aplica:** tras editar, presentar o resumir el cambio y **esperar aprobación explícita** ("sube", "commit", "ya, apruébalo") antes de tocar git. No encadenar el commit en la misma acción que produjo el cambio.

Relacionado: [convención de commits](sin-coauthored-by.md) (formato del mensaje una vez aprobado) · [trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) (aprobar el cambio y aprobar su propagación son permisos distintos).

**Autorización permanente, 2026-08-18.** Trabajando la cola de pendientes el usuario lo paró: *«para qué tanta preguntadera si ya sabe que la tarea es hacer todos los pendientes»*. **Cuando hay una tarea larga ya encargada —cerrar los pendientes, ejecutar una fase aprobada—, el commit y el push van sin preguntar por cada uno.** Preguntar catorce veces por lo mismo no es prudencia: es hacerle repetir el sí.

**Sigue valiendo preguntar** cuando el cambio no está dentro de lo encargado, cuando toca algo que no se puede deshacer, o cuando lo que se va a guardar todavía no se le mostró.
