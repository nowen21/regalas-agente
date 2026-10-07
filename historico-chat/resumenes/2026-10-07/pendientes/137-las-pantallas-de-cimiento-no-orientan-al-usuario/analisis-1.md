# Análisis 1: las pantallas de Cimiento dan por hecho que el usuario sabe dónde están las cosas

> **Aprobado** por el usuario el 2026-10-07, en el turno 96, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisaron las 15 pantallas con formulario y las 14 tablas de Cimiento, no solo «Propuestas» («Dónde más puede pasar») |
| R-2 | Se leyó lo que existe: el capítulo `17`, la plantilla `15-diseno-de-interfaz.md`, la ayuda de la EP-025·HU-018 y los patrones de Scilit |
| R-3 | Las reglas que cambian (`17`, regla nueva) pasan su checklist en la HU que las cambia |
| R-7 | Lo que nadie pidió se preguntó: dónde rige la regla (turno 87) |
| R-8 | «Analicemos» autoriza analizar: no se tocó código ni reglas |
| R-17 | Las respuestas se midieron contra `00·ID9` |
| R-18 | «Lo acordado» se escribió en el turno de cada acuerdo, uno por tema |
| Las demás | No aplican: no se exige campo nuevo en plantillas (R-4), es el análisis 1 (R-6), no hay piloto (R-16) |

---

## Hallazgo

### H-14 · Las pantallas de Cimiento dan por hecho que el usuario sabe dónde están las cosas

| Campo | Valor |
|---|---|
| Qué pasó | Al ir a aprobar las propuestas de la EP-027·HU-007, el usuario no encontró el camino: «Propuestas» no está en el menú, no muestra qué cambió y las preguntas del tipo de versión no se entienden. Los formularios casi no tienen el «?» de ayuda y las tablas no se ordenan ni se filtran como en Scilit. El agente también dio por hecho, en el chat, que el usuario sabía llegar |
| Por qué importa | Cimiento es la línea base de los demás proyectos: si no orienta a su usuario, no puede exigírselo a los demás |

## Pendiente

**Pendiente: las pantallas de Cimiento no orientan al usuario.** Las pantallas suponen que quien las usa conoce cómo está armado Cimiento: «Propuestas», «Reportes», «Vista previa» y «Subir a git» no están en el menú; «Propuestas» no muestra qué cambió; las preguntas del tipo de versión no se entienden; casi ningún formulario tiene su «?»; ninguna tabla se ordena, se filtra ni se pagina; y no hay guía de diseño de pantallas ni regla que exija que la pantalla oriente sola. Importa porque Cimiento es la línea base que siguen los demás proyectos.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 86 · Usuario, 2026-10-07 09:22:36
> Analicemos: el pendiente 137

**Agente**, 2026-10-07 09:23:45
<!-- agente: 7eef84bc-99f7-4ab1-a212-1a862c7d11f5 -->

Antes de proponer nada, leo lo que el estándar ya dice sobre interfaz (capítulo 17) y lo que tiene Scilit.

Esta es la lectura, con lo que existe hoy:

**Lo que ya hay en el estándar**
- El capítulo `17 · Interfaz` es opt-in, y para el estándar mismo está prendido. Su regla `I5` exige seguir «el sistema de diseño que declara el proyecto», pero no existe ningún documento que lo declare: ni en Cimiento ni en Scilit.
- La plantilla `plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md` pide el mapa de navegación, el inventario de pantallas, los flujos y las convenciones visuales. Ningún proyecto la ha llenado.
- Ninguna regla exige que la pantalla oriente sola. `I4` (sin jerga) es lo más cercano.

**Lo que falta**
1. **Una guía de diseño de pantallas.** Debe decir cómo se hace cada pieza:
   - el menú, organizado por tareas;
   - el «Inicio», con lo que espera una decisión;
   - el encabezado de cada pantalla: para qué sirve y sus botones de ayuda;
   - los formularios: el «?» en cada campo y preguntas en el idioma del usuario;
   - las tablas, que se ordenan, se filtran y se dividen en páginas, como en Scilit;
   - las listas por revisar: mostrar qué cambió, aprobar varias a la vez y pedir el motivo al rechazar;
   - los mensajes y las pantallas vacías.
