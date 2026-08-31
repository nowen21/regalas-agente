# Señales del estándar del agente  ·  `[CAPA 3 · memoria por señales]`

Conocimiento de alto valor que **no se recupera leyendo el código ni las reglas**: decisiones, errores resueltos, patrones y aprendizajes. Se guardan señales, no la conversación (`13·DOC5`). La conversación entera vive en [historico-chat/README.md/](../historico-chat/README.md).

Una señal revertida no se borra: se marca `reemplazada` y se enlaza la nueva. Antes de confiar en una vieja, comprobar que sigue vigente.

## Tipos

`decisión` · `error-resuelto` · `patrón` · `aprendizaje` · `alternativa-descartada` · `supuesto` · `restricción` · `pregunta-abierta` · `gotcha` · `deuda-técnica`

**Estado:** `activa` · `reemplazada` · `revertida`.

---

## Señales

## S-001 · El estándar escribía en inglés lo que exige escribir en español  ·  aprendizaje · activa
- **What:** el estándar usaba "spec" en 53 archivos, y su propia regla `01·C8` manda escribir en el idioma del proyecto.
- **Why:** nadie lo notó porque el término se leía como jerga técnica normal. Salió a la luz cuando el usuario preguntó qué significaba.
- **Where:** [base/01-conducta.md](../base/01-conducta.md) · regla `C20`.
- **Learned:** el estándar no se audita a sí mismo con sus propias reglas. Lo que se exige por escrito hay que comprobarlo también sobre el propio texto.
- **When/Who:** 2026-08-14 · usuario + agente.
- **Scope:** estándar.
- **Rel:** —

## S-002 · Escribir código sin haber recorrido la cadena  ·  error-resuelto · activa
- **What:** se escribieron cinco validadores nuevos desde el pendiente 01, sin épica, sin historia de usuario y sin plan aprobado.
- **Why:** el pendiente describía el trabajo con tanto detalle que pareció suficiente para arrancar. Un pendiente no es una historia de usuario: dice qué falta, no qué se acepta como cumplido.
- **Where:** [documentacion/epicas/EP-004-comprobacion-automatica/README.md/](epicas/EP-004-comprobacion-automatica/README.md).
- **Learned:** el pendiente es el origen, no el permiso. Lo escrito quedó como línea base verificada, no como trabajo hecho.
- **When/Who:** 2026-08-14 · usuario.
- **Scope:** estándar.
- **Rel:** —

## S-003 · `F2` está escrita para construir software, no para escribir reglas  ·  pregunta-abierta · activa
- **What:** dos fases seguidas se abrieron declarando que no tienen especificación aparte, porque su entregable es texto normativo o programas cortos.
- **Why:** `F2` da por hecho que lo que se construye es código de un módulo. Cuando el entregable es el propio texto, una especificación aparte diría lo mismo dos veces.
- **Where:** [base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md](../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md).
- **Learned:** una regla que se incumple dos veces seguidas con buenos motivos necesita decir cuándo no aplica, o se vuelve costumbre incumplirla.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendiente 21.

## S-004 · Lo que un validador encuentra sobre el propio estándar no es ruido  ·  aprendizaje · activa
- **What:** al escribir los validadores nuevos aparecieron 354 enlaces que incumplen `DOC14`, 129 reglas sin bloque de checklist, 7 publicadas en "no cumple" y 33 sin clasificar.
- **Why:** son incumplimientos reales del propio estándar, no falsos positivos del validador. Se descubrieron porque nadie los había comprobado nunca.
- **Where:** [validadores/reglas-validables.md](../validadores/reglas-validables.md).
- **Learned:** escribir el validador es la única forma de saber cuánto se incumplía. Antes de tenerlo, el número era cero por falta de medición, no por cumplimiento.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendientes 18 y 19.

## S-005 · Dos sesiones versionando el mismo archivo a la vez  ·  gotcha · activa
- **What:** mientras esta sesión escribía la versión 10.0.0, otra subió la 9.0.0, la 9.1.0 y dejó escrita la 9.2.0 sin guardar. Al final quedaron dos numeraciones vivas.
- **Why:** `VERSION` y el `CHANGELOG` son un archivo único y ninguna sesión sabe qué está haciendo la otra.
- **Where:** [CHANGELOG.md](../CHANGELOG.md) · [VERSION](../VERSION).
- **Learned:** la regla de que cada sesión sube lo suyo se rompe en los archivos que las dos tocan. Hace falta decidir quién manda sobre la versión.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendiente 22.

## S-006 · Mover un archivo que los proyectos llaman por ruta rompe el propio aviso de rotura  ·  error-resuelto · activa
- **What:** la 26.0.0 movió los ocho `hook_*.py` de `validadores/` a `adaptadores/claude-code/` sin dejar nada en la ruta vieja. Los proyectos instalados seguían llamando la ruta vieja: Python salía con código 2, que en el enganche del mensaje **bloquea el mensaje del usuario**, y todos los proyectos quedaron mudos.
- **Why:** el plan de recuperación —«hook_checklist.py lo reclama en el primer mensaje»— corría por el mismo enganche roto. El aviso de desfase viaja por el canal que la mudanza rompe: no puede avisar de su propia caída.
- **Where:** [CHANGELOG.md](../CHANGELOG.md) (26.0.1) · puentes en `validadores/hook_*.py` · [validadores/instalar.py](../validadores/instalar.py).
- **Learned:** lo que otros llaman por ruta absoluta no se muda sin puente en la ruta vieja, y el puente se prueba con el código de salida: para la herramienta, salir con 2 no es fallar — es bloquear al usuario.
- **When/Who:** 2026-08-19 · usuario (reportó el bloqueo) + agente.
- **Scope:** estándar y todos los proyectos instalados.
- **Rel:** S-001 (el estándar no se audita a sí mismo con sus propias reglas).

## S-007 · El enganche de apertura nunca le cargó las reglas al propio estándar  ·  error-resuelto · activa
- **What:** `hook_sesion.py` salía antes de llamar al cargador cuando la carpeta era la del estándar, desde su primera versión (2026-08-05). 30 de 30 aperturas de sesión de este repositorio sin el bloque de reglas; los proyectos herederos sí lo recibían.
- **Why:** la excepción «el propio estándar no se revisa a sí mismo» se escribió para la revisión de instalación y se llevó las reglas por delante. Y nadie lo midió porque las reglas viajan por el canal que no se dibuja: en pantalla se ven los mensajes de estado de los enganches, no lo que llega.
- **Where:** [adaptadores/claude-code/hook_sesion.py](../adaptadores/claude-code/hook_sesion.py) · fase `B-EP-005-HU-009` · caso `arranque-reglas-en-el-estandar` en `evals/`.
- **Learned:** lo que llega por un canal invisible necesita una medición que lo mire, o falta sin que nadie se entere. Y el `CLAUDE.md` §0 de este repositorio lo mandaba por escrito: mandarlo no lo hizo pasar, igual que con el histórico.
- **When/Who:** 2026-08-20 · usuario (preguntó por qué el agente hacía cosas que las reglas no dicen) + agente.
- **Scope:** estándar.
- **Rel:** S-001 · S-006.

## S-008 · El checkpoint se reclama comparando fechas, no leyendo el estado  ·  decisión · activa
- **What:** el enganche del checkpoint decide «falta» o «atrasado» con la fecha de escritura del `estado-fase.md` contra la del documento de puerta recién escrito. No lee ninguno de los dos.
- **Why:** leer el checkpoint y buscar la estación es opinar sobre el texto, y decir en qué estación va la fase es criterio del agente. Dos fechas del sistema de archivos no cuestan nada y no dependen de la redacción.
- **Where:** [validadores/checkpoint.py](../validadores/checkpoint.py) · fase `A-EP-005-HU-013`.
- **Learned:** el aviso se repite mientras el checkpoint siga atrás, a propósito: la marca de «ya avisé» exigiría escribir en un archivo del agente, que es justo lo que este enganche no hace. Solo tres documentos disparan, así que no es ruido.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario en el plan.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-007.

## S-009 · El tramo de consumo es un millón y se decide sin estado  ·  decisión · activa
- **What:** el aviso de consumo a mitad de sesión sale una vez por cada millón de fichas (entrada más salida, sin caché) cruzado, y el cruce se decide comparando el total con el último turno contra el total sin él.
- **Why:** ocho sesiones reales medidas el 2026-08-20 fueron de 144 mil a 12,7 millones: con 200 mil (el tope de la nota de arquitectura) avisaría en todas, y un aviso que sale siempre se deja de leer. Sin estado compartido porque el enganche no tiene archivo propio en el proyecto donde marcar, y crear uno para esto es más estado del que la información vale.
- **Where:** [validadores/presupuesto.py](../validadores/presupuesto.py) · fase `A-EP-005-HU-014`.
- **Learned:** el comando de cierre instalado no se tocó: el modo nuevo entra por un argumento y el viejo es el que corre sin ninguno. Vencer un comando instalado es lo que la 26.0.1 pagó.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario en el plan.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-006.

## S-010 · El andamio traslada solo el enlace que llega exactamente a la raíz  ·  decisión · activa
- **What:** al copiar una plantilla, el andamio reescribe el prefijo `../.../` que desde la carpeta de la plantilla llega a la raíz del repositorio, y el marcador `«RUTA-ESTANDAR»`, con la ruta desde la carpeta de la fase. Un `../` que se queda en `plantillas/`, o que pasa de la raíz, no se toca.
- **Why:** siete fases nacieron hoy con el mismo enlace roto, corregido siete veces con `sed`. Reescribir cualquier `../` habría roto los que no iban a la raíz; las plantillas usan dos formas (`../../` y el marcador) y el andamio atiende las dos para no tocar las plantillas.
- **Where:** [validadores/andamio.py](../validadores/andamio.py) `_reenlazar` · fase `C-EP-004-HU-005`.
- **Learned:** lo que un programa copia de una plantilla hereda la perspectiva de la plantilla, no la del destino. El prefijo se calcula con `relpath`, nunca se escribe fijo.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar.
- **Rel:** S-012.

## S-011 · Un índice que escribe un programa se corrige en el programa, no en el índice  ·  error-resuelto · activa
- **What:** `historico.py` y `resumen.py` escribían el texto del enlace igual al destino (`[2026-08-20/](2026-08-20/)`), y `13·DOC14` pide la ruta desde la raíz. La suite reprobaba cuatro enlaces, dos de ellos nuevos cada sesión.
- **Why:** corregir solo los cuatro habría dejado que la próxima sesión agregara el quinto. La forma del enlace la decide el programa que lo escribe.
- **Where:** [validadores/historico.py](../validadores/historico.py) `_enlace_al_resumen` · [validadores/resumen.py](../validadores/resumen.py) `_indexar_dias` · fase `C-EP-004-HU-008`.
- **Learned:** una suite en rojo por causas viejas esconde la falla nueva; hoy hubo que leer siete fallas para separar tres. El vecino de la misma carpeta sigue por su nombre, que es la excepción que la regla escribe.
- **When/Who:** 2026-08-20 · agente.
- **Scope:** estándar y proyectos instalados (sus índices nuevos nacen bien).
- **Rel:** S-010.

## S-012 · La historia toma el número siguiente al mayor; la fase, el primer hueco  ·  decisión · activa
- **What:** `andamio.py hu` numera la historia con el siguiente al mayor que exista en la épica, como los pendientes; `andamio.py` para la fase sigue tomando la primera letra libre.
- **Why:** la historia se cita por número desde fases, pendientes, commits y el mapa del backlog; un hueco puede ser una historia que se movió, y reutilizarlo haría que «HU-002» apuntara a dos cosas según cuándo se lea. La letra de la fase vive solo dentro de su historia. Un caso lo atrapó: la primera versión tomaba el hueco.
- **Where:** [validadores/andamio.py](../validadores/andamio.py) `siguiente_hu` · fase `B-EP-007-HU-003`.
- **Learned:** los enlaces de la plantilla se trasladan **antes** de poner los propios; al revés, el `../epica.md` recién puesto se trasladaba también. Y la fila del backlog va a «Sin agrupar todavía»: agrupar es criterio y el andamio no lo tiene.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar.
- **Rel:** S-010.

## S-013 · El veredicto se copia solo con concepto escrito, y nunca al checkpoint  ·  decisión · activa
- **What:** `veredicto.py` copia el §6 del resultado a la fila de la historia y a los dos README únicamente cuando el concepto es «cumple» o «no cumple», y no toca el `estado-fase.md`.
- **Why:** un resultado a medio escribir no es un veredicto: propagarlo pondría «no ejecutado» en la historia a cada guardado. El checkpoint es criterio del agente (HU-013). Se reutilizan las expresiones de `fases.py` porque es la que decide la puerta, y dos lecturas del mismo texto se desincronizan.
- **Where:** [validadores/veredicto.py](../validadores/veredicto.py) · [validadores/cerrar.py](../validadores/cerrar.py) `_fila_hecha` · fase `C-EP-005-HU-003`.
- **Learned:** doce copias a mano en un día, y el programa que ya sabía el veredicto solo lo comprobaba después. Se estrenó cerrando sus propias cuatro fases.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-008.

## S-014 · El agente describió lo que Cimiento no tiene sin buscar en el repositorio  ·  error-resuelto · activa
- **What:** al comparar `notas/estructura.md` con Cimiento, el agente respondió que no había memoria semántica vectorial ni política de carga del contexto. Las dos existen: [memoria/semantica.py](../memoria/semantica.py) (FTS5 ∪ `model2vec`, EP-006 · HU-004, cerrada el 2026-08-06) y [validadores/cargador.py](../validadores/cargador.py) (núcleo `00`+`01` literal y sin sellos, el resto como índice, techo de 90 KB vigilado por `pruebas.py`). Se corrigió al tropezar con el 05 en `pendientes/hecho/`, ya con la orden de abrir un pendiente.
- **Why:** se iba a abrir un pendiente por algo construido hace dos semanas. La comparación se hizo sobre lo que el agente había leído en la sesión, no sobre el repositorio; `20·M12` manda buscar antes de crear, y eso vale también para afirmar que algo falta.
- **Where:** [historico-chat/resumenes/2026-08-20/sesion-5.md](../historico-chat/resumenes/2026-08-20/sesion-5.md) H-3 y H-4.
- **Learned:** antes de decir «Cimiento no tiene X», `grep` sobre el repositorio y una pasada por `pendientes/hecho/`. Medido hoy el arranque: 53,9 KB de reglas literales + 14,1 de índice = 68 KB de los 90 del techo; con memoria e histórico, 84 KB. El núcleo pasó de 52 KB el 19-08 a 54 el 20-08.
- **When/Who:** 2026-08-20 · agente, destapado al ejecutar lo que el usuario autorizó.
- **Scope:** estándar.
- **Rel:** S-001.

## S-015 · `sqlite3.connect` crea el archivo si no existe  ·  gotcha · activa
- **What:** para ver qué tablas tenía `senales.db` se abrió con `sqlite3.connect('documentacion/senales.db')`; el archivo no estaba ahí (vive en `memoria/`) y la llamada dejó uno vacío de 0 bytes. Git no lo vio porque `*.db` está ignorado.
- **Why:** una lectura que escribe pasa por inocente. En una carpeta con seguimiento habría aparecido como archivo nuevo; en una ignorada, nadie lo nota.
- **Where:** `documentacion/senales.db` (residuo, pendiente de borrar a mano) · la base real es [memoria](../memoria/) (975 KB).
- **Learned:** abrir en solo lectura, `sqlite3.connect('file:ruta?mode=ro', uri=True)`, que falla si el archivo no existe en vez de crearlo. Y comprobar la ruta antes: el `ls` del mismo comando ya decía que no estaba.
- **When/Who:** 2026-08-20 · agente.
- **Scope:** estándar.
- **Rel:** S-014.

## S-016 · El portero agrega contexto; no reemplaza el resultado de la herramienta  ·  decisión · activa
- **What:** `hook_externo.py` marca lo que una herramienta trae de afuera devolviendo un sobre como contexto adicional del agente (`additionalContext`), y decide por el nombre de la herramienta y sus argumentos, nunca por el resultado. La alternativa de envolver el resultado (`updatedToolResponse`) se descartó.
- **Why:** agregar contexto está en la documentación oficial y no depende de la forma del resultado, que cambia por herramienta y no está documentada; de reemplazarlo la documentación no dice qué herramientas lo aceptan. Y `Read` cuenta como externo solo fuera de la raíz del proyecto: adentro el archivo es del usuario (`04·S9` dibuja la misma frontera).
- **Where:** [validadores/externo.py](../validadores/externo.py) · [adaptadores/claude-code/hook_externo.py](../adaptadores/claude-code/hook_externo.py) · fase `A-EP-005-HU-015`.
- **Learned:** una guarda se diseña sobre lo que se puede probar, no sobre lo más fuerte. Y el mapa del amarre cuenta `hook_` dentro de los docstrings: un módulo agnóstico no nombra a su enganche ni en el comentario, o pasa a amarrado.
- **When/Who:** 2026-08-20 · agente, plan aprobado por el usuario.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-014.

## S-017 · La traza es un lector a demanda y no copia resultados  ·  decisión · activa
- **What:** `validar.py traza` saca la línea de tiempo de una sesión leyendo la transcripción cuando alguien lo pide; no es un enganche, no copia el contenido de ningún resultado, se nombra igual que el histórico de su sesión y empareja llamada con respuesta por identificador, no por orden.
- **Why:** un enganche habría tocado nueve proyectos para algo que se necesita cuando algo salió mal, no en cada respuesta; en los resultados viajan claves y datos; y con llamadas en paralelo las respuestas llegan desordenadas — la primera traza real lo confirmó.
- **Where:** [validadores/traza.py](../validadores/traza.py) · fase `A-EP-005-HU-016` · la primera traza: [historico-chat/trazas/2026-08-20-sesion-5.md](../historico-chat/trazas/2026-08-20-sesion-5.md).
- **Learned:** la sesión que construyó la traza quedó trazada por ella: 191 pasos, 9 errores — y los errores son los tropiezos reales del día (borrados bloqueados, comandos demasiado largos). La medida nació con su primer dato.
- **When/Who:** 2026-08-20 · agente, plan aprobado por el usuario.
- **Scope:** estándar; sirve a cualquier proyecto con histórico.
- **Rel:** S-016.

## S-018 · Una sesión cortada deja artefactos sin cadena: se retoman como línea base, no se rehacen ni se dan por buenos  ·  decisión · activa
- **What:** la sesión que recibió «resuelva el pendiente 16» murió a medias: dejó la regla `M19` y el `CA-05` escritos y sellados, pero la fase con sus cinco documentos en plantilla vacía, sin versión, sin prueba y con una decisión reservada al usuario tomada sin registro. La sesión siguiente no rehizo lo escrito ni lo dio por cerrado: lo declaró línea base en el plan de la fase, sometió a aprobación lo que faltaba, preguntó la decisión pendiente y recién entonces ejecutó pruebas, versión y cierre.
- **Why:** las otras dos salidas pierden algo. Rehacer repite trabajo sin cambiar el resultado; dar por bueno deja una regla que no se puede citar como cumplida (sin prueba ni versión) y normaliza que el orden de `02·F4` se invierta en silencio.
- **Where:** [plan de la fase B](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/plan_trabajo.md), §0 «Cómo llega este plan» y riesgo B-01.
- **Learned:** el detector fue la cadena misma: la transcripción cortada a las 9:08, las plantillas con sus `«...»` y el `VERSION` sin subir dijeron exactamente dónde quedó todo. Y la decisión sin registro se encontró porque el pendiente la dejó escrita como del usuario — lo que se anota como «es de él» se puede reclamar después.
- **When/Who:** 2026-08-21 · agente; opción y planes confirmados por el usuario en el chat.
- **Scope:** estándar; aplica a cualquier proyecto donde una sesión muera a mitad de una fase.
- **Rel:** S-002.

## S-019 · Las pruebas de las vistas escribían el registro real de proyectos  ·  error-resuelto · activa
- **What:** `plantillas/proyectos.md` quedó vacío tres veces en una noche y nadie veía quién lo vaciaba. Eran las pruebas de la interfaz: las vistas llaman `exportar()`, las pruebas llamaban a las vistas con la base de pruebas (vacía tras una baja), y `exportar()` volcaba esa base sobre el archivo real. Un proyecto bien registrado reprobaba «registro» en cada mensaje (pendiente 76, reportado por otra sesión).
- **Why:** una prueba que toca un archivo real del sistema no es una prueba: es un proceso con efectos que corre cuando nadie mira. Y un exportador que escribe cero filas sin preguntarse si antes había algo convierte cualquier base equivocada o vacía en una pérdida de datos.
- **Where:** [interfaz/cimiento/proyectos/core.py](../interfaz/cimiento/proyectos/core.py) (`exportar` con `RegistroVacio`; `registrar`) · [tests.py](../interfaz/cimiento/proyectos/tests.py) (todas con el .md apuntando a una carpeta temporal) · `manage.py registrar` y `validadores/instalar.py` (el alta entra al registro).
- **Learned:** el que lo detectó fue un proyecto instalado, por el checklist que corre en cada mensaje: el estándar se vigiló a sí mismo desde afuera. La regla de oro que queda: toda prueba que escriba, escribe en temporal, y todo exportador se niega a vaciar lo que tenía contenido.
- **When/Who:** 2026-08-22 · agente; el usuario pidió revisar el 76.
- **Scope:** estándar (la interfaz y el instalador).
- **Rel:** S-018.

## S-020 · Un sí dado sobre un diagnóstico viejo se vuelve a verificar contra el estado de hoy  ·  decisión · activa
- **What:** el pendiente 19 pedía cuatro decisiones y el usuario dijo que sí a las cuatro. Al ejecutarlas se encontró que el diagnóstico era del 2026-08-14 y el repositorio ya no era ese: 23 de las 26 particiones estaban hechas desde el 18, dos reglas se habían resuelto sin partirse, y `12·PR3`, que estaba en la lista de derogaciones por «no exigir nada propio», había sido reescrita y hoy exige lo que ninguna otra dice.
- **Why:** ejecutar el sí al pie de la letra habría borrado una exigencia viva (que el dato personal es sensible por defecto) y habría partido reglas ya partidas. La autorización era genuina; lo que había caducado era el diagnóstico sobre el que se dio.
- **Where:** [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), sección «Lo que queda, y es del usuario» · el sello de [`12·PR3`](../base/12-privacidad-datos.md).
- **Learned:** el trabajo de la ronda no fue partir sino **medir de nuevo antes de ejecutar**, y devolverle al usuario las dos que habían cambiado de sentido. Un pendiente con diagnóstico fechado se relee contra el estado actual antes de tocar nada, y lo que cambió se muestra en vez de ejecutarse.
- **When/Who:** 2026-08-22 · agente; las dos decisiones (`17·I3` como una regla, `12·PR3` queda) las tomó el usuario.
- **Scope:** estándar; aplica a cualquier proyecto donde un pendiente viejo se ejecute tal cual.
- **Rel:** S-018.

