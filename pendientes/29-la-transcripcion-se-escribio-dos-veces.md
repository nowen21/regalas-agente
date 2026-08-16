# Pendiente · La transcripción se escribió dos veces, y con horas inventadas

**Estado:** abierto · anotado 2026-08-15 · nace de la sesión [historico-chat/2026-08-15-la-plantilla-del-resultado-de-pruebas.md](../historico-chat/2026-08-15-la-plantilla-del-resultado-de-pruebas.md).

## El problema

Dos defectos en el mismo archivo, los dos del agente.

**1. La transcripción quedó duplicada.** [`validadores/hook_historico.py`](../validadores/hook_historico.py) ya escribe cada mensaje del usuario y cada respuesta del agente, con la hora leída del reloj y su marca `<!-- agente: … -->`. El agente la escribió otra vez a mano encima, con `cat >>`. Resultado en ese archivo: **61 encabezados de usuario para unos 30 mensajes**, numeración pisada —hay dos «5», dos «6», dos «9»— y respuestas del agente en dos versiones, la que dio y la que resumió después.

**2. Las horas se estimaron.** El [`CLAUDE.md`](../CLAUDE.md) exige `AAAA-MM-DD HH:MM:SS` leído del reloj del sistema y dice que una hora no registrada se escribe `hora no registrada`, sin estimarla. El agente leyó el reloj dos veces al arrancar y de ahí en adelante fue inventando horas que avanzaban solas: la última escrita a mano decía 11:58 cuando el reloj marcaba 21:41.

**3. Al intentar arreglarlo se perdieron datos.** Un `git checkout --` sobre el archivo descartó lo que el enganche había escrito después del último commit: las horas reales de los seis últimos mensajes. El texto se recuperó literal; las horas no, y quedaron en `hora no registrada`.

## Por qué pasó

El `CLAUDE.md` de este repositorio manda escribir la transcripción a mano —«se actualiza después de cada intercambio»— y no dice que un programa ya lo hace. El agente obedeció la instrucción escrita sin comprobar si el enganche estaba haciendo lo mismo.

## Qué falta

**1. Limpiar el archivo del 2026-08-15.** Quitar los bloques que escribió el agente a mano y dejar los del enganche, que son los que traen la hora real. Se distinguen: los del enganche llevan `<!-- agente: … -->`. Después renumerar.

**2. Que el `CLAUDE.md` deje de pedir lo que el programa ya hace.** Hoy su sección 1 describe el trabajo a mano como si nadie lo automatizara. Tiene que decir que el enganche escribe la transcripción y que el agente **no** la escribe: solo se asegura de que exista.

**3. Comprobar si le pasa a otras sesiones.** ✅ **Hecho el 2026-08-16.** Al escribir los resúmenes de las sesiones viejas aparecieron **cuatro copias a mano** más, todas sin la marca `<!-- sesion: … -->`:

| Copia borrada | Repetía a |
|---|---|
| `2026-08-06-sesion-7.md` | [no se puede transcribir audio](../historico-chat/2026-08-06-no-se-puede-transcribir-audio.md) |
| `2026-08-06-sesion-9.md` | [la clase del diplomado](../historico-chat/2026-08-06-la-clase-del-diplomado-en-el-repositorio.md) — con la hora del usuario y la del agente idénticas al segundo en los 21 intercambios |
| `2026-08-07-sesion-9.md` | [granularidad de la fase](../historico-chat/2026-08-07-granularidad-de-la-fase.md) |
| `2026-08-07-analisis-cumplimiento-reglas.md` | [el checklist de la regla](../historico-chat/2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md), sus primeros doce intercambios |

Las cuatro se borraron por instrucción del usuario y siguen en el historial de git. Una quinta la había borrado el propio agente el 2026-08-07, en caliente. **Se perdió una cosa al hacerlo**: la copia del diplomado describía cada diapositiva (`[imagen: …]`) y la que quedó no, porque las imágenes llegaron pegadas al chat. Está en el historial.

Sigue faltando el punto 1: la transcripción del 2026-08-15, con 61 encabezados de usuario para unos 30 mensajes.

## El límite

No se toca lo que el enganche escribió: es el registro con hora real. Lo que se quita es la copia a mano.

**Va después de los pendientes [27](27-la-fase-a-de-hu-010-cerro-sin-cumplir.md) y [28](28-el-veredicto-de-la-fase-vive-en-dos-sitios.md):** el archivo se puede leer igual, aunque tenga el doble de encabezados.
