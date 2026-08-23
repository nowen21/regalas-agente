# El ciclo de vida del desarrollo de software (CVDS)

> En inglés se lo encuentra como **SDLC**, *software development life cycle*, que es la sigla que trae casi toda la bibliografía.

Las siete etapas que recorre todo desarrollo, y **qué queda escrito en cada una**. La etapa dice qué pregunta se responde; el molde dice cómo se escribe la respuesta.

Los moldes viven en [`plantillas/ciclo-vida-proyectos/`](../plantillas/ciclo-vida-proyectos/README.md) y no se copian acá: se enlazan, para que no haya dos versiones que diverjan.

| # | Etapa | Qué pregunta responde | Qué queda escrito |
|---|---|---|---|
| 1 |  [`Planificación`](planificacion/README.md) | ¿Vale la pena, y por qué camino? | 01 · 12 · 13 |
| 2 | Análisis de requisitos | ¿Qué debe hacer? | 02 · 03 · 04 |
| 3 | Diseño | ¿Cómo lo va a hacer? | 06 · 14 · 15 · 16 |
| 4 | Implementación | ¿Qué se toca, en qué orden? | 05 · 07 · 10 |
| 5 | Pruebas | ¿Cumple, y con qué evidencia? | 08 · 09 · 11 |
| 6 | Despliegue | ¿Qué se entregó, y cómo se instala? | 17 · 19 · 20 |
| 7 | Mantenimiento | ¿Cómo se sostiene vivo? | 18 · 21 · 22 |

---



## 2 · Análisis de requisitos

**Qué** debe hacer el sistema, sin decir todavía cómo. Confundir las dos cosas acá es el error caro del ciclo: un requisito escrito como solución cierra opciones antes de haberlas mirado.

Va: el alcance completo ítem por ítem (todo lo que el producto debe tener, esté construido o no), agrupado en épicas y bajado a historias de usuario con criterios de aceptación verificables.

Puerta: sin inventario **aprobado por el usuario** no se derivan épicas ([`02·F26`](../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).

Moldes: [02-inventario-funcionalidades](../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), [03-epica](../plantillas/ciclo-vida-proyectos/03-epica.md) y [04-HU](../plantillas/ciclo-vida-proyectos/04-HU.md)

## 3 · Diseño

**Cómo** lo va a hacer, antes de escribir código.

Va: qué hace cada módulo y qué deja explícitamente por fuera, las entidades con el diccionario de cada campo, las pantallas y la navegación, el contrato de la API para quien integre sin leer el código, y las decisiones de arquitectura con su porqué y sus alternativas.

Puerta: sin especificación acordada no hay código ([`02·F2`](../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)).

Moldes: [06-especificacion-modulo](../plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md), [14-modelo-de-datos](../plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md), [15-diseno-de-interfaz](../plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md) y [16-documentacion-de-api](../plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md)

## 4 · Implementación o codificación

El trabajo partido en unidades que caben en una jornada y se pueden revertir.

Va: la fase como unidad de ejecución de una historia, qué archivos se tocan y en qué orden, cómo se deshace si sale mal, y el estado de la fase escrito en el repositorio, porque el chat se pierde y el repositorio no.

Moldes: [05-fase](../plantillas/ciclo-vida-proyectos/05-fase.md), [07-plan-trabajo](../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) ([`02·F14`](../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)) y [10-estado-fase](../plantillas/ciclo-vida-proyectos/10-estado-fase.md)

## 5 · Pruebas

Con qué se comprueba cada criterio, y qué dio.

Va: los casos que cubren **cada** criterio de aceptación, escritos junto al plan de trabajo y aprobados con él ([`02·F4`](../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)); la evidencia de lo que se ejecutó; el veredicto criterio por criterio; y el cierre con lo que quedó hecho y la deuda que se declara.

El estado de una funcionalidad lo fija la prueba ejecutada, no la lectura del código: mientras no haya prueba, lo honesto es «sin verificar».

Moldes: [08-plan-pruebas](../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md), [09-resultado-pruebas](../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) y [11-funcionalidad-implementada](../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md)

## 6 · Despliegue

Ponerlo a andar donde se usa, y dejar constancia de qué se entregó.

Va: la instalación desde cero, literal y verificable por alguien que no estuvo en el desarrollo; qué trae la versión dicho para quien la usa, no para quien la programó; y el acta con la evidencia y la aceptación.

Moldes: [17-manual-de-instalacion](../plantillas/ciclo-vida-proyectos/17-manual-de-instalacion.md), [19-notas-de-version](../plantillas/ciclo-vida-proyectos/19-notas-de-version.md) y [20-acta-de-entrega](../plantillas/ciclo-vida-proyectos/20-acta-de-entrega.md)

## 7 · Mantenimiento

Sostenerlo vivo después de entregar. Es la etapa más larga de todas y la que menos se planea.

Va: respaldos **probados**, no configurados, monitoreo, qué hacer cuando falla, lo que le pasa al sistema en producción en orden cronológico, las rutinas periódicas que lo sostienen y el fin de vida.

Moldes: [18-manual-tecnico-y-de-operacion](../plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md), [21-bitacora-de-operacion](../plantillas/ciclo-vida-proyectos/21-bitacora-de-operacion.md) y [22-plan-de-mantenimiento](../plantillas/ciclo-vida-proyectos/22-plan-de-mantenimiento.md)

---

## Dos cosas que la lista numerada hace creer

**El ciclo es un anillo.** El cierre de la etapa 7, y el de cada fase de la 5, reentra por la 1. El inventario de la etapa 2 tampoco se congela: madura con cada ítem construido hasta convertirse en el manual del producto.

**La envergadura ajusta la profundidad, nunca la existencia.** Ninguna etapa se salta porque el proyecto sea pequeño. La que no tenga materia se llena con «No aplica porque...» y su porqué, que es un dato, mientras que el silencio no dice si se pensó o se olvidó.
