# 2026-08-12 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md](../../2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)). Empezó el 2026-08-12 y siguió hasta el 13.

**Viene de:** —, es trabajo nuevo.

**Propósito:** que ninguna regla de un proyecto exista por su cuenta, sin nada del estándar que la respalde.

---

## Hallazgos de esta sesión

### H-1 · Un proyecto podía escribir reglas que no salían de ninguna parte

- **Qué pasó:** la plantilla del catálogo de reglas de proyecto admitía la salida *«regla nueva, no cubierta por la base»*. Con eso, cada proyecto podía inventar su propia norma sin que nada del estándar la sostuviera.
- **Por qué importa:** el estándar deja de ser el origen común y pasa a ser una sugerencia. Y al revés: lo que un proyecto necesita y la base no cubre es justamente la señal de que **falta una regla en la base**.
- **Qué lo soluciona:** que cada regla de proyecto nombre la regla de `base/` cuyo criterio concreta, y que sin respaldo no se publique — primero se crea la regla agnóstica arriba.
- **Qué se decidió:** nace [`20·M16`](../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md). En la [plantilla](../../../plantillas/reglas-proyecto.md), *Relación con la base* pasó a **Respaldo** obligatorio con enlace. Versión **8.0.0 · MAYOR**: los proyectos con reglas ya escritas tienen que agregarles el respaldo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`M16`](../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md), versión 8.0.0 del [CHANGELOG](../../../CHANGELOG.md), commit `543869e`.
- **Nace en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Cerrado en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Con qué se retoma:** —.

### H-2 · El respaldo tenía que ser del criterio, no del detalle

- **Qué pasó:** el agente avisó antes de escribir nada: tal como estaba pedida, la regla se trancaba. Una regla de proyecto suele ser específica de su stack —*«las rutas van en kebab-case y en plural»*— y eso **nunca** puede subir a `base/`, que se exige agnóstica.
- **Por qué importa:** sin esa lectura, la regla obligaba a meter stack en la base y se contradecía con `M3` desde el primer día.
- **Qué lo soluciona:** que la base fije el criterio agnóstico —*nombres que dicen la intención*— y la regla del proyecto le ponga el valor concreto.
- **Qué se decidió:** así quedó redactada, y el capítulo 20 lleva una sección que lo explica: *el respaldo es del criterio, no del detalle*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/20-meta-reglas/base.md](../../../base/20-meta-reglas/base.md).
- **Nace en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Cerrado en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Con qué se retoma:** —.

### H-3 · «Se le olvidó el estándar»

- **Qué pasó:** el agente escribió la regla directamente. El usuario lo cortó en cinco palabras: *«sí, pero se le olvidó el estándar»*. Faltaban los nueve pasos del procedimiento del capítulo 20.
- **Por qué importa:** es el capítulo que manda cómo nace una regla, y lo estaba incumpliendo justo al escribir una regla de ese capítulo. `M14` existe desde el 2026-08-07 exactamente para esto.
- **Qué lo soluciona:** rehacerlo paso por paso: buscar, enrutar, escribir, declarar dependencia, decidir si es validable, versionar y cerrar con el checklist.
- **Qué se decidió:** se rehízo con los nueve pasos, y quedó la tabla de qué produjo cada uno.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`M14`](../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md), que es la que se estaba saltando.
- **Nace en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Cerrado en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Con qué se retoma:** —.

### H-4 · Lo que el usuario pidió estaba solo dentro de las transcripciones

- **Qué pasó:** el usuario pidió rescatar del histórico lo que pudiera servir como regla, y ponerlo en fichas sueltas. Salieron **26 fichas**, cada una con su cita literal y el enlace a la sesión de donde viene.
- **Por qué importa:** el pedido original es el dato que no se puede reconstruir. La regla que sale de él se puede reescribir mil veces; lo que el usuario dijo, no.
- **Qué lo soluciona:** una carpeta versionada, con su índice por grupo, y una norma de trato: **un prompt no se corrige después**. Cuando la regla terminó exigiendo algo distinto de lo pedido, la diferencia se cuenta en el `CHANGELOG` y en el índice, no reescribiendo lo que el usuario pidió.
- **Qué se decidió:** nace [prompts/README.md/](../../../prompts/README.md), con su fila en la tabla de *dónde va cada cosa* del [CLAUDE.md](../../../CLAUDE.md).
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [prompts/README.md/](../../../prompts/README.md), commit `0e7d9a9`.
- **Nace en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Cerrado en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Con qué se retoma:** —.

### H-5 · El histórico no es regla de nadie

- **Qué pasó:** al analizar las 27 fichas contra el catálogo salió el hueco más grande: la obligación de escribir el histórico se sostiene en el `CLAUDE.md` **de este repositorio**, una plantilla y un enganche. Ninguna regla de `base/` la exige. Un proyecto que herede el estándar y apague el enganche no incumple nada.
- **Por qué importa:** es la pieza sobre la que se construyó todo lo demás, y es la única sin norma que la respalde. El resultado del análisis: de 27 fichas, 13 ya estaban cubiertas, 7 pedían regla nueva, 3 se resolvían afinando y 4 no eran regla del estándar.
- **Qué lo soluciona:** escribir las siete reglas que faltan, agrupadas en una sola entrada del `CHANGELOG` — porque son cinco MAYOR seguidas y, de a una, un proyecto al día recibiría cinco avisos de migración el mismo día.
- **Qué se decidió:** quedó el análisis escrito, con el orden propuesto. Las siete reglas **no se escribieron**: al día siguiente el trabajo se enrutó al brief y sus épicas, y los identificadores que el análisis proponía (`DOC19`, `DOC20`, `C20`, `G9`) hoy los ocupan otras reglas.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, hoy vive como épica: [EP-005](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md), automatismos que no dependen de la memoria.
- **Orden de resolución:** 1 de 2. Va primero: es el hueco que el propio análisis marcó como el más grande.
- **Dónde queda:** [prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md](../../../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md).
- **Nace en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Cerrado en:** —.
- **Con qué se retoma:** de las siete propuestas, ¿cuáles siguen haciendo falta ahora que el trabajo vive en épicas y sus identificadores están ocupados?

### H-6 · Dos reglas del propio estándar se contradicen

- **Qué pasó:** el análisis lo marcó sin rodeos: la ficha de *corregir lo que está mal sin preguntar* choca de frente con [`02·F20`](../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), que manda **parar y proponer** lo que se descubra fuera del criterio de aceptación.
- **Por qué importa:** *«no es redacción, es fondo»*. Una manda arreglar y la otra manda parar, y hoy las dos rigen.
- **Qué lo soluciona:** separar en el texto dos cosas que se parecen: el defecto que el propio agente reportó —que arregla— y la mejora fuera de alcance —que propone y espera.
- **Qué se decidió:** quedó anotado en el análisis. No se tocó ninguna de las dos.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es afinar una regla existente.
- **Orden de resolución:** 2 de 2.
- **Dónde queda:** [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md). La memoria [corregir el defecto que uno mismo detecta](../../memory/corregir-el-defecto-que-uno-mismo-detecta.md) ya trae el matiz — vale solo mientras se ejecuta algo autorizado —, pero `F20` no lo dice.
- **Nace en:** 2026-08-12 · regla de respaldo de las reglas de proyecto.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿dónde termina «el defecto que yo mismo reporté» y empieza «lo que descubrí fuera del alcance»?

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 a H-4 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-5 vive en [EP-005](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md); H-6 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ las siete reglas propuestas se enrutaron a las épicas del brief |
| Lo que se hizo está aprobado y guardado | ☑ commits `543869e`, `88bfe60` y `0e7d9a9` |