2. **Una regla del capítulo 17:** «La pantalla orienta sola: cada función se encuentra desde el menú o desde lo que la pide, sin conocer cómo está armado el sistema por dentro».
3. **Aplicar la guía** a las 15 pantallas de Cimiento, empezando por «Propuestas».

**Recomendación**
- La guía va como plantilla del estándar. Cada proyecto la llena con sus propios componentes, y la `I5` apunta a ella.
- Cimiento la llena primero, tomando como base los patrones de Scilit, y queda como el ejemplo que siguen los demás.

**Preguntas**
1. ¿La guía va como plantilla que llena cada proyecto, o como un documento único del estándar que rige igual para todos?
2. ¿La regla nueva va en el capítulo 17, que es opt-in, o debe regir para todo proyecto que tenga pantallas?
3. ¿Las tablas de Cimiento usan la misma librería que Scilit (List.js, que Tabler ya trae)?

### 87 · Usuario, 2026-10-07 09:31:47
> Respondo:
> 1. documento que rige para todos
> 2. Debe regir para todo proyecto que tenga pantalla
> 3. No es de Scilit es una platilla que se encuentra en: https://tabler.io/admin-template y de hecho esa plantilla sirve de inspiración para escirbir la guía de estilo o sistema de diseño. También puede ayudar: https://adminlte.io/themes/v4/docs/introduction.html

**Agente**, 2026-10-07 09:32:39
<!-- agente: 56f2d3fc-fcfd-4efe-95e7-ba6b53914015 -->

Dejé anotados los tres acuerdos en «Lo acordado». Al cruzarlos con el estándar salen dos choques:

**1. La regla para todo proyecto con pantallas.** Las reglas de pantalla viven en el capítulo `17`, que es opt-in: cada proyecto decide si lo prende. Si la regla nueva va ahí, un proyecto la apaga apagando el capítulo. Hay dos caminos:
- **(a)** El capítulo `17` entero deja de ser opt-in y rige para todo proyecto que tenga pantallas. A uno sin pantallas simplemente no le aplica.
- **(b)** Solo la regla nueva va en un capítulo obligatorio, y las demás del `17` siguen siendo opt-in.

Recomiendo la **(a)**: una pantalla que no orienta, que no se ve en todos los tamaños o que habla en jerga es tan mala como una que no guía.

**2. Una guía única y atada a Tabler.** La regla `20·M3` dice que el estándar no se ata a ninguna tecnología, y Tabler es una. Propongo:
- La guía dice **qué** hace cada pieza. Por ejemplo: «la tabla se ordena al pulsar el título de la columna, se filtra debajo y se pagina con 10, 20, 50 o 100 filas».
- Al lado de cada pieza, un ejemplo de **cómo** se hace en Tabler, que es la referencia y lo que usa Cimiento.
- Un proyecto con otra librería cumple la misma guía con la suya.

**Preguntas**
1. ¿(a) o (b)?
2. ¿La guía dice el qué para todos y pone a Tabler como ejemplo de cómo hacerlo?

### 88 · Usuario, 2026-10-07 09:38:39
> Respondo:
> 1. a
> 2. En ningún momento estoy diciendo que se aten. Estoy diciendo que sirven como inspiración para el diseño de Una guía. Me refuta pero no ha sido capaz de realizar las cosas amigable

**Agente**, 2026-10-07 09:42:13
<!-- agente: 80074307-e35b-40c1-a4af-7cbf349bc63f -->

Tiene razón: no dijo que la guía se atara a una librería, y le respondí refutando algo que no había dicho. Corrijo el acuerdo 3 y anoto el de hoy.

Antes de pedir la aprobación lleno el análisis completo. Primero registro las dos lecciones.

Paso el pendiente y el hallazgo a su versión 2, antes de la aprobación, como pide la plantilla.

El freno volvió a tomar texto del comando como si fuera una ruta (pendiente 113). Lo cambio con el editor.

Tiene razón: en ningún momento dijo que la guía se atara a una librería, y le contesté algo que no había planteado. Quedó registrado como lección (S-347).

El análisis está completo, y el programa no le encuentra nada que impida aprobarlo. Quedan **tres acuerdos**, uno por tema:
1. La guía de diseño de pantallas es un documento único del estándar y rige igual para todos.
2. El capítulo 17 deja de ser opt-in y rige para todo proyecto que tenga pantallas, con una regla nueva: la pantalla orienta sola.
3. La guía se inspira en Tabler y en AdminLTE, sin atarse a ninguna de las dos.

