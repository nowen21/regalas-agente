# Análisis 11: la prueba de la fase A fija cuántas reglas autorizan escribir

> **Aprobado** por el usuario el 2026-10-03, en el turno 434, con la versión 50.0.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 10](analisis-10.md), aprobado el 2026-10-03. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se buscan todos los casos en que una regla entra o sale, no solo el de la prueba que falló |
| R-2 | Se revisa lo que ya existe: la línea «Autoriza escribir» en cada regla y la marca de derogada en su título |
| R-6 | Se leen los acuerdos que llegan con cada mensaje y los análisis 1, 8 y 10 antes de proponer |
| R-7 | Lo que nadie pidió se pregunta acá, no se agrega al plan |
| R-14 | Se confirma con el usuario que el hallazgo que abre este análisis es el H-14 |
| R-15 | Se aplicó: la ejecución se detuvo al aparecer el hallazgo, antes de tocar otro archivo |
| R-17 | Cada respuesta se mide contra `00·ID9` antes de entregarla |
| R-3, R-4, R-5, R-8 a R-13, R-16 | No aplican mientras el análisis no cree ni cambie reglas o plantillas; se revisan si eso cambia |

---

## Hallazgo

### H-14 · El plan de la fase B de la HU-007 no declara la prueba que cuenta las reglas que autorizan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03, al ejecutar la T-03 de la fase `B` de la HU-007, `13·DOC15`, `13·DOC16` y `02·F23` sumaron su línea «Autoriza escribir». La prueba `test_las_diez_reglas_traen_su_linea` de la fase `A` exige exactamente diez reglas con esa línea y ahora falla con trece. Corregirla es tocar `validadores/tests/test_nada_fuera_del_plan.py`, que la tabla 2.1 del plan no declara. |
| Por qué importa | Es escribir fuera del plan aprobado, justo lo que la HU-007 viene a frenar. Si se corrige sin volver al análisis, el plan deja de ser lo que se aprobó. |

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

### 409 · Usuario, 2026-10-03 10:49:57
> pregunta: cuál es el hallazgo?

**Agente**, 2026-10-03 10:50:04
<!-- agente: 0b3dbf5b-b9a7-4239-892a-0566d28a7302 -->

El hallazgo es que el plan de la fase B de la HU-007 olvidó declarar un archivo que su propio trabajo obliga a cambiar.

La tarea T-03 sumó la línea «Autoriza escribir» a tres reglas más: `13·DOC15`, `13·DOC16` y `02·F23`. Ahora son trece las reglas que la traen. La fase A dejó una prueba que exige que sean exactamente diez, y por eso falla.

Para que vuelva a pasar hay que cambiar `validadores/tests/test_nada_fuera_del_plan.py`, pero ese archivo no está en la tabla de archivos del plan aprobado. Cambiarlo sin más sería escribir fuera del plan, que es justo lo que la HU-007 viene a impedir.

### 410 · Usuario, 2026-10-03 10:50:37
> pregunta: cuál archivo?

**Agente**, 2026-10-03 10:50:42
<!-- agente: 6976400f-9397-493d-a109-91d5dcb183f4 -->

Es [test_nada_fuera_del_plan.py](../../../../../validadores/tests/test_nada_fuera_del_plan.py). Son las pruebas de la fase A de la HU-007, y la que falla se llama `test_las_diez_reglas_traen_su_linea`: comprueba que haya exactamente diez reglas con la línea «Autoriza escribir». Con las tres de la T-03 ahora son trece.

### 411 · Usuario, 2026-10-03 10:51:12
> Explique: entiendo elproblema

### 412 · Usuario, 2026-10-03 10:51:39
> Explique: no entiendo el problema

**Agente**, 2026-10-03 10:51:44
<!-- agente: 3263b8e5-e2b3-4e55-aab2-efdfed82dd65 -->

Con un ejemplo sencillo:

La fase A dejó una alarma que revisa algo muy concreto: que haya exactamente diez reglas que dan permiso para escribir. Si encuentra un número distinto, suena.

La fase B, cumpliendo su plan, les dio permiso a tres reglas más, porque así lo pide el acuerdo 46. Ahora son trece y la alarma suena, aunque nada está mal: lo que quedó viejo es la alarma.

Ajustarla para que cuente trece es cambiar un número en el archivo de la alarma. Pero el plan aprobado no dice que se pueda tocar ese archivo, y tocarlo sin permiso es justo lo que el freno viene a impedir.

Por eso paré. Un análisis corto tiene que decidir si se agrega ese archivo al plan. Así lo recomiendo, porque el arreglo es parte del mismo trabajo.

