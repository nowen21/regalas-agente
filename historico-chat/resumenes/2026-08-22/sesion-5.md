# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-sesion-5.md](../../2026-08-22-sesion-5.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «...»

---

## Hallazgos de esta sesión

### El ciclo de vida ya estaba documentado; lo que faltaba era la puerta de entrada

- **Qué pasó:** el usuario preguntó qué va en cada una de las siete etapas del ciclo de vida listadas en `cvds/README.md`, que estaban enumeradas y vacías.
- **Por qué importa:** el repo ya tiene los 22 moldes del ciclo en `plantillas/ciclo-vida-proyectos/`, pero entrar por ahí exige saber de antemano que existen. Llenar `cvds/` copiando lo que ya está escrito habría creado dos versiones que divergen (`M12`).
- **Qué se decidió:** `cvds/README.md` dice **qué va en cada etapa y qué pregunta responde**, y **enlaza** el molde que la escribe en vez de repetirlo. Queda como documento aparte del estándar: no toca `base/` ni `plantillas/`, así que no versiona.
- **Dónde queda:** [cvds/README.md](../../../cvds/README.md).

### El agente metió anglicismos en un documento de un repo que está todo en español

- **Qué pasó:** el agente tituló el documento «(SDLC)» y dejó pasar «WBS», «ROI» y «stakeholders». El usuario lo cortó con «recuerde la regla de español».
- **Por qué importa:** es [`01·C8`](../../../base/01-conducta.md), que ya estaba cargada al abrir la sesión. La carpeta misma se llama `cvds`, que es el acrónimo en español, y el agente le puso encima el inglés, así que el incumplimiento estaba en el título, en la primera línea del archivo.
- **Qué se decidió:** el agente empezó por **borrar** las siglas y traducirlas, y el usuario lo corrigió: «las siglas no las quite, simplemente agregue una aclaración». La sigla se queda y al lado va qué significa en español: SDLC, ROI, WBS y *stakeholders* siguen ahí, glosados. El título sí quedó en CVDS, que es como se llama la carpeta. *Scrum* no se toca: es el nombre propio de un marco.
- **Dónde queda:** [cvds/README.md](../../../cvds/README.md) y este mismo resumen, que también decía «SDLC».

### La raya larga se coló diez veces en el mismo archivo, y el validador ya sabía contarla

- **Qué pasó:** el usuario escribió «esto no va: —». El archivo tenía 12 rayas largas y 15 puntos medios en prosa: 27 marcas de [`00·ID8`](../../../base/00-identidad-y-rol/marcadores-de-ia.md) que `validadores/marcas.py` contaba desde antes de que el usuario las viera.
- **Por qué importa:** el agente escribió el archivo, lo revisó dos veces por otras razones y nunca corrió el validador que este mismo repo tiene para eso. La marca no se detectó leyendo: se detectó porque el usuario la señaló.
- **Qué se decidió:** correr `python validadores/marcas.py --raiz <carpeta>` **antes** de dar por entregado un documento, no después de que lo devuelvan. El archivo quedó en 0 marcas. De paso cayó un «no es una línea: es un anillo», que es la construcción «No es X, es Y» de la sección 1 del anexo.
- **Dónde queda:** [cvds/README.md](../../../cvds/README.md), 27 marcas a 0.

### El molde de factibilidad evalúa tres frentes; la práctica evalúa cuatro, y no son los mismos tres

- **Qué pasó:** el usuario agregó a `cvds/README.md` los doce documentos de la etapa de planificación. Al mapearlos contra los moldes del estándar apareció el choque: el estudio de viabilidad de la etapa evalúa **técnica, económica, operativa y legal**, y [`12-estudio-factibilidad.md`](../../../plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md) pide **técnica, económica y de plazos**. Faltan operativa y legal; sobra un frente que la lista no nombra.
- **Por qué importa:** la viabilidad **legal** es la que pregunta por normativas, licencias y protección de datos. Un proyecto que la salta se entera del problema cuando ya está construido, que es cuando cuesta. La **operativa** pregunta si los usuarios lo van a adoptar, y ese es el frente por el que se muere un sistema técnicamente correcto.
- **Qué se decidió:** todavía nada. Tocar `plantillas/` es cambio del estándar: pide la cadena de `02·F0`, entrada en `CHANGELOG.md` y subir `VERSION` (`M10`), así que no cabe en el trabajo de dar forma a un README.
- **Dónde queda:** por decidir si se abre pendiente. El choque está descrito acá y en la tabla de [cvds/README.md](../../../cvds/README.md), que ya dice qué documentos **no tienen molde propio**: WBS, presupuesto, plan de calidad y estimación de esfuerzo.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☐ |
| Todo hallazgo abierto tiene su pendiente creado | ☐ |
| Toda historia disparada está escrita en su épica | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: resumen sin hallazgos -->
