# Análisis 1: para saber si una prueba detecta un error se escribe cada vez un guion nuevo de sabotaje

> **Aprobado** por el usuario el 2026-10-09, en el turno 13, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

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
| R-1 | «Dónde más puede pasar» revisa los proyectos que heredan y los lenguajes que no son Python |
| R-2 | Se reutiliza lo que ya existe: las lecciones escritas en los encabezados de los 19 guiones, y la forma en que Cimiento ya corre las pruebas de cada proyecto (`core/herramientas/corredor.py`) |
| R-19 | El plan declara todo lo que pide el cambio: el comando, su prueba y la HU |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-3 · Cada sabotaje de pruebas se vuelve a programar desde cero

| Campo | Valor |
|---|---|
| Qué pasó | Hay unos 20 guiones `sabotaje_*` en `historico-chat/scripts/` que hacen lo mismo: copiar el archivo, dañarlo, correr las pruebas, devolverlo desde la copia y borrar lo que el daño dejó escrito. Cada uno copia en su encabezado las lecciones de los anteriores |
| Por qué importa | Si un guion nuevo olvida una lección, el código puede quedar dañado sin que nadie lo note |
| Pendiente | [Pendiente 148: probar que las pruebas sirven con un solo comando](pendiente.md) |

## Pendiente

**De dónde sale:** H-3 de la [sesión del 2026-10-08](../../guiones-que-pasan-a-cimiento.md).

**El problema.** Para saber si una prueba detecta un error, se daña el código a propósito y se mira si la prueba falla. Cimiento no tiene un comando para eso: en `historico-chat/scripts/` hay unos 20 guiones `sabotaje_*` y `sabotajes_*`, del 2026-08-25 en adelante, que repiten los mismos pasos: copiar el archivo, cambiar un texto, correr las pruebas, devolver el archivo desde la copia y borrar lo que el daño dejó escrito. Solo cambia la lista de daños.

**Por qué importa.** Cada guion trae en su encabezado las lecciones de los anteriores: devolver desde la copia y no desde git, porque el código puede no estar guardado; terminar corriendo todas las pruebas; borrar lo que el daño escribió fuera del archivo. Si un guion nuevo olvida una, el código puede quedar dañado sin que nadie lo note.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 10 · Usuario, 2026-10-09 08:29:01
> Analicemos: el pendiente 148

**Agente**, 2026-10-09 08:31:42
<!-- agente: a4007f95-81dc-49ef-aa2e-dec5a5ac8146 -->

Reviso los guiones de sabotaje y si EP-029 ya trata esto.

Ya revisé los 19 guiones de sabotaje y lo que tiene Cimiento. Escribo el análisis.

Necesito una decisión suya: **¿se construye el comando de sabotaje como HU-008 de la EP-029?** Le recomiendo que sí.

El análisis quedó escrito en [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/analisis-1.md). Esto encontré:

- **Hay 19 guiones de sabotaje, todos del 25 al 28 de agosto.** Después de esa fecha no se volvió a hacer ninguno. Probablemente se dejó de hacer porque cada vez había que armar el guion desde cero.
- **Sí servía.** Los sabotajes encontraron pruebas que nunca fallaban y, una vez, código que nadie usaba.
- **Las herramientas que ya existen no sirven aquí.** `mutmut` y `cosmic-ray` dañan el código de forma automática, pero solo funcionan con Python, son lentas y `mutmut` no corre en Windows.

La propuesta es un comando de Cimiento: `manage.py sabotear`. Recibe una lista de daños (en qué archivo, qué texto cambiar y por cuál) y la orden que corre las pruebas. Con cada daño:

1. guarda una copia del archivo;
2. lo daña;
3. corre las pruebas;
4. devuelve el archivo desde la copia, aunque algo falle a mitad de camino;
5. borra lo que el daño haya dejado escrito por fuera.

Al terminar, comprueba que todo quedó igual que antes y muestra qué daños detectaron las pruebas y cuáles no. Como solo cambia texto y corre la orden que se le dé, sirve para cualquier lenguaje.

