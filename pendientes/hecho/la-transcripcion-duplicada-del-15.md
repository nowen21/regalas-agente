# Pendiente · La transcripción se escribió dos veces, y con horas inventadas

**Estado:** **cerrado** el 2026-08-18. Anotado el 2026-08-15 · nace de la sesión [historico-chat/2026-08-15-la-plantilla-del-resultado-de-pruebas.md](../../historico-chat/2026-08-15-la-plantilla-del-resultado-de-pruebas.md).

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-001 — Transcripción de la sesión](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md) — lo que queda por limpiar es una transcripción, que es lo que esa historia gobierna |

## El problema

Dos defectos en el mismo archivo, los dos del agente.

**1. La transcripción quedó duplicada.** [`validadores/hook_historico.py`](../../validadores/hook_historico.py) ya escribe cada mensaje del usuario y cada respuesta del agente, con la hora leída del reloj y su marca `<!-- agente: … -->`. El agente la escribió otra vez a mano encima, con `cat >>`. Resultado en ese archivo: **61 encabezados de usuario para unos 30 mensajes**, numeración pisada —hay dos «5», dos «6», dos «9»— y respuestas del agente en dos versiones, la que dio y la que resumió después.

**2. Las horas se estimaron.** El [`CLAUDE.md`](../../CLAUDE.md) exige `AAAA-MM-DD HH:MM:SS` leído del reloj del sistema y dice que una hora no registrada se escribe `hora no registrada`, sin estimarla. El agente leyó el reloj dos veces al arrancar y de ahí en adelante fue inventando horas que avanzaban solas: la última escrita a mano decía 11:58 cuando el reloj marcaba 21:41.

**3. Al intentar arreglarlo se perdieron datos.** Un `git checkout --` sobre el archivo descartó lo que el enganche había escrito después del último commit: las horas reales de los seis últimos mensajes. El texto se recuperó literal; las horas no, y quedaron en `hora no registrada`.

## Por qué pasó

El `CLAUDE.md` de este repositorio manda escribir la transcripción a mano —«se actualiza después de cada intercambio»— y no dice que un programa ya lo hace. El agente obedeció la instrucción escrita sin comprobar si el enganche estaba haciendo lo mismo.

## Qué falta

**1. Limpiar el archivo del 2026-08-15.** ✅ **Hecho el 2026-08-18**, pero **no como decía este punto**.

Decía quitar todo lo que no llevara la marca del enganche. Al medirlo, **eso borraba dieciséis mensajes reales del usuario**: de los 25 bloques sin marca, solo 9 estaban repetidos palabra por palabra en otro que sí la lleva. Los otros 16 son únicos — el enganche no los escribió, o los escribió sin marca.

Se quitaron los **9 duplicados literales** y el archivo pasó de 57 bloques a 48, renumerados. Arriba quedó una nota que dice qué se hizo y que **las horas de ese archivo no se pueden leer en orden**: las del enganche son del reloj, las otras son estimaciones.

> **La instrucción escrita destruía contenido, y solo se vio al medir.** Un criterio que suena limpio —«borrar lo que no lleva la marca»— puede estar apoyado en que la marca esté siempre, y acá faltaba en la mitad.

**2. Que el `CLAUDE.md` deje de pedir lo que el programa ya hace.** ✅ **Hecho el 2026-08-16.** Su sección 1 describía el trabajo a mano como si nadie lo automatizara. Ahora dice que lo escribe el enganche y que el agente no lo toca.

Eran **dos** archivos, no uno: el [`CLAUDE.md`](../../CLAUDE.md) y el [`historico-chat/README.md`](../../historico-chat/README.md), que repetía la misma orden y es a donde el primero manda para el formato. Arreglar uno solo dejaba la orden viva.

La redacción no hubo que inventarla: [`plantillas/CLAUDE.md.plantilla`](../../plantillas/CLAUDE.md.plantilla) ya decía *«La escribe el programa, no el agente»* desde que se automatizó el histórico. Se actualizó la plantilla que viaja a los proyectos y no la del repo que la escribe, así que **el defecto era solo de acá**: un proyecto instalado leía la versión buena.

**3. Comprobar si le pasa a otras sesiones.** ✅ **Hecho el 2026-08-16.** Al escribir los resúmenes de las sesiones viejas aparecieron **cuatro copias a mano** más, todas sin la marca `<!-- sesion: … -->`:

