# Pendiente · Cerrar un pendiente rompe los enlaces que lo citaban

**Estado:** **cerrado** el 2026-08-17. Anotado el 2026-08-16.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-005 — Comprobar los enlaces y las citas a reglas](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) — los enlaces que rompe el cierre son enlaces, y su RN-01 es que resuelvan |
| **De dónde sale** | El hallazgo H-5 del [resumen de la sesión 7](../../historico-chat/resumenes/2026-08-16/sesion-7.md) |
| **Hermano de** | El punto 4 del [33](lo-que-quedo-abierto-en-las-sesiones-viejas.md) —renombrar una sesión rompe lo de fuera— y del [35](renombrar-deja-el-resumen-coherente.md), que cerró el de adentro |

## El problema

Al cerrar un pendiente, su archivo se mueve a `pendientes/hecho/` con un nombre nuevo. Todo lo que lo citaba queda apuntando a un archivo que ya no está.

**Medido el 2026-08-16:** cerrar el 35 dejó **12 enlaces huérfanos** —dos en el índice del backlog, uno en otro pendiente, seis en tres resúmenes y uno en el plan de trabajo de su propia fase—. Cerrar el 38, el 43, el 30, el 27 y el 28 dejó otros tantos, y todos se corrigieron a mano, uno por uno.

**Y ya había pasado sin que nadie lo viera:** el `plan_trabajo` de la fase `B-EP-007-HU-001` llevaba desde el 2026-08-16 apuntando al archivo del pendiente 45, movido al cerrarlo.

## Por qué importa

El backlog se cita a sí mismo todo el tiempo —el 36 nombra al 34 y al 35, el 33 al 19 y al 31—, y cada cierre rompe esas citas. Es trabajo manual que aparece **justo cuando se está terminando algo**, que es cuando menos ganas hay de mirarlo.

## Qué falta

La solución ya existe en el repositorio, aplicada a otra cosa: [`citas.py`](../../validadores/citas.py) tiene un modo que **repara** las rutas cuando un capítulo se mueve. Falta:

1. Un comando que mueva el pendiente a `hecho/` **y** redirija sus citas, en vez de mover a mano.
2. O, más barato: que el validador de enlaces sepa que un enlace roto a `pendientes/NN-*.md` probablemente esté en `pendientes/hecho/`, y lo diga.

## El límite

No cubre los enlaces desde **fuera del repositorio** —un proyecto heredero que cite un pendiente del estándar—, y eso no tiene arreglo desde acá.

## Cómo se sabrá que cerró

Se cierra un pendiente citado desde varios archivos y el validador de enlaces sigue en cero, sin corregir nada a mano.

---

# Cómo cerró — 2026-08-17

**Por la salida 1**, la que el pendiente daba por más cara: un comando que mueve el pendiente **y** redirige sus citas. La salida 2 —que el validador adivine que un roto a `pendientes/NN-*.md` «probablemente esté en hecho/»— habría dejado el trabajo manual intacto, solo que con una pista.

## Se midió otra vez, y era cuatro veces peor

Cerrar el [53](ningun-validador-termina-en-silencio.md) a mano dejó **58 enlaces rotos en 39 archivos**: doce fases de cuatro épicas, dos resúmenes de sesión, el índice del backlog y el propio documento de cierre que se acababa de escribir. Antes eran 12.

## Lo que se construyó

[validadores/cerrar.py](../../validadores/cerrar.py). **No busca texto:** resuelve cada enlace contra el disco y compara rutas absolutas, así que da igual cuántos `../` lleve delante o desde qué carpeta se escribió. Simula por omisión, como `citas.py`.

Movió los **seis** pendientes que estaban cerrados y seguían en la carpeta —el 25, el 31, el 40, el 41, el 42 y el 44— además del 53: **191 enlaces reescritos, ninguno roto al terminar.**

## Las dos trampas que costaron una corrida cada una

**1 · Los enlaces de salida.** Mover el archivo lo baja un nivel y sus propios `../` quedan cortos. El 53 llegó a `hecho/` con ocho rotos hacia afuera. Arrastrar a quien cita al archivo no basta: hay que recalcular también lo que **el archivo** cita.

**2 · La convención cambia con la carpeta.** Se vio al mover un procedimiento en el [23](plantillas-separa-modelos-de-procedimientos.md): venía de `plantillas/`, que **sí** se copia dentro de los proyectos, y por eso citaba con `«RUTA-ESTANDAR»`. En `base/` eso no vale. Mover un documento entre carpetas no es solo cambiarlo de sitio.

## Y sirve para más que pendientes

`mover()` acepta cualquier `.md`. El [23](plantillas-separa-modelos-de-procedimientos.md) lo usó para llevar `retrodocumentacion.md` a su capítulo, con sus 12 citas. **Eso cierra también el punto 4 del [33](lo-que-quedo-abierto-en-las-sesiones-viejas.md)** en lo que se puede cerrar desde acá: renombrar dejaba rotos los enlaces de fuera, y ahora hay con qué arrastrarlos.

## El límite sigue en pie

No cubre los enlaces desde **fuera del repositorio** —un proyecto heredero que cite un pendiente del estándar—, y eso no tiene arreglo desde acá. Queda dicho.

## Cómo quedó comprobado

[validadores/tests/test_cerrar_arrastra_las_citas.py](../../validadores/tests/test_cerrar_arrastra_las_citas.py), 12 casos: las dos direcciones, el ancla que se conserva, el `%20` que si no se decodifica deja el enlace roto en silencio, lo externo que no se toca, el pendiente de número parecido que no se confunde, y las cuatro salvaguardas —simular no escribe, no pisa un nombre tomado, avisa si el número no existe y avisa si está repetido en vez de elegir uno—.
