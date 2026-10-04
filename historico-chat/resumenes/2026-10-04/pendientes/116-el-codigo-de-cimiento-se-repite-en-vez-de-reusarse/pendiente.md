# Pendiente: el código de Cimiento se repite en vez de reusarse

| | |
|---|---|
| **De dónde sale** | [H-3 · El código de Cimiento se repite en vez de reusarse](../../optimizar-el-codigo-de-cimiento.md), en el resumen de la sesión del 2026-10-04 |

## El problema

Las mismas funciones están copiadas en `validadores/`, `adaptadores/claude-code/` y `plataforma/nucleo/`. `validadores/comun.py` no tiene nada de rutas, raíz ni git, y los enganches y la plataforma no tienen sitio común.

## Por qué importa

Un arreglo llega a una sola copia, y como los validadores sirven a todos los proyectos, la copia sin arreglar falla en todos.
