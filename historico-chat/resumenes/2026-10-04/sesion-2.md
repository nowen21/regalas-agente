# 2026-10-04 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-04-sesion-2.md](../../2026-10-04-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · Nadie ve cuántos tokens se gastan ni puede ajustar las reglas sin tocar código

| Campo | Valor |
|---|---|
| Qué pasó | El usuario pidió ver cuántos tokens se gastan, dónde y en vivo, en todos los proyectos, para saber qué se puede pasar a un programa. Los datos existen: Claude Code anota cada llamada en los `.jsonl` de la sesión y puede mandarla por telemetría; en una sesión medida hubo 1012 llamadas y unos 450 000 tokens releídos por llamada. Pidió además administrar desde Cimiento qué tan rígida es cada regla en cada proyecto, porque hoy cada ajuste es un cambio de código |
| Por qué importa | Lo que más gasta es el contexto que se relee en cada llamada, sobre todo lo que agregan los enganches; sin medirlo no se sabe qué automatizar primero. Y una regla fija en el código puede bloquear a Cimiento para corregirse, como pasó el 2026-10-04 |
| Pendiente | [Pendiente 119: nadie ve cuántos tokens se gastan ni puede ajustar las reglas sin tocar código](pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/pendiente.md) |

### H-2 · Un análisis abierto en una sesión bloqueaba a todas las demás

| Campo | Valor |
|---|---|
| Qué pasó | El estado del análisis prendido era un solo archivo para todo el repositorio, y un análisis aprobado con HU por construir contaba como abierto. El 116 bloqueaba el 119 durante días, y para cambiar esa regla hacía falta un análisis que tampoco se podía abrir |
| Por qué importa | Cimiento tiene que poder corregir sus propias reglas; la rigidez es para los proyectos que heredan, no para la base (lo dijo el usuario) |
| Lo corregido | Con «Apruebo» y «Corrija»: `AnalisisEnCurso` guarda un estado por sesión en `historico-chat/.estado/analisis-en-curso/`; solo bloquea otro análisis sin aprobar en la misma sesión, o el mismo pendiente en otra. `hook_analisis.py`, `hook_historico.py` y `hook_acuerdos.py` pasan a la clase de Cimiento con su sesión. El freno deja corregir con «Corrija» también `proyectos/cimiento/core/`. Pruebas nuevas en `core/enganches/tests_analisis_en_curso.py`; `test_cp005` cambia a la regla nueva |
| Falta | `hook_antes.py` sigue con `validadores/freno.py`, que solo lee el archivo único: no distingue sesiones hasta que se conecte a la clase (fila 21 del análisis 116) |
---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☐ |
| Todo pendiente enlazado existe | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
