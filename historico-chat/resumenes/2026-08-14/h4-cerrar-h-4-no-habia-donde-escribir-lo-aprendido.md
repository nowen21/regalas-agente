# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](../../2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md), con la plantilla [`plantillas/sesion.md`](../../../plantillas/sesion.md). La conversación está allá; acá queda lo que la sesión dejó.

Se anotan todos, resueltos y abiertos.

**Viene de:** 2026-08-14 · hu-de-la-comprobacion-automatica · [H-4 · No había dónde escribir lo aprendido](hu-de-la-comprobacion-automatica.md#h-4--no-había-dónde-escribir-lo-aprendido).

---

## Hallazgos

### H-1 · Se le preguntó al usuario algo que estaba escrito en el repositorio

- **Qué pasó:** el agente ofreció tres órdenes de trabajo posibles y pidió elegir, cuando [HU-008:163](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) ya declara que depende de HU-009.
- **Por qué importa:** la pregunta tenía premisa falsa, así que cualquier respuesta habría contradicho una dependencia escrita. Y le pasa el trabajo de leer a quien ya lo dejó escrito.
- **Qué lo soluciona:**

  **EP-001 · HU nueva — buscar en el repositorio antes de preguntar**
  - **Como** quien ya dejó una decisión escrita
  - **Quiero** que el agente la busque antes de preguntármela
  - **Para** no volver a decidir lo que ya está decidido
  - **Contexto:** hoy existe la regla de que el pedido incompleto se pregunta en vez de adivinarse, y funcionó: el agente preguntó. Lo que falta es el paso previo: antes de preguntar, mirar si la respuesta ya está en el documento. Falta decir dónde se busca (la HU, su sección de dependencias, la épica, el histórico) y qué se hace cuando lo escrito y el pedido se contradicen.
- **Qué se decidió:** sin decidir. Se corrigió la pregunta en el momento, no la conducta.
- **Estado:** abierto.
- **Responde a:** EP-001 · HU-004, las reglas de conducta de la IA.
- **Dispara:** EP-001 · HU nueva, buscar en el repositorio antes de preguntar. Sin escribir.
- **Orden de resolución:** 2 de 2 · no bloquea la cadena de H-4.
- **Dónde queda:** —. Falta el pendiente.
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** —
- **Con qué se retoma:** ¿es regla nueva de `base/01`, o le cabe a la regla que ya existe sobre el pedido incompleto?

### H-2 · Una tarea técnica de la HU era en realidad plan de pruebas

- **Qué pasó:** [HU-009:134](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-009-modelo-del-resumen-de-sesion/HU-009-modelo-del-resumen-de-sesion.md) lleva como tarea *"probar el modelo con más de una sesión"*, que es lo mismo que ya dicen sus CA-01 a CA-03 en su "cómo validarlo".
- **Por qué importa:** el trabajo queda contado dos veces, y con eso una HU parece más grande de lo que es. Fue lo que hizo creer que HU-009 tenía trabajo propio.
- **Qué lo soluciona:** quitar esa tarea de HU-009. Es corrección, no historia nueva.
- **Qué se decidió:** se quitó la tarea y se ajustó el contexto y el DoD que la repetían. HU-009 conserva trabajo propio: decidir desde dónde se enlaza el resumen y qué se hace con un hallazgo arrastrado de otra sesión. Así que H-4 sigue con sus dos historias.
- **Estado:** resuelto acá.
- **Responde a:** EP-003 · HU-009.
- **Dispara:** —. Es corregir un documento.
- **Orden de resolución:** —, ya está cerrado.
- **Dónde queda:** [HU-009, secciones 3, 7, 11 y 13](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-009-modelo-del-resumen-de-sesion/HU-009-modelo-del-resumen-de-sesion.md).
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Con qué se retoma:** —

### H-3 · El resumen no decía de dónde viene la sesión

- **Qué pasó:** esta sesión se abrió con un hallazgo en la mano ("trabajemos en H-4") y la plantilla no tenía dónde escribir ese origen.
- **Por qué importa:** el hallazgo guardaba dónde nace y dónde se cierra, pero la sesión no guardaba de dónde nace. Ese dato se quedaba en la transcripción, que es justo lo que el resumen viene a evitar.
- **Qué lo soluciona:** el campo `Viene de` al principio del resumen. Cabe entero en EP-003 · HU-009, que es la historia del modelo.
- **Qué se decidió:** se agregó el campo, con la fecha, el tema y el número del hallazgo, o `—` si es trabajo nuevo. Es el enlace hacia adelante; el de vuelta ya lo daba el `cerrado en`.
- **Estado:** resuelto acá.
- **Responde a:** EP-003 · HU-009, el modelo del resumen de sesión.
- **Dispara:** —
- **Orden de resolución:** —, ya está cerrado.
- **Dónde queda:** [`plantillas/sesion.md`](../../../plantillas/sesion.md) · versión 12.3.0.
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Con qué se retoma:** —

### H-4 · El orden de dos historias hermanas no se veía desde ninguna épica

- **Qué pasó:** H-4 de la sesión anterior dispara EP-003 · HU-009 y EP-005 · HU-008, y en ninguna de las dos épicas se ve cuál va primero.
- **Por qué importa:** las épicas están cortadas por tipo de entregable (el documento modelo en una, el programa que lo llena en otra), así que un problema partido en dos queda sin dueño del orden. Hubo que deducir a mano que el enganche va después.
- **Qué lo soluciona:** que el campo `Dispara` numere las historias. El hallazgo es el único sitio donde el problema está entero.
- **Qué se decidió:** se descartó recortar las épicas por problema: costaría rehacer las 54 historias ya colgadas. `Dispara` numera, dice por qué cada una va ahí y nombra también lo que las bloquea sin haberlo disparado.
- **Estado:** resuelto acá.
- **Responde a:** EP-003 · HU-009, el modelo del resumen de sesión.
- **Dispara:** —
- **Orden de resolución:** —, ya está cerrado.
- **Dónde queda:** [`plantillas/sesion.md`](../../../plantillas/sesion.md) · versión 12.4.0.
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Con qué se retoma:** —

### H-5 · La marca del espacio por llenar se usa sin estar escrita

- **Qué pasó:** al verificar si HU-001 ya estaba resuelta de hecho, resultó que `«…»` se usa en 25 de las 30 plantillas, pero ninguna regla la exige. Las otras cinco usan `[texto]`, `<texto>` o nada.
- **Por qué importa:** una convención que nadie escribió se cumple mientras alguien se acuerde. Y sin decir qué **no** es un hueco (la sintaxis de un comando lo parece), el programa que la cuente va a reportar de más.
- **Qué lo soluciona:** la fase A de HU-001, abierta y ejecutada en esta sesión.
- **Qué se decidió:** la marca es `«…»`, porque cambiarla costaría 25 archivos en vez de 5. Nacieron tres reglas, no una: `13·DOC19` la marca, `DOC20` que un documento con marcas no está terminado y `DOC21` que lo que no aplica se escribe `N/A`. Se convirtieron 179 huecos en 13 plantillas. Versión 13.0.0, MAYOR.
- **Estado:** abierto. Los tres criterios están en verde y el trabajo hecho, pero falta el commit, que se autoriza aparte.
- **Responde a:** EP-003 · HU-001, la marca de espacio por llenar.
- **Dispara:** —. La historia ya existía; lo que faltaba era bajarla a fase.
- **Orden de resolución:** 1 de 2 · es la primera de la cadena de H-4, y HU-009 la declara dependencia de impacto alto.
- **Dónde queda:** [la fase A-EP-003-HU-001](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md). No lleva pendiente: su continuación ya está abierta.
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** —
- **Con qué se retoma:** autorizar el commit de la fase, y seguir la cadena por EP-003 · HU-009.

### H-6 · El agente escribía el estándar sin haber cargado el estándar

- **Qué pasó:** todo lo escrito hoy incumple `00·ID8`, la regla que prohíbe las marcas de generación automática. La raya larga como inciso está en la especificación, en los dos planes, en el resumen y en casi todas las respuestas del chat.
- **Por qué importa:** la causa no fue el descuido. El `CLAUDE.md` que se instala en un proyecto heredero exige cargar todos los archivos de `base/` al abrir la sesión, y el `CLAUDE.md` de este repositorio no lo pedía. Es decir: un proyecto que hereda cumplía más que el repositorio del que hereda.
- **Qué lo soluciona:** el paso 0 del `CLAUDE.md`, agregado en esta sesión, que copia esa exigencia.
- **Qué se decidió:** se agrega el paso 0 y se deja escrito que `ID8` habla de "todo documento que el agente entrega", lo que incluye las respuestas del chat. Falta corregir lo ya escrito hoy.
- **Estado:** abierto.
- **Responde a:** EP-001 · HU-004, las reglas de conducta de la IA.
- **Dispara:** —. La regla ya existe; lo que faltaba era cargarla.
- **Orden de resolución:** 1 de 3 · mientras no se corrija, cada archivo nuevo repite el incumplimiento.
- **Dónde queda:** [CLAUDE.md](../../../CLAUDE.md), paso 0.
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** —
- **Con qué se retoma:** limpiar de raya larga los archivos escritos en esta sesión, y decidir si el enganche de arranque debe cargar `base/` en lugar de dejarlo al `CLAUDE.md`.

### H-7 · La carpeta de plantillas mezcla modelos con procedimientos

- **Qué pasó:** al aplicar la marca, cuatro de los treinta archivos de `plantillas/` quedaron sin ninguna, y hubo que declararlos como excepción para que la prueba de cobertura se pudiera juzgar.
- **Por qué importa:** la lista de excepciones es el síntoma. Mientras esos cuatro estén ahí, cada comprobación tiene que consultar una lista escrita a mano, y un archivo nuevo sin marca se cuela como "seguro es otro de esos".
- **Qué lo soluciona:** sacarlos de `plantillas/`. Con eso, un archivo sin marca pasa a ser siempre un defecto.
- **Qué se decidió:** sin decidir entre las dos opciones: una subcarpeta `plantillas/procedimientos/`, o sacarlos a `base/` como anexos. La segunda cambia qué copia el instalador.
- **Estado:** abierto.
- **Responde a:** EP-003 · HU-001, la marca de espacio por llenar.
- **Dispara:** —. Es mover archivos, y necesita su fase por la migración.
- **Orden de resolución:** 3 de 3 · no bloquea la cadena de H-4.
- **Dónde queda:** [pendientes/23-plantillas-mezcla-modelos-con-procedimientos.md](../../../pendientes/23-plantillas-mezcla-modelos-con-procedimientos.md).
- **Nace en:** 2026-08-14 · h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.
- **Cerrado en:** —
- **Con qué se retoma:** ¿subcarpeta dentro de `plantillas/`, o anexos en `base/`? Lo segundo cambia qué recibe un proyecto al instalar.

---

## ¿Se puede cerrar la sesión?

**Todavía no.**

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2, H-3 y H-4 |
| Todo hallazgo abierto tiene su pendiente creado | ☐ falta el de H-1. H-5 no lo necesita: su continuación es la fase ya abierta |
| Toda historia disparada está escrita en su épica | ☐ falta la de H-1 |
| Lo que se hizo está aprobado y guardado | ☐ la fase de HU-001 quedó en el commit `b877f37`; la de HU-009 está sin commitear |

**De la cadena de H-4 van dos de tres.** Cerraron [`A-EP-003-HU-001`](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md) y [`A-EP-003-HU-009`](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-009-modelo-del-resumen-de-sesion/A-EP-003-HU-009-modelo-del-resumen-de-sesion/README.md). Falta EP-005 · HU-008, el enganche, que es lo que hace que el resumen exista sin que nadie se acuerde.
