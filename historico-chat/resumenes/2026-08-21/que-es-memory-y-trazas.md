# 2026-08-21 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-21-que-es-memory-y-trazas.md](../../2026-08-21-que-es-memory-y-trazas.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** ninguna sesión anterior — el usuario preguntó directamente.

---

## Hallazgos de esta sesión

### H-1 · El pendiente 16 quedó a medio resolver por una sesión cortada, y la decisión reservada al usuario nunca se registró

- **Qué pasó:** Al recibir «resuelva el pendiente 16» se encontró que la sesión 4 del 2026-08-20 ya había recibido la misma orden y quedó cortada a medias: dejó escritos el `CA-05` de HU-007 y la regla `20·M19` con su checklist en CUMPLE, pero los cinco documentos de la fase B quedaron como plantillas vacías, nada se versionó (`VERSION` sigue en 28.0.0, sin entrada de `M19` en el CHANGELOG) y el pendiente sigue en «abierto». Además, el propio pendiente decía que la elección entre sus dos caminos —CA nuevo en HU-007 u historia propia— «es del usuario», y la sesión cortada tomó la opción 1 sin registro de aprobación.
- **Por qué importa:** Sin la cadena, la regla existe pero no se puede citar como cumplida: sin prueba, sin versión y sin cierre. Y una decisión del usuario tomada por el agente sin registro es exactamente lo que la memoria «Decidir es del usuario» prohíbe.
- **Qué lo soluciona:** No abre historia nueva: la fase [B-EP-001-HU-007](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/README.md) ya existe. Esta sesión llenó sus documentos (plan de trabajo con lo hecho declarado como línea base, plan de pruebas con los tres casos del CA-05, resultado en «no ejecutado», checkpoint en la puerta 7, README que repara el enlace roto del §7 de la HU).
- **Qué se decidió:** El usuario confirmó la opción 1 (el `CA-05` en HU-007, lo construido) y aprobó plan y pruebas («si», 2026-08-21). Con eso la fase se ejecutó y cerró: 3 de 3 casos aprobados, versión 28.1.0, pendiente 16 en `hecho/`, señal S-018 con la lección de la sesión cortada.
- **Estado:** resuelto acá
- **Responde a:** EP-001 · HU-007 · CA-05
- **Dispara:** — (la fase existía; no hizo falta crear nada)
- **Orden de resolución:** —
- **Dónde queda:** la fase [B-EP-001-HU-007](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/README.md) cerrada en Cumple, [pendientes/hecho/primero-que-el-proceso-sirva.md](../../../pendientes/hecho/primero-que-el-proceso-sirva.md), la entrada 28.1.0 del [CHANGELOG](../../../CHANGELOG.md) y la señal S-018
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** — (solo falta el commit, que autoriza el usuario)

### H-2 · El usuario fijó la dirección: los proyectos se administran desde Cimiento, no desde un `.md` hardcodeado

- **Qué pasó:** Al analizar los pendientes 73 y 74, el usuario dio la línea de fondo: Cimiento es el mecanismo que obliga a cumplir el estándar, y su interfaz debe permitir registrar, configurar, consultar y administrar todos los proyectos — la lista no puede seguir siendo `plantillas/proyectos.md` escrito a mano. Y ordenó bajar el 73.
- **Por qué importa:** Todo lo que opera sobre «todos los instalados» (instalar, avisar cierres, validar cumplimiento) cuelga hoy de ese archivo, que envejece en silencio.
- **Qué lo soluciona:** La dirección quedó anotada con sus palabras literales en [prompts/la-administracion-de-proyectos-desde-cimiento.md](../../../prompts/la-administracion-de-proyectos-desde-cimiento.md) y como [pendiente 75](../../../pendientes/75-la-administracion-de-proyectos-vive-en-cimiento-no-en-un-md.md) (P3: falta la decisión de diseño de qué es la «interfaz»). El 73 bajó por la cadena: nace [HU-014 — La guía de entrada del estándar](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-014-la-guia-de-entrada-del-estandar/HU-014-la-guia-de-entrada-del-estandar.md) con su fase A, plan y pruebas escritos, esperando la aprobación del usuario (puertas 4 y 7).
- **Qué se decidió:** El usuario aprobó HU-014 y sus planes («si») y la fase se ejecutó y cerró en Cumple: nace `base/guia-de-entrada.md` (heredable; al arranque solo le suma su línea de índice de 102 bytes, desvío declarado en el resultado), versión 28.2.0, pendiente 73 en `hecho/` con aviso a los 9 instalados y el adjunto borrado como ordenaba. Además el usuario decidió la interfaz del 75: es `interfaz/` (el visor Django) y debe adoptar la estructura de `plantillas/estructura-proyecto-django.md`; la brecha quedó medida en el pendiente, que sube a P2.
- **Estado:** resuelto acá (el 74 y el 75 siguen en el backlog, con su orden acordado: 74, luego 75a y 75b)
- **Responde a:** pendientes 73 y 75
- **Dispara:** EP-001 · HU-014 (ya escrita con sus dos CA)
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/la-guia-de-entrada-es-del-estandar.md](../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md), la entrada 28.2.0 del CHANGELOG, la fase A de HU-014 cerrada, y el [pendiente 75](../../../pendientes/75-la-administracion-de-proyectos-vive-en-cimiento-no-en-un-md.md) con la decisión de diseño escrita
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** — (siguen el 74 y el 75, por su orden; y el commit de esta ronda, que autoriza el usuario)

