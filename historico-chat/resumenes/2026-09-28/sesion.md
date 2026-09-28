# 2026-09-28 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-09-28-sesion.md](../../2026-09-28-sesion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «...»

---

## Hallazgos de esta sesión

### H-1 · Las reglas no llegan completas al agente

- **Qué pasó:** el usuario preguntó por qué el agente recuerda las reglas un rato y después las olvida. Al arrancar la sesión, los enganches le entregaron al agente 79,7 KB. Claude Code guardó ese texto en un archivo aparte, fuera del repo, en su propio almacén de la sesión (`~/.claude/projects/<proyecto>/<id-de-sesión>/tool-results/hook-…-additionalContext.txt`), y en el contexto dejó solo los primeros 2 KB, que traen el comienzo del anexo `acciones-y-riesgo.md`. El resto de `00` y `01`, el índice de recuerdos y el del histórico no entraron. El agente tampoco abrió el archivo. Cuando la conversación se compacta, `SessionStart` vuelve a correr y vuelve a quedar cortado en 2 KB. Además, en una sesión larga el agente atiende más a lo reciente que a lo que se cargó al principio.
- **Por qué importa:** el agente trabaja sin las reglas que el estándar da por cargadas. [validadores/docs/hook_sesion.md](../../../validadores/docs/hook_sesion.md) supone que el texto llega entero, y [notas/compactacion-mata-decisiones.md](../../../notas/compactacion-mata-decisiones.md) marca la reinyección tras compactar como resuelta (✅), y no lo está.
- **Qué lo soluciona:**
  **EP-? · HU nueva — Lo que carga el arranque cabe en el contexto**
  - **Como** agente que abre una sesión
  - **Quiero** recibir las reglas dentro del tope que acepta la herramienta
  - **Para** trabajar con las reglas completas y no con una vista previa
  - **Contexto:** hoy se cargan 79,7 KB y entran 2 KB. Propuesta del usuario: medir qué reglas se usan más y cargar esas. Límite de esa idea: que una regla se use seguido no la hace importante (`N6` casi nunca se usa y es grave). Por eso se proponen tres niveles: el núcleo blindado siempre; después, las más usadas hasta llenar el tope; el resto, buscadas por tema cuando la tarea las pide (`hook_relacionadas` ya hace parte de eso). Guardarlas en una base de datos no arregla esto por sí solo: el tope es el del contexto, no el del almacén.
- **Qué se decidió:** el usuario descartó cargar reglas, sean todas o las más usadas: *«Lo importante es que tenga claro que existen reglas que debe cumplir y que, antes de realizar una tarea, debe identificar y consultar las que correspondan a lo que está haciendo»*. Al arrancar la sesión, el agente recibe esa instrucción y dónde buscar; las reglas se leen cuando la tarea las pide. Los tres niveles quedan descartados.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-? · HU nueva (falta decidir en qué épica va)
- **Orden de resolución:** 4 de 7, después de H-7: la instrucción corta que recibe el agente al arrancar enlaza el mapa, y el mapa tiene que existir primero
- **Dónde queda:** falta crear el pendiente
- **Nace en:** 2026-09-28 · por qué el agente olvida las reglas
- **Cerrado en:** —
- **Con qué se retoma:** ¿cuál es el tope exacto, cuántos de los 79,7 KB aporta cada enganche, y cómo se mide qué regla se usa? H-2 cambia la solución: el enganche no copia las reglas, entrega enlaces a `base/`.

### H-2 · Nada del agente ni del proyecto queda por fuera de ellos

