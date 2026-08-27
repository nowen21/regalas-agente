# Los programas de un solo uso de cada sesión

**Qué guarda esta carpeta.** Los programas que el agente escribió **para aplicar un cambio en lote** durante una sesión: recortar treinta reglas al molde, volver a sellar checklists, escribir los documentos de una fase, medir algo del repositorio.

**Por qué están acá y no fuera.** Lo decidió el usuario el 2026-08-22, con estas palabras: *«nada se debe escribir por fuera, todo debe quedar en historico-chat»*. Hasta ese día vivían en una carpeta temporal del sistema, así que el **resultado** quedaba versionado y el **cómo** se borraba con el temporal: a la pregunta «¿con qué se recortaron esas treinta reglas?» no había respuesta.

**Una carpeta por día**, con el nombre de la fecha. Adentro, un archivo por programa, con el nombre que tuvo al correrse.

**Los días 24 a 27 llegaron tarde.** La regla se fijó el 2026-08-22 y **se dejó de cumplir al día siguiente**: 38 programas siguieron escribiéndose en la carpeta temporal del sistema hasta que el usuario volvió a preguntar el 2026-08-27. Se trajeron ese día, con la fecha real de cada uno. Está contado en `S-057`.

## Qué son y qué no son

| Son | No son |
|---|---|
| El registro de **cómo** se aplicó un cambio grande | Parte del estándar: no viajan a los proyectos |
| Material de una sesión concreta, con su fecha | Herramientas de `validadores/`, que tienen contrato, pruebas y se corren siempre |
| De un solo uso: sirvieron una vez | Algo que haya que mantener, ni volver a correr |

**No se vuelven a correr.** Casi todos escriben sobre rutas que ya cambiaron, y varios llevan dentro la ruta de la máquina donde corrieron. Se guardan **para leerlos**, no para ejecutarlos: son la respuesta a «¿qué le hizo esta sesión al repositorio, exactamente?».

**Si un programa de estos se vuelve útil dos veces, deja de ser de un solo uso**: entonces baja a `validadores/` por la cadena, con su contrato y sus pruebas, como cualquier otra herramienta ([`02·F23`](../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

## Índice

| Día | Qué se hizo con ellos |
|---|---|
| [2026-08-22](2026-08-22/) | El pendiente 19 (las 27 reglas que reprobaban y las 34 pasadas de largo), el 33 entero, y quince fases del 59 |
| [2026-08-24](2026-08-24/) | El borrador de las fichas de funcionalidad de la plataforma |
| [2026-08-25](2026-08-25/) | Las fases C a H de la versión 1 de la plataforma, con sus pruebas y sus cinco sabotajes, y las 23 estaciones de commit que nadie marcó |
| [2026-08-26](2026-08-26/) | El inventario que dejó de mantenerse a mano, el tope de ruta de Windows, el vocabulario del estado, y los cinco documentos que citaban una historia cerrada como abierta |
| [2026-08-27](2026-08-27/) | La `HU-021` en sus dos fases, el resumen de la sesión que iba nueve hallazgos atrás, y el pendiente 88 |
