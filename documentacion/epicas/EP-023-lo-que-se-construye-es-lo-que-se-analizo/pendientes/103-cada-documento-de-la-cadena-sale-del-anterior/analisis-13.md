# Análisis 13: un proyecto no puede reportar un pendiente a la HU del estándar que lo origina

> **Aprobado** por el usuario el 2026-10-03, en el turno 484, con la versión 51.0.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 12](analisis-12.md), aprobado el 2026-10-03. Trata el H-16, que pidió el usuario, y lo que apareció mientras estaba abierto.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se buscan los otros sitios donde un reporte o un aviso entre proyectos puede perderse |
| R-2 | Se revisa lo que ya existe: `02·F24`, `validadores/cerrar.py` y cuántas reglas y programas citan su HU. La medición llegó después de la primera propuesta (lección S-279) |
| R-6 | Se leen los acuerdos de los análisis 1 y 12. Dos se citaron de memoria y mal (lección S-280) |
| R-14 | El H-16 lo pidió el usuario con su texto |
| R-16 | El freno del piloto falló dentro del análisis; su corrección va a la HU-007 |
| R-17 | Cada respuesta se mide contra `00·ID9` antes de entregarla |
| R-3, R-4 | Se aplican en la fase que cambie `02·F24` |
| R-5, R-7 a R-13, R-15 | No aplican: el análisis no crea reglas ni plantillas, y no hay plan en ejecución |

---

## Hallazgo

### H-16 · Un proyecto no puede reportar un pendiente a la HU del estándar que lo origina

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03 el usuario pidió que un proyecto que hereda el estándar pueda reportarle un pendiente al agente, directo a la HU que lo origina. Hoy `02·F24` manda abrir «un pendiente allá» sin decir dónde, aunque desde el CA-08 de la HU-003 el pendiente vive dentro de lo que lo origina. |
| Por qué importa | Si el reporte no dice a qué HU va, el pendiente cae en el resumen del día o en un sitio equivocado, y nadie lo encuentra junto a su dueño. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 4, del [análisis 11](analisis-11.md).

| Campo | Valor |
|---|---|
| De dónde sale | H-13 de la sesión del 2026-09-28, que reúne H-10, H-11 y H-13; H-2 de la sesión del 2026-09-30; y de la sesión del 2026-10-01, H-1, H-3, H-4, H-5, H-7, H-8, H-11, H-13 y H-14, que abrieron los análisis 3 a 11 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente. La plantilla del plan no permite comprobarlo con un programa. Y el análisis no recoge solo lo que pasa: la conversación, lo que aporta al análisis principal y lo que aprende. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 458 · Usuario, 2026-10-03 18:55:43
> Analicemos: Cree un hallazgo para el pendiente 103 con el fin de que los proyectos puedan reportar pendientes al agente. La idea es que el proyecto pueda reportar el pendiente directamente a la HU que lo origina.

**Agente**, 2026-10-03 18:56:21
<!-- agente: a0cfcd97-fcc2-48a6-a81f-daaf98b67ca2 -->

Registré el hallazgo H-16 en el [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-01/sesion.md): «Un proyecto no puede reportar un pendiente a la HU del estándar que lo origina». El análisis 13 ya está prendido.

Hoy existe [`02·F24`](../../../../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md). Cuando un proyecto encuentra un defecto del estándar, la regla manda abrir un pendiente en el estándar y otro de seguimiento en el proyecto. Lo que no dice es dónde va el pendiente en el estándar. Desde el CA-08 de la HU-003, el pendiente vive dentro de lo que lo origina.

**Primera pregunta: ¿cómo sabe el proyecto cuál HU originó el defecto?** Recomiendo esto: la regla o el programa que falla ya dice en su sello de qué HU salió, por ejemplo «fase A de la HU-002 de EP-023». El reporte toma la HU de ahí. Si no la encuentra, el pendiente va al resumen del día del estándar y su análisis decide adónde pertenece.

### 459 · Usuario, 2026-10-03 19:00:01
> Apruebo

**Agente**, 2026-10-03 19:00:24
<!-- agente: 6380ab05-78d7-47bd-8251-e2745e3bd386 -->

Antes de dejarlo como acuerdo tengo que corregir algo que afirmé: no todas las reglas ni todos los programas dicen de qué HU salieron. Lo medí:

- **Reglas:** 14 de 91 citan su HU.
- **Programas:** 33 de 107 la citan en la cabecera.

