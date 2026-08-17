# Pendiente · Cerrar un pendiente rompe los enlaces que lo citaban

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-5 del [resumen de la sesión 7](../historico-chat/resumenes/2026-08-16/sesion-7.md) |
| **Hermano de** | El punto 4 del [33](33-defectos-que-destaparon-los-resumenes-viejos.md) —renombrar una sesión rompe lo de fuera— y del [35](hecho/renombrar-deja-el-resumen-coherente.md), que cerró el de adentro |

## El problema

Al cerrar un pendiente, su archivo se mueve a `pendientes/hecho/` con un nombre nuevo. Todo lo que lo citaba queda apuntando a un archivo que ya no está.

**Medido el 2026-08-16:** cerrar el 35 dejó **12 enlaces huérfanos** —dos en el índice del backlog, uno en otro pendiente, seis en tres resúmenes y uno en el plan de trabajo de su propia fase—. Cerrar el 38, el 43, el 30, el 27 y el 28 dejó otros tantos, y todos se corrigieron a mano, uno por uno.

**Y ya había pasado sin que nadie lo viera:** el `plan_trabajo` de la fase `B-EP-007-HU-001` llevaba desde el 2026-08-16 apuntando al archivo del pendiente 45, movido al cerrarlo.

## Por qué importa

El backlog se cita a sí mismo todo el tiempo —el 36 nombra al 34 y al 35, el 33 al 19 y al 31—, y cada cierre rompe esas citas. Es trabajo manual que aparece **justo cuando se está terminando algo**, que es cuando menos ganas hay de mirarlo.

## Qué falta

La solución ya existe en el repositorio, aplicada a otra cosa: [`citas.py`](../validadores/citas.py) tiene un modo que **repara** las rutas cuando un capítulo se mueve. Falta:

1. Un comando que mueva el pendiente a `hecho/` **y** redirija sus citas, en vez de mover a mano.
2. O, más barato: que el validador de enlaces sepa que un enlace roto a `pendientes/NN-*.md` probablemente esté en `pendientes/hecho/`, y lo diga.

## El límite

No cubre los enlaces desde **fuera del repositorio** —un proyecto heredero que cite un pendiente del estándar—, y eso no tiene arreglo desde acá.

## Cómo se sabrá que cerró

Se cierra un pendiente citado desde varios archivos y el validador de enlaces sigue en cero, sin corregir nada a mano.