## S-021 · Un recuerdo que se cumple a medias se sigue incumpliendo, y el hueco es siempre el mismo  ·  error-resuelto · activa
- **What:** el 2026-08-20 quedó escrito el recuerdo «los guiones de apoyo van dentro del repositorio», después de que el usuario preguntara por qué el agente escribía en la carpeta temporal de la herramienta. El 2026-08-22 el agente escribió **31 guiones** en esa misma carpeta durante una jornada entera, y el usuario volvió a preguntar lo mismo.
- **Why:** el recuerdo decía «dentro del repositorio (en una carpeta temporal ignorada por git) **o no se escribe**», y esa puerta —la carpeta temporal— dejaba el cumplimiento a interpretación. El agente leyó «temporal» y usó la de la herramienta. Y el daño no era el sitio: era que **el resultado quedaba versionado y el cómo se perdía**; a la pregunta «¿con qué se recortaron esas treinta reglas?» no había respuesta en ninguna parte.
- **Where:** el recuerdo [historico-chat/memory/guiones-de-apoyo-dentro-del-repo.md](../historico-chat/memory/guiones-de-apoyo-dentro-del-repo.md), reescrito sin la puerta · la carpeta nueva [historico-chat/scripts/README.md/](../historico-chat/scripts/README.md), con los 31 de esa jornada.
- **Learned:** un recuerdo con una alternativa («esto o aquello») se cumple por la alternativa más cómoda. Y la prueba de que un recuerdo funciona no es que esté escrito: es que el usuario no tenga que repetirlo. Cuando lo repite, lo que hay que arreglar es **el texto del recuerdo**, no la conducta de esa vez.
- **When/Who:** 2026-08-22 · usuario: «nada se debe escribir por fuera, todo debe quedar en historico-chat».
- **Scope:** estándar; aplica a cualquier proyecto donde el agente escriba guiones de apoyo.
- **Rel:** S-020.

## S-022 · El inventario dice lo que el proyecto debe tener; quién dice si ya está hecho es la prueba  ·  decisión · activa
- **What:** el agente armó el inventario de Cimiento como una foto de lo construido: 22 de 27 filas marcadas «Existe» por afirmación suya, y decidía si una funcionalidad entraba según si ya estaba hecha o ya estaba decidida. El usuario lo corrigió en dos frases: «el inventario es todo lo que el proyecto debe tener sin importar si ya está hecho» y «cuando se hagan las pruebas es que se sabe si ya se hizo».
- **Why:** son dos errores encadenados. El primero **recorta el inventario**: si una fila se omite porque «eso ya existe», el documento deja de ser la lista de lo que el producto debe tener y se vuelve una lista de trabajo pendiente — y como el inventario madura hasta ser el manual del producto, el manual nace con huecos justo en lo que sí está construido. El segundo **falsifica el estado**: «Existe» dicho por el agente es una opinión sobre código que leyó por encima, y una opinión no es evidencia. El estado sale de la prueba ejecutada, no de la lectura.
- **Where:** [prompts/cimiento-inventario-funcionalidades.md](../prompts/cimiento-inventario-funcionalidades.md) (las 22 filas «Existe» quedan sin respaldo hasta que se prueben) · la plantilla [`02-inventario-funcionalidades.md`](../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), que define los cuatro estados sin decir quién los fija · [`02·F26`](../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md).
- **Also:** el mismo día el usuario quitó del molde toda la historia que arrastraba: la sección «Lo que el usuario ya definió», la fecha del estado, el registro de las preguntas contestadas y la firma del final. Su frase fue «el documento debe quedar como si no hubiera nada desarrollado, pero se debe utilizar la información que ya se tiene para llenarlo». El agente tuvo que oírla tres veces: quitó la sección, después las fechas, después el resto.
- **Learned:** el inventario tiene dos ejes que se estaban mezclando en una sola columna. Uno es **qué debe tener el producto** — completo, y no se poda por nada: ni porque ya esté construido, ni porque ya se haya decidido, ni porque ya aparezca en otra fila. El otro es **qué tan probado está** — y ese lo llena la evidencia de la prueba, con su resultado, no el agente. Mientras no haya prueba, el estado honesto es «sin verificar», que no es lo mismo que «no existe».
- **When/Who:** 2026-08-22 · usuario: «no se debe colocar lo que ya se decidió, el inventario es todo lo que el proyecto debe tener sin importar si ya está hecho» y «cuando se hagan las pruebas es que se sabe si ya se hizo».
- **Scope:** estándar; aplica a todo proyecto que arme su inventario bajo `02·F26`.
- **Rel:** S-020 (medir contra el estado real antes de dar algo por cierto).

## S-023 · Lo que falta no siempre es un pendiente: si el producto debe tenerlo, es una fila del inventario  ·  decisión · activa
- **What:** el agente encontró dos huecos mientras trabajaba el inventario de Cimiento, la lista de partes del proyecto que exige `13·DOC13` y la épica que recoja las funcionalidades de la interfaz, y ofreció anotarlos como pendientes. El usuario paró: «¿pero para qué pendiente si estamos trabajando sobre ese documento?».
- **Why:** un pendiente es para lo que **no** se está haciendo. Abrir uno mientras se tiene el documento abierto convierte un renglón de dos minutos en un trámite de tres pasos, y encima lo saca del sitio donde alguien lo va a buscar. El backlog crece con cosas que ya estaban al alcance de la mano.
- **Where:** el inventario [prompts/cimiento-inventario-funcionalidades.md](../prompts/cimiento-inventario-funcionalidades.md), fila 2.6, escrita en el momento en vez de anotada.
- **Learned:** ante un hueco hay tres destinos y se eligen por lo que el hueco **es**, no por las ganas de dejarlo anotado. Si es algo que el producto debe tener, es una **fila del inventario**, aunque todavía no exista. Si es el paso siguiente de un camino que ya está escrito, no se anota en ninguna parte: se hace cuando toque. Y solo lo que hay que hacer y no cabe en el trabajo de hoy es un **pendiente**. El agente por defecto tiraba todo al tercero, que es el más caro de los tres.
- **When/Who:** 2026-08-22 · usuario, corrigiendo al agente dos veces en la misma sesión (antes ya había dicho «no hay que abrir pendiente, se debe corregir de una»).
- **Scope:** estándar; aplica a cualquier proyecto donde el agente proponga anotar en vez de resolver.
- **Rel:** S-022.