Con su aprobación, el acuerdo queda así: el reporte toma la HU de la regla o del programa que falla, y si no la encuentra, el pendiente va al resumen del día del estándar. Hoy eso pasaría con la mayoría.

**Siguiente pregunta: ¿se completa la HU de origen en las reglas y los programas que no la tienen?**

Recomiendo que no se haga de una vez. Que se complete cuando el análisis de un pendiente decida a qué HU pertenece, y que desde ahí la regla o el programa la citen. Así nadie inventa un origen para lo viejo.

### 460 · Usuario, 2026-10-03 19:03:38
> Analicemos: Apruebo. También es importante que el agente le comunique al proyecto que ya se solucionó el pendiente

**Agente**, 2026-10-03 19:04:16
<!-- agente: 0d4334b4-ebdd-4d66-8166-f8f15e815189 -->

Esto ya existe en parte. [`validadores/cerrar.py`](../../../../../validadores/cerrar.py) le escribe un aviso a cada proyecto que reportó el pendiente: qué se corrigió, en qué versión llega y qué debe hacer el proyecto. Ese aviso va en la carpeta `pendientes/` del proyecto.

**El problema es que funciona con la forma vieja.** Desde la HU-003 ya no se cumplen sus dos supuestos:
- Antes, cerrar era mover el pendiente a `pendientes/hecho/`. Ahora el cierre se calcula cuando se cumple el plan que salió del pendiente, y no hay ningún momento en que alguien lo «cierre».
- Antes, el aviso iba a `pendientes/` del proyecto. Ahora esa carpeta no se crea en los proyectos nuevos.

Así, un pendiente reportado y resuelto con la forma nueva no le avisa a nadie.

**Propuesta:**
1. **El aviso sale cuando la fase que cumple el plan del pendiente anota su commit.** Ese es el momento en que el cierre se vuelve cierto.
2. **El aviso va dentro de la carpeta del pendiente de seguimiento del proyecto**, al lado de su `pendiente.md`, porque el pendiente vive donde lo origina.
3. **El seguimiento cierra solo cuando el proyecto comprueba la corrección**, como ya dicen `02·F24` y el aviso de hoy.

¿Aprueba la propuesta?

### 461 · Usuario, 2026-10-03 19:05:52
> no va en: pendientes del proyecto recuerde que esa estructura ya cambió con lo que estamos desarrollando

**Agente**, 2026-10-03 19:06:02
<!-- agente: 62d1b739-cad0-4fac-8025-c814b601403c -->

Falta la palabra que dice qué espera; por ejemplo, «Analicemos: ...».

### 462 · Usuario, 2026-10-03 19:06:08
> Analicemos

**Agente**, 2026-10-03 19:06:22
<!-- agente: 27a0aac7-feba-42fa-b4c8-6bcaf62ac1b6 -->

Tiene razón: `pendientes/` era el sitio de antes, el que usa `cerrar.py` hoy. Mi propuesta ya no lo usa. El punto 2 lleva el aviso a la carpeta del pendiente de seguimiento del proyecto, y esa carpeta vive donde nació:

- en la HU del proyecto que encontró el defecto, o
- en la carpeta del resumen del día del proyecto, mientras su análisis no decida adónde va.

Así, el aviso queda al lado del pendiente que espera la respuesta, con la estructura nueva de la HU-003.

¿Aprueba la propuesta con esa precisión?

### 463 · Usuario, 2026-10-03 19:08:27
> Apruebo

**Agente**, 2026-10-03 19:08:40
<!-- agente: afddd1b3-2931-499c-9261-72818f5f67ee -->

Queda aprobado: el aviso de que el pendiente quedó resuelto va al lado del pendiente de seguimiento del proyecto, donde ese pendiente nació.

**Siguiente pregunta: ¿a qué HU va esto?** Recomiendo la HU-003 de EP-023, por dos razones:

- **Ya trata el seguimiento.** Su CA-06 dice que el pendiente de seguimiento cierra cuando cierra el plan de su padre. Lo que acordamos completa ese criterio: dónde llega el reporte y cómo se entera el proyecto.
- **No toca las fases en curso.** Nada de esto obliga a cambiar lo que declaran los planes de la HU-003 y la HU-004 que están por aprobarse, así que va como fase nueva.

El estándar encuentra el seguimiento del proyecto siguiendo los enlaces que ya pide `02·F24`. El pendiente del estándar enlaza el hallazgo del proyecto, y ese hallazgo enlaza su pendiente. Así no hace falta un campo nuevo.

