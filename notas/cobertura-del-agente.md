# Cobertura del estándar: qué cumple y qué no

> Estado a la fecha. "El agente" = Claude Code siguiendo el estándar. Marca ✅ lo que ya está en el estándar, ⏳ lo pendiente.

## ✅ Lo que cumple (ya está en el estándar)

### Núcleo y convenciones base (`base/00`–`16`)

- ✅ **Seguridad crítica** (núcleo blindado): validación previa, git bajo pedido, no romper cosas para pasar, proteger datos reales, operaciones masivas con preview, secretos nunca expuestos. — `00`
- ✅ **Conducta**: avisar antes de tocar, no inventar, quedarse en el alcance, no decidir solo, responder corto. — `01`
- ✅ **Spec-driven development (SDD)**: sin especificación acordada no hay código; la especificación es el contrato. — `02` · F2
- ✅ **Diseño de datos**: normalización, auditoría, migraciones reversibles y retrocompatibles, catálogos, cero-hardcode. — `03`
- ✅ **Seguridad de aplicación**: authz, validación de entrada, inyección, secretos, CSRF, archivos sensibles. — `04`
- ✅ **Errores y logging**: no tragar errores, fallar controlado, mensajes en dos niveles, no loguear secretos. — `05`
- ✅ **Rendimiento**: N+1, paginación, índices, caché, trabajo en segundo plano. — `06`
- ✅ **Calidad de código**: legibilidad, nombres, funciones pequeñas, DRY, lint. — `07`
- ✅ **Pruebas**: qué probar, aislamiento, no-flaky, cobertura con criterio. — `08`
- ✅ **Triangulación de pruebas + corner cases**: derivar los casos con método (frontera, equivalencia, tablas de decisión, negativos) y triangular el resultado esperado desde fuentes independientes. — `08` · T7
- ✅ **Trazabilidad especificación → implementación**: checklist ítem por ítem antes de cerrar. — `13` · DOC3
- ✅ **Git, dependencias, configuración/entornos, privacidad, documentación, estructura/nomenclatura**. — `09`–`14`
- ✅ **Concurrencia/idempotencia** (`03`·D6), **CI/CD gate** (`09`·G6), **UI/UX** (`17`, opt-in) y **backup antes de operación irreversible** (`00`·N4) — agregados tras la auditoría del estándar (3 sub-agentes en paralelo).
- ✅ **Memoria institucional (dentro del proyecto)**: la especificación como memoria de largo plazo, decisiones con porqué, carga de contexto, trazabilidad. — `02`·F1/F2/F6, `13`
- ✅ **Memoria por señales (archivos)**: log de señales tipadas (`13`·DOC5 + `plantillas/senales.md`) con what/why/where/learned.
- ✅ **Memoria buscable central (SQLite+FTS5) — OPERATIVA**: helper `memoria/memoria.py` (init/add/search/supersede) + skill `usar-memoria` + base central con `scope` (una sola para todos los proyectos; las lecciones `organizacion` viajan entre proyectos). Ver [`memoria-buscable-fts5.md`](memoria-buscable-fts5.md). ⏳ Solo queda la búsqueda **semántica** (embeddings/MCP); la léxica ya está.
- ✅ **Registros inmutables** (patrón opt-in). — `15`
- ✅ **Cumplimiento normativo por construcción** (opt-in): OWASP, ISO 25010, y marco legal declarado por proyecto. — `16`

### Capa 3 y herramientas

- ✅ **Plantillas de proyecto**: `CLAUDE.md`, `stack`, `dominio`, `mapeo-nombres`, `marco-normativo`.
- ✅ **Skill `analizar-proyecto`**: diagnóstico de proyecto existente (qué hay / qué falta / qué sigue + estrategia de pruebas + tecnologías).

## ⏳ Lo que NO cumple todavía (pendiente)

- ✅ **SDD Orquestador** (línea de montaje con puertas): `skills/sdd-orchestrator/` — dirige las estaciones, controla las puertas, usa el grafo y persiste el estado. Ver [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md).
- ⚠️ **Orquestación con sub-agentes en paralelo**: el Orquestador la dispone; la ejecución paralela real usa los sub-agentes/workflows del entorno (ya disponibles).
- ✅ **Skill `cerrar-fase`** (rol Verificador): `skills/cerrar-fase/` — pruebas + triangulación + trazabilidad antes de cerrar.
- ✅ **Skill `generar-spec-modulo`** (rol Escritor de especificación): `skills/generar-spec-modulo/` — redacta la especificación guiando la plantilla.
- ✅ **Skill `revisar-critico`** (rol Crítico/Crítico): `skills/revisar-critico/` — revisión adversarial (bugs, seguridad, casos no anticipados).
- ✅ **Skill `planificar-tareas`** (rol Planificador de tareas): `skills/planificar-tareas/` — divide el trabajo con grafo de dependencias (orden topológico + paralelizables) y plan de pruebas.
- ✅ **Skills `proponer-alcance` (Proponente), `disenar-arquitectura` (Diseñador), `implementar` (Implementador)**: completan los **7 roles obreros** de la línea de montaje.
- ✅ **Skill `generar-casos-prueba`**: `skills/generar-casos-prueba/` — deriva la matriz de casos y triangula el esperado (operacionaliza `08`·T7).
- ✅ **Plantilla genérica de especificación de módulo** (agnóstica): `plantillas/plantilla-especificacion-modulo.md`.
- ✅ **Roles especializados**: los 7 obreros + Crítico/Crítico + Orquestador existen como skills en `skills/`. Ver [`roles-especializados.md`](roles-especializados.md).
- ✅ **Grafo de dependencias entre tareas**: el Planificador de tareas lo produce y el Orquestador lo ejecuta (orden topológico + paralelizables).
- ✅ **Checkpoints de calidad impuestos** (las puertas): el Orquestador los controla. ⚠️ **Aislamiento de contexto** (cada rol como sub-agente): dispuesto por el Orquestador, ejecutado por los sub-agentes del entorno. ⏳ **Memoria institucional entre proyectos** (semántica / MCP). Ver [`aislamiento-checkpoints-memoria.md`](aislamiento-checkpoints-memoria.md).

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
- **Falta poco**: la skill `generar-casos-prueba`, la **ejecución paralela real** (usa sub-agentes del entorno) y la **memoria semántica entre proyectos** (MCP/vector). El orquestador y los 8 roles ya están.