## S-024 · Guardar lo que se hizo y guardar lo que se conversó son dos cosas, y mezclarlas rompe una regla ya aprobada  ·  decisión · activa
- **What:** el usuario pidió que las conversaciones completas entraran a la base «porque eso va a permitir sacar estadísticas y encontrar soluciones: algo que se repita mucho es porque el agente no lo está contemplando». Eso choca de frente con `RN-4` de la especificación de Auditoría, aprobada el mismo día: «se registra la acción, no la conversación», con su razón escrita: la transcripción pesa, se llena de ruido y arrastra credenciales.
- **Why:** el choque era aparente, y el agente estuvo a punto de resolverlo por el camino caro: cambiar la especificación aprobada y la regla. Lo que había era **otra funcionalidad**. La auditoría responde *qué se hizo* y sirve para demostrar; el índice de conversaciones responde *qué se conversó* y sirve para descubrir lo que nadie escribió. Dos preguntas, dos almacenamientos, y ninguna regla que tocar.
- **Also:** la razón que motivaba `RN-4` ya no aplicaba, y comprobarlo tomó un `grep`: [validadores/historico.py:82](../validadores/historico.py#L82) enmascara el mensaje y la respuesta antes de escribir, así que el texto del histórico ya está sin claves. El riesgo que la regla evitaba estaba resuelto desde el pendiente 84.
- **Where:** [pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md](../pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md) · épica [EP-011](epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md) · `F-033` y `F-034` del inventario · sección 14.1 del [análisis](../cvds/analisis-requisitos/README.md).
- **Learned:** cuando una petición del usuario choca con algo ya aprobado, la primera pregunta no es «¿cambio lo aprobado?» sino «¿es lo mismo que lo aprobado, o es otra cosa?». Casi siempre es otra cosa, y entonces no hay conflicto: hay una funcionalidad que faltaba. Cambiar la línea base es lo último que se intenta, no lo primero.
- **When/Who:** 2026-08-25 · usuario: «la idea es que todo ese historial también se vaya guardando en la DB».
- **Scope:** estándar; aplica a cualquier petición que parezca contradecir un documento aprobado.
- **Rel:** S-023 (elegir el destino por lo que la cosa es).

## S-025 · Una corrección que se repite no es un descuido del usuario: es una regla que falta  ·  aprendizaje · activa
- **What:** en una sola sesión el usuario tuvo que pedir «español colombiano» tres veces antes de que quedara escrito como recuerdo, y citar `00·ID9` cuatro veces sobre respuestas distintas del agente. Las dos terminaron en algo escrito, pero porque insistió.
- **Why:** el daño no es la corrección: es que el patrón se pierde. Se atiende el caso, la sesión cierra, y nadie cuenta cuántas veces hizo falta decirlo. La transcripción tiene el dato desde el primer día y nadie lo ha leído nunca con esa pregunta.
- **Where:** [EP-011](epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md), que existe para hacer visible ese conteo. Su métrica de éxito no es que el reporte exista: es que de él salga al menos una regla nueva.
- **Learned:** la señal de que falta una regla no es que algo salga mal una vez. Es que el usuario tenga que decir lo mismo dos veces. Y eso se puede contar, porque está escrito.
- **When/Who:** 2026-08-25 · agente, contando sobre la propia sesión.
- **Scope:** estándar.
- **Rel:** S-021 (un recuerdo que se cumple a medias se sigue incumpliendo).

## S-026 · El orden de las fases lo fija la versión, no el número de la épica  ·  gotcha · activa
- **What:** cerrada la fase A, el paso obvio parecía la fase B, conectar un proyecto. La correcta era la D, la auditoría: lo dice el orden aprobado en la etapa de implementación, «registrar desde el primer día evita tener un tramo sin historia». El agente alcanzó a marcar la B como abierta antes de releerlo.
- **Why:** las épicas están numeradas por tema y las fases por letra, y ninguna de las dos numeraciones es el orden de ejecución. El orden vive en un tercer documento, y si nadie lo mira, se ejecuta en el orden que parece natural.
- **Also:** la dependencia parecía circular: la historia de auditoría declara que depende de la de proyectos, y la de proyectos exige que su conexión quede auditada. Se rompe por lo que la especificación ya decía: una acción sin proyecto se registra igual, con el campo vacío.
- **Where:** [cvds/implementacion/README.md](../cvds/implementacion/README.md) §5 · el [índice de épicas](epicas/README.md), que ahora lo dice en una línea.
- **Learned:** antes de abrir la fase siguiente se mira el orden de la versión, no la letra que sigue. Y una dependencia que parece circular casi siempre se rompe con un caso vacío que la especificación ya contempló.
- **When/Who:** 2026-08-25 · agente, al abrir la fase después de cerrar la A.
- **Scope:** producto Cimiento, y cualquier proyecto con versiones que reordenen sus fases.
- **Rel:** —

## S-027 · El caso de «que NO pase» fue el único que encontró el defecto, y los otros seis estaban en verde  ·  aprendizaje · activa
- **What:** en la fase D, seis de los siete casos del plan pasaron a la primera. `CP-007`, el que dice «que NO pase: que algo cambie sin quedar registrado», falló: `almacen.guardar` se podía llamar directo y el archivo cambiaba sin dejar registro. Con ese camino abierto, `CA-01` no se cumplía y la fase habría cerrado en «No cumple».
- **Why:** los seis casos que pasaron probaban **que la auditoría funciona**. Ninguno podía ver que existía un camino que la esquivaba, porque todos entraban por la puerta correcta. El caso de «que NO pase» es el único que mira el conjunto en vez de la parte, y por eso es el que encuentra lo que nadie pensó.
- **Also:** corregirlo obligaba a tocar `plataforma/nucleo/almacen/`, que el plan aprobado no declaraba. La fase **se detuvo y se pidieron dos opciones con su costo** en vez de ampliar el plan por iniciativa, que es lo que pide [`02·F8`](../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md). El usuario autorizó cerrar el hueco, y la razón que inclinó la balanza fue medible: hoy no hay un solo llamador de esa función fuera de las pruebas, y con la fase B encima ya serían varios.
- **Where:** [resultado_pruebas.md de la fase D](epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/resultado_pruebas.md), `DEF-01` y los dos ciclos · la ampliación autorizada, sección 2.1 del plan.
- **Learned:** un plan de pruebas sin al menos un caso de «que NO pase» puede salir entero en verde sobre una implementación con un hueco. Y cuando ese caso encuentra algo fuera de lo que el plan declaraba, lo correcto es parar y presentar opciones con su costo, no arreglarlo callado: la ampliación queda escrita y con nombre de quien la autorizó.
- **When/Who:** 2026-08-25 · agente y usuario.
- **Scope:** estándar; aplica a cualquier fase con plan de pruebas.
- **Rel:** S-022 (el estado sale de la prueba, no de la lectura).

## S-028 · Treinta y siete pruebas en verde no dicen nada hasta que se saboteó el código  ·  patrón · activa
- **What:** la fase D terminó con 37 comprobaciones automáticas pasando a la primera. En vez de darlo por bueno, se rompió el código a propósito cuatro veces: ejecutar antes de registrar, escribir sin tapar claves, dejar editar una fila del índice, y quitar la exigencia de constancia. Las cuatro veces fallaron las pruebas correctas, y solo entonces se dio el verde por bueno.
- **Why:** una prueba que pasa puede estar probando otra cosa, o nada. Es el mismo defecto que ya se documentó en el estándar: un caso que decía «correr el enganche» corrió la función que el enganche usa, y tres criterios quedaron en «cumple» sin estar probados.
- **Also:** el sabotaje también sirvió para elegir qué prueba escribir. `CP-003` tenía tres pasos que mostraban que ante la falla nada cambia, pero eso pasaría igual con un código que ejecuta primero y revierte después. Hubo que agregar un paso que **espía el orden real**: `["constancia", "efecto"]`.
- **Where:** [evidencias/EV-02](epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), con los cuatro sabotajes y qué prueba cazó cada uno.
- **Learned:** antes de reportar una suite en verde, romper a propósito lo que la suite promete cuidar. Si nada falla, la prueba no estaba probando eso. Cuesta minutos y es la diferencia entre «pasa» y «está probado».
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que reporte pruebas.
- **Rel:** S-027.

## S-029 · Una especificación puede decidir cómo se comporta algo que ningún requisito pidió, y entonces nadie lo construye  ·  error-resuelto · activa
- **What:** al ver la primera pantalla de la plataforma, el usuario preguntó «pero eso no tiene administración?». Buscando la respuesta apareció esto: la especificación del módulo Proyectos decidía en su §7 que **desconectar** pide confirmación, y en su §12 que **desconectar no borra la documentación**, con su alternativa descartada y su porqué. Y no existía ninguna funcionalidad `F-` ni requisito `RF-` que lo pidiera. Su propia §1, la de alcance, no lo nombraba.
- **Why:** una decisión escrita en una especificación **no construye nada**. Lo que baja a fase es el inventario, y si la funcionalidad no está ahí, ninguna fase la va a hacer. El documento queda prometiendo un comportamiento que nadie va a implementar, y el hueco no se ve leyendo la especificación: se ve usando el producto, que es tarde.
- **Also:** el daño concreto era que conectar no tenía reversa. Un proyecto registrado con el nombre o la ruta equivocados quedaba así para siempre, y el arreglo era editar a mano el texto que la plataforma administra. Se comportaba como una acción **que no se deshace** cuando debía ser de las que se deshacen solas.
- **Where:** [pendientes/86-conectar-un-proyecto-no-tiene-reversa.md](../pendientes/86-conectar-un-proyecto-no-tiene-reversa.md) · `F-035` y `RF-35` · [HU-004](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md) · la §15 de la [especificación de Proyectos](proyectos/spec.md), donde quedó anotado el cambio.
- **Learned:** al cerrar una especificación, contrastar sus secciones de comportamiento y de decisiones contra su propia sección de alcance, y contra el inventario. Todo lo que la especificación **describe cómo se comporta** tiene que tener una fila en el inventario, o no se va a construir. Y al revés: una decisión tomada sobre algo que no está pedido es la señal de que falta pedirlo.
- **When/Who:** 2026-08-25 · usuario, con una sola pregunta sobre la pantalla.
- **Scope:** estándar; aplica a cualquier proyecto que escriba especificaciones de módulo.
- **Rel:** S-023 (si el producto debe tenerlo, es una fila del inventario), S-027.

## S-030 · Un guion de sabotaje que restaura con el control de versiones no restaura lo que todavía no está versionado  ·  gotcha · activa
- **What:** para comprobar que las pruebas de la fase B servían, se saboteó el código cinco veces. Cuatro de los cinco archivos se restauraban con una copia guardada; uno se restauraba con el control de versiones, y ese archivo era nuevo y todavía no estaba versionado. Quedó saboteado, y solo se notó al final, cuando la corrida limpia salió en rojo con cuatro errores.
- **Why:** el sabotaje existe para confiar en las pruebas. Un guion que no restaura bien hace lo contrario: deja el código roto y las pruebas fallando por una razón que no es la que se estaba investigando. Si el paso final no hubiera corrido la suite completa, el sabotaje se habría quedado dentro del commit.
- **Where:** [evidencias/EV-02 de la fase B](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/B-EP-008-HU-001-se-conecta-un-proyecto/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), que ahora lo dice en su cabecera.
- **Learned:** el sabotaje se restaura con una copia del archivo, nunca con el control de versiones, porque lo que se está probando suele ser código recién escrito. Y el guion **siempre termina corriendo la suite completa**: si esa última corrida no sale limpia, algo quedó saboteado.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028 (romper a propósito lo que la suite promete cuidar).

## S-031 · Un sabotaje que pasa en verde no siempre significa que falte una prueba  ·  gotcha · activa
- **What:** validando las pruebas de la fase H se saboteó el código seis veces. Cinco fallaron las pruebas correctas; el primero pasó en verde. La lectura inmediata fue «falta una prueba que cubra esto». Era falso: ese sabotaje **borraba la ficha del proyecto y la reescribía enseguida**, así que no cambiaba nada observable. No había hueco: el sabotaje no saboteaba.
- **Why:** el sabotaje existe para medir las pruebas, y también hay que mirarlo a él. Dar por bueno el diagnóstico fácil habría llevado a escribir una prueba que no protege de nada, y a creer que la suite es más fuerte de lo que es.
- **Also:** el sabotaje corregido —borrar la documentación del proyecto al desconectar, que es justo lo que `CA-01` promete que no pasa— sí falló, y falló en las dos pruebas que tenían que fallar.
- **Where:** [evidencias/EV-02 de la fase H](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), que lo dice en el comentario del propio guion.
- **Learned:** cuando un sabotaje pasa en verde, la primera pregunta es **si de verdad cambia el comportamiento**, no si falta una prueba. Un sabotaje válido tiene que romper algo que alguien pueda observar desde afuera: un archivo distinto, una respuesta distinta, un dato distinto. Si el resultado final es idéntico, no era un sabotaje.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028, S-030.

## S-032 · Una confirmación que no dice qué NO va a pasar obliga a adivinar  ·  decisión · activa
- **What:** la fase H tuvo que construir la confirmación de cuatro acciones, entre ellas desconectar un proyecto. La primera forma obvia es preguntar «¿seguro?». Se descartó: lo que el usuario necesita saber antes de desconectar no es que se va a desconectar, sino **si va a perder su documentación**.
- **Why:** una confirmación que solo dice qué va a pasar deja fuera justo lo que da miedo. El usuario que no sabe si va a perder algo, o no confirma, o confirma cruzando los dedos. Ninguna de las dos es una decisión.
- **Also:** por lo mismo se decidió **no preguntar por todo**. Conectar una carpeta nueva no pide confirmación; reconectar una que ya tuvo un proyecto sí, porque ahí sí hay algo que se recibe sin haberlo pedido. Preguntar por todo entrena a confirmar sin leer, y entonces la pregunta deja de proteger.
- **Where:** `CONFIRMACIONES` en [views.py de proyectos](../plataforma/nucleo/proyectos/views.py) y la plantilla `confirmar.html` · `CP-005` del [plan de pruebas](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/plan_pruebas.md).
- **Learned:** toda confirmación de una acción que cambia estado lleva dos listas: **qué va a pasar** y **qué NO va a pasar**. La segunda es la que convierte la pregunta en una decisión. Y se pregunta solo donde hay algo que perder o que recibir sin querer, no en cada botón.
- **When/Who:** 2026-08-25 · agente, construyendo `00·N1` en una pantalla.
- **Scope:** estándar; aplica a cualquier proyecto con acciones que cambian estado.
- **Rel:** —

## S-033 · Cuando un sabotaje pasa en verde hay dos diagnósticos, y hay que distinguirlos  ·  aprendizaje · activa
- **What:** en la fase C uno de los seis sabotajes pasó en verde, igual que había pasado en la fase H. En la H el diagnóstico fue «el sabotaje no saboteaba». Acá se aplicó la misma pregunta y la respuesta fue la contraria: **sí saboteaba**. El sabotaje hacía que corregir la ruta guardara la versión nueva en el índice y dejara la vieja en la ficha, así que al rehacer el índice volvía la vieja.
- **Why:** los dos casos se ven idénticos desde afuera —una suite en verde con el código roto— y llevan a acciones opuestas. Si se diagnostica mal, o se escribe una prueba que no protege de nada, o se deja pasar un defecto real creyendo que el sabotaje era malo.
- **Also:** lo que distinguió los dos casos fue **correr el escenario a mano y mirar el estado final**, no razonar sobre el código. En la fase H el archivo quedaba idéntico; acá quedaba distinto, y se vio en tres líneas de salida.
- **Where:** [evidencias/EV-02 de la fase C](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) · la prueba reforzada, `test_corregir_la_ruta_relee_la_version_de_reglas`, que ahora borra el índice y comprueba contra el texto.
- **Learned:** ante un sabotaje en verde, **no se decide leyendo el código: se corre el escenario y se mira el estado final**. Si el estado quedó igual, el sabotaje era malo. Si quedó distinto, es una prueba floja. Y la forma más común de prueba floja es mirar **lo que devuelve la función** en vez de lo que quedó guardado: la función puede devolver lo correcto y haber escrito otra cosa.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028, S-030, S-031.

## S-034 · Una fase puede llegar medio construida por fases anteriores, y hay que decirlo antes de planearla  ·  patrón · activa
- **What:** al planear la fase C apareció que dos de sus tres criterios ya estaban casi construidos. `ruta_viva` y el aviso de la lista habían salido de la fase B, porque el modelo de datos pedía la ruta viva como campo calculado. Ninguna de las dos fases estaba pensando en la historia de la ruta perdida.
- **Why:** el riesgo no es haberlo construido antes: es **darlo por probado**. Ese código nunca se había ejecutado contra los criterios de esta historia, así que estaba sin verificar aunque funcionara. Un plan que solo mirara lo nuevo habría cerrado la fase dejando dos criterios sin una sola prueba.
- **Also:** decirlo antes también evitó lo contrario, que es rehacer lo que ya estaba. La sección 2 del plan lo puso en una tabla de tres columnas: qué pide la historia, qué hay hoy, qué falta.
- **Where:** [plan_trabajo.md de la fase C](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/plan_trabajo.md) §2 · su plan de pruebas §3.2, que exige probar también lo que ya estaba.
- **Learned:** al abrir una fase, mirar qué de sus criterios ya está construido **por otras fases que no se lo proponían**, y escribirlo en el plan antes de empezar. Lo que aparezca así entra igual al plan de pruebas: construido no es probado, y el estado honesto de ese código es «sin verificar».
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier proyecto que ejecute historias por fases.
- **Rel:** S-022 (el estado sale de la prueba, no de la lectura).

## S-035 · Un sabotaje que escribe fuera del código deja restos que restaurar el archivo no limpia  ·  gotcha · activa
- **What:** en la fase E, uno de los ocho sabotajes hacía que traer escribiera un archivo **dentro de la carpeta del proyecto de origen**, que es justo lo que la fase promete que nunca pasa. La prueba lo cazó y el guion restauró el código. Pero el archivo que ese sabotaje alcanzó a escribir —973 líneas en la raíz del repositorio— **se quedó ahí**, y el guion terminó diciendo que todo estaba bien.
- **Why:** restaurar con copia protege el código, no el mundo. Un sabotaje que solo toca el archivo saboteado se deshace con la copia; uno que escribe, borra o mueve algo afuera deja un rastro que ninguna restauración de código va a limpiar. Y como la suite final salía en verde, el guion no tenía cómo notarlo.
- **Also:** se descubrió por casualidad, en la corrida real: una comprobación que preguntaba «¿hay rastro dentro del repositorio?» salió en verdadero cuando debía salir en falso. Sin esa línea, el archivo se habría ido en el commit.
- **Where:** el guion de sabotaje de la fase E, que ahora declara sus `RASTROS` y los limpia al terminar, nombrando lo que borró · [evidencias/EV-02](epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt).
- **Learned:** antes de escribir un sabotaje, preguntarse **qué deja fuera del archivo que se está saboteando**. Si escribe, borra o mueve algo, el guion tiene que declararlo y limpiarlo al final, y decir qué limpió. La suite en verde no prueba que el sabotaje se deshizo: prueba que el código volvió a su sitio.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028, S-030, S-031, S-033.

## S-036 · Traer un documento «tal cual» transformaba los saltos de línea, y el texto se veía idéntico  ·  error-resuelto · activa
- **What:** el módulo que trae la documentación de un proyecto leía cada archivo con la apertura normal de texto. En Python eso hace traducción automática de saltos de línea: un documento escrito en Windows entraba a la plataforma con saltos de Unix. El texto se ve exactamente igual, y `CA-5` de la especificación dice que **nada se transforma sin que el usuario lo diga**.
- **Why:** es la clase de defecto que ninguna revisión encuentra, porque el documento se lee igual. Lo que cambia es el archivo, y eso aparece después: en un control de versiones que marca las 973 líneas como modificadas, o en una comparación que no cuadra.
- **Also:** lo cazó una prueba que compara **byte por byte**, no como texto. La prueba escrita de la forma cómoda —leer los dos y comparar cadenas— habría pasado en verde, porque al leer los dos con la misma traducción los dos salen iguales.
- **Where:** el `newline=""` de `traer`, en [nucleo/importacion/core.py](../plataforma/nucleo/importacion/core.py), con su porqué escrito al lado para que nadie lo quite por parecer de más.
- **Learned:** cuando algo promete copiar «tal cual», la prueba compara **los bytes**, no el texto. Leer los dos lados con la misma función esconde exactamente las transformaciones que esa función hace: codificación, saltos de línea, espacios del final.
- **When/Who:** 2026-08-25 · agente, en la fase E.
- **Scope:** estándar; aplica a cualquier proyecto que copie o importe archivos.
- **Rel:** S-033 (mirar el estado final, no lo que devuelve la función).

## S-037 · Una fase puede probar todo lo que promete y aun así no cumplir lo que declaró  ·  error-resuelto · activa
- **What:** la fase E declaraba en su plan que recorría «la documentación del ciclo de vida». Pasó sus nueve casos y sus ocho sabotajes, y cerró. Al planear la fase G se descubrió que **no recorría las etapas del ciclo**, que en este proyecto viven en `cvds/`. Peor: esa carpeta tampoco estaba en la lista de las que la fase declara como no miradas, así que **se saltaba en silencio**, contra la regla del propio módulo que dice que nada se pierde sin decirlo.
- **Why:** los nueve casos comprobaban que se trajera lo que se decía traer. **Ninguno preguntaba si lo que se decía traer era todo.** Es un punto ciego que ninguna cantidad de sabotajes cubre, porque el sabotaje rompe el comportamiento y acá el comportamiento estaba bien: lo que faltaba era el alcance.
- **Also:** lo encontró la primera fase que necesitó **usar** lo traído para responder una pregunta concreta. Mientras nadie lo usara, el hueco no se veía.
- **Where:** la sección 5.1 del [cierre de la fase E](epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/funcionalidad_implementada.md), que lo anota sin reabrir la fase · corregido en la tarea 1 de la [fase G](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-003-ver-el-estado-de-un-proyecto/G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto/README.md), con su caso `CP-001`.
- **Learned:** cuando una fase declara que recorre, cubre o abarca algo, hace falta **un caso que compruebe el alcance y no solo el comportamiento**: contar lo que se encontró contra lo que debía encontrarse. Y la prueba más dura de una fase que produce datos es la fase siguiente que los consume: hasta que alguien los use, el hueco no aparece.
- **When/Who:** 2026-08-25 · agente, al planear la fase G.
- **Scope:** estándar; aplica a cualquier fase que declare un alcance de recorrido o cobertura.
- **Rel:** S-034 (construido no es probado), S-027.

## S-038 · Lo que no se puede leer se cuenta aparte, nunca se reparte entre las otras dos cuentas  ·  decisión · activa
- **What:** al calcular en qué va un proyecto, la plataforma tiene que decir cuántas fases siguen abiertas. Contando los 125 estados de fase de este repositorio aparecieron **doce formas distintas** de escribir la línea que dice en qué estación va una fase, y **cinco que no se dejan leer**.
- **Why:** las dos salidas fáciles mienten. Contar las ilegibles como cerradas da 41 abiertas; contarlas como abiertas da 46. Ninguna de las dos cifras es verdad, y las dos se ven igual de creíbles en la pantalla.
- **Also:** la forma de resolverlo fue que la función devuelva **dos** valores: si la fase está abierta, y **si se pudo saber**. Un solo valor obliga a inventar una respuesta para el caso que no se pudo leer.
- **Where:** `_esta_abierta` en [nucleo/proyectos/estado.py](../plataforma/nucleo/proyectos/estado.py) · `CP-004` de la fase G, que prueba el caso de una fase ilegible sola: ni abierta ni cerrada.
- **Learned:** cuando algo se cuenta en dos categorías y hay casos que no se pueden clasificar, **la tercera cuenta no es opcional**: es la que hace verdaderas a las otras dos. Y se nombra con su ruta, porque un número de ilegibles sin decir cuáles no se puede corregir.
- **When/Who:** 2026-08-25 · agente, en la fase G.
- **Scope:** estándar; aplica a cualquier proyecto que calcule métricas leyendo texto escrito por personas.
- **Rel:** S-036, S-033.

## S-039 · El caso donde una funcionalidad no hace nada es donde más falta hace que deje constancia  ·  error-resuelto · activa
- **What:** el módulo que trae la documentación de un proyecto se salía temprano cuando no reconocía **ningún** documento: `if not hallazgo.cuantos: return`. Con eso no escribía el reporte de lo que no entró, y **tampoco dejaba registro en la auditoría**. Alguien traía un proyecto, no entraba nada, y no quedaba constancia de que se hubiera intentado ni de por qué.
- **Why:** la salida temprana parece razonable —«no hay nada que hacer, me voy»— y es exactamente al revés: **cuando el resultado es cero es cuando más falta hace explicarlo**. Un usuario que trae un proyecto y no ve nada necesita saber si la plataforma falló, si la carpeta estaba vacía, o si nada seguía un molde conocido. Sin reporte, las tres se ven igual.
- **Also:** lo cazó el caso de «que NO pase», probando con un proyecto donde **nada** se reconoce. Los demás casos usaban proyectos que traían al menos un documento, y con eso el defecto era invisible.
- **Where:** el comentario en `traer`, en [nucleo/importacion/core.py](../plataforma/nucleo/importacion/core.py) · `CP-008` de la fase F.
- **Learned:** una salida temprana por «no hay nada que hacer» hay que mirarla dos veces: si la función deja constancia, registro o reporte, **el caso vacío también tiene que dejarlo**. Y las pruebas necesitan al menos un caso donde el resultado sea cero, porque el camino del cero casi nunca se recorre con datos de prueba normales.
- **When/Who:** 2026-08-25 · agente, en la fase F.
- **Scope:** estándar; aplica a cualquier operación que produzca registro o reporte.
- **Rel:** S-038 (la tercera cuenta no es opcional).

## S-040 · Un registro que dice cuántos sin decir cuáles no demuestra nada  ·  decisión · activa
- **What:** después de traer 994 documentos, el registro de auditoría decía: «994 reconocidos, 1 sin reconocer». Para saber **cuál** era ese uno había que volver a traer el proyecto entero. El registro cumplía su formato y aun así no servía para lo que la auditoría existe: demostrar meses después qué pasó.
- **Why:** un número es un resumen, y un resumen no es una prueba. El propósito escrito de la auditoría es poder rastrear cualquier cambio hasta su origen; con un conteo, el rastro se corta en el propio registro.
- **Also:** la salida fácil era meter la lista completa en el registro, y se descartó por dos razones. Un proyecto que siga el estándar a medias puede dejar cientos de rutas, y el registro quedaría ilegible **justo cuando más falta hace**. Y ya estaba decidido que la auditoría guarda **la acción**, no el contenido.
- **Where:** el reporte como documento propio, con su fecha, en [nucleo/importacion/core.py](../plataforma/nucleo/importacion/core.py) · el registro que lo **enlaza**: «1 sin reconocer. El detalle, en proyectos/.../reportes/2026-08-25-205102-lo-que-no-entro.md».
- **Learned:** cuando un registro resume algo que tiene detalle, el detalle va **en un documento aparte y el registro lo enlaza**. No se copia en los dos sitios: dos copias de lo mismo se separan con el tiempo. Y la prueba de que el enlace sirve tiene dos mitades: que el registro **no** repita la lista, y que desde su ruta **sí** se llegue al detalle.
- **When/Who:** 2026-08-25 · agente y usuario, en la fase F.
- **Scope:** estándar; aplica a cualquier proyecto con registro de auditoría.
- **Rel:** S-024 (guardar la acción y guardar el contenido son cosas distintas).

## S-041 · Un validador que lo recorre todo termina juzgando lo que no es suyo  ·  decisión · activa
- **What:** la plataforma trajo 1005 documentos de un proyecto y los dejó dentro del repositorio. Los validadores del estándar los revisaron como si fueran documentación propia y reportaron **3840 enlaces rotos**. Ninguno lo estaba: son enlaces relativos que resuelven en el proyecto de origen y no en la copia. El validador no encontró un defecto, encontró que estaba mirando el árbol equivocado.
- **Why:** la pregunta que abrió esto era otra —«¿lo traído se versiona?»— y parecía de arquitectura. No lo era: [`DA-02`](../cvds/diseno/decisiones-de-arquitectura.md) ya dice que **se clona la plataforma y está todo**, y [`DA-10`](../cvds/diseno/decisiones-de-arquitectura.md) ya aceptó la duplicación como costo declarado. Lo traído se versiona porque está decidido desde antes. Lo que faltaba decidir era **hasta dónde llega un validador**.
- **Also:** el arreglo fácil era sacar lo traído del control de versiones, y contradice las dos decisiones aprobadas. El segundo arreglo fácil era saltar toda carpeta llamada `datos`, y **esconde documentación de verdad**: cualquier proyecto puede darle ese nombre a una carpeta suya. Se salta por **ruta**, no por nombre.
- **Also (2):** el filtro sobre el recorrido del disco **no alcanzó**. El trinquete de marcas no recorre el disco: lee **lo preparado en git**, y por ahí volvió a entrar lo traído. Se vio por el reloj antes que por el veredicto — el enganche de guardar se quedó minutos, porque compara contra el historial **una llamada a git por archivo**: mil documentos ajenos, mil llamadas. Con el corte puesto, dos segundos. **Un mismo error de categoría entra por tantas puertas como formas haya de listar archivos**, y arreglar una no arregla las otras.
- **Where:** `EXCLUIDAS_POR_RUTA`, `es_ruta_de_datos` y `es_dato_de_la_plataforma` en [validadores/comun.py](../validadores/comun.py), usados por los cuatro caminos que llegaban hasta ahí: `recorrer_md`, [cerrar.py](../validadores/cerrar.py), [expediente.py](../validadores/expediente.py) y el trinquete de [marcas.py](../validadores/marcas.py).
- **Learned:** un validador tiene un **dominio**, y conviene escribirlo antes de que un directorio nuevo se lo amplíe solo. Lo que otro proyecto escribió no se juzga con las reglas de este: ni sus enlaces, porque resuelven en otra parte, ni sus marcas, porque `00·ID8` habla de lo que **el agente entrega**. Y una falla de 3840 no es 3840 problemas: casi siempre es uno.
- **When/Who:** 2026-08-25 · agente y usuario, al decidir si lo traído se versiona.
- **Scope:** estándar; aplica a cualquier proyecto cuyos validadores recorran el repositorio entero.
- **Rel:** S-037 (una fase puede probar todo lo que promete y aun así no cumplir lo que declaró).

## S-042 · Anidar la documentación de un proyecto dentro de otro la empuja fuera del tope de Windows  ·  error-resuelto · activa
- **What:** al guardar lo que la plataforma trajo, `git add` se negó: **`Filename too long`**. Anidar la documentación de un proyecto bajo `plataforma/datos/proyectos/<identificador>/traido/` le suma 54 caracteres a cada ruta, y eso empujó **59 archivos** por encima del tope de 260 de Windows — el más largo llegó a **307**. En su sitio de origen las mismas rutas caben sin problema.
- **Why:** el que se pasa no es el archivo, es **la suma**: una carpeta de historia de usuario con nombre descriptivo, más una de fase que repite el identificador, más el prefijo de la plataforma. Cada tramo por separado es razonable y el total no lo es. Y no aparece al escribir —la plataforma copió los 1005 archivos sin quejarse— sino al **guardar**, que es cuando ya se decidió todo lo demás.
- **Also:** se activó `core.longpaths` en el repositorio, y con eso entró. **No es una solución completa y conviene no creer que lo sea:** es configuración local, así que quien clone en Windows tiene que activarla también o le faltarán esos 59 archivos — justo lo que `DA-02` promete al decir que se clona la plataforma y está todo.
- **Where:** `git config core.longpaths true` en este repositorio · el commit que guardó lo traído lo deja dicho en su cuerpo.
- **Measured:** la primera explicación —«el prefijo de la plataforma es muy largo»— se midió y **resultó falsa**. El prefijo son 55 caracteres y acortarlo al mínimo razonable ahorra 15: la ruta más larga pasaría de 307 a 292, **sigue sin caber**. Lo que de verdad consume el presupuesto es este repositorio en su propio sitio: su ruta más larga mide **252 caracteres sin prefijo ninguno**, a ocho del tope, y **81 archivos** están a menos de 55 del límite antes de que nadie los anide. La carpeta de fase repite el identificador completo de la épica y de la historia que ya vienen en las dos carpetas de encima.
- **Learned:** una ruta que cabe deja de caber al anidarse, y es tentador culpar al prefijo porque es lo último que se agregó. **Medir dice otra cosa**: el que no deja margen es el árbol de origen. Por eso `core.longpaths` no es aquí un parche sino la única salida barata — las otras dos son renombrar la convención de carpetas del estándar entero, o dejar de anidar, que es el diseño. Y de paso: **cuando una explicación de un tope numérico suena obvia, se resta antes de creerla.**
- **When/Who:** 2026-08-25 · agente, al guardar lo traído.
- **Scope:** estándar; aplica a cualquier proyecto que copie árboles de documentación dentro de sí mismo y se trabaje en Windows.
- **Rel:** S-041 (lo traído se versiona, y por eso llega a git).

## S-043 · Una comprobación puede estar bien escrita y no estar conectada, y sus pruebas no lo notan  ·  error-resuelto · activa
- **What:** la fase construyó una comprobación con seis pruebas que la cubrían. Un sabotaje la **descolgó de la corrida** —le quitó la llamada desde `validar`— y **las seis siguieron en verde**. La función existía, funcionaba, y por el comando que la gente corre no salía nada.
- **Why:** las seis pruebas llamaban a la función **directo**, que es lo natural al escribirlas: se prueba lo que se acaba de escribir. Ninguna preguntaba si alguien la llama. Una comprobación que no sale por el comando que la gente corre es una comprobación que no existe, y este es el modo de fallar que las pruebas de la propia función no pueden ver **por construcción**.
- **Also:** el mismo sabotaje trajo el caso contrario y conviene no confundirlos. Otro sabotaje también pasó en verde y ahí **la prueba tenía razón**: reemplazaba una de las tres veces que el pendiente nombra el comando, así que el archivo seguía diciéndolo. Es `S-033` otra vez, y solo se distinguen corriendo el escenario y mirando el estado final.
- **Where:** `test_el_aviso_sale_en_la_corrida_de_fases` en [validadores/pruebas.py](../validadores/pruebas.py), que busca el aviso **a través de `validar`** y no llamando a la función · `DEF-01` de la fase `A-EP-004-HU-019`.
- **Learned:** toda comprobación nueva necesita **una prueba que la busque por el punto de entrada de verdad**, no por su nombre. Las pruebas de la función dicen que hace bien lo suyo; solo esa dice que alguien la llama. Y la forma de descubrir que falta es sabotear la conexión, no el cuerpo.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-019.
- **Scope:** estándar; aplica a cualquier proyecto donde una comprobación se sume a un recorrido que ya existía.
- **Rel:** S-033 (un sabotaje en verde tiene dos diagnósticos opuestos).

## S-044 · Un guion de sabotaje dijo «suite completa en verde» sin haber corrido una sola prueba  ·  error-resuelto · activa
- **What:** el guion terminaba corriendo la suite entera, que es lo que dice si algo quedó saboteado. Usaba `unittest discover` sobre la carpeta, **encontró cero pruebas**, y reportó `OK`. La salida decía `Ran 0 tests in 0.000s` seguida de `OK`, y se lee como éxito.
- **Why:** el veredicto que cierra una fase salía de una corrida vacía. Dos ciclos antes se habría leído como «todo bien» y la fase habría cerrado sobre nada. **Cero pruebas y `OK` no son lo mismo, y el formato de salida los muestra igual.**
- **Also:** el guion existe justamente para no confiar en que las pruebas sirven. Que él mismo mintiera sobre su corrida final es el mismo error un nivel más arriba: quien vigila también necesita que lo vigilen.
- **Where:** el guion lanza `pruebas.py` como programa en vez de `discover`, y **se cae con error si la corrida final no dice `OK` o dice `Ran 0`** · `DEF-02` de la fase `A-EP-004-HU-019`.
- **Learned:** una corrida de pruebas se valida por **dos** cosas, no una: que no haya fallas **y que haya corrido algo**. Cualquier automatismo que decida sobre una suite tiene que mirar el conteo, porque el caso «no corrió nada» sale con el mismo `OK` que el caso bueno.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-019.
- **Scope:** estándar; aplica a cualquier automatismo que lea el resultado de una suite.
- **Rel:** S-043 (una comprobación que nadie llama), S-035 (los rastros que un sabotaje deja fuera).

## S-045 · Un estándar puede arreglar algo para sí mismo y seguir repartiendo el defecto  ·  decisión · activa
- **What:** el estándar le quitó a su inventario de historias la cuenta escrita a mano, después de que se le desfasara tres veces. **La plantilla que reparte a los proyectos seguía enseñando exactamente eso** — los tres campos por llenar, la tabla de una fila por historia, y seis pasos titulados «Cómo se llena la tabla». Y la comprobación que impedía que la copia volviera miraba `pendientes/48-inventario-hu.md`, escrito fijo: en un proyecto el inventario vive en `documentacion/`, así que no veía nada. **La guardia protegía al estándar y a nadie más.**
- **Why:** arreglar algo puertas adentro se siente terminado, porque la molestia desaparece. Pero un estándar tiene dos superficies —lo que hace y lo que reparte— y **la segunda se multiplica**: cada proyecto que instale la plantilla hereda el defecto entero. El costo del descuido no es uno, es uno por proyecto.
- **Also:** las dos mitades no se descubrieron igual. La de la plantilla quedó declarada en el cierre de la fase anterior, porque apareció mientras se escribía. **La de la ruta fija no la vio nadie**: salió de preguntarse, al abrir la historia siguiente, si un proyecto podía siquiera correr el comando. La pregunta era sobre otra cosa.
- **Where:** [plantillas/inventario-hu.md](../plantillas/inventario-hu.md) reescrita, y `CARPETAS_DEL_INVENTARIO` con `_donde_puede_estar_el_inventario` en [validadores/fases.py](../validadores/fases.py) · versión 34.2.0.
- **Learned:** al cerrar algo que el estándar arregló para sí, la pregunta que falta es **«¿y lo que reparto?»** — plantillas, moldes, instaladores. Y la que la acompaña: **«¿la comprobación que lo vigila mira una ruta fija?»** Una guardia atada a la ruta del propio estándar es una guardia que no viaja.
- **When/Who:** 2026-08-26 · agente y usuario, en la fase A de la HU-020.
- **Scope:** estándar; aplica a cualquier proyecto que reparta plantillas o moldes.
- **Rel:** S-043 (una comprobación que nadie llama).

## S-046 · El mismo defecto tiene dos formas, y una sola expresión no caza las dos  ·  error-resuelto · activa
- **What:** la comprobación busca el rótulo de la cuenta **con un número al lado** — `| **Total de HU** | 113 |` — porque en un inventario de verdad el defecto es un número escrito. Un sabotaje devolvió el campo a la **plantilla** y la suite quedó en verde: en una plantilla el mismo defecto viene como `| **Total de HU** | «N» |`, con el hueco por llenar. Sin número, no había coincidencia.
- **Why:** la plantilla es lo que se copia, así que un defecto ahí se multiplica. Y era invisible **justo en el archivo donde más caro sale**. El sabotaje sí saboteaba; la prueba era la que miraba mal.
- **Also:** conviene no arreglarlo haciendo la expresión más laxa. Que el inventario de verdad exija un número **es correcto**: la narrativa del propio inventario tiene cifras, y marcarlas volvería el aviso ruido. Son dos comprobaciones con dos formas, no una comprobación mal escrita.
- **Where:** `test_la_plantilla_no_trae_campos_de_cuenta` en [validadores/pruebas.py](../validadores/pruebas.py), que busca **el rótulo como campo, valga lo que valga** · el sabotaje 5 de la fase `A-EP-004-HU-020`.
- **Learned:** un defecto que puede aparecer en un archivo lleno **y** en la plantilla de la que ese archivo sale tiene **dos formas**: el valor puesto y el hueco por llenar. Reconocer una y creer que se cubrió el caso es lo fácil. Y la plantilla es la que hay que cubrir primero, porque es la que se reparte.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-020.
- **Scope:** estándar; aplica a cualquier comprobación que valga tanto para un documento como para su plantilla.
- **Rel:** S-045 (lo que el estándar reparte se multiplica), S-033 (los dos diagnósticos de un sabotaje en verde).

## S-047 · «No dupliques lo derivable» no aplica a un hecho histórico  ·  error-resuelto · activa
- **What:** al cerrar una fase se escribió, en el campo «Versión del estándar al cerrar», **«la que declara `VERSION`»** en vez del número. Parecía lo correcto —no duplicar un dato que vive en otro archivo—, y venía de haber pasado el día entero quitando copias. Al subir `VERSION` a la 34.2.0, ese cierre pasó a afirmar que había cerrado bajo una versión que **todavía no existía** cuando cerró.
- **Why:** es el error **inverso** al que se acababa de arreglar, cometido por aplicar bien la regla en el sitio equivocado. La cuenta de historias es derivable: se recalcula del árbol y siempre da lo de hoy. **La versión al cerrar es una foto**: su valor es justamente el de aquel momento, y un puntero al valor de hoy lo destruye.
- **Also:** lo cazó el validador que exige el sello de versión en cada cierre, no una lectura. Y lo cazó **una hora después**, cuando el número cambió: mientras `VERSION` no se movió, el puntero decía lo correcto por casualidad.
- **Where:** el campo del cierre de la fase `A-EP-004-HU-019`, con su número literal.
- **Learned:** antes de reemplazar un dato por un puntero, la pregunta es **si el dato es una foto o una cuenta**. Una cuenta se recalcula y el puntero la mejora; una foto se fecha, y el puntero la falsifica el día que la fuente cambie. Y el síntoma es traicionero: **mientras la fuente no cambie, el puntero parece correcto**.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-020, sobre lo escrito en la fase anterior.
- **Scope:** estándar; aplica a todo campo que registre el estado de algo en un momento dado.
- **Rel:** S-040 (un registro que resume enlaza el detalle) — esta señal marca **dónde deja de valer** aquella.

## S-048 · Se citó cuatro veces una historia como «abierta» sin leer su estado, y estaba cerrada  ·  error-resuelto · activa
- **What:** cuatro fases seguidas declararon no llevar especificación aparte, y las cuatro lo justificaron diciendo que la [EP-001 · HU-010](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) **estaba abierta esperando escribir esa regla**. Sobre esa base se levantó un hallazgo entero, `H-34`, que decía «cuatro ya no es un caso suelto: es la regla que falta». **Era falso.** Esa historia dice `Estado: Done`, cerró el 2026-08-18 con su commit, y su pendiente está en `pendientes/hecho/`.
- **Why:** peor todavía, cerró **diciendo justamente lo contrario**: «nada nuevo, y ese es el resultado». La regla ya existía dos reglas más abajo en el mismo capítulo — [`02·F19`](../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), *«la redacción del CA es la especificación funcional»*—, y en su momento se intentó agregar otra que decía lo mismo y **chocaba con `02·F0`**. Se citó como pendiente algo que ya se había resuelto, y se propuso rehacer un trabajo que además se había descartado con razón.
- **Also:** el error se cometió una vez y se **copió** tres. Cada fase nueva tomó la redacción de la anterior sin volver a la fuente, y **la repetición hizo la afirmación más creíble**, no menos: para la cuarta, «es la regla que falta» se leía como un hecho establecido por acumulación. Lo que se leyó de la historia fue su **narrativa**, que describe el problema en presente porque se escribió antes de resolverlo. Nadie miró el campo `Estado`, que está en la primera tabla.
- **Where:** los cinco documentos corregidos, cada uno diciendo qué afirmaba y por qué era falso · el hallazgo `H-34` del resumen, reescrito.
- **Learned:** **el estado de un documento se lee en su campo de estado, no en su narrativa.** Una historia sin resolver y una resuelta se leen igual en el cuerpo: las dos describen el problema en presente. Y hay una comprobación barata que habría bastado: si la historia dice que falta una regla, **buscar la regla**. Estaba a un `grep` del capítulo que la historia misma nombraba.
- **When/Who:** 2026-08-26 · agente, al ir a construir lo que creía pendiente.
- **Scope:** estándar; aplica a toda cita de un documento como pendiente o abierto.
- **Rel:** S-026 (marcar como siguiente una fase que no lo era) — el mismo error de leer el cuerpo y no el estado.

## S-049 · El desorden que se le echa a la gente suele estar enseñado por el molde  ·  decisión · activa
- **What:** 111 de 115 historias declaraban su estado con una palabra que su propio molde no decía. La lectura fácil era descuido acumulado. **No lo era:** cuatro moldes del estándar enseñaban tres palabras distintas para «terminado» —`Completada` en la épica, `Done` en la historia, `Hecha` en la tarea— y la lista de la épica estaba escrita **dos veces sin coincidir**, con `Cancelada` en una y no en la otra. Quien escribía una historia justo después de una épica repetía lo que acababa de leer.
- **Why:** si el diagnóstico hubiera sido «descuido», el arreglo habría sido corregir 111 documentos y pedir más cuidado — y en seis meses estarían otra vez repartidos, porque los moldes seguirían enseñando lo mismo. **El diagnóstico decide el arreglo**, y el barato es siempre culpar a quien escribe.
- **Also:** el número se movió de 51 a 111 al mirarlo bien. Con el vocabulario que cada molde traía, 63 «cumplían»; contra un vocabulario único y en español, solo 4. **Lo que parecía menos de la mitad era casi todo**, y la diferencia era qué se tomaba por correcto.
- **Where:** la sección 5 de [base/glosario.md](../base/glosario.md), única definición · los cuatro moldes citándola · `vocabulario_de_estados` en [validadores/fases.py](../validadores/fases.py) · versión 35.0.0.
- **Learned:** ante muchos documentos que incumplen lo mismo, la primera pregunta no es quién se descuidó sino **qué les enseñó a hacerlo**. Un incumplimiento repartido y constante casi nunca es descuido: es un molde. Y la prueba está en contar cuántas fuentes distintas dicen la misma cosa — si son más de una, ahí está.
- **When/Who:** 2026-08-26 · agente y usuario, en la fase A de la HU-012.
- **Scope:** estándar; aplica a cualquier proyecto con documentos modelo.
- **Rel:** S-040 (dos copias de un dato se separan) — acá eran cuatro copias de un vocabulario.

## S-050 · Una comprobación que reporta lo que no vino a comprobar apaga las demás  ·  error-resuelto · activa
- **What:** la comprobación del vocabulario reportaba también las historias **sin campo de estado**. El plan lo pedía. Al correr la suite completa, dejó **siete pruebas de estructura en rojo**: sus árboles de mentira no traen ese campo porque no están probando eso.
- **Why:** el rojo no era de las siete: era de haber ampliado el alcance de la comprobación un paso más allá de su tema. Y en un proyecto habría hecho lo mismo con **cualquier historia mínima** — un aviso permanente sobre documentos que están bien para lo que son. **Un aviso que no se puede atender se aprende a ignorar, y el que aprende a ignorarlo ignora también los buenos.**
- **Also:** que el campo falte **sí es** un problema, y no desaparece por sacarlo de acá: pasa a quien comprueba que un documento traiga sus campos, que es otra cosa. Sacarlo no es taparlo; es ponerlo donde se puede atender.
- **Where:** el comentario junto al `continue` en `estado_fuera_del_vocabulario`, en [validadores/fases.py](../validadores/fases.py), diciendo qué decidió y por qué · `test_limites_sin_campo_de_estado_no_lo_reporta_esta_comprobacion`.
- **Learned:** una comprobación tiene **un tema**, y lo que reporte fuera de él sale caro en ruido. La señal de que se pasó es barata de leer: **si al agregarla se ponen en rojo pruebas que no hablan de su tema, el alcance se fue de más** — no las pruebas.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-012.
- **Scope:** estándar; aplica a cualquier comprobación que se sume a un recorrido compartido.
- **Rel:** S-043 (una comprobación que nadie llama), S-046 (el mismo defecto con dos formas).

## S-051 · Un rastro fuera del repositorio no lo muestra ningún `git status`  ·  error-resuelto · activa
- **What:** un sabotaje comprobaba que el instalador no escribiera en la configuración **global** de la máquina. Para eso, el sabotaje la escribía. El guion limpiaba los rastros **al final**, así que los tres sabotajes siguientes corrieron con la global puesta: sus fallas se leyeron como «cazado» y venían del rastro anterior, no del sabotaje.
- **Why:** es `S-035` un nivel más arriba. Allá el rastro era un archivo suelto en el repositorio, y `git status` lo mostraba. **Acá queda fuera del repositorio**, en la configuración de la máquina de quien corre las pruebas: ningún `git status`, ningún validador y ninguna corrida lo delatan. Se descubrió leyendo por qué un sabotaje de **documentación** hacía fallar pruebas de código.
- **Also:** y la prueba que existía justo para ese sabotaje **no lo cazó**. Compara el valor global antes y después dentro de sí misma; si otra prueba ya lo dejó puesto, antes y después son iguales y pasa. Se cambió por preguntar el valor **local** del repositorio: si el instalador escribiera afuera, ahí no habría nada. **Eso no depende del orden en que corran las pruebas**, y lo anterior sí.
- **Where:** el guion limpia el rastro **después de cada sabotaje**, no al final · `test_no_se_toca_la_configuracion_global_de_la_maquina` pregunta por `--local`.
- **Learned:** cuando lo que se prueba es que algo **no** salga de su sitio, el sabotaje tiene que salirse — y entonces el rastro cae donde nada lo vigila. Dos cosas se siguen de ahí: **limpiar entre sabotajes y no al final**, y **desconfiar de una prueba que compara un estado global contra sí mismo**, porque otra prueba pudo dejarlo ya cambiado.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-009.
- **Scope:** estándar; aplica a cualquier prueba que toque estado fuera del proyecto.
- **Rel:** S-035 (los rastros que un sabotaje deja fuera del archivo saboteado), S-033 (los dos diagnósticos de un sabotaje en verde).

## S-052 · Una deuda bien escrita en una fase sin cerrar es una deuda que nadie lee  ·  decisión · activa
- **What:** al cerrar seis fases que llevaban cuatro días ejecutadas y sin su documento de cierre, apareció que una de ellas ya había registrado, el 2026-08-22, que **el enganche no viaja con el repositorio: un clon nuevo no lo tiene hasta correr el instalador**. Eso mismo se volvió a descubrir el 2026-08-26 por otro camino —clonando un repositorio de prueba— y se trató como hallazgo nuevo.
- **Why:** la deuda estaba **escrita, fechada y bien redactada**. Lo que fallaba era dónde vivía: en el resultado de una fase que el inventario contaba entre las incompletas, y a la que nadie volvía. **Cerrar no es papeleo: es lo que pone la deuda donde se lee.**
- **Also:** la misma fase traía otra deuda que también se cobró sola. Decía que la batería de antes de publicar **no corre las pruebas de los validadores**, así que un cambio que rompa una prueba se publica igual. Ese mismo día, la suite completa destapó tres defectos que ninguna otra comprobación vio, y **ninguno habría detenido una publicación**.
- **Where:** los seis cierres del 2026-08-26, cada uno con su tabla de deudas y su estado real · el de `A-EP-005-HU-006`, que dice de dónde venía y cuándo se volvió a descubrir.
- **Learned:** una fase que se queda en la estación de cierre **no deja el trabajo a medias: deja el trabajo invisible**. Lo construido funciona, y lo aprendido se pierde. Y hay una señal barata de que está pasando: **cuando un hallazgo «nuevo» resulta estar escrito en un documento propio con fecha anterior**, lo que falló no fue la memoria — fue que ese documento vivía donde nadie lo cuenta.
- **When/Who:** 2026-08-26 · agente y usuario, al cerrar seis fases de golpe.
- **Scope:** estándar; aplica a cualquier proyecto que registre deuda en documentos de fase.
- **Rel:** S-048 (el estado se lee en su campo, no en la narrativa).

## S-053 · Contar archivos presentes da por terminado un molde sin llenar  ·  error-resuelto · activa
- **What:** cuatro fases figuraban completas en el inventario y su `estado-fase` decía **«Ejecutada y cerrada»**. Su documento de cierre era **el molde en blanco**, con 31 marcadores por reemplazar cada uno: todavía decía `«2-4 líneas en lenguaje claro»` y `AAAA-MM-DD`. El trabajo estaba hecho y probado; lo que faltaba era decir qué quedó.
- **Why:** el inventario cuenta que **el archivo exista**, no que diga algo. Un andamio que crea los cinco documentos vacíos convierte una fase recién abierta en una fase «completa» — y el número que dice cuánto falta se vuelve optimista sin que nadie mienta a propósito. **Es el mismo defecto que el inventario a mano, un nivel más adentro**: antes el número se copiaba, ahora se calcula bien y cuenta lo que no debe.
- **Also:** costó dos veces el mismo día. Primero se afirmó que esas fases «están completas con sus cinco documentos» leyendo la **lista de archivos**; se volvió a leer la existencia y no el contenido, que es `S-048` otra vez. Y una de las cuatro traía escrita una deuda que se volvió a descubrir por otro camino cuatro días después, porque su cierre en blanco la dejaba invisible.
- **Where:** los cuatro cierres escritos el 2026-08-27, cada uno diciendo desde cuándo estaba en blanco · la medida que los encontró: contar marcadores `«…»` y `AAAA-MM-DD` por documento, y separar 4 con 31 de 12 con cinco a siete, que son comillas de prosa.
- **Learned:** cuando algo se cuenta por su presencia, **hay que preguntarse qué pasa si está y está vacío**. Y hay una medida barata que lo destapa: **contar los marcadores del molde que quedaron sin reemplazar**. Un documento con treinta no es un documento: es un formulario. La misma cuenta separa el molde en blanco de la prosa que usa comillas angulares, sin falsos positivos.
- **When/Who:** 2026-08-27 · agente y usuario, al ir a cerrar las fases con criterios en rojo.
- **Scope:** estándar; aplica a cualquier conteo que mire si un archivo existe.
- **Rel:** S-052 (una deuda en una fase sin cerrar no la lee nadie), S-048 (leer la existencia y no el contenido).

## S-054 · El inventario cuenta fases terminadas, no criterios cumplidos  ·  decisión · activa
- **What:** al cerrar cinco fases cuyo veredicto es **«No cumple»**, el inventario pasó de 37 incompletas a 32. Las cinco tienen sus cinco documentos, así que cuentan como completas — **y una de ellas dice que su criterio sigue roto hoy**: `250 de 250 reglas no dicen cuándo se revisó si todavía sirven`, un número que además **crece con cada regla nueva**.
- **Why:** el número que responde «cuánto falta» mide **documentos escritos**, no **exigencias cumplidas**. Y los dos se separan justo donde importa: una fase que midió, encontró un rojo y lo dejó bien documentado está terminada como fase y **no resolvió nada**. Contarla igual que una que cumplió hace que el avance se vea mejor de lo que es.
- **Also:** es la tercera forma del mismo defecto en dos días. Primero el número se copiaba a mano y se desfasaba (`S-049`). Después contaba archivos presentes, y un molde en blanco pasaba por terminado (`S-053`). Ahora cuenta fases cerradas sin mirar su veredicto. **Cada arreglo dejó el conteo más honesto y siguió midiendo la cosa de al lado.**
- **Where:** las cinco fases cerradas el 2026-08-27, cada una declarando su rojo arriba del todo y adónde fue a parar · tres de ellas enlazan la fase que lo resolvió; dos siguen sin resolver.
- **Learned:** un conteo de avance necesita decir **qué mide, en su propio nombre**. «Historias completas» se lee como «historias que cumplen» y son cosas distintas. Y el patrón para detectarlo es este: **si mejorar el trabajo no mueve el número, o moverlo no mejora el trabajo, el número mide otra cosa.** Las dos mitades pasaron hoy: llenar cuatro cierres vacíos no movió nada, y cerrar cinco fases con «No cumple» bajó el número en cinco.
- **When/Who:** 2026-08-27 · agente y usuario, al cerrar las fases con criterios en rojo.
- **Scope:** estándar; aplica a cualquier medición de avance.
- **Rel:** S-053 (contar archivos presentes), S-049 (el molde enseñó el desorden).

## S-055 · Un número de avance necesita una prueba que lo contradiga  ·  decisión · activa
- **What:** la cuenta de historias dejó de contar como hechas las fases que no cumplieron. El número real apareció al medirlo: de **85 terminadas, 51 cumplen** — once cerraron declarando que no, y **23 no dicen si cumplen**. El anterior, `85 completas`, estaba sobrestimado en un **40%**.
- **Why:** «completas» se leía como «cumplen», y no era lo mismo. Con ese número se decidió todo el trabajo de dos días, incluida la decisión de construir esto. **Un número de avance que solo puede subir no informa: acompaña.**
- **Also:** la mejor prueba de que hacía falta se dio sola. La historia que se creó para arreglarlo, sin una línea de trabajo hecha, **contaba como terminada**: el andamio le había creado los cinco documentos vacíos. Con la cuenta nueva cae donde corresponde — entre las 23 que no dicen si cumplen.
- **And:** la causa no era descuido. El molde del cierre ofrecía `Cumple / Cumple con observaciones` y **no tenía forma de decir «No cumple»**, así que diecinueve fases lo escribieron en prosa suelta, cada una a su manera, donde ningún programa lo lee. Y los moldes decían que una fase con un criterio en rojo **no cierra**, mientras diecinueve cerradas lo hacían con razón. **Se corrigió la regla, no la práctica**: cerrar no es aprobar, y dejar la fase abierta esconde su deuda.
- **Where:** `veredicto_de` y `por_veredicto` en [validadores/fases.py](../validadores/fases.py) · los tres moldes con un solo vocabulario · versión 35.2.0, con los dos números en su entrada.
- **Learned:** todo número que mida avance necesita **una forma de empeorar**, y hay que buscarla a propósito. Si no la tiene, no está midiendo el avance: está contando actividad. **La pregunta que lo destapa es qué tendría que pasar para que este número baje** — si no hay respuesta, el número no sirve para decidir.
- **When/Who:** 2026-08-27 · agente y usuario, en la fase A de la HU-021.
- **Scope:** estándar; aplica a cualquier medición de avance.
- **Rel:** S-054 (el inventario cuenta fases terminadas, no criterios cumplidos), S-053 (contar archivos presentes), S-049 (el molde enseñó el desorden).

## S-056 · Un criterio de parada con número exacto caza lo que uno «redondeado» deja pasar  ·  decisión · activa
- **What:** el plan de la fase exigía que las historias que «no dicen si cumplen» bajaran **en siete exactamente**. Bajaron seis según la línea, así que se paró y se investigó. La causa no era el arreglo: **la base se había movido**. Al levantar esa misma fase con el andamio, sus cinco documentos vacíos volvieron a meter su historia entre las «no dicen». La base real era 23, no 22 — y 23 − 7 = 16. El arreglo estaba bien.
- **Why:** si el criterio hubiera dicho «que bajen unas siete» o «que bajen», la diferencia de uno se habría atribuido a un error de la cuenta anterior y se habría seguido de largo. **El número exacto convirtió una discrepancia de una unidad en una investigación**, y esa investigación destapó que la fase creada para arreglar el problema volvía a provocarlo — `S-053` por tercera vez en el día, conmigo adentro.
- **Also:** el caso crítico de esta fase no fue leer la forma que faltaba, sino **no leer de más**. En un resultado la palabra «Cumple» aparece en cada fila de criterio: un lector que la buscara sin exigir su encabezado tomaría el primer criterio por el veredicto de la fase. Eso miente **en la dirección optimista**, que es peor que el defecto que se corregía. Cuatro de las ocho pruebas nuevas comprueban que **no** lea.
- **Where:** `_VEREDICTO_BAJO_TITULO` en [validadores/fases.py](../validadores/fases.py) · el §4.2 del [resultado de la fase](epicas/EP-004-comprobacion-automatica/HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido/B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas/resultado_pruebas.md), que cuenta la investigación completa.
- **Learned:** un criterio de suspensión sirve cuando **falla por poco**. El que dice «que mejore» nunca se activa; el que dice un número exacto se activa por una unidad, y esa unidad suele ser el hilo. Y cuando se mide algo mientras se trabaja sobre ello, **hay que preguntar si el propio trabajo mueve la medición** — abrir una fase para arreglar un conteo es, literalmente, agregarle un caso al conteo.
- **When/Who:** 2026-08-27 · agente y usuario, en la fase B de la HU-021.
- **Scope:** estándar; aplica a cualquier plan de pruebas con criterio de suspensión.
- **Rel:** S-055 (un número de avance necesita una prueba que lo contradiga), S-053 (contar archivos presentes da por terminado un molde sin llenar).

## S-057 · Una regla que solo vive en un recuerdo se deja de cumplir al día siguiente  ·  error-resuelto · activa
- **What:** los guiones de apoyo deben escribirse dentro del repositorio, en `historico-chat/scripts/`. La regla se fijó el 2026-08-20 y el usuario la precisó el 2026-08-22 —*«nada se debe escribir por fuera, todo debe quedar en historico-chat»*— porque se estaba cumpliendo a medias. **Se dejó de cumplir el 2026-08-24**, al día siguiente, y siguió incumplida cuatro días: **38 programas** en la carpeta temporal del sistema, más dos clones enteros de la plataforma con su entorno virtual, 6.831 archivos. Lo destapó el usuario preguntando por qué se seguía escribiendo allá.
- **Why:** la regla estaba escrita, era clara y era del usuario. **Lo que no tenía era quién la hiciera cumplir.** Vivía en un recuerdo, y un recuerdo se consulta cuando uno se acuerda de consultarlo — que es exactamente cuando ya no hace falta. La herramienta, además, ofrece una carpeta temporal en cada sesión y la nombra como el sitio recomendado: **el camino fácil apunta al lado contrario de la regla**, y ahí no gana la buena intención.
- **Also:** el daño no es de orden. El resultado de cada cambio quedaba versionado y **el cómo se borraba con el temporal**: cuatro días de sabotajes, de guiones de cierre y de mediciones no tenían respuesta a «¿con qué se hizo esto?». Y es la segunda vez que se responde esa misma pregunta con nada.
- **Where:** los 38 programas traídos a [`historico-chat/scripts/`](../historico-chat/scripts/) con su fecha real, cada día con su README diciendo qué hizo cada uno y qué se dejó afuera a propósito.
- **Learned:** **una regla que depende de que el agente se acuerde ya está incumplida; solo falta saber desde cuándo.** Es el motivo por el que existe este estándar, aplicado a él mismo. Y hay una prueba barata para saber si una regla necesita programa: **preguntar si la herramienta empuja hacia el otro lado**. Si el camino cómodo la incumple, el recuerdo no alcanza — hace falta un enganche que avise, o un validador que la mire.
- **When/Who:** 2026-08-27 · usuario, preguntando por qué el agente seguía escribiendo en la carpeta temporal.
- **Scope:** estándar; aplica a toda regla del proyecto que hoy solo viva en `historico-chat/memory/`.
- **Rel:** S-055 (un número de avance necesita una prueba que lo contradiga), S-050 (una comprobación que reporta lo que no vino a comprobar).

## S-058 · Contar las formas que uno ya reconoce no es enumerarlas  ·  error-resuelto · activa
- **What:** una fase declaró que el veredicto está escrito de **tres formas** y que **39 fases no lo dicen**. Media hora después, al enumerar de verdad los encabezados de los 130 resultados, salieron **seis títulos distintos** que empiezan por «Veredicto» y **dos** fases sin ningún encabezado. No 39: **2**. Diez historias figuraban como mudas **diciéndolo**, y tres de ellas dicen «No cumple».
- **Why:** la medición contó `**Concepto:**`, la tabla y el encabezado `Veredicto de la fase` —**las formas que el programa ya sabía buscar**— y llamó «sin encabezado» a todo el resto, sin abrirlo. **Eso es `04·R4` cometido en la fase que venía a hacer cumplir `04·R4`.** La diferencia entre contar y enumerar es la que separa una verificación de una confirmación: contar lo que uno reconoce siempre devuelve lo que uno esperaba.
- **Also:** el arreglo tuvo su propia trampa, y no era la obvia. El primer patrón aceptaba **cualquier** título que empezara por «Veredicto», y **hoy no habría fallado** — los 70 encabezados «por criterio de aceptación» van seguidos de tabla, no de la palabra suelta. Pero era **un patrón más ancho que el hecho**, que es exactamente cómo nació el defecto que se estaba corrigiendo. Se ajustó a título exacto tras medir cuál de los seis va seguido de la palabra: **uno solo, quince veces**.
- **And:** el criterio de parada no fue «que se recuperen diez», sino **«que se recuperen diez y que las tres que dicen No cumple estén entre ellas»**. Recuperar solo las siete que cumplen habría dejado el número **mejor y más falso**, y se habría leído como un éxito.
- **Where:** `_VEREDICTO_TITULO_SOLO` en [validadores/fases.py](../validadores/fases.py), con los seis títulos y su cuenta escrita al lado · los guiones que lo midieron, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/), guardados para poder repetir la enumeración.
- **Learned:** **una medición que solo mira lo que ya se reconoce confirma; no verifica.** La forma de romperla es barata y hay que hacerla a propósito: **enumerar la categoría entera y contar cuántas clases distintas hay**, en vez de contar los casos de las clases conocidas. Y para el arreglo, la regla que se sigue: **el patrón se ajusta al hecho medido, no a lo que podría existir** — un patrón que hoy no falla por casualidad es el defecto de mañana.
- **When/Who:** 2026-08-27 · agente, al reanudar el trabajo y mirar una de las «39 sin encabezado».
- **Scope:** estándar; aplica a cualquier medición sobre un conjunto de documentos escritos a mano.
- **Rel:** S-056 (un criterio de parada con número exacto), S-055 (un número de avance necesita una prueba que lo contradiga).

