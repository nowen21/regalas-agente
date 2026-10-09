# Análisis 1: el Resumen del gasto tarda más de un segundo y se recalcula con cada mensaje

> **Aprobado** por el usuario el 2026-10-09, en el turno 17, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-2.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | «Dónde más puede pasar» revisa las otras pestañas, la franja de arriba y las demás pantallas que se refrescan solas |
| R-2 | Se reutiliza lo que ya existe: el aviso por SSE de EP-025·HU-027 y el evento `actualizar` que ya escuchan todas las pestañas |
| R-19 | El plan declara todo lo que pide el cambio: `tablero.py`, `tablero.html` y sus pruebas |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-33 · Las pestañas del gasto se tapaban unas a otras, y el Resumen es lento

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, con Chrome sin ventana: al pulsar una pestaña mientras el Resumen cargaba (cerca de 1,5 s), la pestaña quedaba marcada y el Resumen llegaba después y la tapaba. Con cada mensaje nuevo el Resumen se vuelve a pedir, así que con el agente trabajando pasaba seguido. |
| Por qué importa | Para el usuario, «las pestañas no funcionan». La carrera se corrigió en la fase `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto`; la lentitud del Resumen sigue. |
| Pendiente | [Pendiente 146: el Resumen del gasto tarda y se pide con cada mensaje](pendiente.md) |

## Pendiente

**De dónde sale:** H-33 de la [sesión del 2026-10-06](../../../2026-10-06/sesion.md).

**El problema.** En la pantalla del gasto, la pestaña Resumen (`/gasto/pestana/resumen/`) tardó entre 1,5 y 1,8 s el 2026-10-08. Las otras cuatro pestañas tardan entre 0,2 y 0,6 s. Cada vez que el vigilante guarda algo, Cimiento avisa a la pantalla y la pestaña abierta se vuelve a pedir. Mientras el agente trabaja eso pasa con cada mensaje y con cada llamada.

**Por qué importa.** La pantalla responde lento justo cuando más se usa, mientras se trabaja, y la base hace el mismo cálculo pesado muchas veces por minuto.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 15 · Usuario, 2026-10-09 08:57:24
> Analicemos: el pendiente 146
> Cualquier pendiete que salga de esta sesión se debe resolver en esta

**Agente**, 2026-10-09 09:03:38
<!-- agente: 2f200ac8-1b96-476b-9560-b33e5939e705 -->

Mido cuánto tarda cada parte del Resumen sobre la base real.

Ya tengo las mediciones. Escribo el análisis.

Para cerrar el análisis falta una decisión: **¿la pantalla del gasto se refresca sola como máximo cada 30 segundos?** Recomiendo 30 segundos.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/146-el-resumen-del-gasto-tarda-y-se-pide-con-cada-mensaje/analisis-1.md). Hoy el Resumen tarda entre 1,1 y 1,3 s. La propuesta tiene dos partes:

1. **Que el Resumen tarde la mitad.** La gráfica por día trae las 10.550 llamadas y las suma una por una en Python, y eso es más de la mitad del tiempo (0,65 s). Si la base suma por hora y Python solo pasa cada hora a su día, esa gráfica baja a 0,10 s y el Resumen queda en unos 0,6 s.
2. **Que la pantalla no se recalcule con cada mensaje.** Los avisos que llegan seguidos se juntan, y la pantalla se refresca como máximo una vez en ese intervalo. Si la ventana del navegador está escondida, espera y se refresca una sola vez al volver a verla. El botón «Actualizar» sigue siendo inmediato.

El trabajo iría en una HU-030 de la EP-025, que es la épica de la pantalla del gasto.

Queda anotado que todo pendiente que salga de esta sesión se resuelve en esta misma. El primero es el del hallazgo H-2, que corrige `cerrar_fase`, y lo trabajo después del 146.

### 16 · Usuario, 2026-10-09 09:04:37
> continúe

**Agente**, 2026-10-09 09:05:21
<!-- agente: 94940407-09b5-4ffc-a68f-767b6a478204 -->

Tomo los 30 segundos recomendados y dejo anotados los acuerdos en el análisis.

Quedaron anotados en el análisis tres acuerdos:

1. **Más rápido.** Las gráficas por día se suman en la base de datos y no una por una en Python.
2. **Menos seguido.** La pantalla se refresca sola como máximo cada 30 segundos. Mientras está escondida no se refresca, y el botón «Actualizar» sigue respondiendo de inmediato. Tomé los 30 segundos recomendados porque la respuesta fue «continúe».
3. **La épica.** El trabajo va en la EP-025·HU-030.

No queda ninguna decisión pendiente. **Escriba «Apruebo el análisis»**, y con eso hago la HU, el plan, el cambio y las pruebas.

### 17 · Usuario, 2026-10-09 09:05:46
> Apruebo el análisis

**Agente**, 2026-10-09 09:16:45
<!-- agente: a24f5466-8e6b-4362-9274-322750407b10 -->

Aprobado. Registro la lección y miro cómo se probaron antes la pantalla del gasto y su refresco.

Escribo la HU-030 de la EP-025.

Escribo los dos planes. Esta vez pongo un solo caso por fila y los CA en el formato que reconoce `cerrar_fase`, para no repetir el defecto H-2.

Ahora el código de las gráficas en `tablero.py`.

Ahora la pantalla: junto los avisos en `tablero.html`.

Las pruebas que ya existían siguen siendo válidas: `setTimeout` solo corre después de un aviso, así que no cuenta como reloj. Escribo `tests_rapido.py`.

Las 41 pruebas pasan. Quito de la prueba de filas por hora dos líneas que no comprobaban nada, la vuelvo a correr y mido el Resumen sobre la base real (CP-002).

El Resumen bajó de 1,1-1,3 s a 0,28-0,41 s, menos de la mitad. Cierro la fase.

Con un caso por fila, el cierre tomó bien los 3 casos. Lleno los huecos.

Mismo cierre limpio. Marco la verificación del plan (sección 5) y las casillas de la HU, que el cierre no toca.

El pendiente 146 quedó terminado y funcionando.

- **Más rápido:** el Resumen bajó de 1,1-1,3 s a 0,28-0,41 s. Es la cuarta parte; la meta era la mitad.
- **Menos seguido:** la pantalla junta los avisos y se refresca sola como máximo cada 30 segundos. Mientras está escondida no se refresca, y el botón «Actualizar» sigue respondiendo de inmediato.
- **Pruebas:** pasan las 6 nuevas y las 35 que ya había de la pantalla del gasto. Los validadores no dan ninguna falla; el único aviso es que falta el commit.
- **Documentos:** quedan cerradas la EP-025·HU-030 y su fase. La lección quedó como señal S-363.

Al cerrar esta fase el defecto H-2 no se repitió, porque el plan puso un solo caso de prueba por fila. Aun así, `cerrar_fase` sigue dejando sin marcar la verificación del plan y las casillas de la HU, y eso entra en el mismo pendiente.

**Lo siguiente es el pendiente 150: corregir `cerrar_fase` para que lea bien los casos de prueba.** Ese pendiente sale de esta sesión, así que se resuelve en esta. Para abrirlo hace falta el mensaje «Registre el pendiente 150».

Después queda el 149. Antes de empezarlo hay que guardar los cambios de la EP-029·HU-004 en `views.py` y `ajustes.py`, que siguen sin commit.

> acá termina la conversación

---

## Lo acordado

1. Más rápido: las gráficas por día (`por_dia_por_tipo` y `por_dia`) se suman en la base agrupadas por hora en UTC, y Python pasa cada hora a su día (turnos 15 y 16).
2. Menos seguido: los avisos del vigilante se juntan y la pantalla del gasto se refresca sola como máximo una vez cada 30 segundos; escondida en el navegador no se refresca, y al volver a verse se refresca una vez si llegó algo; el botón «Actualizar» sigue siendo inmediato. Los 30 segundos son los recomendados: el usuario respondió «continúe» (turno 16).
3. La épica: se construye como EP-025·HU-030 (turno 16).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `06` (rendimiento: medir antes de optimizar), `08·T1` (el cambio lleva su prueba) y `02·F11` (la fase toca solo el módulo del gasto). No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

Medido el 2026-10-09 sobre la base real, con 10.550 llamadas en los últimos 7 días:

| Qué | Lo que hay hoy |
|---|---|
| El Resumen completo (`GastoDelPeriodo.pestana("resumen")`) | 1,1 a 1,3 s; 2,3 s la primera vez, con la base en frío. 14 consultas |
| La gráfica por día (`por_dia_por_tipo`, `tablero.py:236`) | 0,65 s: trae las 10.550 llamadas y las suma una por una en Python. Es más de la mitad del Resumen |
| La misma gráfica, agrupada por hora en la base | 0,10 s: la base devuelve 101 filas, una por hora con gasto, y Python pasa cada hora a su día |
| Lo que se ahorra (`ahorro`: `sin_tokens` y `candidatos`) | 0,3 s |
| Dónde se gasta (`agrupar`) | 0,16 s |
| El refresco | Cada aviso del vigilante dispara `actualizar` (`tablero.html:70`): la pestaña abierta y la franja de arriba se vuelven a pedir, sin límite, aunque el navegador tenga la pantalla escondida |
| Agrupar por día en la base | No sirve: MySQL no tiene cargadas las zonas horarias, y `CONVERT_TZ` devuelve vacío. Por eso se agrupa por hora en UTC, que no necesita conversión |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| EP-025·HU-026 («nada se pide cada cierto tiempo») y HU-027 («la pantalla se entera en el momento») | Confirman que el refresco va por aviso, no por reloj. El acuerdo que salga no vuelve al reloj: junta los avisos |
| Fase `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto` | Ya corrigió que el refresco tapara la pestaña escogida; el costo quedó |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE (`20·M10`): la pantalla es de Cimiento; no les pide nada |
| Normas y leyes | Ninguna |
| Herramientas | Agrupar por hora da el día exacto en zonas con diferencia de horas enteras, como Colombia (UTC−5). En una zona con media hora, una llamada de esa media hora podría caer en el día vecino |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| La gráfica de días de `todo()` (`por_dia`) | `tablero.py:68`, mismo recorrido una por una | El mismo costo donde se use | Punto 1: se arregla igual |
| La franja de arriba | `_franja.html`, también escucha `actualizar` | Se recalcula con cada aviso | Punto 2: junta los avisos para toda la pantalla |
| Las otras cuatro pestañas | `_donde`, `_contexto`, `_ahorro`, `_actividad` | Lo mismo, con menos costo | Punto 2 |
| Las pantallas de pruebas | `pruebas/lista.html` y `detalle.html` piden cada 15 s, solo mientras se revisa | Ninguno: se apaga sola al terminar | No hace falta cubrirlo |
| El botón «Actualizar» | `tablero.html:64` | Que también quede limitado | Punto 2: el botón sigue pidiendo en el momento |

---

## Propuesta final: hallazgo y pendiente, épica y HU

El hallazgo H-33 y el pendiente 146 quedan como están.

### Épica y HU que salen del análisis

Se suma a la [EP-025: Cimiento se administra y muestra el gasto de tokens](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md), que es la de la pantalla del gasto.

La propuesta tiene dos partes:

1. **Que el Resumen tarde la mitad.** Las gráficas por día se suman en la base, agrupadas por hora, en vez de traer cada llamada a Python. Baja de unos 1,2 s a unos 0,6 s.
2. **Que la pantalla no se refresque con cada aviso.** Los avisos que llegan seguidos se juntan, y la pantalla se refresca como máximo una vez cada 30 segundos; mientras está escondida en el navegador no se refresca, y al volver a verla se refresca una vez si llegó algo. El botón «Actualizar» sigue siendo inmediato.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 030 | El Resumen del gasto responde en la mitad del tiempo y no se recalcula con cada aviso | El Resumen tarda más de un segundo y se pide con cada mensaje | Ninguna | Es la única | 1, 2 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Sumar en Python lo que la base puede agrupar cuesta más a medida que crecen los datos; con MySQL sin zonas horarias, se agrupa por hora en UTC | Falló | S-363 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | `por_dia_por_tipo` y `por_dia` (`core/consumo/tablero.py`) suman en la base agrupando por hora en UTC y pasan cada hora a su día local; dan lo mismo que hoy y el Resumen baja a menos de la mitad del tiempo medido; con sus pruebas | 1, 3 | EP-025·HU-030 |
| 2 | `tablero.html` junta los avisos del vigilante: refresca como máximo una vez cada 30 segundos, no refresca mientras la pantalla está escondida y refresca una vez al volver si llegó algo; el botón «Actualizar» sigue inmediato; con su prueba | 2, 3 | EP-025·HU-030 |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** La pantalla del gasto responde rápido mientras se trabaja: suma en la base y no se recalcula con cada aviso.
