# `prompts/` — lo que el usuario pidió, con sus palabras

Textos que el usuario escribe para pedir una regla, un cambio o un trabajo, guardados **tal como los redactó**. No son norma (`20·M13`): la norma vive en `base/`. Son el origen, y sirven para comprobar después si lo que quedó escrito dice lo que se pidió.

**Nomenclatura:** `<tema>.md`, en minúsculas y con guiones.

Un prompt **no se corrige ni se reescribe** cuando la regla que salió de él quedó redactada de otro modo. Si la regla terminó diciendo algo distinto, eso se explica en el `CHANGELOG.md` y en el histórico de la sesión, no editando el pedido.

## Índice

| Prompt | Qué pidió | En qué quedó |
|---|---|---|
| [regla-reglas-proyecto.md](regla-reglas-proyecto.md) | Que ninguna regla de `reglas-proyecto` exista sin una regla del agente que la respalde, y que la del agente se cree primero si falta. | [`20·M16`](../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) (v8.0.0), con el respaldo puesto sobre el **criterio** y no sobre el detalle, para que no choque con [`20·M3`](../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md). |
