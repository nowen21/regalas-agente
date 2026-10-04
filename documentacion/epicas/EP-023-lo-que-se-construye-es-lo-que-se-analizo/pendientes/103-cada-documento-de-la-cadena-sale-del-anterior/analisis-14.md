# Análisis 14: el validador de origen no acepta que una fila cite el acuerdo de otro análisis

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 13](analisis-13.md), aprobado el 2026-10-03. Trata el H-18, que apareció al revisar el origen del análisis 13 ya aprobado.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se buscó dónde más se cita el acuerdo de otro análisis: la plantilla, que lo trae en cada análisis nuevo, y los otros proyectos, donde el análisis 11 no existe |
| R-2 | Se leyó `origen.py` y se encontró que ya entendía «Análisis N, acuerdo M» en el plan |
| R-12 | La plantilla sirve a cualquier proyecto: por eso la cita al análisis 11 pasa a una regla del estándar (acuerdo 3) |
| R-16 | El freno y el validador del piloto fallaron dentro del análisis y se corrigieron de una |
| R-17 | Cada respuesta se mide contra `00·ID9`; el usuario pidió acortar cuatro veces (lección S-283) |
| R-3 a R-11, R-13 a R-15 | No aplican: no se crean reglas en este análisis y no hay plan en ejecución |

---

## Hallazgo

### H-18 · El validador de origen no acepta que una fila cite el acuerdo de otro análisis

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03, ya aprobado el análisis 13 del pendiente 103, `validar.py origen` falló en su fila 8 de «Lo que se tiene que hacer». La fila dice «Análisis 11, acuerdo 5», y el validador lo lee como el punto 11 de «Lo acordado» del mismo análisis, que no existe. |
| Por qué importa | Pasar el pendiente a su versión siguiente sale siempre de un acuerdo de otro análisis (análisis 11, acuerdo 5). Mientras el validador no lo acepte, cada análisis que lo cite falla, o tiene que citar un número equivocado para pasar. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 5, del [análisis 13](analisis-13.md).

| Campo | Valor |
|---|---|
| De dónde sale | Los hallazgos que abrieron los análisis 3 a 11 y 13, el último el H-16 de la sesión del 2026-10-01 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente; el freno, además, toma por escritura un texto entre comillas y anota hallazgos aparte con un análisis abierto. La plantilla del plan no permite comprobarlo con un programa. El análisis no recoge solo lo que pasa: la conversación, lo que aporta al análisis principal y lo que aprende. Y un proyecto que hereda no tiene cómo reportar un pendiente a la HU que lo originó, ni se entera cuando se resuelve. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 488 · Usuario, 2026-10-03 20:15:29
> Analicemos: el pendiente 103

**Agente**, 2026-10-03 20:15:55
<!-- agente: 3494cc6b-6384-4103-8216-ee00cf966953 -->

El análisis 14 quedó prendido con el H-18. Revisé [`validadores/origen.py`](../../../../../validadores/origen.py): la columna «Sale de lo acordado» toma todos los números de la celda y los busca en «Lo acordado» del mismo análisis. Por eso «Análisis 11, acuerdo 5» lo lee como el acuerdo 11 de este análisis.

El mismo programa ya entiende «Análisis N, acuerdo M» en otro sitio: en las decisiones del plan (tabla 2.6), donde busca el acuerdo en ese otro análisis.

**Propuesta:**
1. **La celda acepta dos formas.** Un número solo es un acuerdo de este análisis. «Análisis N, acuerdo M» es un acuerdo de otro análisis del mismo pendiente, y el validador revisa que exista allá, como ya lo hace con el plan.
2. **La plantilla del análisis lo dice**, en la nota de «Lo que se tiene que hacer».
3. **Va a la HU-002**, porque `origen.py` salió de su CA-01.

Con esto, el análisis 13 pasa sin reescribirlo.

¿Aprueba la propuesta?

### 489 · Usuario, 2026-10-03 20:16:34
> Explique: entiendo lo que pasó

**Agente**, 2026-10-03 20:16:47
<!-- agente: 072d7aeb-910a-4556-804e-988b5182a8ae -->

Entonces explico la solución con un ejemplo.

Cada fila de «Lo que se tiene que hacer» dice de qué acuerdo sale. Hoy el validador solo entiende una forma de decirlo: un número, que busca en este mismo análisis.

- Si la fila dice **«6»**, el validador busca el acuerdo 6 del análisis 13, lo encuentra y la fila pasa.
- Si dice **«Análisis 11, acuerdo 5»**, el validador no sabe leer esa frase. Toma los números sueltos, el 11 y el 5, y los busca en el análisis 13. Como ahí no hay acuerdo 11, marca la falla.

Con la propuesta, el validador entiende las dos formas:
- **«6»**: busca el acuerdo 6 en este análisis, igual que hoy.
- **«Análisis 11, acuerdo 5»**: va al análisis 11 y revisa que su acuerdo 5 exista.

No hay que inventar nada nuevo. El mismo programa ya entiende «Análisis N, acuerdo M» cuando revisa las decisiones del plan. Solo falta que también lo entienda en el análisis.

¿Aprueba la propuesta?

### 490 · Usuario, 2026-10-03 20:18:15
> pregunta por que sucede eso?

**Agente**, 2026-10-03 20:18:27
<!-- agente: 28e1f19d-9f3c-407e-bfb4-9f47ef5b9d84 -->

Por dos razones:

1. **Cuando se construyó `origen.py`, ese caso no existía.** Se hizo en la HU-002, y en ese momento cada fila salía de un acuerdo de su propio análisis. Desde el análisis 11 apareció una fila que se repite en todos los análisis: pasar el pendiente a su versión siguiente. Esa fila sale del acuerdo 5 del análisis 11, no del análisis en curso. El programa nunca aprendió a leer esa forma de citar.

2. **El validador revisa el análisis solo cuando ya está aprobado.** `origen.py` salta a propósito el análisis que todavía se está llenando. «Apruebo el análisis» tampoco lo corre: solo mira que haya filas y que esté «Lo que aporta». Por eso el error apareció después de aprobar, cuando el análisis ya no se puede reescribir.

La segunda razón es la más grave: cualquier error de origen se descubre tarde. Propongo sumar esto a la propuesta: que «Apruebo el análisis» corra la revisión de `origen` y no ponga la marca si encuentra una falla, para que el error se corrija antes de aprobar.

### 491 · Usuario, 2026-10-03 20:18:55
> 00 id9

**Agente**, 2026-10-03 20:19:02
<!-- agente: d83cacbe-446f-4240-80d5-ffe08c74b2dc -->

Sucede por dos razones:

1. **`origen.py` no sabe leer «Análisis 11, acuerdo 5».** Cuando se construyó, todas las filas citaban acuerdos de su propio análisis.
2. **Solo revisa el análisis ya aprobado.** Por eso el error se vio cuando el análisis ya no se podía corregir.

Propongo sumar algo a la propuesta: que «Apruebo el análisis» corra esa revisión antes de poner la marca. Así el error se corrige antes de aprobar.

### 492 · Usuario, 2026-10-03 20:19:39
> osea que hemos analizado pero la plantilla no ha cambiado?

**Agente**, 2026-10-03 20:19:48
<!-- agente: 79aba3ac-be73-4152-9e20-965b84658efc -->

Falta la palabra que dice qué se espera; por ejemplo, «Pregunta: ...» o «Analicemos: ...».

### 493 · Usuario, 2026-10-03 20:19:56
> pregunta

**Agente**, 2026-10-03 20:20:07
<!-- agente: 1dfa78b7-07c9-4cc7-8bfe-046dad1f19ea -->

Sí. Lo que aprueba un análisis no cambia nada por sí solo: pasa a un CA de una HU, y la plantilla o el programa cambian cuando se construye la fase de ese CA.

