# 2026-09-27 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-09-27-reglas-de-redaccion-y-orden-de-la-cadena.md](../../2026-09-27-reglas-de-redaccion-y-orden-de-la-cadena.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** la pregunta del usuario por la regla del español colombiano.

## Hallazgos de esta sesión

### H-1 · Ninguna regla exige quedarse en el asunto

- **Qué pasó:** un pendiente traía una frase que no le aportaba nada. `00·ID9` y `01·C5` miden extensión, no pertinencia.
- **Dónde queda:** resuelto. Pendiente 95, [HU-038](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md) y la regla [`00·ID11`](../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md), versión 38.1.0.

### H-2 · La norma del español de Colombia no tenía regla

- **Qué pasó:** `00·ID10` fija la variedad, pero no qué es escribirla bien.
- **Dónde queda:** resuelto. Pendiente 96, [HU-039](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-039-el-agente-no-conserva-el-espanol-colombiano/HU-039-el-agente-no-conserva-el-espanol-colombiano.md), la regla [`00·ID12`](../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) y su anexo, versión 38.2.0.

### H-3 · El andamio obligaba a crear la HU antes que el pendiente

- **Qué pasó:** el orden que fijó el usuario es hallazgo, pendiente, HU y fase, y `andamio.py` exigía la HU primero. Ninguna regla escribía ese orden.
- **Dónde queda:** resuelto. Pendiente 97, [HU-022 de EP-005](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-022-andamio-impone-un-orden-de-trabajo-incorrecto/HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md), `--hu` opcional y `02·F23` precisada, versión 38.3.0. Señal `S-126`.

### H-4 · El enganche post-commit marcaba como commiteadas fases recién abiertas

- **Qué pasó:** marcaba la estación 12 de toda fase cuyo cierre estuviera en git, y el andamio crea ese cierre vacío al abrir la fase.
- **Dónde queda:** resuelto en la misma fase de HU-022 (CA-07), a pedido del usuario: el enganche exige que el cierre no sea el molde.

### H-5 · El recordatorio de cada turno no traía las reglas nuevas

- **Qué pasó:** `hook_reglas.py` recordaba `C5`, `ID8`, `ID9` e `ID10`, y no `ID11`.
- **Dónde queda:** resuelto en la fase de HU-039, a pedido del usuario: el recordatorio trae `ID11` e `ID12`.

Además, a pedido del usuario: las 55 plantillas de documento traen el formato del plan de trabajo y una tabla con `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12`, versión 38.3.1.

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ Los cinco |
| Todo hallazgo abierto tiene su pendiente creado | ☑ No queda ninguno abierto |
| Toda historia disparada está escrita en su épica | ☑ HU-038 y HU-039 en EP-001, HU-022 en EP-005, las tres terminadas |
| Lo que se hizo está aprobado y guardado | ☑ En `origin/main`, hasta `e4e8e1c` |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.
