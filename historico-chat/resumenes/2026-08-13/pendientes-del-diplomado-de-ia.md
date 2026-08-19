# 2026-08-13 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-13-pendientes-del-diplomado-de-ia.md](../../2026-08-13-pendientes-del-diplomado-de-ia.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** —, es trabajo nuevo. Estrena la idea 1 de la [libreta](../../../pendientes/10-ideas.md): que lo que el usuario aprende en el posgrado entre al estándar.

**Propósito:** comparar los apuntes del diplomado de IA contra el estándar y anotar lo que falte.

---

## Hallazgos de esta sesión

### H-1 · El estándar le exige a los proyectos cosas que no se exige a sí mismo

- **Qué pasó:** de los 130 archivos de los dos módulos salieron **cinco pendientes**, del 12 al 16. Cuatro son el mismo hallazgo visto por cuatro lados: no hay inventario de lo que el agente puede hacer, las reglas no tienen fecha de revisión, el estándar depende de una sola herramienta, y falta el criterio de **si conviene** automatizar y no solo si se puede.
- **Por qué importa:** el estándar pide inventario, ciclo de vida, gestión del riesgo y control de la dependencia del proveedor — y ninguna de esas cosas se las aplica a sí mismo.
- **Qué lo soluciona:** el más barato y el que más desbloquea es el 13, el inventario: el pendiente 12 reusa su tabla de riesgo, y un ítem del pendiente 09 hoy no tiene contra qué lista compararse.
- **Qué se decidió:** los cinco quedaron escritos y en el índice. No se tocó `base/`, ni `VERSION`, ni el `CHANGELOG`: todo dentro de `pendientes/`.
- **Estado:** abierto, que es lo que un pendiente es.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —, el orden está en el índice de pendientes.
- **Dónde queda:** [pendientes 13 a 16](../../../pendientes/README.md) y el [12](../../../pendientes/hecho/patron-ia.md).
- **Nace en:** 2026-08-13 · pendientes del diplomado de IA.
- **Cerrado en:** —.
- **Con qué se retoma:** el 13 primero: es una lista y una tabla, y desbloquea a los otros dos.

### H-2 · Se subieron épicas que todavía no tenían historias

- **Qué pasó:** el usuario pidió subir la documentación **por historia de usuario**. El agente subió también las épicas incompletas. El usuario lo corrigió dos veces, la segunda sin rodeos: *«le dije que es por HU y me subió las épicas que están incompletas; si están incompletas deben esperar que tengan sus HU»*.
- **Por qué importa:** un commit con una épica vacía publica una promesa. Y en el repositorio queda algo que otros documentos citan y que no tiene contenido.
- **Qué lo soluciona:** que la unidad del commit sea la historia, y que lo que no tenga historia escrita espere.
- **Qué se decidió:** el agente deshizo el commit y subió EP-001 en **ocho commits, uno por historia**. Las otras seis épicas quedaron fuera, con dos consecuencias dichas de frente: el brief queda con seis enlaces rotos hasta que suban, y dos planes citan épicas que todavía no están.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** commits `31f2434` a `c21491a`.
- **Nace en:** 2026-08-13 · pendientes del diplomado de IA.
- **Cerrado en:** 2026-08-13 · pendientes del diplomado de IA.
- **Con qué se retoma:** —.

### H-3 · «Que eso quede como una regla»

- **Qué pasó:** el usuario no pidió solo que se subiera así: pidió que la forma de subir quedara escrita como regla.
- **Por qué importa:** sin la regla, la próxima sesión vuelve a mezclar. Con ella, el commit tiene una unidad que no depende de criterio.
- **Qué lo soluciona:** escribirla en el capítulo dueño de los commits, concretando la que ya pedía un propósito por commit.
- **Qué se decidió:** nace [`09·G9 · La historia de usuario es la unidad del commit`](../../../base/09-git.md), con su excepción: lo que no es de ninguna historia y una historia necesita para no citar lo que no está —el brief, el documento de su épica— sube con la primera que lo necesite.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`09·G9`](../../../base/09-git.md).
- **Nace en:** 2026-08-13 · pendientes del diplomado de IA.
- **Cerrado en:** 2026-08-13 · pendientes del diplomado de IA.
- **Con qué se retoma:** —.

### H-4 · La regla quedó escrita y sin subir, porque `VERSION` estaba ocupada

- **Qué pasó:** subir una regla obliga a subir el número de versión, y ese archivo lo estaba usando otra sesión en ese momento: en disco iba en `8.2.0` sin commitear y en el repositorio en `8.0.0`.
- **Por qué importa:** es la cuarta vez en una semana que `VERSION` y el `CHANGELOG` bloquean a una sesión por ser los dos archivos que todas tocan.
- **Qué lo soluciona:** esperar a que la otra sesión suba lo suyo, y commitear la regla sola con su versión.
- **Qué se decidió:** esperar. La pregunta quedó abierta en la sesión.
- **Estado:** resuelto, pero en otra sesión.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [pendientes/hecho/dos-sesiones-versionando-a-la-vez.md](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), que recoge el choque; `G9` está hoy publicada en [base/09-git.md](../../../base/09-git.md).
- **Nace en:** 2026-08-13 · pendientes del diplomado de IA.
- **Cerrado en:** 2026-08-14 · plan de trabajo de la EP-001.
- **Con qué se retoma:** —.

### H-5 · «No entiendo todo eso, menos es más»

- **Qué pasó:** el agente explicó el bloqueo de `VERSION` en un párrafo largo con rutas y números. El usuario lo cortó.
- **Por qué importa:** el bloqueo cabía en tres líneas, y lo único que el usuario tenía que decidir era esperar o no.
- **Qué lo soluciona:** decir qué ya está, qué falta y qué hay que decidir. Nada más.
- **Qué se decidió:** el agente lo reescribió en cuatro frases y terminó con la única pregunta que importaba.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [respuestas cortas](../../memory/respuestas-cortas.md).
- **Nace en:** 2026-08-13 · pendientes del diplomado de IA.
- **Cerrado en:** 2026-08-13 · pendientes del diplomado de IA.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2, H-3 y H-5 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ los cinco del H-1 **son** los pendientes; H-4 quedó en el [22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ los pendientes y las ocho historias de EP-001; `G9` esperó a que se liberara `VERSION` |