Hoy hay varias cosas aprobadas que todavía no se construyen:
- **La plantilla del análisis:** sigue diciendo que todo hallazgo abre un análisis. Eso lo cambia la fase B de la HU-004, que tiene el plan escrito y sin aprobar.
- **La aprobación del análisis:** todavía no revisa que el hallazgo esté en el pendiente. Eso lo hace la fase B de la HU-003, en la misma situación.
- **Los CA del análisis 13:** el CA-10 y el CA-11 de la HU-003, y el CA-05 y el CA-06 de la HU-007, todavía sin fase.

Por eso sigo trabajando con la plantilla y los programas viejos, y van saliendo hallazgos que lo ya aprobado resolvería. El H-18 es un caso nuevo: ningún análisis lo había tratado.

### 494 · Usuario, 2026-10-03 20:20:59
> pregunta: osea que los cambios que habido esto: "C:\Ing. Jose\ia\agente\documentacion\epicas\EP-023-lo-que-se-construye-es-lo-que-se-analizo\pendientes\103-cada-documento-de-la-cadena-sale-del-anterior\borrador-plantilla-analisis.md" no lo sabe?

**Agente**, 2026-10-03 20:21:49
<!-- agente: 94820e77-605c-43e6-b796-3f3417a3383c -->

Ese borrador no es la plantilla que se usa. Es el que se escribió en el análisis 1. La fase A de la HU-001 lo convirtió en [`plantillas/analisis.md`](../../../../../plantillas/analisis.md), y desde entonces se quedó como estaba. Ningún programa lo lee.

La plantilla de verdad sí recogió lo que se fue aprobando después. Ya tiene cosas que el borrador no tiene:
- «Recomendaciones»;
- «Lo acordado» con su turno, en lugar de «Conclusiones»;
- «Dónde más puede pasar»;
- el orden de las HU con sus dependencias;
- la señal S-NNN en las lecciones;
- las rutas exactas para lo que se hace de una;
- «Lo que aporta al análisis principal».

Lo que todavía no ha cambiado es lo aprobado y sin construir, que nombré antes: lo de la HU-003, lo de la HU-004 y el análisis 13. Esos cambios llegan a `plantillas/analisis.md` cuando se construyan sus fases. Al borrador no llegan.

### 495 · Usuario, 2026-10-03 20:22:35
> pregunta: entonces que es lo que genera este análisis?

**Agente**, 2026-10-03 20:22:45
<!-- agente: adf3a058-a5f9-4d4e-95e6-4bd7a3794bdc -->

El análisis 14 deja tres cosas:

1. **Un CA nuevo en la HU-002.** `origen.py` entiende «Análisis N, acuerdo M», y «Apruebo el análisis» corre esa revisión antes de poner la marca. Esto está propuesto y todavía no lo ha aprobado.
2. **Un cambio en la nota de la plantilla del análisis**, que diga las dos formas de citar el origen.
3. **El pendiente 103 en la V6**, con el H-18 en «De dónde sale».

Como con los demás análisis, la plantilla y el programa cambian cuando se construya la fase de ese CA. Lo único que queda hecho al aprobar es el pendiente en la V6.

### 496 · Usuario, 2026-10-03 20:23:26
> pregunta: y por qué en los otros análisis no sucedió?

**Agente**, 2026-10-03 20:23:37
<!-- agente: 1c25c573-6828-4556-98b5-7645f9a706b3 -->

Porque el análisis 13 fue el primero en citar el acuerdo de otro análisis.

- **Análisis 11:** la fila «Pasar el pendiente 103 a la V4» cita el acuerdo 6 de ese mismo análisis, porque ahí se acordó. El validador lo encontró.
- **Análisis 12:** el pendiente no pasó de versión, así que no hubo esa fila.
- **Análisis 13:** pasar a la V5 no se acordó en la conversación, porque ya es una regla que viene del acuerdo 5 del análisis 11. Escribí «Análisis 11, acuerdo 5», y esa forma el validador no la entiende.

Desde ahora, todos los análisis van a tener esa fila, porque todos pasan el pendiente a su versión siguiente. Por eso el error iba a repetirse.

### 497 · Usuario, 2026-10-03 20:24:44
> pregunta: la plantilla ya sabe ese nuevo cambio?

**Agente**, 2026-10-03 20:24:53
<!-- agente: 4a42fe91-4f2d-460d-872a-c85ac62d2e75 -->

No. La plantilla pide el «Pendiente V«N+1»» en la «Propuesta final», pero en «Lo que se tiene que hacer» no trae la fila para pasarlo de versión. Además, su nota dice que «Sale de» cita un punto de «Lo acordado» de ese mismo análisis, sin decir cómo citar el de otro.

Por eso escribí la fila a mano y la cité de una forma que el validador no entiende.

Propongo sumar esto al análisis 14: que la plantilla traiga esa fila ya escrita, con su origen («Análisis 11, acuerdo 5»), y que la nota diga las dos formas de citar.

### 498 · Usuario, 2026-10-03 20:25:26
> de una corrija la plantilla

**Agente**, 2026-10-03 20:26:20
<!-- agente: 1adc76d7-6b7c-4809-9e68-77e485573f34 -->

Registro el acuerdo y su fila «de una» en el análisis 14, para que el freno deje tocar la plantilla.

Ahora la plantilla.

El freno detuvo el cambio a la plantilla. No la toqué.

**Qué pasó:** el freno sí deja pasar las rutas que el análisis prendido manda hacer «de una», pero las busca en la columna «Lo que se tiene que hacer». Yo las puse en «Pasó a», como lo hicieron los análisis 11, 12 y 13 y como lo deja entender la plantilla. El freno lee una columna y los análisis escriben en otra. Lo reporto aquí porque el análisis 14 está prendido.

**Otro efecto:** el freno volvió a anotar un hallazgo en el resumen de la sesión. Es lo mismo del H-17: el acuerdo 6 del análisis 13 ya lo prohíbe, pero todavía no está construido.

**Necesito que decida dos cosas:**
1. **Cómo se hace el cambio de la plantilla ahora.** Recomiendo repetir las rutas en la columna «Lo que se tiene que hacer» de la fila 1 del análisis 14, para que el freno las vea, y sumar al análisis que el freno las lea en «Pasó a».
2. **El hallazgo que anotó el freno.** Recomiendo quitarlo del resumen, como se hizo con el H-17, porque lo resuelve este análisis.

### 499 · Usuario, 2026-10-03 20:26:51
> 00 id9

**Agente**, 2026-10-03 20:26:58
<!-- agente: 5435fffb-42f0-4add-a46d-f9627a46a042 -->

El freno no me dejó cambiar la plantilla. Busca las rutas «de una» en la columna «Lo que se tiene que hacer», y yo las puse en «Pasó a», como en los análisis anteriores. Además, volvió a anotar un hallazgo en el resumen.

Necesito que decida dos cosas:
1. **¿Repito las rutas en la columna que lee el freno?** Así cambio la plantilla ya, y queda en el análisis que el freno debe leerlas en «Pasó a». Lo recomiendo.
2. **¿Quito el hallazgo del resumen, como se hizo con el H-17?** También lo recomiendo.

### 500 · Usuario, 2026-10-03 20:27:30
> analicemos: no entiendo la propuesta

**Agente**, 2026-10-03 20:27:42
<!-- agente: 3b3ed6a1-8a97-4797-9865-bccf4790e763 -->

Lo explico con la fila del análisis 14 que manda cambiar la plantilla. La tabla tiene cuatro columnas:

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que la plantilla traiga la fila... | 1 | Este análisis, de una: `plantillas/analisis.md` |

El freno deja escribir los archivos que una fila «de una» nombra. El problema es dónde los busca: solo en la columna «Lo que se tiene que hacer». Yo los escribí en «Pasó a», así que el freno no vio `plantillas/analisis.md` y me detuvo.

**Propuesta 1:** escribir la ruta también en «Lo que se tiene que hacer», por ejemplo «Que `plantillas/analisis.md` traiga la fila...». El freno la ve y la plantilla se corrige ya. Además, queda acordado que después se arregle el freno para que lea «Pasó a», que es donde los análisis la ponen.

