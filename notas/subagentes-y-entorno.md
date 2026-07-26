# Sub-agentes: qué ofrece el entorno y qué desbloquea

> Varios pendientes decían "⏳ depende del entorno". Este documento aclara que **la capacidad ya existe** en Claude Code; lo que falta es **construir nuestros roles y el orquestador encima**.

## Qué provee Claude Code (ya disponible)

- **Lanzar sub-agentes** (herramienta Agent), en **segundo plano** o en **paralelo**.
- **Tipos de agente especializados** listos: `Explore` (lectura/búsqueda), `Plan` (diseño), `general-purpose`, `code-reviewer`, etc.
- **Contexto aislado por sub-agente**: cada uno trabaja en su propia ventana, sin ver el ruido del resto.
- **Workflows**: orquestación determinista de varios sub-agentes (fan-out, pipeline), con activación explícita.

## Qué pendientes desbloquea

| Pendiente | Antes | Ahora |
|---|---|---|
| **Aislamiento de contexto** | ⏳ dependía del entorno | ✅ **disponible** (sub-agentes con contexto propio) |
| **Roles como actores separados** | ⏳ | ✅ **construibles** (cada rol = un sub-agente con sus reglas) |
| **Orquestación en paralelo** | ⏳ | ✅ **disponible** (workflows) |

## Lo que todavía falta (construir, no capacidad)

- **Cablear los 7 roles** a sub-agentes: cada rol (explorer, proposer, spec writer, designer, task planner, implementer, verifier) definido con su foco = su subconjunto de reglas base.
- **El orquestador** que los llama en orden, controla cada **puerta/checkpoint** y persiste el estado (checkpointing).
- El **grafo de dependencias** que el orquestador usa para ordenar/paralelizar tareas.

## En una frase

**El motor de sub-agentes existe; falta cablear nuestros roles y el orquestador a ese motor.**

Relacionado: [`roles-especializados.md`](roles-especializados.md), [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md), [`aislamiento-checkpoints-memoria.md`](aislamiento-checkpoints-memoria.md).
