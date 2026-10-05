# Análisis 10: los planes se escriben sin leer lo que el análisis decidió

> **Aprobado** por el usuario el 2026-10-03, en el turno 390, con la versión 49.0.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 9](analisis-9.md), aprobado el 2026-10-02. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se busca en qué otros documentos de la cadena puede pasar lo mismo, no solo en el plan |
| R-2 | Se revisa qué existe hoy para que el plan lea el análisis: la R-6 y el ORIGEN del plan |
| R-5 | Se revisan las cuatro partes contra cada punto de «Lo que se tiene que hacer» |
| R-6 | Se leen completos los análisis 1 a 9 antes de proponer |
| R-7 | Lo que nadie pidió se pregunta acá, no se agrega al plan |
| R-14 | Se confirma con el usuario que el hallazgo que abre este análisis es el H-13 |
| R-15 | No aplica: el hallazgo salió al escribir los planes, y esas fases ya cerraron |
| R-17 | Cada respuesta se mide contra `00·ID9` antes de entregarla |
| R-3, R-4, R-8 a R-13, R-16 | No aplican mientras el análisis no cree ni cambie reglas o plantillas; se revisan si eso cambia |

---

## Hallazgo

### H-13 · Los planes se escriben sin leer lo que el análisis decidió

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-02, al escribir los planes de las HU-003 y HU-004, el agente trabajó con los criterios de la HU y no leyó las conclusiones del análisis de las que salen. Preguntó tres veces lo que el análisis ya había decidido: dónde vive el 103, dónde va el índice de pendientes, y si se ajustan el anexo de fases y la frase «el plan aprobado no se modifica» (análisis 1 del pendiente 103, conclusiones 24, 33 y 41 y punto 18). Además, en el análisis 8 había agregado un traslado que ninguna conclusión decía. |
| Por qué importa | El análisis es lo que el usuario ya decidió. Un plan que no lo lee vuelve a abrir decisiones cerradas, gasta la atención del usuario y mete lo que nadie pidió. La recomendación R-6 ya lo pedía, y no bastó con que estuviera escrita: nada comprueba que el plan la siguió. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 357 · Usuario, 2026-10-03 07:33:27
> Analicemos: el pendiente 103

**Agente**, 2026-10-03 07:34:22
<!-- agente: 91059be0-cc5a-4f10-b578-491a68191bd6 -->

El análisis 10 quedó prendido. Leo cómo quedó el archivo y cómo empezó el análisis 9, para llenar el encabezado igual.

Leo las recomendaciones y el pendiente para copiarlos al encabezado.

Lleno el encabezado del análisis 10 con un guion: título, enlaces, recomendaciones, el H-13 y el pendiente copiados.

El análisis 10 está abierto, con su encabezado lleno: título, recomendaciones, el H-13 y el pendiente copiados. Antes de analizar hay que decidir dos cosas.

1. **¿El hallazgo que abre este análisis es el H-13** (los planes se escriben sin leer lo que el análisis decidió)? Así lo pide la R-14.
2. **¿El H-13 es parte del plan en curso?** Mi recomendación es que sí. El pendiente 103 trata justamente de que cada documento salga del anterior, y la EP-023 todavía no tiene nada que compruebe que el plan sale del análisis. Si es parte, se resuelve aquí antes de escribir los planes de las fases B y C (así lo pide `13·DOC24`).

Hay además dos vacíos de las fases B y C que ningún análisis definió. Propongo tratarlos aquí, porque son el mismo problema: un plan que necesita algo que el análisis no decidió.
- **La fase activa:** cuál es la fase contra cuyo plan compara el freno.
- **La integración continua:** cómo trae Cimiento el servidor para correr la revisión.

### 358 · Usuario, 2026-10-03 07:40:54
> Pregunta: qué se pretende tratar en este análisis?

**Agente**, 2026-10-03 07:41:05
<!-- agente: 56e8db55-b4f4-4dff-9b19-5e37f9b11feb -->

Se pretende tratar tres cosas:

1. **El H-13:** cómo lograr que el plan salga de lo que el análisis decidió y no solo de los criterios de la HU. Hoy la R-6 lo pide, pero nada lo comprueba, y por eso el agente volvió a preguntar cosas que ya estaban decididas.
2. **La fase activa:** el freno de la fase B compara con «el plan de la fase activa», y ningún análisis dice cuál es esa fase.
3. **La integración continua:** la capa 4 del freno corre en el servidor, y ningún análisis dice cómo llega Cimiento hasta allá.

Los puntos 2 y 3 los propongo yo y entran solo si usted los acepta. Sin ellos no se pueden escribir los planes de las fases B y C sin inventar.

### 359 · Usuario, 2026-10-03 07:42:55
> Analicemos: acepto sus propuestas y la pregunta es cómo se soluciona eso?

**Agente**, 2026-10-03 07:43:56
<!-- agente: 6d19422f-dd3f-4111-919c-fe4a5a141232 -->

Primero dejo escrito lo que se acaba de acordar. Luego reviso qué comprueba hoy `origen.py` sobre el plan, para que la propuesta del H-13 parta de lo que ya existe.

Ya quedó anotado en «Lo acordado». Estas son las propuestas, con la recomendación primero:

**1. El H-13: que el plan salga del análisis**
- **Recomendada:** el plan suma una tabla «Lo que toma del análisis», donde cada fila es un punto de «Lo acordado» y cómo lo aplica la fase. Toda decisión del plan cita su punto acordado o queda marcada como «propuesta del agente», que espera aprobación. `origen.py` lo revisa en los planes aprobados desde la versión que lo traiga.
- Hoy la cadena se comprueba hasta los criterios de la HU. El plan es el único eslabón que nadie compara con el análisis, y fue justo ahí donde falló.

