# 2026-08-06 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-06-meta-reglas-2.md](../../2026-08-06-meta-reglas-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-15.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)), así que los hallazgos se sacaron de la transcripción, no se anotaron cuando pasaron. «Responde a» y «dispara» van en `—`: las épicas y las historias nacieron el 2026-08-13.

**Viene de:** —, es trabajo nuevo. Sigue el mismo día a [historico-chat](historico-chat.md).

**Propósito:** decidir dónde va una «regla de reglas» y escribirla.

---

## Hallazgos de esta sesión

### H-1 · No había regla que dijera cómo se escribe una regla

- **Qué pasó:** el usuario preguntó dónde iría una «regla de reglas». No existía: el estándar tenía convenciones que se usaban de hecho y nadie había escrito.
- **Por qué importa:** sin ellas, cada regla nueva se escribe distinta, dos reglas pueden contradecirse sin que nada lo note, y no hay forma de decidir cuál gana.
- **Qué lo soluciona:** un capítulo de preámbulo, numerado `00` porque manda sobre los demás y tiene que leerse antes que ellos.
- **Qué se decidió:** nace `base/00-meta-reglas.md` con trece reglas `M1`–`M13`: jerarquía de cuatro niveles, un tema un capítulo, desempate determinista que **termina en pausa** y no en criterio del agente, formato canónico, ID estable, dependencias declaradas, excepciones escritas dentro de la regla, criterio de validable, versionar obligatorio, derogar en vez de borrar, y buscar antes de crear.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** hoy es el capítulo [base/20-meta-reglas/base.md](../../../base/20-meta-reglas/base.md); entró como **1.2.0** en el [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-06 · meta-reglas-2.
- **Cerrado en:** 2026-08-06 · meta-reglas-2.
- **Con qué se retoma:** —.

### H-2 · Lo que manda mantener el estándar no puede viajar a los proyectos

- **Qué pasó:** al ubicar la regla de reglas quedó a la vista que hay dos cosas distintas: cómo el agente **interpreta** las reglas, y cómo se **escribe** una regla nueva de este repositorio.
- **Por qué importa:** si el instructivo de autoría entra a `base/`, se le cuela a todos los proyectos que heredan el estándar sin servirles de nada.
- **Qué lo soluciona:** separarlas por destino: la primera a `base/`, la segunda a un `CLAUDE.md` en la raíz de este repositorio, que no existía.
- **Qué se decidió:** se crea el [CLAUDE.md](../../../CLAUDE.md) raíz, con el histórico obligatorio, el procedimiento de autoría, la tabla de enrutamiento y la aprobación antes de commitear.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el [CLAUDE.md](../../../CLAUDE.md) del repositorio, y hoy la meta-regla `M13` del capítulo [20](../../../base/20-meta-reglas/base.md).
- **Nace en:** 2026-08-06 · meta-reglas-2.
- **Cerrado en:** 2026-08-06 · meta-reglas-2.
- **Con qué se retoma:** —.

### H-3 · La regla del histórico vivía solo en la memoria, y falló tres veces en la misma sesión

- **Qué pasó:** el usuario tuvo que señalar tres veces que el histórico no se estaba escribiendo. La regla existía en la memoria del agente y en un `README`, y ninguna de las dos obliga a nada.
- **Por qué importa:** es la primera vez que se ve el problema que después ordena todo el trabajo: **lo que depende de que el agente se acuerde, no pasa.**
- **Qué lo soluciona:** que la obligación entre al contexto sola, sin que el usuario la pida.
- **Qué se decidió:** el `CLAUDE.md` raíz, que Claude Code lee al abrir sesión en la carpeta. Se descartó apoyarse en el enganche `SessionStart` de entonces, porque [`hook_sesion.py`](../../../validadores/hook_sesion.py) sale sin hacer nada cuando la raíz es la del propio estándar.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el [CLAUDE.md](../../../CLAUDE.md); hoy la transcripción la escribe [`hook_historico.py`](../../../validadores/hook_historico.py) y es toda la épica [EP-005](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md).
- **Nace en:** 2026-08-06 · meta-reglas-2.
- **Cerrado en:** 2026-08-06 · meta-reglas-2.
- **Con qué se retoma:** —.

### H-4 · «Se escribe al cerrar la sesión» era el defecto

- **Qué pasó:** el `README` mandaba escribir la entrada al cerrar. Un chat casi nunca tiene cierre explícito, así que la entrada no se escribía nunca.
- **Por qué importa:** la misma frase, con otras palabras, sigue rigiendo hoy el resumen de la sesión: lo que se deja para el final no se escribe.
- **Qué lo soluciona:** invertir el disparador — crear apenas hay una decisión, y actualizar cada vez que se cierra un tema.
- **Qué se decidió:** se corrigió el `README` y la memoria del agente.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [historico-chat/README.md](../../README.md), la memoria [historico-chat/memory/historico-chat.md](../../memory/historico-chat.md), y hoy [`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md), que lo repite para el resumen.
- **Nace en:** 2026-08-06 · meta-reglas-2.
- **Cerrado en:** 2026-08-06 · meta-reglas-2.
- **Con qué se retoma:** —.

### H-5 · El histórico era un resumen, y lo que se pedía era la transcripción

- **Qué pasó:** el agente escribió la sesión como resumen ejecutivo. El usuario corrigió dos veces: primero «nada de lo que yo pregunto y usted responde aparece», y después «no es resumen, es cada una de las cosas que escribo y lo que responde la IA».
- **Por qué importa:** un resumen es la interpretación del agente de lo que pasó. Cuando esa interpretación es lo único que queda, no hay cómo comprobarla.
- **Qué lo soluciona:** transcripción literal de los dos lados, con marca de tiempo leída del reloj, y `hora no registrada` cuando no se tomó.
- **Qué se decidió:** se reescribió el archivo entero, se cambió la plantilla del `README` y la memoria. Los bloques viejos quedaron con «hora no registrada»: ponerlas de memoria sería inventarlas.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [historico-chat/README.md](../../README.md). Nueve días después, el mismo defecto —horas estimadas en vez de leídas— vuelve a pasar y queda en el [pendiente 29](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md).
- **Nace en:** 2026-08-06 · meta-reglas-2.
- **Cerrado en:** 2026-08-06 · meta-reglas-2.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los cinco |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ está en el repositorio desde entonces |

Cerrada. Quedó dicho que el enganche `Stop` era opcional; el trabajo sin commitear se subió después.
