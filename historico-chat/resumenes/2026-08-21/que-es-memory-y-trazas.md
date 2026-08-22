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
- **Qué lo soluciona:** La dirección quedó anotada con sus palabras literales en [prompts/la-administracion-de-proyectos-desde-cimiento.md](../../../prompts/la-administracion-de-proyectos-desde-cimiento.md) y como [pendiente 75](../../../pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md) (P3: falta la decisión de diseño de qué es la «interfaz»). El 73 bajó por la cadena: nace [HU-014 — La guía de entrada del estándar](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-014-la-guia-de-entrada-del-estandar/HU-014-la-guia-de-entrada-del-estandar.md) con su fase A, plan y pruebas escritos, esperando la aprobación del usuario (puertas 4 y 7).
- **Qué se decidió:** El usuario aprobó HU-014 y sus planes («si») y la fase se ejecutó y cerró en Cumple: nace `base/guia-de-entrada.md` (heredable; al arranque solo le suma su línea de índice de 102 bytes, desvío declarado en el resultado), versión 28.2.0, pendiente 73 en `hecho/` con aviso a los 9 instalados y el adjunto borrado como ordenaba. Además el usuario decidió la interfaz del 75: es `interfaz/` (el visor Django) y debe adoptar la estructura de `plantillas/estructura-proyecto-django.md`; la brecha quedó medida en el pendiente, que sube a P2.
- **Estado:** resuelto acá (el 74 y el 75 siguen en el backlog, con su orden acordado: 74, luego 75a y 75b)
- **Responde a:** pendientes 73 y 75
- **Dispara:** EP-001 · HU-014 (ya escrita con sus dos CA)
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/la-guia-de-entrada-es-del-estandar.md](../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md), la entrada 28.2.0 del CHANGELOG, la fase A de HU-014 cerrada, y el [pendiente 75](../../../pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md) con la decisión de diseño escrita
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** — (siguen el 74 y el 75, por su orden; y el commit de esta ronda, que autoriza el usuario)

### H-3 · El 74 bajó por la cadena: el inventario de funcionalidades como puerta de las épicas

- **Qué pasó:** Publicado el 73 (commit `98468b6`, tras dos tropiezos del trinquete de marcas resueltos), se bajó el 74 según el orden acordado. Nace [EP-003 · HU-011](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-011-el-inventario-de-funcionalidades/HU-011-el-inventario-de-funcionalidades.md) con tres CA: el molde `plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md` (generalizado del caso semilla de `shopnest-mesa`, nacido para madurar hasta manual), la regla `F26` del capítulo `02` (sin inventario aprobado por el usuario no se derivan épicas — MAYOR) y el veredicto escrito sobre si la conducta del `01` ya cubría preguntar el alcance.
- **Por qué importa:** Es la clase de error que costó 21 HU sobre un alcance asumido; la puerta lo corta en la estación correcta.
- **Qué lo soluciona:** La fase [A-EP-003-HU-011](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-011-el-inventario-de-funcionalidades/A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas/plan_trabajo.md) con plan y pruebas escritos; los oráculos son el caso semilla y el caso histórico del mismo proyecto.
- **Qué se decidió:** El usuario aprobó HU-011 y sus planes («si») y la fase cerró en Cumple: nacen `02·F26` (con checklist 20/20 y las tres preguntas de `M19` respondidas: sin validador todavía) y el molde `plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`; versión 29.0.0 (MAYOR); pendiente 74 en `hecho/` con aviso a los 9 instalados. El veredicto de conducta quedó escrito: `C4`/`C7`/`C17`/`C21` no cubrían el alcance asumido y la brecha la cierra `F26`, sin extender el `01`.
- **Estado:** resuelto acá
- **Responde a:** pendiente 74
- **Dispara:** EP-003 · HU-011 (ya escrita)
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md](../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md), la entrada 29.0.0 del CHANGELOG y la fase A de HU-011 cerrada
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** — (sigue el 75 por su orden: primero la estructura de `interfaz/`, después el registro; y el commit de esta ronda, que autoriza el usuario)

### H-4 · El ciclo de vida gana su carpeta de moldes, su lista de entregables y dos correcciones de cómo trabajar