**2. La fase activa**
- **Recomendada:** se calcula sola. Es la fase con plan aprobado desde 48.0.0 cuyo estado todavía no tiene el commit anotado. Si hay varias abiertas, cuentan los planes de todas.
- Otra opción: marcarla a mano en un archivo de estado, como el análisis en curso. Es más explícita, pero alguien tiene que acordarse de prenderla y apagarla.
- Sin fase activa, el freno solo deja escribir lo que una regla autoriza (análisis, resumen, memoria). Es lo que pide «nada se escribe fuera del plan», aunque obliga a tener un plan aprobado para tocar código.

**3. La integración continua**
- **Recomendada:** el instalador detecta qué servicio usa el proyecto (GitHub Actions o GitLab) y le agrega un paso. Ese paso descarga Cimiento en la versión que el proyecto adoptó y corre `validar.py plan` sobre los commits que llegan. El proyecto sin integración continua queda cubierto por el `pre-commit`, y su adaptador lo declara.
- **Riesgo:** el servidor necesita poder descargar Cimiento. El repositorio `nowen21/regalas-agente` tendría que ser público o el proyecto necesitaría un permiso de acceso.

¿Se toman las tres recomendadas, y el repositorio de Cimiento es público?

### 360 · Usuario, 2026-10-03 07:48:37
> Pregunta: si yo reviso en este momento un  CA este no sabe de qué análisis y de qué acuerdo salió?

**Agente**, 2026-10-03 07:48:48
<!-- agente: e18145f1-fc41-4061-97b3-34562345515f -->

Sí lo sabe. Cada CA trae su «Sale de», por ejemplo el CA-02 de la HU-007: «análisis 1, punto 26, y análisis 8, punto 1». Ese punto de «Lo que se tiene que hacer» cita a su vez los acuerdos de los que sale (18, 44 y 46), y `origen.py` comprueba toda la cadena.

Entonces la tabla que propuse repetiría lo que ya está, y eso va contra no escribir lo mismo en dos sitios. El enlace existía y en el H-13 el agente no lo siguió.

Lo que queda sin comprobar es otra cosa: las decisiones que el plan toma por su cuenta y no salen de ningún acuerdo, como el traslado de pendientes del H-13. Corrijo la propuesta 1: cada fila de la tabla de decisiones del plan cita su acuerdo o queda marcada como «propuesta del agente», y el usuario la aprueba con el plan.

### 361 · Usuario, 2026-10-03 07:50:55
> 00 id9

**Agente**, 2026-10-03 07:51:02
<!-- agente: 35052197-9a9a-4401-83c6-de5d786d68dd -->

Sí lo sabe: el «Sale de» de cada CA cita el punto del análisis, ese punto cita sus acuerdos y `origen.py` revisa toda la cadena. La tabla que propuse sobraba.

Lo único que falta comprobar son las decisiones que el plan toma por su cuenta. Corrijo la propuesta 1: cada decisión del plan cita su acuerdo o queda marcada como «propuesta del agente» y se aprueba con el plan.

### 362 · Usuario, 2026-10-03 07:52:38
> Pregunta: entonces en dónde está el problema que no se están revisando los análisis al construir el plan?

**Agente**, 2026-10-03 07:52:52
<!-- agente: 5a582f70-eb9f-46eb-993e-bb59ab180898 -->

El problema está en el agente, no en los documentos. La cadena existe: el CA cita su punto y el punto cita sus acuerdos. Pero al escribir el plan, el agente leyó solo el texto del CA y no siguió esos enlaces hasta los acuerdos.

Hay reglas que piden leerlos (`02·F1`, `01·C23` y la R-6), pero nada obliga a hacerlo. Además, cuando la conversación se resume por largo, lo que el agente leyó de los análisis se pierde.

Una salida que no dependa de la memoria del agente: igual que hoy le llegan las reglas con cada mensaje, que le lleguen también los acuerdos que citan los CA de la fase en la que trabaja. Así no tendría que acordarse de buscarlos.

### 363 · Usuario, 2026-10-03 07:53:33
> analicesmos le hice una pregunta concreta responda la pregunta si explicaciones innecesarias

**Agente**, 2026-10-03 07:53:42
<!-- agente: 9e231d40-9c52-4e84-b2de-597fa916ae6c -->

El problema está en el agente: al escribir el plan leyó solo el texto del CA y no siguió sus enlaces hasta los acuerdos del análisis, y nada lo obliga a hacerlo.

### 364 · Usuario, 2026-10-03 07:54:09
> Pregunta: cómo lo solucionamos?

**Agente**, 2026-10-03 07:54:18
<!-- agente: bf622449-e44a-48fe-a4e1-3a75af4cefca -->

Propongo dos cosas que se apoyan una a la otra:

1. **Que los acuerdos le lleguen solos al agente.** Mientras se trabaja una fase, el enganche lee los CA que cubre, sigue su «Sale de» hasta los acuerdos del análisis y se los entrega con cada mensaje, igual que hoy llegan las reglas. Así el agente no tiene que acordarse de buscarlos, y tampoco los pierde cuando la conversación se resume.
2. **Que el plan no apruebe lo que no sale de un acuerdo.** Cada decisión del plan cita su acuerdo o va marcada como «propuesta del agente», y `origen.py` falla si una decisión no tiene ninguna de las dos.

La primera evita que el agente pregunte lo que ya estaba decidido. La segunda evita que meta lo que nadie pidió.

### 365 · Usuario, 2026-10-03 07:56:10
> Apruebo

**Agente**, 2026-10-03 07:56:39
<!-- agente: 11d69940-8867-45c1-afc4-28998c05e1ba -->

Lo anoto en «Lo acordado».

Quedó anotado como acuerdos 2 y 3. Faltan dos decisiones:

1. **La fase activa.** Recomiendo que se calcule sola: es la fase con plan aprobado desde la 48.0.0 que todavía no tiene su commit anotado. Si no hay fase activa, solo se puede escribir lo que una regla autoriza. ¿Se toma así?
2. **La integración continua.** Para correr la revisión, el servidor tiene que descargar Cimiento desde `nowen21/regalas-agente`. ¿Ese repositorio es público?

### 366 · Usuario, 2026-10-03 07:58:01
> pregunta: con esto ya se soluciona el inconveniente o falta algo?

**Agente**, 2026-10-03 07:58:13
<!-- agente: 10cb6ce0-a0a7-42bc-81f9-ae242603ef17 -->

Falta algo. Hay dos huecos:

1. **Cuándo llegan los acuerdos.** Según lo acordado, le llegan al agente «mientras se trabaja una fase». Pero el H-13 pasó justo al escribir el plan, cuando la fase todavía no tiene plan aprobado y por eso no cuenta como activa. Tienen que llegar desde que la fase se abre, no desde que se aprueba su plan.
2. **El análisis.** En un análisis nuevo el agente también puede volver a preguntar lo que decidió uno anterior del mismo pendiente, como me pasó hoy con «quién anota el hallazgo». Ahí no hay CA que seguir. Lo que tendría que llegar son los acuerdos de los análisis aprobados de ese pendiente.

Con esos dos, el H-13 queda cubierto en el plan y en el análisis.

### 367 · Usuario, 2026-10-03 07:59:30
> analicemos: aclare sus propuestas

**Agente**, 2026-10-03 07:59:48
<!-- agente: 23a843a5-ce45-4917-9460-8d58c11729d9 -->

Las aclaro con el caso real de la fase B de la HU-007.

**1. Los acuerdos llegan desde que la fase se abre**
- Una fase está «en curso» desde que se crea su carpeta hasta que se anota su commit. Eso incluye el tiempo en que se escribe su plan.
- Mientras está en curso, el enganche sigue esta cadena: los CA que cubre la fase, el «Sale de» de cada uno, el punto del análisis y los acuerdos que ese punto cita.
- Ejemplo: la fase B cubre el CA-02. Ese CA sale del análisis 1, punto 26, y del análisis 8, punto 1. Esos puntos citan los acuerdos 18, 44 y 46 del análisis 1 y los acuerdos 1, 2 y 3 del análisis 8. Esos seis acuerdos le llegan al agente con cada mensaje.
- Esto también simplifica la fase activa del freno: se usa la misma fase en curso, y el freno solo compara cuando su plan ya está aprobado. Así hay una sola definición.

**2. Los acuerdos llegan mientras hay un análisis prendido**
- Mientras está prendido un análisis, le llegan al agente los acuerdos de los análisis ya aprobados del mismo pendiente.
- Ejemplo: hoy, con el análisis 10 prendido, llegarían los acuerdos de los análisis 1 a 9 del pendiente 103.
- Son muchos (solo el análisis 1 tiene 47), así que se manejan como las reglas: completos los que quepan, y los demás nombrados con su tema y su número, para leerlos en el archivo cuando el tema salga.

¿Se toman así?

### 368 · Usuario, 2026-10-03 08:12:47
> sigo sin entender

**Agente**, 2026-10-03 08:12:55
<!-- agente: ec85458f-122a-4949-8636-5dca30feb442 -->

Falta la palabra que dice qué se espera. Con «Explique», lo vuelvo a contar con un ejemplo sencillo.

### 369 · Usuario, 2026-10-03 08:18:08
> Explique: sigo sin entender

**Agente**, 2026-10-03 08:18:15
<!-- agente: c8d0bcdb-0078-42c2-8988-5fbafd8302fc -->

Con un ejemplo sencillo:

Usted y yo acordamos cosas en una reunión y quedan escritas en el acta, que son los análisis. Después yo me pongo a trabajar, pero no vuelvo a abrir el acta. Por eso le pregunto cosas que ya estaban en ella, y además hago otras que no estaban.

Lo que propongo es que el acta me llegue sola, pegada a cada menssuyo, para que no dependa de que me acuerde de abrirla. Llegaría en dos momentos:

1. **Cuando trabajo una fase**, aunque todavía esté escribiendo su plan: llegan los acuerdos de los que salió esa fase.
2. **Cuando estamos en un análisis**, como ahora: llegan los acuerdos de los análisis anteriores del mismo pendiente.

Y para lo que yo meta sin que esté en el acta, el plan debe decir «esto lo propone el agente», para que usted lo vea y lo apruebe o lo rechace.

### 370 · Usuario, 2026-10-03 08:20:34
> Entendido

**Agente**, 2026-10-03 08:20:37
<!-- agente: 0600b7ab-8fec-4804-bb8c-a550fc83c7d4 -->

Falta la palabra que dice qué se espera: con «Apruebo» quedan acordadas las dos propuestas y paso a la fase activa y a la integración continua.

### 371 · Usuario, 2026-10-03 08:21:05
> Apruebo

**Agente**, 2026-10-03 08:21:26
<!-- agente: d8849402-e416-4957-8dd7-e07f368a12b2 -->

Quedó como acuerdo 4. Siguen dos decisiones:

1. **La fase activa del freno.** Recomiendo usar la misma «fase en curso» del acuerdo 4, y que el freno compare con su plan solo cuando ese plan ya esté aprobado. Si no hay fase en curso, solo se puede escribir lo que una regla autoriza. ¿Se toma así?
2. **La integración continua.** El servidor tiene que descargar Cimiento desde `nowen21/regalas-agente`. ¿Ese repositorio es público?

### 372 · Usuario, 2026-10-03 08:25:20
> Analicemos
> 1. Pero por qué cuando esté aprobado, osea primero debo aprobar para darme cuenta que me quedó mal?
> 2. No se de donde salió eso?

