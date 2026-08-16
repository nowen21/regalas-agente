# Pendiente · La fase A de EP-003 · HU-010 cerró sin cumplir

**Estado:** abierto · anotado 2026-08-15 · nace del hallazgo H-6 del [2026-08-15 · la-plantilla-del-resultado-de-pruebas](../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md).

## El problema

Al reescribir el [resultado_pruebas.md](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md) de esa fase con la forma nueva de [plantillas/planes/resultados.md](../plantillas/planes/resultados.md), el veredicto pasó de «aprobada con una prueba pendiente» a **No cumple**. No cambió el criterio: cambió que ahora hay dónde escribir lo que faltaba.

Dos cosas que el formato anterior no dejaba ver:

| Qué | Cuánto |
|---|---|
| `RNF-01` sin ningún caso ejecutado | CP-006 necesita que las cinco entradas las lea alguien que no las escribió, y eso no se hizo |
| Pasos del plan sin registro de qué salió | **16 de 35**, más 3 que se hicieron distinto de lo que el plan pedía |

Es el mismo defecto de [`A-EP-005-HU-008`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md): una fase cerrada con criterios en «cumple» que nadie podía respaldar. La diferencia es que allá el defecto salió una sesión después, y acá salió al aplicar la plantilla.

## Qué falta

1. **Correr CP-006.** Conseguir a alguien que no haya participado en escribir el glosario, entregarle las cinco entradas sin explicación, anotar cada pregunta que tenga que hacer y corregir la entrada de cada pregunta.
2. **Resolver los 16 pasos sin registro y los 3 que se hicieron distinto.** Están listados en la sección 2 del resultado, caso por caso. De cada uno: volver a correrlo y anotar qué sale, o dejar escrito por qué no se va a correr.
3. **Rehacer §5 y §5.1 y volver a dar veredicto**, y copiar el concepto al [estado-fase.md](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/estado-fase.md) — hoy dice lo anterior y se contradice con el resultado ([pendiente 28](28-el-veredicto-de-la-fase-vive-en-dos-sitios.md)).

**Se reabre la fase A, no se abre una nueva.** Lo que falla es ese trabajo, y su documentación decía que estaba hecho: es el mismo criterio que se usó con `A-EP-005-HU-008`.

## El límite

Los tres criterios de aceptación sí cumplen y ningún defecto de contenido queda abierto: el glosario está bien. Lo que falta es la prueba de legibilidad y el respaldo de los pasos, no el entregable.

**Va primero de los tres pendientes de esa sesión:** mientras no se resuelva, hay una fase cerrada con un veredicto que no era.
