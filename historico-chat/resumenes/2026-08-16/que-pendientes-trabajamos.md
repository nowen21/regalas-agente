# 2026-08-16 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-que-pendientes-trabajamos.md](../../2026-08-16-que-pendientes-trabajamos.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** la sesión que priorizó el backlog ([2026-08-16 · la prioridad de los pendientes](../../2026-08-16-la-prioridad-de-los-pendientes.md)). Allá se puso la `P`; acá se preguntó qué hay que hacer con los `P0`.

---

## Hallazgos de esta sesión

### H-1 · El `P0` más urgente del backlog ya estaba resuelto

- **Qué pasó:** el usuario preguntó si el borrado de memoria del pendiente 39 «sigue pasando», y después dijo lo que resultó ser la respuesta: *«solo pasó en un proyecto y creo que desde allá se corrigió»*. Se comprobó, y es así:
  - **El código no puede repetirlo.** `migrar()` en [`validadores/recuerdos.py`](../../../validadores/recuerdos.py) (líneas 140–174) solo mueve, con dos guardas — `enlazada()` compara por identidad en disco con `os.path.samefile` y no por el texto de la ruta, y el cinturón de la línea 166 se salta mover un archivo sobre sí mismo. El único `os.remove` que queda en `validadores/` es el de la marca de instalación incompleta ([`checklist.py:339`](../../../validadores/checklist.py)), que no toca memoria.
  - **El proyecto que lo reportó ya se recuperó.** `agro-system`, commit `6d4b130` — *«actualiza a 3.1.1 y saca la memoria del junction»*. Los 75 archivos de `713444b` volvieron; hoy hay 78 y `git status` de esa carpeta está limpio.
  - **Ningún otro proyecto pudo estar afectado.** El defecto solo se dispara con el almacén enlazado. Las nueve carpetas `historico-chat/memory/` del registro y los 16 almacenes de `~/.claude/projects/*/memory/` son todos carpeta normal: ninguno enlazado.
  - Y el `CHANGELOG.md` de la 3.1.1 ya lo decía en una línea que nadie había cruzado con el resto: *«Pasó en un proyecto real, dos veces»* — un proyecto, no varios.
- **Por qué importa:** el pendiente llevaba nueve días encabezando el backlog como «se pierde información que no está en ninguna otra parte», y no había nada que perder. Lo que lo mantuvo vivo fue confundir dos preguntas: *¿el defecto sigue produciéndose?* y *¿el daño quedó deshecho?*. La primera se contestó el 2026-08-07 y la segunda nunca se hizo, así que el pendiente heredó la urgencia de la primera sin tener su contenido.
- **Qué lo soluciona:** cerrarlo, con la comprobación escrita para que no haya que volver a hacerla.
- **Qué se decidió:** cerrarlo y pasarlo a `pendientes/hecho/`, dejando dicho **qué proyecto lo reportó** — lo pidió el usuario, y es lo que faltaba: el pendiente decía «el proyecto de origen es el estándar mismo», que es de quién era el defecto, no quién lo encontró. Son dos datos distintos y el segundo es el que sirve para avisar al cerrar.
- **Estado:** resuelto acá.
- **Responde a:** el hallazgo H-3 del [resumen del 2026-08-07](../2026-08-07/memoria-del-agente-en-el-repo.md), que quedó abierto nueve días.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/memoria-borrada-por-el-enganche.md](../../../pendientes/hecho/memoria-borrada-por-el-enganche.md). Se actualizaron además el [README de pendientes](../../../pendientes/README.md), el [pendiente 33 · punto 6](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) y el [resumen del 2026-08-07](../2026-08-07/memoria-del-agente-en-el-repo.md), donde el hallazgo por fin tiene fecha de cierre.
- **Nace en:** 2026-08-16 · qué pendientes trabajamos.
- **Cerrado en:** 2026-08-16 · qué pendientes trabajamos.
- **Con qué se retoma:** —

### H-2 · El paso 1 del pendiente 39 se apoyaba en un archivo que git no guarda

