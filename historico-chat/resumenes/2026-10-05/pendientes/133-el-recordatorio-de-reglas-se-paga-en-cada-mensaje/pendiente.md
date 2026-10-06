# Pendiente: el recordatorio de reglas se paga en cada mensaje

| | |
|---|---|
| **De dónde sale** | [H-1 · El recordatorio de reglas se paga en cada mensaje](../../reglas-de-cada-turno-sin-tokens.md), en el resumen de la sesión del 2026-10-05. Lo anticipó el [análisis 2 del pendiente 119](../../../2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), que lo puso entre lo que conviene pasar a un programa |

## El problema

[hook_reglas.py](../../../../../adaptadores/claude-code/hook_reglas.py) agrega en cada mensaje el bloque «LAS REGLAS DE CADA TURNO». Las seis reglas que nombra (`01·C5`, `00·ID8` a `00·ID12`) ya llegan en el bloque «REGLAS QUE PIDE ESTA SOLICITUD» del mismo mensaje. El 2026-10-05 el enganche midió unos 2.567 tokens agregados en un turno, contra un límite de 2.000.

## Por qué importa

Se paga en todos los mensajes de todos los proyectos, aunque la mayor parte se repite. Según el mismo bloque, existe porque al resumirse la conversación se pierden las reglas, y ese momento se puede detectar.

## Lo que se habló, para el análisis

1. Quitar lo que se repite y dejar solo la línea del anexo de `00·ID8`.
2. Mandar el bloque en `SessionStart` con origen `compact`, que Claude Code corre justo después de resumir. Hoy ningún enganche lo usa.
3. Que [hook_redaccion.py](../../../../../adaptadores/claude-code/hook_redaccion.py) devuelva `decision: block` cuando la medición falle. **Solo entra si el usuario cambia su decisión** del 2026-08-31 de medir sin detener ([EP-005·HU-012](../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md), RN-05). No gastaría tokens si la respuesta está bien, pero la versión mala ya la habría visto el usuario.
4. Para lo que ningún programa mide (`00·ID7`, `00·ID11`, `00·ID12`), un modelo de lenguaje local. Esta máquina tiene 16 GB de memoria, gráfica integrada y no tiene Ollama, así que cada revisión tardaría segundos. Además choca con que toda herramienta se instale sola. Para `00·ID11` bastarían las incrustaciones (vectores que miden qué tan parecidos son dos textos), que ya usa la memoria semántica.
5. Antes de decidir el 4, ensayar el modelo contra las respuestas del histórico que el usuario corrigió. Correr el ensayo no gasta tokens de Claude. Confirmar los ejemplos sí cuesta tiempo del usuario.