## S-059 · Una medida que separó bien cuatro casos no separa bien seiscientos  ·  error-resuelto · activa
- **What:** `S-053` propuso una medida para saber si un documento sigue siendo el molde sin llenar: **contar los marcadores `«…»` y `AAAA-MM-DD`**. Se comprobó sobre los casos del momento —cuatro con 31 marcadores contra doce con cinco a siete— y separaba limpio. Se recomendó como «ya probada, sin falsos positivos». **En la primera corrida sobre los 664 documentos dio 38, y tres eran de una fase escrita, cerrada y publicada media hora antes**, con 11, 12 y 13 marcadores.
- **Why:** el repositorio usa comillas angulares en prosa todo el tiempo —`«Cumple»`, `«No cumple»`, `«por criterio de aceptación»`—, así que **la cuenta mide el estilo de la casa, no el formulario sin llenar**. Un documento bien escrito y largo acumula más marcadores que un molde corto: la señal y el ruido crecen juntos.
- **Also:** lo que hacía verdadera la afirmación era **el tamaño de la muestra**, no la medida. Dieciséis casos elegidos por ser los sospechosos del día no dicen nada sobre los 648 restantes, y sin embargo la frase «no da falsos positivos» se escribió como si sí.
- **And:** la medida buena no cuenta **cuántos** marcadores hay, sino **cuántos son los del molde**, cruzando cada documento con su plantilla de `plantillas/ciclo-vida-proyectos/`. `«Cumple»` es prosa; `«2-4 líneas en lenguaje claro»` es el formulario. Con ese cruce: **577 sin ninguno, 80 con uno o dos, y 7 que siguen siendo el molde** — cinco `plan_pruebas.md` con 36 marcadores y dos `estado-fase.md` con 16, todos verificados uno por uno.
- **Where:** los dos guiones, el malo y el bueno, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/) — se guardan los dos, porque la diferencia entre ellos es el aprendizaje.
- **Learned:** **una medida se valida sobre el conjunto entero, no sobre los casos que la motivaron.** Los casos que motivan una medida están elegidos por ser extremos, así que cualquier umbral los separa. La pregunta que lo destapa es: **¿qué pasa con los casos que NO me hicieron pensar en esto?** Y hay una forma general de arreglarlo cuando falla: **comparar contra la fuente en vez de contar síntomas** — no «cuántas comillas hay» sino «cuáles de estas comillas están en la plantilla».
- **When/Who:** 2026-08-27 · agente, al medir la línea base del pendiente 88 antes de abrir su fase.
- **Scope:** estándar; aplica a cualquier umbral propuesto desde un puñado de ejemplos.
- **Rel:** S-058 (contar las formas que uno ya reconoce no es enumerarlas), S-053 (contar archivos presentes da por terminado un molde sin llenar).