### 413 · Usuario, 2026-10-03 11:22:52
> Analicemos: Si son reglas, no debería bloquearlas, porque precisamente son reglas y, para que llegaran a serlo, también pasaron por un análisis que fue aprobado.

**Agente**, 2026-10-03 11:23:09
<!-- agente: cb8f1cbb-41c0-433b-bab8-29d8105b94c3 -->

Tiene razón, y en eso no hay choque: las tres reglas no quedaron bloqueadas. Ya tienen su línea «Autoriza escribir» y el freno las respeta. Lo que falló es otra cosa: una prueba de la fase A que quedó mal escrita, porque exige que haya **exactamente** diez reglas con esa línea.

Esa prueba debería comprobar que las diez estén, no que no haya más. Escrita así, falla cada vez que una regla nueva gana su permiso, que es justo lo que el acuerdo 46 espera que pase.

**Propuesta:**
1. Corregir la prueba para que revise que esas diez reglas traen su línea, sin fijar el total.
2. Como el plan de la fase B no nombra ese archivo, el plan pasa a su versión siguiente y lo suma a su tabla. La ejecución sigue desde la T-04.

¿Se hace así?

### 414 · Usuario, 2026-10-03 11:29:00
> Analicemos: debe quedar a que cualquier regla que entre debe funcionar sin que sea rechazada o igual si sale

**Agente**, 2026-10-03 11:29:52
<!-- agente: 76ac6013-8ea0-48df-afee-1bb959f8091c -->

Antes de proponer reviso cómo se marca una regla derogada, porque «si sale» quiere decir que deja de autorizar sin que nada se rompa.

Con lo que pide, encontré otro hueco además de la prueba. Una regla «sale» cuando se deroga: se queda en `base/` con la marca `[DEROGADA…]` en su título. Hoy `autorizado.py` no mira esa marca, así que una regla derogada seguiría dando permiso para escribir.

**Propuesta, para que cualquier regla entre o salga sin romper nada:**
1. **Nada fijo.** La prueba deja de tener una lista de diez nombres. Lee las reglas de `base/` y comprueba que cada una con la línea «Autoriza escribir» aparezca en lo autorizado con sus mismas rutas. Si mañana entran o salen reglas, la prueba sigue pasando sin tocarla.
2. **La que sale deja de autorizar.** `autorizado.py` ignora la regla derogada, y una prueba lo comprueba con una regla de ejemplo.
3. **Cómo entra en el plan.** El plan de la fase B pasa a su versión siguiente y suma a su tabla `validadores/tests/test_nada_fuera_del_plan.py` y `validadores/autorizado.py`. La ejecución sigue desde la T-04.

¿Se toma así?

### 415 · Usuario, 2026-10-03 11:31:55
> Analicemos: debe haber un lugar donde se agregue o quite reglas si que se tenga que modificar el programa

**Agente**, 2026-10-03 11:32:05
<!-- agente: 804fd4da-2589-49fc-b148-fe5246704abb -->

Ese lugar ya existe: es **la regla misma**.

Así quedó decidido en la fase A de la HU-007, a partir del acuerdo 46 del análisis 1. Cada regla que da permiso lleva su línea «Autoriza escribir», y el programa arma la lista leyendo esas líneas. Se descartó una lista aparte porque repetiría en dos sitios lo que ya dice la regla.

Por eso, agregar o quitar un permiso nunca toca el programa:
- **Entra una regla:** se le pone su línea, como acabo de hacer con `13·DOC15`, `13·DOC16` y `02·F23`.
- **Sale una regla:** se deroga o se le quita la línea.

Lo que estaba mal no era el programa sino dos cosas:
- La prueba de la fase A, que tenía escritos a mano los diez nombres.
- `autorizado.py`, que no deja de leer una regla derogada.

Con la propuesta anterior se corrigen las dos, y desde ahí agregar o quitar reglas no obliga a cambiar ni el programa ni la prueba.

¿Se toma así?

### 416 · Usuario, 2026-10-03 11:33:31
> la regla misma dice el estado entonces contra estado es que se sabe si se puede utilizar o no

**Agente**, 2026-10-03 11:33:37
<!-- agente: b8ddfae3-fdde-48f3-a2eb-ec5685200900 -->

Falta la palabra que dice qué se espera. Con «Analicemos», respondo cómo el programa lee el estado de cada regla (vigente o derogada) para saber si puede usarla.

### 417 · Usuario, 2026-10-03 11:33:43
> Analicemos

**Agente**, 2026-10-03 11:33:58
<!-- agente: fb5fa0c3-fd80-41a6-b9a7-9b1298638613 -->