**Propuesta 2:** al detenerme, el freno escribió un hallazgo en el resumen de la sesión. Con un análisis prendido eso no debe pasar (acuerdo 6 del análisis 13). Propongo borrarlo, como se hizo con el H-17.

### 501 · Usuario, 2026-10-03 20:28:19
> 00 id9

**Agente**, 2026-10-03 20:28:29
<!-- agente: 1f1ef7a0-3327-4c64-aa00-650709b88505 -->

El freno solo deja escribir los archivos que encuentra en la columna «Lo que se tiene que hacer». Yo escribí la ruta de la plantilla en «Pasó a», y por eso me detuvo.

Son dos propuestas:
1. **Escribir la ruta también en «Lo que se tiene que hacer»**, para cambiar la plantilla ya. Después se arregla el freno para que lea «Pasó a».
2. **Borrar el hallazgo que el freno anotó en el resumen**, como se hizo con el H-17.

### 502 · Usuario, 2026-10-03 20:28:49
> En serio que no quiero tantas explicaciones quiero algo muy corto

**Agente**, 2026-10-03 20:28:58
<!-- agente: 26e5e25c-a8be-4635-8974-4c1a23d3ca3a -->

Entendido. ¿Repito la ruta donde el freno la lee y borro el hallazgo que anotó? Para hacerlo: «Apruebo».

### 503 · Usuario, 2026-10-03 20:29:47
> explique a un niño: no entiendo el problema

**Agente**, 2026-10-03 20:29:54
<!-- agente: 6448fbc0-0a34-4f97-b3cf-b7a73099d912 -->

El freno es un portero con una lista de los archivos que se pueden tocar. Esa lista la saca de una sola columna de la tabla del análisis. Yo anoté la plantilla en otra columna, así que el portero no la encontró y no me dejó entrar.

### 504 · Usuario, 2026-10-03 20:30:34
> pregunta qué se debe hacer para solucionar el problema?

**Agente**, 2026-10-03 20:30:42
<!-- agente: 4f7c1b82-650f-47ac-b010-46ca5f577c2d -->

Hay que hacer dos cosas:

1. **Ahora:** anotar la plantilla en la columna que lee el freno. Así la puedo corregir.
2. **Después:** arreglar el freno para que también lea la columna «Pasó a», que es donde la escriben los análisis.

### 505 · Usuario, 2026-10-03 20:31:06
> apruebo y solucione de una

**Agente**, 2026-10-03 20:33:04
<!-- agente: 06d7cd92-0984-4536-b4f3-cd433e962a52 -->

Ahora la plantilla.

Ahora el freno: que lea las rutas en las dos columnas.

Corro las pruebas del freno y escribo la versión.

Listo, versión 51.1.0:

- **Plantilla:** trae la fila que pasa el pendiente a su versión siguiente y explica las dos formas de citar el origen.
- **Freno:** ahora también lee las rutas en «Pasó a». Sus 14 pruebas pasan.
- **El H-19 salió del resumen.**

Hay un problema que debe decidir. La plantilla la usan todos los proyectos, pero «Análisis 11, acuerdo 5» solo existe en este repositorio. En otro proyecto esa cita no apunta a nada. ¿La cambio por la regla del estándar que lo exija, cuando exista?

### 506 · Usuario, 2026-10-03 20:34:04
> pues los demás proyectos deben saber que la plantilla cambió para que la actualicen

**Agente**, 2026-10-03 20:34:12
<!-- agente: fc27b16d-2316-4ad9-b39a-280a2a3e4f3a -->

Falta la palabra que dice qué espera; por ejemplo, «Analicemos: ...».

### 507 · Usuario, 2026-10-03 20:34:19
> Analicemos

**Agente**, 2026-10-03 20:34:29
<!-- agente: f464f5c6-420c-4baf-b9fe-19f1041be3bb -->

Sí, eso ya pasa: la versión 51.1.0 queda en el `CHANGELOG.md`, y cada proyecto ve el aviso de desfase y actualiza la plantilla.

Mi duda es otra: lo que dice la fila. En otro proyecto, «Análisis 11, acuerdo 5» busca el análisis 11 de ese proyecto, que no es el nuestro o no existe.

Propongo que la fila cite la regla del estándar que obliga a pasar el pendiente, y crear esa regla en la HU-003, que ya trata el tema. ¿Le parece?

### 508 · Usuario, 2026-10-03 20:35:11
> explique a un niño

**Agente**, 2026-10-03 20:35:18
<!-- agente: 4e6875d3-08b6-4ebf-bec2-79d0ee57c5af -->

Es como una tarea que dice «ver el cuaderno de Pedro, página 11». En el salón de Pedro sirve, porque todos saben cuál es ese cuaderno. En otro salón, nadie tiene el cuaderno de Pedro.

La plantilla les llega a todos los proyectos y dice «Análisis 11, acuerdo 5». Ese análisis es nuestro cuaderno; los demás proyectos no lo tienen.

Lo que propongo es que la plantilla diga «la regla del estándar», que es un libro que tienen todos.

### 509 · Usuario, 2026-10-03 20:36:04
> apruebo

**Agente**, 2026-10-03 20:36:31
<!-- agente: 20587c12-03d5-4aa8-a4c3-3f76b199802e -->

Quedó como acuerdo 3 del análisis 14 y va a la HU-003: se crea la regla del estándar, y la plantilla la cita en lugar del análisis 11. Hasta que esa regla exista, la plantilla sigue citando el análisis 11.

Lo que queda abierto en el análisis 14:
- **Corregir `origen.py`**, para que entienda «Análisis N, acuerdo M» y se corra antes de aprobar.

¿Lo aprueba, para llenar el análisis?

### 510 · Usuario, 2026-10-03 20:36:32
> corrija de una

**Agente**, 2026-10-03 20:40:20
<!-- agente: f911f488-2cea-40d2-b431-8dad23928791 -->

Registro el acuerdo y sus rutas en el análisis 14.

Ahora `origen.py`.

Las pruebas de aprobación usan análisis armados desde la plantilla, con sus marcadores sin llenar, y ahora la revisión de origen los rechaza. Reviso cuáles son.

Agrego a la base de esas pruebas un paso que llena lo mínimo del análisis antes de aprobarlo.

Las 61 pruebas pasan. Sumo `origen.py` a la entrada 51.1.0 del registro de cambios.

Listo:
- **`origen.py`** entiende «Análisis N, acuerdo M». El análisis 13 ya pasa sin reescribirlo, y `origen` no da fallas en todo el repositorio.
- **«Apruebo el análisis»** corre esa revisión antes de poner la marca. Si encuentra una falla, no aprueba y dice cuál.
- **Pruebas:** las 61 de los programas que cambié pasan. Todo queda en la versión 51.1.0.

Queda un riesgo. Hasta que se cree la regla del acuerdo 3, la fila 1 de la plantilla cita «Análisis 11, acuerdo 5». En otro pendiente ese análisis no existe, y ahora el análisis no se podrá aprobar. Por eso recomiendo construir el acuerdo 3 antes de abrir análisis en otros pendientes.

Para cerrar este: «Escriba» y lleno el análisis 14.

### 511 · Usuario, 2026-10-03 20:43:11
> 
> Escriba, pero no voy a cerrar el análisis. Desde aquí vamos a continuar ejecutando lo que falta, porque ya están surgiendo demasiados análisis.

**Agente**, 2026-10-03 20:45:25
<!-- agente: cb3ebe6c-bf1a-4346-b569-1de9f3be5e57 -->

Ahora las secciones que siguen a lo acordado.

Escribí el [análisis 14](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-14.md) y pasé el pendiente 103 a la V6, con el H-18. Si se pidiera la aprobación ahora, la revisión no encontraría nada que le falte, pero lo dejo abierto, como pidió. También registré las lecciones S-282 a S-284.

