# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-que-hace-el-agente-sin-ia.md](../../2026-08-07-que-hace-el-agente-sin-ia.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)). «Responde a» y «dispara» van en `—`: las épicas nacieron el 2026-08-13.

**Viene de:** —, es trabajo nuevo.

**Propósito:** saber qué puede hacer el agente sin la IA, y dejarlo escrito.

---

## Hallazgos de esta sesión

### H-1 · Nadie había separado lo que corre solo de lo que necesita criterio

- **Qué pasó:** a la pregunta «¿qué capacidades tiene el agente sin la ayuda de la IA?», el inventario resultó ser: 23 validadores, 5 enganches, el enganche de git, la memoria, las métricas, el visor y el instalador — todo Python, todo sin IA. Lo que no corre sin IA son las reglas, las skills y los prompts, que son texto que alguien tiene que aplicar.
- **Por qué importa:** es la frontera que ordena el backlog desde entonces. *Completitud se comprueba; calidad se juzga.*
- **Qué lo soluciona:** un documento que lo explique, en una carpeta propia.
- **Qué se decidió:** nace [anatomia/componentes-del-agente.md](../../../anatomia/componentes-del-agente.md) y, enseguida, el [mapa del sitio](../../../anatomia/mapa-del-sitio.md) con las cuatro zonas del repositorio y el dato que más se olvida: **solo la zona Norma viaja a los proyectos que heredan**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la carpeta [anatomia/](../../../anatomia/mapa-del-sitio.md).
- **Nace en:** 2026-08-07 · qué hace el agente sin IA.
- **Cerrado en:** 2026-08-07 · qué hace el agente sin IA.
- **Con qué se retoma:** —.

### H-2 · «Inventario» prometía una lista y adentro había una explicación

- **Qué pasó:** el usuario pidió el documento en una carpeta llamada `inventario` y, de paso, que el agente dijera si el nombre era el adecuado. No lo era: un inventario cuenta existencias, y el documento explica cómo encajan las piezas.
- **Por qué importa:** el nombre de una carpeta es la primera promesa que se le hace a quien busca algo. Si promete mal, el documento no se encuentra.
- **Qué lo soluciona:** un nombre que diga la intención.
- **Qué se decidió:** `anatomia/`. Se descartaron `arquitectura/` —choca con la skill que trata la arquitectura del proyecto, no la del agente— y `catalogo/`, que promete lista igual que `inventario`.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la carpeta [anatomia/](../../../anatomia/mapa-del-sitio.md).
- **Nace en:** 2026-08-07 · qué hace el agente sin IA.
- **Cerrado en:** 2026-08-07 · qué hace el agente sin IA.
- **Con qué se retoma:** —.

### H-3 · El mapa del sitio depende de que alguien se acuerde de actualizarlo