Sí, así debe ser, y el estado ya está escrito en cada regla, así que el programa no necesita otra lista:

- **Vigente:** el título no tiene marca. Si trae la línea «Autoriza escribir», da permiso.
- **Derogada:** el título lleva `[DEROGADA en X → ver Y]`, como `00·ID2`. No da permiso aunque conserve la línea, porque la regla no se borra (`20·M11`).
- **Opcional y apagada:** algunas reglas, como `13·DOC5`, son *opt-in*, y el proyecto puede apagarlas. Mientras estén apagadas, tampoco dan permiso.

**Propuesta:** `autorizado.py` lee esos tres estados en la regla misma y solo usa la vigente. La prueba deja de tener nombres fijos: comprueba con reglas de ejemplo que una vigente autoriza y que una derogada o apagada no. Así, agregar, derogar o apagar una regla cambia lo que se autoriza sin tocar ni el programa ni la prueba.

Esto entra en el plan de la fase B, que pasa a su versión siguiente con `validadores/autorizado.py` y `validadores/tests/test_nada_fuera_del_plan.py` en su tabla.

¿Se aprueba así?

### 418 · Usuario, 2026-10-03 11:34:48
> debemos pasar esto a un análisis?

**Agente**, 2026-10-03 11:34:53
<!-- agente: c75ae202-0a79-4762-a6b9-a726d2b43d94 -->

Falta la palabra que dice qué se espera. Si es una pregunta, la respuesta corta es sí: este es un hallazgo al ejecutar, y se decide en el análisis 11 del pendiente 103. Se abre con «Analicemos: el pendiente 103».

### 419 · Usuario, 2026-10-03 11:35:04
> pregunta

**Agente**, 2026-10-03 11:35:11
<!-- agente: e0acd175-e03b-4c72-896b-da69113d3e0d -->

Sí, hay que pasarlo a un análisis. Es un hallazgo que salió al ejecutar el plan, y el acuerdo 18 del análisis 1 dice que en ese caso la ejecución se detiene y vuelve al análisis. Además cambia lo que el plan aprobado permite tocar, y eso solo se decide en un análisis.

Va al análisis 11 del pendiente 103, que se abre con «Analicemos: el pendiente 103». Ahí se aprueba lo que acabamos de hablar:
- el estado de la regla decide si da permiso;
- la prueba deja de tener nombres fijos;
- el plan suma esos dos archivos.

### 420 · Usuario, 2026-10-03 11:35:38
> Analicemos: el pendiente 103

**Agente**, 2026-10-03 11:36:47
<!-- agente: 342d9b8e-519b-4961-8ea8-7d3442451b05 -->

El análisis 11 quedó prendido desde el turno 420, pero la discusión empezó antes. Busco el turno en que empezó para que la conversación entre completa, como se hizo en el análisis 8.

La discusión empezó en el turno 409, con «¿cuál es el hallazgo?». Ajusto desde dónde entra la conversación y lleno el encabezado del análisis 11 con un guion, igual que en el 10.

El análisis 11 quedó abierto, con su encabezado lleno. Su conversación empieza en el turno 409, con «¿cuál es el hallazgo?», así que lo que hablamos ya está adentro.

Para avanzar necesito dos respuestas:
1. **¿El hallazgo que abre este análisis es el H-14?** Es el de la prueba de la fase A que exige exactamente diez reglas con permiso para escribir (R-14).
2. **¿Se aprueba la solución que ya discutimos?**
   - **El estado de la regla decide si da permiso.** La vigente da permiso; la derogada o la *opt-in* apagada no. Así, agregar o quitar una regla nunca obliga a cambiar el programa.
   - **La prueba deja de tener nombres fijos** y lo comprueba con reglas de ejemplo.
   - **El hallazgo es parte del plan en curso.** El plan de la fase B pasa a su versión siguiente con `validadores/autorizado.py` y `validadores/tests/test_nada_fuera_del_plan.py` en su tabla, y la ejecución sigue desde la T-04.

### 421 · Usuario, 2026-10-03 11:37:33
> apruebo

**Agente**, 2026-10-03 11:39:08
<!-- agente: d7eda5ba-b317-4b7f-aac1-4a038e944792 -->

Lo anoto en «Lo acordado» del análisis 11. Busco los números de turno.

Registro primero las tres lecciones en la base de señales.

Quedó escrito en el análisis 11.

**Lo acordado:**
1. El H-14 es parte del plan en curso.
2. Los permisos se agregan o se quitan en la regla misma.
3. El estado de la regla decide si da permiso.
4. La prueba no fija nombres ni cantidad.

