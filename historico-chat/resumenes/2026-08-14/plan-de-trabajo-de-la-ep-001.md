# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-14-plan-de-trabajo-de-la-ep-001.md](../../2026-08-14-plan-de-trabajo-de-la-ep-001.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es la continuación de EP-001: sus ocho historias ya estaban escritas y solo la primera tenía fase.

**Propósito:** bajar a fases las historias de la épica del cuerpo de reglas heredable.

---

## Hallazgos de esta sesión

### H-1 · Si la IA se prueba a sí misma, la prueba no vale

- **Qué pasó:** al escribir el plan de pruebas de la fase A de HU-002, tres casos resultaron ser de conducta del agente. El agente los dejó marcados para que **los corra el usuario**.
- **Por qué importa:** una prueba que comprueba si el agente se comporta como manda la regla no puede ejecutarla el agente. No es rigor extra: es la única forma de que el resultado signifique algo.
- **Qué lo soluciona:** que el plan diga quién corre cada caso, y que los de conducta no queden a cargo de quien se está probando.
- **Qué se decidió:** quedó escrito en el plan de la fase.
- **Estado:** resuelto acá.
- **Responde a:** EP-001 · HU-002.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** el plan de pruebas de la fase A de HU-002. El mismo criterio reapareció el 2026-08-15, cuando un caso quedó bloqueado por necesitar a alguien que no hubiera escrito el glosario.
- **Nace en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Cerrado en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Con qué se retoma:** —.

### H-2 · Estas fases planean cosas que ya están construidas

- **Qué pasó:** el agente lo dejó dicho como la observación que más pesa: las fases de EP-001 se escriben como plan pendiente, pero lo que planean —el núcleo blindado, el desempate, la tabla de capas— **ya está escrito en el repositorio**.
- **Por qué importa:** si el molde correcto es el de retrodocumentación y no el de una fase por hacer, los documentos de HU-002 hay que rehacerlos **antes** de escribir los de las otras seis historias. Son 24 documentos de diferencia.
- **Qué lo soluciona:** decidir cuál de los dos moldes aplica.
- **Qué se decidió:** nada. Quedó como pregunta abierta al usuario.
- **Estado:** abierto.
- **Responde a:** EP-001.
- **Dispara:** —, hay [plantilla de retrodocumentación](../../../base/13-documentacion/retrodocumentacion.md) escrita; falta decidir si aplica.
- **Orden de resolución:** 1 de 3. Va primero: bloquea escribir las seis historias que faltan.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿las fases de EP-001 son plan o son retrodocumentación de lo que ya está en `base/`?

### H-3 · Tres dudas dejaron la fase escrita y sin poder arrancar

- **Qué pasó:** el plan de la fase A de HU-002 quedó con tres preguntas que lo bloquean: si el preámbulo es una capa o queda fuera, cuántas capas hay contando la del proyecto, y si «opcional» es una marca dentro de la capa o una capa aparte.
- **Por qué importa:** son del contenido, no del proceso. Sin respuesta, escribir la fase igual produciría un documento que después hay que rehacer.
- **Qué lo soluciona:** que las responda el usuario, que es de quien son las decisiones de catálogo.
- **Qué se decidió:** quedaron escritas dentro del plan, en su sección de dudas.
- **Estado:** abierto.
- **Responde a:** EP-001 · HU-002.
- **Dispara:** —.
- **Orden de resolución:** 2 de 3.
- **Dónde queda:** §2.7 del plan de trabajo de la fase A de HU-002.
- **Nace en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Cerrado en:** —.
- **Con qué se retoma:** las tres preguntas, tal como están escritas en el plan.

### H-4 · Se puede commitear solo lo propio; publicar, no

- **Qué pasó:** el agente commiteó solo lo de esta sesión, y hasta preparó aparte la versión del índice del histórico **con una sola línea suya**, porque otras dos sesiones lo estaban tocando al mismo tiempo. Pero al publicar se topó con el límite: en la rama había tres commits sin publicar de otras sesiones, y git no publica un commit suelto.
- **Por qué importa:** es el matiz que faltaba de la regla de no mezclar trabajos. **Separar commits sí se puede; separar el `push`, no.** Publicar el propio publica todo lo que esté antes.
- **Qué lo soluciona:** que cada sesión suba y publique lo suyo apenas cierra, en vez de acumular.
- **Qué se decidió:** commitear sin publicar, y dejar el `push` al usuario cuando esas sesiones cierren.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [no tocar el trabajo de otras sesiones](../../memory/no-tocar-trabajo-de-otras-sesiones.md) y el [pendiente 22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md).
- **Nace en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Cerrado en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Con qué se retoma:** —.

### H-5 · Un aviso del validador en trabajo ajeno

- **Qué pasó:** la fase A de HU-001, escrita por otra sesión, sale con aviso: dice `**Origen:**` donde la plantilla pide `**ORIGEN**`. El agente lo reportó y preguntó si lo corregía, **aunque fuera de otra sesión**.
- **Por qué importa:** es el cruce de dos reglas de trabajo: se corrige lo que uno mismo detecta, pero no se toca lo de otra sesión. Preguntar era lo correcto.
- **Qué lo soluciona:** que lo arregle quien lo escribió, o que el usuario lo autorice.
- **Qué se decidió:** no se tocó.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es una palabra.
- **Orden de resolución:** 3 de 3.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿sigue el aviso `DOC12` en la fase A de HU-001?

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 y H-4 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-2, H-3 y H-5 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md); H-3 vive además dentro del plan de la fase |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commit `70fca40`, sin publicar por decisión del usuario |