Para seguir ejecutando, primero necesito estas aprobaciones:
1. **Los CA nuevos:** CA-10 y CA-11 en la HU-003, y CA-05 y CA-06 en la HU-007.
2. **Los planes ya escritos:** la fase B de la HU-003 y la fase B de la HU-004.

Con «Apruebo» arranco por la fase B de la HU-003.

### 512 · Usuario, 2026-10-03 20:46:01
> apruebo

**Agente**, 2026-10-03 20:47:17
<!-- agente: 56f12f23-82dc-4190-827d-f89a962b1107 -->

Registro las aprobaciones en las HU y en los dos planes.

Ahora la T-01 en `analisis_en_curso.py`.

Me detuve en la T-01. La regla nueva funciona, pero una prueba que ya existía falla: `test_analisis_en_curso.py` arma un análisis 2 sin hallazgo, y la regla nueva lo rechaza, como pide el plan.

Para que pase, a esa prueba hay que darle un hallazgo y su pendiente. Ese archivo no está en el plan de la fase B de la HU-003.

Propongo pasar el plan a su versión 2 sumando `validadores/tests/test_analisis_en_curso.py`, y seguir.

### 513 · Usuario, 2026-10-03 20:52:19
> Explique no entiendo el problema

**Agente**, 2026-10-03 20:52:31
<!-- agente: 98c83493-7729-4b6d-8b75-33c6be0146ab -->

La regla nueva dice que, para aprobar un análisis, su hallazgo tiene que estar en el pendiente.

Hay una prueba vieja que finge aprobar un análisis sin hallazgo, como un examen de práctica con la hoja en blanco. Antes pasaba; con la regla nueva, falla, y eso es lo correcto.

Para arreglarla hay que escribirle un hallazgo de práctica a esa prueba. Esa prueba está en un archivo que el plan no dice que se va a tocar, y por eso me detuve.

Propongo agregar ese archivo al plan y seguir. Para eso: «Apruebo».

### 514 · Usuario, 2026-10-03 20:53:17
> Pregunta pero es de esta epica?

**Agente**, 2026-10-03 20:53:28
<!-- agente: 88fa172c-dd00-443d-b326-9a88dcdb2be5 -->

Sí. Esa prueba es de la HU-001 de esta misma épica, la EP-023, y la que falla la agregué hoy en el análisis 14.

Por eso detiene: es de la épica y, para cerrar la fase, obliga a tocar un archivo que el plan no declara (acuerdo 1 del análisis 12).

### 515 · Usuario, 2026-10-03 20:54:02
> Pregunta: qué archivo?

**Agente**, 2026-10-03 20:54:09
<!-- agente: 756d3772-fbf4-4b62-bec4-f66942eb6427 -->

El archivo es [`validadores/tests/test_analisis_en_curso.py`](../../../../../validadores/tests/test_analisis_en_curso.py), y la prueba que falla es `test_la_fila_puede_citar_el_acuerdo_de_otro_analisis`.

### 516 · Usuario, 2026-10-03 20:55:13
> Y para qué ese archivo?

**Agente**, 2026-10-03 20:55:19
<!-- agente: 98bacd85-5b5a-42e1-92e4-0b0b26cc5665 -->

Falta la palabra que dice qué espera; por ejemplo, «Pregunta: ...».

### 517 · Usuario, 2026-10-03 20:55:48
> pregunta

**Agente**, 2026-10-03 20:55:55
<!-- agente: a5f32647-e168-485c-ae93-2e1ed5ef78e3 -->

Ese archivo guarda las pruebas del programa que aprueba los análisis. Cada prueba arma un análisis de práctica y revisa que «Apruebo el análisis» lo acepte o lo rechace cuando corresponde. Así se sabe que el programa sigue funcionando después de cada cambio.

### 518 · Usuario, 2026-10-03 20:56:37
> explique: no entiendo por que ahora falla

**Agente**, 2026-10-03 20:56:45
<!-- agente: c773c820-8445-4b63-8d21-f7b498cfb597 -->

Porque cambió lo que se pide para aprobar.

- **Antes:** para aprobar un análisis bastaba con que tuviera sus secciones. La prueba armaba un análisis 2 de práctica sin hallazgo, y se aprobaba.
- **Ahora:** con la regla nueva de esta fase, un análisis 2 o posterior también tiene que tener su hallazgo, y ese hallazgo tiene que estar en el pendiente. El análisis de práctica no tiene ninguno, así que ya no se aprueba.

La prueba esperaba que se aprobara y ahora no se aprueba. Por eso falla. La regla funciona bien; lo que quedó viejo es el análisis de práctica.

### 519 · Usuario, 2026-10-03 20:57:18
> Cuál regla nueva?

### 520 · Usuario, 2026-10-03 20:57:35
> pregunta: Cuál regla nueva?

**Agente**, 2026-10-03 20:57:47
<!-- agente: 3d27cf17-a08c-465c-9a8d-d27e68dfa84a -->

Es el CA-09 de la HU-003, que estoy construyendo en esta fase (tarea T-01). Sale del acuerdo 5 del análisis 11: un análisis del número 2 en adelante no se aprueba si su hallazgo no está en «De dónde sale» del pendiente.

La acabo de agregar en [`validadores/analisis_en_curso.py`](../../../../../validadores/analisis_en_curso.py), como la función `hallazgo_en_el_pendiente`.

### 521 · Usuario, 2026-10-03 20:59:00
> pregunta: osea ya fue solucionado

**Agente**, 2026-10-03 20:59:08
<!-- agente: 50118c74-274e-4d57-9275-bff76550c793 -->

Todavía no. La regla ya está escrita y funciona, pero la fase no cierra por dos cosas:
1. La prueba vieja de práctica falla, y arreglarla toca un archivo que el plan no declara. Para eso necesito su «Apruebo».
2. Falta la T-02: las pruebas nuevas, la fila en la HU y la versión 52.0.0.

### 522 · Usuario, 2026-10-03 21:00:30
> pregunta: cuál prueba vieja?

**Agente**, 2026-10-03 21:00:38
<!-- agente: a96d7ea9-3d07-4d6d-96d0-cbb73506e579 -->

Es `test_la_fila_puede_citar_el_acuerdo_de_otro_analisis`, en [`validadores/tests/test_analisis_en_curso.py`](../../../../../validadores/tests/test_analisis_en_curso.py).

Me corrijo: no es vieja. La escribí hoy, en el análisis 14 (acuerdo 4), para probar las citas a otro análisis. Al escribirla no le puse hallazgo al análisis de práctica.

### 523 · Usuario, 2026-10-03 21:01:32
> explique cuál es el problema

**Agente**, 2026-10-03 21:01:45
<!-- agente: 6d2b8faf-23eb-4410-bb5b-4764e939ef9c -->

El problema es pequeño y lo causé yo:

1. Hoy, en el análisis 14, escribí una prueba que arma un análisis 2 de práctica sin hallazgo.
2. Ahora, en esta fase, construí la regla de que un análisis 2 sin hallazgo no se aprueba.
3. La regla rechaza el análisis de práctica de mi prueba, así que la prueba falla.

Se arregla agregándole un hallazgo al análisis de práctica: dos líneas. Lo único que me detuvo es que ese archivo no está en el plan de esta fase.

### 524 · Usuario, 2026-10-03 21:02:20
> pregunta: cómo así que un análisis 2?

**Agente**, 2026-10-03 21:02:28
<!-- agente: 5ede2cbc-63e2-4b34-a5c3-8f872fbe3ab4 -->

No es uno de nuestros análisis. Es un archivo de mentira que la prueba crea en una carpeta temporal y borra al terminar. Lo llamé `analisis-2.md` porque quería probar que un análisis cita el acuerdo de otro anterior, el `analisis-1.md` de mentira.

### 525 · Usuario, 2026-10-03 21:03:10
> pregunta: por qué tiene que estar haciendo eso?

