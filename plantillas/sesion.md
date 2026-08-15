# Lo que sale de una sesión  ·  `[CAPA 3]`

> Plantilla. **No es el resumen del final**: un chat no tiene final, y lo que se deja para el cierre no se escribe nunca. Se llena **en el momento en que aparece el hallazgo**, con doce campos. Reemplaza los `«…»` y borra esta caja.
>
> La conversación entera ya queda en la transcripción de la sesión (`historico-chat/`), que sigue su curso y no se toca. Esto es lo otro: lo que la sesión **dejó** y hay que poder encontrar sin releerla. Se guarda en `historico-chat/resumenes/AAAA-MM-DD/<tema>.md`: **una carpeta por día y un archivo por sesión**, con su línea en el índice de ese día.

## Doce campos

| Campo | Qué se escribe |
|---|---|
| **Qué pasó** | El hecho, en una frase. Sin interpretación. |
| **Por qué importa** | Qué se pierde o qué cuesta si nadie lo sabe. |
| **Qué lo soluciona** | La solución **partida en piezas**, una por cada historia que dispara. Cada pieza trae su narrativa y su contexto, que es lo que esa historia necesita para nacer. |
| **Qué se decidió** | La decisión, o "sin decidir" si quedó abierta. |
| **Estado** | `resuelto acá` o `abierto`. |
| **Responde a** | La épica, la historia y el criterio de aceptación que este hallazgo cumple. `—` si no cae dentro de nada planeado. |
| **Dispara** | La épica, la historia o el criterio **nuevo** que hace falta crear por causa de este hallazgo. Si es más de uno, **numerados en el orden en que se resuelven**, y cada uno con por qué va ahí. `—` si no abre trabajo. |
| **Orden de resolución** | En qué puesto va este hallazgo entre los que quedaron abiertos, y por qué. En los resueltos, `—`. |
| **Dónde queda** | Señal, pendiente, regla o memoria. |
| **Nace en** | La sesión donde apareció: `AAAA-MM-DD · tema`. No cambia nunca, ni cuando el hallazgo se arrastra a otra sesión. |
| **Cerrado en** | La sesión donde se cerró: `AAAA-MM-DD · tema`. Mientras esté abierto, `—`. |
| **Con qué se retoma** | La pregunta que quedó viva. En los resueltos, `—`. |

**«Qué lo soluciona» es la semilla de las historias que dispara.** No basta con decir a dónde se llega: quien tome el hallazgo mañana tiene que poder escribir la historia sin haber estado en la conversación. Por eso cada pieza se escribe con las dos secciones que abren una historia de usuario:

```
**EP-000 · HU nueva — «título»**
- **Como** «rol»
- **Quiero** «capacidad»
- **Para** «beneficio»
- **Contexto:** qué hay hoy, qué falta y qué se rompe si no se hace.
```

**Una pieza, una historia.** Si una pieza no aparece en «dispara», o una historia disparada no sale de ninguna pieza, el hallazgo está mal escrito.

**El orden de las historias se escribe en el hallazgo, y en ninguna otra parte.** Las épicas están cortadas por tipo de entregable (un documento modelo y el programa que lo llena caen en épicas distintas), así que un problema partido en dos historias no deja ver su orden desde ninguna de las dos. El hallazgo es el único sitio donde el problema está entero. Por eso «dispara» los numera, y nombra también lo que las bloquea aunque este hallazgo no lo haya disparado:

```
**Dispara:**
1. EP-000 · HU-000 — «por qué va primero». No sale de este hallazgo: la bloquea.
2. EP-000 · HU-000 — «por qué va después de la anterior».
```

**Nace en y cerrado en son el rastro del hallazgo.** El primero no cambia nunca; el segundo se llena el día que se cierra, aunque sea tres sesiones después. Sin los dos no se puede seguir un hallazgo que se arrastra.

**Un hallazgo se nombra `AAAA-MM-DD · tema · H-N`.** Cada resumen numera los suyos desde `H-1`, así que el número solo no identifica nada: "el H-4" existe en todas las sesiones que tuvieron cuatro hallazgos. La numeración corrida entre sesiones no sirve: obligaría a un contador único, y dos sesiones abiertas a la vez lo rompen.

