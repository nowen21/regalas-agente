# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-13-hu-de-la-comprobacion-automatica.md](../../2026-08-13-hu-de-la-comprobacion-automatica.md), con la plantilla [`plantillas/sesion.md`](../../../plantillas/sesion.md). La conversación está allá; acá queda lo que la sesión dejó.

Se anotan todos, resueltos y abiertos. Los resueltos, para que nadie los vuelva a discutir; los abiertos, para arrancar la próxima discusión sin empezar de cero.

---

## Hallazgos

### H-1 · Se escribió código sin haber recorrido la cadena

- **Qué pasó:** salieron cinco validadores nuevos leyendo el pendiente 01, sin épica, sin historia de usuario y sin plan aprobado.
- **Por qué importa:** sin criterios de aceptación no hay contra qué verificar lo escrito, y nadie aprobó el alcance ni el costo.
- **Qué lo soluciona:**
  **EP-004 · HU-010, HU-011 y HU-012** — ya escritas en esta sesión. Eran las tres historias que faltaban para que el trabajo que se estaba haciendo tuviera de dónde colgar.
- **Qué se decidió:** lo escrito queda como línea base verificada, no como trabajo hecho. Se paró y se encadenó: 54 historias de usuario en las siete épicas y una fase abierta.
- **Estado:** abierto. Las tres historias y la fase quedaron escritas, pero el código que originó el hallazgo sigue sin plan aprobado: la cadena está puesta y este trabajo todavía no la recorrió.
- **Responde a:** —. El trabajo venía del pendiente 01, que no es una historia de usuario.
- **Dispara:** EP-004 · HU-010, HU-011 y HU-012, las tres que no existían y hacían falta para lo que se estaba escribiendo. Ya están escritas.
- **Orden de resolución:** 3 de 7 · aprobar los planes desbloquea el código que ya está escrito.
- **Dónde queda:** señal S-002 · la fase [documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/README.md), que es donde continúa. No lleva pendiente: su continuación ya está abierta.
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —
- **Con qué se retoma:** aprobar los dos planes de la fase `A-EP-004-HU-010` y rehacer bajo ellos los cinco validadores que hoy están sin commitear.

### H-2 · El estándar escribía en inglés lo que exige escribir en español