**Lo demás:**
- Están escritas todas las secciones, cada una saliendo solo de esos cuatro acuerdos.
- Hay tres lecciones, guardadas en la base como S-274 a S-276.
- Los validadores del análisis y de origen no dan fallas.

Para cerrarlo, decir «Apruebo el análisis». Al aprobarlo hago lo que manda:
- Paso el plan de la fase B a su versión siguiente con los dos archivos.
- Corrijo `autorizado.py` y la prueba.
- Sigo la ejecución desde la T-04.

### 422 · Usuario, 2026-10-03 11:39:48
> Pregunta: ya es claro lo que se debe hacer para este hallazgo?

**Agente**, 2026-10-03 11:40:14
<!-- agente: 5a8806cb-243a-4218-8b31-15af63e64a71 -->

Antes de responder compruebo una cosa que di por hecha: que las reglas propias de un proyecto se deroguen con la misma marca.

Casi. Lo de las reglas de `base/` está claro, pero al revisar encontré un punto que el análisis dio por hecho sin acordarlo:

- **Las reglas propias de un proyecto no tienen forma de derogarse.** La plantilla `reglas-proyecto.md` no dice cómo. En «Dónde más puede pasar» escribí que usan la misma marca `[DEROGADA…]`, pero eso no se acordó: lo supuse yo. Propongo acordarlo así: la regla propia que sale lleva en su título la misma marca que las de `base/`, y la plantilla lo explica.

Además, una precisión que no cambia nada: lo *opt-in* se apaga por capítulo, en el `CLAUDE.md` del proyecto, no regla por regla. El programa ya lo lee, así que una regla de un capítulo apagado no da permiso.

Con ese punto acordado, lo que hay que hacer queda claro. ¿Se acuerda así?

### 423 · Usuario, 2026-10-03 14:32:11
> Analicemos: recuerde esto es la base no pueden ingresar reglas del proyecto

**Agente**, 2026-10-03 14:32:50
<!-- agente: 48f4bcde-de19-4d8a-baeb-661b9ca2adc6 -->

Tiene razón: esto es la base, y la forma de las reglas propias de cada proyecto no se decide aquí (`20·M3`, `20·M13`). Retiro esa propuesta.

Quito del análisis 11 la fila de «Dónde más puede pasar» que daba por hecha esa marca. Las reglas del proyecto quedan como las dejó el acuerdo 47 del análisis 1: el programa las lee, y cómo retira el proyecto una regla suya es asunto de ese proyecto.

Listo, la fila quedó fuera del análisis 11. Ahora sí está claro lo que hay que hacer con el H-14:

1. `autorizado.py` usa solo las reglas vigentes de la base. La derogada no da permiso, y tampoco la de un capítulo *opt-in* apagado.
2. La prueba deja de tener nombres o cantidades fijas.
3. El plan de la fase B pasa a su versión siguiente con esos dos archivos, y la ejecución sigue desde la T-04.

Para cerrarlo: «Apruebo el análisis».

### 424 · Usuario, 2026-10-03 14:38:15
> osea ya está claro lo que se tiene que hacer?

**Agente**, 2026-10-03 14:38:19
<!-- agente: 3c1ff691-0c61-40c5-8a04-83de28c752da -->

Falta la palabra que dice qué se espera. Si es una pregunta, la respuesta corta es sí: son los tres puntos de «Lo que se tiene que hacer» del análisis 11, y no queda ninguna duda abierta.

### 425 · Usuario, 2026-10-03 14:39:10
> Pregunta: osea ya está claro lo que se tiene que hacer?

**Agente**, 2026-10-03 14:39:20
<!-- agente: cd4e0571-5ed8-42ba-b011-0f658a9a4a7a -->

Sí, está claro. Para el H-14 hay que hacer tres cosas:

1. **`autorizado.py`** toma en cuenta solo las reglas vigentes de la base. Una regla derogada, o una de un capítulo *opt-in* apagado, no da permiso aunque conserve su línea.
2. **La prueba** comprueba ese comportamiento con reglas de ejemplo, sin nombres ni cantidades fijas. Así, si entra o sale una regla, nada se rompe.
3. **El plan de la fase B** pasa a su versión siguiente con esos dos archivos en su tabla, y la ejecución sigue desde la T-04.

No queda ninguna duda abierta.

### 426 · Usuario, 2026-10-03 15:10:24
> Analicemos: Surge lo siguiente: se está actualizando el análisis padre, pero el "pendiente 103" ha tenido varios hallazgos y ya cuenta con "11 análisis", y aun así sigue siendo el mismo pendiente. Los hijos deben mejorar al padre

