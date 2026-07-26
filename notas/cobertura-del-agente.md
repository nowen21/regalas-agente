# Cobertura del estándar: qué cumple y qué no

> Estado a la fecha. "El agente" = Claude Code siguiendo el estándar. Marca ✅ lo que ya está en el estándar, ⏳ lo pendiente.

## ✅ Lo que cumple (ya está en el estándar)

### Núcleo y convenciones base (`base/00`–`16`)

- ✅ **Seguridad crítica** (núcleo blindado): validación previa, git bajo pedido, no romper cosas para pasar, proteger datos reales, operaciones masivas con preview, secretos nunca expuestos. — `00`
- ✅ **Conducta**: avisar antes de tocar, no inventar, quedarse en el alcance, no decidir solo, responder corto. — `01`
- ✅ **Spec-driven development (SDD)**: sin spec acordada no hay código; la spec es el contrato. — `02` · F2
- ✅ **Diseño de datos**: normalización, auditoría, migraciones reversibles y retrocompatibles, catálogos, cero-hardcode. — `03`
- ✅ **Seguridad de aplicación**: authz, validación de entrada, inyección, secretos, CSRF, archivos sensibles. — `04`
- ✅ **Errores y logging**: no tragar errores, fallar controlado, mensajes en dos niveles, no loguear secretos. — `05`
- ✅ **Rendimiento**: N+1, paginación, índices, caché, trabajo en segundo plano. — `06`
- ✅ **Calidad de código**: legibilidad, nombres, funciones pequeñas, DRY, lint. — `07`
- ✅ **Pruebas**: qué probar, aislamiento, no-flaky, cobertura con criterio. — `08`
- ✅ **Triangulación de pruebas + corner cases**: derivar los casos con método (frontera, equivalencia, tablas de decisión, negativos) y triangular el resultado esperado desde fuentes independientes. — `08` · T7
- ✅ **Trazabilidad spec → implementación**: checklist ítem por ítem antes de cerrar. — `13` · DOC3
- ✅ **Git, dependencias, configuración/entornos, privacidad, documentación, estructura/nomenclatura**. — `09`–`14`
- ✅ **Memoria institucional (dentro del proyecto)**: la spec como memoria de largo plazo, decisiones con porqué, carga de contexto, trazabilidad. — `02`·F1/F2/F6, `13`
- ✅ **Memoria por señales (archivos)**: log de señales tipadas (`13`·DOC5 + `plantillas/senales.md`) con what/why/where/learned. Pendiente la recuperación (SQLite+FTS5) y la capa entre proyectos.
- ✅ **Registros inmutables** (patrón opt-in). — `15`
- ✅ **Cumplimiento normativo por construcción** (opt-in): OWASP, ISO 25010, y marco legal declarado por proyecto. — `16`

### Capa 3 y herramientas

- ✅ **Plantillas de proyecto**: `CLAUDE.md`, `stack`, `dominio`, `mapeo-nombres`, `marco-normativo`.
- ✅ **Skill `analizar-proyecto`**: diagnóstico de proyecto existente (qué hay / qué falta / qué sigue + estrategia de pruebas + tecnologías).

## ⏳ Lo que NO cumple todavía (pendiente)

- ⏳ **SDD Orchestrator** (línea de montaje con puertas): el flujo de `02` existe como reglas, pero **no** hay un orquestador que controle las fases y **bloquee el avance** en cada puerta (spec → plan → código → pruebas → trazabilidad → cierre). Ver [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md).
- ⏳ **Orquestación con sub-agentes en paralelo**: depende de las capacidades del entorno (workflows / sub-agentes de Claude Code), no solo del estándar.
- ✅ **Skill `cerrar-fase`** (rol Verifier): `skills/cerrar-fase/` — pruebas + triangulación + trazabilidad antes de cerrar.
- ✅ **Skill `generar-spec-modulo`** (rol Spec Writer): `skills/generar-spec-modulo/` — redacta la spec guiando la plantilla.
- ⏳ **Skills aún no creadas**: `sdd-orchestrator`, `generar-casos-prueba` (matriz de corner cases), y los roles proposer / designer / task planner / implementer.
- ✅ **Plantilla genérica de spec de módulo** (agnóstica): `plantillas/plantilla-spec-modulo.md` — esqueleto para redactar la spec de cualquier módulo.
- ⏳ **Roles especializados** (explorer, proposer, spec writer, designer, task planner, implementer, verifier): las responsabilidades están como reglas, pero los roles como actores separados no existen. Ver [`roles-especializados.md`](roles-especializados.md).
- ⏳ **Grafo de dependencias entre tareas**: hoy el flujo es lineal; falta que el Task Planner genere prerrequisitos y el orquestador ejecute en orden topológico y detecte tareas paralelizables. Ver [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md).
- ⏳ **Aislamiento de contexto** (cada rol en su propio contexto), **checkpoints de calidad impuestos** (las puertas), y **memoria institucional entre proyectos**. Ver [`aislamiento-checkpoints-memoria.md`](aislamiento-checkpoints-memoria.md).

> **Nota sobre sub-agentes:** el aislamiento de contexto, los roles como actores separados y la orquestación en paralelo **ya son posibles** — Claude Code provee sub-agentes con contexto aislado y workflows. No es falta de capacidad, sino de **construcción**. Ver [`subagentes-y-entorno.md`](subagentes-y-entorno.md).

## ¿Basta con lo que tenemos?

**Para usar el estándar hoy en desarrollo real → sí, basta.** Las 17 secciones + las plantillas de capa 3 + el `CLAUDE.md` + la skill `analizar-proyecto` son un estándar completo y usable. El orquestador y los roles son **mejoras, no requisitos**.

**Para la visión completa (línea de montaje orquestada + memoria por señales) → falta construir, pero no falta capacidad.** Con los mecanismos que ya hay (sub-agentes + skills + archivos) se puede construir casi todo:

| Pendiente | ¿Alcanza con lo que hay? |
|---|---|
| 7 roles especializados | ✅ Sí — cada uno una skill/sub-agente |
| Orquestador con puertas/checkpoints | ✅ Sí — una skill/workflow |
| Aislamiento de contexto | ✅ Sí — sub-agentes |
| Grafo de dependencias | ✅ Sí — lógica del orquestador |
| Memoria por señales (dentro del proyecto) | ✅ Sí — archivos, o SQLite+FTS5 |
| Memoria **entre proyectos / semántica** | ⚠️ Aquí sí conviene algo extra (MCP o vector store) |

**En una frase:** para trabajar hoy, basta; para la visión completa no falta ninguna capacidad — falta **construir**. El único punto que querría una pieza adicional es la **memoria semántica entre proyectos** (un MCP / vector store).

## Resumen

- **Fuerte hoy**: spec-driven development, seguridad, datos, pruebas (con triangulación), trazabilidad, cumplimiento por construcción.
- **Falta**: el **orquestador** que convierta el flujo en una línea de montaje con puertas, y algunas **skills** de apoyo.
