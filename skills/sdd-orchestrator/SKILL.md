---
name: sdd-orchestrator
description: Dirige el flujo completo de desarrollo (spec-driven) de punta a punta: llama a cada rol en su estación, controla las puertas de calidad, usa el grafo de dependencias para ordenar el trabajo y persiste el estado para no perderlo. Úsala para llevar un módulo o una fase de principio a fin de forma controlada, o cuando el usuario pida "orquestá esto", "manejá la fase completa". Es el rol Orchestrator (el director de la línea de montaje).
---

# SDD Orchestrator (el director)

Coordina las 8 skills-rol (más las estaciones **Épica** y **HU**, dirigidas por las reglas `13·DOC16` y `13·DOC15`) como una **línea de montaje**: llama a cada una en su estación, **controla la puerta** de cada estación (nada avanza si no pasa), usa el **grafo de dependencias** del Task Planner para ordenar/paralelizar, y **persiste el estado** en cada puerta para sobrevivir a la compactación. No hace el trabajo de los roles; los **dirige**. Respeta el núcleo (`00`) por encima de todo.

## Las estaciones y sus puertas

| # | Estación (rol / skill) | Puerta para avanzar | ¿Quién aprueba? |
|---|---|---|---|
| 1 | Explorer · `analizar-proyecto` | Contexto entendido, sin supuestos sin verificar | interna |
| 2 | Proposer · `proponer-alcance` | **Alcance aprobado** | **usuario** |
| 3 | Épica Writer · `13·DOC16` (desde `plantillas/epica.md`) | **Épica aprobada** (problema, valor, criterios de resultado, HUs identificadas) | **usuario** |
| 4 | HU Writer · `13·DOC15` (desde `plantillas/HU.md`) | **HUs aprobadas** (criterios de aceptación) | **usuario** |
| 5 | Spec Writer · `generar-spec-modulo` | **Spec aprobada** | **usuario** |
| 6 | Designer · `disenar-arquitectura` | Diseño coherente con la spec | interna |
| 7 | Task Planner · `planificar-tareas` | **Plan + pruebas aprobados** | **usuario** |
| 8 | Implementer · `implementar` | Plan implementado + pruebas verdes | interna |
| 9 | Verifier · `cerrar-fase` | Trazabilidad sin faltantes | interna |
| 10 | Crítico · `revisar-critico` | Sin hallazgos graves (o corregidos) | interna |
| 11 | Cierre documental + señales | Docs y señales al día (`13`) | interna |
| 12 | Commit | **Autorizado** | **usuario** (`00`·N2) |
| 13 | Publicación / despliegue | **Autorizado** | **usuario** (`00`·N2) |

## Reglas del director

- **No saltar ni reordenar** estaciones. **No avanzar** si la puerta no pasa.
- **Precondición (paso 0):** antes de la estación 1 debe existir el **brief** (`plantillas/brief.md` → `prompts/<slug>-brief.md`). Es **obligatorio** (`02·F0` cadena). Si no existe, el director lo pide o ayuda a redactarlo y el usuario lo aprueba antes de arrancar. Sin brief no se orquesta.
- Las puertas de **usuario** (2, 3, 4, 5, 7, 12, 13) exigen OK explícito. Las **internas** son checkpoints de calidad que el director verifica.
- En la estación 3 (**Épica Writer**), generar la épica según `13·DOC16` desde `plantillas/epica.md`, guardarla en `documentacion/epicas/EP-<NNN>-<slug>.md`. Define problema, valor, criterios de **resultado** y las HUs que la componen. **Obligatoria siempre** — no se funde con las HU ni se omite por tamaño (`02·F0` cadena obligatoria); requiere el brief (precondición) que le da origen.
- En la estación 4 (**HU Writer**), generar las HUs según `13·DOC15` desde `plantillas/HU.md`, guardarlas en `documentacion/hus/<modulo>/` con su índice `README.md`. Cada HU declara su **épica** (estación 3) y sus **criterios de aceptación**, que la spec (estación 5) recoge.
- En la estación 7, el Task Planner deriva la **matriz de casos de prueba** con la skill `generar-casos-prueba` (corner cases + triangulación) como parte del plan de pruebas.
- En la estación 8, usar el **grafo de dependencias** del Task Planner: ejecutar en **orden topológico** y, si el entorno lo permite, correr en **paralelo** las tareas independientes.
- **Aislamiento:** cada rol puede correr como **sub-agente** con su propio contexto (entrada acotada: la spec al Designer, el plan al Implementer). Si no hay sub-agentes disponibles, el mismo agente cambia de rol por estación.
- El núcleo manda: no commit/push por iniciativa (`00`·N2), no romper para pasar (`00`·N3), no tocar datos reales (`00`·N4).

## Estado persistido (checkpointing)

En **cada puerta**, escribir el estado en un archivo (ubicación de la capa 3, p. ej. `documentacion/«modulo»/estado-fase.md` · plantilla `plantillas/estado-fase.md`):

- En qué **estación** va y qué puertas ya pasó.
- Las **decisiones y señales** generadas (`13`·DOC5) — para no perderlas al compactar.
- Lo pendiente / preguntas abiertas.

Al reanudar, leer ese archivo y continuar desde la última puerta pasada. Es la defensa contra "la compactación mata decisiones".

## Manejo de fallos

Si una puerta **no pasa** (pruebas rojas, hallazgo grave del Crítico, trazabilidad incompleta, alcance rechazado): **no avanzar**. Volver a la estación que corresponde, corregir **en su lugar**, y **re-verificar** la puerta. No forzar el avance (`00`·N3).

## Salida

Reporte del recorrido: hasta qué estación se llegó, qué puertas pasaron, y — si se bloqueó — en cuál y qué falta. Al llegar a la 11, la fase está lista para el commit que el usuario autorice.

Ver: los 8 roles en `skills/`, el flujo `02` (F1–F7, F4.2 las 11 etapas), el grafo del Task Planner, la memoria por señales (`13`·DOC5), y las notas de diseño en `notas/`.