**Agente**, 2026-10-03 15:10:46
<!-- agente: 1b6cce84-c626-416c-a36e-e8999dd45cf7 -->

Tiene razón, y además eso ya estaba decidido y no se cumplió. El **acuerdo 10 del análisis 1** dice que, cuando un hallazgo vuelve al análisis, el hallazgo y el pendiente pasan a su versión siguiente. Pero los análisis 8, 9, 10 y 11 escribieron «el pendiente sigue en la V3».

Por eso el pendiente 103 no refleja lo que le pasó:
- Su «De dónde sale» nombra solo el H-13 del 2026-09-28 y el H-2 del 2026-09-30. Le faltan el H-8, el H-11, el H-13 y el H-14 del 2026-10-01, que entraron por los análisis 8 a 11.
- Su «El problema» sigue como lo dejó el análisis 2, aunque los hijos fueron precisando partes: el freno por cualquier canal, los acuerdos que no llegaban al agente y los permisos que viven en la regla.

**Propuesta:**
1. **Cada análisis mejora al padre.** Al aprobarse, el pendiente pasa a su versión siguiente: «De dónde sale» suma el hallazgo que abrió ese análisis, y «El problema» y «Por qué importa» se reescriben con lo que el análisis aprendió. Así lo pide el acuerdo 10.
2. **Que no dependa de acordarse.** El validador detiene la aprobación del análisis si su hallazgo no está en el «De dónde sale» del pendiente.
3. **Ponerlo al día ahora, en este análisis:** el pendiente 103 pasa a la V4 con los cuatro hallazgos que le faltan y su problema reescrito.

¿Se toma así?

### 427 · Usuario, 2026-10-03 15:23:17
> Analicemos: Si un pendiente tiene varios análisis, significa que los nuevos análisis van modificando y mejorando ese pendiente. Para el caso que tenemos, existen 11 análisis, pero el primero no cuenta para este propósito porque fue el que originó el pendiente; los otros 10 son los que lo han ido mejorando.

**Agente**, 2026-10-03 15:24:07
<!-- agente: c0641659-d305-41c2-87dd-1e07bc41c462 -->

Para proponer la versión siguiente del pendiente reviso qué hallazgo abrió cada análisis del 2 al 11.

Entendido: el análisis 1 originó el pendiente, y los análisis 2 a 11 son los que lo mejoran. Hoy el pendiente 103 está en la V3, que dejó el análisis 2, así que no recoge lo que aportaron los análisis 3 a 11.

**Propuesta:**
1. **La regla:** cada análisis que se aprueba deja el pendiente en su versión siguiente. «De dónde sale» suma el hallazgo que abrió ese análisis, y «El problema» y «Por qué importa» recogen lo que el análisis precisó. El validador no deja aprobar un análisis si su hallazgo falta en el pendiente.
2. **Ponerlo al día ahora:** el pendiente 103 pasa a la V4. Su «De dónde sale» suma los nueve hallazgos del 2026-10-01 que abrieron los análisis 3 a 11 (H-1, H-3, H-4, H-5, H-7, H-8, H-11, H-13 y H-14), y su problema queda así:

> No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente. La plantilla del plan no permite comprobarlo con un programa. Y el análisis no recoge solo lo que pasa: la conversación, lo que aporta al análisis principal y lo que aprende.

¿Se toma así, o ajusta el texto del problema?

### 428 · Usuario, 2026-10-03 15:25:41
> si

**Agente**, 2026-10-03 15:25:45
<!-- agente: 856686ef-1e0d-4af8-9a8b-2ce180dfeeee -->

Falta la palabra que dice qué se espera. Para acordarlo y escribirlo en el análisis 11, decir «Apruebo».

### 429 · Usuario, 2026-10-03 15:30:44
> Apruebo

**Agente**, 2026-10-03 15:31:46
<!-- agente: 50076494-d5f7-43c1-bb2b-743aabca41cc -->

Lo escribo en el análisis 11, pongo el pendiente 103 en su V4 y registro la lección.

Quedó escrito:

- **[El pendiente 103 en su V4](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md):** su «De dónde sale» ahora tiene los nueve hallazgos que abrieron los análisis 3 a 11, y su problema quedó reescrito. `origen` comprobó que cada hallazgo citado existe.
- **El análisis 11 suma dos acuerdos:**
  - Acuerdo 5: los hijos mejoran al padre. Cada análisis aprobado deja el pendiente en su versión siguiente, y el validador lo exige.
  - Acuerdo 6: el pendiente 103 se pone al día en este análisis.
