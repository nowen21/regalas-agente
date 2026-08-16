# 2026-08-15 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-15-la-plantilla-del-resultado-de-pruebas.md](../../2026-08-15-la-plantilla-del-resultado-de-pruebas.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo.

**Propósito:** que la plantilla del resultado de pruebas diga, sección por sección, **qué pregunta se responde ahí**, y que lo que pide sea tan detallado que la prueba se pueda repetir sin haber estado. Después, aplicarla al resultado de pruebas de una fase real para ver si aguanta.

---

## Hallazgos de esta sesión

### H-1 · Las secciones de la plantilla no decían qué se responde en ellas

- **Qué pasó:** las secciones 0, 1 y 2 de [plantillas/planes/resultados.md](../../../plantillas/planes/resultados.md) arrancaban directo en la tabla.
- **Por qué importa:** una sección que no dice qué responde se llena como trámite. Se pone algo en cada celda y nadie nota que no contesta nada.
- **Qué lo soluciona:** cada sección abre con su pregunta y con qué se hace ahí para responderla.
- **Qué se decidió:** §0 «¿qué se está probando?», §1 «¿cuántas pruebas se planearon, cuántas se hicieron y cómo les fue?», §2 «¿qué problema resuelve cada pareja CA–CP?».
- **Estado:** resuelto acá.
- **Responde a:** EP-003, documentos modelo y procedimientos.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/planes/resultados.md](../../../plantillas/planes/resultados.md), versión 15.4.2 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Con qué se retoma:** —.

### H-2 · «Corrida» era jerga y no estaba definida

- **Qué pasó:** la plantilla usaba «corrida» sin decir qué es. En el [glosario](../../../base/glosario.md) solo existe dentro de «alcance de corrida», no como término propio.
- **Por qué importa:** quien no es del oficio no sabe si una corrida es un caso, una suite o un día de pruebas — y de eso depende cómo se llena la columna **Ciclo**.
- **Qué lo soluciona:** cambiar la palabra por «ejecución» y decir qué es donde se usa.
- **Qué se decidió:** en esa plantilla, «corrida» pasa a «ejecución», y §1 dice: correr las pruebas de principio a fin.
- **Estado:** abierto.
- **Responde a:** EP-003 · HU-010, el glosario de la terminología.
- **Dispara:** —, es replicar lo mismo en otros archivos.
- **Orden de resolución:** 3 de 3. Va último: no bloquea nada, es limpieza de vocabulario.
- **Dónde queda:** [pendientes/26](../../../pendientes/26-corrida-y-ejecucion-en-el-estandar.md). Cambiado solo en [plantillas/planes/resultados.md](../../../plantillas/planes/resultados.md); sigue en [base/02-flujo-de-trabajo](../../../base/02-flujo-de-trabajo/base.md), [base/08-pruebas.md](../../../base/08-pruebas.md), [base/glosario.md](../../../base/glosario.md) y [plantillas/planes/pruebas.md](../../../plantillas/planes/pruebas.md).
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿se reemplaza «corrida» en todo el estándar, o se define en el glosario y se deja?

### H-3 · La sección 2 pedía lo mismo dos veces

- **Qué pasó:** §2 tenía el bloque nuevo por pareja `CA`–`CP` y, más abajo, un «Detalle de `CP-00N`» con tres partes. Pedían lo mismo con nombres distintos.
- **Por qué importa:** cuando dos instrucciones piden lo mismo, quien escribe elige la más corta y cree que cumplió.
- **Qué lo soluciona:** un solo bloque, con las tres partes y con lo que hacía falta para que «detallado» no dependa de opinión.
- **Qué se decidió:** queda el bloque por pareja; se borró el «Detalle de `CP-00N`». Se agregaron las cuatro reglas del paso a paso.
- **Estado:** resuelto acá.
- **Responde a:** EP-003.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/planes/resultados.md](../../../plantillas/planes/resultados.md) §2, versión 16.0.0.
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Con qué se retoma:** —.

### H-4 · Un paso con dos acciones pierde la mitad de lo que salió

- **Qué pasó:** el plan de la fase decía «tomar la lista de origen **y** contar cuántos términos tiene» en una fila, con un solo renglón de resultado. Al ejecutar quedó anotado el conteo y se perdió de dónde salió la lista.
- **Por qué importa:** el caso quedó en «aprobado» con la mitad sin comprobar, y nadie lo vio hasta bajarlo a la forma nueva.
- **Qué lo soluciona:** que el plan exija un paso, una acción.
- **Qué se decidió:** [plantillas/planes/pruebas.md](../../../plantillas/planes/pruebas.md) §6 lo exige, con ejemplo INCORRECTO/CORRECTO. Se aplicó al plan de la fase (versión 1.1): seis pasos partidos o reescritos.
- **Estado:** resuelto acá.
- **Responde a:** EP-003.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/planes/pruebas.md](../../../plantillas/planes/pruebas.md) §6, versión **16.0.0 · MAYOR ⚠ obliga a migrar**.
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Con qué se retoma:** —.