**Lo que sale del análisis: la épica EP-028, con seis historias de usuario**

| Orden | HU | Qué hace |
|---|---|---|
| 1 | HU-001 | El capítulo 17 rige para todo proyecto con pantallas y trae la regla nueva |
| 2 | HU-002 | La guía de diseño de pantallas |
| 3 | HU-003 | El menú se organiza por tareas, y el inicio muestra lo que espera una decisión |
| 4 | HU-004 | «Propuestas» muestra qué cambió, deja aprobar varias juntas y trae las preguntas de versión claras |
| 5 | HU-005 | Cada formulario trae su ayuda |
| 6 | HU-006 | Las tablas se ordenan, se filtran y se paginan |

Además:
- **La versión.** El cambio es **MAYOR**: un proyecto con pantallas que hoy cumple va a tener que hacer algo nuevo.
- **El ajuste del capítulo 17.** El que se creó en la EP-026·HU-009 para prenderlo o apagarlo deja de existir.
- **Lo que ya se hizo.** El pendiente y el hallazgo ya están en su versión 2.

Si está de acuerdo, se aprueba con el mensaje **«Apruebo el análisis»**.

### 89 · Usuario, 2026-10-07 09:43:50
> hágalo: a medida que vayamos acordando deben quedar en los acurdos y mostrar lo que ha acordado

**Agente**, 2026-10-07 09:44:44
<!-- agente: fd9fd496-7ba3-4a43-bacc-30eb31649926 -->

Lo guardo como recuerdo del proyecto, para que rija en todo análisis.

Hecho. Desde esta respuesta, cada vez que algo se acuerde lo anoto en ese mismo turno en «Lo acordado» del análisis, y la respuesta muestra cómo queda la lista.

Lo guardé como recuerdo del proyecto («Lo acordado se anota en el turno y se muestra en la respuesta»). Quedó como la propuesta 6, porque los recuerdos también se aprueban en la pantalla: se llega por el menú **Estándar**, con el enlace **Propuestas** que está en el texto de arriba. Ese camino escondido es justo lo que arregla la HU-003 de este análisis.

**Lo acordado hasta ahora** (análisis del pendiente 137):
1. **La guía de diseño de pantallas** es un documento único del estándar y rige igual para todos los proyectos (turno 87).
2. **Dónde rige:** el capítulo 17 deja de ser opt-in. Rige para todo proyecto que tenga pantallas, con una regla nueva: la pantalla orienta sola (turnos 87 y 88).
3. **De dónde se inspira la guía:** de Tabler y AdminLTE, sin atarse a ellos (turnos 87 y 88).

**Sigue abierto:** nada. El análisis completo está listo para aprobar con «Apruebo el análisis».

### 90 · Usuario, 2026-10-07 10:02:33
> 
> analicemos: para el acuerdo 1 en C:\Ing. Jose\ia\agente\disenio está el prompt para el diseño análicelo para que lo tenga en cuenta

**Agente**, 2026-10-07 10:03:17
<!-- agente: aaf74295-807e-4352-883b-1300b4d8b258 -->

Leí el encargo de `disenio/prompt-guia-estilo.md`. Esta es mi lectura:

**Cómo encaja con lo acordado**
- Sus 14 secciones son el índice de la guía del acuerdo 1. Sirven como criterio para aceptar la HU-002: la guía queda hecha cuando cubre las 14.
- Seis secciones ya tienen su regla en el capítulo 17: los estados (§7, `I1`), las validaciones (§5, `I2`), la accesibilidad (§9, `I3`), el lenguaje (§8, `I4`), la consistencia (§12, `I5`) y el responsive (§10, `I6`). La guía desarrolla el «cómo» de esas reglas sin repetirlas, como el molde `estructura-regla.md` desarrolla la `M5`.
- La sección §5 dice: «si el sistema puede obtener un dato, no se lo pide al usuario». Eso se aplica directo a las preguntas de versión: parte de la respuesta se puede deducir de lo que cambió.

**Un choque con el acuerdo 1**
La sección §1 pide definir la identidad visual: colores, tipografía e iconos. El acuerdo 1 dice que la guía «rige igual para todos». Si los colores también son iguales, Scilit y cualquier otro proyecto se verían idénticos a Cimiento.

