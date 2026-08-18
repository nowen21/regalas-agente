# La compactación mata decisiones

> Amenaza: cuando el contexto del agente se **compacta** (se resume para caber en la ventana), las decisiones y su porqué se pierden. Qué hace el estándar hoy, cómo lo ataca la industria y dónde estamos.

## La amenaza

El chat y el contexto son finitos. Al llenarse, el sistema **compacta** (resume) lo viejo. Si una decisión y su razón vivían solo en esa conversación, **desaparecen**: la siguiente sesión (u otra persona) reinterpreta el negocio desde cero y aparecen contradicciones.

## Qué hace el estándar hoy — `✅` con un límite

Es una de sus razones de existir. `13` arranca con: *"El chat se pierde y el contexto se comprime; los archivos quedan."*

- **La especificación como memoria de largo plazo** — las decisiones viven en un archivo, no en el chat. `02`·F2
- **Documentar decisiones con su porqué** (registro de decisiones). `13`·DOC2
- **Cargar el contexto documentado antes de actuar** + **trazabilidad**. `02`·F1, `13`·DOC3

**Límite:** depende de que el agente **se acuerde de persistir**. Si la compactación pega **a mitad de una tarea, antes de escribir el archivo**, la decisión se pierde igual. No hay **captura automática** al momento de compactar.

## Cómo lo ataca la industria

> Conocimiento general (hasta ene-2026); los detalles de cada producto pueden cambiar.

1. **Memoria externa + recuperación (RAG):** sacar decisiones/hechos a un almacén durable y traer de vuelta lo relevante. ← lo que hace el estándar con los docs.
2. **Memoria jerárquica / paginación de contexto:** working memory corta + memoria larga externa; la compactación resume **preservando** lo crítico (estilo MemGPT/Letta).
3. **Registros de decisiones (ADR):** anotar cada decisión y su razón en un artefacto durable. ← `13`·DOC2.
4. **Scratchpad / state file + journaling:** el agente escribe su **estado** en un archivo que sobrevive la compactación y lo re-lee al reanudar.
5. **Ejecución durable / checkpoints en orquestadores:** el motor persiste el estado en **cada paso** (LangGraph checkpointers, estilo Temporal). ← conecta con el **SDD Orquestador**.
6. **Aislamiento por sub-agentes:** contexto acotado por rol; el hilo principal queda liviano y las decisiones viven en artefactos. ← **aislamiento de contexto**.
7. **Re-inyección tras compactar:** el harness vuelve a meter reglas/memoria en cada ventana (Claude Code re-inyecta `CLAUDE.md` y las memorias). Defensa pasiva.
8. **Grafos de conocimiento / herramientas de memoria** (Mem0, Zep, "engram"…): extraen decisiones a un grafo con relevancia/recencia.

## Dónde queda el estándar

| Defensa | ¿Estándar? |
|---|---|
| 1 Memoria externa (docs) | ✅ |
| 3 Registro de decisiones (ADR) | ✅ |
| 7 Re-inyección tras compactar | ✅ (del harness) |
| 4 Scratchpad/state + captura automática | ⏳ |
| 5 Checkpointing durable | ⏳ (orquestador) |
| 6 Aislamiento por sub-agentes | ⏳ |
| 2 Memoria jerárquica / 8 grafo de conocimiento | ⏳ (capa de memoria) |

**En una frase:** el estándar ataca la compactación **guardando decisiones en archivos**; la defensa fuerte —que no se pierda ni a mitad de tarea— exige el **orquestador con checkpoints** y el **aislamiento**, ya anotados como pendientes.

Relacionado: [`aislamiento-checkpoints-memoria.md`](aislamiento-checkpoints-memoria.md), [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md).