- **Qué pasó:** El usuario ordenó `plantillas/ciclo-vida-proyectos/`. El agente tropezó dos veces (abrió un pendiente en vez de resolver; luego ejecutó una opción que el usuario no había elegido) y las dos correcciones quedaron en el recuerdo [la-orden-se-resuelve-de-una](../../memory/la-orden-se-resuelve-de-una.md). Con el análisis hecho juntos, el usuario decidió: **el ciclo no hace excepciones** (todos los entregables existen en todo proyecto; la envergadura ajusta profundidad; sin materia se declara «No aplica porque...»), y triple A para la carpeta: solo el ciclo, moldes numerados por estación, MAYOR sin redirecciones ni fantasmas.
- **Por qué importa:** Abrir una carpeta y ver el ciclo del 01 al 11 es la cara tangible de la disciplina; y la lista canónica de entregables (IEEE/ISO) fija cuánto falta para el expediente completo que al final «solo genera los .docx».
- **Qué lo soluciona:** Ejecutado el frente 1: los 11 moldes movidos y numerados (la carpeta `planes/` desaparece: son las estaciones 07 a 09), ~20 referencias de código y 137 documentos al día, README del ciclo, mapa del sitio, versión 30.0.0 (MAYOR). De paso el trinquete de marcas aprendió a seguir renombres (`git mv` ponía línea base cero y contaba como nuevas las marcas viejas) con sus 2 pruebas. La lista de entregables quedó en [notas/entregables-del-ciclo-de-vida.md](../../../notas/entregables-del-ciclo-de-vida.md) con el cruce contra Cimiento y la decisión de sin-excepciones.
- **Qué se decidió:** Lo de arriba, todo del usuario. Quedan los frentes 2 (13 moldes faltantes) y 3 (generador `.docx` y mapa de completitud, conectado al pendiente 75).
- **Estado:** resuelto acá (frentes 1 y 2; el 3, el generador de vistas y `.docx`, queda dimensionado en la nota y conecta con el pendiente 75)
- **Responde a:** la orden del usuario del 2026-08-21
- **Dispara:** — (los frentes 2 y 3 se bajarán cuando el usuario los ordene; la nota los dimensiona)
- **Orden de resolución:** —
- **Dónde queda:** [plantillas/ciclo-vida-proyectos/README.md/](../../../plantillas/ciclo-vida-proyectos/README.md), la entrada 30.0.0 del CHANGELOG, la nota de entregables y el recuerdo de las correcciones
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** del frente 3 quedó hecha su base el mismo día: `validar.py expediente` (v30.2.0, 6 pruebas), el mapa de completitud por proyecto — estrenó midiendo `shopnest-mesa`: 3 de 13 entregables. Falta el generador de vistas consolidadas y el `.docx`, cuya casa natural es la interfaz del pendiente 75 (la dependencia python-docx vive allá, no en validadores/). El frente 2 cerró también hoy: moldes 12 a 22 (v30.1.0)

---

### H-5 · El pendiente 75 cerró el día en que nació: los proyectos se administran desde Cimiento