**Preguntas**
1. **La identidad visual.** Recomiendo que la estructura, la jerarquía y el comportamiento sean iguales para todos, y que cada proyecto elija su color principal y su logo dentro de lo que la guía permite. ¿O todo idéntico?
2. **Una guía que se pueda ver.** Tabler y AdminLTE muestran cada componente funcionando. ¿Cimiento tiene una pantalla «Guía de diseño» con cada componente vivo, además del documento?
3. **Dónde guardar el encargo.** La carpeta `disenio/` no aparece en la tabla «Dónde va cada cosa» del `CLAUDE.md`. Lo que el usuario pide con sus palabras va en `prompts/`. ¿Se mueve ahí?

**Lo acordado hasta ahora** (sin cambios en este turno):
1. La guía de diseño es un documento único del estándar y rige igual para todos (turno 87).
2. El capítulo 17 deja de ser opt-in y rige para todo proyecto con pantallas, con la regla nueva de que la pantalla orienta sola (turnos 87 y 88).
3. La guía se inspira en Tabler y AdminLTE, sin atarse a ellos (turnos 87 y 88).

### 91 · Usuario, 2026-10-07 10:14:01
> Respondo 
> 1. 
> 
> La idea no es diseñar una plantilla nueva cada vez que se implemente un proyecto, porque ya existen muchas plantillas que se pueden instalar y utilizar como base.
>
> Lo que busco es que, si un proyecto ya tiene una plantilla instalada, se aprovechen realmente los recursos que esa plantilla ofrece para construir una buena experiencia de usuario: componentes, estilos, estructuras, patrones de navegación y demás elementos disponibles.
>
> Un ejemplo claro es Cimiento. Actualmente utiliza una plantilla, pero muchos de sus componentes y recursos no se están aprovechando. Como consecuencia, toca estar indicando constantemente “haga esto”, “cambie aquello” o “utilice este componente”, cuando precisamente la plantilla ya proporciona elementos que deberían servir como referencia para mantener una interfaz coherente y amigable.
>
> Por lo tanto, antes de crear un componente, diseño o solución nueva, se debería revisar qué ofrece la plantilla instalada y reutilizar sus recursos cuando sean adecuados. La plantilla debe funcionar como una base real para la experiencia de usuario, no simplemente estar instalada mientras cada pantalla se diseña por separado.
>
> 2. La respuesta del punto 1 responde esta pregunta
>
> 3. si

**Agente**, 2026-10-07 10:15:32
<!-- agente: dfd056d1-2f89-4ca4-8249-9737e8da9eaa -->

Anoto el traslado del encargo como fila de «Lo que se tiene que hacer» y lo muevo.

El freno revisa la orden completa antes de correrla, y la fila todavía no existía. Primero agrego la fila y después muevo el archivo.

El freno no deja borrar la carpeta `disenio/`, porque la fila nombra solo los dos archivos. Muevo únicamente el archivo.

El encargo ya está en `prompts/prompt-guia-estilo.md`. La carpeta `disenio/` quedó vacía: git no la guarda, y el freno no me dejó borrarla porque no estaba en la fila. Se puede borrar a mano.

**Lo acordado hasta ahora**
1. **La guía de diseño de pantallas** es un documento único del estándar, rige igual para todos y tiene en cuenta el encargo de `prompts/prompt-guia-estilo.md` (turnos 87 y 90).
2. **Dónde rige:** el capítulo 17 deja de ser opt-in y rige para todo proyecto que tenga pantallas, con la regla nueva de que la pantalla orienta sola (turnos 87 y 88).
3. **La base visual:** no se diseña una plantilla para cada proyecto. Cada uno aprovecha a fondo la que ya tiene instalada (Cimiento usa Tabler). Antes de crear algo nuevo, se revisa lo que esa plantilla ofrece y se reutiliza. Su propia documentación es la referencia visual. Tabler y AdminLTE inspiran la guía sin atarla (turnos 87, 88 y 91).
4. **El encargo** pasó de `disenio/` a `prompts/` (turno 91).