### H-5 · Los pasos de partida estaban dados por supuestos

- **Qué pasó:** dos casos del plan no decían cómo se llega al punto de partida. CP-004 no decía cómo se eligen las tres entradas de muestra; CP-006 no decía que hay que conseguir a alguien que no haya escrito el glosario.
- **Por qué importa:** en CP-006 ese paso invisible era **lo que tenía el caso bloqueado**, y el bloqueo solo se leía en una nota al margen en vez de en una fila.
- **Qué lo soluciona:** que la plantilla diga que se arranca desde cero y que lo que haya que **hacer** para llegar al punto de partida es un paso, no una precondición.
- **Qué se decidió:** es una de las cuatro reglas de §2. Se aplicó al plan de la fase (versión 1.2).
- **Estado:** resuelto acá.
- **Responde a:** EP-003.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [plantillas/planes/resultados.md](../../../plantillas/planes/resultados.md) §2, versión 16.0.0.
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Con qué se retoma:** —.

### H-6 · La fase A de EP-003 · HU-010 no cumple

- **Qué pasó:** al bajar su [resultado_pruebas.md](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md) a la plantilla, el veredicto pasó de «aprobada con una prueba pendiente» a **No cumple**: `RNF-01` no tiene caso ejecutado y **16 de los 35 pasos del plan no dejaron registro de qué salió**, más 3 que se hicieron distinto.
- **Por qué importa:** la fase se dio por cerrada con criterios en «cumple» que no tienen respaldo. Es el mismo defecto que ya pasó en `A-EP-005-HU-008` y que la sesión del 2026-08-14 documentó.
- **Qué lo soluciona:** correr lo que falta y volver a dar veredicto.
- **Qué se decidió:** el documento queda con el veredicto real. No se reejecutó nada en esta sesión.
- **Estado:** abierto.
- **Responde a:** EP-003 · HU-010 · RNF-01.
- **Dispara:** —, no abre historia nueva: es reabrir la fase A que ya existe.
- **Orden de resolución:** 1 de 3. Va primero: mientras no se resuelva, la fase está cerrada con un veredicto que no era.
- **Dónde queda:** [pendientes/27](../../../pendientes/27-la-fase-a-de-hu-010-cerro-sin-cumplir.md), y D-04 del [resultado_pruebas.md](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/resultado_pruebas.md) de la fase.
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿quién lee las cinco entradas de CP-006, y se reejecutan los 16 pasos sin registro o se deja escrito por qué no?

### H-7 · El `estado-fase.md` de esa fase contradice su resultado

- **Qué pasó:** [estado-fase.md](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/estado-fase.md) sigue diciendo «aprobada con una prueba pendiente»; el resultado dice «No cumple».
- **Por qué importa:** el `estado-fase` es lo que se mira para pasar la puerta de verificación. Si dice que cumple, la fase pasa sin que nadie abra el resultado.
- **Qué lo soluciona:** copiar el veredicto real, o —mejor— que un validador no deje que los dos digan cosas distintas.
- **Qué se decidió:** sin decidir. No se tocó el archivo porque el usuario no lo pidió.
- **Estado:** abierto.
- **Responde a:** EP-004, la comprobación automática.
- **Dispara:** [EP-004 · HU-014](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) — «un solo veredicto por fase», ya escrita.
  - **Como** quien revisa una fase
  - **Quiero** que el concepto del `resultado_pruebas` y el del `estado-fase` no puedan decir cosas distintas
  - **Para** no pasar una puerta de verificación con un veredicto viejo
  - **Contexto:** hoy el veredicto se escribe a mano en los dos archivos. Nada comprueba que coincidan, y esta sesión dejó un caso donde ya no coinciden. Si no se hace, la puerta de verificación se apoya en el archivo que nadie actualizó.
- **Orden de resolución:** 2 de 3. Va después de H-6: primero hay que saber cuál es el veredicto bueno.
- **Dónde queda:** [pendientes/28](../../../pendientes/28-el-veredicto-de-la-fase-vive-en-dos-sitios.md) y [EP-004 · HU-014](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md).
- **Nace en:** 2026-08-15 · plantilla del resultado de pruebas.
- **Cerrado en:** —.
- **Con qué se retoma:** ¿se corrige el `estado-fase` a mano ahora, o se espera al validador que lo compare?

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, H-3, H-4 y H-5 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ [26](../../../pendientes/26-corrida-y-ejecucion-en-el-estandar.md), [27](../../../pendientes/27-la-fase-a-de-hu-010-cerro-sin-cumplir.md) y [28](../../../pendientes/28-el-veredicto-de-la-fase-vive-en-dos-sitios.md) |
| Toda historia disparada está escrita en su épica | ☑ [EP-004 · HU-014](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) |
| Lo que se hizo está aprobado y guardado | ☐ sin aprobar y sin commit |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