## S-060 · Un guion que rompe a propósito tiene que restaurar pase lo que pase  ·  error-resuelto · activa
- **What:** el guion de sabotaje de la fase se cayó **entre romper el archivo y restaurarlo**. La causa fue tonta: `print` de una línea de resultado con caracteres que la consola de Windows no sabe escribir. **El repositorio quedó con el sabotaje puesto** — `fases.py` sin la mitad que compara contra la plantilla — y el guion no dijo nada.
- **Why:** un guion que rompe a propósito **es el único programa del repositorio cuyo estado intermedio es un defecto real**. Si muere ahí, no deja un trabajo a medias: deja el código roto y con apariencia de sano, porque nadie vuelve a mirar un archivo que «ya se restauró». La restauración no puede depender de que el guion llegue vivo hasta ella: va en `try/finally`.
- **Also:** el fallo **no se notó al correrlo**, y esa es la mitad peor. El guion se lanzó con `| tail -45`, así que el código de salida que se vio fue el de `tail` —cero— y no el de Python. **Canalizar un guion de sabotaje esconde exactamente lo que se quiere saber.** Se redirige a un archivo y se lee.
- **And:** es la tercera vez en el día que la herramienta que juzga falla, y las tres de la misma familia: un guion que dijo «suite completa OK» sin haber corrido nada (`S-044`), otro que buscaba «OK» en un texto que trae «OK: sin incumplimientos.», y este. **El código que se está construyendo se prueba; el que lo comprueba, no.**
- **Where:** el `try/finally` y la limpieza de la salida en [historico-chat/scripts/2026-08-27/sabotaje_hu022a.py](../historico-chat/scripts/2026-08-27/sabotaje_hu022a.py), con el arreglo escrito en su propio guion al lado.
- **Learned:** cuando un programa deja el sistema en un estado malo a mitad de camino, **la vuelta atrás va en `finally`, no al final del bloque feliz** — y la prueba de que hace falta es preguntarse qué pasa si revienta la línea de en medio. Y para correrlo: **nunca por una tubería**, porque el código de salida que se lee es el del último eslabón. La restauración con copia salvó esto: el archivo bueno estaba en la carpeta de copias, intacto.
- **When/Who:** 2026-08-27 · agente, corriendo los seis sabotajes de la fase A de la `HU-022`.
- **Scope:** estándar; aplica a todo guion que modifique el repositorio para comprobar algo.
- **Rel:** S-044 (un guion dijo «suite completa en verde» sin correr nada), S-051 (un rastro fuera del repositorio no lo muestra ningún `git status`).

## S-061 · Un veredicto «No cumple» es una foto, y nadie la vuelve a mirar  ·  decisión · activa
- **What:** de las tres historias que aparecieron diciendo «No cumple» al enseñarle al programa a leer sus veredictos, **dos ya estaban resueltas de hecho**. `EP-003·HU-002` no cumplía porque *«el planteamiento de esta casa está vacío»* — se llenó el 2026-08-22, y hoy tiene 106 líneas sin un solo marcador. `EP-005·HU-001` no cumplía por *«nada enmascara»* — el enmascarado existe, está conectado al enganche del histórico, y lo construyó `EP-005·HU-002`. **Solo una sigue viva.**
- **Why:** el veredicto se escribe una vez, el día que se cierra la fase, y **nada vuelve a mirarlo**. Lo que arregla el rojo suele ser **otra fase, de otra historia, meses después**, y esa no tiene por qué saber a quién le estaba fallando el criterio. El resultado es un número de trabajo abierto que **solo puede subir**: entra cuando una fase cierra en rojo y no sale nunca.
- **Also:** es el mismo defecto de la jornada, en la dirección contraria. Todo el día el número mintió siendo **optimista** —contaba como hecho lo que no lo estaba— y este lo hace **pesimista**: cuenta como pendiente lo que ya se resolvió. Las dos mitades vienen de lo mismo: **el número se escribe a mano una vez y después vive solo**.
- **And:** hay una asimetría que lo explica. Cuando una fase cierra bien, su rastro apunta hacia adelante —qué dejó, dónde quedó—. Cuando cierra en rojo, **el rastro que haría falta apunta hacia atrás**: quién viene después a arreglarlo. Y ese eslabón no lo escribe nadie, porque en el momento de cerrar todavía no existe.
- **Where:** los tres veredictos, en `EP-001·HU-007`, `EP-003·HU-002` y `EP-005·HU-001` · la comprobación que los hizo visibles, en `veredicto_de` de [validadores/fases.py](../validadores/fases.py).
- **Learned:** **hacer visible un número no lo vuelve cierto.** Un rojo declarado necesita algo que lo cierre —una fase que lo nombre, una comprobación que lo vuelva a correr— o se convierte en deuda perpetua que nadie se atreve a borrar porque nadie sabe si sigue siendo cierta. **La pregunta que lo destapa: ¿qué tendría que pasar para que este número baje, y quién lo haría?** Si la respuesta es «alguien que se acuerde», ya está mal.
- **When/Who:** 2026-08-27 · agente, al ir a recomendar por dónde seguir y comprobar los tres rojos uno por uno en vez de creerles.
- **Scope:** estándar; aplica a todo veredicto o hallazgo que se escriba con fecha y no se vuelva a evaluar.
- **Rel:** S-055 (un número de avance necesita una prueba que lo contradiga), S-052 (una deuda en una fase sin cerrar no la lee nadie).

## S-062 · Una prueba que se rompe cuando el repositorio mejora está atada al síntoma  ·  error-resuelto · activa
- **What:** una prueba comprobaba que `B-EP-004-HU-011/plan_pruebas.md` fuera reconocido como plantilla sin llenar. **Era cierto cuando se escribió, y dejó de serlo el mismo día**: ese documento se escribió unas horas después — que era exactamente el objetivo del trabajo. La prueba se cayó **porque el repositorio mejoró**.
- **Why:** apuntaba a **un caso concreto del árbol real**, no a la regla. Un documento sin llenar es un estado transitorio por definición: el trabajo consiste en que deje de estarlo. **Atar una prueba a un ejemplo que se quiere eliminar la condena a fallar el día que se cumple el objetivo.** Se reescribió copiando la plantilla real a un árbol de mentira: la plantilla no cambia, el caso sí.
- **Also:** el mismo día se encontró la falla gemela, y peor. Una comprobación decía `assertIn("«", mensaje + "«")` — **cierta siempre**, porque compara contra un texto al que se le acaba de pegar lo que busca. Pasaba con cualquier mensaje, incluso vacío, y por eso un sabotaje que vaciaba el aviso pasó en verde. **Una comprobación que no puede fallar da la misma señal verde que una que funciona.**
- **And:** un tercer caso de la misma familia, el más engañoso: una prueba usó una ruta con un byte nulo creyendo que reventaría al resolverse, para tocar la rama de «ante la duda se calla». **No revienta** — se resuelve contra el directorio actual como cualquier otra, así que la prueba nunca tocó la rama que decía probar. Se reescribió forzando el fallo a propósito.
- **Where:** las tres, en `validadores/pruebas.py`, cada una con el porqué escrito encima · los sabotajes que destaparon dos de ellas, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/).
- **Learned:** hay tres formas de que una prueba mienta en verde, y las tres se ven igual desde el reporte: **está atada a un caso que va a desaparecer**, **no puede fallar**, o **no toca la rama que dice tocar**. Ninguna se descubre leyendo la prueba — las tres salieron **rompiendo el código a propósito y viendo qué no se cayó**. La pregunta que las separa: *¿qué tendría que cambiar en el código para que esta prueba fallara?* Si la respuesta es «nada» o «algo que no es el tema», la prueba no está probando.
- **When/Who:** 2026-08-27 · agente, saboteando las fases `A` de la `HU-022` y de la `HU-018`.
- **Scope:** estándar; aplica a toda prueba que nombre un archivo del árbol real o compare contra algo construido en la propia comprobación.
- **Rel:** S-043 (una comprobación puede estar bien escrita y no estar conectada), S-060 (un guion que rompe a propósito restaura en `finally`).

## S-063 · Un veredicto puede estar mal el día que se escribe, no solo envejecer  ·  error-resuelto · activa
- **What:** de los dos rojos que parecían resueltos de hecho, **solo uno lo era**. `EP-005·HU-001` no cumplía su exigencia de privacidad porque *«nada enmascara»*, y hoy sí enmascara — el veredicto **fue cierto y dejó de serlo**, que es `S-061`. Pero `EP-003·HU-002` no cumplía porque *«el planteamiento de esta casa está vacío»*, **y su `CA-01` no pide eso**: pide que existan los tres modelos y que la cadena se recorra en los dos sentidos. La propia fase escribió que los tres existen y que **no hay una sola falla en 68 historias**. **Se reprobó a sí misma por algo que su criterio no exige.**
- **Why:** un criterio de aceptación es el contrato de la fase, y **medirla contra algo de al lado la deja en rojo sin que nadie pueda cerrarlo** — no hay trabajo que hacer, porque el trabajo que pedía el criterio ya estaba hecho. El rojo queda ahí, se hereda a la historia, y quien lo lea después va a buscar un defecto que no existe.
- **Also:** cómo se cuela. El criterio dice *«existen los tres modelos»*, y el modelo del planteamiento existía; lo que faltaba era **el documento que ese modelo produce en este repositorio**. Son dos cosas: **el molde y lo que se llena con él**. La fase encontró un hueco real —la casa no tenía su planteamiento, y lo anotó bien— y **lo cobró en la factura equivocada**.
- **And:** es el mismo defecto de toda la jornada, en otra escala. El conteo de historias midió cuatro veces la cosa de al lado; acá lo hizo un veredicto. **Un rojo mal puesto cuesta más que un verde mal puesto**: el verde se descubre cuando algo falla, y el rojo no se descubre nunca, porque nadie duda de una mala noticia.
- **Where:** los dos veredictos, en las fases `A` de `EP-003·HU-002` y `EP-005·HU-001` · el enmascarado comprobado corriéndolo, no leyéndolo: `API_KEY=…` sale tapado y «la clave del asunto» no se toca.
- **Learned:** antes de aceptar un «No cumple», **hay que leer el criterio y preguntar si lo que falló es lo que el criterio pide**. Y hay una señal barata de que está mal puesto: **si la justificación del rojo nombra algo que no aparece en el criterio**, o si «qué falta para que cumpla» resulta ser trabajo de otra historia, el veredicto está midiendo otra cosa. El hallazgo se conserva; lo que se corrige es dónde se cobra.
- **When/Who:** 2026-08-27 · agente, al ir a cerrar dos rojos que creía envejecidos y encontrar que uno nunca fue cierto.
- **Scope:** estándar; aplica a todo veredicto de fase.
- **Rel:** S-061 (un veredicto «No cumple» es una foto y nadie la vuelve a mirar), S-054 (el inventario cuenta fases terminadas, no criterios cumplidos).

## S-064 · Una historia se crea, se le hace su carpeta, y nadie vuelve a la tabla de su épica  ·  error-resuelto · activa
- **What:** al volver a medir la cadena de trazabilidad sobre el árbol real —en vez de citar la medición de otra fase— apareció que **tres historias no estaban en la tabla de su épica**: `HU-036` en `EP-001`, y `HU-017` y `HU-018` en `EP-005`. Las tres tenían su carpeta, su documento y su trabajo; lo que faltaba era la fila.
- **Why:** la carpeta y el documento se crean en el momento de trabajar, y **la tabla de la épica se edita en otro archivo y en otro momento**. Nada obliga a volver. La historia queda accesible por su ruta, así que el hueco no molesta a nadie hasta que alguien intenta recorrer la cadena **de arriba abajo** — y ahí no existe.
- **Also:** la detección ya estaba construida y funcionando. `trazabilidad.py` reportaba las tres, con su nombre, desde el día que se crearon. **El problema no era que no se supiera: era que el hallazgo salía entre otros cuarenta y cinco avisos**, y un aviso que convive con cuarenta y cuatro no se lee. Se arreglaron las tres y la cadena quedó en **cero fallas sobre 11 épicas y 119 historias**.
- **And:** lo destapó una regla del plan, no la casualidad. La fase decía *«se corre, no se cita»* — apoyarse en la medición de otra fase habría heredado su resultado de hace diez días, cuando la cadena sí estaba limpia. **Una medición vieja no es una medición.**
- **Where:** las tres filas, en las tablas de `EP-001` y `EP-005` · el guion que volvió a medir, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/).
- **Learned:** cuando el trabajo se registra **en dos sitios que se editan en momentos distintos**, el segundo se queda atrás — y da igual cuál sea el segundo. La pregunta que lo destapa: **¿qué archivo hay que tocar después, en otro rato, para que esto quede completo?** Ese es el que va a faltar. Y si ya hay un programa que lo detecta, el trabajo no es construir otro: **es que su hallazgo no se pierda entre los demás**.
- **When/Who:** 2026-08-27 · agente y usuario. El usuario cortó la propuesta de anotarlo como pendiente: *«¿para qué dejar pendientes si se puede solucionar?»*.
- **Scope:** estándar; aplica a todo dato que viva en un documento y en el índice de otro.
- **Rel:** S-063 (un veredicto puede estar mal el día que se escribe), S-057 (una regla que solo vive en un recuerdo se deja de cumplir al día siguiente).

## S-065 · Hacer el trabajo y verificarlo no cierra un rojo: nada lee la corrección  ·  decisión · activa
- **What:** se construyeron dos fases que volvían a verificar criterios declarados en rojo, se midió que hoy se cumplen —enmascarado corriendo por sus dos mitades, cadena de trazabilidad en cero sobre 11 épicas y 119 historias— y las dos cerraron con «Cumple». **El número no se movió: `16 no cumplen` siguió siendo 16.** El conteo mira **todas** las fases de la historia, y las fases `A` siguen diciendo «No cumple».
- **Why:** la regla que lo causa es correcta para su caso — *«basta una fase que no cumpla»* impide que cerrar la primera fase cierre la historia. Lo que le falta es distinguir **«todavía no se hizo»** de **«se hizo después, y una fase posterior lo verificó»**. Sin esa distinción, **un rojo no tiene forma de cerrarse**: se puede hacer el trabajo, medirlo y declararlo, y el número no lo lee.
- **Also:** es la vuelta de `S-061` con la prueba en la mano. Aquella dijo que un rojo declarado necesita algo que lo cierre; **esto comprueba que hacerlo a mano tampoco basta**. Y explica por qué el número solo sabe empeorar en esa cuenta: entra cuando una fase cierra en rojo y **no sale nunca**.
- **And:** lo medido antes de diseñar cambia el diseño. De las **16 historias con un rojo, 8 tienen una fase posterior y 8 no**. Pero **tener fase posterior no es haber resuelto el rojo**: una fase que trabajó otro criterio no arregla el anterior. De las ocho, solo dos volvieron a verificar de verdad. **Por eso el reemplazo se declara y no se deduce** — deducirlo por el orden taparía rojos vivos con trabajo ajeno, que es la forma optimista de mentir.
- **Where:** las dos fases `D` de `EP-003·HU-002` y `EP-005·HU-001` · `por_veredicto` en [validadores/fases.py](../validadores/fases.py) · la medición, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/).
- **Learned:** **un estado que solo tiene camino de entrada no es un estado: es una marca.** Al diseñar cualquier cuenta hay que preguntar **cómo sale algo de acá, y quién lo saca** — si la respuesta es «nadie», la cuenta va a crecer para siempre y dejará de mirarse. Y la salida se **declara**, no se infiere del orden: lo implícito tapa por accidente justo lo que la cuenta viene a mostrar.
- **When/Who:** 2026-08-27 · agente y usuario, al terminar dos fases que verificaban rojos y ver que el número no se movía.
- **Scope:** estándar; aplica a cualquier cuenta de deuda o de hallazgos.
- **Rel:** S-061 (un veredicto en rojo es una foto y nadie la vuelve a mirar), S-055 (un número de avance necesita una prueba que lo contradiga).