**Sigue abierta una pregunta**
La regla `17·I5` pide hoy usar «los componentes del sistema de diseño que declara el proyecto». Con el acuerdo 3, recomiendo que diga: «antes de crear un componente, se usa el que trae la plantilla instalada». Así lo que se acordó queda exigido como regla, y no solo escrito en la guía. ¿Se ajusta?

### 92 · Usuario, 2026-10-07 10:20:25
> apruebo el ajuste

**Agente**, 2026-10-07 10:20:55
<!-- agente: 11108cb8-bc97-483f-8b1e-8e140095ece2 -->

Quedó anotado el ajuste de la `17·I5`: hace parte del acuerdo 2 y de la fila 3, en la HU-001 de la EP-028.

**Lo acordado hasta ahora**
1. **La guía de diseño de pantallas:** es un documento único del estándar, rige igual para todos y tiene en cuenta el encargo `prompts/prompt-guia-estilo.md` (turnos 87 y 90).
2. **Las reglas de pantalla:** el capítulo 17 deja de ser opt-in y rige para todo proyecto que tenga pantallas, con una regla nueva: la pantalla orienta sola. Además, la `17·I5` pasa a decir que, antes de crear un componente, se usa el que trae la plantilla instalada (turnos 87, 88 y 92).
3. **La base visual:** cada proyecto aprovecha a fondo la plantilla que ya tiene instalada, y antes de crear algo revisa lo que ella ofrece. La documentación de esa plantilla es la referencia. Tabler y AdminLTE sirven de inspiración (turnos 87, 88 y 91).
4. **El encargo:** quedó en `prompts/` (turno 91).

**Sigue abierta:** ninguna.

El análisis está completo y el programa no le encuentra nada que impida aprobarlo. Para aprobarlo hay que escribir **«Apruebo el análisis»**.

### 93 · Usuario, 2026-10-07 10:27:25
> Pregunta: quedó claro lo que se quiere, eso significa que se va hacer lo que se pide y no otra cosa?

**Agente**, 2026-10-07 10:27:44
<!-- agente: cd327be9-e1e3-43ad-93f3-1372bbfc7b42 -->

Casi. Revisé las diez filas de «Lo que se tiene que hacer» contra lo acordado, y hay una diferencia.

**Lo que sí está acordado:**
- la guía;
- el capítulo 17 con su regla nueva y el ajuste de la `I5`;
- el uso de la plantilla instalada;
- el traslado del encargo a `prompts/`.

Eso se hace tal cual, y nada más. Si al construir aparece algo que el plan no dice, el trabajo se detiene y vuelve al análisis (`02·F8`, `02·F20`).

**Lo que puse yo sin que se acordara:** las filas 5 a 9 traen soluciones puntuales que propuse y que no se aprobaron una por una:
- el menú armado por tareas;
- un «Inicio» con lo que espera una decisión;
- «Propuestas» que muestren qué cambió y dejen aprobar varias juntas;
- las preguntas de versión reescritas;
- el «?» en cada campo;
- tablas con orden, filtro y paginación.

Salen del problema que describe el pendiente, pero el «cómo» lo escribí yo.

Hay dos caminos:
- **(a)** Confirmar esas soluciones tal como están.
- **(b)** Que esas filas digan solo «aplicar la guía a esta pantalla», y que el «cómo» lo decida la guía (HU-002), que está hecha para eso.

Recomiendo la **(b)**: así no se construye nada que no haya salido de la guía aprobada.

¿(a) o (b)?

### 94 · Usuario, 2026-10-07 10:29:05
> Respondo:
> resuma aplicando 00 id7 y 00 id9

**Agente**, 2026-10-07 10:29:15
<!-- agente: a0a1e29b-0c5e-4fa4-8493-e7143bfe7877 -->

Se va a hacer lo que se acordó y nada más. Hay un detalle: en cinco de las tareas yo ya escribí cómo hacerlas, y eso usted no lo aprobó.

Son estas:
- el menú;
- el inicio;
- la pantalla de propuestas;
- los formularios;
- las tablas.

Hay dos caminos:
- **(a)** Aprobar cómo las escribí.
- **(b)** Que esas tareas digan solo «arreglar esta pantalla siguiendo la guía», y que el cómo lo decida la guía.

Recomiendo la **(b)**. ¿Cuál se elige?

### 95 · Usuario, 2026-10-07 10:32:44
> Respondo: utilice los recursos de la plantilla instalada recuerde el acurdo 3