**Agente**, 2026-10-03 08:25:35
<!-- agente: 4d1e64d1-6005-4880-86a4-21ba4d88e067 -->

1. **No hay que aprobar para darse cuenta.** Me expliqué mal. El freno no revisa si el plan quedó bien: eso se ve al revisarlo antes de aprobarlo, con los acuerdos 3 y 4. Lo que hace el freno es impedir que se escriba lo que el plan no dice.
   - Mientras el plan no está aprobado, el freno deja escribir solo los documentos de la fase (el plan y el plan de pruebas) y lo que una regla autoriza. Ningún código.
   - Ya aprobado, deja escribir también lo que el plan declara.

2. **La integración continua sale del análisis 8, acuerdo 3** (turnos 144, 153 y 155). Ahí quedó el freno en cuatro capas, y la cuarta es la integración continua: la revisión que corre en el servidor (por ejemplo GitHub) cada vez que llegan commits.
   - La pregunta por el repositorio sí es mía. Para esa revisión, el servidor de cada proyecto necesita los programas de Cimiento, y para descargarlos tiene que poder entrar a `nowen21/regalas-agente`.

### 373 · Usuario, 2026-10-03 08:44:31
> Analicemos: los proyectos que implementa el agente están en mi local porque por ahora el agente es una herramienta personal pero no queda cerrado a que pueda se utilizado por otros usuarios

**Agente**, 2026-10-03 08:44:41
<!-- agente: 93ed4029-2112-4b40-9cf3-6a0703bc20e4 -->

Entonces la capa 4 no puede depender de que hoy exista un servidor ni de que el repositorio sea público. Propongo:

1. **Recomendada: construirla ahora, apagada hasta que haga falta.** El instalador mira si el proyecto tiene integración continua (por ejemplo una carpeta `.github/workflows/`). Si la tiene, le agrega el paso de revisión; si no, no hace nada y el proyecto queda cubierto por las capas 1 a 3. De dónde se descarga Cimiento queda como un dato del proyecto, no fijo en el código, para que otro usuario pueda apuntar a su copia o usar una clave de acceso si el repositorio es privado.
2. **Dejarla como pendiente** hasta que algún proyecto tenga servidor. El análisis 8 ya decidió que existe la capa 4, así que esto cambiaría lo acordado y tendría que quedar escrito.

Hoy tus proyectos son locales, así que con la opción 1 la capa 4 no se activa en ninguno, pero queda lista para quien la use.

### 374 · Usuario, 2026-10-03 08:46:02
> apruebo

**Agente**, 2026-10-03 08:46:22
<!-- agente: 805b4586-ecbc-4785-82bb-d4a50e32923d -->

Quedó como acuerdo 5. Falta solo la fase activa, ya con la aclaración: el freno usa la «fase en curso» del acuerdo 4. Antes de aprobar el plan deja escribir solo los documentos de la fase y lo que autoriza una regla; después de aprobarlo, también lo que el plan declara. Sin fase en curso, solo lo que autoriza una regla.

¿Se aprueba así?

### 375 · Usuario, 2026-10-03 08:47:12
> Apruebo

**Agente**, 2026-10-03 08:47:25
<!-- agente: d8d7346f-9401-4fac-aee2-6ec66276d1d2 -->

Quedó anotado como acuerdo 6, y ya no hay preguntas abiertas.

Para cerrar el análisis 10 faltan sus secciones: lo que aportó cada parte, dónde más puede pasar, la propuesta final con las HU y su orden, las lecciones, lo que se tiene que hacer y lo que aporta al análisis principal. Las escribo saliendo solo de los seis acuerdos cuando digas «Escriba».

### 376 · Usuario, 2026-10-03 08:48:10
> Escriba

**Agente**, 2026-10-03 08:51:51
<!-- agente: 650f5535-a742-4aba-a4c2-3f66f5eb54b7 -->

Leo las secciones que faltan en la plantilla y cómo las llenó el análisis 9.

Necesito ver las HU de la EP-023 y su estado, para saber a cuál va cada punto, y cómo se registra una lección como señal.

La HU-005 («nada se agrega fuera de lo pedido») y la HU-002 («cada documento sale del anterior») tocan el H-13. Leo sus criterios y sus fases.

Registro las lecciones como señales de tipo `leccion`. Pruebo con la primera para ver qué número le asigna.

Las lecciones se escriben a mano en `documentacion/senales.md`, que sigue su propia numeración (va en S-126), distinta de la base local. Antes de escribir verifico los nombres que voy a citar.

Escribo las secciones y las cuatro lecciones con un guion.

Las lecciones y las secciones pasan. Corro los validadores del análisis, de origen y de enlaces, y las marcas sobre lo escrito.

(`enlaces` no es un comando de `validar.py`; los enlaces los revisa `estandar`.) Lo corro.

`estandar` no cubre `documentacion/`, así que reviso a mano los enlaces que escribí.

Escribí todas las secciones del [análisis 10](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md), y todo sale de los seis acuerdos:

- **Lo que se tiene que hacer**, cuatro puntos:
  - A la HU-002 van dos: que los acuerdos le lleguen al agente con cada mensaje, y que cada decisión del plan cite su acuerdo o vaya marcada como «propuesta del agente».
  - A la HU-007 van otros dos, que precisan su CA-02: la fase activa (fase B) y la integración continua (fase C).
- **Orden:** primero la HU-002, porque la HU-007 usa la «fase en curso» que ella define.
- **Cuatro lecciones**, registradas como S-127 a S-130 en [documentacion/senales.md](../../../../../documentacion/senales.md).

Los validadores del análisis y de origen pasan, `estandar` también, y los enlaces existen.

Encontré una cosa al registrar las lecciones: `memoria.py add` les pone otro número (S-270), porque usa la base local, mientras el validador las busca en `senales.md` (S-127). La primera quedó registrada dos veces con números distintos. ¿La anoto como hallazgo?

