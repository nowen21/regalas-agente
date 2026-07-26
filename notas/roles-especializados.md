# Roles especializados (línea de montaje del SDD Orchestrator)

> Diseño de los roles que compondrían el orquestador. Cada rol es una **estación** de la línea de montaje: recibe algo, produce algo, y su salida debe **pasar una puerta** antes de avanzar al siguiente. Cada rol aplica las reglas base que le tocan.

## La línea de montaje

```
1. EXPLORER  →  2. PROPOSER  →  3. SPEC WRITER  →  4. DESIGNER  →  5. TASK PLANNER  →  6. IMPLEMENTER  →  7. VERIFIER
   (lee)          (define qué)     (requisitos)       (arquitectura)   (divide trabajo)     (escribe código)    (valida)
      └── puerta ──┘  └── puerta ──┘   └── puerta ────┘  └── puerta ───┘   └── puerta ──────┘   └── puerta ──────┘
```

Regla de oro: **nada avanza a la estación siguiente si no pasa la puerta de la actual.**

## Los 7 roles

### 1. Explorer — lee el código
- **Hace:** entiende lo que ya existe (código, datos, dependencias, documentación). Solo lectura.
- **Entrada:** el proyecto + la solicitud del usuario.
- **Salida:** inventario de lo relevante (qué hay, dónde, cómo funciona).
- **Reglas base:** `02` F1 (cargar contexto), `01` C2 (verificar, no inventar). Es la skill `analizar-proyecto`.
- **Puerta:** ¿se entendió el contexto y no quedan supuestos sin verificar?

### 2. Proposer — define QUÉ se va a hacer
- **Hace:** traduce la solicitud en un alcance concreto (qué se construye y qué no). Propone, no decide.
- **Entrada:** solicitud + inventario del Explorer.
- **Salida:** propuesta de alcance, con opciones si hay ambigüedad.
- **Reglas base:** `01` C4 (no decidir solo), `01` C7 (preguntar ante dos lecturas).
- **Puerta:** ¿el usuario aprobó el alcance?

### 3. Spec Writer — escribe los requisitos
- **Hace:** redacta la especificación: reglas de negocio, modelo de datos, criterios de aceptación, permisos, pruebas esperadas.
- **Entrada:** alcance aprobado.
- **Salida:** la **spec** (el contrato).
- **Reglas base:** `02` F2 (sin spec no hay código), `16` (marco normativo si aplica).
- **Puerta:** ¿la spec está aprobada por el usuario?

### 4. Designer — define la arquitectura
- **Hace:** decide cómo se construye: esquema de datos, servicios, dónde vive cada cosa, decisiones técnicas y sus porqués.
- **Entrada:** spec aprobada.
- **Salida:** diseño técnico + decisiones documentadas.
- **Reglas base:** `03` (datos), `14` (estructura/nomenclatura), `04`/`06` (seguridad/rendimiento por diseño), `13` DOC2 (decisiones con porqué).
- **Puerta:** ¿el diseño cumple la spec y respeta las convenciones?

### 5. Task Planner — divide el trabajo
- **Hace:** parte el diseño en tareas/fases ejecutables, cada una con su **plan de pruebas**.
- **Entrada:** diseño.
- **Salida:** plan de trabajo + plan de pruebas por fase.
- **Reglas base:** `02` F3 (plan aprobado = ejecución continua), `02` F4 (todo plan lleva pruebas), `08` T7 (derivar los casos).
- **Puerta:** ¿el usuario aprobó el plan y su plan de pruebas?

### 6. Implementer — escribe el código
- **Hace:** implementa las tareas del plan, con su código y sus pruebas.
- **Entrada:** plan aprobado.
- **Salida:** código + pruebas escritas.
- **Reglas base:** `07` (calidad), `03`/`04`/`05`/`06` (datos, seguridad, errores, rendimiento), `09` (git bajo pedido).
- **Puerta:** ¿se implementó todo lo del plan, sin salirse del alcance?

### 7. Verifier — valida la calidad
- **Hace:** corre las pruebas, triangula resultados, revisa calidad y comprueba la trazabilidad spec → implementación.
- **Entrada:** código + pruebas.
- **Salida:** veredicto (pasa / no pasa) con evidencia.
- **Reglas base:** `08` (pruebas) + `08` T7 (triangulación), `13` DOC3 (trazabilidad), `07` (calidad), `04` (seguridad).
- **Puerta final:** ¿pruebas verdes + trazabilidad sin faltantes? Solo entonces se cierra.

## Roles adicionales (más allá de los 7)

Los 7 cubren el flujo completo. Para un set serio se suman:

**Esencial (el director):**
- **Orchestrator / Coordinador** — no es un obrero; **maneja la línea**: llama a cada rol en orden, controla las puertas/checkpoints, persiste el estado. Sin él, los 7 existen pero nadie los coordina. (pendiente `sdd-orchestrator`)

**Alto valor:**
- **Reviewer / Crítico** — revisión **adversarial e independiente**: intenta *refutar*, busca bugs y agujeros de seguridad. Distinto del Verifier (que comprueba **conformidad con la spec**); el Crítico pregunta "¿qué puede salir mal?".

**Opcionales (se pueden plegar):**
- **Documenter / Scribe** — mantiene la memoria por señales al día; puede ir integrado al flujo.
- **Researcher** — mira **hacia afuera**: docs, mejores prácticas, evaluar librerías (el Explorer mira adentro).
- **Deployer** — pasos de despliegue (etapa 11); es una etapa más que un rol permanente.

**Se pliegan en existentes:** seguridad → Reviewer/Verifier · debugger/refactorer → Implementer.

**Set mínimo serio = los 7 + Orchestrator + Reviewer/Crítico.** Los 7 hacen el trabajo, el Orchestrator los dirige, el Crítico da la segunda mirada independiente.

## Cómo se relaciona con lo pendiente

- Estos roles son **skills** que hoy no existen (salvo el Explorer ≈ `analizar-proyecto`).
- El **SDD Orchestrator** es el coordinador que los llama en orden y controla cada puerta. Ver [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md).
- Ejecutarlos **en paralelo** (varios roles a la vez) depende de las capacidades de sub-agentes de Claude Code; en secuencia, es el mismo agente cambiando de rol en cada estación.
