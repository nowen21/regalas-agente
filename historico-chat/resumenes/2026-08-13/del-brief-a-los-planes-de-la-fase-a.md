# 2026-08-13 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-13-del-brief-a-los-planes-de-la-fase-a.md](../../2026-08-13-del-brief-a-los-planes-de-la-fase-a.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Arranca con una pregunta suelta sobre machine learning y termina con la primera fase del estándar planificada.

**Propósito:** que el estándar se construya a sí mismo con su propio flujo: brief, épicas, historias, fase.

---

## Hallazgos de esta sesión

### H-1 · El agente no es Claude

- **Qué pasó:** el usuario tuvo que corregirlo cuatro veces seguidas: *«no estoy hablando de Claude sino del agente, el agente no es Claude»*, *«¿dónde dice que el agente es Claude?»*, *«el agente es lo que está en `C:\Ing. Jose\ia\agente`»*. El agente respondía sobre el modelo cuando le preguntaban por el estándar.
- **Por qué importa:** son tres cosas distintas y confundirlas cambia la respuesta. **El agente** es lo que se instala en cada proyecto: enganches, validadores, reglas. **El estándar** son `base/` y `plantillas/`. **Claude** es la IA que lo opera. En cada proyecto no se instala Claude.
- **Qué lo soluciona:** dejar el vocabulario escrito.
- **Qué se decidió:** quedó como recuerdo, y de ahí sale una de las épicas: el aprendizaje que vive en esa carpeta es el resultado de lo que se fue aprendiendo, no un modelo entrenado.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [terminología: agente vs estándar vs Claude](../../memory/terminologia-agente-vs-estandar.md).
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-13 · del brief a los planes de la fase A.
- **Con qué se retoma:** —.

### H-2 · El agente contestó tres veces distinto la misma pregunta

- **Qué pasó:** a *«¿es recomendable aplicarle machine learning al agente?»* el agente respondió primero que el estándar no tiene nada de eso, después que no conviene, y después que sería ponerle un segundo modelo encima del que ya lo hace funcionar. El usuario le puso las tres respuestas al lado: *«acá se está contradiciendo»*.
- **Por qué importa:** además fue a buscar en las reglas una pregunta que no era sobre las reglas. El usuario lo dijo entero: *«lo ideal sería que se limite a responder la pregunta y no dar explicaciones que no se le pidieron, y eso es una regla del agente»*.
- **Qué lo soluciona:** responder lo que se preguntó, con lo que se sabe, sin ir a buscar respaldo a un sitio que no viene al caso.
- **Qué se decidió:** el agente corrigió y unificó la respuesta.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** las memorias de [respuestas cortas](../../memory/respuestas-cortas.md) y [pregunta, afirmación o indicación](../../memory/pregunta-no-es-instruccion.md).
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-13 · del brief a los planes de la fase A.
- **Con qué se retoma:** —.

### H-3 · El brief describía una solución, no una necesidad

- **Qué pasó:** el usuario pidió el brief del agente, preguntó qué era un brief, y con la respuesta en la mano objetó lo que estaba escrito: *«si un brief es la necesidad, ¿por qué el que redactó no lo hizo de esa manera?»*. Y puso la condición: *«asuma que no existe nada todavía, porque precisamente estamos arrancando con la necesidad»*.
- **Por qué importa:** un brief que parte de lo ya construido no puede cuestionarlo. Escribirlo desde cero es lo que permitió que las épicas salieran de la necesidad y no del inventario de lo que ya había.
- **Qué lo soluciona:** reescribirlo desde la necesidad, sin dar por hecho nada de lo existente.
- **Qué se decidió:** nace [planteamiento.md](../../../planteamiento.md) con esa premisa, y de él salen las **siete épicas**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [planteamiento.md](../../../planteamiento.md) y [documentacion/epicas/README.md/](../../../documentacion/epicas/README.md), versiones 8.0.1 y 8.1.0 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-13 · del brief a los planes de la fase A.
- **Con qué se retoma:** —.

### H-4 · «Y si en la plantilla no está, hay que corregirlo»