Para cerrar el análisis, basta con decir «Apruebo el análisis».

### 377 · Usuario, 2026-10-03 08:52:10
> Pregunta: por qué están quedando las señales en pendiente?

**Agente**, 2026-10-03 08:52:36
<!-- agente: eb251a88-b991-4b20-ade4-6877cc59a740 -->

Asumo que pregunta por las señales «Por escribir» de los análisis 1 a 9 (46 en total). Si se refiere a otra cosa, dígamelo.

Quedan así porque esos análisis se aprobaron antes de la versión 46.0.0, que fue la que exigió que cada lección enlace su señal. El plan de la fase A de la HU-006 decidió dejarlas como estaban, con «Por escribir»: un análisis aprobado no se reescribe, y la exigencia rige desde esa versión en adelante.

El análisis 10 ya cumple: sus cuatro lecciones tienen señal (S-127 a S-130).

Escribir ahora las señales de los análisis 1 a 9 cambiaría esa decisión, y habría que acordarlo en este análisis.

### 378 · Usuario, 2026-10-03 08:54:59
> Ya entiendo

**Agente**, 2026-10-03 08:55:08
<!-- agente: 80bb0812-a321-4fac-8656-557357c44899 -->

Falta la palabra que dice qué se espera. Quedan dos decisiones: si la doble numeración de las señales se anota como hallazgo («Registre») y si se cierra el análisis («Apruebo el análisis»).

### 379 · Usuario, 2026-10-03 08:55:45
> Analicemos: entiendo la explicación

**Agente**, 2026-10-03 08:55:50
<!-- agente: 652a7061-3282-4dd6-abfe-bebed2f8a219 -->

Entonces las lecciones de los análisis 1 a 9 se quedan con «Por escribir», como decidió la HU-006, y el análisis 10 no cambia.

Quedan dos cosas por decidir:
1. **La doble numeración de las señales.** `memoria.py add` numera en la base local (S-270) y el validador busca en `senales.md` (S-127), así que una misma lección queda con dos números. Para anotarla como hallazgo, «Registre».
2. **Cerrar el análisis 10**, con «Apruebo el análisis».

### 380 · Usuario, 2026-10-03 08:56:43
> Pregunta y para qué doble numeración?

**Agente**, 2026-10-03 08:56:49
<!-- agente: ff323665-3639-4a92-b85b-9e8b8c6d5a4a -->

No sirve para nada: nadie la diseñó así, es un defecto.

Hay dos sitios donde se guardan las señales:
- `memoria/senales.db` es la base local para buscar. No se versiona y junta señales de todos los proyectos de la máquina, por eso va en S-270.
- `documentacion/senales.md` es el archivo del estándar, versionado, y va en S-130.

Cada uno numera por su lado, así que la misma lección queda con dos números distintos. Lo correcto sería un solo número para cada señal.

### 381 · Usuario, 2026-10-03 08:58:19
> Analicemos: si es un defecto de una corregirlo

**Agente**, 2026-10-03 08:58:50
<!-- agente: 25f72732-e3e2-43d3-8fcb-44ce5b69f755 -->

Antes de proponer cómo corregirlo, reviso cómo se relacionan hoy la base local y `senales.md`.

Revisé las dos y el problema es más grande que el número. No solo numeran por separado: tienen contenidos distintos con el mismo número. La S-001 de la base local es «no usar `git add -A`», y la S-001 de `senales.md` es «el estándar escribía en inglés».

- **La base local** (`memoria/senales.db`) es de la máquina y no se versiona. Junta señales de todos los proyectos (cada una dice de qué proyecto es o si es general) y sirve para buscar.
- **`senales.md`** es de cada proyecto, va en git y es el que lee el validador.

**Propuesta (recomendada):**
1. La señal vive en el `senales.md` del proyecto, y su número sale de ese archivo.
2. `memoria.py add` la escribe ahí y guarda una copia en la base para buscarla, con el mismo número más el nombre del proyecto. Así dos proyectos pueden tener cada uno su S-127 sin chocar.
3. Las señales que hoy existen solo en la base se quedan como están, con su proyecto o «general», y no se renumeran.
4. Se borra de la base la S-270 que creé hoy.

Se corrige de una, en este análisis y sin fase, como el H-9, porque es el piloto (R-16).

**Descartada:** que el validador lea la base local. No va en git, así que otra máquina no la tendría.

¿Se hace así?

### 382 · Usuario, 2026-10-03 09:06:00
> explique: por que hay dos fuentes la que prima es la DB

**Agente**, 2026-10-03 09:06:32
<!-- agente: 58942376-a57b-4f27-be67-544b136c2464 -->

Busco dónde se decidió cómo conviven las dos, antes de explicar.

**Por qué hay dos:** nacieron en momentos distintos y nadie las unió después. Según la nota [notas/memoria-por-senales.md](../../../../../notas/memoria-por-senales.md):
1. Primero se hizo `senales.md`, un archivo por proyecto, versionado.
2. Después se agregó la base (`senales.db`), única para todos los proyectos y con el proyecto de cada señal, para buscar y compartir lo aprendido entre proyectos («el agente es único, su memoria también»).

Ninguna de las dos alimenta a la otra, y por eso el mismo número quedó con contenidos distintos.

**Si prima la base**, la propuesta se invierte:
- El número y el contenido salen de la base: `memoria.py add` escribe solo ahí.
- `senales.md` deja de escribirse a mano y lo genera un programa desde la base, con las señales de ese proyecto y las generales, con los mismos números. Así sigue en git, que es lo que pide `01·C29` (nada del proyecto queda fuera del repositorio), porque la base no se versiona.
- El validador sigue leyendo `senales.md`, pero ese archivo ya sería una copia exacta de la base.
- Las S-127 a S-130 que escribí a mano se pasan a la base, y el archivo se vuelve a generar.