## S-066 · La mayoría de las fases no tiene dónde marcar la casilla que nadie marca  ·  decisión · activa
- **What:** el pendiente 87 decía que **la estación del commit casi nunca se marca**, porque el commit ocurre después de que el agente termina de escribir. Al medirlo antes de construir salió lo esperado —**22 fases cerradas de hecho con la casilla en blanco**— y algo que no: **de los 140 `estado-fase.md` del árbol, 106 ni siquiera traen la fila de la estación 12**.
- **Why:** el problema no era solo que nadie volviera a marcar. **Tres de cada cuatro fases no tienen dónde.** Se escribieron con otra estructura, o sin la tabla de estaciones, y un programa que ponga el hash no tendría en qué escribirlo. **Un automatismo sobre un campo que no existe en el 76% de los casos no es una solución: es una solución para la minoría que ya estaba bien.**
- **Also:** es el mismo patrón de `S-053` y `S-064` una vez más — **medir antes de construir cambió el alcance**. Sin la medición, la historia se habría escrito para «los que no marcan», y al correrla habría tocado 34 fases de 140 sin que nadie entendiera por qué las otras no se movían.
- **And:** el reparto separa dos trabajos que se ven igual. De las 23 sin marcar, **22 son solo la marca** —su documento de cierre ya está en git, comprobado contra el historial— y **una es trabajo de verdad**. Contarlas juntas daría 23 «fases sin commitear» donde hay una.
- **Where:** la medición, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/) · el [pendiente 87](../pendientes/hecho/el-hash-del-commit-se-anota-solo.md).
- **Learned:** antes de automatizar el llenado de un campo, **hay que contar en cuántos documentos ese campo existe**. La pregunta es corta y ahorra el trabajo entero: **¿sobre cuántos de los casos reales puede actuar esto?** Si la respuesta es «sobre los que ya estaban bien», el automatismo no resuelve el problema que lo motivó — y el resto queda igual, pero ahora con la apariencia de estar cubierto.
- **When/Who:** 2026-08-27 · agente y usuario, al bajar el pendiente 87 a historia.
- **Scope:** estándar; aplica a todo automatismo que escriba en un campo de un documento.
- **Rel:** S-064 (una historia se crea y nadie vuelve a la tabla de su épica), S-053 (contar archivos presentes da por terminado un molde sin llenar).

## S-067 · Un enganche que arregla algo después del commit no puede meterlo dentro de ese commit  ·  decisión · activa
- **What:** para que la casilla del commit se marcara sola hacía falta el hash, y **el hash no existe hasta que el commit está hecho**. Se midió en un repositorio de mentira antes de escribir código: el enganche escribe bien, el commit se hace, el hash es el correcto — **y el archivo queda modificado y sin guardar**. Lo que quedó dentro del commit sigue diciendo `PENDIENTE`.
- **Why:** es una consecuencia del orden, no un defecto que se pueda pulir. **Cualquier automatismo que necesite el resultado de una operación para completarla llega tarde por definición**, y solo tiene tres salidas: dejar el rastro para después, reescribir la operación, o hacer otra encima.
- **And:** las tres se descartaron o se eligieron **por argumento, no por gusto**. Reescribir el commit (`--amend`) **se muerde la cola**: cambia el hash, así que el documento apuntaría a un commit que ya no existe. Hacer un segundo commit automático **cruza `00·N1`** — un cambio de estado sin aprobación, y eso es núcleo blindado. Queda dejar el archivo modificado, que es la única donde **nada se reescribe y nada se guarda sin que el usuario lo apruebe**.
- **Also:** el costo se declara en vez de disimularse: **después de cada commit el árbol queda sucio**, con un archivo y una línea, que entra en el commit siguiente. Puede confundirse con trabajo sin guardar, y por eso el conteo tiene que decir por nombre cuáles son.
- **Where:** la medición, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/) · la duda declarada en el §2.7 del plan, con su instrucción de parar si el resultado no se explicaba en una línea.
- **Learned:** **cuando un automatismo necesita el resultado de lo que quiere completar, no hay solución limpia: hay tres costos y se elige uno.** Escribirlos los tres antes de decidir es lo que evita descubrir el elegido por sus efectos. Y la pregunta que ordena la elección no es cuál es más cómoda, sino **cuál no rompe una regla de núcleo** — acá dos de las tres la rompían, y eso dejó una sola.
- **When/Who:** 2026-08-27 · agente y usuario, resolviendo la duda declarada antes de construir.
- **Scope:** estándar; aplica a todo enganche que actúe después de la operación que documenta.
- **Rel:** S-066 (la mayoría de las fases no tiene dónde marcar), S-060 (un guion que rompe a propósito restaura en `finally`).

## S-068 · Un sabotaje que no se pudo aplicar no es un sabotaje que pasó  ·  decisión · activa
- **What:** al sabotear la fase se rompieron cinco piezas y **cuatro se cazaron**. La quinta no: el guion imprimió *«NO SE PUDO SABOTEAR: el texto cambió»*. La causa era boba — el texto del sabotaje se escribió **sin los acentos** que el archivo real tiene, así que la búsqueda no encontró nada y no se rompió nada.
- **Why:** **un sabotaje que no se aplica produce exactamente la misma salida que un sabotaje que las pruebas no detectan: todo en verde.** Sin la guardia que lo dice, se habría leído como «las pruebas no cazan este caso» —y se habrían escrito pruebas nuevas para un defecto que nunca se introdujo— o, peor, como «cinco de cinco cazados». Las dos lecturas llevan a decisiones equivocadas y ninguna se distingue del resultado.
- **Also:** la guardia era una línea, y estaba puesta desde el primer guion de la jornada. **Lo que la hace valiosa no es lo que evita: es que convierte un silencio en un mensaje.** Un guion que sabotea sin comprobar que sabteó de verdad no está midiendo la calidad de las pruebas — está midiendo si acertó a escribir el texto.
- **And:** el mismo día, la suite completa cazó un defecto que las pruebas propias no vieron: un hallazgo nuevo **no nombraba la regla que se incumple** en la forma que el estándar exige. **La clase propia estaba en verde**; lo encontró una prueba transversal escrita meses antes. Es la tercera vez en la jornada que el estándar comprueba al agente.
- **Where:** el `sabotaje_hu019a.py` y su línea de guardia, en [historico-chat/scripts/2026-08-27/](../historico-chat/scripts/2026-08-27/).
- **Learned:** **todo guion que rompe algo a propósito tiene que comprobar que lo rompió**, y decirlo cuando no. La regla general: **cuando una herramienta puede fallar en silencio produciendo el mismo resultado que el éxito, hay que hacerla hablar** — no por prolijidad, sino porque el silencio se lee como la conclusión que uno esperaba. Y correr la suite entera, no solo la clase propia: lo que vigila el trabajo de uno rara vez es lo que uno acaba de escribir.
- **When/Who:** 2026-08-27 · agente, saboteando la fase A de la `HU-019`.
- **Scope:** estándar; aplica a todo guion de sabotaje y a toda comprobación que pueda no ejecutarse.
- **Rel:** S-062 (tres formas de que una prueba mienta en verde), S-044 (un guion dijo «suite completa en verde» sin correr nada).

## S-069 · Recomendar trabajo sin leer el criterio repite el error que uno acaba de señalar  ·  error-resuelto · activa
- **What:** se recomendó tres veces revisar las 250 reglas del estándar, presentándolo como la deuda que sostenía un veredicto en rojo — *«`251 de 251` sin fecha de revisión»*. **El `CA-04` de esa historia no pide que las reglas estén revisadas:** pide que **se sepa cuáles llevan más tiempo sin revisarse**, ordenadas, con su fecha y sus incumplimientos. `vigencia.py` hace exactamente eso.
- **Why:** y no era ambiguo. El documento del procedimiento lo dice en una línea: *«arranca ausente en todas las reglas, a propósito; ponérsela de una vez a las doscientas habría sido escribir doscientas fechas que no responden por ninguna revisión»*. **La ausencia de fechas es el diseño**, y tratarla como deuda habría llevado a sellar 250 reglas sin revisarlas — exactamente el sello vacío que ese documento existe para evitar.
- **Also:** es el mismo defecto que se había señalado **dos horas antes** en otra fase, y escrito como `S-063`: un veredicto que reprueba por algo que su criterio no pide. **Haberlo nombrado no evitó repetirlo** — y esta vez el error no estaba en un documento viejo sino en la recomendación que se le daba al usuario para decidir en qué trabajar.
- **And:** lo que lo destapó fue leer el procedimiento **para poder ejecutarlo**, no para revisarlo. La recomendación se sostuvo tres veces sin abrir ni el criterio ni el documento que lo explica; bastó ir a hacer el trabajo para que se cayera en la primera lectura.
- **Where:** el `CA-04` de `EP-001·HU-007` · [base/20-meta-reglas/revision-de-vigencia.md](../base/20-meta-reglas/revision-de-vigencia.md) · la salida real de `vigencia.py`, que ordena las 251 y dice cuántos incumplimientos produce cada una.
- **Learned:** **antes de recomendar trabajo, leer el criterio que lo justifica** — no el resumen de quien lo declaró en rojo. Un rojo heredado se cita con la misma confianza que un hecho medido, y **nadie duda de una mala noticia**. La comprobación es barata y cabe en una pregunta: **¿lo que falta es lo que el criterio pide, o es un estado de los datos que alguien interpretó como falta?**
- **When/Who:** 2026-08-27 · agente, al ir a ejecutar el trabajo que él mismo había recomendado tres veces.
- **Scope:** estándar; aplica a toda priorización que se apoye en un veredicto ajeno.
- **Rel:** S-063 (un veredicto puede estar mal el día que se escribe), S-061 (un veredicto en rojo es una foto y nadie la vuelve a mirar).

## S-070 · Un checklist que uno firma sobre su propio trabajo no comprueba nada  ·  error-resuelto · activa
- **What:** la regla `04·S18`, escrita el mismo día, llevaba su bloque de checklist declarando **«CUMPLE» en las veinte filas**. La fila 10 —que el cuerpo quepa en el molde— **era falsa**: medía 360 caracteres para un límite de 320. Lo destapó `validar.py metareglas` al ir a mirar otra cosa, horas después y por casualidad.
- **Why:** el checklist se escribió **a la vez que la regla y por la misma mano**, en el mismo minuto, sin correr la comprobación que existe para eso. **Un checklist así no es una verificación: es una declaración de intenciones con forma de tabla** — y su peor efecto no es que falle, sino que **queda escrito como si alguien hubiera comprobado**, y el siguiente que lo lea no vuelve a mirar.
- **Also:** el defecto no era invisible: hay un programa que lo mide y bastaba correrlo. **La regla se firmó y se publicó sin ejecutarlo**, en una jornada en la que el agente había escrito tres señales sobre no afirmar lo que no se midió. Lo que fallaba no era saberlo.
- **And:** lo que sobraba tampoco era exigencia. Al recortar quedó a la vista que el cuerpo mezclaba **la orden** —dónde va el guion— con **el porqué** —que sin eso el resultado queda y el cómo se borra—. El porqué se movió al bloque del checklist, que es donde las demás reglas lo ponen. **Pasarse del molde suele ser el síntoma de eso, no un problema de longitud.**
- **Where:** `04·S18` en [base/04-seguridad.md](../base/04-seguridad.md), con su fila 10 corregida y el porqué debajo.
- **Learned:** **el checklist de una regla se llena corriendo el validador, no leyendo la regla** — y menos si lo llena quien acaba de escribirla. La comprobación cuesta un comando. Y hay una señal barata de que un checklist es de intenciones: **si sus veinte filas dan ✅ a la primera**, alguien lo dedujo en vez de medirlo.
- **When/Who:** 2026-08-27 · agente, al mirar por qué la columna «falla hoy» de `vigencia.py` estaba vacía.
- **Scope:** estándar; aplica a toda regla nueva y a todo checklist que se firme sobre trabajo propio.
- **Rel:** S-062 (tres formas de que una prueba mienta en verde), S-069 (recomendar sin leer el criterio).

## S-071 · Un archivo que ninguna sesión registró no parece ajeno: parece de nadie  ·  error-resuelto · activa
- **What:** un commit se llevó **712 líneas de trabajo ajeno** —dos moldes de manual y su entrada del registro de cambios— barridas por un `git add -A`. El commit trataba de otra cosa y **no las nombra en su mensaje**. Se descubrió dos commits después, y no por una comprobación: **el número de versión no cuadraba**. Se había escrito `35.6.0` en `VERSION` y lo guardado decía `35.7.0`.
- **Why:** la comprobación que existe para esto —*«el commit no se lleva lo ajeno»*— **corrió y dijo OK**. Pregunta si lo que entra al commit **lo tocaron dos sesiones distintas**, y los archivos ajenos **no los había registrado ninguna**. Un archivo sin registro no se ve como de otro: se ve como de nadie, y la comprobación solo se dispara cuando dos registros chocan.
- **Also:** las tres formas de quedar sin registro son normales, no excepciones. **La sesión que lo escribió cerró hace más de doce horas** y su registro caducó a propósito; **se escribió antes de que el enganche existiera**; o **se escribió por fuera de las herramientas que el enganche ve** — una redirección dentro de un comando no deja rastro.
- **And:** la señal que sí estaba a la vista era el propio archivo. **`VERSION` cambió de contenido bajo la mano de quien lo editaba**: se escribió un número y se guardó otro. Nadie lo miró porque al revisar el commit se contaron los archivos —«43»— **sin mirar cuáles**.
- **Where:** el commit `6abffdc`, y la constancia puesta en la entrada `35.7.0` del [CHANGELOG](../CHANGELOG.md) para que el registro no siga atribuyendo mal.
- **Learned:** **una comprobación que compara dos fuentes solo ve lo que ambas conocen.** Cuando una de las dos puede estar vacía —por caducidad, por antigüedad o por no cubrir todos los caminos—, su silencio significa «no lo sé», y se está leyendo como «está bien». La pregunta que lo destapa: **¿qué pasa si el registro no tiene nada de este archivo?** Y la otra mitad, más barata: **antes de aprobar un commit, mirar los nombres de los archivos, no cuántos son.**
- **When/Who:** 2026-08-28 · agente y usuario, al no cuadrar el número de versión de un cambio de una línea.
- **Scope:** estándar; aplica a toda comprobación que cruce lo que entra a un commit con un registro que puede estar incompleto.
- **Rel:** S-068 (un sabotaje que no se pudo aplicar no es uno que pasó), S-062 (tres formas de que una prueba mienta en verde).

## S-072 · El hueco por el que entró lo ajeno es el mismo por el que pasa casi todo lo propio  ·  decisión · activa
- **What:** para que la comprobación de sesiones viera los archivos que **ninguna sesión registró** —por ahí entraron 712 líneas ajenas— se propuso avisar de ellos cuando al menos uno de los que entran al commit sí tuviera registro. **Medido sobre los últimos doce commits: avisaría en siete, con hasta 31 archivos de una vez.** Eso no es una comprobación, es ruido — y un aviso que se aprende a ignorar apaga también lo que sí importaba.
- **Why:** el registro se llena desde las herramientas de escritura del agente, y **la mayoría de los archivos se escriben desde guiones que se corren en la terminal**, que el enganche no ve. Así que *«sin registro»* no significa *«de otro»*: significa *«escrito de la forma habitual»*. **El hueco por el que entró lo ajeno es el mismo por el que pasa casi todo lo propio**, y con ese registro no hay forma de separarlos.
- **Also:** la medición mató el diseño obvio antes de escribirlo, que es exactamente para lo que sirve medir. La idea se veía razonable y estaba bien argumentada; **lo único que la descartó fue correrla contra el historial real**. Sin ese paso se habría construido, habría avisado siete de doce veces, y se habría apagado.
- **And:** eso reencuadra el problema. No es que la comprobación esté mal escrita: es que **su fuente de datos no cubre cómo se trabaja de verdad**. Arreglar la comprobación sin arreglar el registro sería afinar un instrumento que mide otra cosa — el defecto que este repositorio ya cometió cuatro veces con el número de avance.
- **Where:** la medición, en [historico-chat/scripts/2026-08-28/](../historico-chat/scripts/2026-08-28/) · `validar_preparados` en `validadores/sesiones.py`.
- **Learned:** antes de afinar una comprobación que calla, **hay que preguntar por qué calla** — y si la respuesta es que su registro está incompleto, el trabajo no está en la comprobación sino en el registro. La prueba barata: **correr la regla nueva contra el historial y contar cuántas veces habría hablado.** Si habla en más de la mitad de los casos, no distingue nada.
- **When/Who:** 2026-08-28 · agente y usuario, midiendo antes de construir el arreglo obvio.
- **Scope:** estándar; aplica a toda comprobación que se apoye en un registro que el agente llena mientras trabaja.
- **Rel:** S-071 (un archivo que ninguna sesión registró parece de nadie), S-059 (una medida que separó bien cuatro casos no separa bien seiscientos).

## S-073 · Una clase de pruebas en verde no dice nada sobre las de al lado  ·  error-resuelto · activa
- **What:** al agregar una aserción a la prueba de un enganche, la búsqueda del texto a reemplazar coincidió **primero con la prueba de otro enganche**, y ahí quedó pegada — usando una variable que en esa clase ni existe. Corrí la clase nueva sola, en verde, y seguí. La suite completa habría reventado con un `NameError`.
- **Why:** para ahorrar los tres minutos de la suite entera, corrí solo la clase que estaba escribiendo. **Es exactamente donde el error no estaba.** Un cambio hecho por reemplazo de texto no cae necesariamente donde se cree: cae en la primera coincidencia.
- **Also:** lo destapó un sabotaje que *«se coló»* sin razón aparente. Al perseguir por qué no lo cazaban las pruebas, apareció el verdadero desorden. **El sabotaje encontró un defecto distinto del que buscaba.**
- **And:** la clase sola tardaba 5 segundos; la suite, 185. Esa proporción es la que empuja a saltarse la suite, y **es la misma que hace que el error tarde en aparecer**.
- **Where:** `validadores/pruebas.py`, entre `ElAgenteNoEscribeFuera` y `ElTurnoAnotaLoQueCambio`.
- **Learned:** **un reemplazo de texto se verifica mirando dónde cayó, no mirando si el archivo compila.** Y antes de dar una fase por terminada, la suite completa corre entera aunque tarde: el verde de una clase es una afirmación sobre esa clase y nada más.
- **When/Who:** 2026-08-28 · agente, depurando por qué un sabotaje no se cazaba.
- **Scope:** estándar; aplica a todo cambio hecho por búsqueda y reemplazo sobre un archivo grande.
- **Rel:** S-062 (tres formas de que una prueba mienta en verde), S-068 (un sabotaje que no se pudo aplicar no es uno que pasó).

## S-074 · Un sabotaje que se cuela sin razón aparente suele señalar código muerto  ·  aprendizaje · activa
- **What:** rompí a propósito la línea que ponía la hora del registro —`os.utime(ruta, None)`— esperando que las pruebas lo cazaran. **No lo cazaron, y tenían razón:** el archivo se acababa de crear en el renglón anterior, así que ya traía la hora de ahora. La línea no hacía nada.
- **Why:** se escribió por costumbre, para «asegurar» un estado que la operación anterior ya garantizaba. Ninguna prueba podía distinguir el antes del después, porque **no había diferencia que distinguir**.
- **Also:** la reacción instintiva fue la equivocada: agregar una prueba que cazara ese sabotaje. Habría sido una prueba de una línea inútil, y **el código muerto habría quedado con una prueba encima que lo hace parecer necesario**.
- **And:** el otro sabotaje que se coló en la misma tanda sí era un defecto de verdad —el enganche creaba carpetas fuera de todo proyecto—, así que la tanda separó dos cosas distintas con la misma señal: **una prueba que falta, y una línea que sobra.**
- **Where:** `anotar_el_turno` en `validadores/sesiones.py`, fase `A-EP-005-HU-020`.
- **Learned:** cuando un sabotaje se cuela, hay dos preguntas y en este orden: **¿falta una prueba, o sobra el código?** Si nadie puede observar la diferencia entre romper la línea y dejarla, la línea no está haciendo nada. Se quita, y el sabotaje se apunta al renglón que sí decide.
- **When/Who:** 2026-08-28 · agente, corriendo la tanda de sabotajes de la fase.
- **Scope:** estándar; aplica a toda revisión por sabotaje.
- **Rel:** S-073 (una clase en verde no dice nada sobre las de al lado), S-062 (tres formas de que una prueba mienta en verde).

## S-075 · Cuatro registros llevados a mano se quedaron atrás, y ninguno avisó  ·  error-resuelto · activa
- **What:** en una sola jornada aparecieron **cuatro listas que alguien mantiene a mano y que estaban desactualizadas**: el índice de la épica `EP-005` (cuatro historias atrás), el mapa del amarre a la herramienta (siete archivos), el mapa del sitio (dos carpetas) y la lista de exentos del detector de secretos (dos archivos). Ninguna se descubrió trabajando: las cuatro las destapó correr los comprobadores.
- **Why:** los cuatro son **el segundo sitio**. El primero —la carpeta de la historia, el archivo del validador, la carpeta nueva, la prueba nueva— se crea al trabajar y no se puede olvidar, porque es el trabajo. El segundo se edita en otro rato, y nada obliga a volver. **La pregunta que lo destapa: ¿qué archivo hay que tocar después, en otro momento, para que esto quede completo?**
- **Also:** la de exentos es la más cara de las cuatro, y muestra el costo real. Dejó `validar.py todo` **en rojo seis días**, y el rojo era «posible secreto en el código» — el mismo mensaje que daría una credencial de verdad. **Un control que lleva días en rojo por una lista vieja ya no distingue lo nuevo**, que es exactamente lo que el pendiente que creó esa lista había advertido, con esas palabras, diez días antes.
- **And:** tres de las cuatro **sí tienen comprobador** —`amarre`, `sitio`, `secretos` los ven— y aun así estuvieron rotas días. **Tener el comprobador no alcanza si nadie lo corre entre commit y commit.** El cuarto, el índice de la épica, ni comprobador tiene: se vio porque el molde de cierre pide marcar una casilla y esta vez se miró antes de firmarla.
- **Where:** `validadores/secretos.py` (`EXENTOS`) · `anatomia/mapa-del-sitio.md` · `anatomia/que-esta-amarrado-a-la-herramienta.md` · el `README.md` de `EP-005`.
- **Learned:** **un registro llevado a mano no se mantiene solo por tener un comprobador; se mantiene si el comprobador corre.** Automatizarlo tampoco sirve cuando el registro es una *decisión* —cuáles pruebas pueden traer algo con forma de clave lo decide una persona, y una lista que se llena sola sería el agujero—. Lo que falta no es la lista ni el comprobador: es **que la corrida completa sea parte de cerrar, no algo que se recuerda**.
- **When/Who:** 2026-08-28 · agente, al correr todos los comprobadores antes de cerrar una fase.
- **Scope:** estándar; aplica a todo dato que se escriba en dos sitios que se editan en momentos distintos.
- **Rel:** S-070 (un checklist que uno firma sobre su propio trabajo no comprueba nada), S-064 (una historia se crea y nadie vuelve a la tabla de su épica), S-057 (la regla se fijó y se dejó de cumplir al día siguiente).

