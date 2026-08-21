# 2026-08-20 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-20-sesion-5.md](../../2026-08-20-sesion-5.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** 2026-08-19 · sesión 4 · análisis de `notas/estructura.md` (la pregunta continúa esa comparación, bloque `llm/`)

---

## Hallazgos de esta sesión

### H-1 · Cimiento no necesita la capa `llm/` (backends + enrutador) de `notas/estructura.md`

- **Qué pasó:** Se comparó el bloque `llm/` del documento (`LLMBackend` abstracto, backends Ollama/OpenAI/Anthropic, `router.py` con selección por tarea y *fallback* en cascada) contra lo que tiene Cimiento.
- **Por qué importa:** Es una pregunta que vuelve cada vez que se lee ese documento; sin respuesta escrita, alguien podría construir una capa de backends para un solo caso, que es lo que [adaptadores/contrato.md](../../../adaptadores/contrato.md) prohíbe.
- **Qué lo soluciona:** No abre trabajo. Cimiento tiene la **interfaz** (el contrato: cinco capacidades, sin nombrar herramienta) y **una** implementación (`adaptadores/claude-code/`). No tiene backends alternos ni enrutador porque no llama a ningún modelo: lo llama la herramienta, y el modelo lo escoge ella.
- **Qué se decidió:** No se necesita hoy. Se necesitará el día que exista un segundo agente real que quiera usar el estándar; el costo ya está medido en el contrato (8 programas a traducir, `validadores/` y `base/` intactos).
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** este resumen; la justificación de fondo ya está en [adaptadores/contrato.md](../../../adaptadores/contrato.md) («No soporta un segundo agente, y no debe»)
- **Nace en:** 2026-08-20 · sesión 5
- **Cerrado en:** 2026-08-20 · sesión 5
- **Con qué se retoma:** —

### H-2 · Cimiento no necesita la capa `tools/` (Tool ABC, registro, implementaciones)

- **Qué pasó:** Se comparó el bloque `tools/` del documento (`Tool` con schema/risk_level/run, `registry.py` con descubrimiento y filtrado por permisos, implementaciones SQL/HTTP/archivo/vector) contra lo que tiene Cimiento.
- **Por qué importa:** Misma trampa que `llm/`: construir manos para un agente que ya las trae.
- **Qué lo soluciona:** No abre trabajo. Las herramientas las da Claude Code. Cimiento tiene el nivel de riesgo como texto ([base/00-identidad-y-rol/acciones-y-riesgo.md](../../../base/00-identidad-y-rol/acciones-y-riesgo.md), por clase de acción y no por herramienta), el registro a mano ([validar.py](../../../validadores/validar.py) + `reglas-validables.md`) y los permisos en `.claude/settings.json` más `S9`/`S10`/`N8` como reglas.
- **Qué se decidió:** No se necesita hoy. Único punto a revisar si llega un segundo agente vía MCP: los validadores no declaran schema; envolverlos sería trabajo del adaptador, no de `base/`.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** este resumen
- **Nace en:** 2026-08-20 · sesión 5
- **Cerrado en:** 2026-08-20 · sesión 5
- **Con qué se retoma:** —

### H-3 · La memoria semántica sí existe: la respuesta sobre `memory/` fue errada

- **Qué pasó:** Al comparar el bloque `memory/` del documento se respondió que Cimiento no tiene recuperación vectorial. Sí la tiene: [memoria/](../../../memoria/) — `senales.db` (SQLite + FTS5, 975 KB), `semantica.py` (`model2vec` local, opt-in, EP-006 · HU-004) y `parecidas.py`. Episódica (`historico-chat/`), compactación (resúmenes) y semántica están cubiertas; solo la ventana de contexto se delega en la herramienta.
- **Por qué importa:** La respuesta errada iba camino de un pendiente por algo construido el 2026-08-06. Es la misma falla de la S-001: el estándar no se mira a sí mismo antes de afirmar.
- **Qué lo soluciona:** No abre trabajo. Corregido en el chat y registrado en la señal S-014.
- **Qué se decidió:** `memory/` del documento **no se necesita**: ya está, en su forma, y la parte vectorial desde hace dos semanas.
- **Estado:** resuelto acá
- **Responde a:** EP-006 · HU-004 (búsqueda por significado)
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal S-014 en [documentacion/senales.md](../../../documentacion/senales.md)
- **Nace en:** 2026-08-20 · sesión 5
- **Cerrado en:** 2026-08-20 · sesión 5
- **Con qué se retoma:** —

### H-4 · La política de carga del contexto ya existe; no se abre pendiente

