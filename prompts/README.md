# `prompts/` — lo que el usuario pidió, con sus palabras

Textos que el usuario escribe para pedir una regla, un cambio o un trabajo, guardados **tal como los redactó**. No son norma (`20·M13`): la norma vive en `base/`. Son el origen, y sirven para comprobar después si lo que quedó escrito dice lo que se pidió.

**Nomenclatura:** `<tema>.md`, en minúsculas y con guiones.

Un prompt **no se corrige ni se reescribe** cuando la regla que salió de él quedó redactada de otro modo. Si la regla terminó diciendo algo distinto, eso se explica en el `CHANGELOG.md` y en el histórico de la sesión, no editando el pedido.

## Índice

| Prompt | Qué pidió |
|---|---|
| [regla-reglas-proyecto.md](regla-reglas-proyecto.md) | Que ninguna regla de `reglas-proyecto` exista sin una regla del agente que la respalde. Quedó en [`20·M16`](../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md). |

## Rescatado del histórico

Pedidos que quedaron dichos en las sesiones y que sirven como regla. Cada ficha trae la cita literal y de qué sesión sale. **Cuáles ya son regla y cuáles no, se revisa aparte**: esto es el material, no el veredicto.

### Cómo se escribe

| Prompt | Qué pidió |
|---|---|
| [redaccion-clara-para-quien-no-sabe.md](redaccion-clara-para-quien-no-sabe.md) | Que todo lo escrito lo entienda quien no sabe del tema, e idealmente un niño. |
| [menos-es-mas.md](menos-es-mas.md) | Explicaciones cortas: menos es más. |
| [sin-marcadores-de-ia.md](sin-marcadores-de-ia.md) | Que ningún documento lleve las marcas que delatan generación automática. |
| [espanol-colombiano-correcto.md](espanol-colombiano-correcto.md) | Español colombiano, con ortografía, gramática y sintaxis correctas. |

### Cómo se trabaja con el usuario

| Prompt | Qué pidió |
|---|---|
| [una-pregunta-no-es-una-instruccion.md](una-pregunta-no-es-una-instruccion.md) | Si pregunta, se responde; no se edita nada. |
| [preguntas-en-el-chat-no-en-formulario.md](preguntas-en-el-chat-no-en-formulario.md) | Las preguntas se entregan en el chat para analizarlas, sin obligar a responder. |
| [corregir-lo-que-esta-mal-sin-preguntar.md](corregir-lo-que-esta-mal-sin-preguntar.md) | Lo que el agente detecta mal, lo corrige. |
| [trabajo-confinado-a-la-carpeta.md](trabajo-confinado-a-la-carpeta.md) | Mientras se trabaja un tema, todo queda dentro de su carpeta. |
| [no-tocar-lo-de-otras-sesiones.md](no-tocar-lo-de-otras-sesiones.md) | Se versiona solo lo que hizo esta sesión. |

### Memoria e histórico

| Prompt | Qué pidió |
|---|---|
| [historico-de-cada-sesion.md](historico-de-cada-sesion.md) | Todo lo hablado queda escrito, literal y con fecha, hora, minutos y segundos. |
| [la-sesion-se-nombra-al-abrirla.md](la-sesion-se-nombra-al-abrirla.md) | Que la sesión pida su nombre y ese nombre se vea también en la pestaña. |
| [memoria-en-el-repo.md](memoria-en-el-repo.md) | La memoria vive en `historico-chat/memory/`, no en el equipo. |

### Instalación y actualización

| Prompt | Qué pidió |
|---|---|
| [toda-herramienta-se-replica-sola.md](toda-herramienta-se-replica-sola.md) | Lo que se construya llega solo a cualquier proyecto, sin trabajo manual. |
| [claude-md-es-el-setup-del-agente.md](claude-md-es-el-setup-del-agente.md) | El agente se instala y se configura solo, leyendo su `CLAUDE.md`. |
| [checklist-de-instalacion-incompleta.md](checklist-de-instalacion-incompleta.md) | Mientras falte algo, el agente avisa qué es y queda marcado como incompleto. |
| [stack-de-instalacion-y-actualizaciones.md](stack-de-instalacion-y-actualizaciones.md) | El proyecto registra qué versión usa y se le avisa solo lo que debe aplicar. |
| [la-instalacion-no-borra-lo-que-ya-existe.md](la-instalacion-no-borra-lo-que-ya-existe.md) | Instalar de nuevo no destruye lo que el proyecto ya tiene. |

### Cómo se escriben y se auditan las reglas

| Prompt | Qué pidió |
|---|---|
| [la-regla-en-reglas-la-explicacion-en-base.md](la-regla-en-reglas-la-explicacion-en-base.md) | En `reglas/` va la regla; la explicación va en `base.md`. |
| [cada-cita-lleva-su-link.md](cada-cita-lleva-su-link.md) | Toda regla citada se enlaza al sitio exacto. |
| [checklist-dentro-de-cada-regla.md](checklist-dentro-de-cada-regla.md) | El resultado del checklist queda dentro de la regla; el instrumento, aparte. |
| [analisis-de-reglas-candidatas.md](analisis-de-reglas-candidatas.md) | El formato para sacar reglas candidatas de lo ya trabajado. |
| [analisis-de-cumplimiento-de-reglas.md](analisis-de-cumplimiento-de-reglas.md) | El formato para auditar si las reglas cumplen el estándar. |
| [el-informe-no-se-corrige-se-enlaza.md](el-informe-no-se-corrige-se-enlaza.md) | Un informe no se reescribe: se enlaza dónde quedó corregido. |

### Documentación del propio agente

| Prompt | Qué pidió |
|---|---|
| [documentacion-de-cada-archivo-de-codigo.md](documentacion-de-cada-archivo-de-codigo.md) | Un documento por archivo de código, en lenguaje claro y sin tecnicismos. |
| [mapa-del-sitio-siempre-al-dia.md](mapa-del-sitio-siempre-al-dia.md) | El mapa del sitio refleja siempre la estructura real. |
| [lo-que-pueda-hacer-un-script-no-lo-hace-la-ia.md](lo-que-pueda-hacer-un-script-no-lo-hace-la-ia.md) | Lo que se pueda resolver con reglas y validaciones no depende de la IA. |