¿Se hace así?

### 383 · Usuario, 2026-10-03 09:08:55
> aunque la DB no se versione si está dentro del proyecto y por eso se diñó en sqlite

**Agente**, 2026-10-03 09:09:03
<!-- agente: c0cbd4f2-5819-46e5-9162-afb63c3b87e4 -->

Falta la palabra que dice qué se espera. Con «Analicemos», ajusto la propuesta: la base está dentro del proyecto y basta con ella, sin generar `senales.md`.

### 384 · Usuario, 2026-10-03 09:09:23
> Analicemos: aunque la DB no se versione si está dentro del proyecto y por eso se diñó en sqlite

**Agente**, 2026-10-03 09:10:35
<!-- agente: 95a916a5-a8d7-4d9c-9e09-356b71739901 -->

Antes de ajustar la propuesta cuento cuántos documentos citan hoy las señales de `senales.md`, porque eso decide qué se hace con las que ya existen.

Tiene razón: la base está dentro del proyecto y basta con ella. Ajusto la propuesta:

1. **La base es la única fuente.** Toda señal nueva entra con `memoria.py add`, y su número sale de la base.
2. **`senales.md` se queda como está, sin señales nuevas.** No se renumera, porque 643 documentos citan sus S-001 a S-126. Como las nuevas salen de la base a partir de la S-270, ya no vuelven a chocar con las del archivo.
3. **Las cuatro lecciones de hoy van a la base.** Quito las S-127 a S-130 que escribí a mano en `senales.md`. La primera ya existe en la base como S-270 y registro las otras tres. La tabla de lecciones cita esos números.
4. **El validador de lecciones lee el tipo en la base**, no en `senales.md`.
5. **`13·DOC5` y la plantilla de señales** dicen que la señal va a la base.

Se hace de una, en este análisis.

¿Se aprueba así?

### 385 · Usuario, 2026-10-03 09:12:55
> pregunta: que necesita que le apruebe?

**Agente**, 2026-10-03 09:12:59
<!-- agente: c1d30351-7d6c-4a82-8b27-1789b7bfcff4 -->

Necesito una sola aprobación: que las señales nuevas vayan solo a la base y que `senales.md` quede como está, sin señales nuevas. Lo demás es consecuencia de eso, y usted ya dijo que se corrige de una.

### 386 · Usuario, 2026-10-03 09:13:22
> apruebo

**Agente**, 2026-10-03 09:16:52
<!-- agente: 8cfe5f4c-82ed-45dd-a91f-b0991b22d0cd -->

Lo anoto en «Lo acordado» y reviso el esquema de la base y las pruebas que hoy usan `senales.md` para las lecciones.

Ahora aplico la corrección. Primero el validador de lecciones: que lea el tipo en la base.

Ajusto un detalle: sin base se salta solo la comprobación del tipo; una lección sin ningún número sigue fallando.

26 de 26. El enganche que cada mensaje dice «la señal va a `documentacion/senales.md`» también hay que corregirlo. Lo reviso.

Ahora `senales.md`: quito las cuatro que escribí a mano y dejo dicho que ya no recibe señales nuevas.

Ahora registro en la base las otras tres lecciones y reviso la S-270.

Actualizo el análisis 10: el acuerdo 7, las lecciones con los números de la base y lo que se tiene que hacer.

Ahora el registro de cambios y la versión (49.0.0), y compruebo las lecciones del análisis 10 contra la base real.

Paso las marcas sobre lo que cambió.

La corrección del acuerdo 7 quedó hecha y anotada en el análisis 10:

- **El validador de lecciones** lee el tipo de la señal en la base ([analisis.py](../../../../../validadores/analisis.py)). Si en esa máquina no hay base, revisa solo que la lección traiga su número.
- **Las cuatro lecciones** están en la base como S-270 a S-273, y el análisis las cita con esos números. Quité las S-127 a S-130 que había escrito a mano en `senales.md`.
- **[documentacion/senales.md](../../../../../documentacion/senales.md)** dice que desde la 49.0.0 no recibe señales nuevas. Lo mismo dicen las plantillas de señales y del análisis, y el aviso del enganche.
- **`13·DOC5` no cambió**, porque no nombra dónde se guarda la señal.
- **La versión sube a 49.0.0**, con su entrada en el registro de cambios.

Las pruebas del análisis y del enganche de señales pasan, y los validadores `analisis`, `origen` y `estandar` no dan fallas.

Falta cerrar el análisis 10, con «Apruebo el análisis».

### 387 · Usuario, 2026-10-03 09:19:02
> pregunta: ya quedó claro lo que se tiene que hacer y se cumplio el desarrollo del hallazgo que generó este análisis?

**Agente**, 2026-10-03 09:19:09
<!-- agente: 6832c4a9-e3c5-43a2-ab02-3cc32cd67b0f -->

Lo que se tiene que hacer sí quedó claro: son cinco puntos, cada uno con su acuerdo de origen y su destino.

El H-13 no quedó resuelto todavía; quedó decidido cómo se resuelve:
- **Hecho:** solo el punto 5, el de las señales, que se corrigió de una.
- **Decidido y sin construir:** los puntos 1 y 2, que son la solución del H-13 (los acuerdos le llegan al agente, y el plan marca lo que propone por su cuenta). Van a la HU-002, que necesita sus criterios nuevos y su fase.
- **Decidido y sin construir:** los puntos 3 y 4, que precisan el CA-02 de la HU-007 para sus fases B y C.

Al aprobar el análisis, el H-13 pasa a «anotado»: tiene su pendiente y su destino, pero no está resuelto. Queda resuelto cuando la HU-002 construya esos dos puntos.

### 388 · Usuario, 2026-10-03 09:20:10
> pregunta: sino está resuelto por qué me pide aprobar el análisis?