**Agente**, 2026-10-03 21:03:18
<!-- agente: 30e8ed37-d9c6-4693-9267-7827b576a5df -->

La prueba ensaya el programa con análisis de mentira para no tocar los análisis de verdad.

Si se probara contra el análisis 13 o el 14 reales, un error podría ponerles la marca de aprobado o dañarlos. Con un análisis de mentira, la prueba ve si «Apruebo el análisis» acepta lo que debe aceptar y rechaza lo que debe rechazar, sin arriesgar nada.

### 526 · Usuario, 2026-10-03 21:04:06
> pregunta por que análisis de mentira luego no tiene 14?

**Agente**, 2026-10-03 21:04:15
<!-- agente: 028aea19-6482-44bc-9844-1f7ada72878a -->

Porque las pruebas no pueden usar los análisis de verdad, por tres razones:

1. **Los dañarían.** Una prueba aprueba y rechaza análisis. Si usara el análisis 14 real, le pondría la marca de aprobado sin que usted lo apruebe.
2. **Cambian.** El análisis 14 se sigue escribiendo, así que una prueba que dependa de él fallaría cada vez que cambie.
3. **Tienen que servir en cualquier proyecto.** En otros proyectos no hay análisis 14. Las pruebas viajan con el estándar y arman lo que necesitan.

### 527 · Usuario, 2026-10-03 21:06:11
> analicemos: pero por hacer eso mire lo que está pasando no me da solución me paró lo que estaba haciendo

**Agente**, 2026-10-03 21:06:26
<!-- agente: fc943abf-599b-41b4-a31d-97371c55c1ea -->

Tiene razón: lo paré por algo que tenía solución ahí mismo.

Esa prueba la escribí hoy en el análisis 14, y su fila 4 ya autoriza tocar ese archivo de una (`validadores/tests/test_analisis_en_curso.py`). Además, el acuerdo 45 del análisis 1 dice que un error dentro de lo ya aprobado no es hallazgo: se corrige y se sigue.

**Solución:** le agrego el hallazgo de práctica a esa prueba bajo la fila 4 del análisis 14, y sigo con la fase B de la HU-003 sin cambiar su plan.

¿Lo hago?

### 528 · Usuario, 2026-10-03 21:07:11
> apruebo

**Agente**, 2026-10-03 21:12:29
<!-- agente: 94fa680d-9eba-4ea9-8a9b-3ec752158b6b -->

Ahora la T-02: las pruebas de la fase.

Las 35 pruebas pasan. Ahora el cierre: la fila en la HU, la versión 52.0.0 y los documentos de la fase.

Actualizo el estado de la fase y corro los validadores.

La fase B de la HU-003 quedó hecha. Sigo con la fase B de la HU-004, cuyo plan también aprobó.

Estoy cerrando la fase B de la HU-004. El validador del estándar marca una falla en las reglas que cambié; la reviso.

Las dos fases quedaron construidas y sin fallas:

- **Fase B de la HU-003** (versión 52.0.0): «Apruebo el análisis» no pone la marca si el hallazgo falta en el pendiente. Sus 6 pruebas pasan, junto con las del programa que cambió.
- **Fase B de la HU-004** (versión 52.1.0): `02·F9`, `13·DOC24` y la plantilla dicen que solo detiene el hallazgo que obliga a salirse del plan.

`estandar`, `flujo` y `origen` no dan fallas.

**Lo que falta, en orden:**
1. Su aprobación de las dos fases y del commit de todo lo de hoy (se pregunta aparte).
2. Escribir los planes de los criterios nuevos:
   - HU-003: CA-10, CA-11 y la regla del acuerdo 3 del análisis 14;
   - HU-007: CA-05 y CA-06.
3. La fase C de la HU-007.
4. El pendiente 109.

### 529 · Usuario, 2026-10-03 21:13:07
> Pregunta: qué sigue?

**Agente**, 2026-10-03 21:13:17
<!-- agente: c7b4301a-ad24-4864-8a62-0191e82091a8 -->

Sigue que apruebe las dos fases que terminé, la B de la HU-003 y la B de la HU-004. Para eso: «Apruebo».

Después le pregunto aparte por el commit, y luego escribo los planes de los criterios nuevos de la HU-003 y la HU-007.

### 530 · Usuario, 2026-10-03 21:13:27
> Apruebo

**Agente**, 2026-10-03 21:13:46
<!-- agente: 640b0dfd-5816-4b11-a67c-462a2383499c -->

Registro la aprobación en las dos fases.

Quedó registrado: las dos fases aparecen como aprobadas por usted el 2026-10-03.

¿Hago el commit de todo lo de hoy? Entrarían las versiones 51.1.0, 52.0.0 y 52.1.0, los análisis 13 y 14, el pendiente en la V6, las HU y las dos fases. Quedan fuera los archivos de otras sesiones: la auditoría `2026-10.md` y la sesión y los resúmenes del 2026-09-30.

Para hacerlo: «Apruebo el commit».

### 531 · Usuario, 2026-10-03 21:14:13
> Apruebo el commit y suba a git

**Agente**, 2026-10-03 21:14:56
<!-- agente: d59f7e80-1e52-4353-9086-251c6dbb51ae -->

El commit no entró. El control previo al commit encontró el signo «...», escrito como un solo carácter, en las conversaciones de los análisis 13 y 14: 2 en el 13 y 6 en el 14. Salieron de mis respuestas, por ejemplo «Analicemos: ...», y la regla `00·ID8` no lo deja pasar.

Para que entre hay que cambiar ese carácter por tres puntos sueltos («...») en los dos análisis. El 13 ya está aprobado y no se reescribe, pero el cambio no toca lo que dice, solo cómo está escrito el signo.

¿Hago ese cambio en los dos y repito el commit y la subida? Para eso: «Apruebo».

### 532 · Usuario, 2026-10-03 21:16:55
> Apruebo

**Agente**, 2026-10-03 21:17:31
<!-- agente: 156980b9-4e7d-4040-96cb-e95486329813 -->

El commit volvió a fallar, ahora por otra razón. Ya quité los «...»: eran 2 en el 13 y 8 en el 14.

**Qué pasó:** el control del commit revisa cada archivo contra los planes de las fases en curso. Tres archivos que cambié «de una» por el análisis 14 no están en ningún plan:
- `validadores/origen.py`
- `validadores/tests/test_origen.py`
- `validadores/tests/test_analisis_en_curso.py`

El freno sí deja pasar las rutas «de una» del análisis prendido, pero el control del commit no las lee. Los dos guardias usan listas distintas.

**Propuesta:** que el control del commit acepte también las rutas «de una» del análisis prendido, igual que el freno. Lo corrijo de una, como acuerdo 5 del análisis 14, y repito el commit y la subida.

¿Lo apruebo así?

### 533 · Usuario, 2026-10-03 21:18:17
> pues aplique las reglas de corrección ya nos ha pasado varias veces

**Agente**, 2026-10-03 21:20:34
<!-- agente: 98e52817-5036-43b7-aed2-a92de1ded32c -->

Registro el acuerdo 5 y su fila «de una» en el análisis 14, y aplico la corrección.

Listo: el commit `372c94e` quedó en GitHub.

Para que entrara hice dos correcciones de una, registradas como acuerdo 5 del análisis 14:
- **El control del commit** ahora acepta las rutas «de una» del análisis prendido, igual que el freno (versión 52.1.1). Las 31 pruebas del commit y del freno pasan.
- **Los «...» de los análisis 13 y 14** quedaron como «...».

Quedan dos cosas sin guardar:
- **Los estados de las dos fases**, donde el control anotó el commit. Entran en el commit siguiente.
- **Un riesgo que se va a repetir.** El análisis 14 copia la conversación desde la transcripción, y ahí siguen los «...» de mis respuestas. En el próximo commit volverán a aparecer, a menos que la copia los limpie. Propongo que el programa que copia la conversación cambie «...» por «...» al copiarla, como ya cambia la raya larga por coma.

