# 2026-10-04 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-04-sesion-2.md](../../2026-10-04-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · El gasto no llega en vivo, lo repetido no se automatiza, y lo que Cimiento hace no siempre se puede deshacer

| Campo | Valor |
|---|---|
| Qué pasó | EP-025 dejó el gasto en la base y en un tablero, pero lo vivo depende de la telemetría y el `.jsonl` se lee al abrir el tablero y una vez al día; el tablero no separa lo automatizable; el cierre de cada fase se hizo con guiones casi iguales; y Cimiento no trae ayuda ni manual. Además, Cimiento crea sin poder deshacer: el andamio creó una HU con el número equivocado y no había cómo quitarla, y el freno, que bloqueó con razón, no ofrecía salida; el usuario tuvo que borrar la carpeta y editar el estado del análisis a mano |
| Por qué importa | Sin ver el gasto en cuanto ocurre y sin separar lo automatizable, no se sabe qué pasar a un programa; y cada acción sin contraria y cada bloqueo sin salida terminan en el usuario tocando archivos, en Cimiento y en todo proyecto que lo herede |
| Versión | 4, según el [análisis 3 del pendiente 119](pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md); la 3 salió del análisis 2 y la 2, del análisis 1, que se construyó en EP-025 |
| Pendiente | [Pendiente 119: el gasto no llega en vivo, lo repetido no se automatiza, y lo que Cimiento hace no siempre se puede deshacer](pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/pendiente.md) |

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