- **Qué pasó:** su paso 1 mandaba sacar la fecha de instalación de cada proyecto del historial de git de [`plantillas/proyectos.md`](../../../plantillas/proyectos.md). Ese archivo está en `.gitignore` (línea 20) y git no lo rastrea: `git log` sobre él devuelve vacío, y el propio archivo lo dice en su cabecera — «NO se versiona».
- **Por qué importa:** era el primero de los cuatro pasos y de él salían los demás. Quien lo hubiera tomado se estrellaba en el primer comando. Y muestra algo más general: **un pendiente escrito y no ejecutado no está comprobado**. Este llevaba nueve días citando una fuente que no existe, y nadie lo notó porque nadie lo abrió.
- **Qué lo soluciona:** la fecha de instalación sale del **primer commit del `CLAUDE.md`** instalado en cada proyecto, que sí se versiona en el repositorio del proyecto.
- **Qué se decidió:** quedó escrito dentro del archivo de `hecho/`, aunque el pendiente ya no se vaya a ejecutar: si alguna vez hace falta esa fecha, la vía buena está anotada y no se vuelve a proponer la mala.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/memoria-borrada-por-el-enganche.md](../../../pendientes/hecho/memoria-borrada-por-el-enganche.md), sección «Por qué se cerró sin ejecutar lo que pedía».
- **Nace en:** 2026-08-16 · qué pendientes trabajamos.
- **Cerrado en:** 2026-08-16 · qué pendientes trabajamos.
- **Con qué se retoma:** —

### H-3 · El `CLAUDE.md` de este repo mandaba escribir a mano lo que el enganche ya escribe

- **Qué pasó:** se cerró el punto 2 del [pendiente 29](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md). Su sección 1 ordenaba *«actualizarlo después de cada intercambio»*, *«la transcripción literal»* y *«cada interacción lleva `AAAA-MM-DD HH:MM:SS` leída del reloj»*, sin decir que [`hook_historico.py`](../../../validadores/hook_historico.py) ya lo hace solo. El agente obedecía y escribía encima.
- **Por qué importa:** el resultado eran archivos con la conversación duplicada —61 encabezados de usuario para 30 mensajes— y horas estimadas donde el enganche había puesto las reales. Ya había pasado seis veces.
- **Qué lo soluciona:** dos cosas que aparecieron durante la conversación y no estaban en el pendiente:
  - **Eran dos archivos, no uno.** [`historico-chat/README.md`](../../README.md) repetía la misma orden, y el `CLAUDE.md` manda ahí para el formato: arreglar uno solo dejaba la orden viva.
  - **La redacción ya existía.** [`plantillas/CLAUDE.md.plantilla`](../../../plantillas/CLAUDE.md.plantilla) dice *«La escribe el programa, no el agente»* desde que se automatizó el histórico. Se actualizó la plantilla que viaja a los proyectos y no la del repo que la escribe, así que **el defecto era solo de acá** — un proyecto instalado leía la versión buena. Es el mismo hueco que el propio `CLAUDE.md` §0 ya describe: *«un proyecto heredero cumplía más que el repo del que hereda»*.
- **Qué se decidió:** las dos secciones ahora dicen que la transcripción la escribe el enganche y que el agente no la toca — solo comprueba que exista y propone el nombre cuando el enganche se lo pide. Lo que sí le queda al agente es el resumen, que es otra cosa: lo que quedó, no lo que se dijo.
- **Estado:** resuelto acá. El punto 1 del 29 —limpiar el archivo del 2026-08-15— sigue abierto, ahora sin riesgo de volver a ensuciarse.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [`CLAUDE.md`](../../../CLAUDE.md) §1 y [`historico-chat/README.md`](../../README.md). El pendiente 29 baja de `P0` a `P2` en el [README de pendientes](../../../pendientes/README.md), y su dependencia dura queda resuelta.
- **Nace en:** 2026-08-16 · qué pendientes trabajamos.
- **Cerrado en:** 2026-08-16 · qué pendientes trabajamos.
- **Con qué se retoma:** —

### H-4 · Se leyó de más para contestar una pregunta que un `grep` ya había contestado

- **Qué pasó:** al preguntar el usuario si el cambio tocaba también las plantillas, el agente siguió abriendo archivos después de que la búsqueda ya había dado la respuesta. El usuario cortó dos veces: *«para contestar la pregunta tiene que leer todos esos archivos?»* y *«no tendría que leer todo el proyecto para responderme o sí?»*.
- **Por qué importa:** es lo mismo que [`00·ID9`](../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) pide del texto, aplicado a la investigación: cuando la evidencia ya alcanza, seguir buscando no agrega certeza, gasta el turno del usuario. Y hubo un segundo error de fondo: el agente insistió en que la plantilla y el `CLAUDE.md` son hermanos sin ver que, para la pregunta que el usuario hacía —*¿el padre está mal?*—, el dato que zanjaba era uno solo y ya lo tenía en la mano.
- **Qué lo soluciona:** parar en cuanto la respuesta esté, y darla.
- **Qué se decidió:** queda anotado acá. No se promueve a regla: es conducta, y ya hay memoria del usuario sobre brevedad.
- **Estado:** anotado.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** este resumen.
- **Nace en:** 2026-08-16 · qué pendientes trabajamos.
- **Cerrado en:** —
- **Con qué se retoma:** si vuelve a pasar, es candidata a recuerdo en [`historico-chat/memory/`](../../memory/memory.md).

