# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-reglas-con-expresiones-regulares.md](../../2026-08-07-reglas-con-expresiones-regulares.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Fue una consulta: no se tocó ni un archivo.

**Propósito:** entender hasta dónde llega un patrón cuando se trata de comprobar una regla.

---

## Hallazgos de esta sesión

### H-1 · La regex sirve para lo que tiene forma fija, no para juzgar

- **Qué pasó:** el usuario preguntó pro y contra de trabajar las reglas con expresiones regulares. La línea quedó dicha así: **si el patrón necesita saber *dónde* está el texto** —dentro de un comentario, de un bloque de código, de un ejemplo INCORRECTO— la regex ya no alcanza.
- **Por qué importa:** el peligro no son los falsos positivos, es la tentación: lo difuso parece alcanzable «con una regex más», y eso rompe el criterio de qué es validable — *si dos personas pueden discutir el resultado, no es validador*.
- **Qué lo soluciona:** repartir por tipo. Patrón para la estructura del propio estándar, que la escribe el estándar mismo; herramienta del ecosistema para lo que ya resuelven linter y suite; y las de criterio humano se quedan en el `.md`.
- **Qué se decidió:** nada que cambiara un archivo. Quedó el criterio y el ejemplo trabajado sobre `M1`.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [validadores/reglas-validables.md](../../../validadores/reglas-validables.md).
- **Nace en:** 2026-08-07 · reglas con expresiones regulares.
- **Cerrado en:** 2026-08-07 · reglas con expresiones regulares.
- **Con qué se retoma:** —.

### H-2 · El ancla es lo que separa un validador usable de uno que nadie enciende

- **Qué pasó:** al bajar `M1` a patrón apareció el detalle: la palabra `BLINDADA` sale en seis archivos, casi siempre en prosa. Anclando al **encabezado de la regla** (`^## …`) se descartan todos los falsos positivos de una.
- **Por qué importa:** un validador que reporta de más se termina apagando, y un control apagado es peor que ninguno porque figura como cubierto.
- **Qué lo soluciona:** anclar al encabezado, y para lo que la regex no distingue —citar una regla del núcleo no es ajustarla— pedirle al proyecto que declare el ajuste con una marca fija. **Regex de extractor, no de juez**: es el único uso que envejece bien.
- **Qué se decidió:** nada. La parte 1 y la 3 quedaron implementables ya en `metareglas.py`; la 2 exige cambiar el estándar, y eso era decisión del usuario.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es completar un validador que ya existe.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md). Se cruza con el [pendiente 19](../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que cuenta cuántas meta-reglas siguen sin comprobar.
- **Nace en:** 2026-08-07 · reglas con expresiones regulares.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿se implementan las dos comprobaciones de `M1` que ya se pueden, o se espera a decidir la declaración de capa 3?

### H-3 · El agente editó tres archivos en una sesión que era solo de preguntas

- **Qué pasó:** *«estoy preguntando solamente, no entiendo para qué está editando»*. El agente había escrito el histórico —que sí manda el `CLAUDE.md`— y además cambiado un recuerdo por su cuenta, porque leyó «menos es más» como corrección.
- **Por qué importa:** es la misma falla del día anterior. Interpretar un comentario como orden convierte una conversación en cambios que nadie pidió.
- **Qué lo soluciona:** revertir y preguntar.
- **Qué se decidió:** los tres archivos volvieron a como estaban. *«Nada pendiente de esta sesión.»*
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [pregunta, afirmación o indicación](../../memory/pregunta-no-es-instruccion.md).
- **Nace en:** 2026-08-07 · reglas con expresiones regulares.
- **Cerrado en:** 2026-08-07 · reglas con expresiones regulares.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 y H-3 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-2 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ quedó sin tocar nada del repositorio |
