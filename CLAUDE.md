# Trabajar en este repo

Este repo **es el estándar**: las reglas que otros proyectos heredan (`base/`, `plantillas/`, `skills/`, `validadores/`).

Este archivo manda sobre el trabajo **dentro de este repo** — mantener el estándar. No viaja a los proyectos que lo heredan; lo que sí les llega es `base/` (`00·M13`).

## 0 · Obedecer `base/` antes de tocar nada

Las reglas de `base/` se obedecen. No se cargan todas al abrir: con cada mensaje llegan las de las tareas que pide su palabra clave de `01·C28`. Si el mensaje no trae la palabra, el agente no actúa: la recuerda y espera. Las reglas de cada tarea están completas en [`base/reglas-por-tarea/`](base/reglas-por-tarea/README.md). Qué reglas tiene cada tarea lo dice [`base/mapa-de-tareas.md`](base/mapa-de-tareas.md). `base/00-nucleo-blindado.md` tiene prioridad absoluta y no se contradice nunca.

Es el mismo paso 2 que el `CLAUDE.md` instalado le exige a cualquier proyecto que hereda ([`plantillas/CLAUDE.md.plantilla`](plantillas/CLAUDE.md.plantilla)). Acá faltaba, y la consecuencia era esta: el agente escribía el estándar sin haber leído el estándar, así que lo incumplía escribiéndolo. Un proyecto heredero cumplía más que el repo del que hereda.

Las reglas se aplican a lo que el agente entrega en este repo, sin excepción. `00·ID8` no dice "todo documento del proyecto": dice **"todo documento que el agente entrega"**, y eso incluye las respuestas del chat, los planes, las especificaciones y el histórico.

## 1 · Toda sesión se escribe en `historico-chat/` — sin que haya que pedirlo

Es obligatorio, no una cortesía. El chat se borra; el repo no.

**La escribe el programa, no el agente.** [`validadores/hook_historico.py`](validadores/hook_historico.py) anota cada mensaje del usuario apenas lo envía y cada respuesta del agente apenas termina, con la hora del reloj de la máquina, y le pone su línea al índice. Así queda registrado desde el primer mensaje, aunque sea un "hola".

**El agente no la escribe.** Solo comprueba que el archivo exista y, cuando el enganche se lo pide, propone el nombre del tema. Escribir la transcripción a mano la duplica y le mete horas inventadas: ya pasó seis veces.

Lo que sí escribe el agente es el **resumen** de la sesión, en `historico-chat/resumenes/` — lo que quedó, no lo que se dijo. Va en el momento en que aparece cada hallazgo, no al cerrar.

Formato y plantilla, en [`historico-chat/README.md`](historico-chat/README.md).

## 2 · Agregar o cambiar una regla del estándar

El procedimiento completo está en las meta-reglas del preámbulo — se sigue tal cual, sin atajos. En corto: buscar antes de crear (`M12`), enrutar (`M13`, `M1`, `M2`), verificar que sea agnóstica de stack (`M3`), ID libre del prefijo del capítulo (`M4`), formato canónico con una sola exigencia y ejemplo INCORRECTO/CORRECTO (`M5`), declarar dependencias y excepciones (`M7`, `M8`), decidir si es validable (`M9`), versionar (`M10`).

**Y si el cambio sale de un pendiente, primero va la cadena.** El backlog de [`pendientes/`](pendientes/) no se ejecuta desde su archivo: cada uno se baja a historia de usuario y se construye como fase, con su plan y sus pruebas (`02·F23`). Ese procedimiento dice cómo queda escrita la regla; no reemplaza los eslabones de `02·F0`.

**Versionar no es opcional** (`M10`): todo cambio del estándar o de la configuración de un proyecto sube su versión y deja su registro. El estándar pasa a vivir en la base de Cimiento y se administra desde su pantalla ([EP-026](documentacion/epicas/EP-026-el-estandar-vive-en-la-base-de-cimiento-y-cada-cambio-queda-versionado/epica.md)); mientras esa base no lo guarde, el registro es [`CHANGELOG.md`](CHANGELOG.md) y la versión, [`VERSION`](VERSION).

- **MAYOR** — obliga a un proyecto al día a hacer algo nuevo.
- **MENOR** — aditivo: regla opt-in, plantilla, validador, capítulo.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

Nada se renumera ni se borra: las reglas se derogan (`M11`), porque especificaciones, commits y fases cerradas citan por ID.

## 3 · Dónde va cada cosa

| Si es… | Va en… |
|---|---|
| Regla que aplica a **cualquier** proyecto | `base/` |
| Instructivo para mantener el estándar | este `CLAUDE.md` |
| **Por qué** se diseñó algo así (razonamiento, alternativas) | `notas/` |
| Mejora acordada pero aún no hecha | `pendientes/` |
| Lo que pidió el usuario, con sus palabras | `prompts/` |
| Qué pasó en una sesión | `historico-chat/` |
| Preferencia del usuario sobre cómo trabajar | [`historico-chat/memory/`](historico-chat/memory/memory.md) |
| **Cómo está armado** el estándar por dentro: qué archivo hace qué | [`anatomia/`](anatomia/mapa-del-sitio.md) |

Regla que solo sirve a un stack o a un cliente: no va en `base/` (`M3`, `M13`).

**La memoria del agente es un archivo del repo, no un ajuste de la herramienta** (`01·C19`). Todo recuerdo se escribe en [`historico-chat/memory/`](historico-chat/memory/memory.md) —uno por archivo, con su línea en el índice— y el almacén de Claude Code (`~/.claude/projects/<proyecto>/memory/`) queda **vacío**: ni el texto ni un puntero. Lo que aparezca ahí lo mueve solo `validadores/hook_recuerdos.py`.

## 4 · Antes de commitear

No hacer `commit` ni `push` hasta que el usuario haya leído el cambio y lo apruebe. Que apruebe el cambio no es que apruebe el commit: se pregunta aparte. Cuando Cimiento tenga su botón para subir a git ([EP-026·HU-007](documentacion/epicas/EP-026-el-estandar-vive-en-la-base-de-cimiento-y-cada-cambio-queda-versionado/HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento/HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md)), esa aprobación se da desde la pantalla.

En el cuerpo del commit va primero la idea del usuario y después lo que hizo el agente. Nunca `Co-Authored-By`.
