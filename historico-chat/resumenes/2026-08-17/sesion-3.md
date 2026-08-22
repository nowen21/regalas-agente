# 2026-08-17 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-17-sesion-3.md](../../2026-08-17-sesion-3.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «[plan de pruebas y estado de las 51 fases](plan-de-pruebas-y-estado-de-las-51-fases.md)» — allá quedaron las 51 fases con sus cuatro documentos escritos y ninguna aprobada. Acá el usuario las aprueba todas y manda ejecutarlas.

---

## Hallazgos de esta sesión

### H-1 · De las 51 fases aprobadas, 26 tienen una duda de §2.7 que solo el usuario puede resolver

**Qué se midió.** Se leyó la §2.7 de los 51 `plan_trabajo.md`. **25 fases no tienen ninguna duda** y se pueden ejecutar enteras. Las otras **26 suman 40 dudas**, todas dirigidas al usuario, y todas bloquean al menos una tarea.

**Por qué importa.** «Ejecútelos todos» no puede significar que el agente decida esas 40: son elecciones de diseño del estándar —si una regla entra a `base/` o se difiere, sobre qué proyecto se prueba, si un enganche detiene el commit o solo avisa—. Decidirlas el agente es exactamente lo que el recuerdo [decidir es del usuario](../../memory/decidir-es-del-usuario.md) prohíbe.

**Dónde queda.** Las 40 preguntas se le presentan al usuario en el chat, agrupadas. Mientras tanto se ejecuta todo lo que no depende de ellas.

### H-2 · Una fase puede hacer todo lo que su plan aprobado pedía y aun así no cumplir

**Qué pasó.** La primera fase ejecutada —[`A-EP-006-HU-001`](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-001-que-se-guarda-tipos-y-alcances/A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md)— corrió sus tres casos, cumplió sus dos CA numerados… y quedó en **No cumple**. La HU tiene además dos criterios **transversales**, y el plan de pruebas no les escribió caso mientras declaraba «cobertura 100%».

**Quién lo detectó.** No el agente: `validar.py fases`, con la comprobación que dejó [`A-EP-004-HU-014`](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/A-EP-004-HU-014-comparar-los-dos-veredictos/funcionalidad_implementada.md). El agente había escrito «Cumple con defectos abiertos», que la [plantilla del resultado](../../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) §6 no admite: «no hay estado intermedio».

**Por qué importa.** Los 51 planes se escribieron con el mismo molde y varios cuentan la cobertura igual. **Es un defecto de método, no de una fase**, y va a reaparecer.

**Dónde queda.** En el veredicto de esa fase, y la fase `B-EP-006-HU-001` queda propuesta —sin abrir— para los dos transversales.

### H-3 · Los 51 planes de pruebas omiten los criterios transversales — los 51

**Qué se midió.** Al descubrir el hallazgo 2 en una fase, se midió en todas antes de ejecutar las otras 50. El resultado no admite lectura amable:

| Medición, 2026-08-17 | Número |
|---|---|
| Fases aprobadas sin ejecutar | 50 |
| Cuya HU declara criterios de aceptación **transversales** | **50** |
| Cuyo `plan_pruebas.md` les escribe **algún** caso | **0** |

Y los transversales **no son plantilla sin llenar**: cada HU eligió los suyos y los reescribió con sus palabras. «El hallazgo no reproduce el secreto encontrado» ([EP-004 · HU-007](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-007-claves-y-datos-sensibles/HU-007-claves-y-datos-sensibles.md)). «Si no se puede decidir si pisar, no se pisa y se dice» ([EP-007 · HU-005](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md)). Son exigencias reales, y cada plan declara «cobertura 100%» sin contarlas.

**Cómo se ejecuta el resto, entonces.** No se reescribe ningún `plan_pruebas.md`: está aprobado y [`02·F4`](../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) dice que no se toca al ejecutar. Lo que se hace en cada fase es **comprobar también los transversales y decirlo en el resultado**, marcados como lo que son: exigencias de la HU que el plan no cubrió. Así una fase cierra en «Cumple» cuando de verdad cumple, y en «No cumple» solo cuando algo falla — no las 51 por el mismo defecto de molde. No toca ningún archivo que el plan no declare, así que [`02·F8`](../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) queda a salvo.

