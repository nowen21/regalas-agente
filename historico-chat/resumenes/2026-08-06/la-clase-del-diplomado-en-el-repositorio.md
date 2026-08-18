# 2026-08-06 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-06-la-clase-del-diplomado-en-el-repositorio.md](../../2026-08-06-la-clase-del-diplomado-en-el-repositorio.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-15.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).
>
> **Tuvo una copia.** `2026-08-06-sesion-9.md` repetía esta conversación resumida a mano, con las horas inventadas. Se borró el 2026-08-16; sigue en el historial de git, y con ella la descripción de cada diapositiva, que solo estaba ahí.

**Viene de:** —, es trabajo nuevo.

**Propósito:** pasar a texto las diapositivas de la primera clase del diplomado de IA.

---

## Hallazgos de esta sesión

### H-1 · Material que no es del estándar entró al repositorio del estándar

- **Qué pasó:** se creó `diplomado-ia/` en la raíz de este repositorio y ahí quedaron 25 archivos de una clase: doce imágenes y sus transcripciones, más los `README` del módulo y del diplomado.
- **Por qué importa:** este repositorio **es el estándar**. Lo que no es regla, plantilla, validador o bitácora no va acá: se mezcla con lo que se hereda, y de hecho rompió una prueba de enlaces el mismo día.
- **Qué lo soluciona:** sacarlo a la carpeta del posgrado, que es donde vive.
- **Qué se decidió:** en la sesión no se decidió; el material se organizó dentro del repositorio. Al día siguiente el usuario pidió moverlo, y ahí salió.
- **Estado:** resuelto, pero en otra sesión.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** se movió a `Escom/…/Proyecto de grado/diplomado-ia/` en la sesión del [2026-08-07](../../2026-08-07-la-carpeta-del-diplomado-sale-del-repositorio.md). Lo que sí volvió al estándar fueron los [pendientes 13 a 16](../../../pendientes/README.md), que salieron de comparar esos apuntes contra el repositorio.
- **Nace en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Cerrado en:** 2026-08-07 · sesión 2.
- **Con qué se retoma:** —.

### H-2 · Una imagen pegada en el chat no se puede guardar

- **Qué pasó:** el usuario pidió transcribir la imagen **y guardarla** en la carpeta. El agente transcribió, pero la imagen llegó pegada en el chat, no como archivo en disco: no tiene sus bytes para escribirla.
- **Por qué importa:** es un límite que se repite y conviene saber de antemano. Cuando la imagen sí está en disco, el agente la lee y hasta la renombra.
- **Qué lo soluciona:** el `.md` referencia el nombre que va a tener y el usuario deja la imagen ahí.
- **Qué se decidió:** eso mismo: el agente dejó la referencia puesta y el usuario guardó las imágenes con el nombre acordado.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** en la conversación. No quedó escrito en ninguna parte.
- **Nace en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Cerrado en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Con qué se retoma:** —.

### H-3 · «Que ese resumen lo entienda un niño»

- **Qué pasó:** al pedir el índice de la clase, el usuario puso la condición: *«que ese resumen lo entienda un niño»*. El agente cambió la tabla por secciones, porque en una celda no cabe una explicación así.
- **Por qué importa:** es la primera vez que aparece la exigencia de redacción que dos días después se vuelve regla del estándar y hoy rige **todo** lo que el agente escribe, reglas incluidas.
- **Qué lo soluciona:** escribir para quien no sabe del tema, sin jerga.
- **Qué se decidió:** se aplicó a los tres `README` de la clase, del módulo y del diplomado.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [estilo de redacción simple](../../memory/estilo-redaccion-simple.md), y hoy la regla `00·ID7`, nacida en la sesión del [2026-08-08](../../2026-08-08-escribir-para-que-lo-entienda-quien-no-sabe.md) con la v6.0.0 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Cerrado en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Con qué se retoma:** —.

### H-4 · La transcripción se escribió dos veces, y con horas iguales

- **Qué pasó:** además del archivo que escribió el enganche, quedó `2026-08-06-sesion-9.md` con la misma conversación resumida a mano. Ahí la hora del usuario y la del agente son **idénticas al segundo** en los 21 intercambios: no se leyeron del reloj.
- **Por qué importa:** es el mismo defecto del [pendiente 29](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md), nueve días antes. Y responde lo que ese pendiente dejó preguntado: sí, le pasó a más sesiones — dos veces solo el 2026-08-06.
- **Qué lo soluciona:** revisar el histórico completo y quedarse con lo que escribió el enganche.
- **Qué se decidió:** nada en su momento; nadie lo notó hasta el 2026-08-15.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, cae dentro del pendiente 29.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/hecho/la-transcripcion-duplicada-del-15.md](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md).
- **Nace en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Cerrado en:** —.
- **Con qué se retoma:** de las dos copias, ¿cuál se borra? La del enganche trae las horas reales; la de a mano trae las imágenes descritas.

### H-5 · Una explicación de otro tema quedó dentro de esta sesión

- **Qué pasó:** en medio de la clase, el usuario preguntó por la regla `F0` y el agente la explicó entera. Después avisó: *«perdón, eso no era de esta sesión»*.
- **Por qué importa:** el histórico es transcripción literal, así que el intercambio quedó ahí, en una sesión que trata de otra cosa. Quien busque esa explicación de `F0` no la va a encontrar nunca por el título.
- **Qué lo soluciona:** nada que se hiciera entonces. Hoy sería el índice temático que quedó planteado el [2026-08-14](../../2026-08-14-indice-tematico-del-historico.md).
- **Qué se decidió:** no se tocó nada — no hubo cambio en `base/`, ni en el `CHANGELOG`, ni en `VERSION`. El intercambio se quedó en la transcripción.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la transcripción de esta sesión, intercambios 16 a 18.
- **Nace en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Cerrado en:** 2026-08-06 · la clase del diplomado en el repositorio.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2, H-3 y H-5; H-1 se cerró al día siguiente |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-4 va al [29](../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ está en el repositorio desde entonces |
