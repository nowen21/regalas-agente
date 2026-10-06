# Pendiente: el freno le cobra a una sesión lo que escribe otra al mismo tiempo

| | |
|---|---|
| **De dónde sale** | [H-11 · El freno le cobra a esta sesión lo que otra escribe al mismo tiempo](../../../2026-10-04/sesion-3.md), en el resumen de la sesión del 2026-10-04 |

## El problema

Antes de cada orden de consola, el freno toma una foto de lo que git ve cambiado (`Freno.tomar_foto`, en `proyectos/cimiento/core/enganches/freno.py:474`). Después de la orden compara con esa foto (`Freno.despues_por_nivel`, línea 495), y todo archivo que cambió en el medio lo trata como escrito por la orden. No mira quién lo cambió.

El 2026-10-05, entre las 18:56 y las 18:58, otra sesión editaba 17 archivos: `base/00-identidad-y-rol/marcadores-de-ia.md`, la regla `ID8`, los pendientes 91 y 92, seis de `pendientes/hecho/`, cuatro de `validadores/` y dos de `plantillas/`. Esta sesión corrió dos órdenes que no escriben ahí: `cerrar_fase` y una lectura con `ls` y `grep`. El freno le atribuyó los 17 archivos a esta sesión, pidió detener la ejecución y escribió 17 hallazgos iguales en su resumen.

Además, la foto es un solo archivo para todas las sesiones (`.git/cimiento-freno.json`, línea 63). Si dos sesiones corren órdenes casi al mismo tiempo, una pisa la foto de la otra.

## Por qué importa

Con dos sesiones abiertas en el mismo repositorio, cada orden de consola de una puede llenar de hallazgos falsos el resumen de la otra y frenar trabajo que sí está en su plan. El agente tiene que limpiar el resumen a mano y el aviso ocupa miles de tokens (unos 3300 en este caso). `cambios_por_sesion` ya separa lo de cada sesión para el commit, pero el freno no lo usa.