### H-3 · El 74 bajó por la cadena: el inventario de funcionalidades como puerta de las épicas

- **Qué pasó:** Publicado el 73 (commit `98468b6`, tras dos tropiezos del trinquete de marcas resueltos), se bajó el 74 según el orden acordado. Nace [EP-003 · HU-011](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-011-el-inventario-de-funcionalidades/HU-011-el-inventario-de-funcionalidades.md) con tres CA: el molde `plantillas/inventario-funcionalidades.md` (generalizado del caso semilla de `shopnest-mesa`, nacido para madurar hasta manual), la regla `F26` del capítulo `02` (sin inventario aprobado por el usuario no se derivan épicas — MAYOR) y el veredicto escrito sobre si la conducta del `01` ya cubría preguntar el alcance.
- **Por qué importa:** Es la clase de error que costó 21 HU sobre un alcance asumido; la puerta lo corta en la estación correcta.
- **Qué lo soluciona:** La fase [A-EP-003-HU-011](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-011-el-inventario-de-funcionalidades/A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas/plan_trabajo.md) con plan y pruebas escritos; los oráculos son el caso semilla y el caso histórico del mismo proyecto.
- **Qué se decidió:** El usuario aprobó HU-011 y sus planes («si») y la fase cerró en Cumple: nacen `02·F26` (con checklist 20/20 y las tres preguntas de `M19` respondidas: sin validador todavía) y el molde `plantillas/inventario-funcionalidades.md`; versión 29.0.0 (MAYOR); pendiente 74 en `hecho/` con aviso a los 9 instalados. El veredicto de conducta quedó escrito: `C4`/`C7`/`C17`/`C21` no cubrían el alcance asumido y la brecha la cierra `F26`, sin extender el `01`.
- **Estado:** resuelto acá
- **Responde a:** pendiente 74
- **Dispara:** EP-003 · HU-011 (ya escrita)
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md](../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md), la entrada 29.0.0 del CHANGELOG y la fase A de HU-011 cerrada
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** — (sigue el 75 por su orden: primero la estructura de `interfaz/`, después el registro; y el commit de esta ronda, que autoriza el usuario)

---

También hubo consulta: el usuario preguntó qué guardan `historico-chat/memory/` (las preferencias del usuario como recuerdos versionados en el repo, con el almacén local de la herramienta vacío, `01·C19`) y `historico-chat/trazas/` (la traza técnica por sesión que produce `validar.py traza`: cada herramienta ejecutada con hora, duración y estado). Las dos respuestas salieron de leer lo que ya está escrito en [memory.md](../../memory/memory.md) y en [trazas/README.md](../../trazas/README.md); no se decidió ni se cambió nada.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ no quedan abiertos |
| Toda historia disparada está escrita en su épica | ☑ no se disparó ninguna |
| Lo que se hizo está aprobado y guardado | ☐ aprobado y escrito; falta el commit de la ronda de la guía, que autoriza el usuario |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: resumen sin hallazgos -->

<!-- aviso: falta decir si la sesión se puede cerrar -->