- **Lo que se tiene que hacer** queda con cinco puntos. El 4 va a la HU-003, que es la dueña de la forma del pendiente. El 5 ya está hecho.
- **Se suma la lección S-277:** el acuerdo 10 del análisis 1 no se estaba cumpliendo.

Los validadores no dan fallas. Para cerrar: «Apruebo el análisis».

### 430 · Usuario, 2026-10-03 15:37:20
> pregunta: si ya estaba aprobado por qué los hallazgos no mejoraron el pendiente?

**Agente**, 2026-10-03 15:37:31
<!-- agente: 85a7bdf0-9129-491f-ba76-ade3899af789 -->

Por dos razones:

1. **Quedó escrito, pero nada lo hace cumplir.** El acuerdo 10 del análisis 1 se convirtió en la regla `02·F28`, que construyó la HU-004 en la versión 47.0.0: cada documento cambia en su mismo archivo y pasa a su versión siguiente. Pero ningún programa comprueba que el pendiente recoja el hallazgo de cada análisis.
2. **Yo no lo apliqué.** La plantilla del análisis pide escribir el pendiente en su versión siguiente, en «Propuesta final». En los análisis 8, 9, 10 y 11 la reemplacé por «el pendiente sigue en la V3», sin pasarlo de versión.

Es la misma falla del H-13: lo aprobado se cumple solo si el agente se acuerda. Por eso el acuerdo 5 de este análisis no se queda en texto y le encarga al validador no dejar aprobar un análisis cuyo hallazgo falte en el pendiente.

### 431 · Usuario, 2026-10-03 15:48:08
> pregunta: pero si se acordó por qué no quedó cumpliendose cuando lo que se aprueba en el análisis se hace?

**Agente**, 2026-10-03 15:48:19
<!-- agente: a2773ee1-8bf6-4759-9e8e-00e38b41f6cb -->

Porque fallé yo al hacerlo. El acuerdo 10 se aprobó, y aprobarlo ya era la orden de cumplirlo cada vez: en cada análisis siguiente me tocaba pasar el pendiente a su versión siguiente. En vez de eso escribí «el pendiente sigue en la V3» y seguí de largo, y nada me detuvo.

No hay otra razón. Es lo mismo que ya quedó en el recuerdo [aprobar es la orden de dejarlo funcionando](../../../../../historico-chat/memory/aprobar-es-la-orden-de-hacerlo.md): lo aprobado se cumple completo, sin esperar que alguien lo vuelva a pedir.

El acuerdo 5 de este análisis cierra ese hueco con un programa. Si un análisis no pone su hallazgo en el pendiente, el validador no lo deja aprobar, así que ya no depende de que yo me acuerde.

### 432 · Usuario, 2026-10-03 15:49:57
> ok entonces que sigue?

**Agente**, 2026-10-03 15:50:06
<!-- agente: 2e43e2c5-e102-4a48-8c91-14d2218443b1 -->

Falta la palabra que dice qué se espera. Si es una pregunta, lo que sigue es cerrar el análisis 11 con «Apruebo el análisis». Después vienen la versión siguiente del plan de la fase B y la ejecución desde la T-04.

### 433 · Usuario, 2026-10-03 16:00:08
> pregunta: ok entonces que sigue?

**Agente**, 2026-10-03 16:00:13
<!-- agente: 18219dda-aa07-40dd-a8e9-97fb77426a20 -->

Lo que sigue, en orden:

1. **Cerrar el análisis 11**, con «Apruebo el análisis».
2. **Continuar la fase B de la HU-007.** Paso su plan a la versión siguiente con `autorizado.py` y su prueba, los corrijo y sigo desde la T-04 hasta terminar la fase.
3. **Llevar el punto 4 del análisis 11 a la HU-003.** Es la regla de que cada análisis aprobado pasa el pendiente a su versión siguiente, con el validador que lo exige. Necesita su criterio en la HU-003 y su fase.
4. **La fase C de la HU-007:** la integración continua y el contrato de cada adaptador.

### 434 · Usuario, 2026-10-03 16:00:56
> Apruebo el análisis

**Agente**, 2026-10-03 16:06:17
<!-- agente: f7e4a7d8-eb25-4cf3-83a8-fcee5a3bd91d -->

El análisis 11 quedó aprobado. Como aprobar es la orden de hacerlo, sigo con lo que manda. Primero el H-14 en el resumen y la versión 2 del plan de la fase B.

Ahora el resumen, la versión 2 del plan y el estado de la fase.

