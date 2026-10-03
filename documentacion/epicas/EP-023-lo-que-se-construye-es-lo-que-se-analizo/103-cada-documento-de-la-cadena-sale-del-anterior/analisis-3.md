# Análisis 3: lo aprobado ordena distinto el análisis principal y la épica

> **Aprobado** por el usuario el 2026-10-01, en el turno 25. El hallazgo y el pendiente no pasaron a otra versión, porque el análisis no los cambió. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 2](analisis-2.md), aprobado el 2026-10-01. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Recomendaciones

> Se agregó en el piloto, por el [análisis 9](analisis-9.md): este análisis no consultó recomendaciones, porque el archivo no existía. De sus lecciones salen: R-6, R-7 y R-10.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| Ninguna | El archivo de [recomendaciones del análisis](../../../../plantillas/recomendaciones-del-analisis.md) nació después |

---

## Hallazgo

### H-1. Lo aprobado ordena distinto el análisis principal y la épica

| Campo | Valor |
|---|---|
| Qué pasó | Al escribir EP-023 y sus HU desde los análisis 1 y 2 del pendiente 103, apareció que lo aprobado dice dos cosas sobre el análisis principal de Cimiento. La propuesta final del análisis 1 pone su creación, el punto 32, dentro de la HU 1 de EP-023. Los turnos 141, 167 y 171 del mismo pendiente lo ponen antes de la épica, porque es el que decide las épicas. |
| Por qué importa | El orden decide si EP-023 se escribe ya o espera al análisis principal. Lo que se escriba con el orden equivocado hay que rehacerlo. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La pasa el enganche desde la [transcripción del día](../../../../historico-chat/2026-10-01-sesion.md), a partir del turno 14, donde se dijo «Analicemos: el pendiente 103».

### 14 · Usuario, 2026-10-01 19:39:52
> Analicemos: el pendiente 103

**Agente**, 2026-10-01 19:41:25
<!-- agente: 397e6903-a00d-44f5-bf1b-0117cd04d425 -->

Prendo el análisis 3 como lo fijó el análisis 2: anoto el hallazgo, creo `analisis-3.md` desde el borrador y escribo el archivo de estado. Primero reviso cómo están hoy el guion, el enganche y el resumen de hoy.

El análisis 3 quedó prendido.

- **Hallazgo:** H-1 en el [resumen de hoy](../../../../historico-chat/resumenes/2026-10-01/sesion.md), con solo «Qué pasó» y «Por qué importa».
- **Análisis:** [analisis-3.md](analisis-3.md), armado desde el borrador. Ya le entró el turno 14.

**Lo primero, según la conclusión 7 del análisis 2:** el hallazgo es parte del plan en curso, porque detiene la escritura de EP-023. Se resuelve antes de seguir.

**El choque, mirado de cerca.** Las conclusiones aprobadas no se contradicen entre sí:

- La conclusión 30 dice que el análisis 1 hace de inventario antes de crear la épica (`02·F26`). La puerta para escribir EP-023 ya existe.
- La conclusión 49 dice que el análisis principal se crea después de aprobar el análisis 1, sin ponerlo antes de la épica.
- El punto 32 lo manda a la HU 1.

El orden «análisis principal primero, después la épica» lo propuse yo en los turnos 141, 167 y 171, y nunca pasó a una conclusión.

| Opción | Qué pasa |
|---|---|
| **A. Seguir las conclusiones** | EP-023 se escribe ya, y el análisis principal se construye como criterio de la HU 1, con su plan y sus pruebas |
| B. Seguir mis propuestas de los turnos | EP-023 espera al análisis principal, y el punto 32 sale de la HU 1 |

**Recomiendo A.** Lo aprobado son las conclusiones, no lo que el agente propuso de paso. Con B, una propuesta mía que nadie aprobó cambiaría el reparto de las HU.

¿A o B?

### 15 · Usuario, 2026-10-01 19:47:02
> pero por qué se abre un nuevo análisis si ya estaba en una conclusión?

**Agente**, 2026-10-01 19:47:07
<!-- agente: 0d9a73ea-b265-4f21-95af-4b9dbcf053a1 -->

Falta la palabra que dice qué se espera (`01·C28`). Para responder por qué se abrió el análisis 3, escribir «Explique».

### 16 · Usuario, 2026-10-01 19:47:31
> Pregunta: pero por qué se abre un nuevo análisis si ya estaba en una conclusión?

