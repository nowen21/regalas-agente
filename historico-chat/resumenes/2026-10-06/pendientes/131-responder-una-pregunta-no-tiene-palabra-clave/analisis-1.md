# Análisis 1: responder una pregunta del agente no tiene palabra clave

> **Aprobado** por el usuario el 2026-10-06, en el turno 72, con la versión 55.6.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-2.md`.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisó quién lee la lista: el enganche de reglas, el mapa de tareas y el guardado del gasto |
| R-2 | Se leyó cómo se arma la lista: `RecuperadorDeReglas.palabras_de_la_lista` la toma de las tablas de `palabras-clave.md` |
| R-17 | Las respuestas se miden contra `00·ID9` |
| Las demás | No aplican: no se crea regla (R-3, R-4), es el análisis 1 (R-6), no hay piloto (R-16) |

---

## Hallazgo

### H-5 · Responder una pregunta del agente no tiene palabra clave

| Campo | Valor |
|---|---|
| Qué pasó | El usuario respondió «autorizo» a una pregunta del agente y el enganche de reglas lo tomó como mensaje sin palabra clave de `01·C28`: hubo que repetirlo con «Hágalo». El usuario aprobó sumar «Respondo» a la lista |
| Por qué importa | Cada respuesta que no encaja cuesta un mensaje más, y obliga a usar palabras que autorizan más de lo que la respuesta quería |

## Pendiente

## Pendiente: responder una pregunta del agente no tiene palabra clave

| | |
|---|---|
| **De dónde sale** | [H-5 · Responder una pregunta del agente no tiene palabra clave](../../../../../historico-chat/resumenes/2026-10-05/sesion-2.md), en el resumen de la sesión del 2026-10-05 |

### El problema

Cuando el agente pregunta («¿A o B?», «¿se aprueba?») y la respuesta no abre con una palabra de [`01·C28`](../../../../../base/01-conducta/palabras-clave.md), el enganche de reglas la toma como un mensaje sin orden y el agente no actúa. El 2026-10-06 pasó con «autorizo»: hubo que repetir la respuesta con otra palabra. Para responder hay que acomodar la respuesta a una palabra de la lista, aunque lo que se quiere decir es solo «A» o «sí». El usuario aprobó sumar **«Respondo»**: contestar la pregunta que hizo el agente, y autorizar justo lo que esa pregunta pedía decidir, nada más.

### Por qué importa

Cada respuesta que no encaja en la lista cuesta un mensaje más, y obliga a usar palabras como «Apruebo» o «Hágalo» para decir otra cosa, que pueden autorizar más de lo que la respuesta quería.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 65 · Usuario, 2026-10-06 11:03:15
> Analicemos el pendiente 131

**Agente**, 2026-10-06 11:06:42
<!-- agente: f2da0675-c42a-4965-8263-79ee795ec7ea -->

Prendido el análisis 1 del pendiente 131. Reviso cómo lee Cimiento la lista de palabras y qué tarea le asigna a cada una.

Añadir la palabra es simple: Cimiento lee la lista directamente de `palabras-clave.md`, así que basta una fila nueva en la tabla y no hay que tocar código. Busco qué HU es la dueña de esa lista.

La dueña de la lista es la EP-001·HU-036, «el pedido dice qué se espera». Escribo el análisis.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/analisis-1.md), con el acuerdo 1: **«Respondo»** contesta la pregunta del agente y autoriza solo lo que esa pregunta pedía decidir.

Lo que encontré: Cimiento lee la lista de palabras directamente del archivo, así que basta con sumar una fila a la tabla y no hay que cambiar código.

Faltan dos decisiones, y para las dos recomiendo una opción:
- **Sin tarea propia**, igual que «Pregunta»: la respuesta trae solo las reglas de todo mensaje. Si lo respondido pide un cambio, las reglas de ese cambio llegan cuando el agente actúa.
- **Como fase nueva de la EP-001·HU-036**, la historia que creó la lista y la `01·C28`.

¿Se aprueban así?

### 66 · Usuario, 2026-10-06 11:17:41
> Apruebo3

**Agente**, 2026-10-06 11:19:10
<!-- agente: 1e85b372-42ab-4583-8298-24578200541c -->

Tomé «Apruebo3» como «Apruebo»: la palabra va al comienzo, solo con un 3 pegado. Anoto los acuerdos y completo el análisis.

Quedaron anotados los acuerdos 2 y 3: «Respondo» no pide tarea propia y va como fase nueva de la EP-001·HU-036. El análisis está completo y el pendiente ya pasó a su versión 2.

Para cerrarlo, escribir **«Apruebo el análisis»**.

### 67 · Usuario, 2026-10-06 11:20:24
> pregunta: cuáles son los acuerdos

**Agente**, 2026-10-06 11:20:37
<!-- agente: 9b6e36b7-a7af-4bbe-a920-816df8a69ad1 -->

Son tres:

1. **La palabra.** Se suma «Respondo» a la lista. Sirve para contestar una pregunta del agente y autoriza solo lo que esa pregunta pedía decidir, nada más.
2. **Sin tarea propia.** Igual que «Pregunta», «Respondo» no pide reglas especiales. Si lo que se responde lleva a un cambio, las reglas de ese cambio llegan cuando el agente actúa.
3. **Dónde va.** Como fase nueva de la EP-001·HU-036, la historia que creó la lista de palabras.

### 68 · Usuario, 2026-10-06 11:38:30
> pregunta falta algo más?

**Agente**, 2026-10-06 11:38:46
<!-- agente: bb66d1af-5586-4ff7-954f-3f06c1490c92 -->

Sí, falta decidir un caso que salió hoy mismo. Su mensaje «Apruebo3» no fue reconocido, porque el «3» quedó pegado a la palabra. El sistema lo tomó como mensaje sin palabra clave, y yo seguí solo porque lo interpreté a mano.

Propongo un **acuerdo 4**: que el programa reconozca la palabra aunque traiga pegado un número o un signo, por ejemplo «Apruebo3», «Respondo:» o «Hágalo.». Seguirían sin contar las palabras parecidas, como «Arregle» en lugar de «Corrija», tal como dice la lista hoy. Esto sí exige un cambio pequeño en `recuperar.py`, con su prueba.

Fuera de eso, no falta nada. ¿Se agrega el acuerdo 4?

### 69 · Usuario, 2026-10-06 11:58:53
> Analicemos
> Respuesta: me equivoqué y escribí Apruebo3 pero era Apruebo

**Agente**, 2026-10-06 11:59:22
<!-- agente: eb896dda-10db-42eb-9044-f54cc557ce5a -->

Entendido: fue un error de tecleo, y vale como «Apruebo».

Lo comprobé en el programa: hoy ya reconoce la palabra con dos puntos, punto, coma o en minúscula («Apruebo: B», «Hágalo,», «apruebo A»). Solo falla cuando la palabra lleva pegado un número o una letra, como en «Apruebo3». Así que «Respondo: B» va a funcionar sin cambiar nada más.

Mi recomendación es **no agregar el acuerdo 4**. Lo de «Apruebo3» fue un tecleo aislado, y aceptar palabras con cosas pegadas abre la puerta a reconocer lo que no se escribió. Si se queda así, el análisis queda con sus tres acuerdos y se cierra con «Apruebo el análisis».

### 70 · Usuario, 2026-10-06 12:19:15
> analicemos si ya hice la aclaración es claro que ya no es un acuerdo

**Agente**, 2026-10-06 12:19:27
<!-- agente: 1ac8ad8f-850c-4135-be83-8ee2eced7d58 -->

Tiene razón: con la aclaración bastaba, y no hacía falta proponerlo otra vez. No hay acuerdo 4. El análisis queda con sus tres acuerdos.

Para cerrarlo, escribir **«Apruebo el análisis»**.

### 71 · Usuario, 2026-10-06 12:24:03
> Apruebo el análisis

**Agente**, 2026-10-06 12:26:04
<!-- agente: 67c5dfd9-aca1-4c2a-8454-a79ff95175f8 -->

Arreglé el análisis del pendiente 131 y ya pasa la revisión, pero todavía no está aprobado. El primer «Apruebo el análisis» se rechazó y no quedó marcado.

**Qué tenía mal:** el acuerdo 1 citaba el turno 64, que queda antes de la conversación del análisis. Ahora cita el turno 66, donde se confirmaron los acuerdos.

**Lo que falta, en orden:**
1. Usted manda otra vez «Apruebo el análisis».
2. Con eso agrego «Respondo» a la lista de palabras clave, compruebo que el sistema la reconoce, la anoto en el CHANGELOG y subo la versión menor.
3. Le pregunto antes de hacer el commit de lo que quedó de esta sesión.
4. Usted reinicia Cimiento y el vigilante, y revisa la pantalla «Gasto».

### 72 · Usuario, 2026-10-06 12:29:01
> Apruebo el análisis

**Agente**, 2026-10-06 12:39:05
<!-- agente: e19b5663-9d47-4680-9895-f3462e4e20b2 -->

Abro la fase B de EP-001·HU-036 con las plantillas del estándar.

Escribo el plan y las pruebas de la fase B a partir de las plantillas.

Ahora el cambio y las pruebas.

Pruebas en verde. Ahora el CHANGELOG, la versión y el índice de la HU.

Otra sesión agregó la 56.0.0 al CHANGELOG mientras yo trabajaba, así que la mía pasa a ser 56.1.0 y va encima.

Cierro la fase con `cerrar_fase`.

Shell variable again; literal path.

La fase quedó cerrada. Quito el falso H-6 que el freno escribió por la variable de consola.

Ajusto la fila al formato del README.

Ya está «Respondo» en la lista de palabras clave. El sistema la reconoce y la fase B quedó cerrada; sus 2 pruebas pasan.

- **La palabra:** quedó en [palabras-clave.md](../../../../../base/01-conducta/palabras-clave.md), en la tabla de las que mandan sobre el trabajo. Sirve para contestar la pregunta del agente y autoriza solo lo que esa pregunta pedía decidir.
- **No trae reglas de tarea:** con «Respondo» llegan solo las reglas de todo mensaje. Lo comprueba [tests_respondo.py](../../../../../proyectos/cimiento/core/herramientas/tests_respondo.py).
- **Versión 56.1.0, no 55.7.0:** mientras se hacía la fase, otra sesión agregó la 56.0.0 al CHANGELOG (pendiente 132), así que esta entrada va encima. Esa otra sesión también dejó cambios sin guardar en [VERSION](../../../../../VERSION) y en el CHANGELOG, y no los toqué.
- **Aviso falso del freno, ya borrado:** se detuvo una orden porque escribí la ruta con una variable de consola. Escribió ese caso como hallazgo H-6 en el resumen de la sesión y lo quité, porque no era un hallazgo.

**Lo que falta, en orden:**
1. Decidir si se hace el commit de lo de esta sesión: la fase B, el pendiente 131 con su análisis, las marcas de las fases anteriores y los guiones. Para separarlo de lo de la otra sesión, en el CHANGELOG solo entra la entrada 56.1.0.
2. Reiniciar Cimiento y el vigilante, y revisar la pantalla «Gasto».

¿Hago el commit?

> acá termina la conversación

---

## Lo acordado

1. La palabra: «Respondo» entra a la tabla de las palabras que mandan sobre el trabajo mismo, en `palabras-clave.md`. Autoriza contestar la pregunta que hizo el agente y lo que esa pregunta pedía decidir, nada más. Se aprobó antes de prender el análisis y se ratificó con los demás acuerdos (turno 66).

2. Tarea: «Respondo» no pide tarea propia, igual que «Pregunta»; trae solo las reglas de todo mensaje, y las de lo que se haga llegan con la acción (turnos 65 y 66).
3. Dónde: una fase nueva de EP-001·HU-036, la historia que creó `01·C28` y la lista (turnos 65 y 66).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

`01·C28`: sin palabra, el agente no actúa; la lista vive en su anexo. `00·N1` y `01·C24`: solo la palabra del usuario aprueba; «Respondo» aprueba solo lo que la pregunta pedía. Ninguna regla choca.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| La lista | Tres tablas en [palabras-clave.md](../../../../../base/01-conducta/palabras-clave.md): las que no tocan nada, las que cambian el proyecto y las que mandan sobre el trabajo (Apruebo, Continúe, Pare) |
| Quién la lee | `RecuperadorDeReglas.palabras_de_la_lista`, que toma toda fila de tabla con la palabra en negrita: sumar la fila basta, sin tocar código |
| Las tareas | `base/tareas.md` dice qué palabras piden cada tarea; las que no piden ninguna dejan solo las de `siempre` |
| La HU dueña | [EP-001·HU-036, el pedido dice qué se espera](../../../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/HU-036-el-pedido-dice-que-se-espera.md), que creó `01·C28` y la lista |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-5 de la sesión del 2026-10-05 | El caso de «autorizo», que abrió este pendiente |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | La lista llega a todos: versión MENOR según `20·M10`, porque suma una opción y no obliga a nada |
| Normas y leyes | Ninguna |
| Herramientas | Ninguna |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Responder sin palabra en cualquier proyecto | Todo proyecto que hereda la lista | El mismo mensaje de más | Acuerdo 1: la lista es una sola |
| «Respondo» tomado como permiso amplio | El agente | Que haga más de lo preguntado | Acuerdo 1: autoriza solo lo que la pregunta pedía |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Responder una pregunta del agente no tiene palabra clave

| Campo | Valor |
|---|---|
| Qué pasó | El usuario respondió «autorizo» a una pregunta del agente y el enganche de reglas lo tomó como mensaje sin palabra clave de `01·C28`: hubo que repetirlo con «Hágalo». La lista no tiene una palabra para contestar lo que el agente pregunta |
| Por qué importa | Cada respuesta que no encaja cuesta un mensaje más, y obliga a usar palabras que autorizan más de lo que la respuesta quería |

### Pendiente V2. Responder una pregunta del agente no tiene palabra clave

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V2, «Responder una pregunta del agente no tiene palabra clave» |
| El problema | La lista de `01·C28` no tiene una palabra para contestar una pregunta del agente; la respuesta corta se toma como mensaje sin orden |
| Por qué importa | Un mensaje de más por cada respuesta, y palabras que autorizan de más |

### Épica y HU que salen del análisis

Épica existente: EP-001 (cuerpo de reglas heredable).

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-001·HU-036, fase nueva | «Respondo» contesta la pregunta del agente | La lista no tiene palabra para responder | Ninguna | Es la única | 2, 3 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Leer cómo arma el programa la lista antes de proponer mostró que el cambio es solo una fila, sin código | Funcionó | S-327 | Complementa R-2 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/pendiente.md`, hecho el 2026-10-06 |
| 2 | Sumar «Respondo» a la tabla de las que mandan sobre el trabajo, en `base/01-conducta/palabras-clave.md`, con su alcance | 1 | EP-001·HU-036, fase nueva |
| 3 | Comprobar que el enganche de reglas reconoce «Respondo» y no le asigna tarea propia; CHANGELOG y versión MENOR | 1, 2 | EP-001·HU-036, fase nueva |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** la lista de palabras clave suma «Respondo», para contestar lo que el agente pregunta sin autorizar nada más.
