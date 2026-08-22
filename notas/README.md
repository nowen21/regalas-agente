# Notas de diseño

Notas sobre el diseño y los pendientes del estándar. No son parte del estándar en sí (`base/`, `plantillas/`, `skills/`), sino el registro de decisiones, explicaciones y trabajo futuro.

## Índice

- [cobertura-del-agente.md](cobertura-del-agente.md) — qué cumple el estándar hoy y qué no (✅ / ⏳).
- [roles-especializados.md](roles-especializados.md) — los 7 roles (explorer → verifier) como estaciones de la línea de montaje.
- [orquestador-y-triangulacion.md](orquestador-y-triangulacion.md) — diseño del SDD Orquestador, la línea de montaje, la triangulación y el grafo de dependencias.
- [que-es-triangulacion-de-pruebas.md](que-es-triangulacion-de-pruebas.md) — explicación llana de qué es triangular una prueba.
- [aislamiento-checkpoints-memoria.md](aislamiento-checkpoints-memoria.md) — aislamiento de contexto, checkpoints de calidad y memoria institucional.
- [compactacion-mata-decisiones.md](compactacion-mata-decisiones.md) — la amenaza de perder decisiones al compactar el contexto y cómo se ataca.
- [notas/como-se-guarda-la-historia-de-un-valor.md](como-se-guarda-la-historia-de-un-valor.md) — por qué reconstruir el pasado sumando lo vivo devuelve el estado teórico y no el que hubo, y cómo se guardan los tramos. Es el detalle de `03·D7`.
- [notas/rutas-fuera-del-proyecto.md](rutas-fuera-del-proyecto.md) — qué rutas quedan fuera del alcance del agente y por qué autorizar un archivo no autoriza a su carpeta padre. Es el detalle de `04·S9`.
- [notas/pertenencia-y-autoria.md](pertenencia-y-autoria.md) — por qué se confunde «de quién es el dato» con «quién lo tocó», y qué se rompe: el segundo usuario del mismo contenedor no ve nada. Es el porqué de `03·D8`.
- [notas/la-fuente-de-las-reglas-es-el-texto.md](la-fuente-de-las-reglas-es-el-texto.md) — por qué las reglas viven en archivos y no en una base de datos: lo que se perdería es poder ver qué cambió y aprobarlo antes de que rija.
- [notas/entregables-del-ciclo-de-vida.md](entregables-del-ciclo-de-vida.md) — la lista canónica de documentos que el ciclo de vida del software exige entregar (IEEE/ISO), con el cruce contra los moldes de Cimiento; material del análisis de `plantillas/ciclo-vida-proyectos/` (2026-08-21).
- [notas/estructura.md](estructura.md) — referencia de arquitectura de un agente LLM en producción (capas, presupuesto, evals, contenido no confiable). Cimiento la cumple por concepto, no por carpeta: el análisis del 2026-08-19 dejó sus brechas en el resumen de esa sesión.
- [memoria-por-senales.md](memoria-por-senales.md) — diseño concreto de la memoria: señales tipadas con what/why/where/learned, metadatos y ciclo de vida.
- [memoria-buscable-fts5.md](memoria-buscable-fts5.md) — backend opcional SQLite+FTS5 para hacer buscables las señales (esquema y consultas listos).
- [subagentes-y-entorno.md](subagentes-y-entorno.md) — qué sub-agentes ofrece Claude Code y qué pendientes desbloquea (falta construir, no capacidad).
- [velocidad-consistencia-calidad.md](velocidad-consistencia-calidad.md) — el estándar frente a los tres: consistencia y calidad de fábrica, velocidad con matiz.
- [agente-24-7-y-tareas.md](agente-24-7-y-tareas.md) — automatización: 24/7, rutinas y cola de tareas, con el trade-off de seguridad.
- [notas/porques-recortados-al-molde.md](porques-recortados-al-molde.md): los porqués que salieron de cinco reglas de los capítulos `18` y `19` al recortarlas al molde (pendiente 19, 2026-08-22).
- [marca-del-espacio-por-llenar.md](marca-del-espacio-por-llenar.md) — por qué los huecos de un modelo se marcan `«…»` y qué marcas se descartaron.

## Hoja de ruta (pendientes, por orden sugerido)

| # | Pendiente | Tamaño | Depende de | Nota |
|---|---|---|---|---|
| ~~1~~ | ~~**Plantilla genérica de especificación de módulo**~~ | — | — | ✅ **Hecha** — `plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md` |
| ~~2~~ | ~~**Skill `generar-spec-modulo`**~~ | — | — | ✅ **Hecha** — `skills/generar-spec-modulo/` (rol Escritor de especificación) |
| ~~3~~ | ~~**Skill `cerrar-fase`**~~ | — | — | ✅ **Hecha** — `skills/cerrar-fase/` (rol Verificador) |
| ~~4~~ | ~~**Skill `generar-casos-prueba`**~~ | — | — | ✅ **Hecha** — `skills/generar-casos-prueba/` |
| ~~5~~ | ~~**Roles especializados como skills**~~ | — | — | ✅ **Hechos** — los 7 obreros + Crítico/Crítico (`skills/`) |
| ~~6~~ | ~~**Grafo de dependencias entre tareas**~~ | — | — | ✅ Planificador de tareas lo produce · Orquestador lo ejecuta |
| ~~7~~ | ~~**SDD Orquestador**~~ | — | — | ✅ **Hecho** — `skills/sdd-orchestrator/` |
| 8 | **Ejecución paralela real** (sub-agentes) | — | entorno (workflows) | dispuesta por el Orquestador; la corre el entorno |
| 9 | **Aislamiento de contexto** (cada rol como sub-agente) | — | entorno (sub-agentes) | dispuesto por el Orquestador |
| ~~10~~ | ~~**Checkpoints de calidad**~~ | — | — | ✅ el Orquestador impone las puertas |
| ~~11a~~ | ~~**Memoria buscable central con scope**~~ | — | — | ✅ **Hecha** — `memoria/` + skill `usar-memoria` (léxica, entre proyectos) |
| 11b | **Búsqueda semántica** (por significado) | Medio | MCP / vector | la léxica ya está; falta embeddings |

## Ya resuelto

- ✅ **Triangulación de pruebas** — `base/08-pruebas.md` · `T7`.
- ✅ **Explorador** — cubierto por la skill `analizar-proyecto`.