### 464 · Usuario, 2026-10-03 19:09:52
> Pregunta: qué sigue?

**Agente**, 2026-10-03 19:10:03
<!-- agente: 8609b61b-e894-42cb-827a-3101db0e5403 -->

Sigue esto, en orden:

1. **Responder mi última pregunta:** ¿esto va a la HU-003? Es lo único abierto del análisis 13.
2. **Llenar el análisis 13.** Ahí van lo acordado, las secciones que siguen, el pendiente 103 en su V5 con el H-16 en «De dónde sale», y las lecciones aprendidas.
3. **Aprobar el análisis:** «Apruebo el análisis».
4. **Llevarlo a la HU-003** como un CA nuevo, que usted aprueba.
5. **Retomar lo que estaba en espera:**
   - aprobar los planes de la fase B de la HU-003 y de la HU-004,
   - la fase de este CA nuevo,
   - la fase C de la HU-007,
   - el pendiente 109.

### 465 · Usuario, 2026-10-03 19:11:01
> Analicemos: si van en la: HU-003

**Agente**, 2026-10-03 19:11:30
<!-- agente: 9bd20202-9f5d-475b-b600-0c6fd24e5dcb -->

El freno detuvo una orden mía, y fue un error del freno. Yo solo estaba leyendo el análisis 13, pero la orden traía entre comillas el texto `> acá termina la conversación`. El freno tomó ese `>` como si fuera a escribir en un archivo llamado `acá`.

Al detenerla, anotó el H-17 en el [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-01/sesion.md) como si yo hubiera intentado escribir fuera del plan. Eso no pasó.

Este hallazgo es de la EP-023, porque el freno lo construyó la HU-007. No obliga a tocar nada fuera de un plan en curso, así que no detiene el análisis 13; puedo leer el análisis sin ese texto.

**Lo que necesito que decida:** ¿corrijo el H-17 para que diga que fue una detención por error del freno, y creo su pendiente en la HU-007? Lo recomiendo, porque así el error del freno queda con su dueño.

### 466 · Usuario, 2026-10-03 19:13:03
> Explique lo del: H-17

**Agente**, 2026-10-03 19:13:13
<!-- agente: 5c4272bf-98d1-48e0-8b60-515012b0857b -->

El freno es un portero: antes de cada orden mira si esa orden va a escribir algún archivo, y si el archivo no está en el plan, la detiene.

En la consola, el signo `>` sirve para mandar lo que sale de una orden a un archivo. Por ejemplo, `dir > lista.txt` escribe la lista en `lista.txt`.

Yo mandé una orden que solo leía el análisis 13, y adentro, entre comillas, buscaba el texto `> acá termina la conversación`. Ese `>` era parte de lo que buscaba, no una orden de escribir. El portero no se fijó en las comillas: vio `>` seguido de `acá` y creyó que yo iba a escribir un archivo llamado `acá`.

Por eso pasaron dos cosas:
1. **Detuvo la orden**, aunque no iba a escribir nada.
2. **Anotó el H-17** en el resumen de la sesión con este texto: «el freno detuvo una orden de consola sobre `acá`». Leído así, parece que yo intenté escribir fuera del plan, y eso no pasó.

El defecto es que el freno no distingue un `>` escrito dentro de unas comillas de un `>` que de verdad escribe. Mientras no se corrija, cualquier orden que solo lea texto con ese signo se puede detener por error.

### 467 · Usuario, 2026-10-03 19:14:45
> 00 id9

**Agente**, 2026-10-03 19:14:54
<!-- agente: 8fdccb37-eda9-4d51-826a-3ef0d1d6a81f -->

El freno lee cada orden antes de dejarla pasar. Si ve un `>`, cree que la orden va a escribir un archivo.

Mi orden solo leía el análisis 13, pero buscaba el texto `> acá termina la conversación`, que trae ese `>` entre comillas. El freno no se fijó en las comillas y creyó que yo iba a escribir un archivo llamado `acá`.

Por eso detuvo la orden y anotó el H-17 como si yo hubiera querido escribir fuera del plan, cosa que no pasó.

El defecto es que el freno no distingue un `>` dentro de comillas de uno que de verdad escribe.

### 468 · Usuario, 2026-10-03 19:15:19
> pregunta: que debemos hacer con H-17?

**Agente**, 2026-10-03 19:15:28
<!-- agente: 5d9282fb-70b3-48b5-91d7-335d9b4c4fb1 -->