### H-5 · El validador de enlaces no era un programa que se pudiera correr

- **Qué pasó:** durante toda la sesión el agente comprobó su trabajo con `python validadores/enlaces.py <archivos>` y reportó «sin roturas» tres veces. [`enlaces.py`](../../../validadores/enlaces.py) **no tiene `__main__`**: es una biblioteca. Correrlo así no comprueba nada y sale con código 0. El programa real es `validar.py estandar`, y al correrlo aparecieron 88 fallas.
- **Por qué importa:** un cero de un programa que no hizo nada se lee igual que un cero de uno que sí. El agente le dio al usuario tres confirmaciones vacías.
- **Qué lo soluciona:** correr el punto de entrada, no el módulo. Los que tienen `__main__` son `validar.py`, `citas.py`, `historico.py`, `instalar.py`, `pruebas.py` y los `hook_*`.
- **Qué se decidió:** queda anotado. Es candidato a que `enlaces.py` avise cuando se lo llama directo, en vez de salir en silencio.
- **Estado:** anotado.
- **Dónde queda:** este resumen.
- **Nace en:** 2026-08-16 · qué pendientes trabajamos.
- **Cerrado en:** —
- **Con qué se retoma:** ¿un módulo del estándar que se puede invocar y no hace nada debería fallar en vez de callar?

### H-6 · El pendiente 34 daba por bueno lo que había que comprobar

- **Qué pasó:** se ejecutó el [34](../../../pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md) — los enlaces de las plantillas pasan de `../base/…` a `«RUTA-ESTANDAR»/base/…`. Su paso 3 decía de [`enlaces.py`](../../../validadores/enlaces.py): *«en principio el validador la comprueba sin cambios; confirmarlo con una prueba»*. La prueba dijo que no: **87 enlaces quedaron dados por rotos**, porque dentro de este repositorio el marcador está sin llenar. Hubo que enseñárselo.
- **Por qué importa:** es lo mismo que el H-2 con el otro pendiente. Un pendiente escrito describe lo que alguien supone; recién al ejecutarlo se sabe. Dos de dos en esta sesión.
- **Qué lo soluciona:** ya está — el validador resuelve el marcador contra la raíz del repositorio.
- **Qué se decidió:** además, la cuenta del pendiente estaba vieja: eran **91** enlaces en **22** plantillas, no 77 en 21.
- **Estado:** resuelto acá.
- **Dispara:** el aviso a `shopnest-mesa`, **escrito el mismo día**: su pendiente 01 y la fila de su README dicen que la corrección está hecha, con qué opción se eligió y qué falta de su lado. Queda abierto allá hasta que corran el instalador y comprueben — el aviso no cierra el pendiente del proyecto, lo desbloquea. Lo mandó una persona acordándose, que es el paso 6 que el [36](../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md) todavía no automatiza.
- **Dónde queda:** [pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md](../../../pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md), las 22 plantillas, [`enlaces.py`](../../../validadores/enlaces.py) y el [CHANGELOG](../../../CHANGELOG.md) 20.0.1.
- **Nace en:** 2026-08-16 · qué pendientes trabajamos.
- **Cerrado en:** 2026-08-16 · qué pendientes trabajamos.
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 y H-2 en [pendientes/hecho/memoria-borrada-por-el-enganche.md](../../../pendientes/hecho/memoria-borrada-por-el-enganche.md); H-3 en el [`CLAUDE.md`](../../../CLAUDE.md) y el [README del histórico](../../README.md); H-6 en [pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md](../../../pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md) |
| Todo hallazgo abierto tiene su pendiente creado | ☑ quedan anotados el H-4 y el H-5, los dos acá; lo que sigue del 29 es su punto 1, ya en el [pendiente](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia. El H-6 disparó el aviso a `shopnest-mesa`, escrito allá |
| Lo que se hizo está aprobado y guardado | ☑ commit `1c0b70f`, 41 archivos. Sin `push`, y sin commitear el aviso a `shopnest-mesa`: el usuario pidió solo este repositorio |

**Sí se puede cerrar**, salvo el commit. La sesión entró con cuatro `P0` y sale con uno: el **36**. Se cerraron el 39, el punto 2 del 29 y el 34.

Lo que sigue vivo y no es de esta sesión: el punto 1 del 29, y el hueco del sello entre el `CLAUDE.md` y su plantilla — se habló acá y no se creó pendiente, por decisión del usuario.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
