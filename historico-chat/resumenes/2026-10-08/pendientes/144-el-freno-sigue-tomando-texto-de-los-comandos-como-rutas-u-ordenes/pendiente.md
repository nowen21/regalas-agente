# Pendiente: el freno sigue tomando texto de los comandos como rutas u órdenes

| | |
|---|---|
| **De dónde sale** | H-29, H-30, H-40 y H-42 de la [sesión del 2026-10-06](../../../2026-10-06/sesion.md); H-1 y H-5 de la [sesión del 2026-10-08](../../guiones-que-pasan-a-cimiento.md) |

## El problema

El [pendiente 113](../../../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md) corrigió los tres casos de scilit (el `EOF`, el `sed` y el `mkdir`). El freno (`proyectos/cimiento/core/enganches/freno.py`) siguió deteniendo órdenes válidas, en seis casos nuevos:

| Hallazgo | Cuándo | Qué detuvo y por qué no debía |
|---|---|---|
| H-29 | 2026-10-07 21:49 | Tomó como ruta `proyectos/cimiento/3`, un pedazo del texto que iba después de un `>` |
| H-30 | 2026-10-07 22:01 | Tomó como ruta `proyectos/cimiento/$P`; `$P` era una variable de la misma orden, que nombraba un archivo declarado en el plan |
| H-40 | 2026-10-08 13:46 | Un `Start-Process ... -Wait` de PowerShell, por «deja un proceso corriendo después del turno (04·S10)»; con `-Wait`, la orden espera a que el proceso termine |
| H-42 | 2026-10-08 15:04 | Un `manage.py cerrar_fase`, por la misma razón, porque el texto de `--hallazgos` decía «Start-Process -Wait»: leyó como orden un argumento entre comillas |
| H-1 (2026-10-08) | 2026-10-08 22:19 | Una orden que solo listaba carpetas, por «escribió `proyectos/cimiento/core/herramientas/tests_instalacion.py`»; ese archivo tenía cambios sin guardar de otra sesión |
| H-5 (2026-10-08) | 2026-10-08 23:06 | Un `git status`, por «escribió `proyectos/cimiento/core/herramientas/desinstalar.py`»; también tenía cambios sin guardar de otra sesión |

Los dos primeros son variables y redirecciones que el freno no resuelve. Los dos últimos son nuevos: el freno busca palabras de órdenes peligrosas en todo el texto, también dentro de las comillas, y no mira las opciones que les quitan el peligro. Los dos del 2026-10-08 son de otra clase: al comparar lo que cambió en la carpeta antes y después de una orden, el freno le atribuye a esa orden lo que escribió otra sesión que trabaja al mismo tiempo.

## Por qué importa

Cada falso positivo detiene el trabajo, deja un hallazgo falso en el resumen y obliga a reescribir la orden de otra forma. Con el tiempo se aprende a esquivar el freno en vez de obedecerlo, y eso le quita valor a sus detenciones legítimas, como H-38, H-39 y H-41 de la misma sesión.
