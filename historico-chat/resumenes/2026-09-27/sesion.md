# 2026-09-27 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-09-27-sesion.md](../../2026-09-27-sesion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** la pregunta del usuario por la regla del español colombiano.

---

## Hallazgos de esta sesión

### H-1 · La norma del español de Colombia no tiene regla

- **Qué pasó:** `00·ID10` fija la variedad, la persona y la forma verbal. La ortografía, el léxico, la gramática y la redacción colombianas no las exige ninguna regla, y la línea 135 de `marcadores-de-ia.md` sigue diciendo que la regla «no existe».
- **Qué se decidió:** el usuario pidió una regla que las cubra todas y que extienda `00·ID8`. El borrador de `00·ID12` quedó acordado.
- **Dónde queda:** anotado en el [pendiente 96](../../../pendientes/96-la-norma-del-espanol-de-colombia-no-tiene-regla.md). La HU se crea al aprobarse.

### H-2 · El andamio obliga a crear la HU antes que el pendiente

- **Qué pasó:** `andamio.py pendiente` falla si la historia no existe. El agente creó un esqueleto de HU-038 para poder crear el pendiente, y el usuario lo corrigió: el orden es hallazgo → pendiente → HU (hija de una épica) → fase.
- **Qué se decidió:** se quitó el esqueleto de HU-038. El orden completo no está escrito en ninguna regla, y eso también entra al pendiente.
- **Dónde queda:** anotado en el [pendiente 97](../../../pendientes/97-el-andamio-exige-la-historia-antes-que-el-pendiente.md), y en la señal `S-126`.

### H-3 · Ninguna regla exige quedarse en el asunto

- **Qué pasó:** el pendiente 96 llevaba una frase que no aportaba nada. El agente citó `00·ID9`, y el usuario mostró que esa regla exige extensión, no foco.
- **Dónde queda:** anotado en el [pendiente 95](../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md), que el usuario aprobó y bajó a [HU-038](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md). Borrador de `00·ID11` acordado.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ — 95, 96 y 97 |
| Toda historia disparada está escrita en su épica | ☑ — HU-038 en EP-001 |
| Lo que se hizo está aprobado y guardado | ☐ — falta el commit |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
