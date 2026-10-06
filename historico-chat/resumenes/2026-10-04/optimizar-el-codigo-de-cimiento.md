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
| Qué se decidió | Su [análisis 1](pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md) quedó aprobado el 2026-10-05, con todas sus filas hechas. El código vive en `proyectos/cimiento/core/`, con los validadores como clases; en `validadores/` quedan las puertas y los puentes de los enganches. Lo retirado se borró con `validadores/retirar.py`, que deja en texto simple los enlaces que lo nombraban |

### H-4 · Nada comprueba `07·Q4` al crear una función

| Campo | Valor |
|---|---|
| Qué pasó | Ningún validador revisa si una función nueva ya existe en otro archivo, y por eso nacen las copias del H-3 |
| Por qué importa | Si solo se juntan las copias de hoy, las nuevas siguen apareciendo |
| Pendiente | [Pendiente 117: nada avisa cuando se crea una función que ya existe](pendientes/117-nada-avisa-cuando-se-crea-una-funcion-que-ya-existe/pendiente.md) |
| Qué se decidió | Lo trató el análisis 1 del pendiente 116 y quedó hecho con `EP-004` HU-026; para las reglas, `EP-004` HU-027 avisa las parecidas al crear una |

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

### H-7 · Pasar los validadores a clases destapa errores que la paridad copiaba

| Campo | Valor |
|---|---|
| Qué pasó | Al escribir las pruebas de las clases nuevas aparecieron dos errores viejos. `plantillas.py` reportaba una regla de negocio sin origen en la línea anterior a la suya. Y las dos pruebas de renombrado del trinquete de marcas no probaban nada: `git mv` fallaba callado porque la carpeta destino no existía. El enlace al README de una carpeta (fila 18) fue el tercero |
| Por qué importa | La paridad compara lo viejo con lo nuevo, así que un error del viejo pasa igual al nuevo. Solo una prueba escrita de cero lo ve |
| Qué se decidió | Se corrigen en las dos versiones, la vieja y la clase, y la paridad se vuelve a correr: queda igual en este repo y en tres proyectos reales |
| Pendiente | [Pendiente 116: el código de Cimiento se repite en vez de reusarse](pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/pendiente.md), fila 19 de su análisis |

### H-1 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-04 10:17, el freno detuvo una orden de consola sobre `/tmp/f.txt`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Ninguno, aprobado por el usuario el 2026-10-05: la escritura se rehízo dentro del repositorio, en `historico-chat/scripts/`, como pide `04·S9` |

### H-2 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-04 10:29, el freno detuvo una orden de consola sobre `$f`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Ninguno, aprobado por el usuario el 2026-10-05: el freno tomó la variable `$f` como ruta; lo trata el [pendiente 113: el freno toma texto de los comandos como rutas](pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md) |

### H-3 · Apareció `proyectos/cimiento/node_modules/` y el freno lo cuenta como cambio

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-04, al medir el umbral de la HU-027, el freno detuvo la ejecución por cientos de archivos de `proyectos/cimiento/node_modules/` (Tabler, ApexCharts, htmx, Popper). Esta sesión no los creó: la orden solo leía. El `.gitignore` tapa `proyectos/*/.venv/` pero no `node_modules/`. |
| Por qué importa | Es el mismo caso del `.venv` de la HU-008: lo que instala un proyecto se ve como cambio sin plan, y el freno para todo lo demás. |
| Pendiente | Resuelto el 2026-10-05: `proyectos/*/node_modules/` ya está en el `.gitignore` y git la ignora. |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: resumen sin hallazgos -->

<!-- aviso: falta decir si la sesión se puede cerrar -->