**El hallazgo que se hereda no se copia.** La sesión que retoma un hallazgo abierto de otra lo **nombra** en su «viene de» y trabaja sobre el original: ahí actualiza el estado, el «cerrado en» y lo que se decidió. Copiarlo al resumen nuevo deja dos versiones del mismo hallazgo, y la que manda termina siendo la que nadie está mirando.

**Los dos del medio son los que enganchan el hallazgo con el trabajo.** Uno mira hacia atrás: esto que apareció, ¿ya estaba pedido en alguna parte? El otro mira hacia adelante: resolverlo, ¿obliga a abrir una historia nueva? Un hallazgo con los dos en `—` no es trabajo: es una nota, y probablemente sea una señal y nada más.

**Se anotan todos**, los resueltos también. El que se resolvió en la sesión sirve para que nadie vuelva a discutirlo, y el que quedó abierto sirve para arrancar la próxima discusión sin empezar de cero. Por eso el estado, el «cerrado en» y el «con qué se retoma» importan más que el resto: dicen si está cerrado, dónde se cerró y por dónde sigue.

## Dónde termina cada cosa

| Si es… | Va a… |
|---|---|
| Algo que se **aprendió** y no se recupera del código | `documentacion/senales.md` (`13·DOC5`) |
| Algo que **falta hacer** | `pendientes/` |
| Algo que **hay que exigir siempre** | Una regla de `base/`, por el procedimiento del capítulo `20` |
| Cómo quiere trabajar **el usuario** | `historico-chat/memory/` (`01·C19`) |

Un hallazgo que no cabe en ninguno de los cuatro no era un hallazgo: era conversación, y ya quedó en la transcripción.

---

## De dónde viene esta sesión

Una sesión se abre por dos motivos: porque hay trabajo nuevo, o porque alguien fue a buscar un hallazgo que otra sesión dejó abierto. En el segundo caso hay que decir **cuál**, con su fecha, su tema y su número:

**Viene de:** «AAAA-MM-DD · tema · H-N» / «—, es trabajo nuevo»

Es el enlace hacia adelante. El de vuelta ya existe: el «cerrado en» de ese hallazgo apunta a esta sesión el día que se cierre. Sin los dos, un hallazgo que se arrastra tres sesiones no se puede seguir en ninguna dirección.

Si la sesión atiende más de un hallazgo, se nombran todos.

**Ese hallazgo no se copia acá.** Se nombra, y lo que se decida se escribe en el resumen donde nació. Este resumen anota los hallazgos **nuevos**, los que aparecieron en esta sesión.

---

## Hallazgos de esta sesión

### H-1 · «título corto»

- **Qué pasó:** «…»
- **Por qué importa:** «…»
- **Qué lo soluciona:**
  **EP-000 · HU nueva — «título»**
  - **Como** «rol»
  - **Quiero** «capacidad»
  - **Para** «beneficio»
  - **Contexto:** «qué hay hoy, qué falta y qué se rompe si no se hace».
- **Qué se decidió:** «…»
- **Estado:** «resuelto acá / abierto»
- **Responde a:** «EP-000 · HU-000 · CA-00» / «—»
- **Dispara:** «EP-000 · HU-000 nueva» / «numeradas, si son varias» / «—»
- **Orden de resolución:** «n de N · por qué va ahí» / «—»
- **Dónde queda:** «señal S-00 / pendiente NN / regla NN·Xn / memoria»
- **Nace en:** «AAAA-MM-DD · tema de la sesión»
- **Cerrado en:** «AAAA-MM-DD · tema de la sesión» / «—»
- **Con qué se retoma:** «la pregunta que quedó viva» / «—»

### H-2 · «…»

- **Qué pasó:** «…»
- **Por qué importa:** «…»
- **Qué lo soluciona:** «una pieza por cada historia que dispara, con su narrativa y su contexto»
- **Qué se decidió:** «…»
- **Estado:** «…»
- **Responde a:** «…»
- **Dispara:** «…»
- **Orden de resolución:** «…»
- **Dónde queda:** «…»
- **Nace en:** «…»
- **Cerrado en:** «…»
- **Con qué se retoma:** «…»

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☐ |
| Todo hallazgo abierto tiene su pendiente creado | ☐ |
| Toda historia disparada está escrita en su épica | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_