**Lo que hay que decidir, y no lo decide el agente:** si el molde de `plantillas/ciclo-vida-proyectos/08-plan-pruebas.md` pasa a exigir una fila por transversal. Es cambio de plantilla, y va al usuario.

### H-4 · La búsqueda de la memoria encuentra, pero no dice dónde está lo que encontró

**Qué pasó.** Al ejecutar [`A-EP-006-HU-003`](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-003-busqueda-por-palabra/A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/resultado_pruebas.md) salieron **dos defectos** que llevaban ahí desde que existe la búsqueda:

| Defecto | Qué es | Tamaño del arreglo |
|---|---|---|
| `D-01` | `cmd_search` **no imprime `where_`**. El dato se guarda —`memoria.py add --where`— y la búsqueda ni lo selecciona. El CA-01 pide que el resultado alcance «para abrir lo que se encontró», y no alcanza | Una línea |
| `D-02` | El camino «(sin señales relevantes)» de `cmd_search` retorna **sin cerrar la conexión**. En Windows deja el archivo tomado | Una línea |

**Por qué no se arreglaron.** §2.1 del plan aprobado dice «`memoria.py` y el esquema no se tocan», y [`02·F8`](../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) no deja salirse del plan. **Quedaron probados, no anotados:** cada uno tiene su prueba marcada `expectedFailure`, así la suite sigue verde, el defecto queda con evidencia, y el día que alguien lo arregle la prueba pasa a «éxito inesperado» y obliga a volver al documento.

**Lo que esta fase enseña de método.** Las **seis metas** de su plan de pruebas quedaron en verde —cobertura, acentos, señales perdidas, herramientas instaladas— y la fase **no cumple**. Ninguna de las seis medía lo único que fallaba. Un tablero verde no es un veredicto.

**Dónde queda.** Fase `B-EP-006-HU-003` propuesta, sin abrir.

### H-5 · EP-006 entera ejecutada: **las 7 fases cierran en «No cumple»**, y ninguna por no haberse hecho

**Qué pasó.** Las 7 fases de la épica de la memoria corrieron completas —39 pruebas nuevas en `memoria/pruebas.py` y 12 en `validadores/pruebas.py`— y **las 7 dieron «No cumple»**. En todas, el trabajo del plan se hizo entero y lo que falla es una exigencia que la corrida destapó.

| Fase | Qué falla |
|---|---|
| [HU-001](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-001-que-se-guarda-tipos-y-alcances/A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md) | `13·DOC5` no dice que no se guarden datos personales ni claves |
| [HU-002](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-002-guardar-en-el-repositorio/A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio/resultado_pruebas.md) | **Las 237 señales no están versionadas**: `senales.db` está en `.gitignore`, **cero commits** |
| [HU-003](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-003-busqueda-por-palabra/A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/resultado_pruebas.md) | La búsqueda no dice **dónde** está lo que encontró |
| [HU-004](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-004-busqueda-por-significado/A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado/resultado_pruebas.md) | **Sin el modelo, la búsqueda se cae entera** y arrastra a la léxica, que no necesita nada |
| [HU-005](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-005-separar-aprendizaje-de-preferencia/A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia/resultado_pruebas.md) | La terminología está guardada **en los dos sitios** y las dos versiones ya divergen |
| [HU-006](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-006-sacar-del-almacen-local/A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md) | El recogido se lleva **todo**, también lo que no es un recuerdo |
| [HU-007](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-007-marcar-lo-que-dejo-de-aplicar/A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar/resultado_pruebas.md) | Marcar una señal **no deja fecha ni dice qué la reemplazó** |

**El más grave es el de HU-004.** `disponible()` comprueba que `numpy` y `model2vec` **importen**, no que el modelo cargue. En una máquina nueva, con la caché borrada o sin red la primera vez, la memoria entera deja de responder — también la parte que no necesita ni modelo ni red. No se ve nunca donde se desarrolla, porque ahí el modelo ya está descargado.