**Agente**, 2026-10-01 19:47:42
<!-- agente: fe7b433d-9861-450d-84e5-8e46c2ff914e -->

No debía abrirse. La respuesta ya estaba en lo aprobado.

- La conclusión 30 del análisis 1 dice que ese análisis hace de inventario antes de crear la épica.
- La conclusión 49 y el punto 32 ponen el análisis principal dentro de la HU 1.

El supuesto choque era contra los turnos 141, 167 y 171, que son propuestas mías hechas de paso y que nunca se volvieron conclusión. Según la conclusión 45, eso no es un hallazgo: lo que manda son las conclusiones y se sigue con ellas.

El error fue el mismo de antes: leí los turnos antes de cotejarlos con las conclusiones, y llamé hallazgo a mi propia propuesta.

Quedaron tres cosas de más:

1. `analisis-3.md`.
2. El H-1 en el [resumen de hoy](../../../../historico-chat/resumenes/2026-10-01/sesion.md).
3. El archivo de estado, que sigue prendido y le pasa la conversación al análisis 3, incluido este turno.

Con «Revierta» se quitan las tres. Después, con «Corrija», se arreglan los puntos 1, 3 y 4 de la revisión: mover la épica y las tres HU a `documentacion/epicas/`, llevar ahí la carpeta del pendiente, quitar lo que no sale de los análisis y nombrar el borrador en la HU-001. Luego siguen las HU 4 a 7.

### 17 · Usuario, 2026-10-01 19:50:24
> Pregunta: Pero entonces, ¿por qué dijo que se contradecía? Esto no debería pasar. ¿Acaso la solución que estamos planteando está generando más problemas de los que existían inicialmente?

**Agente**, 2026-10-01 19:50:38
<!-- agente: 6521572a-3d43-4304-9507-b390dd9632df -->

Dije que se contradecía porque puse al mismo nivel la conversación y las conclusiones. El análisis guarda las dos cosas, y en la conversación están también mis propuestas. Cité los turnos 141, 167 y 171 como si fueran lo aprobado, y no los cotejé con las conclusiones, que son lo que se aprobó.

**¿La solución genera más problemas?** No. Lo que salió hoy no vino del diseño:

- Escribí en la ruta equivocada, agregué lo que no salía de los análisis e inventé un choque. Son los mismos comportamientos que describe el pendiente: el agente agrega o supone sin cotejar con lo aprobado.
- Lo que los ataja todavía no existe. El «Sale de» con su validador es la HU-002 y el freno es la HU-007. Hoy nada me detiene, igual que antes del análisis.
- El análisis sí funcionó: cada respuesta que hizo falta hoy ya estaba en sus conclusiones.

**Una debilidad que sí deja ver el diseño.** El análisis mezcla en un mismo archivo la conversación, con propuestas que nadie aprobó, y las conclusiones. Ni la plantilla ni ninguna regla dicen cuál manda. Eso facilita citar una propuesta como si fuera decisión, que es lo que me pasó.

Una nota en el borrador lo resolvería: «Lo que manda son las conclusiones; la conversación es contexto». Es una decisión de diseño y la toma el usuario.

### 18 · Usuario, 2026-10-01 19:57:04
> Pregunta: no se supone que se aprueba en últimas es el apartado: "Lo que se tiene que hacer" y la: "Propuesta final" eso lo que en última se va a convertir en plan de trabajo o no?

**Agente**, 2026-10-01 19:57:15
<!-- agente: cd377bc6-abf2-455e-8d9f-8e1905228f35 -->

Sí. Lo que se convierte en trabajo son esas dos secciones:

- **La propuesta final** dice qué épica y qué HU salen (conclusión 53).
- **Lo que se tiene que hacer** se vuelve los criterios de aceptación de cada HU (conclusión 23), y la columna «Pasó a» dice a cuál va cada punto.
- **El plan** sale de esos criterios (`02·F18`), no directamente del análisis.

La cadena queda así: lo que se tiene que hacer → criterios de la HU → plan.

Entonces, para escribir EP-023 y sus HU solo había que leer esas dos secciones de los dos análisis. Ahí el punto 32 está en la HU 1, sin choque. Lo inventé al ir a la conversación, que es contexto y no se convierte en nada.

Esto también corrige lo que dije en la respuesta anterior: la nota que propuse para el borrador sobra. El borrador ya lo dice en «Lo que se tiene que hacer»: «Cada fila se convierte en un criterio de aceptación de una HU».

