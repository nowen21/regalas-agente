# 2026-10-04 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-04-optimizar-el-codigo-de-cimiento.md](../../2026-10-04-optimizar-el-codigo-de-cimiento.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | Pedido del usuario: optimizar el código de Cimiento |

---

## Hallazgos de esta sesión

El punto de partida fue el inventario: Cimiento tiene 663 archivos `.py` propios, 208 en `historico-chat/scripts/`, 217 en `plataforma/`, 87 en `validadores/`, 89 de pruebas de los validadores, 21 en `adaptadores/` y 42 en el resto. `interfaz/.venv` no cuenta, porque es lo instalado.

### H-3 · El código de Cimiento se repite en vez de reusarse

| Campo | Valor |
|---|---|
| Qué pasó | El inventario encontró la misma función copiada en muchos archivos (`_leer` en 13, `raiz_pedida` en 10, `dicho` en 9, `_entrada` en 8, `_git` en 6) y dos formas distintas de saber si una ruta queda dentro del proyecto. Cada vez que hizo falta algo se creó un archivo nuevo sin buscar si eso ya existía |
| Por qué importa | Un arreglo llega a una sola copia: el commit `1295614` corrigió `/c/...` en `freno.py` y `rutas_fuera.py` siguió sin entenderlo |
| Pendiente | [Pendiente 116: el código de Cimiento se repite en vez de reusarse](pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/pendiente.md) |

### H-4 · Nada comprueba `07·Q4` al crear una función

| Campo | Valor |
|---|---|
| Qué pasó | Ningún validador revisa si una función nueva ya existe en otro archivo, y por eso nacen las copias del H-3 |
| Por qué importa | Si solo se juntan las copias de hoy, las nuevas siguen apareciendo |
| Pendiente | [Pendiente 117: nada avisa cuando se crea una función que ya existe](pendientes/117-nada-avisa-cuando-se-crea-una-funcion-que-ya-existe/pendiente.md) |

### H-5 · El análisis del pendiente 110 no se cerraba nunca

| Campo | Valor |
|---|---|
| Qué pasó | `validadores/analisis_en_curso.py` juntaba cada HU de la columna «Pasó a» con la primera épica de la celda, y de las rutas de lo hecho «de una y sin fase» armaba `EP-023 HU-012`, que no existe |
| Por qué importa | No dejaba abrir ningún análisis nuevo, tampoco el del pendiente 116 |
| Pendiente | Ninguno: corregido con «Corrija». Lo hecho de una no espera HU y cada HU va con su épica. Prueba: `validadores/tests/test_el_plan_del_analisis_lee_bien_sus_hu.py` |

### H-6 · El freno detuvo el traslado de la plataforma que el usuario ordenó

| Campo | Valor |
|---|---|
| Qué pasó | Con «Hágalo: moverlo acá: C:\Ing. Jose\ia\agente\proyectos», se sacó la historia de `plataforma/` a la rama `plataforma-historia` y se clonó en `proyectos/plataforma/`. El freno detuvo `proyectos/plataforma/` por `02·F8`: no hay fase ni fila del análisis que lo nombre. Además, el clon quedó sin archivos: Windows no admite rutas de más de 260 caracteres y `datos/proyectos/cimiento-el-estandar/traido/...` llega a 273 |
| Por qué importa | Lo que el usuario ordena en el chat no pasa el freno; y la plataforma no se puede abrir en `proyectos/` sin `core.longpaths` |
| Pendiente | [Pendiente 118: el freno detiene lo que el usuario ya autorizó](pendientes/118-el-freno-detiene-lo-que-el-usuario-ya-autorizo/pendiente.md), que scilit reportó por la misma causa |

### H-1 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-04 10:17, el freno detuvo una orden de consola sobre `/tmp/f.txt`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

### H-2 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-04 10:29, el freno detuvo una orden de consola sobre `$f`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

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

<!-- aviso: resumen sin hallazgos -->

<!-- aviso: falta decir si la sesión se puede cerrar -->