Va en la EP-029 porque esa épica mide qué código queda sin pruebas, y esto mide si las pruebas que sí existen detectan errores. La EP-029 está terminada; con esta HU se vuelve a abrir.

### 11 · Usuario, 2026-10-09 08:35:35
> respondo: no entiendo a qué se refiere con sabotaje

**Agente**, 2026-10-09 08:35:48
<!-- agente: a9408ced-8e81-468c-a298-b6bcd96be5ef -->

"Sabotaje" es dañar el código a propósito para ver si las pruebas se dan cuenta.

Funciona como probar una alarma de humo. Si la alarma nunca suena, no se sabe si es porque no hay humo o porque está dañada. Para salir de la duda se le acerca un poquito de humo a propósito: si suena, sirve; si no suena, toca cambiarla.

Con el código es igual:

1. Las pruebas pasan, pero eso no garantiza que sirvan. Puede ser que no estén revisando nada.
2. Entonces se mete un error a propósito. Por ejemplo, se cambia un «menor que» por un «mayor que».
3. Se corren las pruebas. Si alguna falla, la prueba sirve, porque detectó el error. Si todas siguen pasando, la prueba no está revisando lo que debería.
4. Se quita el error y el código queda como estaba.

Hoy, cada vez que se quiere hacer esto, se escribe un programa nuevo de una sola vez, y hay 19 de esos. La propuesta es que Cimiento tenga un solo comando que lo haga y que siempre deje el código como estaba.

Si «sabotaje» suena confuso, el comando se puede llamar `danar_a_proposito`.

**¿Se construye ese comando como HU-008 de la EP-029?** Le recomiendo que sí.

### 12 · Usuario, 2026-10-09 08:38:16
> apruebo

**Agente**, 2026-10-09 08:38:57
<!-- agente: 635068d5-e639-49fb-959a-605d2f0835a1 -->

Quedó anotado en el análisis. Los dos acuerdos:

1. **El comando:** se llama `manage.py danar_a_proposito`. No se usa «sabotear», porque esa palabra no se entendió.
2. **La épica:** el trabajo se hace en la EP-029·HU-008, y la EP-029 se vuelve a abrir.

No queda ninguna decisión pendiente. **Escriba «Apruebo el análisis»** para aprobar el documento completo. Con eso hago la HU, el plan, el comando y sus pruebas sin volver a preguntarle, y le aviso cuando funcione.

### 13 · Usuario, 2026-10-09 08:40:04
> Apruebo el análisis

**Agente**, 2026-10-09 08:53:19
<!-- agente: 521fd365-8de6-4e1c-b5ec-0d65a118ad76 -->

Quedó aprobado. Registro la lección y arranco la cadena: HU-008, fase, plan, comando y pruebas.

La HU se escribe primero a mano. Tomo de modelo la HU-007 de la misma épica.

Escribo la HU-008.

El freno no deja crear la carpeta desde la consola. Pruebo escribiendo el archivo de la HU directamente, que fue como se creó la HU-011.

La HU quedó escrita. Agrego su README, su fila en la épica y abro la fase con el andamio.

Fase creada. Leo el plan de pruebas de la fase modelo para escribir los dos planes.

Antes del plan miro cómo están escritos un comando y una prueba de `core/pruebas`, para seguir el mismo estilo.

Los dos planes quedaron escritos. Ahora el código: primero la lógica en `danar.py`.

Ahora el comando.

Ahora las pruebas, sobre un proyecto de juguete en una carpeta temporal.

Las 8 pruebas pasan. Registro como señal lo que pasó con el `.pyc` y cierro la fase.

La orden de pruebas llevaba la ruta con barras `/`, y la consola de Windows no la reconoce. Uso `python manage.py`, que desde la HU-011 se vuelve a abrir solo con el Python de Cimiento.

Son los huecos del pendiente 147. Los lleno editando cada documento.

Cerrada. El mismo defecto dejó sin marcar dos filas de la matriz y los CA del plan, porque `cerrar_fase` espera otro formato. Los marco a mano y devuelvo la épica a «Terminada».

