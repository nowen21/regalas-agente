# Análisis 12: el plan no busca qué pruebas leen lo que cambia

> **Aprobado** por el usuario el 2026-10-03, en el turno 450, con la versión 50.0.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 11](analisis-11.md), aprobado el 2026-10-03. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se busca en qué otros sitios un plan deja de declarar lo que su tarea obliga a tocar |
| R-2 | Se revisa lo que ya existe: la lección S-274 del análisis 11 y lo que hoy hace el plan con las pruebas |
| R-6 | Se leen los acuerdos de los análisis 1, 8, 10 y 11 que llegan con cada mensaje |
| R-7 | Lo que nadie pidió se pregunta acá, no se agrega al plan |
| R-14 | Se confirma con el usuario que el hallazgo que abre este análisis es el H-15 |
| R-15 | Se aplicó: la ejecución se detuvo al aparecer el hallazgo |
| R-17 | Cada respuesta se mide contra `00·ID9` antes de entregarla |
| R-3, R-4, R-5, R-8 a R-13, R-16 | No aplican mientras el análisis no cree ni cambie reglas o plantillas; se revisan si eso cambia |

---

## Hallazgo

### H-15 · El plan de la fase B de la HU-007 no declara las pruebas del freno viejo

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-03, al correr las pruebas de los programas que cambia la fase `B` de la HU-007, fallaron 3 de `validadores/tests/test_las_reglas_llegan_antes_de_actuar.py` (EP-005, HU-023). Prueban el freno viejo: que mire solo la herramienta de escritura, que una orden de consola nunca se detenga y el mensaje «FUERA DEL PROYECTO». La fase cambia ese comportamiento a propósito, y el plan no declara ese archivo. |
| Por qué importa | Es el mismo caso del H-14: el plan no buscó qué pruebas leen lo que la tarea cambia (lección S-274). Corregirlas sin volver al análisis es escribir fuera del plan aprobado. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 4, del [análisis 11](analisis-11.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13; [H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md); y de la sesión del 2026-10-01, [H-1](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-3](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-4](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-5](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-7](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-8](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-11](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), [H-13](../../../../../historico-chat/resumenes/2026-10-01/sesion.md) y [H-14](../../../../../historico-chat/resumenes/2026-10-01/sesion.md), que abrieron los análisis 3 a 11 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente. La plantilla del plan no permite comprobarlo con un programa. Y el análisis no recoge solo lo que pasa: la conversación, lo que aporta al análisis principal y lo que aprende. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 435 · Usuario, 2026-10-03 16:18:12
> Analicemos: el pendiente 103

**Agente**, 2026-10-03 16:18:46
<!-- agente: b39fc035-65cf-46c7-82fd-d0bd46ff8f32 -->

El análisis 12 quedó prendido. Lleno su encabezado: el H-15 y el pendiente en su V4.

El análisis 12 quedó prendido, con su encabezado lleno: el H-15 y el pendiente en su V4. Para avanzar necesito tus respuestas:

1. **¿El hallazgo que abre este análisis es el H-15?** Son las pruebas del freno viejo que el plan no declara.
2. **¿Es parte del plan en curso?** Recomiendo que sí. Esas tres pruebas prueban un comportamiento que la fase B cambia a propósito: hay que actualizarlas al freno nuevo, y el plan pasa a su versión 3 con ese archivo en su tabla.
3. **Para que no vuelva a pasar** (es la segunda vez, después del H-14), propongo:
   - Al escribir el plan, un programa busca las pruebas que usan cada programa que el plan cambia y las pone con su ruta exacta en la tabla 2.1, como «se modifican si el cambio aprobado las rompe».
   - `flujo.py` no deja aprobar un plan que no las declare.
   - Así, si una se rompe por el cambio aprobado, ya está declarada y no hay que parar.

¿Se toma así?

### 436 · Usuario, 2026-10-03 16:20:08
> Pregunta: cuál es el problema?

**Agente**, 2026-10-03 16:20:17
<!-- agente: 3e34d4c6-7d52-493a-b879-9ead1f1a5fe4 -->

El problema es que hay unas pruebas viejas que esperan que el freno se comporte como antes, y esta fase lo cambió a propósito.

En la EP-005 se hizo un freno que solo miraba la herramienta de escritura y nunca detenía una orden de consola. Sus pruebas comprueban justo eso. Ahora la fase B, como quedó aprobado en los análisis 8 y 10, hace que el freno mire toda acción, también la consola, y esas pruebas fallan porque esperan el comportamiento viejo.

Hay que actualizarlas al freno nuevo, pero el plan aprobado no nombra ese archivo, así que tocarlo sería escribir fuera del plan.

Además, es la segunda vez que pasa lo mismo, después del H-14. Al planear no busqué qué pruebas usan los programas que la fase cambia.

### 437 · Usuario, 2026-10-03 16:33:32
> pruebas de qué?

**Agente**, 2026-10-03 16:33:41
<!-- agente: 3bab9aa0-eb9c-4728-943d-e6748dd822fd -->

Falta la palabra que dice qué se espera. Si es una pregunta, la respuesta corta es esta: son las pruebas automáticas del freno viejo, que lo ponen a prueba con escrituras de ejemplo y revisan que reaccione como se diseñó en la EP-005.

### 438 · Usuario, 2026-10-03 16:34:17
> Pregunta: pruebas de qué?

**Agente**, 2026-10-03 16:34:24
<!-- agente: 2bf76865-99e6-4df9-baf7-6cded4961b64 -->

Son **pruebas automáticas**: pequeños programas que revisan solos que otro programa haga lo que debe. Se corren con un comando, y cada una dice «pasa» o «falla».

Estas tres revisan el **freno**, el programa `hook_antes.py`, que decide si el agente puede escribir un archivo. Se escribieron en la EP-005, cuando el freno solo cuidaba que nada se escribiera fuera del proyecto. Cada una revisa algo distinto:
1. Que el freno se active solo cuando el agente usa la herramienta de escritura.
2. Que una orden de consola nunca se detenga.
3. Que, al detener, el mensaje diga «FUERA DEL PROYECTO».

La fase B cambió ese freno, como lo pidieron los análisis 8 y 10: ahora revisa toda acción, también la consola, y su mensaje es otro. Las pruebas siguen esperando el freno viejo y por eso fallan.

### 439 · Usuario, 2026-10-03 16:36:24
> Pregunta: esas pruebas viejas son del pendiente 103?

**Agente**, 2026-10-03 16:36:32
<!-- agente: e114ad96-1f9e-4081-b06d-2852f1588419 -->

No. Son de la **EP-005, HU-023**, que es otra épica y ya cerró. Ahí nació el freno, con sus pruebas, cuando solo cuidaba que nada se escribiera fuera del proyecto.

Lo que sí es del pendiente 103 es el programa que esas pruebas revisan, `hook_antes.py`. El análisis 8, en su acuerdo 2, decidió que el freno se amplía dentro de la HU-007 y no en un pendiente aparte. Por eso esta fase cambió el mismo programa, y las pruebas viejas de la EP-005 quedaron describiendo el freno que ya no existe.

### 440 · Usuario, 2026-10-03 16:39:50
> Pregunta: pero es que eso no es de la EP-23 y por qué lo está tratando acá?

**Agente**, 2026-10-03 16:40:01
<!-- agente: 2ff03342-4ed0-4cd0-8657-08eb5916642d -->

Lo trato aquí porque lo rompió el trabajo de la EP-023, no porque las pruebas sean de esta épica.

Esas pruebas son de la EP-005 y pasaban bien hasta hoy. Fallan porque la fase B de la HU-007 cambió el programa que revisan, `hook_antes.py`, como quedó en el acuerdo 2 del análisis 8: el freno se amplía en la HU-007. Si las dejo así, el estándar queda con pruebas rotas por un cambio que hizo esta épica.

Por eso propuse arreglarlas aquí: el que las rompió es el que las pone al día. Lo de la EP-005 no se reabre; solo se actualizan sus pruebas al freno nuevo.

Si prefiere que sea asunto de la EP-005, la otra opción es crear un pendiente aparte para ella. Pero mientras tanto esas pruebas seguirían fallando.

### 441 · Usuario, 2026-10-03 16:41:15
> pero en qué afecta eso la épica 23?

**Agente**, 2026-10-03 16:41:19
<!-- agente: 6acf0093-ee15-497a-a6d2-6b61a80c3687 -->

Falta la palabra que dice qué se espera. Si es una pregunta, la respuesta corta es que a la EP-023 no la afecta: su freno funciona y sus 13 pruebas pasan. Lo que falla son pruebas de la EP-005 que describen el freno viejo.

### 442 · Usuario, 2026-10-03 16:41:35
> pregunta: pero en qué afecta eso la épica 23?

**Agente**, 2026-10-03 16:41:44
<!-- agente: 2cb8f1d8-df7c-4260-a229-9b82e556e70e -->

No la afecta. El freno de la EP-023 funciona y sus 13 pruebas pasan. Las que fallan son las de la EP-005, que describen el freno de antes. Tampoco bloquean nada: ni el commit ni la subida al servidor corren esas pruebas.

Entonces el H-15 no es parte del plan en curso. Para ese caso, `13·DOC24` dice que se crea su pendiente y el plan continúa.

**Propuesta:**
1. El H-15 va a un pendiente propio, para poner al día las pruebas del freno de la EP-005. Mientras no se decida su dueño, vive en la carpeta del resumen del día, como dice el acuerdo 11 del análisis 1.
2. La fase B de la HU-007 sigue y cierra sin tocar esas pruebas.

¿Se toma así?

### 443 · Usuario, 2026-10-03 16:43:14
> analicemos: que no sea de esta épica no tiene por que parar el proceso

**Agente**, 2026-10-03 16:43:25
<!-- agente: 5eccf113-39ff-498b-9db5-b464ff7b0438 -->

Tiene razón: el H-15 no toca nada de lo que construye la fase B, y aun así la paré.

**Propuesta para el análisis 12:**
1. **Solo detiene el hallazgo que afecta al plan en curso.** Afecta si, para cerrar la fase, hay que tocar algo que el plan no declara. Si no la afecta, el hallazgo se anota con su pendiente en el resumen del día y el trabajo sigue sin pasar por un análisis. Esto precisa el acuerdo 18 del análisis 1, que hoy detiene todo hallazgo sin distinguir.
2. **El H-15 no la afecta.** Su pendiente va al resumen del día: poner al día las pruebas del freno de la EP-005. La fase B sigue y cierra sin tocar esas pruebas.

¿Se aprueba así?

### 444 · Usuario, 2026-10-03 16:52:38
> Hágalo: cree el pendiente en dónde pertenece

**Agente**, 2026-10-03 16:54:26
<!-- agente: bde6531a-8f05-4db6-9ebf-57eacfece7fa -->

Ese pendiente pertenece a la EP-005, HU-023, que es donde nacieron el freno viejo y sus pruebas. Busco su carpeta y cómo crea el andamio un pendiente dentro de una HU.

Lleno el pendiente 109 con el H-15.

Lo dejo escrito en «Lo acordado» del análisis 12 y completo sus secciones.

Listo:

- **[Pendiente 109](../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md):** creado en la HU-023 de la EP-005, donde nacieron el freno viejo y sus pruebas. Lo enlazan el H-15 y el índice de pendientes.
- **La fase B de la HU-007** ya no está detenida: el H-15 no la afecta.
- **El análisis 12 quedó escrito:**
  - Acuerdo 1: solo detiene el hallazgo que afecta al plan en curso.
  - Acuerdo 2: el H-15 no lo afecta y su pendiente es el 109.
  - El cambio de `02·F9` va a la HU-004.
  - Se suma la lección S-278.

Los validadores no dan fallas. Para cerrar el análisis: «Apruebo el análisis». Después termino la fase B, que solo tiene pendiente la T-08 de cierre.

### 445 · Usuario, 2026-10-03 16:55:02
> Pregunta: osea que el análisis 12 fue un falso positivo?

**Agente**, 2026-10-03 16:55:09
<!-- agente: f918372c-131b-40e6-89d9-92652ed99479 -->

En parte sí. Visto como alarma, el H-15 fue un falso positivo: no tocaba lo que construye la fase B ni era del pendiente 103, y no debió detener la fase ni abrir un análisis aquí.

Pero el análisis 12 no quedó en blanco. Sacó a la luz por qué pasó: el acuerdo 18 se estaba leyendo como «todo hallazgo detiene». Su acuerdo 1 lo precisa: solo detiene el que obliga a tocar algo que el plan no declara. Con eso, la próxima alarma de este tipo ya no detiene el trabajo.

### 446 · Usuario, 2026-10-03 16:55:32
> Pregunta: qué sigue?

**Agente**, 2026-10-03 16:55:37
<!-- agente: 2471b596-2dbd-4f4f-ab22-190670fd4451 -->

Sigue esto, en orden:

1. **Cerrar el análisis 12** con «Apruebo el análisis».
2. **Terminar la fase B de la HU-007.** Falta su cierre: el registro de cambios y la versión 51.0.0, el mapa del sitio, el resultado de las pruebas, el documento de lo implementado y la reinstalación para que el freno quede activo. Después viene su commit.
3. **Llevar a sus HU lo que dejaron los análisis 11 y 12:**
   - A la HU-003: que cada análisis pase el pendiente a su versión siguiente.
   - A la HU-004: que solo detenga el hallazgo que afecta al plan en curso.
4. **La fase C de la HU-007:** la integración continua y el contrato de cada adaptador.

### 447 · Usuario, 2026-10-03 17:02:25
> Pregunta: quedó claro que si el hallazgo no es de la épica no para ?

**Agente**, 2026-10-03 17:02:33
<!-- agente: 39f9180b-4faf-4f1a-8787-5e7e527ee457 -->

No con esas palabras. El acuerdo 1 quedó escrito con otro criterio: «solo detiene el hallazgo que obliga a tocar algo que el plan no declara». Se parece, pero no es igual a lo que usted dijo.

Propongo dejar el acuerdo 1 con su criterio explícito:

> Un hallazgo que no es de la épica en curso no detiene el trabajo: su pendiente nace donde pertenece y la fase sigue. Uno que sí es de la épica detiene solo si, para cerrar la fase, obliga a tocar algo que el plan no declara.

¿Lo corrijo así?

### 448 · Usuario, 2026-10-03 17:03:12
> Hágalo

**Agente**, 2026-10-03 17:03:30
<!-- agente: e177a741-94b2-4e29-b250-2a3195cd5f5f -->

Corregido. El acuerdo 1 del análisis 12 dice ahora lo que pediste. Un hallazgo que no es de la épica en curso no detiene el trabajo: su pendiente nace donde pertenece y la fase sigue. El que sí es de la épica detiene solo si, para cerrar la fase, obliga a tocar algo que el plan no declara.

Ajusté igual el punto 1 de «Lo que se tiene que hacer», que es el cambio de `02·F9` que va a la HU-004, y lo que el análisis le aporta al análisis principal. `origen` no da fallas.

Para cerrar el análisis 12, escribir «Apruebo el análisis».

### 449 · Usuario, 2026-10-03 17:07:15
> pregunta: qué sigue?

**Agente**, 2026-10-03 17:07:25
<!-- agente: e59ba6ea-b3e9-4941-adf1-46be1146a466 -->

Sigue, en orden:

1. **Cerrar el análisis 12**, con «Apruebo el análisis».
2. **Terminar la fase B de la HU-007.** Le falta el cierre: registro de cambios, versión 51.0.0, mapa del sitio, resultado de las pruebas y documento de lo implementado. Además hay que reinstalar para que el freno quede activo. Después viene el commit.
3. **Pasar a sus HU lo que dejaron los análisis 11 y 12:**
   - A la HU-003, que cada análisis pase el pendiente a su versión siguiente.
   - A la HU-004, que solo detenga el hallazgo de la épica que afecta al plan en curso.
4. **La fase C de la HU-007:** la integración continua y el contrato de cada adaptador.

### 450 · Usuario, 2026-10-03 17:09:37
> Apruebo el análisis

**Agente**, 2026-10-03 17:12:37
<!-- agente: b49e3dba-5408-4eb3-ac9e-c912dcf3a586 -->

El análisis 12 quedó aprobado. Termino la fase B de la HU-007: primero el registro de cambios, la versión y el mapa del sitio.

Pasan las 29 pruebas de la fase y las 114 de los programas que cambió (fuera de las tres de la EP-005, que quedaron en el pendiente 109). Corro los validadores y las marcas.

Sin fallas. Escribo el cierre de la fase: el resultado de las pruebas, lo implementado, el estado y la fila en la HU.

El freno ya está activo en este repositorio. Compruebo que deja pasar una orden de lectura.

Terminé la fase B de la HU-007. Falta tu aprobación para hacer el commit.

**Qué hace ahora el freno:**
- Antes de cada acción, detiene lo que el plan de la fase en curso no declara y ninguna regla vigente autoriza. Revisa todos los canales: la herramienta de escritura, la consola, las órdenes en segundo plano, las instalaciones y los procesos que quedan corriendo. Si la acción publica algo, pregunta antes.
- Después de cada orden de consola, compara lo que cambió en git con el plan.
- Cuando detiene algo, anota el hallazgo en el resumen de la sesión.
- Ya está activo en este repositorio: reinstalé, y una orden de lectura pasó sin problema.

**Pruebas:** pasan las 29 de la fase y las 114 de los programas que cambié. `estandar`, `tareas`, `origen`, `flujo` y `fases` no dan fallas, y no hay marcas nuevas. Las tres pruebas viejas de la EP-005 siguen fallando, como quedó acordado: están anotadas en el pendiente 109.

**Cierre:** quedan escritos el resultado de las pruebas, el documento de lo implementado, el estado de la fase y su fila en la HU. La versión sube a 51.0.0.

El commit incluiría también los análisis 11 y 12 y el pendiente 103 en su V4. Para hacerlo y subirlo, «Apruebo y suba».

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. Qué hallazgo detiene: el que no es de la épica en curso no detiene el trabajo; su pendiente nace donde pertenece y la fase sigue. El que sí es de la épica detiene solo si, para cerrar la fase, obliga a tocar algo que el plan no declara. Precisa el acuerdo 18 del análisis 1 (turnos 443, 444, 448 y 449).
2. El H-15 no afecta al plan en curso: las pruebas que fallan son de la EP-005 y la fase `B` de la HU-007 cierra sin tocarlas. Su pendiente, el 109, vive en la HU-023 de EP-005, donde nacieron el freno viejo y sus pruebas, y la fase sigue (turnos 440 a 444).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` y `02·F9` (lo que el plan no previó detiene la ejecución) y `13·DOC24` (el análisis siguiente decide si el hallazgo es parte del plan en curso). El acuerdo 1 precisa cuándo detener: antes de esa decisión ya se distingue si el hallazgo afecta al plan. Lo recoge el punto 1 de «Lo que se tiene que hacer».

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `validadores/tests/test_las_reglas_llegan_antes_de_actuar.py` | Tres pruebas de la EP-005 esperan el freno viejo y fallan |
| `02·F9` | Dice que lo no previó detiene la ejecución, sin distinguir si afecta al plan en curso |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1, acuerdo 18 | Detener ante un hallazgo; se aplicaba a todos. Lo precisa el acuerdo 1 |
| Análisis 11, lección S-274 | Al planear no se buscaron las pruebas que leen lo que cambia; volvió a pasar en el H-15 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Cambia `02·F9`: va con la fase que lo construya, en versión MENOR, porque detiene menos |
| Normas y leyes | Ninguna aplica |
| Herramientas | Ninguna condiciona lo acordado |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Prueba de otra épica que falla por un cambio aprobado | Cualquier proyecto | Se detiene una fase que podía cerrar | Punto 1 |
| Hallazgo que sí obliga a tocar algo fuera del plan | Cualquier fase | Se escribe fuera del plan | Punto 1: ese sí detiene |
| Pendiente que nace en el sitio equivocado | Cualquier hallazgo | Nadie lo encuentra con su dueño | Acuerdo 2: nace donde pertenece |

---

## Propuesta final: hallazgo y pendiente

> El H-15 no cambia. El pendiente 103 no pasa de versión: el H-15 no es de él, y su pendiente es el [pendiente 109](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md). EP-023 no suma HU.

### Épica y HU que salen del análisis

EP-023, Lo que se construye es lo que se analizó.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | [HU-004](../../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md) | Un hallazgo detiene la ejecución y vuelve al análisis | Nada distingue el hallazgo que afecta al plan en curso del que no | HU-003 | Es la dueña de `02·F9` | 1 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Se detuvo una fase por un hallazgo que no la afectaba | Falló | S-278 | complementa R-15 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que `02·F9` diga que el hallazgo que no es de la épica en curso no detiene el trabajo y su pendiente nace donde pertenece, y que el que sí es de la épica detiene solo si obliga a tocar algo que el plan no declara | 1 | EP-023, [HU-004](../../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis/HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md) |
| 2 | Crear el [pendiente 109](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md) en la HU-023 de EP-005 y seguir la fase `B` de la HU-007 | 2 | Este análisis, de una y sin fase: `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md`, hecho el 2026-10-03 |

## Lo que aporta al análisis principal

**Resultado:** Aclara.

**Lo que suma al análisis principal:** El hallazgo que no es de la épica en curso no detiene el trabajo: su pendiente nace donde pertenece. El que sí es de la épica detiene solo si obliga a tocar algo que el plan no declara.
