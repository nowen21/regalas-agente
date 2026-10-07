# Pendiente: las pantallas orientan al usuario sin que tenga que conocer cómo está armado el sistema

| | |
|---|---|
| **De dónde sale** | [H-14 · Las pantallas no orientan al usuario, y el estándar no tiene guía ni regla que lo exija](../../../2026-10-06/sesion.md), en el resumen de la sesión del 2026-10-06 |

## El problema

El capítulo `17 · Interfaz` es opt-in y no exige que la pantalla oriente sola, y el estándar no tiene una guía de diseño de pantallas. En Cimiento:

- «Propuestas», «Reportes», «Vista previa» y «Subir a git» no están en el menú, y «Inicio» no avisa lo que espera una decisión.
- «Propuestas» (`proyectos/cimiento/core/estandar/templates/estandar/propuestas.html`) muestra el documento entero sin marcar qué cambió, obliga a aprobar una por una y no pide motivo al rechazar.
- Las preguntas del tipo de versión (`historia/_tipo_de_version.html`) no se entienden y no tienen su «?».
- De 15 formularios, solo 2 tienen el «?» por campo; ninguna de las 14 tablas se ordena, se filtra ni se pagina.

## Por qué importa

Lo que no se encuentra no se usa, y la línea base no puede exigir lo que ella misma no cumple.