La conversación sirve para entender un punto cuando hay duda, no para sacar trabajo de ella. Además, las conclusiones son el paso intermedio: de ellas sale lo que se tiene que hacer, y cada punto cita la suya en «Sale de».

### 19 · Usuario, 2026-10-01 19:59:21
> enotonces en qué quedamos?

**Agente**, 2026-10-01 19:59:25
<!-- agente: 2e7f6af6-29e9-4a36-b74b-8f4f5557a6f2 -->

Falta la palabra que dice qué se espera (`01·C28`). Para el resumen de en qué quedó todo, escribir «Pregunta» o «Explique».

### 20 · Usuario, 2026-10-01 19:59:58
> Pregunta: enotonces en qué quedamos?

**Agente**, 2026-10-01 20:00:07
<!-- agente: 6f8e385c-6fed-49aa-ad70-642e043705ff -->

Quedamos así:

**No hay nada que analizar.** EP-023 y sus siete HU salen de la propuesta final y de «Lo que se tiene que hacer» de los análisis 1 y 2, tal como están. El análisis 3 se abrió por error.

**Lo que hay hoy:**
- `epica.md` y las HU 1, 2 y 3, escritas en la carpeta del resumen del 2026-09-30, que no es su sitio. Además traen cosas que no salen de esas dos secciones.
- `analisis-3.md`, el H-1 en el resumen de hoy y el archivo de estado, que sigue prendido y le pasa esta conversación al análisis 3. Los tres sobran.

**Lo que sigue, en orden:**
1. **«Revierta»:** quitar el análisis 3, el H-1 y el archivo de estado.
2. **«Corrija»:**
   - mover la épica y las HU 1 a 3 a `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/`, con la carpeta del pendiente 103 adentro;
   - dejarles solo lo que sale de esas dos secciones;
   - nombrar el borrador de la plantilla en la HU-001;
   - corregir los enlaces.
3. **«Continúe»:** escribir las HU 4 a 7 con el mismo criterio.

Lo primero que se necesita es «Revierta».

### 21 · Usuario, 2026-10-01 20:03:42
> pregunta: ya es claro en qué orden se va a desarrollar los puntos de: "Lo que se tiene que hacer" porque sino se tiene claro el orden también pueden generar hallazgos

**Agente**, 2026-10-01 20:04:10
<!-- agente: abe4fa10-39a3-4564-bf60-1092b3a3cbec -->

Entre HU sí está claro. Dentro de cada HU no, y no le toca al análisis.

**Entre HU.** La propuesta final del análisis 1 fija el orden 1, 5, 2, 3, 4, 7 y 6, cada uno con su razón:
- la 1 va primero porque las demás se apoyan en el análisis;
- la 5 es pequeña y ataca la causa más directa;
- la 7 necesita que la 4 defina qué pasa con un hallazgo.

**Dentro de cada HU.** Ninguno de los dos análisis ordena los puntos, y según la cadena no es su trabajo. El orden de los criterios de una HU se fija en la columna «Depende de» de la HU (sección 8) y en el plan de cada fase (`02·F14`). Así lo trae la plantilla de la HU: «sirve para no ordenar las fases al revés y descubrirlo al probar».

**Un cruce entre HU que conviene vigilar.** El punto 6 del análisis 2 está en la HU 1: la herramienta no prende otro pendiente mientras el plan del análisis abierto no se cumpla. Para eso tiene que saber cuándo se cumplió un plan, y el cierre por el plan es el punto 12, que está en la HU 3, que va después.

No parece bloquearla. El dato se puede leer con enlaces que ya existen: la columna «Pasó a» lleva a la HU, la HU a sus fases y cada fase dice si cerró. Hay que confirmarlo en el plan de la HU 1, antes de aprobarlo.

### 22 · Usuario, 2026-10-01 20:06:02
> Pregunta: entendido, qué sigue?

**Agente**, 2026-10-01 20:06:09
<!-- agente: 316c2346-8a73-4b2d-b395-99fa6120a9a4 -->

Sigue «Revierta», para quitar lo que sobra del análisis 3:

- `analisis-3.md`;
- el H-1 del resumen de hoy;
- el archivo de estado, que todavía le pasa esta conversación al análisis 3.

Después:

1. **«Corrija»:** pasar la épica y las HU 1 a 3 a `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/`, con la carpeta del pendiente 103 adentro. Dejarles solo lo que sale de la propuesta final y de «Lo que se tiene que hacer», nombrar el borrador en la HU-001 y corregir los enlaces.
2. **«Continúe»:** escribir las HU 4 a 7 con ese mismo criterio.
3. Revisar el cambio y aprobarlo. El commit se pregunta aparte.

### 23 · Usuario, 2026-10-01 20:07:16
> no se revierte el análisis 3 porque ahí se aclaran cosas aunque no se tomaron decisiones importante para lo que ya estaba

**Agente**, 2026-10-01 20:07:21
<!-- agente: bac395c4-d120-4fba-aeb9-e5686a54146b -->

Falta la palabra que dice qué se espera (`01·C28`). Puede ser «Escriba», para llenar el análisis 3 con lo que se aclaró y dejarlo listo para aprobar, o «Explique», si se quiere que primero responda cómo queda.

### 24 · Usuario, 2026-10-01 20:07:34
> Escriba

**Agente**, 2026-10-01 20:09:36
<!-- agente: 9ae870a6-7e75-4c90-a3cf-f2ecbdbddb4c -->

Escribí las secciones del análisis 3. Ahora las mido con el validador de redacción.

Quedó escrito el [análisis 3](analisis-3.md), y el validador de redacción no le encuentra marcas.

- **8 conclusiones**, cada una con el turno de donde sale. La principal: lo que pasa a trabajo es la propuesta final y «Lo que se tiene que hacer», y la conversación es solo contexto.
- **La propuesta final** no cambia nada: el H-1 queda como está, el pendiente sigue en la V3 y EP-023 queda como la dejaron los análisis 1 y 2.
- **4 lecciones**: tres de lo que falló y una de lo que funcionó.
- **4 puntos de lo que se tiene que hacer**: los tres arreglos de EP-023 y confirmar en el plan de la HU 1 cómo sabe la herramienta que un plan se cumplió.

Como no hay versión nueva del hallazgo ni del pendiente, no hay nada que pasar a los originales antes de aprobar (conclusión 11 del análisis 2). Para cerrarlo hace falta «Apruebo el análisis».

Aparte, el validador encontró marcas en la épica y en las HU 1 a 3: entre 9 y 22 por archivo. Se corrigen en el mismo paso de «Corrija».

### 25 · Usuario, 2026-10-01 20:10:49
> Apruebo el análisis

**Agente**, 2026-10-01 20:11:21
<!-- agente: cbb21543-8cff-4f74-ac26-9326257cbc32 -->

El análisis 3 quedó aprobado. Su cabecera dice que se aprobó el 2026-10-01, en el turno 25, y que el hallazgo y el pendiente siguen en la versión que tenían.

El enganche se apaga solo: cuando esta respuesta entre al análisis, el guion ve la marca «Aprobado» y borra el archivo de estado. El próximo mensaje ya no entra.

Lo que sigue son los puntos 1 a 3 de «Lo que se tiene que hacer» del análisis 3:

- pasar la épica y las HU 1 a 3 a `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/`, con la carpeta del pendiente 103 adentro;
- dejarles solo lo que sale de las dos secciones que pasan a trabajo;
- nombrar el borrador en la HU-001.

Para eso hace falta «Corrija».

> acá termina la conversación

---

## Lo acordado

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis, que después se quitaron para no repetirlas; cada punto conserva el número de su conclusión. No decide nada nuevo.