- **Qué pasó:** el usuario lo dijo tres veces, cada vez que un documento salía incompleto: los nombres de los archivos de las épicas no cumplían el estándar, los planes no decían cuál es el propósito de cada documento, y la historia no decía qué va en el plan de trabajo y qué en el de pruebas. Las tres veces la instrucción fue la misma: **si eso no está en la plantilla, hay que corregir la plantilla.**
- **Por qué importa:** es la diferencia entre arreglar un documento y arreglar la causa. Corregir solo el documento deja el mismo hueco esperando al siguiente que use la plantilla.
- **Qué lo soluciona:** que el defecto de un entregable se persiga hasta el molde que lo produjo.
- **Qué se decidió:** se corrigieron las plantillas, no solo los documentos. Versiones 8.2.0 y 9.0.0.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/](../../../plantillas/) — épica, historia y los dos planes. Es el mismo criterio que dos días después vuelve a aplicarse a la [plantilla del resultado de pruebas](../2026-08-15/la-plantilla-del-resultado-de-pruebas.md).
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-13 · del brief a los planes de la fase A.
- **Con qué se retoma:** —.

### H-5 · Un documento que dice «qué no es» está diciendo dos veces lo mismo

- **Qué pasó:** el usuario lo preguntó de frente: *«si estamos colocando el qué, ¿para qué colocar el qué no es?»*.
- **Por qué importa:** la sección de lo que algo no es se llena de suposiciones que nadie tuvo. Ocupa espacio en un documento que se lee para saber qué hacer.
- **Qué lo soluciona:** decir qué es, y dejar fuera de alcance solo lo que de verdad alguien podría creer incluido.
- **Qué se decidió:** se quitó lo que no aportaba.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** las plantillas de [épica](../../../plantillas/epica.md) e [historia](../../../plantillas/HU.md).
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-13 · del brief a los planes de la fase A.
- **Con qué se retoma:** —.

### H-6 · La historia no decía cuáles fases la implementan

- **Qué pasó:** el usuario lo notó por simetría: *«si en la épica se enumeran las HU, ¿por qué en la HU no va qué es del plan de trabajo y qué del plan de pruebas?»*. Y después: *«pero no está el formato dentro de la fase»*.
- **Por qué importa:** sin esa lista, para saber por dónde va una historia hay que abrir carpetas. La cadena se sigue hacia abajo desde la épica hasta la fase, o se rompe en algún eslabón.
- **Qué lo soluciona:** una sección *Fases que la implementan* en la historia, y el formato de la fase escrito en su plantilla.
- **Qué se decidió:** se agregó a la plantilla de la historia y se armó la fase A de HU-001 con sus dos planes.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/HU.md](../../../plantillas/HU.md) y [plantillas/fase.md](../../../plantillas/fase.md), versión 9.0.0.
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-13 · del brief a los planes de la fase A.
- **Con qué se retoma:** —.

### H-7 · El resultado de pruebas tiene que responderle al plan de pruebas

- **Qué pasó:** lo dejó dicho en una línea al cerrar: *«ese resultado de pruebas debe cumplir lo que dice el plan de pruebas»*.
- **Por qué importa:** es la exigencia que dos días después destapa que una fase cerrada no cumplía: al bajar su resultado al molde, 16 de 35 pasos no tenían registro de qué salió.
- **Qué lo soluciona:** que el resultado se escriba contra el plan, caso por caso, y no como un relato de lo que se hizo.
- **Qué se decidió:** quedó pedido acá; el molde que lo hace cumplir se escribió el 2026-08-15.
- **Estado:** resuelto, pero en otra sesión.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/planes/resultados.md](../../../plantillas/planes/resultados.md), y el resumen de [la plantilla del resultado de pruebas](../2026-08-15/la-plantilla-del-resultado-de-pruebas.md).
- **Nace en:** 2026-08-13 · del brief a los planes de la fase A.
- **Cerrado en:** 2026-08-15 · la plantilla del resultado de pruebas.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los siete; H-7 se cerró dos días después |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ las ocho historias de EP-001 quedaron escritas |
| Lo que se hizo está aprobado y guardado | ☑ versiones 8.0.1, 8.1.0, 8.2.0 y 9.0.0 |
