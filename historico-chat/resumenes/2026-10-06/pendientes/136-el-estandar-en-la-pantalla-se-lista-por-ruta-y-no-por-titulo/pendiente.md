# Pendiente: las reglas del estándar viven en tablas con la estructura del molde

| | |
|---|---|
| **De dónde sale** | [H-12 · Las reglas del estándar se guardan como texto entero, y la pantalla no puede mostrarlas por su nombre ni relacionarlas](../../sesion.md), en el resumen de la sesión del 2026-10-06 |

## El problema

Las 269 reglas del estándar están en 152 documentos de texto, en la tabla `estandar_documento` (`proyectos/cimiento/core/estandar/models.py`), cada uno con solo `ruta` y `contenido`. La pantalla las lista por ruta, sus 2.697 enlaces no abren, las propuestas, la historia y la memoria muestran rutas o números, y las reglas de cada proyecto siguen en archivos.

## Por qué importa

Sin casillas no se puede mostrar, buscar ni relacionar una regla por lo que es.
