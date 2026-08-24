# El ciclo de vida del desarrollo de software (CVDS)

> En inglés se lo encuentra como **SDLC**, *software development life cycle*, que es la sigla que trae casi toda la bibliografía.

Las siete etapas que recorre todo desarrollo, y **qué queda escrito en cada una**. La etapa dice qué pregunta se responde; el molde dice cómo se escribe la respuesta.

Los moldes viven en [`plantillas/ciclo-vida-proyectos/`](../ciclo-vida-proyectos/README.md) y no se copian acá: se enlazan, para que no haya dos versiones que diverjan.

| # | Etapa | Qué pregunta responde | Qué queda escrito |
|---|---|---|---|
| 1 | [`Planificación`](planificacion/README.md) | ¿Vale la pena, y por qué camino? | 01 · 12 · 13 |
| 2 | [`Análisis de requisitos`](analisis-requisitos/README.md) | ¿Qué debe hacer? | 02 · 03 · 04 |
| 3 | [`Diseño`](diseno/README.md) | ¿Cómo lo va a hacer? | 06 · 14 · 15 · 16 |
| 4 | [`Implementación`](implementacion/README.md) | ¿Qué se toca, en qué orden? | 05 · 07 · 10 |
| 5 | [`Pruebas`](pruebas/README.md) | ¿Cumple, y con qué evidencia? | 08 · 09 · 11 |
| 6 | [`Despliegue`](despliegue/README.md) | ¿Qué se entregó, y cómo se instala? | 17 · 19 · 20 |
| 7 | [`Mantenimiento`](mantenimiento/README.md) | ¿Cómo se sostiene vivo? | 18 · 21 · 22 |

---



**Cada etapa tiene su documento**, con lo que se decide en ella, sus entregables, sus puertas y su cierre. El molde vive en esta misma carpeta; lo llenado, en el proyecto que lo use.

---

## Dos cosas que la lista numerada hace creer

**El ciclo es un anillo.** El cierre de la etapa 7, y el de cada fase de la 5, reentra por la 1. El inventario de la etapa 2 tampoco se congela: madura con cada ítem construido hasta convertirse en el manual del producto.

**La envergadura ajusta la profundidad, nunca la existencia.** Ninguna etapa se salta porque el proyecto sea pequeño. La que no tenga materia se llena con «No aplica porque...» y su porqué, que es un dato, mientras que el silencio no dice si se pensó o se olvidó.