Lo que corresponde según el acuerdo 1 del análisis 12:

1. **Corregir el texto del H-17.** Debe decir lo que pasó: el freno tomó por escritura un `>` que estaba entre comillas en una orden que solo leía.
2. **Crear su pendiente en la HU-007**, que es la que construyó el freno. El pendiente lleva el siguiente número libre y el H-17 lo enlaza.
3. **Seguir con el análisis 13.** El H-17 es de la EP-023, pero no obliga a tocar nada fuera de un plan en curso, así que no lo detiene.

Si está de acuerdo: «Hágalo».

### 469 · Usuario, 2026-10-03 19:16:31
> Pregunta por qué crear un nuevo pendiente luego dónde se origina el H?

**Agente**, 2026-10-03 19:16:45
<!-- agente: fc546c77-d30b-471d-a3d9-20ef036db037 -->

Tiene razón: no va un pendiente nuevo. Me equivoqué.

El H-17 nace en el freno. El freno lo construyó la HU-007, y la HU-007 salió del pendiente 103. El acuerdo 10 del análisis 1 dice que el hallazgo de algo ya construido no abre un pendiente nuevo: vuelve al pendiente del que salió, se abre el análisis siguiente y el pendiente pasa a su versión siguiente.

Entonces:
1. **El H-17 va al pendiente 103.** Su campo «Pendiente» lo enlaza a ese pendiente.
2. **Tiene su propio análisis.** El análisis 13 ya trata el H-16, y cada análisis lleva un solo hallazgo (acuerdo 44). Al H-17 le toca el 14, después de aprobar el 13.
3. **Se corrige el texto del H-17** para que diga lo que pasó.

### 470 · Usuario, 2026-10-03 19:18:22
> pregunta toca cerrar este para seguir con el otro?

**Agente**, 2026-10-03 19:18:33
<!-- agente: 847eb5b3-3509-4be9-a8b9-b4fb8d1803fd -->

Sí. Solo puede haber un análisis prendido a la vez, y la conversación entra a ese. El H-17 no puede entrar al 13, porque el 13 trata solo el H-16.

El orden queda así:
1. **Llenar y aprobar el análisis 13.** Ya no queda nada abierto: lo acordado está completo.
2. **Prender el 14** con «Analicemos: el pendiente 103», y tratar ahí el H-17.

Mientras tanto, el H-17 no detiene nada. Lo único que cambia es que, hasta corregirlo, evito órdenes que lean texto con `>` entre comillas.

### 471 · Usuario, 2026-10-03 19:19:16
> pero es que no se deben crear hallazgos están un análisis abierto para eso se está en análisis

**Agente**, 2026-10-03 19:19:21
<!-- agente: 80476099-1731-4b77-9a07-06c17361cd1b -->

Falta la palabra que dice qué espera; por ejemplo, «Analicemos: ...».

### 472 · Usuario, 2026-10-03 19:22:59
> Analicemos: Pero es que no se deben crear hallazgos mientras haya un análisis abierto. Lo que se debe hacer es reportarlo para que quede registrado dentro del análisis y pueda ser resuelto allí.

**Agente**, 2026-10-03 19:23:31
<!-- agente: fe0bc49d-4212-488f-814f-f6c50a56de7c -->

Entiendo, y además corrijo algo: el acuerdo 44 no dice que cada análisis lleve un solo hallazgo. Dice que los pendientes 104 y 105 se unieron al 103. Lo cité mal.

Lo que usted plantea cambia esto:

1. **El H-17 sale del resumen.** Ya quedó reportado en la conversación de este análisis (lo que pasó, por qué pasó y qué efecto tuvo), así que se resuelve aquí, en el análisis 13, junto con el H-16.
2. **El freno no crea hallazgos mientras haya un análisis prendido.** Detiene la acción y avisa. El agente lo reporta en la conversación y el análisis lo resuelve. Sin un análisis prendido, el freno sigue anotando el hallazgo en el resumen, como hoy.
3. **El defecto del H-17 se corrige en la HU-007.** El freno deja de tomar como escritura un `>` que está entre comillas.

¿Aprueba estos tres puntos?

### 473 · Usuario, 2026-10-03 19:25:06
> Explique: mejor

**Agente**, 2026-10-03 19:25:17
<!-- agente: 7efe8da9-6905-4d13-9ea0-e95f4175f32b -->