**Agente**, 2026-10-07 10:33:33
<!-- agente: 141d547e-4109-4882-b5b6-1b708a2b606a -->

Listo. Quité de las tareas 5 a 9 las soluciones que yo había escrito. Ahora cada una dice qué pantalla se arregla, y que se arregla con los recursos de la plantilla instalada (Tabler) siguiendo la guía. Los títulos de las historias de usuario 3 a 6 dicen lo mismo.

**Lo acordado hasta ahora**
1. **La guía de diseño de pantallas:** es un documento único del estándar, que rige igual para todos. Tiene en cuenta el encargo que quedó en `prompts/` (turnos 87 y 90).
2. **Las reglas de pantalla:** el capítulo 17 rige para todo proyecto con pantallas, con la regla nueva de que la pantalla orienta sola. La `I5` pide usar los componentes de la plantilla instalada (turnos 87, 88 y 92).
3. **La base visual:** cada proyecto aprovecha a fondo su plantilla instalada. Las pantallas de Cimiento se arreglan con los recursos de Tabler, no con soluciones que invente el agente. Tabler y AdminLTE sirven de inspiración (turnos 87, 88, 91 y 95).
4. **El encargo:** quedó en `prompts/` (turno 91).

**Sigue abierta:** ninguna. Para aprobar el análisis hay que escribir **«Apruebo el análisis»**.

### 96 · Usuario, 2026-10-07 10:36:12
> Apruebo el análisis

**Agente**, 2026-10-07 10:38:01
<!-- agente: 12ecd36e-0040-40c0-aafb-361a4c43fce1 -->

Análisis aprobado. Creo la épica EP-028 y sus seis historias de usuario.

Quedaron creadas la épica EP-028 y sus seis historias de usuario. Antes de seguir hay un orden que no cierra, y lo tiene que decidir usted.

**El problema.** La HU-001 cambia el capítulo 17, y todo cambio del estándar se aprueba en «Propuestas». Pero el turno 85 decidió que las propuestas esperan hasta que esa pantalla esté arreglada, y eso lo hace la HU-004, que va después de la HU-001 y de la guía. Así, la HU-001 no puede aprobarse hasta que exista la HU-004, y la HU-004 depende de la HU-001.

**Opciones:**
- **(a)** Arreglar primero «Propuestas» (la HU-004) con los recursos de Tabler, antes que la regla y la guía. Con la pantalla ya clara, se aprueban las propuestas de la HU-001 y las cinco de la EP-027.
- **(b)** Aprobar las propuestas de la HU-001 en la pantalla de hoy. Yo acompaño el paso a paso: menú **Estándar**, luego el enlace **Propuestas**, luego cada propuesta.

Recomiendo la **(a)**. Es la pantalla que hoy bloquea todo, y su arreglo usa lo que Tabler ya trae.

¿(a) o (b)?

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. La guía de diseño de pantallas: es un documento único del estándar, que rige igual para todos los proyectos, y tiene en cuenta el encargo `prompts/prompt-guia-estilo.md` (turnos 87 y 90).
2. Las reglas de pantalla: el capítulo 17 deja de ser opt-in y rige para todo proyecto que tenga pantallas, con su regla nueva de que la pantalla oriente sola; y `17·I5` se ajusta para decir que, antes de crear un componente, se usa el que trae la plantilla instalada (turnos 87, 88 y 92).
3. La base visual: no se diseña una plantilla para cada proyecto. Cada uno aprovecha a fondo la plantilla que ya tiene instalada (Cimiento, Tabler): antes de crear un componente, un diseño o una solución nueva, se revisa lo que ella ofrece y se reutiliza. Esa plantilla, con su propia documentación, es la referencia visual; no hace falta una pantalla aparte que la muestre. Tabler y AdminLTE inspiran la guía sin atarla. Las pantallas de Cimiento se arreglan con los recursos de su plantilla instalada, y no con soluciones que invente el agente (turnos 87, 88, 91 y 95).
4. El encargo de la guía: pasa de `disenio/prompt-guia-estilo.md` a `prompts/` (turno 91).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `17·I4` (texto para el usuario, no jerga), `17·I5` (consistencia con el sistema de diseño, que hasta hoy ningún proyecto declara), `20·M3` (la guía se inspira en Tabler y AdminLTE sin atarse a ellas) y `20·M10` (todo cambio sube versión).