- **Qué pasó:** a raíz de H-1, el usuario fijó un principio general: *«nada debe quedar por fuera del agente o del proyecto. Si se necesita alguna información, debe existir un enlace que lleve al lugar donde está el contenido […] Eso debe aplicar para todo»*.
- **Por qué importa:** [`01·C19`](../../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) cubre solo la memoria, y [`04·S9`](../../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) solo lo que escribe el agente. Ninguna cubre lo que guarda la herramienta por su cuenta, como la salida de los enganches. Además, un recuerdo vigente decía lo contrario: que leer lo guardado por fuera sí valía.
- **Qué lo soluciona:**
  **EP-? · HU nueva — Nada del proyecto queda en el almacén de la herramienta**
  - **Como** usuario del estándar
  - **Quiero** que todo lo del agente y del proyecto viva en el repositorio y se alcance por enlaces
  - **Para** que nada importante quede donde no se versiona ni se revisa
  - **Contexto:** hoy el enganche de arranque copia 79,7 KB de reglas y Claude Code lo guarda fuera del repositorio (H-1). Hay que decidir si esto sube a `base/` como regla general que absorba lo que exigen `C19` y `S9`, y qué validador la hace cumplir.
- **Qué se decidió:** quedó como recuerdo, [nada del agente ni del proyecto queda por fuera de ellos](../../memory/nada-del-proyecto-queda-en-la-herramienta.md), y se corrigió el recuerdo de los guiones que lo contradecía. Falta aprobar si sube a regla.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-? · HU nueva (falta decidir en qué épica va)
- **Orden de resolución:** 2 de 7, después de H-6 y antes de H-7: define que el mapa y las reglas viven en el repositorio y al agente le llega un enlace
- **Dónde queda:** memoria y [pendiente 99](../../../pendientes/99-nada-del-proyecto-queda-fuera-del-proyecto.md), hecho: la regla [`01·C29`](../../../base/01-conducta.md#c29--guarda-dentro-del-repositorio-todo-lo-del-agente-y-del-proyecto), versión 39.1.0, construida en la fase `B` de HU-011. Falta el commit
- **Nace en:** 2026-09-28 · por qué el agente olvida las reglas
- **Cerrado en:** —
- **Con qué se retoma:** ¿sube a `base/` como regla nueva o como cambio de `C19`?

### H-3 · El formato de las plantillas no estaba escrito en ninguna parte

- **Qué pasó:** el usuario preguntó si convenía hacer una plantilla de hallazgo o escribir el formato que siguen todas las plantillas. El molde del hallazgo ya estaba en [plantillas/sesion.md](../../../plantillas/sesion.md), y copiarlo aparte lo dejaba en dos sitios (H-2). El formato, en cambio, solo se sacaba mirando las 55 plantillas: la caja de reglas está copiada en cada una, y 38.3.1 tuvo que agregar `ID12` en las 55. La primera versión de la sección dejó por fuera lo que la sesión [2026-09-27 · reglas de redacción y orden de la cadena](../2026-09-27/reglas-de-redaccion-y-orden-de-la-cadena.md) había fijado con el plan de trabajo como modelo: la nota debajo de cada `###`, el párrafo «Para qué sirve este documento», la redacción con `ID8` e `ID9` y las excepciones. El usuario lo señaló y se corrigió. Justamente eso pasa cuando el formato no está escrito: ni el agente que lo aplicó el día anterior lo recuerda.
- **Por qué importa:** quien arma una plantilla nueva no tiene dónde ver el formato, y la caja de reglas copiada obliga a tocar 55 archivos cada vez que cambia.
- **Qué lo soluciona:**
  **EP-? · HU nueva — La caja de reglas de las plantillas es un enlace, no una copia**
  - **Como** mantenedor del estándar
  - **Quiero** que cada plantilla enlace la lista de reglas de redacción en vez de copiarla
  - **Para** cambiar la lista en un solo sitio
  - **Contexto:** hoy la tabla `ID8`·`ID9`·`ID11`·`ID12` está repetida en 55 plantillas. Además, [04-HU.md:3](../../../plantillas/ciclo-vida-proyectos/04-HU.md) dice «Elimine las secciones que no apliquen», y [`13·DOC21`](../../../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) pide escribirlas `N/A`. Y [ADR.md:12](../../../plantillas/ADR.md) todavía cierra su caja con «Reemplaza los `«…»` y borra esta caja», que tutea, en vez de la frase del modelo.
- **Qué se decidió:** el usuario aprobó escribir el formato en [plantillas/README.md](../../../plantillas/README.md), sección «Cómo está hecho un modelo», y no en un archivo aparte. El usuario agregó que cada nota de definición traiga un ejemplo y diga qué no va en la sección, y pidió que el README abra con la tabla de reglas de redacción y cumpla esas reglas. Queda en 38.4.0 (MENOR). Por ahora las tablas copiadas en las plantillas no se tocan, y ninguna plantilla trae todavía los ejemplos. Después el usuario fijó el rumbo: *«la idea no es saturar las plantillas sabiendo que hay un documento maestro que le dice cómo hacer las cosas»*. El README es ese documento maestro, `CLAUDE.md.plantilla` manda leerlo antes de crear, cambiar o llenar una plantilla, y la historia que queda es sacar de las plantillas lo que el README ya dice.
- **Estado:** abierto: el formato ya está escrito; falta la historia de reemplazar la caja por un enlace y corregir `04-HU.md` y `ADR.md`.
- **Responde a:** —
- **Dispara:** EP-? · HU nueva (falta decidir en qué épica va)
- **Orden de resolución:** 7 de 7: sacar de las plantillas lo que ya dice el README no afecta el olvido de las reglas, y puede esperar a que lo demás esté hecho
- **Dónde queda:** [plantillas/README.md](../../../plantillas/README.md) · falta crear el pendiente
- **Nace en:** 2026-09-28 · por qué el agente olvida las reglas
- **Cerrado en:** —
- **Con qué se retoma:** ¿la caja se reemplaza por un enlace a la sección del README, y eso es PARCHE o MAYOR para los proyectos?

### H-4 · Las reglas de la plantilla no se cumplen al llenar el documento durante la sesión

- **Qué pasó:** el usuario pidió que las reglas de las plantillas rijan cada vez que se escribe en un documento, no solo al crear la plantilla. Se midió este mismo resumen, llenado por el agente a lo largo de la sesión, y tiene 39 líneas con marcas de `ID8`. Unas son descuido del agente: punto medio en prosa, puntos suspensivos de un solo carácter, raya larga. Otras las impone la plantilla [plantillas/sesion.md](../../../plantillas/sesion.md): cada campo lleno queda como viñeta que abre con negrita y dos puntos, y el molde de la pieza de solución trae raya.
- **Por qué importa:** si las reglas solo se revisan al crear la plantilla, los documentos que salen de ella las incumplen en cada sesión, y nadie lo ve hasta que alguien los mide.
- **Qué lo soluciona:**
  **EP-? · HU nueva · Las reglas de redacción se revisan cada vez que se escribe un documento de plantilla**
  - **Como** usuario del estándar
  - **Quiero** que cada escritura en un documento hecho con plantilla se mida contra las reglas de redacción
  - **Para** que el documento las cumpla durante toda la sesión y no solo al nacer
  - **Contexto:** hoy `hook_md.py` revisa los enlaces al escribir, pero nada cuenta las marcas del documento escrito. Además, el formato de campos de `sesion.md` produce marcas por sí solo al llenarse.
- **Qué se decidió:** sin decidir.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-? · HU nueva (falta decidir en qué épica va)
- **Orden de resolución:** 5 de 7, después de H-7: el enganche lee el mapa para saber qué reglas de redacción mostrar
- **Dónde queda:** falta crear el pendiente
- **Nace en:** 2026-09-28, por qué el agente olvida las reglas
- **Cerrado en:** —
- **Con qué se retoma:** ¿el aviso al escribir basta, o el campo de formulario lleno se acepta como formato y se cambia el anexo de marcas? El usuario precisó: *«todo debe saber en tiempo real que se deben aplicar esas reglas»*. El recordatorio de cada turno (`hook_reglas.py`) ya nombra `ID8`, `ID9`, `ID11` e `ID12`, y aun así el agente llenó este resumen con marcas: recordar no alcanza, hace falta medir en el momento de escribir. Después amplió el alcance: *«todo el historico-chat lo debe cumplir porque desde ahí se está haciendo todo mal»*. Medido: `resumenes/` tiene 5550 marcas en 68 de 90 archivos, las transcripciones 4696 en 67 de 70 y `memory/` 112 en 25 de 26 (parte de las de los resúmenes son campos de formulario llenos). [hook_redaccion.py](../../../adaptadores/claude-code/hook_redaccion.py) mide cada respuesta del agente pero, según su propio comentario, nunca le devuelve nada al modelo: mide y el agente no se entera. Las transcripciones son literales y no se retocan; se corrigen en el origen, avisándole al agente cuando responde.

### H-5 · El agente actuó sin la palabra que exige `01·C28`

- **Qué pasó:** el usuario preguntó qué regla obliga a decirle al agente qué debe hacer. El agente citó solo [`01·C21`](../../../base/01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar), y el usuario señaló [base/01-conducta/palabras-clave.md](../../../base/01-conducta/palabras-clave.md), el anexo de [`01·C28`](../../../base/01-conducta.md#c28--sin-la-palabra-que-diga-qué-se-espera-el-agente-no-actúa). Revisada la sesión, el agente cambió archivos sin esa palabra: con un «si» escribió la sección del README y la línea de `CLAUDE.md.plantilla`; sin «Recuerde» escribió un recuerdo; con «revise» corrigió la tabla del README.
- **Por qué importa:** la regla existe para que el agente no lea una pregunta como una orden, y el agente la incumplió sin tenerla presente. Es el mismo caso de H-1 y H-4: la regla no estaba a la vista cuando hacía falta.
- **Qué lo soluciona:** lo mismo que H-1 y H-4. La regla tiene que llegarle al agente en el momento de actuar, no solo al arrancar la sesión.
- **Qué se decidió:** sin decidir.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** —, cae en la historia de H-4
- **Orden de resolución:** 6 de 7, junto con H-4: es el mismo enganche, que además muestra `C28` al recibir un pedido
- **Dónde queda:** falta crear el pendiente
- **Nace en:** 2026-09-28, por qué el agente olvida las reglas
- **Cerrado en:** —
- **Con qué se retoma:** ¿cómo le llega `C28` al agente en el momento de actuar? Los cambios hechos sin la palabra se dejan, por decisión del usuario.

### H-6 · Ninguna regla pone las reglas por encima de lo que el usuario pida en el momento

- **Qué pasó:** el usuario dijo: *«las reglas deben tener prioridad sobre lo que yo diga, porque precisamente se crean para establecer las condiciones que el agente debe cumplir»*. Hoy eso está solo en el recuerdo [las reglas son la decisión del usuario](../../memory/reglas-son-decision-del-usuario.md). En `base/` la única precedencia escrita es núcleo, luego convenciones, luego proyecto.
- **Por qué importa:** si una instrucción del momento puede pasar por encima de una regla, la regla no obliga a nada.
- **Qué lo soluciona:**
  **EP-? · HU nueva · Las reglas mandan sobre la instrucción del momento**
  - **Como** usuario del estándar
  - **Quiero** que el agente cumpla la regla aunque yo le pida lo contrario, y me diga cuál es
  - **Para** que las reglas se cumplan siempre, y cambiarlas sea una decisión escrita y no un descuido
  - **Contexto:** la memoria lo dice y `base/` no. Según [memory.md](../../memory/memory.md), la preferencia que vale para todos sube a `base/` como regla y el recuerdo se queda.
- **Qué se decidió:** el usuario aprobó el pendiente 98 y decidió que la regla va en el núcleo `00`, como blindada. Pidió escribir una HU y su fase, pero el núcleo tiene historia dueña ([HU-012](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md)) y todo cambio del capítulo baja por ella; el agente no creó la HU nueva y se lo dijo.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** EP-001 · HU-012 · CA-05, fase `B` (no una HU nueva: HU-012 es la historia dueña del núcleo)
- **Orden de resolución:** —
- **Dónde queda:** [pendiente 98](../../../pendientes/98-las-reglas-mandan-sobre-la-instruccion-del-momento.md), hecho: la regla blindada [`00·N10`](../../../base/00-nucleo-blindado.md#n10--una-regla-escrita-manda-sobre-la-instrucción-del-momento-blindada), versión 39.0.0, construida en la fase `B` de HU-012 y subida en el commit `5421ece`
- **Nace en:** 2026-09-28, por qué el agente olvida las reglas
- **Cerrado en:** 2026-09-28, por qué el agente olvida las reglas
- **Con qué se retoma:** —

### H-7 · No hay un mapa que diga qué reglas aplican a cada tarea

- **Qué pasó:** el usuario decidió que el agente no cargue las reglas, sino que antes de cada tarea identifique y lea las que le corresponden (H-1). Para eso, el agente y el enganche de H-4 y H-5 necesitan saber qué reglas aplican a cada tarea: escribir un documento, recibir un pedido, hacer un commit. Ese mapa no existe. Los índices de `base/` están ordenados por capítulo, no por tarea.
- **Por qué importa:** sin el mapa, H-1 dice que hay que buscar y no dice dónde, y el enganche no sabe qué regla mostrar. Es la pieza que une H-1, H-4 y H-5.
- **Qué lo soluciona:**
  **EP-? · HU nueva · Cada tarea sabe qué reglas le aplican**
  - **Como** agente que va a hacer una tarea
  - **Quiero** un mapa que lleve de la tarea a las reglas que le aplican, con su enlace
  - **Para** leer solo esas, sin cargar todas
  - **Contexto:** hoy hay que saber en qué capítulo está cada regla. El enganche de H-4 y H-5 leería este mapa para decidir qué mostrar.
- **Qué se decidió:** sin decidir.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** EP-? · HU nueva (falta decidir en qué épica va)
- **Orden de resolución:** 3 de 7, después de H-2 y antes de H-1, H-4 y H-5: la instrucción de arranque y el enganche lo usan
- **Dónde queda:** falta crear el pendiente
- **Nace en:** 2026-09-28, por qué el agente olvida las reglas
- **Cerrado en:** —
- **Con qué se retoma:** ¿el mapa es un archivo en `base/` o sale solo de las reglas, cada una declarando a qué tareas aplica? El agente recomendó lo segundo, con la tabla generada en `base/mapa-de-tareas.md`. Hay un antecedente: [validadores/reglas-antes-de-la-accion.md](../../../validadores/reglas-antes-de-la-accion.md), del 2026-09-16, clasifica las 248 reglas por cuándo se pueden comprobar antes de la acción.

---

## Orden de resolución de los hallazgos abiertos

| Puesto | Hallazgo | Por qué va ahí |
|---|---|---|
| — | ~~H-6, las reglas mandan sobre lo que pida el usuario~~ | Cerrado el 2026-09-28 con `00·N10` |
| 2 | H-2, nada queda fuera del repositorio | Define que las reglas y el mapa viven en el repositorio y al agente le llega un enlace |
| 3 | H-7, el mapa de qué reglas aplican a cada tarea | La instrucción de arranque y el enganche lo usan |
| 4 | H-1, la instrucción corta al arrancar | Enlaza el mapa, que tiene que existir primero |
| 5 | H-4, el enganche que revisa la redacción al escribir | Lee el mapa para saber qué reglas mostrar |
| 6 | H-5, el enganche muestra `C28` al recibir un pedido | Es el mismo enganche de H-4 |
| 7 | H-3, sacar de las plantillas lo que ya dice el README | No afecta el olvido de las reglas y puede esperar |

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda a medias. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- Resuelto acá, con lo que se hizo escrito en el campo de dónde queda.
- Anotado, con su pendiente creado y su historia de usuario disparada escrita. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☐ |
| Todo hallazgo abierto tiene su pendiente creado | ☐ |
| Toda historia disparada está escrita en su épica | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