Hoy, cuando algo falla, el freno lo anota como hallazgo en el resumen de la sesión. Con un análisis abierto, eso hace que el problema quede en dos sitios: en la conversación del análisis y en el resumen. Tampoco queda claro quién lo resuelve.

Con lo que se plantea, cambian tres cosas:

1. **El H-17 se borra del resumen.** Lo que pasó ya está contado en esta conversación, y la conversación queda guardada en el análisis 13. El análisis 13 lo resuelve, además del H-16.
2. **Con un análisis abierto, el freno ya no escribe en el resumen.** Detiene la acción y avisa al agente. El agente lo cuenta en la conversación y se resuelve ahí. Cuando no hay un análisis abierto, el freno sigue anotando el hallazgo en el resumen, como hoy.
3. **Se arregla el freno.** Si un `>` está dentro de comillas, el freno entiende que es texto y no una orden de escribir un archivo. Ese arreglo va a la HU-007, que es la que construyó el freno.

Para aprobar estos tres puntos: «Apruebo».

### 474 · Usuario, 2026-10-03 19:26:23
> apruebo

**Agente**, 2026-10-03 19:26:53
<!-- agente: 5d11c19b-a350-428f-8e0e-181472236e35 -->

Quité el H-17 del [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-01/sesion.md). Lo que pasó queda contado en la conversación del análisis 13, y el análisis lo resuelve.

Los otros dos puntos van a la HU-007:
- con un análisis abierto, el freno no escribe en el resumen;
- el freno deja de leer como escritura un `>` que está entre comillas.

Así quedan los acuerdos del análisis 13:
1. El reporte del proyecto toma la HU de la regla o del programa que falla; si no la encuentra, el pendiente va al resumen del día del estándar.
2. La HU de origen se completa cuando el análisis de un pendiente decide a qué HU pertenece, no toda de una vez.
3. El aviso de que el pendiente quedó resuelto sale cuando la fase que lo cumple anota su commit, y va al lado del pendiente de seguimiento del proyecto.
4. El seguimiento cierra cuando el proyecto comprueba la corrección.
5. Todo lo anterior va a la HU-003.
6. Con un análisis abierto no se crean hallazgos: lo que aparece se reporta en la conversación y se resuelve ahí.
7. Los dos cambios del freno van a la HU-007.

Si no queda nada más por discutir, lleno el análisis 13 con «Escriba».

### 475 · Usuario, 2026-10-03 19:27:39
> Escriba

### 476 · Usuario, 2026-10-03 19:29:44
> no tiene que tomar ningún guión, para eso está la plantilla

**Agente**, 2026-10-03 19:31:49
<!-- agente: 58d557d6-16e1-460b-917a-367c8c870cd3 -->

Entendido: lleno la plantilla del análisis directamente, sin guion.

Ahora lo acordado y las secciones que siguen.

Listo: llené el [análisis 13](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-13.md) en la plantilla y pasé el [pendiente 103](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md) a la V5, con el H-16 en «De dónde sale».

- **Lo acordado:** 7 puntos, sin preguntas abiertas.
- **Lo que se tiene que hacer:**
  - Los puntos 1 a 4 van a la HU-003: el reporte, la HU de origen, el aviso y el cierre del seguimiento.
  - Los puntos 5 y 6 van a la HU-007: el freno con un análisis abierto y el `>` entre comillas.
  - El 7 y el 8 ya están hechos: quitar el H-17 del resumen y pasar el pendiente a la V5.
- **Lecciones:** S-279, S-280 y S-281, registradas en la base de señales.

La redacción no tiene marcas. El validador de análisis no le encuentra nada al 13. Sí reporta una falla que ya traía el análisis 11, que está aprobado y no se reescribe: en su tabla, la HU-007 va antes de la HU-003, de la que depende.

Para cerrar: «Apruebo el análisis».

### 477 · Usuario, 2026-10-03 19:32:46
> Pregunta: ya quedó claro todo?

**Agente**, 2026-10-03 19:32:59
<!-- agente: 02836206-2dd0-4db1-8d60-8146bc1df0f6 -->

Casi todo. Queda un punto por confirmar en el acuerdo 6: qué significa «análisis abierto».

En el estándar, esa expresión hoy dice dos cosas distintas:
- **Prendido:** el análisis que está recibiendo la conversación, como el 13 ahora.
- **Abierto:** cualquier análisis sin aprobar, y también uno aprobado cuyo plan no se ha cumplido. Con esta definición, el análisis 11 sigue abierto hasta que se termine la HU-003.