**Nada se parcheó.** Los siete defectos tocan archivos que los planes aprobados excluyen ([`02·F8`](../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Quedaron **probados con `expectedFailure`**: la suite sigue verde, el defecto tiene evidencia, y el día que se arregle la prueba pasa a «éxito inesperado» y obliga a volver al documento. Cinco fases dejan propuesta su fase `B`; dos dejan una decisión al usuario.

**Lo que esto enseña de método, y se repitió cuatro veces:** las metas de los planes de pruebas quedaron **todas en verde** y las fases no cumplen. Medían cobertura, acentos, señales perdidas, herramientas instaladas — y ninguna medía lo que fallaba. **Un tablero verde no es un veredicto.**

### H-6 · Lo único que se escribió de nuevo en toda la épica: el criterio de cuál va dónde

**Qué pasó.** De las 7 fases, solo una tenía que **escribir** algo: el criterio que separa la preferencia del usuario del aprendizaje del proyecto. No existía — se venía aplicando por costumbre.

**Cómo quedó.** En [`historico-chat/memory/memory.md`](../../memory/memory.md), con la pregunta que decide —**qué haría que eso cambiara**—, el caso de borde de la preferencia que resulta valer para todos, y la regla de que **nada se guarda en dos sitios**.

**Y al aplicarlo apareció el duplicado.** El índice advertía desde siempre que dos copias terminan diciendo cosas distintas; lo decía del almacén de la herramienta, y estaba pasando **entre los dos sitios del repositorio**, donde nadie miraba.

### H-7 · Tres defectos previos que tenían la suite en rojo, corregidos

**Qué se encontró** al correr la suite completa antes de ejecutar:

1. **`hook_resumen.py` era el único de los seis enganches que no preparaba su salida.** Su texto lleva acentos, así que salía en la página de códigos de la consola y con la salida en tubería no se podía ni decodificar. Es el [pendiente 45](../../../pendientes/hecho/instalar-prepara-su-propia-salida.md) otra vez, en otro archivo. **Corregido**, con la prueba que recorre los seis para que no vuelva a pasar. Va en la **23.2.1**.
2. **Cinco «citas sueltas» en `base/`, y las cinco son falsos positivos**: `citas.py` cuenta como cita un identificador usado **como ejemplo** en prosa —«como `C20` o `F12`», «ponerle `G9` a una regla de pruebas»—, y `G9` ni existe. **No se editó `base/`**, que está bien escrito: se midió y se agregó al [pendiente 55](../../../pendientes/hecho/los-enlaces-de-ejemplo-no-son-enlaces.md), que ya cubre esta familia.
3. **`validar.py estandar` tenía 5 fallas**, todas previas: un enlace a una sesión renombrada, un pendiente cerrado en otro proyecto que se movió a `hecho/`, y tres pendientes sin línea en el índice — uno de ellos, el 44, **se declaraba abierto mientras el índice lo daba por cerrado**. **Las cinco corregidas**; `estandar` quedó en cero.

### H-8 · Las 25 fases libres, ejecutadas: **9 cumplen y 16 no**, y ninguna por trabajo sin hacer

**Qué se hizo.** Las 25 fases sin duda en §2.7 corrieron completas, con sus cinco documentos. El inventario [48](../../../pendientes/48-inventario-hu.md) pasó de **14 completas a 39** de 68.

| Épica | Fases | Cumplen | No cumplen |
|---|---:|---:|---:|
| EP-006 · memoria | 7 | 0 | 7 |
| EP-004 · comprobación | 6 | 4 | 2 |
| EP-007 · instalación | 4 | 3 | 1 |
| EP-005 · automatismos | 3 | 1 | 2 |
| EP-003 · documentos modelo | 3 | 2 | 1 |
| EP-001 · reglas · EP-002 · versionado | 2 | 1 | 1 |

**Las 16 que no cumplen fallan por algo que la corrida destapó**, no por trabajo pendiente. Lo más grave, en orden:

| Qué | Dónde |
|---|---|
| **Con las librerías puestas y el modelo ausente, la memoria entera deja de responder** — también la búsqueda por palabra, que no necesita nada | [EP-006 · HU-004](../../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-004-busqueda-por-significado/A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado/resultado_pruebas.md) |
| **Un `.md` que no se puede decodificar tumba la corrida entera**, y se lleva todos los hallazgos ya encontrados | [EP-004 · HU-003](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-003-formato-del-hallazgo/A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md) |
| **Cuatro reglas del capítulo 16 no existen para el validador**: están escritas con `###` y el analizador solo ve `## `. Nunca pasaron por ninguna de las 20 filas del checklist | [EP-004 · HU-002](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-002-marca-de-comprobable-en-cada-regla/A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla/resultado_pruebas.md) |
| **`15.4.0` aparece dos veces en el registro**, con contenidos distintos: un proyecto que la declare no puede saber cuál adoptó | [EP-002 · HU-001](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-001-numero-de-version-y-que-significa/A-EP-002-HU-001-retrodocumentar-el-numero-de-version/resultado_pruebas.md) |
| **La simulación del instalador dice que no hay registro de versión que escribir, y al aplicar lo escribe** | [EP-007 · HU-002](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-002-mostrar-antes-de-hacer/A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md) |
| **El disparo al escribir nunca detiene**: todo avisa, y hay constancia de un aviso ignorado una sesión entera | [EP-005 · HU-003](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md) |
| **Este repositorio no tiene planteamiento**: las 7 épicas cuelgan de nada | [EP-003 · HU-002](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo/resultado_pruebas.md) |

**Nada se parcheó fuera del plan aprobado.** Los defectos que tocan archivos que los planes no declaran quedaron **probados con `expectedFailure`** —siete en total—: la suite sigue verde, el defecto tiene evidencia, y el día que se arregle la prueba pasa a «éxito inesperado» y obliga a volver al documento.

**Lo construido de nuevo, versionado:** `validadores/pendientes.py` con su subcomando, y la línea del inventario de HU en `validar.py fases` (**23.3.0**), más el arreglo del enganche del resumen (**23.2.1**).

### H-9 · Las 26 fases con duda quedan aprobadas y **detenidas**, con sus 42 preguntas en un solo sitio

**Qué se hizo.** Las 26 pasaron de la estación 4 —esperando aprobación— a la **6, detenidas**: el plan **está aprobado** desde hoy, y lo que falta ya no es la aprobación sino **la respuesta**. Su `estado-fase.md` lo dice, para que la sesión que siga no vuelva a buscar.

**Las 42 dudas quedaron agrupadas por decisión** en el pendiente [59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md), no fase por fase: varias son la misma pregunta repetida, y así se contestan de corrido. Nombrar un proyecto desbloquea cuatro fases; decidir «¿detiene o avisa?» desbloquea otras cuatro.

**Va como `P0` por una sola de las 42:** hoy **una clave pegada en el chat queda escrita en claro en la transcripción, que se versiona**. Se comprobó. Nada enmascara, y lo que falta para construirlo son dos decisiones.

### H-10 · El repositorio que define el criterio de qué se guarda tiene una sola señal en 237

**Qué se midió.** `memoria/senales.db`, el 2026-08-17: **237 señales**, y de alcance `proyecto:estandar-agente` hay **una**, la `S-003`, del 2026-07-25 — anterior a que se abriera ninguna épica. De cinco decisiones reales de fases cerradas de este repositorio, cuatro son señal según [`13·DOC5`](../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) y ninguna se guardó.

**De paso:** de los diez tipos del esquema, **tres no se han usado nunca** (`alternativa-descartada`, `supuesto`, `pregunta-abierta`), y de las tres formas de alcance, `modulo:` tampoco.

**Por qué importa.** El criterio está escrito, decide bien y no se aplica donde se escribió. No se corrige guardando las cuatro a posteriori: `RN-04` de la HU dice que lo que se guarda se decide al guardarlo.

**Dónde queda.** Defecto `D-01` del resultado de la fase, y reportado al usuario.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ — los tres defectos previos corregidos, con su versión (23.2.1) y su prueba; las 5 fallas de `validar.py estandar` en cero |
| Todo hallazgo abierto tiene su pendiente creado | ☑ — las 42 dudas en el [59](../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md); los falsos positivos de `citas.py` sumados al [55](../../../pendientes/hecho/los-enlaces-de-ejemplo-no-son-enlaces.md); el planteamiento vacío ya estaba en el [56](../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md); los siete defectos que tocan archivos fuera de plan, probados con `expectedFailure` y con su fase `B` propuesta en la HU |
| Toda historia disparada está escrita en su épica | ☑ — no nació ninguna HU. Lo que salió son **siete fases `B` propuestas**, escritas en el §8 de su HU, y decisiones que van al usuario |
| Lo que se hizo está aprobado y guardado | ☑ — commit `925d5b0` en `main`, 152 archivos. Sin `push`, que no se autorizó. Se dejaron fuera los dos archivos de la sesión anterior |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_