Ahora la T-09: `autorizado.py` lee el estado de cada regla en la regla misma.

T-10: reescribo las pruebas de lo autorizado para que usen reglas de ejemplo.

Otra vez el problema de las barras al escribir desde la consola. Lo corrijo con el editor.

16 de 16. Sigo con la T-04: la nota de la plantilla del análisis.

T-05: reescribo `hook_antes.py` para que corra sobre toda acción usando `freno.py`.

Corrijo un error de precedencia en el mensaje de «pregunta».

T-07: el instalador. Cambio la entrada de `hook_antes.py`, sumo `hook_despues.py` y hago que un guion viva en un solo grupo por evento.

T-08: las pruebas de la fase.

13 de 13. Ahora las pruebas de los programas que cambié: el instalador, `autorizado.py` y el enganche de antes.

Fallan 3 pruebas de un archivo más antiguo, `test_las_reglas_llegan_antes_de_actuar.py` (de la EP-005), que prueba el freno viejo. Miro qué exigen antes de decidir nada.

Avancé casi toda la fase B de la HU-007, pero apareció otro hallazgo y la ejecución quedó detenida antes del cierre.

**Lo hecho:**
- Quedaron escritos el freno antes de actuar, el freno después de actuar, la línea «Autoriza escribir» en las HU, las épicas y los pendientes, y el cambio del instalador.
- `autorizado.py` lee el estado de cada regla y la prueba quedó sin nombres fijos (análisis 11).
- Pasan las 13 pruebas del freno y las 16 de lo autorizado.
- Hechas 9 de 10 tareas. Falta solo la T-08, que es el cierre.

**Hallazgo H-15:** fallan 3 pruebas de `test_las_reglas_llegan_antes_de_actuar.py`, un archivo de la EP-005 que prueba el freno viejo. Exigen que el freno mire solo la herramienta de escritura y que la consola nunca se detenga, que es justo lo que esta fase cambia. El plan no declara ese archivo, así que lo anoté y paré.

Es el mismo error del H-14, que ya dejó la lección S-274: al planear, no busqué qué pruebas leen lo que la tarea cambia. Esta vez lo busqué al correr las pruebas, no al planear.