Si se toma «abierto», casi siempre hay un análisis abierto. Entonces el freno nunca anotaría un hallazgo, ni siquiera cuando nadie está conversando un análisis.

Recomiendo «prendido», que es como lo escribí en el acuerdo 6 y en el punto 5: lo que aparece mientras se conversa un análisis se reporta en ese análisis. Si no hay ninguno prendido, el freno anota el hallazgo en el resumen, como hoy.

¿Lo confirma?

### 478 · Usuario, 2026-10-03 19:33:53
> pregunta: lo de abierto lo dije yo?

**Agente**, 2026-10-03 19:34:02
<!-- agente: 7f18779a-1a04-4b87-973c-501f2d3b1005 -->

Sí. En el turno 472 dijo «no se deben crear hallazgos mientras haya un análisis abierto». Yo lo pasé al acuerdo 6 como «prendido» sin preguntarle, y eso no se debía hacer.

Por eso pregunto: en esa frase, ¿«abierto» es el análisis que se está conversando, o cualquier análisis que no ha terminado?

### 479 · Usuario, 2026-10-03 19:35:17
> analicemos: me estoy refiriendo al estado en que se encuentra en este momento el analisis-13.md

**Agente**, 2026-10-03 19:35:41
<!-- agente: 9c67dd86-7be1-4730-8da5-eb4c7238a027 -->

Entendido. «Abierto» es el estado en que está ahora el análisis 13: recibe la conversación y todavía no se ha aprobado. Desde que se aprueba, ya no está abierto.

Lo dejé así en el acuerdo 6, citando su turno 479. Mientras haya un análisis en ese estado, lo que aparece se reporta en la conversación y el freno no escribe en el resumen. Si no hay ninguno, el freno anota el hallazgo en el resumen, como hoy.

Con esto no queda nada por aclarar. Para cerrar: «Apruebo el análisis».

### 480 · Usuario, 2026-10-03 19:35:58
> pregunta: tiene otro nombre?

**Agente**, 2026-10-03 19:36:07
<!-- agente: 0e9c3d18-b62d-434b-ba5a-18504ec5a7d6 -->

Sí. En el estándar ese estado se llama **prendido**. Así lo nombra [`validadores/analisis_en_curso.py`](../../../../../validadores/analisis_en_curso.py), que tiene tres controles para el análisis:
- se **prende** con «Analicemos: el pendiente N»;
- se **pausa** con «Pare»;
- se **apaga** con «Apruebo el análisis».

El aviso que llega con cada mensaje también lo llama «análisis en curso».

En cambio, «abierto» ya significa otra cosa en ese mismo programa: el análisis sin aprobar, o aprobado pero con su plan sin cumplir.

Por eso recomiendo escribir «prendido» en el acuerdo 6, para no darle a «abierto» un segundo significado.

### 481 · Usuario, 2026-10-03 19:37:09
> entendido entonces prendido

**Agente**, 2026-10-03 19:37:15
<!-- agente: 126b90d5-86c0-4a04-9f4c-e2e47895f039 -->

Falta la palabra que dice qué espera; para cambiar el acuerdo 6 a «prendido», por ejemplo, «Corrija».

### 482 · Usuario, 2026-10-03 19:37:31
> Corrija

**Agente**, 2026-10-03 19:37:47
<!-- agente: f8bbd9eb-ad5a-4d0a-b51f-d9c692bdf9c5 -->

Listo. El acuerdo 6 del [análisis 13](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-13.md) ahora dice «prendido». Define prendido como el análisis que recibe la conversación y todavía no se ha aprobado, y aclara que no se dice «abierto» porque esa palabra ya nombra otra cosa. Cita los turnos 479 a 482. El punto 5 de «Lo que se tiene que hacer» ya usaba «prendido».

Para cerrar: «Apruebo el análisis».

### 483 · Usuario, 2026-10-03 19:38:18
> pregunta: ya es claro todo?

**Agente**, 2026-10-03 19:38:28
<!-- agente: 6dd58328-b692-494c-9e2b-01d0a8e2c053 -->

Sí. No queda ninguna pregunta abierta: los siete acuerdos tienen su turno, cada punto de «Lo que se tiene que hacer» dice adónde va, y el pendiente 103 ya está en la V5 con el H-16.

Para cerrarlo: «Apruebo el análisis».

