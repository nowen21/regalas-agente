# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-sesion-2.md](../../2026-08-22-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo.

---

## Hallazgos de esta sesión

### H-1 · El encuadre del planteamiento de Cimiento se llenó con procedencia en vez de con instrucción de uso

- **Qué pasó:** [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md) ocupa el renglón «Encuadre» del molde con fecha de redacción, fuentes, una cita del usuario y el número del pendiente que cierra, en lugar de lo que el molde pone ahí ([`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md)): la ruta del flujo y el «no generar código hasta que el plan esté aprobado».
- **Por qué importa:** el encuadre es lo primero que lee un agente en frío y es lo único que le dice que ese documento es **insumo y no orden**. Sustituido por procedencia, el archivo queda sin la barrera que evita que alguien lo lea como encargo y arranque a codificar. Además, tres de sus cuatro datos ya están repetidos en §0 y §2.
- **Qué lo soluciona:**
  **Reescribir el encuadre con dos párrafos:** el del molde (qué es el documento y qué no autoriza) y uno propio de este archivo (se escribió con el proyecto ya andando, así que su uso es medir contra él lo que se le proponga a Cimiento). La procedencia baja a un renglón «Cómo se levantó» en la tabla de §0; «cierra el pendiente 56» se va al `CHANGELOG.md` y al estado de la fase.
- **Qué se decidió:** el encuadre comunica **cómo se usa el documento**, no de dónde salió. Y el usuario amplió el criterio: el planteamiento **se redacta como si el proyecto fuera a empezar ahora**, tomando lo construido solo como materia prima. Nada de «se escribió hacia atrás», «hoy 14 de 14» ni identificadores de señales y pendientes ya cerrados: eso es descripción de lo hecho, no planteamiento de lo que se necesita.
- **Estado:** resuelto acá, y el molde también: la fase C quedó ejecutada el mismo día
- **Responde a:** — (salió de revisar el entregable del pendiente 56, no de un criterio planeado)
- **Dispara:** —
- **Orden de resolución:** 1 de 2 · es el archivo concreto; H-2 generaliza lo que acá se ve.
- **Dónde queda:** [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md). No se parchó: el usuario pidió borrarlo y escribirlo de nuevo desde las fuentes (README, `prompts/`, notas, inventario), para que la reconstrucción no arrastrara la voz descriptiva del texto anterior.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** 2026-08-22 · encuadre del planteamiento
- **Con qué se retoma:** —

### H-2 · Nada impide que un planteamiento llenado pise el encuadre del molde

- **Qué pasó:** el molde marca su recuadro de instrucciones con «borrar este recuadro», pero el renglón «Encuadre para el agente» queda fuera de ese recuadro y sin decir que **no se sustituye**. H-1 es la consecuencia: un planteamiento real lo reemplazó por otra cosa y ningún validador lo notó.
- **Por qué importa:** si el encuadre se puede pisar, cualquier planteamiento heredado puede llegar al agente sin la frase que frena el código antes del plan aprobado. Es el mismo riesgo en todos los proyectos instalados, no solo acá.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — «el planteamiento conserva su encuadre»**
  - **Como** quien mantiene el estándar
  - **Quiero** que el molde declare el encuadre como texto fijo y que la comprobación automática avise cuando un `*-planteamiento.md` no lo tenga
  - **Para** que ningún planteamiento llegue al agente sin la instrucción que le impide leerlo como orden de entregar código
  - **Contexto:** hoy el molde deja el encuadre fuera del recuadro que sí manda borrar, sin decir si se conserva o se reemplaza; `validar.py` no lo mira. Si no se hace, el caso de H-1 se repite en cada proyecto que herede el molde y el freno de `02·F2`/`02·F4` desaparece del punto donde más se necesita.
- **Qué se decidió:** el usuario aprobó atacarlo. Se parte en dos: que el molde declare el encuadre como texto fijo entra en la fase C de HU-002; que un programa lo compruebe queda como pendiente 77, en EP-004 · HU-004.
- **Estado:** abierto, anotado
- **Responde a:** —
- **Dispara:** 1. [Pendiente 77](../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md), EP-004 · HU-004.
- **Orden de resolución:** 2 de 2 · conviene fijar primero la redacción buena en H-1 y recién después exigirla a todos.
- **Dónde queda:** [pendiente 77](../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md), y la mitad del molde en la [fase C de HU-002](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md), tarea T-05.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** el pendiente 77 propone comprobar las dos frases que importan en vez del texto literal, para que corregir el molde no reviente el validador. Falta que el usuario lo confirme al construirlo.

### H-3 · Los moldes del ciclo llevan las marcas que el estándar prohíbe, y se las pasan a todo documento que nace de ellos

- **Qué pasó:** el planteamiento reescrito salió con 33 marcas mecánicas de [`00·ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md); el usuario lo notó antes que el agente, que no había corrido [`validadores/marcas.py`](../../../validadores/marcas.py). Al limpiarlo quedaron 2, y las 2 vienen copiadas del molde: el título y el nombre de la sección 1. Contados aparte, los moldes de `plantillas/` suman **461 marcas en 31 archivos**, y los del ciclo de vida **197 en 10**.
- **Por qué importa:** el estándar exige `00·ID8` a todo documento que el agente entrega, y sus propios moldes son la fuente. Todo planteamiento, especificación o plan que un proyecto escriba nace incumpliendo, y el que lo llena no tiene forma de saber si la marca es suya o heredada. El trinquete del commit reparte así: en `base/` y `plantillas/` falla ante cualquier marca, y en el resto solo avisa. El planteamiento vive en `prompts/`, o sea en «el resto», y por eso pasó sin que nada lo detuviera. Y sobre el molde tampoco sirve, porque no exige limpiar lo que ya está: exige no agregar.
- **Qué lo soluciona:**
  **EP-003 · HU nueva — «los moldes se entregan limpios de marcas»**
  - **Como** quien llena un molde en cualquier proyecto
  - **Quiero** que el molde no traiga marcas de generación automática
  - **Para** que el documento que escribo no nazca incumpliendo una regla que yo no escribí
  - **Contexto:** hoy `plantillas/` acumula 461 marcas mecánicas y cada copia las propaga al proyecto que la usa. Limpiar la prosa de un molde es reescribirla, así que no lo puede hacer el reemplazo automático: va molde por molde. Si no se hace, la regla queda escrita y sistemáticamente incumplida desde su propia fuente, que es la peor forma de tener una regla.
- **Qué se decidió:** el usuario aprobó anotarlo. No es hallazgo nuevo: es el pedazo chico de la decisión que el [pendiente 11](../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) dejó abierta al cerrar, acotada a los 10 moldes del ciclo. El planteamiento de Cimiento quedó limpio salvo las 2 heredadas del molde.
- **Estado:** abierto, anotado
- **Responde a:** —
- **Dispara:** 1. [Pendiente 78](../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md), EP-004 · HU-012, la misma historia del pendiente 11.
- **Orden de resolución:** 3 de 3 · es el trabajo más largo de los tres y no bloquea a los otros dos.
- **Dónde queda:** [pendiente 78](../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md).
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** antes de limpiar hay una decisión del usuario que el pendiente 11 ya había dejado escrita: si la voz de esta casa sí lleva la raya larga, lo que se cambia es el anexo de marcadores, no los moldes.

### H-4 · Se reportó un defecto del recuento que no existe  ·  **cerrado por falso**

- **Qué pasó:** el agente afirmó que [`validadores/marcas.py`](../../../validadores/marcas.py) contaba 14 marcas que están dentro de bloques de código, y que `contar()` no respetaba los bloques cercados aunque `limpiar()` sí. **Es falso.** `contar()` recorre el archivo con `lineas_utiles()`, y esa función salta los bloques cercados desde que se escribió. Las 14 las contó un clasificador improvisado que el propio agente escribió para repartir las marcas por clase, y que toggleaba la cerca pero seguía contando adentro.
- **Por qué importa:** el hallazgo llegó a escribirse en un pendiente, en el registro de cambios y en el cierre de una fase antes de comprobarse. La comprobación era una corrida de cuatro líneas: contar con `lineas_utiles()` y contar dentro de las cercas, y ver que los dos números no se solapan. **Una diferencia entre dos recuentos propios no es un defecto del programa: es una pregunta sobre cuál de los dos está mal.**
- **Qué lo soluciona:** nada que construir. Lo que había que hacer era comprobarlo, y ya está hecho: `marcas.py` cuenta 126 y dentro de las cercas hay 14 que **no** entran en esa cuenta.
- **Qué se decidió:** cerrado por falso el 2026-08-22. Se borró el pendiente 79 que se había abierto, y se corrigió la afirmación en el `CHANGELOG`, en el resultado de pruebas de la fase, en su estado y en el pendiente 78.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [resultado_pruebas.md](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo/resultado_pruebas.md) §4, D-04.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** 2026-08-22 · encuadre del planteamiento
- **Con qué se retoma:** —

### H-5 · De las 197 marcas de los moldes, la mayoría no es adorno sino notación del formulario

- **Qué pasó:** clasificadas una por una, las marcas de `plantillas/ciclo-vida-proyectos/` se reparten así. Adorno de prosa: **71**, ya limpiadas (197 → 126). Lo que queda son 43 viñetas que abren con negrita y dos puntos y **son las etiquetas de los campos del formulario** (`- **Objetivo:** «…»`), 40 en celdas de tabla, 23 en títulos y nombres de sección (`# EP-000 — «Título»`, `## 1. Necesidad — en una frase`), y 21 de la forma `**CAE-01** — «texto»`, que es un identificador con su enunciado.
- **Por qué importa:** quitarlas no limpia el molde, lo daña. Y hay una consecuencia comprobable: renombrar las secciones de un molde hace que **todos los documentos ya escritos** con él reporten «sección de la plantilla ausente» en `validar.py plantilla`. La limpieza cosmética rompería la comprobación de forma de 650 documentos.
- **Qué lo soluciona:** que el anexo declare estas cuatro formas como notación, igual que hizo el 2026-08-18 con el punto medio de los encabezados. Ese precedente está escrito en el propio anexo y bajó el recuento de 16 477 a 15 485 sin tocar un solo texto.
- **Qué se decidió:** sin decidir: es del usuario. La limpieza de adorno se hizo; la de notación se detuvo acá a propósito.
- **Estado:** abierto
- **Responde a:** el [pendiente 78](../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md), que preveía esta decisión y la nombraba antes de empezar.
- **Dispara:** —, si el usuario decide declararlas notación se edita el anexo por el procedimiento del capítulo 20.
- **Orden de resolución:** decide si el 78 puede cerrar o queda a medias.
- **Dónde queda:** el [pendiente 78](../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md).
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** ¿las cuatro formas se declaran notación en el anexo, o se reescriben los moldes asumiendo que 650 documentos van a reportar secciones ausentes?

### H-6 · Otra sesión commiteó este trabajo a medio hacer, y publicó el criterio equivocado

- **Qué pasó:** mientras esta sesión construía las dos fases, otra sesión del mismo usuario hizo `git add` de todo el árbol y commiteó. Los commits `7eaade3` (12:02) y `0e7e307` (12:10) se llevaron el archivo de pruebas sin sus dos últimos casos, `plantillas.py` **con el criterio que reprobaba documentos correctos** y sin la corrección de la tabla de ficha, las tres carpetas de fase con los moldes del andamio sin llenar, y el planteamiento reconstruido. Y subieron `VERSION` de `31.9.0` a `31.11.0`, con lo que el número que los planes de las fases declaraban quedó viejo.
- **Por qué importa:** lo que quedó publicado durante ocho minutos fue la versión del validador que reprobaba [`planteamiento.md`](../../../planteamiento.md) estando bien y reprobaba de más 110 planes de pruebas. Un validador así es el caso borde que el propio planteamiento de Cimiento nombra en §8: enseña a ignorar los veredictos. Además el usuario tiene una regla escrita de que no hay commit hasta que él lea el cambio, y este commit no pasó por ahí.
- **Qué lo soluciona:**
  **EP-005 · HU nueva — «dos sesiones a la vez no se pisan»**
  - **Como** quien trabaja con más de una sesión abierta sobre el mismo repositorio
  - **Quiero** que una sesión no se lleve en su commit lo que otra está construyendo
  - **Para** no publicar trabajo a medias, con criterios que todavía se están corrigiendo
  - **Contexto:** hoy nada lo impide. El enganche de `pre-commit` mira marcas y versión, no de quién es cada archivo que entra. `git add -A` barre con lo ajeno sin avisar. El caso ya está listado como riesgo en el planteamiento §8 y en el pendiente 43, y esta es la primera vez que se documenta ocurriendo con daño concreto.
- **Qué se decidió:** el usuario ordenó seguir sobre lo que hay, y después ordenó **resolverlo en vez de anotarlo**. Se construyó el guardián el mismo día: la [HU-017](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-017-el-commit-no-se-lleva-lo-ajeno/HU-017-el-commit-no-se-lleva-lo-ajeno.md) y su fase A. La pregunta imposible —qué sesión commitea, que `git` no sabe— se dio vuelta: se comprueba que el commit **mezcle**, y eso se ve desde los archivos.
- **Estado:** resuelto acá
- **Responde a:** el caso borde de §8 del [planteamiento](../../../prompts/cimiento-planteamiento.md).
- **Dispara:** 1. EP-005 · HU nueva, «dos sesiones a la vez no se pisan».
- **Orden de resolución:** va primero de los abiertos: mientras no se resuelva, cualquier sesión puede publicar el trabajo a medias de otra.
- **Dónde queda:** [pendiente 80](../../../pendientes/hecho/dos-sesiones-a-la-vez-no-se-pisan.md), cerrado, en EP-005 · HU-017.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** 2026-08-22 · encuadre del planteamiento
- **Con qué se retoma:** —

### H-7 · La otra sesión dio por bueno el molde sin comprobarlo, y el molde copia una cadena que ya no coincide

- **Qué pasó:** el resumen [el-encuadre-enlaza-la-cadena-no-la-copia](el-encuadre-enlaza-la-cadena-no-la-copia.md), de otra sesión de la misma jornada, cierra su H-1 diciendo que no dispara nada porque «se revisó el molde: **enlaza** `02·F0`, no copia la cadena. La copia se inventó al llenar el archivo; la plantilla está bien». Comprobado hoy, la línea 12 de [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md) sí copia una cadena, y es la divergente: «análisis → alcance → épica/HU → especificación → plan aprobado → implementación», mientras [`02·F0`](../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) dice «planteamiento → épica → HU → especificación → plan → código».
- **Por qué importa:** ese hallazgo se cerró como resuelto y sin disparar trabajo, con lo cual el defecto de fondo quedó registrado como inexistente. La copia divergente sigue viajando a cada proyecto que instale el estándar, y el registro dice que ya se miró y estaba bien, que es peor que no haberlo mirado.
- **Qué lo soluciona:** entra en la [fase C de EP-003 · HU-002](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md), que ya iba a tocar ese mismo renglón: el encuadre del molde enlaza `02·F0` en vez de copiarle la cadena.
- **Qué se decidió:** el defecto se anota acá y la corrección se hace en la fase C, que sigue esperando aprobación. No se corrige el resumen de la otra sesión: es su registro, y lo que corresponde es que este lo contradiga con la comprobación a la vista.
- **Estado:** abierto
- **Responde a:** —
- **Dispara:** —, la fase C ya existe y absorbe la tarea.
- **Orden de resolución:** con la fase C.
- **Dónde queda:** tarea nueva en el plan de la [fase C](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md).
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** la fase C, cuando el usuario apruebe su plan.

### H-8 · El agente corrió la batería entera cuatro veces, que es lo que `02·F5` pone como INCORRECTO

- **Qué pasó:** para cerrar dos fases que tocan un solo archivo de código, el agente corrió `unittest discover` sobre las 593 pruebas del repositorio cuatro veces, y además levantó una copia limpia del último commit en otro directorio para comparar los rojos. Costó unos catorce minutos de espera. Lo que la regla pide son las suites que la fase toca: dos archivos, 14 pruebas, **una décima de segundo**. Para la fase de los moldes son cinco archivos y 47 pruebas, nueve segundos.
- **Por qué importa:** [`02·F5`](../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) trae ese caso como su ejemplo INCORRECTO, con su consecuencia escrita: «cientos de pruebas, minutos de espera y **rojos que ya existían antes**». Ocurrieron las tres. Los once rojos previos obligaron a montar la copia limpia para separarlos de los propios, y ese trabajo entero es el que la regla existe para evitar. El agente citó `F5` en los dos planes mientras hacía lo contrario.
- **Qué lo soluciona:** nada que construir. La regla ya existe, dice qué correr y trae el ejemplo. Lo que faltó fue leerla al llegar a la casilla de pruebas en vez de citarla al escribir el plan.
- **Qué se decidió:** el usuario lo señaló. Las tres fases quedaron con su evidencia corregida: dicen las suites que tocan y su conteo, no la batería. La afirmación de «591 pruebas, 11 fallas previas» salió de los cuatro documentos donde estaba.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** en el `plan_pruebas` §3.5 y el `resultado_pruebas` de cada fase.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** 2026-08-22 · encuadre del planteamiento
- **Con qué se retoma:** —

### H-9 · De las 26 fases que el pendiente 59 daba por detenidas, 16 solo esperaban que alguien marcara la casilla

- **Qué pasó:** el [pendiente 59](../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) decía que 26 fases estaban detenidas esperando respuesta. Contadas el 2026-08-22, los planes con la §2.7 en «Pendiente» eran **31**, y de esos **16 ya habían corrido y tenían su veredicto escrito**: la duda estaba resuelta desde el 2026-08-18 y nadie volvió a la casilla. Las otras 15 sí son fases que nunca corrieron.
- **Por qué importa:** el pendiente describía como bloqueo lo que en más de la mitad de los casos era papeleo. Quien lo leyera para decidir por dónde empezar estaba mirando un número inflado. Y al revés: las 15 que sí faltan quedaban escondidas entre las que ya estaban hechas.
- **Qué lo soluciona:** llevar cada decisión a la §2.7 del plan que la esperaba, con su número y su enlace, y dejar el pendiente diciendo qué falta de verdad. Hecho el mismo día: 33 dudas resueltas en 16 planes.
- **Qué se decidió:** **nueve de esas 33 no eran decisiones de nadie**: se contestaban mirando lo que ya estaba construido, y quedan marcadas así en el plan para que no vuelvan a detener a nadie. Una, la del capítulo completo al escribir un archivo, se devolvió al usuario porque contradice el `CA-01` de su historia y por [`02·F19`](../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) manda el criterio de aceptación.
- **Estado:** abierto, con lo que falta medido
- **Responde a:** el pendiente 59.
- **Dispara:** —, las 15 fases restantes ya existen con su plan aprobado.
- **Orden de resolución:** las 15 se ejecutan una por una; cuatro esperan un dato del usuario, no una decisión.
- **Dónde queda:** el [pendiente 59](../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), sección «Medido el 2026-08-22».
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** las 15 fases, y el dato que falta: sobre qué proyecto y con qué encargo chico se prueban cuatro de ellas.

### H-10 · La primera fase que se desbloqueó traía dos afirmaciones falsas en su propio plan

- **Qué pasó:** al ejecutar [`A-EP-001-HU-006`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md), la primera de las 15 detenidas, dos cosas escritas en el plan no se sostuvieron. **Una:** el proyecto que el pendiente 59 proponía, shopnest-mesa, **no tiene reglas propias**, que es justamente lo que la fase viene a probar; se cambió a AgroSystem, que tiene 56. **Dos:** el plan daba por inexistente la comprobación de `M16`, y el pendiente 53 la había construido cinco días antes; lo que faltaba era saber que se invoca con `--catalogo` y no con `--raiz`.
- **Por qué importa:** los planes de estas 15 fases se escribieron el 2026-08-17 y llevan cinco días sin tocarse mientras el repositorio cambiaba debajo. **Su línea base envejeció, y `02·F17` existe justamente para que un plan no afirme lo que no verificó.** Si la primera que se abre trae dos afirmaciones falsas, conviene contar con que las otras catorce también.
- **Qué lo soluciona:** verificar la §2 de cada plan **antes** de ejecutarlo, en vez de darla por buena porque está aprobada. Es una tarea al abrir cada fase, no una fase nueva.
- **Qué se decidió:** se ejecutó igual, corrigiendo las dos afirmaciones dentro del `resultado_pruebas` en vez de tocar el plan aprobado. La fase cerró en **No cumple** por el CA-03, que no se puede provocar sin escribir contra el núcleo en un proyecto real, y eso lo prohíbe la decisión 35 del propio 59.
- **Estado:** abierto
- **Responde a:** el pendiente 59.
- **Dispara:** 1. [Pendiente 81](../../../pendientes/hecho/metareglas-sobre-un-proyecto-da-veredictos-falsos.md), que salió de la ejecución: apuntar `metareglas --raiz` a un proyecto devuelve cinco veredictos falsos, y uno de ellos afirma con el dato vacío.
- **Orden de resolución:** antes de abrir las otras 14, porque el mismo defecto de línea base las afecta a todas.
- **Dónde queda:** el [resultado de pruebas de la fase](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md) §1.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** las 14 fases restantes, verificando su §2 al abrirlas. Y el CA-03 de esta, que necesita un proyecto de mentira en carpeta temporal.

### H-11 · El único solape de tema que tiene el cuerpo de reglas ya estaba resuelto, y nadie lo sabía

- **Qué pasó:** el CA-02 de [EP-001 · HU-005](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-005-convenciones-de-ingenieria/A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas/resultado_pruebas.md) pedía revisar el cuerpo entero buscando el mismo tema en dos capítulos, y nadie lo había hecho nunca. Se barrieron las **84 reglas** comparando los títulos por pares de capítulos distintos: salieron **4 candidatos**, tres de ellos temas distintos que comparten palabras, y **uno real**: `02·F6` y `13·DOC1`, las dos sobre persistir el trabajo al cerrar. Ese ya estaba **derogado desde la 4.0.0**, con su cabecera diciendo que el dueño del tema es `13·DOC1` por `M2`.
- **Por qué importa:** es la primera medición del cuerpo completo contra `M2`, y el resultado dice algo bueno que no estaba comprobado: el procedimiento de derogación funciona y se usó. Pero también dice que **la única forma de saberlo era hacer el barrido a mano**, porque ningún programa mira `M2` sobre el cuerpo entero.
- **Qué lo soluciona:** el barrido se puede automatizar, con el límite que tiene: mira los **nombres** de las reglas, no lo que exigen. Dos reglas que exijan lo mismo con títulos distintos se le escapan, y eso queda escrito para que el «Cumple» no se lea de más.
- **Qué se decidió:** dejarlo como comprobación manual documentada, con su alcance declarado. Automatizarlo es una fase de EP-004 y no se abre sin decidirlo.
- **Estado:** abierto
- **Responde a:** el CA-02 de EP-001 · HU-005, que quedó cumplido.
- **Dispara:** —, por ahora.
- **Orden de resolución:** después de las 14 fases que faltan del pendiente 59.
- **Dónde queda:** [resultado_pruebas.md](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-005-convenciones-de-ingenieria/A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas/resultado_pruebas.md) §2, defecto D-03.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** ¿se automatiza el barrido de solapes, sabiendo que solo alcanza los títulos?

### H-12 · Un proyecto puede declarar una versión inventada, y con eso apaga el aviso que lo vigilaba

- **Qué pasó:** al ejecutar [EP-002 · HU-003](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/A-EP-002-HU-003-retrodocumentar-la-version-adoptada/resultado_pruebas.md) se copió el `CLAUDE.md` de shopnest-mesa a una carpeta temporal, se le puso `99.9.9` como versión adoptada y se corrió `validar.py version`. Respuesta: **«OK: sin incumplimientos»**. No solo no detecta el número falso: como es mayor que la vigente, concluye que el proyecto está al día y **deja de avisar del desfase**.
- **Por qué importa:** la comprobación se apaga sola con un número inventado, y el que la apaga no se entera de que la apagó. Es peor que no tenerla, porque deja la sensación de que algo vigila.
- **Y hay daño hoy, en un proyecto real:** shopnest-mesa declara `27.2.0` y su propio historial de adopciones dice que el 2026-08-20 a las 18:35 pasó a `28.0.0`. Los dos del mismo día. **Nada compara las dos cosas**, así que la contradicción lleva dos días sin que nadie la vea y el aviso de desfase se calcula sobre el número equivocado.
- **Qué lo soluciona:**
  **EP-002 · HU-003, fase nueva — «la versión adoptada se comprueba contra el registro»**
  - **Como** quien mantiene varios proyectos con el estándar instalado
  - **Quiero** que la versión que un proyecto declara se compruebe contra las que existen y contra su propio historial
  - **Para** que el aviso de desfase diga la verdad, y no se pueda apagar escribiendo un número
  - **Contexto:** hoy `version.py` compara la declarada con la vigente y nada más. Si no existe, pasa; si es mayor, calla. Y el historial que el instalador escribe en `documentacion/versiones/` no se mira nunca.
- **Qué se decidió:** las dos comprobaciones van juntas y en ese orden, primero que la versión exista y después que coincida con el historial, porque mientras un número inventado apague el aviso cualquier proyecto puede quedar en silencio sin que se note.
- **Estado:** abierto, anotado
- **Responde a:** el CA-02 de EP-002 · HU-003, que quedó en rojo.
- **Dispara:** 1. [Pendiente 82](../../../pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md), `P0`.
- **Orden de resolución:** primero de los abiertos: es la comprobación que se apaga sola.
- **Dónde queda:** [pendiente 82](../../../pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md).
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** el pendiente 82, y de paso averiguar si el instalador escribe el registro sin actualizar la declaración, que es lo que explicaría el caso de shopnest-mesa.

### H-13 · Una funcionalidad se ve andar todos los días en el único sitio donde no hace falta

- **Qué pasó:** el aviso de quedarse atrás de versión está construido y dice lo correcto, pero **hay que pedirlo a mano**. El enganche de apertura llama a `sesion.revisar()` y a `cargador.contexto()`, y ninguno de los dos mira la versión. Corrido sobre un proyecto atrasado dos versiones mayores, el arranque devuelve un solo hallazgo y es otro. Lo encontró la fase [`A-EP-002-HU-004`](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase/resultado_pruebas.md).
- **Por qué importa:** es la funcionalidad central de su historia y lleva sin conectarse desde que se escribió. **Y lo que la hizo invisible es lo que vale la pena guardar:** el aviso se ve funcionar todos los días **en el repositorio del estándar**, donde el agente corre las comprobaciones a mano. En un proyecto instalado, que es donde tiene que llegar, no aparece nunca. Una funcionalidad que se ve andar en el único sitio donde no hace falta es la más fácil de dar por hecha.
- **Qué lo soluciona:** conectar el aviso al arranque, y después hacer que diga qué cambió entre las dos versiones, que es lo que fijó la decisión 24 y sigue sin implementarse. En ese orden: conectar un aviso incompleto ya sirve; completar un aviso que nadie recibe, no.
- **Qué se decidió:** queda anotado y no se construye ahora. Antes va el [pendiente 82](../../../pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md), porque un aviso calculado sobre una versión inventada llega igual de mal.
- **Estado:** abierto, anotado
- **Responde a:** el CA-01 de EP-002 · HU-004, que quedó en rojo.
- **Dispara:** 1. [Pendiente 83](../../../pendientes/hecho/el-aviso-de-desfase-no-llega-al-abrir-sesion.md), `P0`.
- **Orden de resolución:** después del 82 y antes de seguir con las fases que quedan.
- **Dónde queda:** [pendiente 83](../../../pendientes/hecho/el-aviso-de-desfase-no-llega-al-abrir-sesion.md).
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** la pregunta que deja abierta para todo lo demás: **¿qué otras funcionalidades se ven andar solo acá?** Las cuatro fases ejecutadas hoy encontraron tres cosas desconectadas, y las tres se veían bien desde el repositorio del estándar.

### H-14 · Las quince fases detenidas se ejecutaron, y cinco no cumplen

- **Qué pasó:** las 15 fases que el pendiente 59 dejaba sin correr se ejecutaron el 2026-08-22. **Diez cumplen, cinco no.** El pendiente quedó cerrado.
- **Por qué importa:** los cinco «No cumple» son cosas que nadie sabía, y tres tienen daño hoy: una clave pegada sin comillas queda en claro en la transcripción versionada; una versión adoptada inventada pasa y **apaga** el aviso de desfase; y el aviso de quedarse atrás **no llega al abrir sesión**, hay que pedirlo a mano. Los otros dos son huecos de medición: las 249 reglas tienen la misma antigüedad de revisión —ninguna—, y un ajuste contra el núcleo no se puede provocar sin escribir en un proyecto real.
- **Y hay un hallazgo que vale más que los cinco:** las once fases encontraron que **su propio plan afirmaba cosas falsas**. No por descuido de quien las escribió, sino porque llevaban cinco días quietas mientras el repositorio cambiaba debajo. Retomar el hilo y retomar la verdad no son lo mismo, y el procedimiento que dirige solo garantiza lo primero.
- **Qué se decidió:** los cinco defectos con daño quedaron en pendientes propios, cuatro nuevos: [81](../../../pendientes/hecho/metareglas-sobre-un-proyecto-da-veredictos-falsos.md), [82](../../../pendientes/hecho/la-version-adoptada-no-se-comprueba-contra-nada.md), [83](../../../pendientes/hecho/el-aviso-de-desfase-no-llega-al-abrir-sesion.md) y [84](../../../pendientes/hecho/una-clave-pegada-sin-comillas-queda-en-claro.md), tres de ellos `P0`.
- **Estado:** resuelto acá
- **Responde a:** el [pendiente 59](../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md), cerrado.
- **Dispara:** los cuatro pendientes de arriba, ya escritos.
- **Orden de resolución:** el 84 y el 82 primero, que son los que dejan algo sin protección hoy.
- **Dónde queda:** los quince `resultado_pruebas.md` del 2026-08-22, y el cierre del pendiente 59.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** 2026-08-22 · encuadre del planteamiento
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ (H-1) |
| Todo hallazgo abierto tiene su pendiente creado | ☑ (77, 78 y 80 cerrados; 81 a 84 abiertos con su archivo; el 79 se borró por falso) |
| Toda historia disparada está escrita en su épica | ☑ (CA-04 en HU-002, CA-05 en HU-004, CA-04 en HU-012, y la HU-017 nueva en EP-005) |
| Lo que se hizo está aprobado y guardado | ☐ falta el commit. Las cuatro fases están en la puerta 12 |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