**Lo que sigue:** el análisis 12 del pendiente 103, con «Analicemos: el pendiente 103». Recomiendo:
1. Las 3 pruebas viejas se actualizan al freno nuevo, y el plan pasa a su versión 3 con ese archivo.
2. Que el plan liste solo, al escribirse, las pruebas que leen los archivos que cambia, para que no vuelva a pasar.

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. El hallazgo y el plan en curso: el H-14 abre este análisis y es parte del plan en curso. El plan de la fase `B` de la HU-007 pasa a su versión siguiente con `validadores/autorizado.py` y `validadores/tests/test_nada_fuera_del_plan.py` en su tabla, y la ejecución sigue desde la T-04 (turnos 420 y 421).
2. Dónde se agrega o se quita un permiso: en la regla misma, con su línea «Autoriza escribir». Una regla que entra o sale funciona sin que se rechace y sin tocar el programa (turnos 413 a 415).
3. El estado de la regla decide: la vigente da permiso; la derogada, con `[DEROGADA…]` en su título, y la *opt-in* apagada no lo dan, aunque conserven la línea (turnos 416 a 421).
4. La prueba no fija nombres ni cantidad: comprueba con reglas de ejemplo que la vigente autoriza y que la derogada o la apagada no (turnos 413, 414 y 421).
5. Los hijos mejoran al padre: el análisis 1 originó el pendiente, y cada análisis siguiente lo mejora. Al aprobarse, el pendiente pasa a su versión siguiente: «De dónde sale» suma el hallazgo que abrió ese análisis, y «El problema» y «Por qué importa» recogen lo que precisó. El validador no deja aprobar un análisis cuyo hallazgo falta en el pendiente. Es el acuerdo 10 del análisis 1, que no se estaba cumpliendo (turnos 426 a 429).
6. El pendiente 103 al día: pasa a la V4, con los nueve hallazgos del 2026-10-01 que abrieron los análisis 3 a 11 y su problema reescrito con lo que ellos precisaron. Se hace de una, en este análisis (turnos 428 y 429).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `20·M11` (la regla que sale se deroga y no se borra), `02·F8` y `02·F9` (lo que el plan no previó detiene la ejecución) y el acuerdo 46 del análisis 1 (el freno solo detiene lo que no está autorizado en ninguna parte). Ninguna choca con lo acordado.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/autorizado.py` | Lee la línea «Autoriza escribir» de toda regla, sin mirar si está derogada o apagada |
| `validadores/tests/test_nada_fuera_del_plan.py` | Su prueba `test_las_diez_reglas_traen_su_linea` exige exactamente diez reglas, con sus nombres |
| Reglas derogadas | Llevan `[DEROGADA en X → ver Y]` en su título y se quedan en `base/` |
| Reglas *opt-in* | `validadores/recuperar.py` sabe cuáles apagó el proyecto (`opt_in_apagados`) |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1, acuerdo 46 | La regla es la que autoriza. Lo recogen los acuerdos 2 y 3 |
| Fase `A` de la HU-007 | Decidió que la línea vive en la regla y no en una lista aparte; su prueba contradijo esa decisión con una lista fija. Lo recoge el acuerdo 4 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Entra en la versión MAYOR de la fase `B` de la HU-007; `02·F22` no aplica |
| Normas y leyes | Ninguna aplica |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Prueba que fija cuántas o cuáles reglas hay | Cualquier validador del estándar | Falla cada vez que una regla entra o sale | Punto 2 |
| Regla derogada que conserva su línea | Cualquier proyecto | Sigue dando permiso sin regir | Punto 1 |
| Regla *opt-in* apagada | Proyectos que apagan reglas opcionales | Da permiso aunque el proyecto no la usa | Punto 1 |
| Pendiente con varios análisis que no recoge lo que ellos aprendieron | Cualquier pendiente que vuelve al análisis | Se lee un problema viejo y se pierden los hallazgos | Punto 4 |
| Tarea que cambia algo que una prueba o un programa lee | Cualquier fase | Sale un hallazgo al ejecutar | Lección 1: al planear se buscan los que leen lo que cambia |

---

## Propuesta final: hallazgo y pendiente

> El H-14 no cambia. El pendiente pasa a la V4. EP-023 no suma HU.

### Pendiente V4. Lo que se construye se aparta de lo aprobado

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13; [H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md); y de la sesión del 2026-10-01, [H-1](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-3](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-4](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-5](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-7](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-8](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-11](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-13](../../../../../historico-chat/resumenes/2026-10-01/sesion.md) y [H-14](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), que abrieron los análisis 3 a 11 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente. La plantilla del plan no permite comprobarlo con un programa. Y el análisis no recoge solo lo que pasa: la conversación, lo que aporta al análisis principal y lo que aprende. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) | Nada se escribe fuera del plan aprobado | Nada detiene al agente cuando trabaja fuera del plan aprobado | HU-002, HU-003, HU-004 | Es el plan en curso; la ejecución sigue desde la T-04 | 1, 2, 3 |
| 2 | [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) | El hallazgo y el pendiente tienen solo lo que les corresponde | El pendiente no recoge lo que aprenden sus análisis | HU-001 | Ya trata la forma del pendiente; no depende del freno | 4 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Al planear un cambio de reglas no se buscó qué pruebas las leen | Falló | S-274 | complementa R-2 |
| 2 | Una prueba con una lista fija de reglas falla cada vez que una regla entra o sale | Falló | S-275 | complementa R-12 |
| 3 | El estado vive en la regla: entrar o salir no toca el programa | Funcionó | S-276 | complementa R-1 |
| 4 | Los análisis no pasaban el pendiente a su versión siguiente, aunque el acuerdo 10 del análisis 1 lo pedía | Falló | S-277 | complementa R-9 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que `autorizado.py` lea el estado de cada regla y use solo la vigente: la derogada y la *opt-in* apagada no autorizan | 2, 3 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), fase B |
| 2 | Que la prueba de lo autorizado no fije nombres ni cantidad, y lo compruebe con reglas de ejemplo | 4 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), fase B |
| 3 | Pasar el plan de la fase `B` a su versión siguiente con `validadores/autorizado.py` y `validadores/tests/test_nada_fuera_del_plan.py` en su tabla, y seguir desde la T-04 | 1 | EP-023, [HU-007](../../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), fase B |
| 4 | Que cada análisis aprobado pase el pendiente a su versión siguiente con su hallazgo y lo que precisó, y que el validador no deje aprobarlo si su hallazgo falta en el pendiente | 5 | EP-023, [HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| 5 | Pasar el pendiente 103 a la V4 | 6 | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md`, hecho el 2026-10-03 |

## Lo que aporta al análisis principal

**Resultado:** Aclara.

**Lo que suma al análisis principal:** Agregar o quitar un permiso es cambiar la regla, no el programa: el programa lee en cada regla si está vigente, y las pruebas no fijan cuáles ni cuántas son. Cada análisis mejora a su pendiente: lo deja en su versión siguiente.
