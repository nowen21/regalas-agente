# Hecho · El veredicto de la fase A de EP-003 · HU-010

Origen: pendiente 27, abierto el 2026-08-15 y cerrado el 2026-08-16.

| | |
|---|---|
| **De dónde salía** | El hallazgo H-6 del [2026-08-15 · la plantilla del resultado de pruebas](../../historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md) |
| **Dónde se resolvió** | En la propia fase [`A-EP-003-HU-010`](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/), como el pendiente pedía: **se reabrió, no se abrió una nueva** |

## Qué pasaba

Al reescribir el resultado de pruebas con la forma nueva, el veredicto pasó de «aprobada con una prueba pendiente» a **No cumple**. No cambió el criterio: cambió que por fin había dónde escribir lo que faltaba. Eran tres cosas:

1. `RNF-01` sin ningún caso ejecutado — el `CP-006` pedía que las entradas las leyera alguien que no las escribió.
2. **16 de 35 pasos** del plan sin registro de qué salió, más 3 hechos distinto de lo que el plan pedía.
3. El `estado-fase` decía lo anterior y se contradecía con el resultado.

## Cómo cerró

**Las tres se resolvieron, y dos de ellas antes de que esta sesión las mirara:**

- **El ciclo 2** (2026-08-15) corrió los 12 pasos sin registro que sí se podían correr y los 3 hechos distinto. De ahí salió el defecto `D-05`: faltaban cinco términos.
- **El ciclo 3** (2026-08-16) ejecutó el `CP-006`, y de la única forma en que podía ejecutarse: el usuario llegó al glosario por su cuenta, no entendió la entrada **Brief** y preguntó tres veces. Las tres preguntas eran defectos. Se corrigieron los tres, se reescribieron las 72 definiciones y `brief` pasó a **planteamiento** en toda la zona normativa (v18.0.0).
- **El veredicto quedó en Cumple**, con una salvedad escrita: se probó una entrada de las cinco previstas.

**Lo que faltaba el 2026-08-16 era otra cosa, y más chica:** la cabecera del resultado seguía diciendo «ciclo 1» y «CP-006 sin ejecutar» mientras el cuerpo del mismo documento ya iba por el ciclo 3 y lo daba por corrido. Un documento contradiciéndose a sí mismo. Se puso al día el §0 y el §1, con la nota de qué decían antes.

## Lo que se aprendió

**El caso que «no puede correr el agente» corrió solo, sin que nadie lo planeara.** El `CP-006` pedía un lector de fuera y llevaba dos ciclos sin ejecutarse; se ejecutó el día que el usuario leyó el glosario para otra cosa y tropezó con una entrada mala. Sus tres preguntas fueron, palabra por palabra, lo que el paso 4 del caso mandaba anotar.

Vale para el diseño de casos: uno que depende de una persona no se marca «no ejecutable», se deja escrito qué hay que anotar cuando ocurra — porque ocurre.

## Lo que sigue abierto

- **Cuatro de las cinco entradas** no pasaron por lector de fuera. Está anotado como salvedad del veredicto, no como incumplimiento.
- Que el `resultado_pruebas` y el `estado-fase` no puedan volver a decir cosas distintas es el [pendiente 28](un-solo-veredicto-por-fase.md), que este destapó y que cerró el mismo día.

## Cómo se supo que cerró

El resultado de pruebas no se contradice a sí mismo: cabecera, cuerpo, veredicto y `estado-fase` dicen los tres lo mismo, y el `CP-006` tiene su ejecución escrita paso por paso.