- **Qué pasó:** Ejecutado el 75 completo. **(a)** `interfaz/` adoptó la estructura estándar Django: `requirements/` con lock, `config/settings/` base+local, `.env.example`, módulo completo, y los terceros fuera del repo (`descargar_estaticos.py` los trae pineados por huella SHA-256, verificados 8 de 8 contra el CDN antes de borrar nada; sigue sin internet tras instalar). **(b)** Nace `interfaz/proyectos/`: el registro como datos con pantallas (registrar, editar, baja sin borrar historia, **medir** el expediente con `validar.py expediente`), 7 pruebas en verde; `plantillas/proyectos.md` pasó a generarse desde el registro, con los 10 proyectos reales e ida y vuelta verificada.
- **Por qué importa:** Es la dirección que el usuario fijó en H-2, cumplida: Cimiento administra y mide sus proyectos desde la aplicación, no desde un archivo a mano.
- **Qué lo soluciona:** Hecho; versión 30.3.0. Dos tropiezos del camino, ya corregidos y con prueba: el filtro del encabezado se comía a «Proyecto de grado» al importar, y un `exportar` corrió antes de verificar el `importar` y vació el `.md` real (se reconstruyó completo desde la transcripción de esta sesión, que lo tenía literal — el histórico pagó su costo hoy).
- **Qué se decidió:** La deuda declarada en el cierre: el instalador aún anota altas en el `.md` generado y la interfaz las importa; escribirlas directo al registro es mejora futura. Y dos decisiones más del usuario al revisar: la interfaz debía cumplir la plantilla Django **completa** (encontró cinco huecos: paquete, `templates/`, `static/vendor`, `asgi`, `.venv`; cerrados el mismo día) y **la base de Cimiento es MariaDB en el puerto 3307** (hecho el 2026-08-22 a primera hora: base `cimiento`, credenciales solo en `.env`, 10 proyectos migrados, pruebas contra MariaDB; v30.4.0).
- **Estado:** resuelto acá
- **Responde a:** pendiente 75 (H-2 de esta sesión)
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md](../../../pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md), la entrada 30.3.0 del CHANGELOG, `interfaz/proyectos/` y la pantalla Proyectos del visor
- **Nace en:** 2026-08-21 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-21 · que-es-memory-y-trazas
- **Con qué se retoma:** — (quedan en el backlog: el 59 que espera tus respuestas, los arreglos chicos 33/71/72, el 19 y el 48 por tandas; y el generador de vistas y `.docx`, ya con casa: la interfaz)

---

### H-6 · El registro de proyectos se vaciaba solo, y eran nuestras propias pruebas

- **Qué pasó:** Otra sesión (proyecto `gestion de servicios tecnologicos`) reportó el pendiente 76: `plantillas/proyectos.md` quedaba vacío de la nada y su checklist reprobaba «registro» en cada mensaje. El usuario pidió revisarlo. La causa estaba en casa: las pruebas de las vistas de la interfaz llamaban `exportar()` sin redirigir el `.md`, y volcaban la base de pruebas (vacía tras una baja) sobre el archivo real — tres veces, coincidiendo con tres corridas de `manage.py test`. Al corregir, las pruebas del instalador hicieron lo mismo por otro camino (el alta nueva vía `manage.py registrar` metió dos «proyecto de prueba» en MariaDB); se borraron y se puso el guardia.
- **Por qué importa:** Una prueba con efectos sobre un archivo real es un proceso que corre cuando nadie mira; y un exportador que escribe cero filas sin mirar qué había convierte cualquier base equivocada en pérdida de datos. Lo detectó un proyecto instalado: el estándar se vigiló desde afuera.
- **Qué lo soluciona:** Hecho (v30.5.0, 10 pruebas de la interfaz en verde, la base real con sus 10 proyectos después de correr ambas suites): ninguna prueba toca el registro real; `exportar()` se niega a vaciar (`RegistroVacio`) y las pantallas lo dicen; el instalador da de alta con `manage.py registrar` solo contra el registro real (cierra la deuda del 75). Señal S-019.
- **Qué se decidió:** El checklist sigue leyendo el `.md`, que ahora es confiable: lo genera el registro, nada lo vacía y el instalador no lo escribe a mano.
- **Estado:** resuelto acá
- **Responde a:** pendiente 76 (secuela del 75)
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/hecho/el-registro-no-se-vacia-y-el-alta-entra-a-cimiento.md](../../../pendientes/hecho/el-registro-no-se-vacia-y-el-alta-entra-a-cimiento.md), la entrada 30.5.0 del CHANGELOG y la señal S-019
- **Nace en:** 2026-08-22 · que-es-memory-y-trazas
- **Cerrado en:** 2026-08-22 · que-es-memory-y-trazas
- **Con qué se retoma:** — (el commit de esta ronda, que autoriza el usuario)

---

También hubo consulta: el usuario preguntó qué guardan `historico-chat/memory/` (las preferencias del usuario como recuerdos versionados en el repo, con el almacén local de la herramienta vacío, `01·C19`) y `historico-chat/trazas/` (la traza técnica por sesión que produce `validar.py traza`: cada herramienta ejecutada con hora, duración y estado). Las dos respuestas salieron de leer lo que ya está escrito en [historico-chat/memory/memory.md](../../memory/memory.md) y en [historico-chat/trazas/README.md](../../trazas/README.md); no se decidió ni se cambió nada.

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
