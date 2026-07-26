# Memoria por señales

> Diseño concreto de la memoria institucional: en vez de "documentá decisiones" (vago), un **catálogo de señales tipadas**. Una **señal** es un pedazo de conocimiento de alto valor que **no se puede recuperar del código**. Se guardan **señales, no la conversación**.
>
> **Estado:** ✅ **versión con archivos implementada** — plantilla `plantillas/senales.md` + regla base `13`·DOC5 (opt-in). Pendiente: la recuperación (SQLite+FTS5) y la capa entre proyectos (MCP).

## Esquema base de una señal

Cada señal se registra con la misma estructura:

- **What** — qué se decidió o hizo.
- **Why** — por qué (la razón que no está en el código).
- **Where** — dónde, con enlace `archivo:línea`.
- **Learned** — la lección para la próxima vez.

> El estándar hoy cubre `what/why/where` de las decisiones (`13`·DOC2). **`learned`** y los tipos/metadatos de abajo son la extensión.

## Tipos de señal

| Tipo | Qué captura | Estado en el estándar |
|---|---|---|
| **Decisión** | Qué se eligió y por qué | ✅ `13`·DOC2 |
| **Error resuelto** | Un problema y cómo se solucionó (para no re-resolverlo) | ⏳ nuevo |
| **Patrón / anti-patrón** | Solución reutilizable, o algo a evitar | ⚠️ parcial |
| **Aprendizaje** | La lección ("esto falló por X; la próxima, evitar Y") | ⏳ nuevo |
| **Alternativa descartada** | "Probamos X, no sirvió por Z" (el **no**, para no reintentarlo) | ⏳ nuevo |
| **Supuesto** | Lo que se dio por cierto sin confirmar (riesgo si es falso) | ⏳ nuevo |
| **Restricción** | Límite duro (legal, técnico, negocio) que no se cruza | ⚠️ parcial (`16`) |
| **Pregunta abierta** | Lo pendiente de aclarar | ⏳ nuevo |
| **Trampa / gotcha** | Peculiaridad no obvia del entorno ("este motor tiene el bug X") | ⏳ nuevo |
| **Deuda técnica** | Lo que se sabe que hay que revisar después | ⏳ nuevo |

## Metadatos por señal (además de what/why/where/learned)

| Campo | Para qué |
|---|---|
| **When / Who** | Cuándo y quién (o qué rol) la generó → auditoría y contexto. |
| **Scope** | ¿aplica al módulo, al proyecto o a **toda la organización**? → clave para la memoria **entre proyectos**. |
| **Status** | `activa / reemplazada / revertida`. Las decisiones cambian; se marca la vieja y se enlaza a la nueva, **sin borrarla**. |
| **Relaciones** | `reemplaza a`, `causada por`, `relacionada con` → las señales forman un **grafo**, no una lista. |
| **Evidence** | Enlace al test/commit que la prueba. |
| **Tags / trigger** | Cuándo debe **resurgir** esta señal (palabras clave, contexto). |

## Ciclo de vida y recuperación

Lo que hace que la memoria **funcione con el tiempo**, no que solo se archive:

- **Supersesión con rastro:** una decisión revertida no se borra; se marca `reemplazada` y apunta a la que la sustituye. *(Ya lo pedían las reglas de origen: "nunca borrar la decisión anterior sin dejar rastro".)*
- **Verificar antes de confiar:** una señal puede quedar **obsoleta**; antes de aplicarla, confirmar que sigue vigente (si nombra un archivo/función, que aún exista). Coincide con `01`·C2 (no inventar, verificar).
- **Recencia + relevancia:** traer la señal correcta en el momento correcto, no todas. Sin recuperación, la memoria que nunca se consulta es inútil.
- **Deduplicar / fusionar:** no guardar la misma señal dos veces; actualizar la existente.

## Lo más valioso a agregar (prioridad)

Tres cambios convierten el modelo base en una memoria seria:

1. **Status + supersesión** — las decisiones evolucionan sin perder historia.
2. **Scope** — módulo / proyecto / organización → habilita la memoria institucional **entre proyectos**.
3. **Trigger / tags para recuperación** — que la señal **resurja** cuando es relevante, no que solo se archive.

## Dónde se guardan las señales: archivos vs MCP

El estándar debe quedar **agnóstico al backend de memoria**: define **qué** son las señales; el **dónde** se guardan es implementación (capa 3).

Hay tres niveles, de más simple a más potente:

| | Archivos markdown | SQLite + FTS5 | Servidor de memoria por MCP |
|---|---|---|---|
| Simplicidad | ✅ Alta | ✅ Alta (un archivo `.db`) | ⚠️ Agrega infraestructura |
| Versionado / transparencia | ✅ (git) | ⚠️ Binario, menos legible en git | ⚠️ Fuera del repo |
| Recuperación | ❌ Manual | ✅ Búsqueda por palabra + ranking (BM25) | ✅ Semántica (embeddings) |
| Memoria **entre proyectos** | ❌ Difícil | ⚠️ Posible (db compartida) | ✅ Natural |
| Dependencia | ✅ Ninguna | ✅ Ninguna (SQLite incluido) | ⚠️ Un servicio más |