### 484 · Usuario, 2026-10-03 19:38:43
> Apruebo el análisis

**Agente**, 2026-10-03 19:40:16
<!-- agente: 51d813ae-137a-4011-8e4d-34e86bd71dd1 -->

Llevo los puntos del análisis 13 a sus HU como criterios nuevos.

Ahora la HU-003.

Llevé el análisis 13 a sus HU, y las dos quedan pendientes de su aprobación:
- **HU-003:** CA-10 (el proyecto reporta el pendiente a la HU que lo originó) y CA-11 (el proyecto se entera cuando su pendiente se resuelve).
- **HU-007:** CA-05 (con un análisis prendido, el freno no anota hallazgos) y CA-06 (un `>` entre comillas no es escritura).

La redacción no tiene marcas. Pero `origen` da una falla en el análisis 13, que ya está aprobado. En la fila 8 de «Lo que se tiene que hacer» escribí «Análisis 11, acuerdo 5», y el validador lo lee como el punto 11 de este análisis, que no existe.

El análisis aprobado no se reescribe, así que lo reporto aquí. Este turno todavía entra en la conversación del 13.

**Necesito que decida una de dos:**
1. **Corregir el validador** para que acepte que una fila cite el acuerdo de otro análisis. Recomiendo esta, porque la fila es correcta: la V5 sale del acuerdo 5 del análisis 11.
2. **Cambiar la celda a «6»**, aunque eso reescriba un análisis aprobado.

> acá termina la conversación

---

## Lo acordado

1. De dónde toma el proyecto la HU: de la regla o del programa que falla, que la citan; si no la encuentra, el pendiente va al resumen del día del estándar y su análisis decide adónde pertenece (turnos 458 y 459).
2. La HU de origen que falta: no se completa de una vez. Se cita cuando el análisis de un pendiente decide a qué HU pertenece (turnos 459 y 460).
3. El aviso de que el pendiente quedó resuelto: sale cuando la fase que cumple el plan del pendiente anota su commit, y va al lado del pendiente de seguimiento del proyecto, donde ese pendiente nació (en su HU o en la carpeta del resumen del día), no en `pendientes/` (turnos 460 a 463).
4. Cuándo cierra el seguimiento: cuando el proyecto comprueba la corrección (turnos 460 y 463).
5. A qué HU va: los puntos 1 a 4, a la HU-003 (turnos 463 y 465).
6. Con un análisis prendido no se crean hallazgos: lo que aparece se reporta en la conversación y se resuelve en ese análisis. Prendido es el análisis que está recibiendo la conversación y no se ha aprobado, como el 13 mientras se discute; se dice «prendido» y no «abierto», que ya nombra otra cosa en `validadores/analisis_en_curso.py`. El H-17, que el freno anotó con este análisis prendido, sale del resumen y se resuelve aquí. Con un análisis prendido, el freno detiene y avisa, pero no escribe en el resumen (turnos 472 a 474 y 479 a 482).
7. El freno deja de tomar por escritura un `>` que está entre comillas. Este punto y el anterior van a la HU-007 (turnos 465 a 474).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F24` (el defecto del estándar se reporta en el estándar), `02·F23` (el pendiente se ejecuta como fase de una HU) y `13·DOC22` (lo que la sesión deja va a su resumen). Choca `02·F24`, que no dice dónde va el pendiente en el estándar; lo resuelve el punto 1. Choca `13·DOC22` con el acuerdo 6, porque hoy todo hallazgo va al resumen; lo resuelve el punto 5.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/cerrar.py` | Escribe el aviso de resuelto en `pendientes/` del proyecto al mover el pendiente a `pendientes/hecho/`. Con la forma nueva no hay movimiento ni esa carpeta |
| `validadores/pendientes.py` | Calcula el estado del pendiente; el de seguimiento toma el de su padre |
| La HU de origen | La citan 14 de 91 reglas y 33 de 107 programas |
| `validadores/freno.py` | Anota el hallazgo en el resumen aunque haya un análisis prendido, y toma por escritura un `>` entre comillas |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1, acuerdo 10 | El hallazgo de algo ya construido vuelve a su pendiente; lo confirma el acuerdo 6 |
| Análisis 1, acuerdos 11 y 36 | El pendiente vive donde nace y cierra con el plan, también entre proyectos; lo recogen los acuerdos 3 y 4 |
| Análisis 12, acuerdo 1 | Qué hallazgo detiene; el acuerdo 6 suma que con un análisis abierto no se crea hallazgo |
| Lecciones S-279, S-280 y S-281 | Las de este análisis |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MAYOR: el reporte y el aviso cambian de sitio. Va con la fase que lo construya |
| Normas y leyes | Ninguna |
| Herramientas | El aviso se escribe en la carpeta del proyecto. Hoy los proyectos están en el mismo equipo, en `plantillas/proyectos.md`, y no queda cerrado a otros usuarios |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| El defecto está en algo que no cita su HU | Cualquier proyecto que hereda | El pendiente no llega a su dueño | Punto 1: va al resumen del día del estándar |
| Un pendiente viejo de `pendientes/` se resuelve | El estándar | Pierde su aviso | No hace falta: sigue con `cerrar.py`; los viejos pasan a la forma nueva cuando se trabajan (análisis 1, acuerdo 38) |
| El proyecto que reportó no está en el mismo equipo | Otros usuarios | El aviso no llega | No hace falta hoy: todos los proyectos registrados están en el mismo equipo |
| Otra orden lleva `>` como texto, por ejemplo en un mensaje de commit | Cualquier proyecto | El freno la detiene por error | Punto 6; y la capa 2 ve lo que de verdad se escribió |
| El freno detiene algo con un análisis abierto en otro proyecto | Cualquier proyecto | El problema queda en dos sitios | Punto 5 |

