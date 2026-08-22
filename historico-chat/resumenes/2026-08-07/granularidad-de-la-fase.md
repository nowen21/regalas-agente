# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-granularidad-de-la-fase.md](../../2026-08-07-granularidad-de-la-fase.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).
>
> **Tuvo una copia.** `2026-08-07-sesion-9.md` repetía esta conversación, escrita a mano. Se borró el 2026-08-16; sigue en el historial de git.

**Viene de:** —, es trabajo nuevo. Dos preguntas, ningún archivo tocado.

**Propósito:** saber cuántos criterios de aceptación lleva una fase.

---

## Hallazgos de esta sesión

### H-1 · La pregunta ya estaba respondida en el estándar

- **Qué pasó:** el usuario preguntó si el plan de trabajo se ejecuta por los CA de la historia o por cada CA. La respuesta ya estaba escrita: `F12.9` cuando el CA se implementa, prueba y cierra solo; `F12.10` cuando varios CA comparten línea base y solo se validan juntos.
- **Por qué importa:** el criterio práctico que salió de ahí es el que se sigue usando — *agrupar los CA que cierran con la misma prueba; separar en cuanto un CA pueda demostrarse solo*. Y dos límites que ya estaban: no partir por nomenclatura, y decidir la granularidad **antes** de aprobar el plan, porque después no se subdivide.
- **Qué lo soluciona:** nada nuevo: leer lo que hay.
- **Qué se decidió:** no se tocó ningún archivo del estándar.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`F12.9` y `F12.10`](../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md). Ocho días después nace la memoria [buscar en el repositorio antes de preguntar](../../../pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md) por el defecto contrario.
- **Nace en:** 2026-08-07 · granularidad de la fase.
- **Cerrado en:** 2026-08-07 · granularidad de la fase.
- **Con qué se retoma:** —.

### H-2 · La dependencia entre criterios de aceptación no tiene dónde escribirse

- **Qué pasó:** la segunda pregunta llegó al hueco real: la dependencia entre CA es justo el insumo que decide si van en una fase o en varias, y el orden. Hoy la [plantilla de la historia](../../../plantillas/ciclo-vida-proyectos/04-HU.md) declara dependencias **a nivel de historia**, no CA a CA.
- **Por qué importa:** sin ese mapa, la dependencia se descubre a mitad de ejecución y toca pausar. Y la distinción importa: la de **validación** —CA-03 no se puede probar si CA-01 no existe— manda sobre las fases; la **técnica** —dos CA comparten una migración— no es dependencia del CA, es soporte dentro del plan.
- **Qué lo soluciona:** una fila en la sección 8 de la plantilla: `CA-0X depende de CA-0Y (motivo)`.
- **Qué se decidió:** nada. El agente lo propuso y esperó; no hubo respuesta.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es una fila en una plantilla que ya existe.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md](../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md).
- **Nace en:** 2026-08-07 · granularidad de la fase.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿la dependencia CA→CA entra a la plantilla de la historia, o se mapea aparte al armar las fases?

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-2 en el [33](../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ no se tocó ningún archivo |
