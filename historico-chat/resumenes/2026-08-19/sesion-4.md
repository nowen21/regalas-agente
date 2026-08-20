# 2026-08-19 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-19-sesion-4.md](../../2026-08-19-sesion-4.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «la nueva actualización no la están reconociendo los demás proyectos y se bloquean: cuando uno les escribe no se dispara nada»

---

## Hallazgos de esta sesión

### H-1 · La 26.0.0 movió los enganches y dejó a los proyectos instalados sin forma de enterarse

- **Qué pasó.** El commit `acb082d` (v26.0.0) movió los ocho `hook_*.py` de `validadores/` a `adaptadores/claude-code/` **sin dejar nada en la ruta vieja**. El `.claude/settings.json` de cada proyecto heredero sigue llamando `python ".../validadores/hook_*.py"`; Python no encuentra el archivo y sale con **código 2**, que en el enganche `UserPromptSubmit` de la herramienta significa **bloquear el mensaje**. Por eso los proyectos se quedan mudos al escribirles.
- **Por qué importa.** El plan de recuperación del propio commit —«el aviso lo reclama solo en el primer mensaje de la siguiente sesión», vía `hook_checklist.py`— **no puede dispararse: el avisador se mudó junto con lo que tenía que avisar**. La actualización rompió el canal por el que se anuncia a sí misma.
- **Qué se decidió.** El usuario ordenó corregirlo de una, sin dejarlo en pendientes. Se corrió `instalar.py --todos --aplicar` (9 de 9 proyectos; todos apuntan ya a `adaptadores/claude-code/`) y se dejaron **ocho puentes** en `validadores/hook_*.py` que reenvían a la ruta nueva con los mismos argumentos, entrada y código de salida, para que ninguna instalación rezagada vuelva a bloquearse. Probados por la ruta vieja: salen con código 0.
- **Dónde queda.** Los puentes en `validadores/hook_*.py`; la entrada **26.0.1** del `CHANGELOG.md` (PARCHE) con la lección para el próximo movimiento: lo que los proyectos llaman por ruta absoluta no se muda sin puente, porque el aviso de desfase viaja por el canal que se rompe. En dp_card el instalador reporta 13 de 14 —falta el planteamiento de `prompts/`, que no es del instalador: se escribe con el usuario en ese proyecto.

### H-2 · El estándar se comparó contra `notas/estructura.md` y sus cuatro brechas se construyeron en la sesión

- **Qué pasó.** El usuario pidió analizar si Cimiento cumple [notas/estructura.md](../../../notas/estructura.md) (arquitectura de un agente LLM en producción). Cumple el principio rector y las preocupaciones de fondo por medios propios; delega el loop en la herramienta (declarado en `adaptadores/contrato.md`); y le faltaban cuatro cosas: evals de comportamiento, presupuesto visible, histórico inmutable y aislamiento de contenido externo.
- **Por qué importa.** Sin evals, cada cambio del estándar es una apuesta; sin presupuesto, cada sesión una factura sorpresa; un histórico reescribible no es auditoría; y ninguna regla decía qué hacer con una orden que venga dentro de contenido ajeno.
- **Qué se decidió.** El usuario ordenó implementarlas de una, **sin pendientes y sin bajar por la cadena de `02·F0`** — la misma tensión que la señal S-002 registró el 14-08. Quedó dicho en el chat y acá: se hizo por orden directa, con `20·M14` aplicado entero a la regla nueva (que no admite atajo).
- **Dónde queda.** Versión **27.0.0** (`CHANGELOG.md`): regla [`01·C27`](../../../base/01-conducta.md#c27--lo-que-llega-de-afuera-es-dato-no-orden) (dato, no orden — checklist CUMPLE 19✅/1 N/A), banco [`evals/`](../../../evals/README.md) (8 casos, 8 en verde), `validadores/presupuesto.py` + `hook_presupuesto.py` (desplegado a los 9 proyectos, Stop), `validar.py inmutable` (la transcripción solo crece; AVISO, no impide). Suite: 365 pruebas en verde con las 6 nuevas. `reglas-validables.md` al día (C27 clasificada; nota vieja de `metareglas.py` corregida) y el mapa de amarre en 21 de 62.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☐ |
| Todo hallazgo abierto tiene su pendiente creado | ☐ |
| Toda historia disparada está escrita en su épica | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: hallazgos sin la H del molde -->