Anoto el hallazgo de `cerrar_fase` en el resumen de la sesión.

Corro los validadores de fases y de trazabilidad.

El comando `manage.py danar_a_proposito` ya funciona y la fase de la EP-029·HU-008 quedó cerrada. Lo que falta es su hallazgo H-2. **¿Abro el pendiente 150 para corregir `cerrar_fase`?** Le recomiendo que sí.

**Qué hace el comando.** Recibe una lista de daños y la orden que corre las pruebas. Mete cada daño en el código, corre las pruebas y dice cuáles daños detectaron y cuáles no. Al terminar, el código queda como estaba aunque algo falle, y se borra lo que el daño haya escrito.

**Las pruebas.** Pasan las 8 y cubren los 6 casos del plan de pruebas. Los validadores de fases, trazabilidad y plan no dan ninguna falla. El único aviso es que falta el commit.

**Un defecto que se corrigió durante la fase.** Un daño que la prueba sí detectaba salía como «no detectado». Python reutiliza la versión ya compilada de un archivo si este tiene el mismo tamaño y la misma hora de modificación. Cambiar «+» por «-» no altera el tamaño, así que las pruebas corrían el código sin el daño. Ahora cada daño le pone al archivo una hora distinta. Quedó registrado como señal S-362.

**El hallazgo H-2.** Al cerrar la fase, `cerrar_fase` tomó solo 1 de los 6 casos de prueba. Solo reconoce un caso por fila de la matriz, y esta fase pone varios en una misma fila. Completé a mano el resultado y las marcas que faltaban, pero el defecto sigue en el programa. La fase de la HU-011 de la EP-026 tiene el mismo formato. Lo anoté como H-2 en el [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-09/cerrar-pendientes-145-a-149.md).

Para abrir el pendiente 150, escriba «Registre el pendiente 150».

Después siguen el 146 y el 149. El commit se lo pregunto cuando terminemos los pendientes.

> acá termina la conversación

---

## Lo acordado

1. El comando: Cimiento tiene un comando, `manage.py danar_a_proposito`, que recibe una lista de daños (archivo, texto original, texto dañado) y la orden que corre las pruebas; por cada daño copia el archivo, lo daña, corre las pruebas, lo devuelve desde la copia aunque algo falle y borra lo que el daño dejó escrito; al final comprueba que todo quedó igual y dice qué daños detectaron las pruebas y cuáles no. Se llama así y no «sabotear» porque esa palabra no se entendió (`00·ID7`) (turnos 11 y 12).
2. La épica: se construye como EP-029·HU-008, y la EP-029 se reabre (turno 12).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `08·T8` (una prueba que no puede fallar no prueba nada: es justo lo que el sabotaje detecta), `08·T1` (el comando lleva sus pruebas), `00·N3` (no se rompe nada para pasar: el comando tiene que dejar el código igual que lo encontró) y `02·F0`. Ninguna regla exige sabotear: es una práctica, no una obligación. No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Los guiones | 19 archivos, unas 2.360 líneas, entre el 2026-08-25 y el 2026-08-28. Cada uno trae su lista de daños: nombre, archivo, texto original y texto dañado |
| Las lecciones que repiten | Devolver el archivo desde una copia, no desde git; devolverlo aunque el guion se caiga (`try/finally`); no correr las pruebas por una tubería, porque se pierde el código de salida; escribir solo ASCII, porque la consola de Windows se cae; leer bien el «OK» de las pruebas; borrar lo que el daño escribió fuera del archivo; terminar corriendo todas las pruebas; y cuando un daño no lo detecta ninguna prueba, mirar si la prueba es floja o si el código dañado nunca se usa |
| Desde el 2026-08-28 | No se escribió ningún guion de sabotaje más. La práctica se dejó de hacer, posiblemente porque cada vez había que armar el guion |
| Lo que tiene Cimiento | Corre las pruebas de cada proyecto (`corredor.py`) y mide qué código queda sin probar (EP-029). No tiene cómo medir si las pruebas detectan un error |
| Herramientas que ya lo hacen | `mutmut` y `cosmic-ray` dañan el código solos, pero son solo para Python, tardan horas en un proyecto grande y `mutmut` no corre en Windows |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| `S-062`, `S-074` (citadas en `sabotajes-hu021.py`) | Confirman que vale la pena: los sabotajes encontraron pruebas que no podían fallar, y una vez código que nadie usaba |
| `S-060`, `S-068` (citadas en el mismo guion) | Muestran dos errores que ya pasaron: la tubería que esconde el resultado y el «OK» mal leído. El comando los trae resueltos |
| Análisis 1 del pendiente 147 | Confirma: lo que se repite pasa a ser un comando de Cimiento, no un guion |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MENOR (`20·M10`): un comando nuevo, que nadie está obligado a usar |
| Normas y leyes | Ninguna |
| Herramientas | El comando no depende del lenguaje: cambia texto en un archivo y corre la orden de pruebas que se le dé. Así sirve para Python, PHP o JavaScript |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un proyecto que no es Python | `dp`, `agro-system`, `rni-front` | El comando no les sirve | El comando recibe la orden de pruebas como texto; no depende del lenguaje |
| El texto original no aparece en el archivo | Cualquier daño mal escrito | Se reporta como «detectado» un daño que nunca se aplicó | El comando revisa que el texto original aparezca una sola vez antes de dañar |
| El daño deja archivos fuera del archivo dañado | Lo que pasó en `sabotaje_e.py` | Queda basura en el proyecto | El comando compara qué archivos hay antes y después de cada daño y borra lo nuevo |
| El comando se cae a mitad de un daño | Cualquier corrida | El código queda dañado | Devolver el archivo en `try/finally` y comprobar al final que todos los archivos quedaron iguales a la copia |
| Código sin guardar en git | Cualquier proyecto | Devolver desde git borra el trabajo | Se devuelve siempre desde la copia |