1. Qué pasa a trabajo: La propuesta final dice qué épica y qué HU salen, y lo que se tiene que hacer se vuelve los criterios de cada HU. Las conclusiones son el paso intermedio. La conversación es contexto para entender un punto, y de ella no sale trabajo (Turnos 16 y 18).
2. El choque no existía: El punto 32 está en la HU 1. Las conclusiones 30 y 49 del análisis 1 no ponen el análisis principal antes de la épica. El orden «análisis principal primero» venía de propuestas del agente en los turnos 141, 167 y 171, que nunca fueron conclusión. EP-023 se escribe ya (Turnos 16 y 17).
3. El H-1 no era hallazgo: Fue un error del agente al leer el análisis, dentro de lo aprobado (conclusión 45 del análisis 1) (Turnos 16 y 17).
4. De dónde salen los errores de hoy: No del diseño. Escribir en otra ruta, agregar lo que no salía de los análisis y crear un choque son los comportamientos que describe el pendiente, y lo que los ataja (HU 2 y HU 7) todavía no existe (Turno 17).
5. El orden: Entre HU lo fija la propuesta final del análisis 1: 1, 5, 2, 3, 4, 7 y 6. Dentro de cada HU lo fijan la columna «Depende de» de la HU y el plan de cada fase (`02·F14`), no el análisis (Turnos 21 y 22).
6. Un cruce entre HU: El punto 6 del análisis 2, en la HU 1, necesita saber cuándo se cumplió un plan, y el cierre por el plan es el punto 12, en la HU 3. Se puede leer con enlaces que ya existen (de «Pasó a» a la HU, de la HU a sus fases y de la fase a su cierre). Se confirma en el plan de la HU 1, antes de aprobarlo (Turno 21).
7. Este análisis se conserva: No cambia lo decidido, pero deja aclarado qué pasa a trabajo y en qué orden (Turno 23).
8. Lo que se corrige sin análisis: La ruta de EP-023, lo que no sale de los análisis y la falta del borrador de la plantilla en la HU 1 son errores de ejecución: se corrigen y se sigue (Turno 20).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F18` (el plan sale de los criterios de la HU), `02·F14` (el plan dice en qué orden se hace), `02·F12`, punto 13, y `13·DOC16` (dónde vive una épica). Ninguna choca.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| EP-023 | `epica.md` y las HU 1, 2 y 3 están en la carpeta de este pendiente y no en `documentacion/epicas/`. Traen datos que no salen de los análisis |
| Plantilla de la HU | Su sección 8 tiene la columna «Depende de», que ordena los criterios dentro de la HU |
| Borrador de la plantilla del análisis | Ya dice que cada fila de lo que se tiene que hacer se convierte en un criterio de una HU |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Conclusión 45 del análisis 1 | Un error dentro de lo aprobado no es hallazgo: se corrige y se sigue. Lo recogen las conclusiones 3 y 8 |
| Conclusiones 23 y 53 del análisis 1 | Lo que pasa a trabajo es la propuesta final y lo que se tiene que hacer. Lo recoge la conclusión 1 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Nada cambia: este análisis no agrega trabajo ni versión |
| Normas y leyes | Ninguna aplica |
| Herramientas | La conversación entró con el guion intermedio, prendido escribiendo a mano el archivo de estado |

### Dónde más puede pasar

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Error del agente al leer un análisis | Cualquier análisis | Se toma como hallazgo lo que no lo es | Conclusiones 3 y 8 |
| Orden entre HU | Cualquier épica | Se construye en un orden que no se decidió | Conclusión 5 |
| Una HU que necesita algo de otra | Cualquier épica | Se construye antes de tiempo | Conclusión 6 |

---

## Propuesta final: hallazgo y pendiente

> El H-1 no cambia: queda como lo que pasó, y la conclusión 3 dice que no era un choque. El pendiente sigue en la V3. EP-023 y sus siete HU quedan como las dejó la propuesta final del análisis 1, con los puntos del análisis 2 en las HU 1 y 4.

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | El agente sacó un orden de trabajo de la conversación y no de lo que se tiene que hacer, creó un choque que no existía y abrió un análisis sin necesidad | Falló | Por escribir |
| 2 | El agente leyó solo una parte de los análisis y escribió EP-023 en la carpeta del resumen, aunque la conclusión 30 ya decía que el pendiente vive en EP-023 | Falló | Por escribir |
| 3 | El agente agregó a la épica y a las HU datos sin origen, que es lo que el pendiente quiere evitar | Falló | Por escribir |
| 4 | Preguntar qué es lo que pasa a trabajo deshizo la confusión de una vez | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar la épica y sus HU a `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/`, con la carpeta de este pendiente adentro, y corregir los enlaces | 2, 8 | EP-023, al escribirla |
| 2 | Dejar en la épica y en las HU solo lo que sale de la propuesta final y de lo que se tiene que hacer de los análisis 1 y 2 | 1, 8 | EP-023 y sus siete HU |
| 3 | Nombrar en la HU 1 el borrador de la plantilla del análisis como punto de partida | 8 | EP-023, HU 1 |
| 4 | Confirmar en el plan de la HU 1 cómo sabe la herramienta que el plan del análisis abierto se cumplió | 6 | EP-023, HU 1, en su plan |

## Lo que aporta al análisis principal

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

**Resultado:** Aclara.

**Lo que suma al análisis principal:** De un análisis pasan a trabajo su propuesta final y lo que se tiene que hacer; la conversación es el contexto.