**Agente**, 2026-10-03 09:20:17
<!-- agente: 557fd900-c5bc-41bf-b331-5b7c05fd4a4a -->

Porque aprobar el análisis aprueba las decisiones, no la obra terminada. La cadena va en orden: análisis, HU, plan, código.
- Sin el análisis aprobado no se pueden escribir los criterios nuevos de la HU-002 ni precisar el CA-02 de la HU-007, porque cada criterio tiene que salir de un análisis aprobado (`02·F27`).
- Aprobarlo tampoco cierra el pendiente: el análisis sigue contando como abierto hasta que las HU de su columna «Pasó a» estén terminadas, y el H-13 sigue «anotado» hasta entonces.

Es como aprobar los planos de una casa: con eso se puede empezar a construir, pero la casa todavía no existe.

### 389 · Usuario, 2026-10-03 09:21:48
> entendido

**Agente**, 2026-10-03 09:21:51
<!-- agente: 81381e46-da6f-4ea7-9f4f-ecd46ddb8c62 -->

Falta la palabra que dice qué se espera. Para cerrar el análisis 10, escribir «Apruebo el análisis».

### 390 · Usuario, 2026-10-03 09:22:03
> Apruebo el análisis

**Agente**, 2026-10-03 09:22:20
<!-- agente: ed6a3bfa-e917-4ab0-80b4-47ded789f6b4 -->

El enganche puso la marca de aprobado. Compruebo que el aporte haya pasado al análisis principal y actualizo la línea del H-13 en el resumen.

El análisis 10 quedó aprobado con la versión 49.0.0:
- Su aporte pasó al análisis principal.
- En el resumen de la sesión, el H-13 apunta al análisis 10 y dice qué HU lo resuelven.

**Lo que falta, en orden:**
1. Escribir los criterios nuevos de la HU-002 (puntos 1 y 2) y precisar el CA-02 de la HU-007 (puntos 3 y 4). Con «Escriba», los redacto para revisarlos.
2. El plan de la fase de la HU-002.
3. Los planes de las fases B y C de la HU-007.
4. El commit de lo de hoy: el análisis 10 y la corrección de las señales (versión 49.0.0), cuando lo apruebes.

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. Qué trata este análisis: el H-13, que lo abre; cuál es la fase activa contra la que compara el freno, y cómo llega Cimiento a la integración continua. Los dos últimos los propuso el agente y el usuario los aceptó (turno 359).

2. Dónde está el problema del H-13: la cadena del CA al acuerdo ya existe y `origen.py` la revisa; el agente leyó solo el texto del CA y no siguió sus enlaces hasta los acuerdos, y nada lo obliga (turnos 362 y 364).
3. Cómo se resuelve el H-13: mientras se trabaja una fase, el enganche sigue el «Sale de» de sus CA hasta los acuerdos del análisis y se los entrega al agente con cada mensaje, como las reglas. Y cada decisión del plan cita su acuerdo o va marcada como «propuesta del agente», y `origen.py` falla la que no tenga ninguna de las dos (turnos 365 y 366).
4. Cuándo llegan los acuerdos: precisa el 3. Llegan en dos momentos. Mientras una fase está en curso, desde que se crea su carpeta hasta que se anota su commit, incluido el tiempo en que se escribe su plan: los acuerdos de los que salen sus CA. Y mientras hay un análisis prendido: los acuerdos de los análisis aprobados del mismo pendiente. Como las reglas, llegan completos los que caben y los demás nombrados con su tema y su número (turnos 367 a 372).
5. La integración continua: hoy los proyectos son locales, porque el agente es una herramienta personal, pero puede usarlo otra persona. La capa 4 se construye ahora y se activa sola: el instalador mira si el proyecto tiene integración continua y, si la tiene, le agrega el paso de revisión; si no, el proyecto queda con las capas 1 a 3. De dónde se descarga Cimiento es un dato del proyecto, no queda fijo en el código, para que otro usuario apunte a su copia o use una clave si el repositorio es privado (turnos 374 y 375).
6. La fase activa del freno: es la fase en curso del acuerdo 4. Antes de aprobarse su plan, el freno deja escribir solo los documentos de la fase y lo que una regla autoriza; aprobado el plan, también lo que el plan declara. Sin fase en curso, solo lo que una regla autoriza. El freno no revisa si el plan quedó bien: eso se ve al revisarlo antes de aprobarlo (turnos 373, 375 y 376).
7. Las señales tienen una sola fuente: la base de señales, que está dentro del proyecto. Cada señal nueva entra con `memoria.py add`, que le da su número; `documentacion/senales.md` se queda como está, sin señales nuevas y sin renumerar, porque otros documentos citan sus números. El validador de lecciones lee el tipo en la base. Se corrige de una, en este análisis y sin fase (turnos 380 a 387).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F27` (cada documento cita su origen), `02·F1` (cargar el contexto antes de actuar) y `01·C23` (buscar en el repositorio antes de preguntar), que ya pedían leer el análisis y no bastaron: los recogen los puntos 1 y 2 de «Lo que se tiene que hacer». Aplican `02·F8` (editar solo lo que el plan declara) y `04·S9` (nada se escribe fuera del proyecto), que el freno hace cumplir según el punto 3. Ninguna choca con lo acordado.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/origen.py` | Sigue la cadena hasta el criterio de la HU; no mira las decisiones del plan |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Su sección 2.6, «Decisiones técnicas», no pide de qué acuerdo sale cada decisión |
| `validadores/recuperar.py` y `adaptadores/claude-code/hook_reglas.py` | Entregan las reglas con cada mensaje; no entregan acuerdos |
| `validadores/analisis_en_curso.py` | Sabe qué análisis está prendido y de qué pendiente es |
| `adaptadores/claude-code/hook_antes.py` | Frena solo lo que sale del proyecto, y solo en la herramienta de escritura |
| `validadores/ci.py` | Avisa si el proyecto no tiene integración continua; no le agrega pasos |
| `memoria/senales.db` y `documentacion/senales.md` | Dos fuentes de señales que numeran cada una por su lado: el mismo número tiene contenidos distintos en cada una |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-13 y la R-6 | La recomendación escrita no bastó: nada obliga a recorrer la cadena. Lo recoge el acuerdo 2 |
| Análisis 1, punto 26, y análisis 8, acuerdo 8 | Ya decían que el freno anota el hallazgo, y en este análisis se volvió a preguntar: confirma el H-13. Lo recoge el acuerdo 4 |
| Análisis 8, acuerdo 3 | Fijó las cuatro capas sin decir cuál es la fase activa ni cómo llega Cimiento al servidor. Lo recogen los acuerdos 5 y 6 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MAYOR: el plan marca lo que propone el agente y el freno no deja escribir código antes de aprobar el plan. `02·F22` no aplica: nada se deroga |
| Normas y leyes | Ninguna aplica |
| Herramientas | La herramienta resume la conversación cuando crece y se pierde lo leído; el enganche que entrega las reglas con cada mensaje es el que puede entregar los acuerdos |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Plan escrito sin leer los acuerdos | Cualquier proyecto y agente | Vuelve a preguntar lo decidido o mete lo que nadie pidió | Puntos 1 y 2 |
| Análisis que vuelve a preguntar lo que decidió otro del mismo pendiente | Pendientes con varios análisis | La discusión se repite | Punto 1 |
| Conversación resumida por largo | Herramientas que resumen el contexto | Lo leído se pierde | Punto 1: los acuerdos llegan con cada mensaje |
| Acuerdos que no caben en el mensaje | Pendientes con muchos análisis | El mensaje se llena o se corta | Punto 1: completos los que caben y los demás nombrados |
| Código escrito antes de aprobar el plan | Cualquier fase | Código sin plan | Punto 3 |
| Trabajo sin ninguna fase en curso | Cambios fuera de la cadena | Código sin plan | Punto 3: solo lo que una regla autoriza |
| Proyecto sin integración continua | Proyectos locales | Sin la capa 4 | Punto 4: quedan las capas 1 a 3 |
| Cimiento privado, o una copia de otro usuario | Otros usuarios | El servidor no puede descargarlo | Punto 4: el origen es un dato del proyecto |
| Señal con el mismo número en dos sitios | Cualquier proyecto con base y archivo de señales | Se cita una señal y se lee otra | Punto 5 |
| Agente que no es Claude Code | Otras herramientas | Los acuerdos no le llegan por enganche | Punto 2: `origen.py` falla el plan con cualquier agente; el contrato del adaptador dice qué cubre (análisis 8, acuerdo 3) |