---

## Propuesta final: hallazgo y pendiente V5, épica y HU

> El H-16 no cambia. El pendiente 103 pasa a la V5.

### Pendiente V5. Lo que se construye se aparta de lo aprobado

| Campo | Valor |
|---|---|
| De dónde sale | Los de la V4, y el H-16 de la sesión del 2026-10-01, que abrió el análisis 13 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente; el freno, además, toma por escritura un texto entre comillas y anota hallazgos aparte con un análisis abierto. La plantilla del plan no permite comprobarlo con un programa. El análisis no recoge solo lo que pasa: la conversación, lo que aporta al análisis principal y lo que aprende. Y un proyecto que hereda no tiene cómo reportar un pendiente a la HU que lo originó, ni se entera cuando se resuelve. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) | El hallazgo y el pendiente tienen solo lo que les corresponde | Un proyecto no puede reportar un pendiente a la HU que lo originó, ni se entera cuando se resuelve | HU-001 | Ya trata dónde vive el pendiente y cuándo cierra el seguimiento | 1 a 4 |
| 2 | [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) | Nada se escribe fuera del plan aprobado | El freno toma por escritura un texto entre comillas y anota hallazgos aparte con un análisis abierto | HU-002, HU-003, HU-004 | Es la dueña del freno | 5, 6 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Se afirmó sin medir que las reglas y los programas citan su HU | Falló | S-279 | complementa R-2 |
| 2 | Se citaron acuerdos de memoria y se propuso lo contrario de lo acordado | Falló | S-280 | complementa R-6 |
| 3 | Con un análisis abierto, el freno anotó un hallazgo aparte | Falló | S-281 | complementa R-16 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que `02·F24` diga que el reporte va a la HU que originó el defecto, tomada de la regla o del programa que falla; si no la cita, al resumen del día del estándar | 1 | EP-023, [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| 2 | Que la regla o el programa citen su HU cuando el análisis de un pendiente decida a cuál pertenece | 2 | EP-023, [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| 3 | Que, al anotar su commit, la fase que cumple el plan de un pendiente reportado escriba el aviso al lado del pendiente de seguimiento del proyecto, encontrado por los enlaces | 3 | EP-023, [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| 4 | Que el seguimiento cierre solo cuando el proyecto comprueba la corrección | 4 | EP-023, [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| 5 | Que, con un análisis prendido, el freno detenga y avise sin escribir en el resumen, y que `13·DOC22` lo diga | 6 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) |
| 6 | Que el freno no tome por escritura un `>` que está entre comillas | 7 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) |
| 7 | Quitar el H-17 del resumen | 6 | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-01/sesion.md`, hecho el 2026-10-03 |
| 8 | Pasar el pendiente 103 a la V5 | Análisis 11, acuerdo 5 | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md`, hecho el 2026-10-03 |

## Lo que aporta al análisis principal

**Resultado:** Amplía.

**Lo que suma al análisis principal:** Un proyecto que hereda reporta su pendiente a la HU del estándar que lo originó y recibe el aviso cuando se resuelve; con un análisis abierto, lo que aparece se resuelve en ese análisis.