- **Qué pasó:** "spec" aparecía en 53 archivos, contra su propia regla [`01·C8`](../../../base/01-conducta.md#c8--habla-el-idioma-del-proyecto).
- **Por qué importa:** quien lee "falta la spec" no sabe qué documento le piden ni dónde ponerlo.
- **Qué lo soluciona:** la regla [`01·C20`](../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) y la traducción del texto, hechas en esta sesión. No dispara historias nuevas: cabía entero en EP-001 · HU-004.
- **Qué se decidió:** se tradujo el texto, sin tocar rutas ni nombres de archivo, y nació la regla que faltaba.
- **Estado:** resuelto acá.
- **Responde a:** EP-001 · HU-004, las reglas de conducta de la IA.
- **Dispara:** —
- **Orden de resolución:** —, ya está cerrado.
- **Dónde queda:** regla [`01·C20`](../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) · señal S-001 · versión 10.0.0.
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Con qué se retoma:** —

### H-3 · Explicar largo no es explicar

- **Qué pasó:** una pregunta de una línea se contestó tres veces seguidas con párrafos, tablas y opciones.
- **Por qué importa:** lo largo no se lee, así que la información se pierde igual que si no se hubiera escrito.
- **Qué lo soluciona:** la regla [`01·C5`](../../../base/01-conducta.md#c5--responde-corto), reescrita en esta sesión para cubrir también las explicaciones. No dispara historias nuevas.
- **Qué se decidió:** `C5` pasa a cubrir también las explicaciones, y "menos es más" queda fijado como señal de que hay que responder otra vez, más corto.
- **Estado:** resuelto acá.
- **Responde a:** EP-001 · HU-004, las reglas de conducta de la IA.
- **Dispara:** —
- **Orden de resolución:** —, ya está cerrado.
- **Dónde queda:** regla [`01·C5`](../../../base/01-conducta.md#c5--responde-corto) · memoria [respuestas-cortas.md](../../memory/respuestas-cortas.md) · versión 12.1.0.
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Con qué se retoma:** —

### H-4 · No había dónde escribir lo aprendido

- **Qué pasó:** [`13·DOC5`](../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) manda registrar señales y este repositorio no tenía el archivo donde escribirlas.
- **Por qué importa:** todo lo aprendido en la sesión iba a quedar solo en la transcripción, que nadie relee.
- **Qué lo soluciona:**

  **EP-003 · HU nueva — el modelo del resumen de sesión**
  - **Como** quien retoma un trabajo días después
  - **Quiero** un modelo fijo donde quede lo que cada sesión dejó
  - **Para** encontrarlo sin releer la conversación
  - **Contexto:** la transcripción guarda lo que se dijo, y es larga. Lo que quedó —hallazgos, decisiones, preguntas vivas— no tenía forma ni sitio, así que se perdía. El modelo existe desde hoy, con ocho campos por hallazgo, y falta someterlo al procedimiento de un documento modelo.

  **EP-005 · HU nueva — el enganche que sostiene el resumen**
  - **Como** quien retoma el trabajo días después
  - **Quiero** que el resumen exista aunque nadie se acuerde de escribirlo
  - **Para** no depender de la memoria del agente
  - **Contexto:** hoy la plantilla y la carpeta están, pero llenarlas depende de que el agente se acuerde. Es lo mismo que pasaba con la transcripción, que solo se escribió siempre cuando la escribió un programa. Tres piezas: crear el archivo al abrir la sesión, avisar cuando la sesión ya produjo algo y el resumen sigue vacío, y arrastrar a la siguiente lo que quedó sin cerrar.
- **Qué se decidió:** se creó el archivo de señales y la plantilla de lo que deja una sesión, con estado, trazabilidad y pregunta viva.
- **Estado:** **reabierto** el 2026-08-14 en la sesión `el-enganche-del-resumen-no-crea-el-resumen`. Se había cerrado ese mismo día, y el cierre no era cierto: el enganche que sostiene el resumen nunca lo crea, así que la mitad del hallazgo, *"que exista aunque nadie se acuerde"*, sigue sin cumplirse. La otra mitad, el sitio y el modelo, sí quedó.
- **Responde a:** EP-006 · HU-002, guardar lo aprendido en el repositorio.
- **Dispara:** EP-003 · HU-009 (el modelo del resumen) y EP-005 · HU-008 (el enganche que lo sostiene). Ya están escritas.
- **Orden de resolución:** —, ya está cerrado.
- **Dónde queda:** las tres fases de la cadena: [A-EP-003-HU-001](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md), [A-EP-003-HU-009](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-009-modelo-del-resumen-de-sesion/A-EP-003-HU-009-modelo-del-resumen-de-sesion/README.md) y [A-EP-005-HU-008](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md) · reglas [`13·DOC19`](../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) a [`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) · [plantillas/sesion.md](../../../plantillas/sesion.md) · [validadores/resumen.py](../../../validadores/resumen.py) · versiones 13.0.0 a 15.1.0.
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —. El `cerrado en` anterior, `2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido`, quedó anulado.
- **Con qué se retoma:** la fase A de EP-005 · HU-008 se reabrió y ya corrige el programa; falta lo único que no se puede simular, que en una sesión nueva de verdad el archivo aparezca solo. Sigue viva, sin bloquear, la pregunta de con qué señal se sabe que un tema cerró: el enganche mira si la sección de cierre está llena, que no es lo mismo.

### H-5 · El estándar no cumple su propia regla de enlaces

- **Qué pasó:** el validador nuevo de `DOC14` encontró 354 enlaces del propio estándar cuyo texto no dice dónde vive el archivo.
- **Por qué importa:** son incumplimientos reales, no falsos positivos, y hasta hoy nadie los había contado.
- **Qué lo soluciona:** corregir los enlaces, uno por uno, con la lista que ya da el validador. Es trabajo, no historia nueva: `DOC14` y su comprobación ya existen.
- **Qué se decidió:** el validador se corre aparte, no en la corrida de todos los días, hasta limpiarlos.
- **Estado:** abierto.
- **Responde a:** EP-004 · HU-005, comprobar los enlaces y las citas.
- **Dispara:** —. Limpiar 354 enlaces es trabajo, no historia nueva.
- **Orden de resolución:** 7 de 7 · mecánico y sin urgencia.
- **Dónde queda:** [pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md](../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md).
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —
- **Con qué se retoma:** de los 354, ¿cuáles cuentan? Las transcripciones se copian literales y `prompts/` son palabras del usuario. Quedan unos 200 reales.

### H-6 · El capítulo de meta-reglas no se cumple a sí mismo

- **Qué pasó:** de 188 reglas, 129 no traen su bloque de checklist, 7 están publicadas en "no cumple" y 33 no aparecen clasificadas, incluidos los capítulos 18 y 19 completos.
- **Por qué importa:** `M14` dice que sin checklist en CUMPLE una regla no se publica, y hay siete publicadas igual.
- **Qué lo soluciona:**

  **EP-001 · HU nueva — poner al día las reglas que no pasan su propio checklist**
  - **Como** quien confía en el cuerpo de reglas
  - **Quiero** que ninguna regla esté publicada sin su checklist en CUMPLE
  - **Para** que obedecer una regla no dependa de si alguien la revisó alguna vez
  - **Contexto:** de 188 reglas, 129 no traen el bloque, 7 lo traen en "no cumple" y 33 no están clasificadas. El validador ya lo mide; lo que falta es decidir qué se hace con cada grupo: corregir, derogar o aceptar que el checklist no aplica a las viejas.
- **Qué se decidió:** sin decidir. El validador ya lo mide.
- **Estado:** abierto.
- **Responde a:** EP-004 · HU-011, comprobar que cada regla cumple su molde.
- **Dispara:** EP-001 · HU-009, poner al día las reglas que no pasan su propio checklist. Ya está escrita.
- **Orden de resolución:** 5 de 7 · es el más grande y no bloquea a nadie.
- **Dónde queda:** [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —
- **Con qué se retoma:** qué se hace con las siete en "no cumple": se corrigen, se derogan o se acepta que el checklist no aplica a las viejas.

### H-7 · `F2` está escrita para construir software, no para escribir reglas

- **Qué pasó:** dos fases seguidas se abrieron declarando que no tienen especificación aparte, porque su entregable es texto normativo o programas cortos.
- **Por qué importa:** una regla que se incumple dos veces seguidas con buenos motivos se vuelve costumbre incumplirla.
- **Qué lo soluciona:**

  **EP-001 · HU nueva — cuándo `F2` no aplica**
  - **Como** quien abre una fase cuyo entregable no es código
  - **Quiero** saber si necesita especificación aparte
  - **Para** no incumplir la regla ni escribir un documento que repite la historia de usuario
  - **Contexto:** dos fases seguidas se abrieron declarando que no la tienen, porque entregan texto normativo o programas cortos. `F2` da por hecho que se construye el código de un módulo. La regla necesita su excepción escrita, con condición, límite y quién autoriza, o aceptar que la historia hace de especificación cuando el módulo es el propio estándar.
- **Qué se decidió:** sin decidir. Queda la duda anotada en el plan de la fase.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** EP-001 · HU-010, cuándo no aplica la exigencia de especificación. Ya está escrita.
- **Orden de resolución:** 4 de 7 · hoy se incumple sin saber si está bien.
- **Dónde queda:** señal S-003 · [pendientes/20-f2-no-dice-cuando-no-aplica.md](../../../pendientes/20-f2-no-dice-cuando-no-aplica.md).
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —
- **Con qué se retoma:** ¿se le escribe a `F2` esa excepción, o se acepta que la historia de usuario hace de especificación cuando el módulo es el propio estándar?

### H-8 · La traducción quedó a medias

- **Qué pasó:** los nombres de los trece roles siguen en inglés (Explorer, Proposer, Designer, Implementer, Verifier, Spec Writer), y el glosario de la terminología del estándar no existe.
- **Por qué importa:** es el mismo incumplimiento de `C8` que se acaba de corregir en el texto.
- **Qué lo soluciona:**

  **EP-003 · HU nueva — el glosario de la terminología del estándar**
  - **Como** quien lee el estándar por primera vez
  - **Quiero** un sitio donde cada término esté definido en una línea
  - **Para** entender un documento sin ir preguntando qué significa cada palabra
  - **Contexto:** hoy la terminología está repartida en las reglas que usan cada palabra. Son unos treinta términos en cuatro grupos: la cadena de trabajo, las reglas, lo que comprueba y lo que se guarda. Con el glosario escrito se ve además cuáles siguen en inglés sin necesidad, y se cambian todos de una vez en lugar de uno por uno.
- **Qué se decidió:** no se tocaron, para no mezclarlo con el cambio de la 10.0.0.
- **Estado:** abierto.
- **Responde a:** EP-001 · HU-004, de donde salió `C20`.
- **Dispara:** EP-003 · HU-010, el glosario de la terminología. Ya está escrita.
- **Orden de resolución:** 2 de 7 · el glosario desbloquea traducir el resto de una sola vez.
- **Dónde queda:** [pendientes/21-el-glosario-y-los-terminos-en-ingles.md](../../../pendientes/21-el-glosario-y-los-terminos-en-ingles.md).
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —
- **Con qué se retoma:** primero el glosario: con los treinta términos escritos se ve cuáles más están en inglés sin necesidad y se cambian todos de una vez.

### H-9 · Dos sesiones versionando el mismo archivo a la vez

- **Qué pasó:** mientras esta sesión escribía la 10.0.0, otra subió la 9.0.0, la 9.1.0 y la 9.2.0. Al final del día la versión iba en 12.2.0 con dos numeraciones vivas.
- **Por qué importa:** la regla de que cada sesión sube lo suyo se rompe en los archivos que las dos tocan.
- **Qué lo soluciona:**

  **EP-002 · HU nueva — quién manda sobre la versión cuando hay dos sesiones abiertas**
  - **Como** quien trabaja con otra sesión abierta al mismo tiempo
  - **Quiero** una regla de quién sube la versión
  - **Para** que dos sesiones no dejen dos numeraciones vivas
  - **Contexto:** en un mismo día, una sesión escribió la 10.0.0 mientras otra subía la 9.0.0, la 9.1.0 y la 9.2.0. `VERSION` y el registro de cambios son un archivo único y ninguna sesión sabe qué hace la otra. Una opción es que la versión se suba al guardar el cambio y no al editarlo.
- **Qué se decidió:** sin decidir. Se subió lo de esta sesión y se avisó del cruce.
- **Estado:** abierto.
- **Responde a:** EP-002 · HU-001, el número de versión y qué significa cada parte.
- **Dispara:** EP-002 · HU-006, quién sube la versión cuando hay dos sesiones abiertas. Ya está escrita.
- **Orden de resolución:** 6 de 7 · estorba, pero no rompe nada.
- **Dónde queda:** señal S-005 · [pendientes/22-dos-sesiones-versionando-a-la-vez.md](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md).
- **Nace en:** 2026-08-14 · hu-de-la-comprobacion-automatica.
- **Cerrado en:** —
- **Con qué se retoma:** una opción es que la versión se suba al commitear y no al editar.

---

## ¿Se puede cerrar la sesión?

**Todavía no.**

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los dos: H-2 y H-3 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ los pendientes 17 a 22. H-1 no lo necesita: su continuación es la fase ya abierta |
| Toda historia disparada está escrita en su épica | ☑ las seis |
| Lo que se hizo está aprobado y guardado | ☐ los validadores siguen sin commitear |

Falta también decidir qué se hace con los dos pendientes que se escribieron sin aprobación (17 y 18), que son las tres fallas que hoy reporta `validar.py estandar`.

Y la fase `A-EP-004-HU-010` queda detenida esperando la aprobación de sus dos planes: eso no impide cerrar la sesión, porque está escrito y anotado.