- **Qué pasó:** Se iba a abrir un pendiente «política de carga del contexto al abrir sesión» y se encontró que [validadores/cargador.py](../../../validadores/cargador.py) ya la tiene escrita: `00-*` y `01-*` van literales y sin sellos; del resto va solo el índice con la orden de leer antes de tocar el tema; un techo de 90 KB vigilado por `pruebas.py` (CP-004).
- **Por qué importa:** Medido hoy: 53,9 KB de reglas + 14,1 de índice = **68 de 90 KB**; con memoria (6,6) e índice del histórico (5,7), 84 KB. El núcleo creció de 52 a 54 KB en un día. El techo avisa cuando se corre la suite, no al arrancar.
- **Qué lo soluciona:** No abre trabajo hoy (`20·M12`). Lo único no escrito es qué se recorta el día que `00`+`01` solos pasen el techo; esa decisión se toma cuando la prueba salte, que es lo que está diseñada para provocar.
- **Qué se decidió:** No se abre pendiente. El número que vigilar es 68/90.
- **Estado:** resuelto acá
- **Responde a:** EP-005 · HU-009 (lo que rige cada frase llega puesto)
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal S-014 (la medición)
- **Nace en:** 2026-08-20 · sesión 5
- **Cerrado en:** 2026-08-20 · sesión 5
- **Con qué se retoma:** —

### H-5 · Un `senales.db` vacío quedó en `documentacion/` por abrirlo con `sqlite3.connect`

- **Qué pasó:** Al verificar la base de señales se abrió `documentacion/senales.db`, que no existía; `sqlite3.connect` lo creó vacío. La real es `memoria/senales.db`. El borrado lo bloqueó dos veces el clasificador de la herramienta.
- **Por qué importa:** Residuo de 0 bytes en una ruta ignorada por git: no rompe nada, pero confunde a quien busque la base.
- **Qué lo soluciona:** Borrarlo a mano: `Remove-Item documentacion\senales.db`.
- **Qué se decidió:** Lo borra el usuario; el agente no insiste contra el bloqueo.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** 1 de 1 · es un comando
- **Dónde queda:** señal S-015 (el gotcha)
- **Nace en:** 2026-08-20 · sesión 5
- **Cerrado en:** —
- **Con qué se retoma:** ¿ya se borró `documentacion/senales.db`?

### H-6 · Dos bloques de `estructura.md` sí hacen falta pronto: el portero y la traza

- **Qué pasó:** De los diez bloques del árbol, cinco se compararon (H-1 a H-4 y `core/` de ayer). De lo que falta, dos se necesitan en un futuro cercano: `policy/sanitizer` (nada marca lo externo como dato; `C27` es solo texto) y `observability/tracer` (se guarda qué se dijo y cuánto costó, no qué se ejecutó). El usuario decidió: *«la idea no es que asuma que solo yo lo veo»*, y después *«listo hágalo»*.
- **Por qué importa:** Una guarda de seguridad que se instala después del primer incidente llegó tarde; y con nueve proyectos, reconstruir «cómo pasó» va a hacer falta en semanas.
- **Qué lo soluciona:** Bajó por la cadena con el andamio.
  **EP-005 · HU-015 — Lo que llega de afuera llega marcado**
  - **Como** quien opera el agente en cualquier proyecto heredero
  - **Quiero** que todo texto que entre por una herramienta externa llegue marcado como dato, con su origen
  - **Para** que una instrucción escondida no se confunda con una orden mía y quede rastro
  - **Contexto:** `C27` existe sin programa; el evento «al devolver una herramienta» acepta contexto adicional (documentación oficial). Pendiente 72.
  **EP-005 · HU-016 — La traza de la sesión, paso a paso**
  - **Como** quien revisa qué hizo el agente en una sesión
  - **Quiero** la línea de tiempo: hora, herramienta, entrada, duración, error
  - **Para** reconstruir cómo pasó algo sin leer la transcripción entera
  - **Contexto:** la transcripción interna tiene `tool_use`/`tool_result` con hora; nadie los lee. Lector a demanda, sin tocar proyectos. Pendiente 73.
- **Qué se decidió:** Los dos se construyeron el mismo día, con los planes aprobados por el usuario («si»). El portero quedó instalado en los 9 proyectos y verificado en vivo; la traza estrenó con esta misma sesión: 191 pasos, 9 errores, 0,69 s. Versión 28.0.0.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:**
  1. [EP-005 · HU-015](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-015-lo-que-llega-de-afuera-llega-marcado/HU-015-lo-que-llega-de-afuera-llega-marcado.md) — primero, porque es seguridad.
  2. [EP-005 · HU-016](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-016-la-traza-de-la-sesion-paso-a-paso/HU-016-la-traza-de-la-sesion-paso-a-paso.md) — después; no depende de la anterior.
- **Orden de resolución:** 1 de 2 abiertos (H-5 es un comando del usuario)
- **Dónde queda:** [pendientes/hecho/lo-que-llega-de-afuera-llega-marcado.md](../../../pendientes/hecho/lo-que-llega-de-afuera-llega-marcado.md) y [pendientes/hecho/la-sesion-tiene-su-traza.md](../../../pendientes/hecho/la-sesion-tiene-su-traza.md), con sus fases A cerradas (Cumple las dos), las señales S-016 y S-017, y la entrada 28.0.0 del CHANGELOG
- **Nace en:** 2026-08-20 · sesión 5
- **Cerrado en:** 2026-08-20 · sesión 5
- **Con qué se retoma:** — (solo falta el commit, que autoriza el usuario)

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-6 (72 y 73) · ☐ H-5 (no es pendiente, es un comando del usuario) |
| Toda historia disparada está escrita en su épica | ☑ (HU-015 y HU-016 en EP-005) |
| Lo que se hizo está aprobado y guardado | ☐ (todo aprobado y construido; falta el commit, que autoriza el usuario) |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
