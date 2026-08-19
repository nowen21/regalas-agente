# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-por-que-pide-tanto-permiso.md](../../2026-08-07-por-que-pide-tanto-permiso.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Empieza siendo una consulta sobre las pantallas de permiso y termina subiendo el trabajo de tres sesiones.

**Propósito:** que la pantalla de permisos deje de salir a cada rato.

---

## Hallazgos de esta sesión

### H-1 · No pide permiso por leer archivos: pide permiso por Bash

- **Qué pasó:** el usuario preguntó por qué el agente pide tanto permiso para leer archivos del proyecto. No los pide: `Read`, `Glob` y `Grep` dentro del proyecto no preguntan nada. Lo que preguntaba era un comando de shell.
- **Por qué importa:** el comando de la foto juntaba las tres razones que siempre disparan la pantalla — una carpeta fuera del proyecto, una sustitución `$(...)` que no se puede analizar de antemano, y un `&&` que basta con que una parte no esté permitida.
- **Qué lo soluciona:** dos cosas, y solo una es del usuario. Permisos permanentes para los comandos de lectura que salen siempre; y del lado del agente, **leer con las herramientas de lectura en vez de con `cat`, `ls` y `grep` por shell**, y mandar los comandos sueltos y simples.
- **Qué se decidió:** dar permiso por comando y dejar que lo demás pregunte. Se descartaron permitir todo Bash y el modo sin permisos: son los que quitan el control sobre lo que escribe o borra.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la conversación. No quedó escrito como regla ni como memoria; que el agente prefiera las herramientas de lectura sigue dependiendo de que se acuerde.
- **Nace en:** 2026-08-07 · por qué pide tanto permiso.
- **Cerrado en:** 2026-08-07 · por qué pide tanto permiso.
- **Con qué se retoma:** —.

### H-2 · El agente pedía permiso para hacer a mano lo que un enganche ya hacía solo

- **Qué pasó:** una de las pantallas era el agente comprobando que la carpeta de memoria local estuviera vacía. [`hook_recuerdos.py`](../../../validadores/hook_recuerdos.py) ya hace esa comprobación al abrir la sesión y después de cada escritura.
- **Por qué importa:** *«lo correcto es que no corra ese comando, no que le des permiso»*. Cada verificación repetida a mano es una pantalla de permiso que no tenía por qué existir.
- **Qué lo soluciona:** que el agente sepa qué hacen los enganches antes de repetirlo.
- **Qué se decidió:** dejar de correrlo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la conversación. Es el mismo patrón que ocho días después deja el [pendiente 29](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md): el agente rehaciendo a mano lo que el programa ya hizo.
- **Nace en:** 2026-08-07 · por qué pide tanto permiso.
- **Cerrado en:** 2026-08-07 · por qué pide tanto permiso.
- **Con qué se retoma:** —.

### H-3 · Otra transcripción duplicada, esta sí borrada en caliente

- **Qué pasó:** el agente escribió a mano el histórico de esta sesión en un archivo aparte, cuando el enganche ya la estaba escribiendo. Lo notó él mismo y preguntó si lo borraba.
- **Por qué importa:** es el cuarto duplicado del histórico y el **único que se limpió el mismo día**. Los otros tres siguen ahí.
- **Qué lo soluciona:** borrar la copia y su línea del índice.
- **Qué se decidió:** borrado. El índice quedó como estaba antes de que el agente lo tocara.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [pendientes/hecho/la-transcripcion-duplicada-del-15.md](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md), como el caso que muestra cómo se limpia.
- **Nace en:** 2026-08-07 · por qué pide tanto permiso.
- **Cerrado en:** 2026-08-07 · por qué pide tanto permiso.
- **Con qué se retoma:** —.

### H-4 · «Si está mal, ¿para qué me pide permiso para corregir?»

- **Qué pasó:** el agente reportó que una cita quedó apuntando a una regla derogada y preguntó si la corregía. El usuario le devolvió la pregunta.
- **Por qué importa:** de ahí sale una regla de trabajo que se sigue usando: lo que el agente reporta como mal, lo arregla — no pregunta si lo arregla. Vale mientras ejecuta algo ya autorizado; el commit sigue siendo aparte.
- **Qué lo soluciona:** corregir y avisar.
- **Qué se decidió:** se corrigió, y quedó escrito como recuerdo el mismo día.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [corregir el defecto que uno mismo detecta](../../memory/corregir-el-defecto-que-uno-mismo-detecta.md).
- **Nace en:** 2026-08-07 · por qué pide tanto permiso.
- **Cerrado en:** 2026-08-07 · por qué pide tanto permiso.
- **Con qué se retoma:** —.

### H-5 · Un commit se llevó el trabajo de tres sesiones a la vez

- **Qué pasó:** esta sesión no cambió nada del estándar, pero el árbol tenía 25 archivos modificados y 8 nuevos de otras sesiones — incluido el `README` del histórico, que ya venía tocado. El agente puso las tres opciones y el usuario eligió *«suba todo»*: `ef2ae49`, 40 archivos.
- **Por qué importa:** ese commit es el caso que después funda una regla de trabajo. Al mezclarse, las entradas del `CHANGELOG` de varias sesiones caen en el mismo movimiento y **ningún commit corresponde ya a un salto de versión**, que es justo lo que `M10` pide.
- **Qué lo soluciona:** montar solo lo que hizo la sesión, y decir en voz alta qué se deja quieto.
- **Qué se decidió:** subir todo. La lección se escribió después, no acá.
- **Estado:** resuelto, pero en otra sesión.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [no tocar el trabajo de otras sesiones](../../memory/no-tocar-trabajo-de-otras-sesiones.md), que cita este día como el caso que la originó.
- **Nace en:** 2026-08-07 · por qué pide tanto permiso.
- **Cerrado en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Con qué se retoma:** —.

### H-6 · La renumeración de `F4` se cruzó con otra sesión trabajando

- **Qué pasó:** mientras esta sesión iba a commitear, otra estaba renumerando `F4.1`–`F4.5` a `F14`–`F20`. El validador falló con tres enlaces rotos, y después quedó una cita viva apuntando a `F4.3` como si todavía rigiera.
- **Por qué importa:** dos sesiones tocando el mismo capítulo dejan el árbol a medio camino, y quien commitea no sabe si lo que ve está terminado. El mismo choque vuelve a aparecer días después como [pendiente 22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).
- **Qué lo soluciona:** arreglar lo roto antes de subir, y revisar las citas al final.
- **Qué se decidió:** se arreglaron los tres enlaces y la cita a `F4.3`. Las cinco reglas viejas **no se borran**: quedan derogadas apuntando a su reemplazo, porque specs y fases cerradas las citan. Quedó abierto que `M4` sigue reprobando su propia fila por los sub-ID `F12.1`–`F12.13`.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** commit `87200d0`. Lo de los sub-ID sigue vivo en el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).
- **Nace en:** 2026-08-07 · por qué pide tanto permiso.
- **Cerrado en:** 2026-08-07 · por qué pide tanto permiso.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los cinco; H-5 se cerró en otra sesión |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commits `ef2ae49` y `87200d0` |