### 534 · Usuario, 2026-10-03 21:21:16
> pregunta: qué sigue?

**Agente**, 2026-10-03 21:21:24
<!-- agente: ddebc629-0cbf-4ca0-83c9-676e20449134 -->

Lo que sigue, en orden:

1. **Decidir lo de los «...».** Propongo que la copia de la conversación los cambie por «...», para que el próximo commit no vuelva a fallar.
2. **Escribir los planes de los criterios nuevos:**
   - HU-003: CA-10, CA-11 y la regla del acuerdo 3 del análisis 14.
   - HU-007: CA-05 y CA-06.
3. **La fase C de la HU-007:** la integración continua y el contrato de cada adaptador.
4. **El pendiente 109** de la EP-005.

Para el punto 1: «Apruebo». Para el punto 2: «Escriba».

### 535 · Usuario, 2026-10-03 21:21:58
> Apruebo, solucione de una

**Agente**, 2026-10-03 21:22:57
<!-- agente: 2512ab71-e4c5-479e-9645-eb99879aef67 -->

Listo, versión 52.1.2. Cuando la conversación se copia al análisis, los «...» ahora pasan a «...», igual que la raya larga pasa a coma. Lo registré como acuerdo 6 del análisis 14. Las 33 pruebas de ese programa pasan.

No he hecho commit de este cambio. Entrará con el siguiente, junto con los estados de las dos fases.

Lo que sigue son los planes de los criterios nuevos de la HU-003 y la HU-007. Para escribirlos: «Escriba».

### 536 · Usuario, 2026-10-03 21:24:28
> Escriba

**Agente**, 2026-10-03 21:28:24
<!-- agente: 14b57285-05ef-4df2-b340-7bff74458e7c -->

Estoy escribiendo los dos planes. Antes reviso dónde se copia `13·DOC22` y qué dice el freno al detener.

Escribo los documentos de la fase C de la HU-003.

Ahora la fase de la HU-007.

Escribí los planes de dos fases nuevas. Cada una tiene su plan de pruebas y su estado. Los validadores `flujo` y `origen` no encuentran fallas, y la revisión de redacción tampoco deja marcas.

**[Fase C de la HU-003](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera/plan_trabajo.md)** (CA-10 y CA-11), versión 53.0.0:
- `02·F24` dirá que el reporte nace en la HU de origen o, si no la hay, en el resumen del día.
- Un programa nuevo, `aviso_resuelto.py`, dejará el aviso de resuelto al lado del pendiente de seguimiento del proyecto cuando se anote el commit.
- El seguimiento cerrará solo cuando el proyecto cambie «Comprobado: no» por la fecha.

**[Fase C de la HU-007](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-007-nada-se-escribe-fuera-del-plan-aprobado/C-EP-023-HU-007-el-freno-respeta-el-analisis-prendido-y-las-comillas/plan_trabajo.md)** (CA-05 y CA-06), versión MENOR:
- Con un análisis prendido, el freno detiene la acción pero no anota en el resumen; `13·DOC22` lo dirá.
- El freno dejará de tomar por escritura un `>` que esté entre comillas.

Decidí dos cosas que conviene revisar antes de aprobar:
- La integración continua, que antes se anunciaba como fase C de la HU-007, pasa a la fase D.
- La regla del acuerdo 3 del análisis 14 queda fuera de estos planes, porque su CA nace cuando ese análisis se apruebe.

Para aprobar los dos planes: «Apruebo».

### 537 · Usuario, 2026-10-03 21:29:05
> Apruebo

**Agente**, 2026-10-03 21:37:12
<!-- agente: f3f28fc6-dc73-4fea-8928-2bdf73229e70 -->

T-02 y T-03 hechas. Sigue la T-04: veo `pendientes.estado()` y el plan.

Cambio `estado()`: el seguimiento cierra con el padre y el aviso comprobado.

Sigo con lo que sí está en el plan: las pruebas nuevas.

Lo nuevo funciona: las 6 pruebas de la fase pasan (CP-002 y CP-003). Pero el freno paró una corrección, y no me toca decidirla a mí.

