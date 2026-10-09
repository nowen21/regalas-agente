# Análisis 4: el freno detiene sin motivo lo que hizo otra sesión y lo que lee mal de una orden

> **Aprobado** por el usuario el 2026-10-09, en el turno 61, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Plantilla del análisis. Al llenarla se reemplazan los `«…»` y se borran las notas como esta, menos la tabla de reglas.
>
> Solo entra lo que ayuda a entender qué pasa y a tomar una decisión. Lo que no aporta a decidir no se escribe.
>
> Todo título y todo enlace dicen de qué se trata, nunca solo un número: «Pendiente: lo que se construye se aparta de lo aprobado», no «pendiente 103».
>
> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-5.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md` propio.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisan las otras formas en que el freno lee mal una orden, y todos los proyectos con varias sesiones a la vez |
| R-2 | Se leyó el código del freno: `Freno.partes`, `Freno.destinos`, `Freno.cambiados` y `fuera_del_plan` |
| R-10 | Se explica con los dos casos de esta sesión |
| Las demás | Se aplican al escribir lo acordado |

---

## Hallazgo

### H-1 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 11:24, el freno detuvo lo que escribió una orden de consola sobre `.gitignore`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Lo que se encontró | Esta sesión no escribió `.gitignore`: la orden que se detuvo solo leía (`sed` y `grep`). El cambio (`proyectos/*/.agente/` pasó a `.agente/`) lo hizo otra sesión abierta al mismo tiempo, a las 11:24:18. El freno compara la foto de antes y la de después de cada orden, y le carga a esta sesión lo que cambió otra |
| Pendiente | Por crear, y lo decide el usuario: el freno no distingue los cambios de otra sesión simultánea. No es de la EP-005, así que no detiene la construcción del pendiente 133 |

### H-5 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 12:05, el freno detuvo una orden de consola sobre `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/después`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Lo que se encontró | La orden era un `sed -i` que cambiaba «Sin empezar» por «Terminada» en la HU-027 y en la épica, las dos autorizadas. El freno toma como archivos las palabras sueltas de la expresión de `sed` («después» salió de «vuelve después de un resumen»). Es el mismo tropiezo de leer la orden de consola que el de `$R` (H-4): el agente lo evitó usando la herramienta de edición |
| Pendiente | Por crear, y lo decide el usuario: el freno lee como archivos las palabras de una expresión de `sed` que tiene espacios |

## Pendiente

| | |
|---|---|
| **De dónde sale** | [Hallazgo V2 de H-1 · Las reglas llegan repetidas en cada mensaje y no llegan cuando se actúa](../../reglas-de-cada-turno-sin-tokens.md), según el [análisis 1](analisis-1.md), en el resumen de la sesión del 2026-10-05; [hallazgo V2 de H-6 · Partir `cambiar-codigo` se hace por temas](../../../2026-10-09/sesion-2.md), según el [análisis 2](analisis-2.md), y [hallazgo V2 de H-7 · Llenar un análisis lo hace Cimiento, sin guiones sueltos](../../../2026-10-09/sesion-2.md), según el [análisis 3](analisis-3.md), en el resumen de la sesión 2 del 2026-10-09 |

## El problema

Las reglas se eligen solo por la palabra clave del mensaje. Lo que de verdad dice qué reglas rigen es la acción, y antes de ella no llega nada: [base/tareas.md](../../../../../base/tareas.md) lo describe, pero ningún enganche lo hace. Por eso `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar`, que no tienen palabra clave, no entregan sus reglas en ningún momento. Mientras tanto, con cada mensaje llegan las mismas listas, y seis reglas llegan dos veces. Y las reglas de código llegan todas, sin importar qué archivo se escribe. Además, cada análisis se llena con un guion escrito para él.

## Por qué importa

El agente trabaja sin las reglas de lo que está haciendo, recibe reglas que no aplican a lo que hace, y cada mensaje de todos los proyectos paga reglas que no usa. Y llenar cada análisis con un guion nuevo gasta trabajo repetido y puede traer un error distinto cada vez.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 56 · Usuario, 2026-10-09 14:16:45
> Analicemos: el pendiente 133

**Agente**, 2026-10-09 14:18:19
<!-- agente: 7dbbb749-03ff-457c-ad7e-3db73b88bee5 -->

El análisis 4 quedó prendido. Antes de proponer, reviso en el código del freno de dónde sale cada uno de los dos errores.

Cimiento ya llenó solo las rutas y la copia del pendiente del análisis 4: lo construido en la HU-033 funcionó. Lleno el resto del encabezado con el comando nuevo.

El encabezado del [análisis 4](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md) quedó lleno. Encontré la causa de los dos errores:

1. **Lo de otra sesión.** El freno toma una foto de los archivos antes de cada orden y otra después. Todo lo que cambió entre las dos fotos se lo carga a la sesión que dio la orden, aunque lo haya cambiado otra sesión abierta al mismo tiempo.
   **Propuesta:** antes de detener, el freno revisa qué hicieron las otras sesiones abiertas en los últimos minutos. Si una de ellas tocó ese archivo, no se lo carga a esta.

2. **Las palabras del `sed`.** El freno parte la orden por cada `|` antes de mirar las comillas. El texto que se iba a escribir tenía `|` porque era una tabla, así que lo cortó en pedazos y tomó esos pedazos como nombres de archivo.
   **Propuesta:** que solo parta por los `|` que están fuera de las comillas.

¿Se aceptan las dos?

### 57 · Usuario, 2026-10-09 14:32:30
> Explique aplicando las reglas 00·ID7 y 00·ID9, de modo que la explicación cumpla con lo establecido en ambas.

**Agente**, 2026-10-09 14:32:38
<!-- agente: 1410958d-0504-4c30-a75a-b2299a2e2b19 -->

Los dos errores se pueden corregir así:

1. **El freno culpa a una sesión por lo que hizo otra.** Hoy, cuando ve un archivo cambiado, supone que lo cambió la sesión que está revisando.
   **Arreglo:** antes de detener, el freno mira si otra sesión abierta tocó ese archivo. Si fue otra, no detiene a esta.

2. **El freno corta mal algunas órdenes.** El signo `|` separa una orden de otra, pero dentro de unas comillas es solo texto. El freno cortaba la orden también por los `|` que estaban dentro de las comillas.
   **Arreglo:** que solo corte por los `|` que están fuera de las comillas.

Con estos dos arreglos, el freno deja de detener trabajo permitido.

¿Se aceptan?

### 58 · Usuario, 2026-10-09 14:33:59
> apruebo

**Agente**, 2026-10-09 14:40:07
<!-- agente: f109f3ab-eb74-4792-acac-533eb597a646 -->

Anoto los dos acuerdos y completo el análisis 4 con el comando nuevo, sección por sección.

Solo queda el título de la sección de propuesta. Lo corrijo y paso el pendiente a su versión 5 y los dos hallazgos a su versión 2.

Los dos arreglos quedaron anotados como acuerdos, y el [análisis 4](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md) está completo. Esta vez lo llené con el comando nuevo de Cimiento, sin programas sueltos. El pendiente ya pasó a su versión 5 y los dos hallazgos a su versión 2.

Cuando se apruebe, construyo la HU-009 de la EP-023, que corrige el freno.

**Lo que se necesita ahora:** escribir «Apruebo el análisis».

### 59 · Usuario, 2026-10-09 15:14:22
> Apruebo el análisis

**Agente**, 2026-10-09 15:14:57
<!-- agente: c23e17b3-d127-40f0-b465-c5920d59ae69 -->

El punto 3 no se lee bien porque el signo `|` dentro de la tabla parte la fila en dos columnas. Lo marco para que se lea como texto, en el análisis y en el resumen.

Corregido: el punto 3 ya dice que sale del acuerdo 2.

**Para seguir, hace falta escribir otra vez «Apruebo el análisis».**

### 60 · Usuario, 2026-10-09 15:19:26
> Apruebo el análisis

**Agente**, 2026-10-09 15:19:54
<!-- agente: e33c0c54-f638-4999-bce4-0b8bbe958e33 -->

El validador sigue partiendo la fila por la barra, aunque esté marcada. Reescribo esas filas con palabras, sin el signo.

Listo: las filas ya no tienen el signo de barra y el validador las lee completas.

**Para seguir, hace falta escribir otra vez «Apruebo el análisis».**

### 61 · Usuario, 2026-10-09 15:21:48
> Apruebo el análisis

**Agente**, 2026-10-09 15:29:11
<!-- agente: 81325467-ace7-4983-8e6c-196053b0deda -->

Aprobado. Construyo la HU-009 de la EP-023. Primero leo la parte del freno que revisa lo que cambió después de cada orden.

Ya veo dónde corregir cada error. Escribo la HU-009.

Escribo el plan de la fase.

Ahora el código del freno.

Ahora las pruebas de la fase.

Las 343 pruebas pasan, incluidas todas las del freno. Cierro la fase.

El freno quedó corregido:
- Ya no detiene a esta sesión por lo que cambió otra sesión abierta.
- Ya no toma el texto entre comillas como si fuera el nombre de un archivo.

Pasan las 343 pruebas, incluidas todas las que el freno ya tenía.

Con esto, cada problema anotado en el resumen tiene su pendiente. **La sesión se puede cerrar** cuando se haga el commit de este último cambio.

¿Hago el commit?

> acá termina la conversación

---

## Lo acordado

1. El freno no le carga a una sesión lo que hizo otra: antes de detener por un archivo que cambió durante una orden de consola, mira si otra sesión abierta del mismo proyecto lo tocó en los últimos minutos; si fue otra, no detiene a esta ni lo anota como hallazgo suyo (turno 57).
2. El freno parte una orden de consola solo por los separadores (`|`, `;`, `&&`, `||`) que están fuera de las comillas; dentro de las comillas son texto (turno 57).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

> Cada subsección es obligatoria: el validador detiene el cierre si falta una.

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (lo que el plan no declara se detiene: el freno lo hace cumplir), `13·DOC22` (el hallazgo del freno va al resumen de la sesión que actúa) y `13·DOC26`. No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| La foto de antes y después | `Freno.tomar_foto` y `Freno.cambiados` (`core/enganches/freno.py`) comparan lo que `git status` ve cambiado; todo lo nuevo se le carga a la orden |
| Partir la orden | `Freno.partes` la corta con una expresión que no mira las comillas |
| Leer las palabras | `Freno.palabras` ya usa `shlex`, que sí respeta las comillas, pero recibe pedazos ya cortados |
| Las otras sesiones | Claude Code guarda la transcripción de cada sesión en la misma carpeta; cada escritura queda ahí con su ruta |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-1 y H-5 del 2026-10-09 | Los dos casos: `.gitignore`, cambiado por otra sesión, y la tabla dentro de un `sed` |
| H-4 del 2026-10-09 | Otro caso de leer mal una orden (una variable `$R`), que no se trata acá: el agente lo evitó escribiendo la ruta |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | PARCHE (`20·M10`): corrige el freno sin pedirles nada |
| Normas y leyes | Ninguna |
| Herramientas | Claude Code permite varias sesiones del mismo proyecto a la vez |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Otra sesión cambia un archivo mientras esta corre una orden | Cualquier proyecto con dos sesiones abiertas | Detiene trabajo permitido y ensucia el resumen | Acuerdo 1 |
| Una barra vertical o un punto y coma dentro de comillas en cualquier orden, no solo `sed` | Cualquier orden con texto entre comillas | Toma texto como archivo | Acuerdo 2 |
| Una sesión abierta pero quieta | Un proyecto con una sesión olvidada | Ninguno: solo cuenta la que escribió en los últimos minutos | Acuerdo 1 |

---

## Propuesta final: hallazgos V2 y pendiente V5, épica y HU

### Hallazgo V2 de H-1. El freno le carga a una sesión lo que hizo otra

| Campo | Valor |
|---|---|
| Qué pasó | Otra sesión cambió `.gitignore` mientras esta corría una orden que solo leía, y el freno la detuvo. La foto de antes y después no distingue quién cambió cada archivo |
| Por qué importa | Con dos sesiones abiertas, el freno detiene trabajo permitido y anota hallazgos que no son de la sesión |

### Hallazgo V2 de H-5. El freno corta las órdenes por los separadores que están dentro de comillas

| Campo | Valor |
|---|---|
| Qué pasó | Un `sed` cambiaba una fila de tabla, con barras verticales dentro de las comillas. El freno partió la orden por esas barras y tomó los pedazos como archivos |
| Por qué importa | Detiene cambios permitidos cada vez que una orden lleva una barra vertical o un punto y coma dentro de un texto |

### Pendiente V5. Las reglas llegan cuando se actúa, los análisis se llenan sin guiones y el freno no detiene sin motivo

| Campo | Valor |
|---|---|
| De dónde sale | Los hallazgos de las versiones anteriores, y los hallazgos V2 de H-1 y H-5 del 2026-10-09 |
| El problema | Además de lo de la versión 4: el freno le carga a una sesión lo que hizo otra, y corta las órdenes por separadores que están dentro de comillas |
| Por qué importa | Además de lo de la versión 4: el trabajo permitido se detiene sin motivo |

### Épica y HU que salen del análisis

Se suma a la [EP-023: lo que se construye es lo que se analizó](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/epica.md), donde vive el freno.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | HU-009 | El freno no detiene lo que hizo otra sesión ni lo que lee mal de una orden | El freno detiene trabajo permitido | Ninguna | Es la única | 2 y 3 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Cuando el freno detiene algo, revisar primero si la orden o el archivo eran de esta sesión antes de tomarlo como hallazgo | Funcionó | Se escribe al aprobar | Complementa R-15 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md` |
| 2 | Antes de detener por un archivo que cambió durante una orden, el freno lee las transcripciones de las otras sesiones del proyecto escritas en los últimos minutos; si alguna escribió ese archivo, no detiene ni anota hallazgo | 1 | EP-023·HU-009 |
| 3 | `Freno.partes` corta la orden solo por los separadores que están fuera de comillas: la barra vertical, el punto y coma, el doble «y», la doble barra y el salto de línea | 2 | EP-023·HU-009 |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** El freno no detiene lo que hizo otra sesión abierta al mismo tiempo, y lee las órdenes respetando las comillas.