**FTS5** = búsqueda de texto completo de SQLite: indexa las señales y las busca por palabra/frase con ranking, **sin servidor**. Es el punto medio: recuperación real, cero dependencias, un solo archivo. Su límite: busca por **léxico** (palabras), no por **significado**; para "traeme señales parecidas aunque usen otras palabras" hace falta búsqueda **semántica** (embeddings) → ahí sí un MCP.

**Recomendación (escalar según necesidad):**
- **Dentro de un proyecto, poco volumen** → **archivos markdown** (lo que ya hace el estándar).
- **Dentro de un proyecto, con búsqueda** → **SQLite + FTS5** (recuperación por palabra + ranking, local y sin dependencias).
- **Entre proyectos / búsqueda semántica** → **servidor de memoria por MCP** (Mem0, Zep, "engram", o propio).

> MCP = Model Context Protocol: el mecanismo para conectarle al agente herramientas o servidores externos. El estándar no lo exige; es una opción de backend para la memoria entre proyectos.

## Dónde vive la memoria: por proyecto vs central (el `scope`)

Con **muchos proyectos**, el campo `scope` de cada señal permite **una sola memoria central** en vez de una por proyecto. Cada señal va a "su caja" (el proyecto) o a "la repisa" (la organización):

```
        ┌──── REPISA COMPARTIDA (scope = organizacion) ────┐
        │  lo que sirve para CUALQUIER proyecto            │
        └──────────────────────────────────────────────────┘
   ┌── Laravel ──┐   ┌── Python ──┐   ┌── Spring ──┐
   │ solo tienda │   │ solo pipe  │   │ solo API   │   (scope = proyecto:X)
   └─────────────┘   └────────────┘   └────────────┘
```

**En las cajas (scope=proyecto):** "Producto usa borrado lógico" (Laravel), "el pipeline corre a las 2am" (Python), "OrderService usa bloqueo optimista" (Spring). No le sirve a los otros.

**En la repisa (scope=organizacion):** "nunca loguear tarjetas completas — nos marcó una auditoría", "el servidor de prod tiene 2GB, no cargar datasets enormes", "este cliente redondea a 2 decimales hacia arriba", "commits en español".

**El momento clave:** una lección aprendida en el proyecto Laravel (subir a la repisa) **aparece** al arrancar el proyecto Python semanas después → **no repetís el error**, aunque sea otro stack.

**Por qué funciona entre stacks distintos:** la repisa **no guarda código** — guarda **lecciones, decisiones, reglas del cliente y preferencias**, que **no dependen del lenguaje**. "No loguear tarjetas" vale igual en Laravel, Python o Spring.

**Sin repisa (archivo por proyecto):** la lección queda atrapada en un proyecto; los otros **tropiezan con la misma piedra**.

Por eso, para muchos proyectos, **una DB central con `scope`** (no una por proyecto) es lo que habilita la memoria **entre proyectos**. Coincide con el agente centralizado: el agente es único, su memoria también.

## Memoria vs reglas (no se reemplazan)

Fácil de confundir, pero son cosas distintas que **conviven**:

| | `reglas-proyecto.md` | Memoria (señales) |
|---|---|---|
| **Qué es** | Reglas propias del proyecto | Historia: decisiones, errores resueltos, gotchas, aprendizajes |
| **Naturaleza** | Obligación ("siempre hacé X") | Conocimiento ("decidimos X porque Y") |
| **Cuándo aplica** | **Siempre** — cargada en cada sesión | **Cuando es relevante** — se busca y se trae |
| **Tipo** | Prescriptiva (manda) | Descriptiva (informa) |

**Por qué la memoria NO reemplaza a las reglas:** una regla debe aplicarse **siempre**; si se vuelve "buscable" (solo aparece si la consulta coincide), una regla no recuperada es una regla **incumplida** (ej. "todo endpoint va con HTTPS" no puede depender de que alguien busque "https"). La memoria es distinto: traer solo la porción relevante está bien; no recuperar una señal vieja no es grave.

```
Siempre cargado (obligaciones):  base/00–16 + .agente/reglas-proyecto.md
Se consulta cuando sirve (saber): memoria de señales (archivo hoy, buscable mañana)
```

Una dice "hacelo así"; la otra dice "ojo, esto ya lo vivimos". Se necesitan las dos.

## Relación con el resto

- Es el **diseño concreto** de la "memoria institucional" (hoy `✅` dentro del proyecto, `⏳` entre proyectos) — ver [`aislamiento-checkpoints-memoria.md`](aislamiento-checkpoints-memoria.md).
- Ataca "la compactación mata decisiones" guardando las señales fuera del contexto — ver [`compactacion-mata-decisiones.md`](compactacion-mata-decisiones.md).
- La **captura automática** de señales (no depender de que el agente se acuerde) es trabajo del **orquestador con checkpoints** — ver [`orquestador-y-triangulacion.md`](orquestador-y-triangulacion.md).