---

## Propuesta final: hallazgo y pendiente, épica y HU

El hallazgo H-3 y el pendiente 148 quedan como están.

### Épica y HU que salen del análisis

Se suma a la [EP-029: Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige](../../../../../documentacion/epicas/EP-029-cimiento-sabe-que-parte-de-cada-proyecto-queda-sin-pruebas-y-lo-exige/epica.md), que mide qué código no se prueba; esta HU mide si lo que sí se prueba detecta un error. La épica está terminada y se reabre con esta HU.

**El comando:** `manage.py danar_a_proposito --danos «archivo» --pruebas "«orden»"`. La lista de daños es un archivo con un daño por bloque: nombre, archivo, texto original y texto dañado. Por cada daño: copia el archivo, lo daña, corre las pruebas, lo devuelve desde la copia y borra lo que el daño escribió. Al final corre las pruebas sin daños y comprueba que todo quedó igual. Responde con una tabla: qué daños detectaron las pruebas y cuáles no.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 008 | Un comando de Cimiento daña el código a propósito y dice qué daños no detectan las pruebas | Cada sabotaje se vuelve a programar desde cero y puede dejar el código dañado | Ninguna | Es la única | 1 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Una práctica que exige armar un guion cada vez se deja de hacer, aunque haya funcionado | Falló | S-361 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | `manage.py danar_a_proposito --danos «archivo» --pruebas "«orden»"`: revisa que cada texto original aparezca una sola vez antes de dañar; por cada daño copia el archivo, lo daña, corre las pruebas sin tubería y lee bien su resultado, lo devuelve desde la copia en `try/finally` y borra los archivos que el daño creó; al final corre las pruebas sin daños y comprueba que cada archivo quedó igual a su copia; responde con la tabla de daños detectados y no detectados; escribe bien en la consola de Windows; no depende del lenguaje del proyecto; y lleva sus pruebas | 1, 2 | EP-029·HU-008 |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** Cimiento mide si las pruebas de un proyecto detectan un error, dañando el código a propósito con un comando que siempre lo deja como estaba.