---

## Propuesta final: hallazgo y pendiente

> El H-13 no cambia. El pendiente sigue en la V3. EP-023 no suma HU: la HU-002 suma criterios y la HU-007 precisa su CA-02.

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | [HU-002](../../HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md) | Cada documento sale del anterior | Nada obliga a que cada documento salga del anterior | Ninguna | Define la fase en curso y entrega los acuerdos que la HU-007 usa al escribir sus planes | 1, 2 |
| 2 | [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) | Nada se escribe fuera del plan aprobado | Nada detiene al agente cuando trabaja fuera del plan aprobado | HU-002, HU-003, HU-004 | Su freno usa la fase en curso de la HU-002 | 3, 4 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Los planes se escribieron con el texto del CA, sin seguir su cadena hasta los acuerdos | Falló | S-270 | complementa R-6 |
| 2 | El agente propuso una tabla que repetía la cadena que ya existía; la pregunta del usuario lo mostró | Falló | S-271 | complementa R-2 |
| 3 | El agente dio por hecho un servidor y un repositorio público; los proyectos son locales y otros pueden usar el agente | Falló | S-272 | complementa R-1 |
| 4 | El ejemplo del acta de una reunión aclaró la propuesta que dos explicaciones técnicas no aclararon | Funcionó | S-273 | complementa R-10 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que el agente reciba con cada mensaje los acuerdos de los que sale lo que trabaja: en una fase en curso, los que citan sus CA; con un análisis prendido, los de los análisis aprobados del mismo pendiente; completos los que caben y los demás nombrados con su tema y su número | 3, 4 | EP-023, [HU-002](../../HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md) |
| 2 | Que cada decisión del plan cite su acuerdo o vaya marcada como «propuesta del agente», y que `origen.py` falle la que no tenga ninguna de las dos | 3 | EP-023, [HU-002](../../HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md) |
| 3 | Precisar el CA-02 de la HU-007: la fase activa es la fase en curso; antes de aprobar su plan solo se escriben los documentos de la fase y lo que una regla autoriza, y sin fase en curso, solo lo autorizado | 6 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), fase B |
| 4 | Precisar el CA-02 de la HU-007: la capa 4 se activa sola si el proyecto tiene integración continua, y de dónde se descarga Cimiento es un dato del proyecto | 5 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), fase C |
| 5 | Que las señales nuevas vayan solo a la base: el validador de lecciones lee el tipo en ella, `senales.md` dice que no recibe señales nuevas, y las plantillas del análisis y de las señales y el aviso de señales lo dicen. Las lecciones de este análisis van a la base | 7 | Este análisis, de una y sin fase |

## Lo que aporta al análisis principal

**Resultado:** Amplía la idea.

**Lo que suma al análisis principal:** El agente recibe los acuerdos de los que sale lo que trabaja, y lo que el plan decide por su cuenta queda marcado como propuesta suya. El freno compara con la fase en curso, y la revisión en el servidor se activa sola donde hay integración continua. Las señales tienen una sola fuente, la base.