## S-076 · El sello de «commit autorizado» no distingue el commit que cierra una fase del que la abre  ·  error-resuelto · activa
- **What:** el enganche de `post-commit` selló la estación 12 —«Commit · 👤 autorizado»— de una fase **recién creada**, con el hash del commit que la estaba creando. La fase iba por la estación 7 y su documento decía que ya había pasado la 12.
- **Why:** el enganche marca **toda fase cuya carpeta toque el commit**, y esa condición no separa los dos casos: el commit que guarda una fase terminada toca su carpeta, y el que la abre también. Es la misma forma de error que `S-071` —una condición que parece discriminar y en realidad cubre los dos lados— con otro disfraz.
- **Also:** el daño es de los caros porque **es silencioso y afirma de más**. Un documento de fase que dice «commit autorizado» sin que nadie lo autorizara es exactamente lo que el estándar existe para impedir, y quien lo lea después no tiene cómo saber que lo escribió un programa.
- **And:** se vio **en la misma vuelta en que ocurrió**, porque el enganche imprime lo que hizo. Si callara —que es la tentación de todo automatismo que «no molesta»— el sello falso se habría quedado. **Un automatismo que escribe tiene que decir qué escribió**, aunque nadie se lo pregunte.
- **Where:** `validadores/hook_estacion.py` y `validadores/estacion_commit.py`, de la fase `A-EP-005-HU-019` · la fila corregida a mano en el `estado-fase.md` de `A-EP-005-HU-021`.
- **Learned:** cuando un automatismo marca un hito, la pregunta no es «¿tocó esto el commit?» sino **«¿este commit es el hito?»**. Lo que distingue los dos casos acá está a la vista y no se está mirando: una fase que se cierra trae su `resultado_pruebas.md` lleno y su veredicto escrito; una que se abre trae los moldes en blanco.
- **When/Who:** 2026-08-28 · agente, al leer lo que el enganche imprimió después de guardar.
- **Scope:** estándar; aplica a todo automatismo que selle un hito a partir de qué archivos cambiaron.
- **Rel:** S-071 (un archivo que ninguna sesión registró parece de nadie), S-075 (cuatro registros llevados a mano se quedaron atrás).

## S-077 · Un aviso que dice «nunca» sobre algo que pasó dos veces manda a repetir trabajo inútil  ·  error-resuelto · activa
- **What:** el reclamo de las pruebas del estándar corrió por primera vez de verdad —en un `push`— y dijo: *«las pruebas del estándar nunca corrieron en esta copia»*. **Habían corrido dos veces ese mismo día.** Lo que pasaba es que el sello solo se escribía cuando la corrida quedaba **limpia**, y la carpeta tiene ocho fallas conocidas.
- **Why:** el programa confundía dos cosas distintas: **«no hay constancia» y «no corrió»**. Son la misma ausencia de archivo y llevan a acciones opuestas. Con la primera lectura, el aviso manda a esperar diez minutos para volver a leer exactamente lo mismo — y **un aviso que manda a hacer algo que no cambia nada se aprende a ignorar en dos intentos.**
- **Also:** el defecto no lo encontró ninguna de las 22 pruebas de la fase, ni los once sabotajes: **lo encontró correrlo de verdad, una vez, en el momento en que sirve.** Las pruebas cubrían «sin sello reclama» y «con sello limpio calla», y el caso real —sello ausente *porque* hubo fallas— caía entre las dos.
- **And:** el arreglo dice **tres cosas distintas** en vez de una: nunca corrieron, la última dejó N fallas, o hay commits que no vieron. Y el sello guarda el conteo, así que un sello viejo sin él se lee como limpio: es lo único que aquella versión sabía escribir.
- **Where:** `validadores/corredor.py` · `sellar` y `reclamo`, fase `A-EP-005-HU-021`.
- **Learned:** **antes de escribir un mensaje que afirma algo, preguntar qué otra situación produce la misma señal.** Acá la señal era «no hay archivo» y el mensaje eligió una de sus tres causas, la menos probable. La prueba barata: leer el aviso en voz alta y preguntar **«¿qué hago con esto, y qué pasa si lo hago?»**. Si la respuesta es «lo mismo otra vez», el mensaje está mal.
- **When/Who:** 2026-08-28 · agente y usuario, en el primer push con el enganche puesto.
- **Scope:** estándar; aplica a todo aviso que se dispare por la **ausencia** de algo.
- **Rel:** S-071 (un archivo que ninguna sesión registró parece de nadie), S-075 (cuatro registros llevados a mano se quedaron atrás), S-068 (un sabotaje que no se pudo aplicar no es uno que pasó).

## S-078 · Un sabotaje que deja el archivo sin compilar no cazó nada  ·  error-resuelto · activa
- **What:** uno de los doce sabotajes se reportó como **CAZADO** y no había cazado nada: el texto que insertaba dejaba un paréntesis suelto, así que las pruebas fallaban con `SyntaxError`. **Fallaban por la sintaxis, no por el comportamiento.**
- **Why:** el guion juzga por el código de salida de `unittest`, y un archivo que no compila da el mismo código de salida que una prueba que atrapa un defecto. **La misma señal, dos causas, y la que interesa es la otra.**
- **Also:** es `S-068` con otra forma. Allá el sabotaje **no se aplicaba** —los acentos no calzaban— y el verde se leyó como que la prueba lo había atrapado. Acá sí se aplicó, y aun así lo que se midió fue el intérprete de Python.
- **And:** la corrección es de tres líneas y vale para siempre: si la salida trae `SyntaxError` o `IndentationError`, el resultado no es *cazado* ni *se coló*, sino **NO VALE** — y cuenta como fallo del guion, para que nadie lo lea como cobertura.
- **Where:** `historico-chat/scripts/2026-08-28/sabotajes-hu021.py`.
- **Learned:** **un sabotaje se juzga por lo que rompió, no por el color que sale.** Antes de dar uno por bueno hay que poder decir *qué comportamiento* dejó de cumplirse; si la respuesta es «no sé, pero falló», no probó nada. Las tres formas de mentir en verde que lleva esta casa son ya: no aplicarse, dejar el archivo sin compilar, y apuntar a una línea que no hace nada.
- **When/Who:** 2026-08-28 · agente, mirando la salida de la tanda en vez de solo su total.
- **Scope:** estándar; aplica a toda revisión por sabotaje.
- **Rel:** S-068 (un sabotaje que no se pudo aplicar no es uno que pasó), S-074 (un sabotaje que se cuela suele señalar código muerto), S-062 (tres formas de que una prueba mienta en verde).

## S-079 · El sello de una corrida se contaba como una conversación viva  ·  error-resuelto · activa
- **What:** el sello de la última corrida de pruebas se guardó en `historico-chat/.tocado/`, la carpeta del registro de sesiones. `sesiones.registros()` lee **todo** `.txt` de ahí como el registro de una conversación, así que el sello apareció como **una sesión viva llamada «internas» con dos archivos** — que en realidad eran una fecha y un número.
- **Why:** las dos cosas son «estado de trabajo de esta máquina que no se versiona», y esa semejanza bastó para meterlas en el mismo cajón. Pero **el cajón tiene un lector que asume que todo lo que hay dentro es del mismo tipo**, y ese lector alimenta la comprobación que evita que un commit se lleve trabajo ajeno.
- **Also:** el daño era pequeño y silencioso: infla el número de sesiones que el aviso reporta. Se volvía grave el día que dos conversaciones sí chocaran y el mensaje dijera «3 sesiones» contando una que no existe.
- **And:** **apareció al ir a comprobar otra cosa.** El usuario preguntó si el defecto del commit que se llevó 712 líneas ya estaba cerrado; al medirlo —listando las sesiones vivas para responder con datos y no de memoria— salió una sesión de más. **Verificar una afirmación destapó un defecto que nadie buscaba.**
- **Where:** `validadores/corredor.py` · `SELLO`, ahora en `historico-chat/.estado/`.
- **Learned:** **antes de guardar algo junto a otra cosa, preguntar quién lee esa carpeta y qué asume de lo que hay dentro.** «Es del mismo tipo de dato» no basta: lo que decide es si algún programa recorre el sitio entero. Y la prueba que lo fija no mira el archivo del sello: mira que **el registro de sesiones siga vacío** después de sellar.
- **When/Who:** 2026-08-28 · agente y usuario, al pedir la comprobación de si un defecto anterior estaba cerrado.
- **Scope:** estándar; aplica a toda carpeta que un programa recorra entera.
- **Rel:** S-077 (un aviso que dice «nunca» sobre algo que pasó), S-075 (cuatro registros llevados a mano se quedaron atrás), S-071 (un archivo sin registro parece de nadie).

## S-080 · «Sí, con un límite» es un «cumple con observaciones» disfrazado  ·  error-resuelto · activa
- **What:** el usuario preguntó si un defecto ya estaba cerrado. Respondí **«sí, con un límite»**: el arreglo está construido, probado y publicado, pero **no se ha observado funcionando** porque el caso —dos conversaciones simultáneas chocando— no se ha dado desde que se instaló. El usuario cortó la respuesta: *«si hay un límite no es sí»*.
- **Why:** el límite no era un matiz sobre algo cumplido: **era la parte que falta.** Lo pedido es que la colisión se vea; lo que hay es una prueba con repositorios armados a mano. Poner eso bajo un «sí» hace que quien lea la respuesta deje de mirar, y **el trabajo que falta desaparece detrás de la palabra que lo aprueba.**
- **Also:** el estándar ya había peleado esto mismo y ganado. Hasta la versión 35.1.0 el molde de cierre ofrecía «Cumple / Cumple con observaciones» y **no tenía forma de decir «No cumple»**: las diecinueve fases que no cumplían tuvieron que escribirlo cada una a su manera, y ningún programa podía leerlo. **Volví a cometer en una respuesta de chat el defecto que el molde ya no permite en un documento.**
- **And:** los documentos de la fase sí lo decían bien \u2014 el `CP-006` declara el límite con su número y dice que el cero no prueba que las colisiones se vean\u2014. **El defecto no fue de análisis sino de redacción del veredicto**, que es donde menos se vigila porque «ya está escrito bien más abajo».
- **Where:** la respuesta al usuario · el molde `11-funcionalidad-implementada.md`, que desde la 35.1.0 solo admite Cumple / No cumple.
- **Learned:** **el veredicto se da con la misma regla en el chat que en el documento: si algo de lo pedido falta, es «no».** El detalle va después, y va completo — pero no dentro de la palabra que aprueba. La prueba barata: si la respuesta necesita un «pero», «con», «salvo» o «falta» para ser cierta, empieza por **no**.
- **When/Who:** 2026-08-28 · usuario, corrigiendo un «sí, con un límite».
- **Scope:** estándar; aplica a todo veredicto que el agente entregue, escrito o hablado (`00·ID8`).
- **Rel:** S-070 (un checklist que uno firma sobre su propio trabajo no comprueba nada), S-077 (un aviso que dice «nunca» sobre algo que pasó dos veces).

## S-081 · Veintiún documentos idénticos: el molde se aprueba una vez, y las cifras se miden una por una  ·  decisión · activa
- **What:** `EP-001` tiene una historia por cada capítulo de `base/`, y las veintiuna pedían lo mismo con distinto número. Cerrarlas exigía **105 documentos** de fase. Se hicieron dos cosas distintas con esa repetición: **el molde se aprobó una sola vez**, declarándolo en los dos planes, y **las cifras de cada documento las midió un programa capítulo por capítulo** en vez de copiarse.
- **Why:** son dos riesgos opuestos y los dos reales. Pedir veintiuna aprobaciones de un texto idéntico **convierte la puerta en trámite**, y una puerta que es trámite deja de mirar — el mismo mecanismo por el que se firma un checklist sin correrlo (`S-070`). Y copiar ciento cinco documentos **es la forma más segura de que uno diga algo falso sin que nadie lo note**, porque nadie relee el número veinte de una serie.
- **Also:** la medición pagó en el acto. El capítulo `16` salió con **cero reglas**, y no porque esté vacío: su encabezado usa una forma que el analizador no reconoce. Copiando cifras, ese documento habría dicho un número inventado; midiendo, dice el cero **con su explicación y su defecto abierto**, enrutado a la fase que existe para eso.
- **And:** lo que hace legítimo automatizar la escritura no es que ahorre tiempo, sino que **cada documento afirme solo sobre lo que se leyó** (`04·R4`). El programa lee el capítulo de cada uno: cuántas reglas tiene, de qué forma está en el disco, si su cabecera nombra la historia y si el enlace resuelve. **Y trae el criterio de suspensión adentro**: si el enlace no resolviera, esa fase no se escribe.
- **Where:** `historico-chat/scripts/2026-08-28/retrodocumentar-los-capitulos.py` · las 21 fases `A-EP-001-HU-0NN-retrodocumentar-el-capitulo-NN`.
- **Learned:** cuando hay que producir N documentos casi iguales, **la pregunta no es «cómo los escribo más rápido» sino «qué dato de cada uno es distinto, y quién lo mide»**. Si la respuesta es «ninguno», sobran los documentos; si hay datos distintos, los mide un programa y no la paciencia. Y la aprobación se pide **una vez sobre el molde**, diciéndolo, en vez de N veces sobre copias.
- **When/Who:** 2026-08-28 · agente y usuario, al cerrar las 21 historias de capítulo de `EP-001`.
- **Scope:** estándar; aplica a toda tanda de documentos que compartan estructura.
- **Rel:** S-070 (un checklist que uno firma sobre su propio trabajo no comprueba nada), S-075 (cuatro registros llevados a mano se quedaron atrás), S-064 (una historia se crea y nadie vuelve a la tabla de su épica).

## S-082 · El aviso disparó las tres veces y no cambió nada  ·  error-resuelto · activa
- **What:** el agente escribió tres guiones de apoyo en la carpeta temporal de la herramienta, fuera del repositorio, y los documentos de fase que esos guiones produjeron quedaron sin su evidencia. **El enganche que avisa de eso existe, está colgado y disparó las tres veces**: se comprobó corriéndolo, `hook_rutas.py` imprime el aviso y nombra el destino correcto.
- **Why:** la regla es `04·S18` y salió del [pendiente 89](../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md), que se cerró seis días antes por exactamente esto. **No faltaba el control: el control habló y no cambió nada.** El enganche sale con código 0, así que avisa y sigue.
- **Also:** lo notó el usuario, no el agente ni el enganche. La causa no fue una duda sobre dónde va el guion: fue tomar el camino que no fallaba, porque el heredoc de la terminal se rompía con las comillas.
- **And:** el contraste está dentro de la misma sesión. El enganche del commit **sí detiene**, con código 2, y rechazó un commit por dos puntos suspensivos de un solo carácter. Ese se notó en el acto y se corrigió en el acto.
- **Where:** `adaptadores/claude-code/hook_rutas.py` · `historico-chat/scripts/2026-08-30/` · el `H-7` del resumen de la sesión.
- **Learned:** un aviso con código 0 sobre una regla **que ya se dejó de cumplir dos veces** no es un control, es una nota al pie. Lo que distingue a los dos enganches de esta sesión no es qué comprueban: es si detienen. Antes de dar por cubierta una regla con un aviso, vale preguntar cuántas veces se ha incumplido con el aviso puesto.
- **When/Who:** 2026-08-30 · el usuario lo vio y preguntó por qué el agente escribía afuera.
- **Scope:** estándar; aplica a toda regla que hoy se sostiene solo con un aviso.
- **Rel:** S-057 (los guiones de apoyo se borraban con el temporal), S-070 (un checklist que uno firma sobre su propio trabajo no comprueba nada).

## S-083 · Un cero que salía de no mirar se publicó como «limpio»  ·  error-resuelto · activa
- **What:** el agente corrió `validar.py marcas` sobre veinticinco documentos nuevos, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de esos archivos. El enganche del commit, que lee lo que entra al índice, encontró **trece avisos en esos mismos archivos**.
- **Why:** el subcomando solo recorre `base/` y `plantillas/`. Sobre `documentacion/` devuelve cero **porque no mira**, no porque esté limpio, y la salida no distingue una cosa de la otra.
- **Also:** el mismo programa tiene el otro filo, más viejo: cuenta las secciones 2 y 3 del anexo de marcadores y las de la 4 en adelante piden lectura. Su «0 en 0 archivos» tampoco lo dice.
- **And:** la afirmación falsa quedó publicada y hubo que corregirla en el commit siguiente. El commit no se enmendó porque el enganche `post-commit` ya había escrito su hash dentro de los documentos de fase.
- **Where:** [pendiente 91](../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md) · `validadores/marcas.py` · commits `b7b8fc0` y `870ef69`.
- **Learned:** antes de citar un cero como evidencia, hay que saber **sobre qué corrió el programa**. Un validador que no dice qué recorrió no entrega un veredicto: entrega un número que el lector completa con lo que quiere creer.
- **When/Who:** 2026-08-30 · agente, al cerrar cinco veredictos en rojo.
- **Scope:** estándar; aplica a toda salida de validador que se cite en un documento o en un commit.
- **Rel:** S-081 (las cifras de cada documento las mide un programa), S-061 (nadie vuelve a mirar un veredicto en rojo).

## S-084 · Una prueba que exige lo que la casa decidió no cumplir no mide nada  ·  decisión · activa
- **What:** la versión `15.4.0` aparece dos veces en el registro porque dos sesiones numeraron a la vez. El registro decidió el 2026-08-15 **no renumerar**, con el motivo escrito: un proyecto pudo haber adoptado ese número. La prueba del criterio seguía exigiendo unicidad, y llevaba ocho días marcada como fallo esperado.
- **Why:** el veredicto de la historia quedaba en rojo por una exigencia que nadie pensaba cumplir. **Un fallo esperado permanente enseña a mirar los fallos esperados como paisaje**, y entonces el que aparezca de verdad tampoco se mira.
- **Also:** la salida no fue aflojar la prueba. Pasó a exigir lo que sí se sostiene, que la repetición esté declarada con sus dos entradas a la vista, y se le agregó la contraprueba: un número repetido **sin** declarar sí falla. Sin esa segunda mitad, aceptar el declarado era aceptar cualquiera.
- **And:** el `CHANGELOG.md` no se tocó. Lo que estaba mal no era el dato: era la exigencia.
- **Where:** `validadores/pruebas.py`, clase `NumeroDeVersion` · la fase `B-EP-002-HU-001-el-numero-repetido-se-declara`.
- **Learned:** cuando una prueba lleva días en fallo esperado, la primera pregunta no es cómo arreglarla sino **si lo que exige sigue siendo lo que la casa quiere**. A veces el rojo no señala trabajo pendiente: señala una decisión que se tomó y que nadie bajó a la prueba.
- **When/Who:** 2026-08-30 · usuario decide la lectura del criterio, agente la implementa.
- **Scope:** estándar; aplica a toda prueba marcada como fallo esperado por más de una sesión.
- **Rel:** S-065 (un rojo entraba en la cuenta y no salía nunca), S-061 (nadie vuelve a mirar un veredicto en rojo).

## S-085 · «Ocho historias en rojo» eran dos cosas distintas  ·  aprendizaje · activa
- **What:** ocho historias terminadas arrastraban un «No cumple» y ninguna tenía fase posterior. Medidas una por una, tres eran trabajo y se hicieron; **las otras cinco no son trabajo: son decisiones del usuario**, y cuatro de ellas ya estaban escritas como tales dentro del propio repositorio.
- **Why:** «ocho en rojo» se lee como ocho tareas, y confundirlas lleva a lo peor de los dos lados: o el agente decide por su cuenta lo que no le toca (`01·C4`), o el trabajo que sí está hecho se queda sin declarar.
- **Also:** el repositorio lo tenía dicho y nadie lo estaba leyendo. La prueba de `EP-006·HU-006` lo escribe textual: *«las dos salidas son malas y elegir entre ellas no es del que ejecuta... queda como fallo esperado y como pregunta al usuario, no como parche»*.
- **And:** la partición sale de **ejecutar el criterio**, no de leer el documento de la fase. Dos de los tres que resultaron ser trabajo estaban en rojo por razones honestas que ya no eran ciertas o que nunca se habían podido provocar.
- **Where:** `historico-chat/scripts/2026-08-30/` · las fases `B` de `EP-001·HU-006`, `EP-002·HU-001` y `EP-007·HU-002`.
- **Learned:** antes de estimar una lista de rojos, medirla. La pregunta que la parte en dos es **«¿esto se cierra construyendo, o se cierra decidiendo?»**, y la respuesta cambia quién tiene que hacer el siguiente movimiento.
- **When/Who:** 2026-08-30 · el usuario pidió terminar las ocho.
- **Scope:** estándar; aplica a cualquier lote de veredictos en rojo.
- **Rel:** S-081 (el molde se aprueba una vez y las cifras se miden), S-061 (nadie vuelve a mirar un rojo).