| Copia borrada | Repetía a |
|---|---|
| `2026-08-06-sesion-7.md` | [no se puede transcribir audio](../../historico-chat/2026-08-06-no-se-puede-transcribir-audio.md) |
| `2026-08-06-sesion-9.md` | [la clase del diplomado](../../historico-chat/2026-08-06-la-clase-del-diplomado-en-el-repositorio.md) — con la hora del usuario y la del agente idénticas al segundo en los 21 intercambios |
| `2026-08-07-sesion-9.md` | [granularidad de la fase](../../historico-chat/2026-08-07-granularidad-de-la-fase.md) |
| `2026-08-07-analisis-cumplimiento-reglas.md` | [el checklist de la regla](../../historico-chat/2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md), sus primeros doce intercambios |

Las cuatro se borraron por instrucción del usuario y siguen en el historial de git. Una quinta la había borrado el propio agente el 2026-08-07, en caliente. **Se perdió una cosa al hacerlo**: la copia del diplomado describía cada diapositiva (`[imagen: …]`) y la que quedó no, porque las imágenes llegaron pegadas al chat. Está en el historial.

**Sigue faltando solo el punto 1:** limpiar la transcripción del 2026-08-15, con 61 encabezados de usuario para unos 30 mensajes. Ya se puede hacer sin que se vuelva a ensuciar, que era la dependencia.

## El límite

No se toca lo que el enganche escribió: es el registro con hora real. Lo que se quita es la copia a mano.

**Va después de los pendientes [27](el-veredicto-de-la-fase-a-de-hu-010.md) y [28](un-solo-veredicto-por-fase.md):** el archivo se puede leer igual, aunque tenga el doble de encabezados.

---

# Cómo cerró el punto 1 — 2026-08-17

**La transcripción del 2026-08-15 quedó limpia**, y con un resultado distinto del que este pendiente esperaba.

## Cómo se distinguían

El molde del enganche se leyó de la **otra** sesión del mismo día, que estaba limpia:

```
### N · Usuario — hora
> lo que dijo el usuario

**Agente** — hora
<!-- agente: uuid -->
```

El enganche **nunca** escribe un encabezado `### N · Agente`. Los 38 que había los escribió el agente, con su copia del texto y con horas estimadas. Eso da una regla que se comprueba, no que se adivina.

## Lo que se hizo, y lo que **no**

| | Cuántos |
|---|---|
| Copias a mano quitadas, porque el enganche traía la suya | 22 |
| Mensajes de usuario repetidos, con hora inventada | 5 |
| **Respuestas conservadas que solo existían en la copia a mano** | **16** |

**Las 16 no se borraron, y ahí está el hallazgo.** Este pendiente daba por hecho que la copia a mano era pura duplicación —«61 encabezados de usuario para unos 30 mensajes»—. No lo era: de 63 mensajes de usuario, el enganche solo alcanzó a registrar 32 respuestas. Las otras 16 existen **únicamente** en lo que escribió el agente.

Borrarlas habría dejado una transcripción con 63 preguntas y 32 respuestas, y habría repetido el error que este mismo pendiente documenta unas líneas más arriba: al borrar la copia del diplomado se perdió con ella la descripción de las diapositivas, y solo se supo después.

Se quedan, pero **dejan de mentir sobre su hora**:

```
**Agente** — reconstruido a mano, sin hora del reloj
<!-- sin marca del enganche: la hora original era una estimación (2026-08-15 09:28:20) -->
```

## Cómo quedó

| | Antes | Ahora |
|---|---|---|
| Líneas | 1101 | 857 |
| Encabezados `### N · Agente` | 38 | **0** |
| Mensajes de usuario | 68, con números repetidos | **63**, correlativos |
| Respuestas con marca del enganche | 32 | 32 |
| Respuestas marcadas como reconstruidas | 0 | 16 |

**Con los tres puntos hechos, el pendiente cierra.**

## Lo que se supo

**Una transcripción escrita dos veces no se limpia borrando una de las dos.** Las dos copias eran incompletas por lados distintos: el enganche tenía las horas buenas y le faltaban 16 respuestas; la copia a mano las tenía todas y con las horas inventadas. Lo que sirve es quedarse con lo verificable de cada una y **marcar cuál es cuál** — no elegir una y tirar la otra.