Choca el encabezado del capítulo `17`, marcado `[CAPA 2 · opt-in]`: el punto 2 de «Lo acordado» lo vuelve obligatorio para todo proyecto con pantallas. Se resuelve en el punto 2 de «Lo que se tiene que hacer».

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Menú | Inicio, Proyectos, Configuración, Gasto, Estándar, Historia ([base.html](../../../../../proyectos/cimiento/templates/base.html)); «Propuestas», «Reportes», «Vista previa» y «Subir a git» solo se alcanzan por enlaces dentro de «Estándar» |
| Propuestas | Documento entero sin marcar lo que cambió, una por una, sin motivo al rechazar ([propuestas.html](../../../../../proyectos/cimiento/core/estandar/templates/estandar/propuestas.html)) |
| Preguntas de versión | Dos preguntas sin «?» ni ejemplo ([_tipo_de_version.html](../../../../../proyectos/cimiento/core/historia/templates/historia/_tipo_de_version.html)) |
| Ayuda | Funciona el botón «Ayuda» de cada pantalla; el «?» por campo y los botones de pantalla solo están en «Configuración» y «Suspensiones» (EP-025·HU-018) |
| Tablas | 14, ninguna se ordena, filtra ni pagina; Tabler, que ya usa Cimiento, trae el patrón |
| Guía de diseño | No existe; la plantilla `15-diseno-de-interfaz.md` no la reemplaza: es el mapa de pantallas de cada proyecto |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| EP-025·HU-018 | Confirma: ya pedía ayuda en cada campo y en cada pantalla; los formularios nacidos después no la recibieron. Lo recoge el punto 1 de «Lo acordado» |
| EP-014 de Scilit | Confirma: la ayuda y las tablas que funcionan salieron de ahí |
| S-347 y S-348 | Lecciones de este análisis |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Versión `MAYOR` según `20·M10`: el capítulo `17` pasa a regir a todo proyecto con pantallas. No aplica `02·F22`: no se deroga ninguna regla |
| Normas y leyes | Ninguna |
| Herramientas | Cimiento usa Tabler; la guía toma de Tabler y AdminLTE la inspiración. Las pantallas se arreglan con sus recursos: sin dependencias nuevas |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Pantalla sin entrada en el menú | «Propuestas», «Reportes», «Vista previa», «Subir a git», «Versiones» | El usuario no la encuentra | Punto 5 |
| Lo que espera una decisión no se ve | Propuestas y reportes abiertos | Se quedan sin atender | Punto 5 |
| Formulario sin «?» | 13 de 15 formularios | Se llena adivinando | Punto 8 |
| Tabla sin orden ni filtro | 14 tablas | Lo que se busca no se encuentra | Punto 9 |
| El ajuste `opt_in_17` | Configuración de cada proyecto (EP-026·HU-009) | Deja apagar un capítulo que ya no es opcional | Punto 2 |
| Scilit y los demás proyectos con pantallas | Cada proyecto | Siguen sin guía ni regla | Puntos 3 y 4: rigen para todos |
| El agente pide algo en la pantalla | Chat | Da por hecho que el usuario sabe llegar | S-348 |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Las pantallas no orientan al usuario, y el estándar no tiene guía ni regla que lo exija

| Campo | Valor |
|---|---|
| Qué pasó | Al ir a aprobar las propuestas de la EP-027·HU-007, el usuario no encontró el camino. El análisis mostró que pasa en todo Cimiento y que el estándar no tiene una guía de diseño de pantallas ni una regla obligatoria que exija que la pantalla oriente sola |
| Por qué importa | Cimiento es la línea base de los demás proyectos: si no orienta a su usuario, no puede exigírselo a los demás |

### Pendiente V2. Las pantallas orientan al usuario sin que tenga que conocer cómo está armado el sistema

| Campo | Valor |
|---|---|
| De dónde sale | Hallazgo V2: las pantallas no orientan al usuario, y el estándar no tiene guía ni regla que lo exija |
| El problema | El capítulo `17` es opt-in y no exige que la pantalla oriente; no hay guía de diseño de pantallas; y Cimiento tiene pantallas fuera del menú, propuestas que no muestran qué cambió, preguntas que no se entienden, formularios sin ayuda y tablas sin orden ni filtro |
| Por qué importa | Lo que no se encuentra no se usa, y la línea base no puede exigir lo que ella misma no cumple |