## S-086 · Un reclamo que sale siempre es el que se aprende a ignorar  ·  error-resuelto · activa
- **What:** el reclamo de que una entidad inmutable no tiene su permiso salía en **todo proyecto con una entidad inmutable**, desde hacía meses. El patrón se declara como `anular_<recurso>` y la expresión se arma reemplazando el marcador **sobre el texto ya escapado**: hasta Python 3.6 `re.escape` escapaba los ángulos y el reemplazo encajaba; desde 3.7 no. La expresión quedaba literal y no encontraba ningún permiso.
- **Why:** el daño no es el falso positivo: es **lo que le enseña al que lo lee**. Un veredicto que sale siempre deja de leerse, y con él dejan de leerse los que sí eran ciertos. Es el mismo mecanismo por el que un enganche que estorba se apaga en una tarde.
- **Also:** se rompió **en silencio y sin tocar el código**. Nadie editó esa línea: cambió lo que hacía una función de la biblioteca estándar por debajo. Una prueba lo habría cazado el día del cambio de versión, y no la había.
- **And:** apareció al **provocar** el criterio en un proyecto de prueba, no al leerlo. Los cinco criterios de esa historia llevaban trece días sin ejecutarse, y el defecto llevaba meses.
- **Where:** `validadores/entidades.py`, `recursos_con_permiso` · la fase `A-EP-004-HU-010-declaracion-y-comprobacion`.
- **Learned:** cuando un reemplazo depende de **cómo quedó** un texto después de pasar por otra función, se busca lo mismo que se transformó (`re.escape("<recurso>")`) en vez de escribir a mano el resultado esperado. Y todo validador merece la pregunta: **¿este reclamo puede salir siempre?** Si puede, hay que probar el caso en que no debe salir.
- **When/Who:** 2026-08-30 · agente, al ejecutar los cinco criterios de `EP-004·HU-010`.
- **Scope:** estándar; aplica a toda comprobación que arme una expresión desde un patrón declarado.
- **Rel:** S-083 (un cero que salía de no mirar se publicó como limpio), S-082 (el aviso disparó y no cambió nada).

## S-087 · Un caso mal armado se lee igual que un programa roto  ·  aprendizaje · activa
- **What:** al provocar los criterios de `EP-004·HU-010`, las dos primeras vueltas dieron «no cumple» y el programa tenía razón: la declaración de prueba nombraba los estados por el **nombre de la columna** cuando se buscan como **valores entre comillas**, y el patrón del permiso iba **sin su marcador**. El proyecto de prueba tampoco era un repositorio, y las comprobaciones solo miran lo versionado.
- **Why:** el resultado se lee idéntico en los dos casos: «el programa no reporta lo que debería». Acusar al programa cuando el caso está mal armado lleva a «arreglar» lo que funcionaba, y eso sí rompe.
- **Also:** la tercera vuelta sí encontró un defecto de verdad (`S-086`). Las tres se distinguen por lo mismo: **mirar qué espera el programa antes de acusarlo**.
- **And:** que el proyecto de prueba no fuera un repositorio no dio error: dio **cero hallazgos**, que se lee como «todo bien». El silencio otra vez.
- **Where:** `historico-chat/scripts/2026-08-30/provocar-los-ca-de-hu010.py`.
- **Learned:** antes de reportar que una comprobación no reporta, hay que leer **qué busca exactamente**: qué formato, en qué archivos y bajo qué condición. Y el caso de prueba se arma con las mismas exigencias que el real, incluida la de estar versionado.
- **When/Who:** 2026-08-30 · agente.
- **Scope:** estándar; aplica a toda provocación de un criterio en un proyecto de prueba.
- **Rel:** S-086 (el reclamo que salía siempre), S-081 (las cifras las mide un programa).

## S-088 · El fallo esperado es la única nota que reclama sola  ·  patrón · activa
- **What:** cinco fases anteriores encontraron defectos que **no podían arreglar**, porque su plan aprobado declaraba no tocar el programa. En vez de anotarlo en prosa, dejaron la prueba escrita y marcada como **fallo esperado**. Al arreglarlos el 2026-08-30, la corrida reportó «éxitos inesperados» y obligó a volver a destapar cada una.
- **Why:** un defecto anotado en un documento se pierde: nadie relee el §6 de una fase cerrada. Uno anotado como fallo esperado **reclama solo el día que deja de ser cierto**, y no hay forma de cerrarlo sin verlo.
- **Also:** funcionó cinco veces el mismo día, en dos archivos de pruebas distintos. Ninguna de las cinco se habría encontrado leyendo.
- **And:** tiene su límite, y conviene decirlo: un fallo esperado que se queda años deja de avisar y pasa a ser paisaje. Eso es lo que le pasó al de la versión repetida, que llevaba ocho días exigiendo algo que la casa ya había decidido no cumplir (`S-084`).
- **Where:** `validadores/pruebas.py` y `memoria/pruebas.py`, en las fases `B` cerradas el 2026-08-30.
- **Learned:** cuando `02·F8` impida arreglar lo que una fase encuentra, se deja **la prueba escrita y marcada**, no una nota. Y se revisa: un fallo esperado con más de una sesión encima es una decisión pendiente, no una tarea.
- **When/Who:** 2026-08-30 · agente y usuario, al ejecutar las cinco fases detenidas.
- **Scope:** estándar; aplica a todo defecto que una fase encuentra y no puede tocar.
- **Rel:** S-084 (una prueba que exige lo que se decidió no cumplir no mide nada), S-061 (nadie vuelve a mirar un rojo).

## S-089 · Cuatro reglas invisibles: el capítulo salía en verde porque nadie lo corregía  ·  error-resuelto · activa
- **What:** las cuatro reglas del capítulo de cumplimiento estaban escritas un nivel más abajo que las demás, porque el capítulo agrupa en partes. El analizador solo reconocía los dos niveles de arriba, así que **no existían para el programa**: ninguna de las veinte filas del checklist se les aplicó nunca. Ninguna traía su bloque de checklist y una no tenía su ejemplo.
- **Why:** el capítulo pasaba **por el mismo motivo por el que pasaría un examen que no se corrige**. Y no había forma de notarlo desde el resultado: cero incumplimientos se lee igual que cumplir.
- **Also:** ensanchar el analizador sin más creaba un defecto nuevo. Una sección del anexo de meta-reglas **nombra** a una regla que vive en su propio archivo, y pasó a contarse como una segunda definición: reclamaba un identificador repetido que no existe.
- **And:** lo que separa la regla de su eco es que **el identificador es único**: el que ya se definió arriba no puede ser otra definición. Y hay que mirarlo en una **pasada previa** sobre todo el árbol, porque en el orden de los archivos el eco se lee antes que la regla.
- **Where:** `validadores/metareglas.py`, `reglas()` · `base/16-cumplimiento-y-calidad.md` · la fase `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas`.
- **Learned:** cuando un analizador recorre por forma —el nivel de un título, la posición de una marca—, lo que no encaja **desaparece sin decir nada**. La pregunta que lo caza es «¿cuántas encontró?», no «¿cuántas fallaron?». Y al ensanchar el criterio hay que preguntar de inmediato qué **más** empieza a encajar.
- **When/Who:** 2026-08-30 · agente, con la decisión del usuario de corregir el capítulo en la misma fase.
- **Scope:** estándar; aplica a todo programa que reconozca documentos por su forma.
- **Rel:** S-081 (las cifras las mide un programa), S-083 (un cero que salía de no mirar).

## S-090 · Una norma escrita dentro de un documento modelo solo la hereda quien llene ese modelo  ·  aprendizaje · activa
- **What:** la exigencia de escribir en la lengua del proyecto, en tercera persona y con las acciones en infinitivo estaba escrita como **la regla once de dos manuales**. El usuario la pidió para un documento cualquiera y no hubo regla que citar. Subió al cuerpo de reglas como `00·ID10` el 2026-08-30, en la versión `37.0.0`.
- **Why:** un documento modelo se copia para llenarlo, y lo que dice adentro viaja con esa copia y con ninguna otra. Todo lo demás que el agente entrega quedaba sin la norma, y la convención se aplicaba **copiándola a mano** de una plantilla a otra: lo que se copia a mano se copia distinto.
- **Also:** el propio estándar ya lo tenía escrito y nadie lo había leído como una tarea. El anexo de marcas de generación automática decía en su cierre que la norma del idioma «necesita su propia regla, y todavía no existe».
- **And:** el alcance lo decidió el usuario, e incluye **lo que el agente contesta en el chat**. Es lo que más se lee y lo único que no queda versionado, así que es donde la convención se pierde primero: en esta misma sesión hubo que corregirla tres veces.
- **Where:** `base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md` · la fase `A-EP-001-HU-037`.
- **Learned:** cuando una exigencia aparece escrita dentro de un documento modelo, la pregunta es **quién más debería cumplirla**. Si la respuesta es «cualquiera que entregue algo», está en el sitio equivocado y se aplica por copia, que es la forma en que una norma se deforma sin que nadie lo decida.
- **When/Who:** 2026-08-30 · el usuario decidió el alcance; el agente escribió la regla.
- **Scope:** estándar; aplica a toda exigencia que hoy viva dentro de una plantilla.
- **Rel:** S-084 (una prueba que exige lo que se decidió no cumplir), S-089 (cuatro reglas invisibles).

## S-091 · La frase que describe lo que hace un programa se deriva, no se escribe  ·  patrón · activa
- **What:** el validador de marcas decía «0» sin decir sobre qué había corrido, y ese cero se publicó en un commit como si dijera que veinticinco documentos estaban limpios. Al arreglarlo, la frase del alcance **se arma con lo que la corrida recorrió**: las carpetas salen de la misma constante que el recorrido usa, y el número de archivos lo cuenta la propia pasada.
- **Why:** una frase escrita aparte **envejece sin avisar**. El día que alguien amplíe el alcance y no la toque, el reporte empieza a mentir y nada se cae. Derivada, la prueba se cae en vez de dejar que mienta.
- **Also:** el número importa tanto como el nombre de la carpeta. «Se recorrió `base/`» es cierto también cuando no había un solo archivo, y ese es justamente el otro cero que se confundía.
- **And:** el mismo patrón resolvió un defecto distinto el mismo día. El patrón del permiso de anular se armaba reemplazando `<recurso>` sobre el texto ya escapado, con el resultado del escapado **escrito a mano**; cuando la biblioteca cambió, el reemplazo dejó de encajar y el reclamo salió en todos los proyectos (`S-086`). La cura fue la misma: buscar lo mismo que se transformó, sin suponer cómo quedó.
- **Where:** `validadores/marcas.py`, `alcance()` · `validadores/entidades.py`, `recursos_con_permiso` · `validadores/tests/test_el_validador_dice_sobre_que_corrio.py`.
- **Learned:** todo texto que describa lo que un programa hace —su alcance, su cobertura, su patrón— se **deriva de lo que el programa usa**. Escribirlo aparte crea dos verdades que empiezan iguales y se separan sin que nadie lo note.
- **When/Who:** 2026-08-30 · agente.
- **Scope:** estándar; aplica a toda salida que describa el propio recorrido de un programa.
- **Rel:** S-083 (un cero que salía de no mirar), S-086 (un reclamo que sale siempre).

## S-092 · Trece rojos, cinco fases detenidas y siete pruebas: casi nada era trabajo  ·  aprendizaje · activa
- **What:** la jornada empezó con 13 historias en rojo, 5 terminadas sin decir si cumplían, 5 fases detenidas y 7 pruebas del estándar en rojo. Al medirlas una por una: **cinco rojos ya no eran ciertos**, cinco eran decisiones del usuario, tres eran trabajo; las cinco mudas **sí decían su veredicto** y el programa no sabía leerlo; las cinco fases estaban escritas y esperando una firma; y de las siete pruebas, una era un defecto de la propia prueba y cinco eran de archivos de otra sesión.
- **Why:** treinta ítems se leen como treinta tareas, y **menos de un tercio lo era**. Tratarlos como deuda técnica lleva a estimar mal y, peor, a no preguntar lo que hay que preguntar: cinco de esos ítems llevaban entre ocho y trece días esperando una respuesta de dos frases.
- **Also:** lo que separa una cosa de la otra es siempre lo mismo: **ejecutar el criterio**, no leer el documento que lo describe. Los cinco rojos que ya no eran ciertos se vieron corriéndolos; los tres que sí eran trabajo, también.
- **And:** la cuenta terminó en 122 historias que cumplen, cero rojas y cero mudas. Lo que queda son cuatro historias de producto sin ninguna fase, que es la única deuda que de verdad era trabajo.
- **Where:** `historico-chat/scripts/2026-08-30/` · el resumen de la sesión `2026-08-28 · plantilla-manual-instalacion`.
- **Learned:** antes de estimar una lista de pendientes, medirla. Las preguntas que la parten son tres: **¿esto se cierra construyendo, decidiendo, o solo declarándolo?** Y una cuarta que aparece cuando hay varias sesiones a la vez: **¿es mío?**
- **When/Who:** 2026-08-30 · usuario y agente, en una sola jornada.
- **Scope:** estándar; aplica a toda revisión de una cuenta de pendientes.
- **Rel:** S-085 («ocho historias en rojo» eran dos cosas distintas), S-088 (el fallo esperado es la única nota que reclama sola).

## S-093 · Una regla escrita informa; un programa ejecuta, y el estándar no distinguía las dos  ·  aprendizaje · activa
- **What:** se contaron las 18 reglas vigentes del capítulo `00` y se buscó su identificador dentro de los programas y de los enganches. **Siete no aparecían en ninguno**, y de las once que sí, solo dos tenían una pieza que de verdad las ejecutara. **Catorce de dieciocho** dependían de que el agente se acordara, y ninguna lo decía.
- **Why:** el núcleo es lo que no se relaja, así que es justo donde una regla que solo está escrita se lee igual que una que manda. Quien la abre ve una exigencia; lo que hay detrás puede ser un programa que la rechaza o nada en absoluto, y hasta el 2026-08-31 no había forma de saber cuál de las dos.
- **Also:** «nombrarse en un programa» no es «hacerse cumplir». Once reglas se nombraban en algún archivo, casi siempre en un comentario que explicaba por qué esa comprobación existe. El paso que separa una cosa de la otra no lo da ningún guion: hay que leer la pieza y decidir si ejecuta la exigencia.
- **And:** el usuario cortó la salida fácil. Catorce reglas sin quién las ejecute daban catorce pendientes, y dijo *«no las deje como pendiente de una solución»*. Salió **una sola pieza** para las tres que sí son medibles (`ID8`, `ID9`, `ID10`) y, para las otras once, la declaración escrita de que la sostiene la puerta de aprobación, que ningún programa ve.
- **Where:** `validadores/ejecutable.py` · `base/20-meta-reglas/estructura-regla.md` sección 6 · la fase `A-EP-005-HU-012`.
- **Learned:** cuando una regla se escribe, la pregunta que falta casi siempre es **quién la ejecuta**. Las dos respuestas valen —una pieza, o nadie con su motivo—; la que no vale es callarse, porque entonces la regla que manda y la que solo está escrita se leen igual.
- **When/Who:** 2026-08-31 · el usuario decidió el alcance; el agente construyó.
- **Scope:** estándar; hoy solo el capítulo `00`, y se extiende si el caso aparece fuera.
- **Rel:** S-089 (cuatro reglas invisibles), S-090 (una norma escrita dentro de un documento modelo).

## S-094 · Una línea nueva dentro de una regla la miran cuatro comprobaciones, y ninguna sabía que existía  ·  patrón · activa
- **What:** al escribir en las dieciocho reglas del núcleo la línea que dice quién las hace cumplir, saltaron tres defectos de golpe: ocho reglas empezaron a **reprobar el largo del molde**, catorce **sellos del checklist se dieron por vencidos**, y tres declaraciones traían raya larga, que el trinquete del `pre-commit` habría rechazado. Ninguna regla había cambiado lo que exige.
- **Why:** el archivo de una regla lo leen a la vez el molde (`M5`, el largo del cuerpo), el sello (¿cambió el texto desde que se aplicó el checklist?), el contador de marcas de `00·ID8` y el validador nuevo. Las cuatro tenían su idea de dónde termina la regla, y **ninguna contemplaba una línea que fuera de la regla sin ser su cuerpo**.
- **Also:** los tres se arreglaron con el mismo argumento, que ya estaba escrito para otro caso: el sello responde por lo que la regla **exige**, y cambiar la tipografía no cambia ninguna respuesta del checklist. La declaración tampoco. Que el argumento ya existiera es la señal de que el defecto era de familia conocida.
- **And:** los tres se vieron **antes de commitear**, corriendo las comprobaciones sobre el trabajo a medio hacer. El de las rayas se contó comparando las marcas nuevas contra lo guardado, que es exactamente lo que el enganche iba a hacer al rechazar el commit.
- **Where:** `validadores/metareglas.py`, `_FUERA_DEL_CUERPO` y `_sin_declaracion` · la fase `A-EP-005-HU-012`.
- **Learned:** agregar una línea de molde a un documento que ya tiene comprobaciones cuesta más que escribirla: hay que preguntarse **quién más lee ese archivo**. Y la forma barata de averiguarlo es correr las comprobaciones sobre el cambio a medio hacer, no después del rechazo.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar; aplica a todo campo nuevo dentro de un documento que ya se valida.
- **Rel:** S-091 (la frase que describe lo que hace un programa se deriva), S-084 (una prueba que exige lo que se decidió no cumplir).

## S-095 · La comprobación de la frontera miraba un canal, y había dos  ·  patrón · activa
- **What:** al mover `hook_estacion.py` de `validadores/` al adaptador, la prueba que vigila la frontera dio rojo. Comparaba los enganches que hay contra los que el instalador conecta, y para eso leía **una sola tabla**: la de la herramienta. Ese enganche va por el otro canal, el `post-commit` de git, así que recién mudado parecía un archivo que nadie usa.
- **Why:** la pieza estaba mal puesta desde el día que nació y la prueba lo decía; lo que impedía arreglarlo era que **arreglarlo rompía otra prueba**. El defecto no era el archivo: era que la cuenta de lo conectado estaba incompleta, y nadie lo iba a ver hasta que alguien intentara la mudanza.
- **Also:** la lista ahora se **deriva de las mismas plantillas que el instalador escribe**, no de una escrita al lado. Es el patrón de `S-091` otra vez: dos verdades que empiezan iguales se separan sin que nadie lo note.
- **And:** al escribir los mensajes nuevos apareció un efecto lateral medible. Decir «lo corre el enganche `hook_rutas.py`» hizo que el contador del amarre leyera **dos programas agnósticos como amarrados a la herramienta**: busca la palabra dentro del texto y no distingue nombrar de ser. El recuento subió de 27 a 29, y por eso se vio. Se resolvió nombrando al corredor sin su archivo.
- **Where:** `validadores/instalar.py`, `enganches_enchufados()` · `validadores/tests/test_la_frontera_del_adaptador.py` · la fase `C-EP-005-HU-011`.
- **Learned:** cuando una prueba lleva meses en rojo y el arreglo obvio rompe otra, el defecto casi nunca está donde apunta la falla. Está en el criterio que la otra prueba da por supuesto.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar; aplica a toda comprobación que compare «lo que hay» contra «lo que se conecta».
- **Rel:** S-091 (la frase que describe lo que hace un programa se deriva), S-094 (una línea nueva la miran cuatro comprobaciones).

## S-096 · Dos reglas puestas se rompieron igual: lo nuevo no pasó por donde la regla vigila  ·  aprendizaje · activa
- **What:** dos criterios de la misma historia estaban cumplidos y dejaron de estarlo. Ningún programa termina en silencio: dos nacidos después no lo cumplían. La corrida termina con un resumen único: un bloque agregado después quedó **debajo** de ese resumen. Las dos pruebas lo decían desde entonces.
- **Why:** una regla escrita se cumple el día que se escribe y se rompe el día siguiente, cuando alguien agrega algo por un camino donde la regla no vigila. La prueba existía, pasaba a rojo, y **nadie la corría**: es la misma raíz que hizo falta cerrar en `EP-005·HU-021`, cuando 650 pruebas escritas no las ejecutaba ningún comando.
- **Also:** el arreglo obligó a **ampliar la comprobación que reportaba el defecto**, y ahí está el riesgo: es la forma más fácil de hacer desaparecer un rojo sin arreglar nada. Se cubrió con sabotaje — un módulo de mentiras que no imprime nada y sale con 0, escrito y borrado por la propia prueba, para comprobar que el silencio se sigue cazando.
- **And:** lo que se amplió no fue cuánto silencio se acepta, sino **qué cuenta como decir por dónde se corre**. Dos programas no cuelgan del validador: los llama un enganche, y exigirles que nombraran `validar.py` era obligarlos a mandar al lector a un subcomando que no existe.
- **Where:** `validadores/comun.py`, `no_es_punto_de_entrada` · `validadores/validar.py`, `cmd_todo` · la fase `D-EP-004-HU-008`.
- **Learned:** al ampliar una comprobación para que deje de reportar algo, **sabotearla en la misma vuelta**. Si el caso original sigue cazándose, la ampliación era correcta; si no, lo que se hizo fue apagar el reporte.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar; aplica a todo cambio sobre una prueba que está reportando en rojo.
- **Rel:** S-093 (una regla escrita informa; un programa ejecuta), S-075 (tres registros con comprobador y rotos días igual).

## S-097 · La batería de la plataforma no la corre nadie, y una subida de versión la puso en rojo  ·  aprendizaje · activa
- **What:** al abrir la primera fase de la plataforma en once días, dos de sus 187 pruebas estaban en rojo. **No por esa fase:** su proyecto de mentiras declaraba la versión del estándar escrita a mano, y esa misma mañana el estándar había subido de `37.0.0` a `37.1.0`. Las dos pruebas daban por supuesto que el proyecto estaba al día, y dejó de ser cierto.
- **Why:** `validar.py internas` corre las pruebas de `validadores/tests/` y **ninguna de las 187 de `plataforma/`**. Así que el rojo estuvo puesto desde la mañana y se supo por la tarde, y solo porque hubo que tocar la plataforma. El estándar tiene una historia entera sobre esto —que las pruebas que existen se corran— y la plataforma quedó fuera de su alcance sin que nadie lo notara.
- **Also:** el defecto de las dos pruebas es el mismo patrón de siempre: **un número escrito a mano al lado de otro que se mueve**. La cura fue la de siempre: leerlo de donde vive. Ahora el proyecto de mentiras declara la versión que el estándar publica, y la prueba no se cae la próxima vez que suba.
- **And:** lo que lo destapó fue correr la batería entera **antes** de dar la fase por buena, no después. Si esta fase solo hubiera corrido sus propias pruebas —que era lo que `02·F5` permite— el rojo seguiría puesto.
- **Where:** `plataforma/nucleo/proyectos/tests.py`, `version_al_dia()` · la fase `A-EP-011-HU-001`.
- **Learned:** cuando un repositorio guarda dos productos con dos baterías, la que no corre el comando de todos los días **se pudre sin avisar**. Y una prueba que escribe a mano un número que otro programa mueve tiene fecha de caducidad desde que se escribe.
- **When/Who:** 2026-08-31 · agente.
- **Scope:** estándar y plataforma; aplica a toda suite que no cuelgue de la corrida diaria.
- **Rel:** S-091 (la frase que describe lo que hace un programa se deriva), S-096 (lo nuevo no pasó por donde la regla vigila).
