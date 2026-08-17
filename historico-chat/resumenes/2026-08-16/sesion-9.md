# 2026-08-16 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-sesion-9.md](../../2026-08-16-sesion-9.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** 2026-08-16 · las HU sin su fase · H-1. Ese hallazgo sigue abierto y se trabaja allá; acá solo van los nuevos.

---

## Hallazgos de esta sesión

### H-1 · La casilla «Fase» marcaría una carpeta que git no guarda

- **Qué pasó:** el paso 2 del inventario dice «se crea la carpeta `<letra>-EP-0NN-HU-0NN-<slug>` y se marca **Fase**». Git no registra carpetas vacías, así que las 51 carpetas quedarían solo en esta máquina y la ☑ afirmaría algo que ningún clon puede ver.
- **Por qué importa:** el inventario existe para no tener que recorrer las carpetas a mano. Una columna que dice ☑ sobre algo que no está en ningún commit lo vuelve menos confiable que contar a mano — que es justo lo que vino a evitar.
- **Qué lo soluciona:**
  **EP-003 · HU nueva — El procedimiento del inventario dice qué deja escrito en el repositorio**
  - **Como** quien llena un inventario de HU
  - **Quiero** que el paso que crea la fase diga qué archivo la hace visible en el control de versiones
  - **Para** que la casilla marcada signifique lo mismo en mi máquina y en un clon recién bajado.
  - **Contexto:** hoy [`plantillas/inventario-hu.md`](../../../plantillas/inventario-hu.md) y el pendiente [48](../../../pendientes/48-inventario-hu.md) dicen «se crea la carpeta y se marca Fase», sin más. Ninguna herramienta del repositorio guarda carpetas vacías, así que el procedimiento tal como está produce marcas que no se pueden comprobar.
- **Qué se decidió:** sin decidir. Se le pasaron al usuario las tres salidas —`.gitkeep` en cada carpeta, carpeta sola, o escribir ya el `plan_trabajo.md`— con la primera recomendada. Nada se creó mientras tanto.
- **Estado:** abierto
- **Responde a:** EP-004 · HU-017 — el inventario que esa HU va a contar es este mismo.
- **Dispara:** 1. EP-003 · HU nueva — el procedimiento del inventario declara qué deja en el repositorio. Va antes de llenar las 51 filas: si se llenan primero, hay que rehacerlas.
- **Orden de resolución:** 1 de 2 · bloquea el trabajo que pidió la sesión.
- **Dónde queda:** pendiente [57](../../../pendientes/57-la-fase-recien-abierta-no-queda-en-el-repositorio.md), con las tres salidas y la recomendación escritas · toca el [48](../../../pendientes/48-inventario-hu.md) y la plantilla [`inventario-hu.md`](../../../plantillas/inventario-hu.md)
- **Nace en:** 2026-08-16 · el inventario de HU
- **Cerrado en:** —
- **Con qué se retoma:** ¿con qué archivo se hace visible una fase recién abierta, antes de que tenga su `plan_trabajo.md`?

### H-2 · El conteo del backlog y el del inventario se separan solos

- **Qué pasó:** la línea del 48 en [`pendientes/README.md`](../../../pendientes/README.md) decía «52 de las 66 HU · 49 sin ninguna fase» cuando la tabla del propio pendiente ya iba en 68, 54 y 51. Dos HU nacidas el mismo día movieron un número y no el otro.
- **Por qué importa:** el README es por donde se entra al backlog. Si su número no es el de la tabla, la prioridad del pendiente se decide sobre un dato viejo.
- **Qué lo soluciona:** es exactamente lo que hace la HU-017 ya escrita — que la cuenta la haga un programa y no una edición a mano. No abre historia nueva.
- **Qué se decidió:** se corrigió a mano la línea del README a 68 · 54 · 51, y se dejó intacto el número del [`CHANGELOG.md`](../../../CHANGELOG.md), que es el registro de lo que era cierto ese día.
- **Estado:** resuelto acá
- **Responde a:** EP-004 · [HU-017 — Decir cuántas HU quedan sin su fase completa](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md)
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [`pendientes/README.md`](../../../pendientes/README.md) · el pendiente pasa a llamarse [`48-inventario-hu.md`](../../../pendientes/48-inventario-hu.md)
- **Nace en:** 2026-08-16 · el inventario de HU
- **Cerrado en:** 2026-08-16 · el inventario de HU
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ · el H-2 dice qué se corrigió y qué se dejó intacto |
| Todo hallazgo abierto tiene su pendiente creado | ☑ · el H-1 quedó en el [57](../../../pendientes/57-la-fase-recien-abierta-no-queda-en-el-repositorio.md) |
| Toda historia disparada está escrita en su épica | ☐ · la HU de EP-003 que dispara el H-1 no se escribió: qué exige depende de la decisión que el 57 deja abierta |
| Lo que se hizo está aprobado y guardado | ☑ · el usuario pidió subir todo lo que había |

**Queda una sin marcar, y a propósito.** La historia que dispara el H-1 no se puede redactar hoy: su criterio de aceptación sería «la fase se ve en un clon nuevo», y con qué archivo se logra es justo lo que falta decidir. Escribirla antes obligaría a rehacerla. El hallazgo no se pierde porque el 57 lo sostiene y nombra qué hay que tocar cuando se decida.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: resumen sin hallazgos -->

<!-- aviso: falta decir si la sesión se puede cerrar -->
