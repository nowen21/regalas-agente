# El ciclo de vida del desarrollo de software (CVDS)

> En inglés se lo encuentra como **SDLC**, *software development life cycle*, que es la sigla que trae casi toda la bibliografía.

Las siete etapas que recorre todo desarrollo, y **qué queda escrito en cada una**. La etapa dice qué pregunta se responde; el molde dice cómo se escribe la respuesta.

Los moldes viven en [`plantillas/ciclo-vida-proyectos/`](../plantillas/ciclo-vida-proyectos/README.md) y no se copian acá: se enlazan, para que no haya dos versiones que diverjan.

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

## El estado del proyecto contra este ciclo

Cuántas exigencias de cada etapa cumple hoy el proyecto, cuántas están a medias y cuántas no existen.

| Etapa | Cumple | A medias | No existe |
|---|---|---|---|
| 1 · Planificación | 17 | 0 | 0 |
| 2 · Análisis de requisitos | 11 | 0 | 0 |
| 3 · Diseño | 3 | 5 | 3 |
| 4 · Implementación | 7 | 2 | 1 |
| 5 · Pruebas | 5 | 4 | 0 |
| 6 · Despliegue | 3 | 5 | 3 |
| 7 · Mantenimiento | 5 | 4 | 4 |
| **Total** | **51** | **20** | **11** |

**Dónde es fuerte y dónde es débil, dicho de una vez.** El proyecto cumple casi entero la mitad de en medio del ciclo, que es construir y comprobar: ahí está lo que se hizo con método, con evidencia y con documento. Lo que falta se concentra en los dos extremos: **lo que se decide antes de empezar** y **lo que sostiene el sistema después de entregado**.

Es coherente con cómo nació: el estándar se escribió resolviendo incumplimientos concretos del agente, uno por uno, y por eso tiene músculo donde hubo dolor y hueco donde nunca lo hubo.

**Exigencia por exigencia, con lo que la cumple y dónde está:** en la última sección del documento de cada etapa.

> **Actualizado el 2026-08-24: las etapas 1 y 2 quedaron cerradas y aprobadas.** Sus dieciocho hallazgos se resolvieron uno por uno, con el detalle en la última sección de [planificación](planificacion/README.md) y de [análisis](analisis-requisitos/README.md). Lo escrito ahí es la línea base, y con el inventario aprobado queda abierta la puerta de las épicas.

> **Cómo se hizo.** Se recorrió el árbol del repositorio y se contó: 249 reglas en los 23 capítulos de `base/` (84 con archivo propio y 165 como sección de su capítulo), 7 épicas, 102 historias, 119 fases, 115 resultados de prueba, 101 cierres de funcionalidad, 68 pruebas de los validadores, 10 destrezas y 81 pendientes cerrados. Lo que aparece como cumplido es porque el archivo existe y se abrió; lo que aparece como ausente es porque se buscó y no está.

---

## Los cinco huecos que importan

De los 11 ausentes, estos cinco son los que cambian algo si se llenan. El resto son papeles que un proyecto de una persona puede no necesitar, y decirlo así es más honesto que fingir que faltan.

| # | Hueco | Por qué importa |
|---|---|---|
| 1 | Nadie ajeno al autor instaló el estándar siguiendo solo el manual | Es lo único que separa un estándar de una preferencia personal. Sostiene el proyecto entero y sigue sin comprobarse |
| 2 | El proyecto no tiene inventario de funcionalidades | Es la puerta que le exige a todos los demás (`02·F26`). Incumple escribiendo lo que exige |
| 3 | Sin integración continua | El propio validador la exige y aquí no existe. Las pruebas corren porque alguien se acuerda, que es justo lo que el estándar prohíbe |
| 4 | Ningún respaldo restaurado | Un respaldo sin restaurar es un archivo. Vale para el repositorio y para la base de la memoria |
| 5 | Ninguna decisión de arquitectura escrita | Hay cinco decisiones grandes tomadas y ninguna con sus alternativas descartadas. Dentro de seis meses no se podrán defender |

---

## Lo que este análisis no puede decir

- **No mide calidad, mide existencia.** Que un documento exista no dice que esté bien escrito ni que se siga.
- **No leyó las 249 reglas una por una.** Se verificó qué capítulos existen y qué comprueba cada validador, no el contenido de cada regla.
- **Cuenta lo que el repositorio muestra hoy.** Un archivo puede estar sin usar desde hace meses y aquí aparece igual.

---

## Dos cosas que la lista numerada hace creer

**El ciclo es un anillo.** El cierre de la etapa 7, y el de cada fase de la 5, reentra por la 1. El inventario de la etapa 2 tampoco se congela: madura con cada ítem construido hasta convertirse en el manual del producto.

**La envergadura ajusta la profundidad, nunca la existencia.** Ninguna etapa se salta porque el proyecto sea pequeño. La que no tenga materia se llena con «No aplica porque...» y su porqué, que es un dato, mientras que el silencio no dice si se pensó o se olvidó.