### Épica y HU que salen del análisis

Épica nueva: **EP-028, las pantallas orientan al usuario sin que tenga que conocer cómo está armado el sistema**.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-028·HU-001 | El capítulo 17 rige para todo proyecto con pantallas y exige que la pantalla oriente sola | El capítulo es opt-in y no lo exige | Ninguna | La regla tiene que existir antes de lo que la cumple | 2, 3 |
| 2 | EP-028·HU-002 | El estándar tiene su guía de diseño de pantallas | No hay guía | EP-028·HU-001 | Las pantallas se arreglan siguiendo la guía | 4 |
| 3 | EP-028·HU-003 | El menú y el inicio de Cimiento llevan a cada función con los recursos de Tabler | Pantallas fuera del menú | EP-028·HU-002 | Sigue la guía | 5 |
| 4 | EP-028·HU-004 | La pantalla de propuestas y las preguntas de versión se entienden, con los recursos de Tabler | La pantalla de propuestas | EP-028·HU-002 | Sigue la guía | 6, 7 |
| 5 | EP-028·HU-005 | Cada formulario de Cimiento trae su ayuda | Formularios sin «?» | EP-028·HU-002 | Sigue la guía | 8 |
| 6 | EP-028·HU-006 | Las tablas de Cimiento usan los recursos de tablas de Tabler | Tablas sin orden ni filtro | EP-028·HU-002 | Sigue la guía | 9 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Se responde a lo que el usuario dijo, no a lo que el agente supone que dijo | Falló | S-347 | Complementa R-8 |
| 2 | Lo que se le pide hacer al usuario en la pantalla va con el camino desde el menú | Falló | S-348 | Complementa R-10 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/pendiente.md` y `historico-chat/resumenes/2026-10-06/sesion.md`, hecho el 2026-10-07 |
| 2 | El capítulo `17` deja de ser opt-in y rige para todo proyecto con pantallas; sale el ajuste `opt_in_17` | 2 | EP-028·HU-001 |
| 3 | Regla nueva del capítulo `17`: la pantalla orienta sola, sin que el usuario conozca cómo está armado el sistema; y `17·I5` dice que antes de crear un componente se usa el de la plantilla instalada | 2, 3 | EP-028·HU-001 |
| 4 | Guía de diseño de pantallas, documento único del estándar: cubre las 14 secciones del encargo `prompts/prompt-guia-estilo.md` y manda a usar a fondo la plantilla instalada del proyecto antes de crear nada | 1, 3 | EP-028·HU-002 |
| 5 | Arreglar el menú y el inicio de Cimiento, para que toda pantalla se alcance sin conocer cómo está armado, con los recursos de la plantilla instalada y siguiendo la guía | 1, 3 | EP-028·HU-003 |
| 6 | Arreglar «Propuestas» con los recursos de la plantilla instalada y siguiendo la guía | 1, 3 | EP-028·HU-004 |
| 7 | Arreglar las preguntas del tipo de versión para que las entienda quien no conoce `20·M10`, con los recursos de la plantilla instalada y siguiendo la guía | 1, 3 | EP-028·HU-004 |
| 8 | Dar a todo formulario de Cimiento la ayuda que ya pidió la EP-025·HU-018, siguiendo la guía | 1, 3 | EP-028·HU-005 |
| 9 | Arreglar las tablas de Cimiento con los recursos de tablas de la plantilla instalada, siguiendo la guía | 1, 3 | EP-028·HU-006 |
| 10 | Mover el encargo de la guía a `prompts/` | 4 | Este análisis, de una y sin fase: `disenio/prompt-guia-estilo.md` y `prompts/prompt-guia-estilo.md`, hecho el 2026-10-07 |

## Lo que aporta al análisis principal

**Resultado:** amplía la idea y cambia lo que se construye.

**Lo que suma al análisis principal:** las pantallas de todo proyecto orientan a su usuario sin que tenga que conocer cómo está armado el sistema: el capítulo de interfaz rige para todo proyecto con pantallas, el estándar trae una guía de diseño de pantallas inspirada en Tabler y AdminLTE, y Cimiento es el primero que la cumple.