- **Qué pasó:** el usuario pidió que el mapa se mantenga al día cada vez que se agregue o se quite un componente. Eso quedó escrito **dentro del propio documento**.
- **Por qué importa:** es el letrero otra vez. Un mapa desactualizado es peor que ninguno: dice dónde están las cosas y se equivoca.
- **Qué lo soluciona:** escribirlo en el `CLAUDE.md` y, como se puede comprobar sin criterio, un validador que compare el árbol del mapa contra el disco.
- **Qué se decidió:** nada. El agente lo propuso y esperó el visto bueno; tampoco se agregó la fila de `anatomia/` a la tabla del [CLAUDE.md](../../../CLAUDE.md) §3, que sigue sin estar.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es una fila en una tabla y un validador chico.
- **Orden de resolución:** 1 de 2. Va primero: es más barato que el otro y hoy la tabla del `CLAUDE.md` no nombra la carpeta.
- **Dónde queda:** [pendientes/33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-07 · qué hace el agente sin IA.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿el mapa se comprueba con un validador, o se deja como documento que se actualiza a mano?

### H-4 · Ejecutar una fase y comprobar que se ejecutó bien no son lo mismo

- **Qué pasó:** el usuario preguntó si el agente ya puede ejecutar las fases de una historia. Sí puede: el orquestador dirige las estaciones y las skills hacen el trabajo. Lo que falta es **comprobarlo mecánicamente** — y en particular la puerta `F2`, que hoy verifica el agente leyendo, no un programa.
- **Por qué importa:** si el agente se salta `F2`, nada lo detiene. Es la puerta que define el estándar y es la única sin mecanismo.
- **Qué lo soluciona:** los validadores que faltan, empezando por los que no necesitan diseño.
- **Qué se decidió:** el agente corrigió su propia respuesta anterior, que mezclaba las dos cosas. Y dijo lo incómodo: **nada de esto se ha corrido punta a punta contra un proyecto real**.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, ya está anotado.
- **Orden de resolución:** 2 de 2.
- **Dónde queda:** [pendientes/01](../../../pendientes/01-validadores-de-codigo-de-proyecto.md). El gate `F2` sigue sin validador; el [pendiente 30](../../../pendientes/30-el-checklist-no-ve-la-cadena.md), del 2026-08-15, es el mismo hueco visto desde un proyecto real.
- **Nace en:** 2026-08-07 · qué hace el agente sin IA.
- **Cerrado en:** —.
- **Con qué se retoma:** la respuesta del propio agente: probarlo de brief a fase cerrada en un proyecto real **antes** de construir nada más.

### H-5 · Lo que el agente tiene que recordar es un backlog, no una virtud

- **Qué pasó:** el usuario pidió el análisis completo de qué podría funcionar sin IA. Salieron **16 automatizaciones**, verificadas contra el código para que ninguna existiera ya.
- **Por qué importa:** tres de ellas destapan agujeros reales: el histórico **puede filtrar un secreto** —copia el chat literal a un archivo versionado y ningún validador lo revisa—, nada obliga a subir `VERSION`, y las meta-reglas del capítulo 20 son las únicas que nadie comprueba.
- **Qué lo soluciona:** construir primero las cinco de complejidad baja, y dejar el gate `F2` para el final: sin las otras daría tantos falsos positivos que se terminaría apagando, y un control apagado es peor que ninguno porque figura como cubierto.
- **Qué se decidió:** se escribió el backlog. No se construyó nada — la recomendación del propio agente fue no construir todavía y probar el estándar en un proyecto real primero.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es el pendiente 09 completo.
- **Orden de resolución:** —, cada ítem se promueve a su propio pendiente cuando se vaya a construir.
- **Dónde queda:** [pendientes/09-autonomia-sin-ia.md](../../../pendientes/09-autonomia-sin-ia.md).
- **Nace en:** 2026-08-07 · qué hace el agente sin IA.
- **Cerrado en:** —.
- **Con qué se retoma:** de los 16, ¿cuál se construye primero? La recomendación escrita es `estado.py`, porque otras tres dependen de ella.

### H-6 · El agente analizó una carpeta que la instrucción no nombraba

- **Qué pasó:** el usuario lo cortó a mitad: *«pero por qué está analizando diplomado si esa no fue la instrucción»*.
- **Por qué importa:** es la tercera vez en dos días que aparece lo mismo — el agente amplía el alcance por su cuenta.
- **Qué lo soluciona:** hacer lo que se pidió, y nada más.
- **Qué se decidió:** el agente rehízo el trabajo sobre lo que sí se le pidió y creó la carpeta donde correspondía.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [trabajo confinado a la carpeta](../../memory/trabajo-confinado-a-la-carpeta.md).
- **Nace en:** 2026-08-07 · qué hace el agente sin IA.
- **Cerrado en:** 2026-08-07 · qué hace el agente sin IA.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, H-2 y H-6 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-3 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), H-4 en el [01](../../../pendientes/01-validadores-de-codigo-de-proyecto.md), H-5 en el [09](../../../pendientes/09-autonomia-sin-ia.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ está en el repositorio desde entonces |
