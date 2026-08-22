# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-14-resultado-de-pruebas-y-cierre-de-fase.md](../../2026-08-14-resultado-de-pruebas-y-cierre-de-fase.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** 2026-08-13 · del brief a los planes de la fase A. Sigue esa sesión: ya hay planes, y ahora se cierra la fase.

**Propósito:** que al cerrar una fase se pueda comprobar que se hizo lo que el plan dijo que se iba a hacer.

---

## Hallazgos de esta sesión

### H-1 · Nada verificaba que el plan de trabajo se hubiera cumplido

- **Qué pasó:** el usuario lo preguntó en una línea: *«¿en dónde se verifica que el plan de trabajo se llevó a cabo?»*. En ningún lado. El resultado de pruebas comprueba que **el resultado sirve**; que se haya hecho lo que se dijo no lo revisaba nadie. El avance se marcaba con una casilla **dentro del propio plan** —autorreporte, y encima pisando el documento aprobado— y el cierre trazaba solo contra la especificación.
- **Por qué importa:** una fase podía pasar todas las pruebas y haber dejado tres tareas sin tocar, o haber tocado archivos que el plan no declaraba, sin que quedara rastro.
- **Qué lo soluciona:** dos trazabilidades separadas, porque responden preguntas distintas: **spec → implementación** (qué había que lograr) y **plan → ejecución** (qué se iba a hacer para lograrlo).
- **Qué se decidió:** el cierre gana la trazabilidad tarea por tarea, con dos preguntas que antes no se hacían: las **tareas que no se hicieron** y los **archivos tocados que el plan no declaraba**. El plan pierde su columna de estado, el seguimiento en vivo pasa al estado de fase, y queda la cadena completa: el plan dice qué se va a hacer, el estado dice por dónde va, el cierre dice qué se hizo. Versión **9.1.0**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md](../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) §2, versión 9.1.0 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Cerrado en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Con qué se retoma:** —.

### H-2 · La deuda técnica no decía de dónde salía

- **Qué pasó:** el usuario objetó la sección de deuda: *«si se aprueba un plan y ahí dice lo que se va a hacer, ¿por qué hay deuda técnica?»*. Y llegó él mismo a la causa: *«la deuda técnica queda porque no se hizo ese análisis»* — el del proyecto real, antes de escribir el plan.
- **Por qué importa:** no todas las deudas dicen lo mismo. Una que sale de no haber visto lo que se iba a romper señala que la línea base se hizo floja; una decidida por tiempo, o diferida por el propio plan, no señala nada malo. Sin separarlas no se puede saber si el análisis previo se está haciendo bien.
- **Qué lo soluciona:** una columna que diga el origen, con cuatro valores: *no previsto*, *atajo decidido*, *cambio del entorno* y *diferido por el plan*.
- **Qué se decidió:** se agregó. Y quedó escrito para qué sirve: **un análisis bueno no elimina la deuda, convierte la descubierta en declarada.** Si fase tras fase se repite «no previsto», el problema no es la deuda: es la línea base. Versión **9.2.0**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md](../../../plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) §6, versión 9.2.0 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Cerrado en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Con qué se retoma:** —.

### H-3 · El agente convirtió una observación en un cambio

- **Qué pasó:** el usuario hizo una observación sobre la deuda técnica y el agente se puso a modificar. La corrección vino en dos partes: *«no modifique nada, solo estoy haciendo la observación para que me explique y luego sí se haga la corrección si es necesario; no asuma que porque digo algo ya tiene que modificar»*, y después la general: *«necesito que entienda cuándo estoy preguntando, cuándo afirmando o dando una indicación de que se ejecute algo»*.
- **Por qué importa:** el recuerdo que había cubría solo la pregunta. Faltaba el caso del medio, que es el más frecuente: **la observación**, que pide explicación y espera.
- **Qué lo soluciona:** tres modos, con qué hacer en cada uno. Pregunta: solo se responde. Observación: se explica y se espera. Indicación: se ejecuta. En la duda, no se toca.
- **Qué se decidió:** el usuario pidió escribirlo — *«sí claro, escríbalo»*.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [pregunta, afirmación o indicación](../../memory/pregunta-no-es-instruccion.md).
- **Nace en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Cerrado en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Con qué se retoma:** —.

### H-4 · Lo trabajado se estaba mezclando en una sola sesión

- **Qué pasó:** el usuario lo cortó al final: *«lo que hemos trabajado hoy manéjelo en otra sesión con su respectivo nombre identificativo para que no se pierda la trazabilidad»*.
- **Por qué importa:** una sesión que arranca por un tema y termina en otro deja los dos sin nombre propio. Es la misma razón por la que el nombre se pone dentro de la sesión y no al final.
- **Qué lo soluciona:** abrir sesión nueva cuando el tema cambia, y nombrarla.
- **Qué se decidió:** así se hizo: lo que siguió se abrió aparte.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [historico-chat/README.md](../../README.md), y es lo que hoy hace la sección de cierre de cada resumen.
- **Nace en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Cerrado en:** 2026-08-14 · resultado de pruebas y cierre de fase.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los cuatro |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ versiones 9.1.0 y 9.2.0 |