**Lo que pasó:** ahora el pendiente de seguimiento solo cierra cuando el proyecto pone la fecha en «Comprobado» del aviso. Eso lo pide el CA-11. Una prueba vieja, [test_el_pendiente_tiene_solo_lo_suyo.py:131](../../../../../validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py#L131), espera la regla anterior: que cierre apenas cierra el padre. Por eso falla. Ese archivo no está en el plan, así que el freno no me dejó tocarlo.

**Propuesta:** agregar ese archivo a la 2.1 del plan, aprobado en su versión 2. El cambio en la prueba es pequeño: antes del «cerrado», espera «abierto» y escribe el aviso con la fecha. No volví a tocar el plan por mi cuenta.

**¿Lo apruebas?**

Si dices que sí, falta:
1. Esa prueba.
2. `mapa_tareas.py`.
3. El mapa del sitio y la fila de la fase en la HU.
4. `CHANGELOG` y `VERSION` en 53.0.0.
5. El resultado, la funcionalidad y el estado de la fase.
6. Tu aprobación de las fases C y, aparte, del commit.

### 538 · Usuario, 2026-10-03 21:39:31
> 
> explique el problema

**Agente**, 2026-10-03 21:39:43
<!-- agente: cbfc4303-bdd2-4784-bdf5-7249796d8b85 -->

El cambio nuevo hace bien su trabajo, pero una prueba vieja espera lo contrario.

- **Antes:** el pendiente que el proyecto deja para seguir el reporte cerraba apenas el estándar arreglaba el problema.
- **Ahora (CA-11):** cierra solo cuando el proyecto revisa el arreglo y pone la fecha en «Comprobado».
- **La prueba vieja** ([test_el_pendiente_tiene_solo_lo_suyo.py:131](../../../../../validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py#L131)) espera la regla de antes. Por eso ahora falla.
- **Por qué no la arreglé:** la corrección es un cambio pequeño, pero ese archivo no está en el plan, y el freno solo deja tocar lo que el plan nombra.

Falta aprobar que ese archivo entre al plan.

### 539 · Usuario, 2026-10-03 21:40:20
> 00 id9

**Agente**, 2026-10-03 21:40:26
<!-- agente: 2d643d6d-c0de-48af-9da6-a017c467b72d -->

Una prueba vieja espera que el seguimiento cierre sin comprobación. Ahora necesita la comprobación, así que falla. Para corregirla, primero hay que agregarla al plan.

### 540 · Usuario, 2026-10-03 21:40:45
> pregunta: cual prueba vieja?

**Agente**, 2026-10-03 21:40:54
<!-- agente: 5354563a-a6aa-43b8-a597-eb3ed733a20f -->

La prueba es `test_toma_el_estado_de_su_padre`, en [test_el_pendiente_tiene_solo_lo_suyo.py:131](../../../../../validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py#L131). Es de la fase A de la HU-003.

### 541 · Usuario, 2026-10-03 21:41:24
> pregunta: en qué falla esa prueba?

**Agente**, 2026-10-03 21:41:31
<!-- agente: 645dc609-5064-40e7-ad45-c7d7538cf6b0 -->

La prueba arma un pendiente de seguimiento y cierra su padre. Después espera que el seguimiento dé «cerrado», pero ahora da «abierto». Da «abierto» porque falta el aviso con la fecha en «Comprobado».

### 542 · Usuario, 2026-10-03 21:42:26
> cuál es la solución?

**Agente**, 2026-10-03 21:42:33
<!-- agente: c0b72538-a9b1-4123-98b8-c8d0f29e2d89 -->

Falta la palabra que dice qué se espera (por ejemplo, «Pregunta»).

### 543 · Usuario, 2026-10-03 21:42:40
> Pregunta

**Agente**, 2026-10-03 21:42:50
<!-- agente: cbcc0910-be62-412f-8ff0-b7a977ae5c47 -->

La solución es agregar a la prueba el paso que falta: escribir el aviso con la fecha en «Comprobado». Así la prueba vuelve a esperar «cerrado» y pasa.

Para hacerlo, primero hay que meter ese archivo de pruebas en la sección 2.1 del plan de la fase, con aprobación.

### 544 · Usuario, 2026-10-03 21:43:29
> pregunta y por qué en los anteriores no falló?

**Agente**, 2026-10-03 21:43:38
<!-- agente: d5656a3b-780e-40b5-ba61-90c0d89a18d5 -->

Antes no fallaba porque la regla vieja cerraba el seguimiento junto con el padre, y la prueba esperaba justo eso. La regla cambió en esta fase, con la T-04.

Lo que sí falló fue el plan. Al buscar qué pruebas leen `pendientes.py`, solo nombró las de `validadores/pruebas.py` y se le pasó este archivo.

### 545 · Usuario, 2026-10-03 21:44:19
> pregunta: qué soluciona el problema?

**Agente**, 2026-10-03 21:44:30
<!-- agente: 2602604b-b17f-470b-bdb9-9a08347f67d0 -->

Hay dos niveles:

- **Para hoy:** agregar el archivo a la 2.1 del plan y escribir en la prueba el aviso con la fecha en «Comprobado».
- **Para que no se repita:** al hacer el plan, buscar en todas las pruebas cuáles usan la función que cambia (aquí, `pendientes.estado`). Hoy el plan solo revisó `validadores/pruebas.py`.

### 546 · Usuario, 2026-10-03 21:44:54
> pregunta: cuál archivo?

**Agente**, 2026-10-03 21:45:06
<!-- agente: facccd0b-1b6e-4888-9426-39ca3152df3a -->

Es [validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py](../../../../../validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py).

Hay otras cinco pruebas que llaman una función `estado`, pero no las he corrido con el cambio. Toca correrlas para saber si alguna más espera la regla vieja.

### 547 · Usuario, 2026-10-03 21:46:03
> pregunta y qué soluciona?

**Agente**, 2026-10-03 21:46:11
<!-- agente: d0a4f261-6566-4c26-a765-65f4cdfbbd2a -->

Ese archivo tiene las pruebas de la fase A de la HU-003. Comprueban que el pendiente tenga solo sus tres partes, que el plan calcule su cierre, que el hallazgo calcule su estado y que el seguimiento cierre junto con su padre.

Lo último cambió en esta fase. Por eso hay que actualizar esa prueba.

### 548 · Usuario, 2026-10-03 21:47:00
> entonces no podemos seguir?

**Agente**, 2026-10-03 21:47:06
<!-- agente: 13e6fabd-fff4-4fb9-aebb-bf438c85492b -->

Falta la palabra que dice qué se espera (por ejemplo, «Pregunta»).

### 549 · Usuario, 2026-10-03 21:47:10
> pregunta

**Agente**, 2026-10-03 21:47:18
<!-- agente: 46f48df0-f598-4a6b-8de1-192ee37d72b9 -->

Sí se puede seguir. Hay dos caminos y los dos necesitan un «Apruebo»:

- **Recomendado:** agregar el archivo a la 2.1 del plan, que pasa a su versión 2, y corregir la prueba.
- **Otra opción:** anotarlo en el análisis 14, que está prendido, como fila «de una y sin fase». Así se hizo con la prueba que falló antes.

Con cualquiera de los dos se termina la fase.

### 550 · Usuario, 2026-10-03 21:48:26
> apruebo: anotarlo en el análisis 14

**Agente**, 2026-10-03 22:06:32
<!-- agente: 57841ccf-c801-4e09-8422-b813a3d45a58 -->

Leo el análisis 14 para agregar la fila.

Fila 8 anotada y prueba corregida. Ahora corro las pruebas que llaman `estado`.

El plan nombró `trabajar-cadena-2.md`, pero la copia de `02·F24` quedó en `trabajar-cadena-1.md`. Mientras tanto avanzo con lo que el plan sí nombra.

Falta el resultado de las pruebas de la fase. Lo escribo con el formato de la fase C de la HU-007.

Ahora el estado de la fase.

Terminé la fase C de la HU-003: el estándar queda en la 53.0.0. Sus 6 pruebas pasan, igual que las 67 que llaman una función `estado`, y los validadores `estandar`, `tareas`, `flujo` y `origen` no muestran fallas.

Quedan tres cosas para revisar en el análisis 14:

1. **`base/reglas-por-tarea/trabajar-cadena-1.md`:** `mapa_tareas.py` copió `02·F24` en ese archivo, pero el plan nombró `trabajar-cadena-2.md`. El control del commit lo va a rechazar. Se arregla con una fila «de una», como la de la prueba.
2. **`validadores/pruebas.py`:** falla 1 de 571 pruebas, `test_limites_sin_la_carpeta_es_falla`. No la causó esta fase. Espera que la falta de `pendientes/` sea falla, y desde la 45.0.0 no lo es.
3. **El freno:** detuvo un `sed` porque tomó el texto entre barras como un archivo. Hice el mismo cambio con el editor.

Falta aprobar las fases C de la HU-003 y de la HU-007, y los puntos 1 y 2. El commit se aprueba aparte.

### 551 · Usuario, 2026-10-03 22:06:59
> 00 id9

**Agente**, 2026-10-03 22:07:07
<!-- agente: 054ed567-9418-4461-ab94-2c64bf27537f -->

La fase C de la HU-003 está construida, en la 53.0.0, y las pruebas pasan.

Faltan tres cosas:
1. `trabajar-cadena-1.md` no está en el plan y el commit lo rechazaría. Se arregla con una fila «de una» en el análisis 14.
2. Falla una prueba vieja de `pruebas.py` que esta fase no causó.
3. El freno confundió un `sed` con una escritura.

Hace falta aprobar las fases C de la HU-003 y la HU-007, y los puntos 1 y 2.

### 552 · Usuario, 2026-10-03 22:07:39
> apruebo

**Agente**, 2026-10-03 22:13:24
<!-- agente: e47073c8-7de7-4479-8360-6fc8ccb4ef53 -->

Marco las dos fases como aprobadas y anoto los puntos 1 y 2 en el análisis 14.

Ahora corrijo la prueba vieja de `pruebas.py`.

Dejé aprobadas las fases C de la HU-003 y de la HU-007.

- **Punto 1:** `trabajar-cadena-1.md` quedó anotado como fila 9 del análisis 14.
- **Punto 2:** la prueba vieja de `pruebas.py` ya está al día (fila 10). Ahora pasan las 571.
- **Validadores:** `estandar` y `origen` no muestran fallas.

¿Hago el commit y lo subo? Los dos archivos de otras sesiones se quedan por fuera.

### 553 · Usuario, 2026-10-03 22:13:54
> hágalo

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. La plantilla del análisis, de una: «Lo que se tiene que hacer» trae ya escrita la fila que pasa el pendiente a su versión siguiente, citando el análisis 11, acuerdo 5, y su nota dice las dos formas de citar el origen: un número es un acuerdo de este análisis, y «Análisis N, acuerdo M» es el de otro análisis del mismo pendiente (turnos 496 a 498).
2. El freno lee las rutas «de una» también en «Pasó a», donde las escriben los análisis, y se corrige de una. El H-19, que anotó al detener el cambio de la plantilla con este análisis prendido, sale del resumen (turnos 499 a 505).
3. La plantilla la usan todos los proyectos, y «Análisis 11, acuerdo 5» solo existe en este repositorio. Se crea una regla del estándar que obliga a pasar el pendiente a su versión siguiente, y la fila 1 de la plantilla la cita en lugar del análisis 11. Va a la HU-003, que ya trata el tema (turnos 506 a 510).
4. `origen.py` entiende «Análisis N, acuerdo M» como un acuerdo de otro análisis del mismo pendiente, y «Apruebo el análisis» corre esa revisión antes de poner la marca: si falla, no aprueba y dice qué falta. Se corrige de una (turnos 488 a 494 y 511).
5. El control del commit acepta también las rutas «de una» del análisis prendido, igual que el freno: los dos guardias usan la misma lista. Se corrige de una (turnos 531 a 533).
6. Al copiar la conversación al análisis, los puntos suspensivos de un solo carácter pasan a tres puntos, como la raya larga pasa a coma: así el commit no los rechaza. Se corrige de una (turnos 534 y 535).
7. La prueba de la fase A de la HU-003 que espera que el seguimiento cierre con su padre se pone al día con el CA-11: espera también el aviso con la fecha en «Comprobado». El plan de la fase C no la nombró, y se corrige de una aquí (turnos 538 a 550).
8. La copia de `02·F24` que escribe `mapa_tareas.py` quedó en `base/reglas-por-tarea/trabajar-cadena-1.md`, no en la `-2` que nombró el plan de la fase C. Entra de una aquí (turnos 550 a 552).
9. La prueba `test_limites_sin_la_carpeta_es_falla` de `validadores/pruebas.py` espera que la falta de `pendientes/` sea falla, y desde la 45.0.0 no lo es. Se pone al día de una aquí (turnos 550 a 552).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F27` (cada punto dice de dónde sale, y lo revisa `origen.py`), `02·F8` (el freno) y `20·M10` (versionar). Choca la plantilla con `20·M3`: una cita a un análisis de este repositorio no sirve en otros proyectos; lo resuelve el punto 5.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/origen.py` | Entendía «Análisis N, acuerdo M» en el plan, no en el análisis; revisaba solo el análisis aprobado. Corregido (punto 4) |
| `validadores/freno.py` | Leía las rutas «de una» en la primera columna; los análisis las escriben en «Pasó a». Corregido (punto 3) |
| `plantillas/analisis.md` | No traía la fila que pasa el pendiente a su versión siguiente. Corregido (punto 2); su cita queda para el punto 5 |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 11, acuerdo 5 | Cada análisis pasa el pendiente a su versión siguiente: por eso la fila se repite en todos |
| Análisis 13, acuerdo 6 | Con un análisis prendido no se crean hallazgos; el H-19 salió del resumen (acuerdo 2) |
| Lecciones S-282, S-283 y S-284 | Las de este análisis |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR, 51.1.0: la plantilla suma una fila y la aprobación revisa el origen. Lo ven en el aviso de desfase |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un análisis de otro pendiente o proyecto copia la fila 1 de la plantilla | Cualquier proyecto | «Apruebo el análisis» lo rechaza: el análisis 11 no existe ahí | Punto 5 |
| Un análisis cita el acuerdo de un análisis de otro pendiente | Cualquier proyecto | `origen.py` no lo encuentra | No hace falta: el acuerdo 4 se limita al mismo pendiente |
| Un error de origen en un análisis ya aprobado | Los análisis aprobados antes de 51.1.0 | No se pueden reescribir | Acuerdo 4: desde ahora se revisa antes de aprobar |

---

## Propuesta final: hallazgo y pendiente V6, épica y HU

> El H-18 no cambia. El pendiente 103 pasa a la V6.

### Pendiente V6. Lo que se construye se aparta de lo aprobado

| Campo | Valor |
|---|---|
| De dónde sale | Los de la V5, y el H-18 de la sesión del 2026-10-01, que abrió el análisis 14 |
| El problema | El de la V5, y además: el validador de origen no entendía la cita a un acuerdo de otro análisis y solo revisaba el análisis ya aprobado, y la plantilla del análisis no traía la fila que pasa el pendiente a su versión siguiente. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) | El hallazgo y el pendiente tienen solo lo que les corresponde | La plantilla cita un análisis que solo existe en este repositorio | HU-001 | Ya trata el paso del pendiente a su versión siguiente | 5 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Las rutas de una se escribieron sin mirar dónde las lee el freno | Falló | S-282 | complementa R-2 |
| 2 | El usuario pidió acortar las respuestas cuatro veces en un mismo análisis | Falló | S-283 | complementa R-17 |
| 3 | La plantilla citó un análisis que solo existe en este repositorio | Falló | S-284 | complementa R-12 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | Análisis 11, acuerdo 5 | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md`, hecho el 2026-10-03 |
| 2 | Que `plantillas/analisis.md` traiga la fila que pasa el pendiente a su versión siguiente y diga las dos formas de citar el origen, con su entrada en `CHANGELOG.md` y `VERSION` | 1 | Este análisis, de una y sin fase: `plantillas/analisis.md`, `CHANGELOG.md`, `VERSION`, hecho el 2026-10-03 |
| 3 | Que `validadores/freno.py` lea las rutas «de una» también en «Pasó a», con su prueba en `validadores/tests/test_el_freno.py`, y quitar el H-19 de `historico-chat/resumenes/2026-10-01/sesion.md` | 2 | Este análisis, de una y sin fase: `validadores/freno.py`, `validadores/tests/test_el_freno.py`, `historico-chat/resumenes/2026-10-01/sesion.md`, hecho el 2026-10-03 |
| 4 | Que `validadores/origen.py` entienda «Análisis N, acuerdo M» y que `validadores/analisis_en_curso.py` no apruebe un análisis con fallas de origen, con sus pruebas en `validadores/tests/test_origen.py` y `validadores/tests/test_analisis_en_curso.py`, y su entrada en `CHANGELOG.md` y `VERSION` | 4 | Este análisis, de una y sin fase: `validadores/origen.py`, `validadores/analisis_en_curso.py`, `validadores/tests/test_origen.py`, `validadores/tests/test_analisis_en_curso.py`, `CHANGELOG.md`, `VERSION`, hecho el 2026-10-03 |
| 6 | Que `validadores/plan_vs_hecho.py` acepte en el commit las rutas «de una» del análisis prendido, con su prueba en `validadores/tests/test_nada_fuera_del_plan.py`, y su entrada en `CHANGELOG.md` y `VERSION` | 5 | Este análisis, de una y sin fase: `validadores/plan_vs_hecho.py`, `validadores/tests/test_nada_fuera_del_plan.py`, `CHANGELOG.md`, `VERSION`, hecho el 2026-10-03 |
| 7 | Que `validadores/analisis_en_curso.py` cambie los puntos suspensivos de un solo carácter por tres puntos al copiar la conversación, con su prueba en `validadores/tests/test_analisis_en_curso.py`, y su entrada en `CHANGELOG.md` y `VERSION` | 6 | Este análisis, de una y sin fase: `validadores/analisis_en_curso.py`, `validadores/tests/test_analisis_en_curso.py`, `CHANGELOG.md`, `VERSION`, hecho el 2026-10-03 |
| 8 | Que la prueba del seguimiento en `validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py` espere el aviso con la fecha en «Comprobado» antes de dar el seguimiento por cerrado | 7 | Este análisis, de una y sin fase: `validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py`, hecho el 2026-10-03 |
| 9 | Que la copia de `02·F24` en `base/reglas-por-tarea/trabajar-cadena-1.md` entre con la fase C de la HU-003 | 8 | Este análisis, de una y sin fase: `base/reglas-por-tarea/trabajar-cadena-1.md`, hecho el 2026-10-03 |
| 10 | Que `test_limites_sin_la_carpeta_es_falla` en `validadores/pruebas.py` espere que la falta de `pendientes/` no sea falla | 9 | Este análisis, de una y sin fase: `validadores/pruebas.py`, hecho el 2026-10-03 |
| 5 | Crear la regla del estándar que obliga a pasar el pendiente a su versión siguiente, y que la fila 1 de la plantilla del análisis la cite en lugar del análisis 11 | 3 | EP-023, [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |

## Lo que aporta al análisis principal

**Resultado:** Aclara.

**Lo que suma al análisis principal:** Cada punto de un análisis puede salir de un acuerdo de otro análisis del mismo pendiente, y la aprobación revisa ese origen antes de poner la marca.
