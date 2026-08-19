# 20 · Anatomía de una regla — el molde

> **De dónde sale.** La regla [`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) dice que todas las reglas se escriben igual. Aquí se explica ese "igual" con calma. En [`base.md`](base.md) queda el resumen; el detalle está solo aquí, para no tenerlo escrito en dos sitios ([`M2`](reglas/M2-un-tema-un-capitulo-un-dueno.md)).
>
> **Para qué sirve.** Una regla es una orden que el agente tiene que cumplir. Todas se escriben con la misma forma, y esa forma es la de abajo. Quien vaya a escribir una regla nueva, copia el molde y lo rellena.
>
> **Los ejemplos son inventados.** Van encerrados entre líneas de comillas invertidas (` ``` `). `R7` no es una regla de verdad: se la inventamos para mostrar cómo queda una terminada. Si algún día se hace un programa que cuente las reglas, tiene que saltarse lo que está encerrado así; si no, contará estos ejemplos como si fueran reglas.

---

## El esqueleto

```
## <PREFIJO><n> · <Título imperativo>   ·   `[marca]`        ← ENCABEZADO
│                                                              M4 · M5
│   ├── PREFIJO   letras exclusivas del capítulo (N, C, F, DOC…)
│   ├── n         consecutivo libre · no se reutiliza · no cambia nunca
│   ├── Título    imperativo · se entiende leyéndolo solo, en un índice
│   └── marca     [BLINDADA] | *opt-in* | [DEROGADA en X.Y.Z → ver ID]
│                 ← estas tres y ninguna más
│
├── CUERPO — 1 a 4 líneas, en presente e imperativo             M5
│   │
│   ├── UNA sola exigencia. Si aparece un "y además", son dos reglas.
│   │
│   ├── dependencia, si la hay, entre paréntesis                M7
│   │   ├── (extiende NN·ID)     agrega detalle · la otra sigue rigiendo
│   │   ├── (depende de NN·ID)   no se cumple si la otra no se cumplió
│   │   └── (deroga NN·ID)       la reemplaza · misma capa · con M11
│   │
│   ├── excepción, si la hay — va AQUÍ DENTRO, no en otro lado  M8
│   │   ├── condición   cuándo aplica
│   │   ├── límite      hasta dónde
│   │   └── autoriza    quién
│   │       (las [BLINDADA] no admiten excepción: eso es ser blindada)
│   │
│   └── lo que ya dice otra regla se ENLAZA (`ver 04·S4`), no se copia
│
└── EJEMPLO — obligatorio si la regla se puede malinterpretar   M5
    ```
    INCORRECTO: <el error concreto que se ve en la práctica>
    CORRECTO:   <qué se hace en su lugar>
    ```
```

---

## Parte por parte

### 1 · Encabezado — `## <PREFIJO><n> · <Título>`

Es el renglón de arriba: el nombre de la regla. Tiene cinco piezas.

| Pieza | Qué es | Así se ve | ¿Va siempre? | Lo que sale mal |
|---|---|---|---|---|
| `##` | Dos gatitos, siempre dos. Son los que convierten el renglón en un título. | `## R7 · Mide antes de optimizar` | Sí | `### R7 · Mide antes…` — con tres, la regla se esconde: no sale en la lista y el programa que las revisa no la ve. |
| PREFIJO | Las letras. Dicen de qué capítulo es la regla. Cada capítulo tiene las suyas y nadie más las usa ([`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)). | git → [`G2`](../09-git.md#g2--mensajes-que-explican-qué-y-por-qué) · documentación → [`DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) · rendimiento → `R7` | Sí | Ponerle `G9` a una regla del capítulo de pruebas, cuando `G` es de git. |
| `n` | El número. Se pone el siguiente que esté libre. | Si ya están el [`R1`](../06-rendimiento.md#r1--evita-consultas-en-bucle-n1), [`R2`](../06-rendimiento.md#r2--nunca-cargues-conjuntos-sin-límite)... hasta el [`R6`](../06-rendimiento.md#r6--mide-antes-de-optimizar), la nueva es la `R7` | Sí | Renumerar para "dejarlo ordenado": borrar la [`R3`](../06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena) y correr la [`R4`](../06-rendimiento.md#r4--cachea-lo-caro-y-estable-con-invalidación-clara) a [`R3`](../06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena). **El número no se cambia nunca** ([`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)). Es como el número de la camiseta: aunque el jugador se corte el pelo, sigue siendo el 7. Muchos papeles ya la llaman por ese número; si se lo cambias, todos apuntan a nadie. |
| Título | Lo que hay que hacer, dicho como una orden. Tiene que entenderse leyéndolo solo, sin abrir nada más. | `Recorre la cadena completa, sin saltar eslabones` | Sí | `La secuencia completa, de la necesidad al cierre` — eso cuenta algo, no manda nada. |
| marca | Una etiqueta al final. Solo hay tres. | `[BLINDADA]` = nadie la puede saltar → `## N4 · Proteger los datos reales · [BLINDADA]`<br>`*opt-in*` = cada proyecto decide si la usa → `## DOC5 · Registrar señales — *opt-in*`<br>`[DEROGADA…]` = ya no manda, y dice cuál la reemplazó → `## G4 · Trabaja en ramas · [DEROGADA en 2.0.0 → ver G9]` | No | Inventarse una etiqueta: `## F13 · … · [GATE DE ARRANQUE]`. Si de verdad hace falta una nueva, primero se agrega a la lista de [`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md). |

**Las letras que ya están ocupadas.** Antes de estrenar letras nuevas hay que mirar esta lista: si están aquí, ya son de otro capítulo y no se pueden repetir.

| Letras | Capítulo | De qué habla |
|---|---|---|
| `ID` | 00 · Identidad y rol | Quién es el agente, qué asume y dónde está su borde. |
| `N` | 00 · Núcleo blindado | Lo que no se toca nunca: seguridad. Todas van marcadas `[BLINDADA]`. |
| `C` | 01 · Conducta | Cómo se porta el agente: cuándo avisa, cuándo pregunta, cuándo para. |
| `F` | 02 · Flujo de trabajo | El orden para trabajar: entender, planear, hacer, probar, cerrar. |
| `D` | 03 · Datos | Cómo se guardan los datos y cómo se cambian sin romper los que ya hay. |
| `S` | 04 · Seguridad | Que nadie entre donde no debe ni haga lo que no le toca. |
| `E` | 05 · Errores y registro | Qué hacer cuando algo falla, y qué se anota para poder averiguar por qué. |
| `R` | 06 · Rendimiento | Que las cosas vayan rápido y no se atasquen cuando hay mucho. |
| `Q` | 07 · Calidad del código | Que el código se entienda: nombres claros, piezas pequeñas. |
| `T` | 08 · Pruebas | Comprobar que lo hecho funciona, y que se pueda volver a comprobar. |
| `G` | 09 · Git | Cómo se guarda el historial del proyecto: qué se guarda y cómo se describe. |
| `DEP` | 10 · Dependencias | Los programas de otros que el proyecto usa: cuáles, en qué versión. |
| `CFG` | 11 · Configuración y entornos | Los ajustes que cambian según dónde corra: en tu máquina, en el servidor. |
| `PR` | 12 · Privacidad | Cuidar los datos de las personas: pedir solo lo necesario y no enseñarlos. |
| `DOC` | 13 · Documentación | Dejar escrito qué se hizo y por qué, para que se entienda después. |
| `EST` | 14 · Estructura del código | Dónde va cada archivo y cómo se llama. |
| `IM` | 15 · Registros que no se borran | Lo que ya quedó registrado no se cambia; si estaba mal, se anula aparte. |
| `CQ` | 16 · Cumplimiento y calidad | Las leyes y normas que el proyecto tiene que cumplir. |
| `I` | 17 · Interfaz | Lo que ve y usa la persona: que se entienda y que funcione para todos. |
| `DP` | 18 · Despliegue | Cómo se pone el programa a funcionar de verdad, sin hacerlo a mano. |
| `OB` | 19 · Observación y operación | Poder ver desde fuera si el sistema está bien o está fallando. |
| `M` | 20 · Meta-reglas | Cómo son las reglas: esta lista, este molde, cómo se agrega una nueva. |

Si nace un capítulo nuevo, elige unas letras que no estén en esta lista y **se agrega aquí**. Las letras de un capítulo no se reciclan aunque el capítulo se quede sin reglas.

### 2 · Cuerpo

Es lo que la regla pide. **Pide una sola cosa.** Esta es la prueba más fácil: si al leerla aparece un "y además", ahí hay dos reglas metidas en una y hay que separarlas. La vieja se queda con su número y la nueva toma el siguiente libre ([`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).

**Cómo darse cuenta de que son varias.** Estas pistas casi nunca fallan:

| La pista | Regla mal armada | Por qué son dos | Cómo queda separada |
|---|---|---|---|
| Un **"y además"**, un "también" | "Todo cambio lleva prueba **y además** se documenta." | Son dos trabajos. Puedes hacer uno hoy y el otro mañana. | [`T1`](../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba) lleva prueba · [`DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md) se documenta |
| Dos **órdenes** pegadas con "y" | "**Valida** la entrada **y registra** el intento fallido." | Una cuida que no entre basura. La otra deja constancia. No se parecen. | [`S2`](../04-seguridad.md#s2--valida-y-sanea-toda-entrada-externa) valida · [`E4`](../05-errores-y-logging.md#e4--loguea-con-niveles-y-con-propósito) registra |
| **El título** lleva "y" | `## G2 · Mensajes claros y ramas limpias` | Una dice cómo contar lo hecho. La otra, dónde trabajar. | [`G2`](../09-git.md#g2--mensajes-que-explican-qué-y-por-qué) mensajes · [`G4`](../09-git.md#g4--trabaja-en-ramas-integra-limpio) ramas |
| Se puede **cumplir la mitad** | "Prueba el código **y** borra el que ya no se usa." | Si prueba todo y no borra nada, probó bien. Le falta otra cosa, no media prueba. | [`T1`](../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba) prueba · [`Q7`](../07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) borra |
| Hacen falta **dos ejemplos** | Uno para cada mitad | Un ejemplo enseña una cosa. Dos ejemplos, dos cosas. | Cada ejemplo, su regla |
| Una **lista** donde cada punto manda algo distinto | "hazlo así", "guárdalo allá", "avisa a fulano" | Cada punto se cumple solo. | Una regla por punto |

**La prueba que decide:** ¿se pueden cumplir por separado? Sí → son dos. No → es una.

Por eso hay "y" que no cuentan. `G2 · Mensajes que explican qué y por qué` es **una**: no puedes explicar el "qué" y saltarte el "por qué".

### Probemos con una regla de verdad: `F0`

[`F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) se llama "La secuencia completa — de la necesidad al cierre" y ocupa casi una página. Vamos a abrirla y ver qué hay dentro. Son **siete trozos**:

| # | Trozo | Qué dice | ¿Manda algo? |
|---|---|---|---|
| 1 | Una tabla de 7 pasos | Paso 0 la necesidad, paso 1 el análisis... hasta el paso 6, construir. Y dónde está la regla de cada paso. | **No.** Es un mapa: sirve para ubicarse. |
| 2 | La cadena obligatoria | Sin planteamiento no hay épica, sin épica no hay historia, sin historia no hay plan, sin plan no hay código. No se salta ninguno, ni aunque el trabajo sea chico. | **Sí.** Esta es la orden. |
| 3 | Qué es un planteamiento | "La necesidad escrita y sus restricciones." | No. Es una explicación. |
| 4 | Qué es una épica, un módulo y una fase | Tres explicaciones y un ejemplo de facturación. | No. Explicaciones, y de otros capítulos. |
| 5 | "Sin atajos por tamaño" | Un trabajo chico tampoco se salta la cadena. | Sí... pero es **la misma orden del trozo 2**, otra vez. |
| 6 | El ejemplo INCORRECTO/CORRECTO | Mal: idea → plan directo. Bien: idea → análisis → épica → historia → plan. | Es el ejemplo de la orden del trozo 2. |
| 7 | "Encadenamiento" | Qué otra regla cubre cada paso. | No. Es otro mapa. |

Ahora le pasamos las pistas:

- **¿Se puede cumplir la mitad?** Sí. Puedes recorrer la cadena (trozo 2) sin haber mirado nunca el mapa (trozo 1). Y al revés: puedes leerte el mapa entero y saltarte la cadena. Como se cumplen por separado, **no son una sola regla**.
- **¿Hay una lista donde cada punto manda algo distinto?** El trozo 4 son tres explicaciones seguidas. Ninguna manda nada — y encima el dueño de esos temas es otro capítulo.
- **¿Hay un "y además"?** Con esas palabras no, pero el trozo 5 repite el trozo 2. Decir lo mismo dos veces es la versión disimulada del "y además".

**Conclusión:** ahí dentro hay **una sola regla**, y la forman dos trozos: el 2 (la orden) y el 6 (su ejemplo). Los otros cinco no son regla: son mapa, explicaciones y una repetición.

Así queda cada trozo:

| Trozo | A dónde va |
|---|---|
| 2 y 6 | Se quedan. Son [`F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), con su número de siempre. |
| 1 y 7 | Suben al principio del capítulo: ahí va lo que orienta. |
| 3 y 4 | Se borran de aquí y se pone un enlace al capítulo que ya los explica. |
| 5 | Se borra. Ya lo dice el trozo 2. |

Y así queda la regla, ya con el molde:

````markdown
## F0 · Recorre la cadena completa, sin saltar eslabones

Todo desarrollo —funcionalidad nueva o cambio de comportamiento— recorre
`planteamiento → épica → HU → especificación → plan → código`, grande o chico. Ningún eslabón se
salta, se fusiona ni se omite por tamaño. Si te piden un paso y falta el
anterior, **PAUSAR y crearlo primero** (depende de `02·F2`, `13·DOC15`,
`13·DOC16`).

**Excepción** — lo que **no es desarrollo** queda fuera de la cadena: leer o
investigar, configuración local, comandos que el usuario pide, y el arreglo que
solo devuelve el código a lo que ya decía la especificación (condición). Cubre ese trabajo
puntual; no habilita a construir funcionalidad sin cadena (límite). Si hay duda
de si el caso es desarrollo, decide el usuario (`01·C7`) (autoriza).

```
INCORRECTO: llega una idea → se escribe el plan de trabajo directo
CORRECTO:   idea → análisis → objetivo y alcance → épica → HU → especificación
            → plan → construir
```
````

Tres cosas que cambiaron, y ninguna es lo que la regla exige:

- **El título ahora manda.** Antes contaba ("La secuencia completa..."), ahora ordena ("Recorre la cadena completa...").
- **Pasó de casi una página a doce líneas.** Lo que se fue no se perdió: está en el encabezado del capítulo y en los capítulos dueños de cada tema.
- **La excepción quedó completa.** Antes decía cuándo no aplica, pero no hasta dónde llega ni quién da el permiso. Ahora tiene las tres partes.

El número sigue siendo [`F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md). Eso no se toca nunca.

Cabe en una a cuatro líneas, y se escribe mandando. Si no cabe, casi siempre pasa una de dos: hay dos órdenes juntas, o se está contando **por qué** existe la regla — y el porqué se guarda en `notas/`, no aquí ([`M13`](reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)).

Tres cosas que **no** van aquí:

- **Copiar lo que ya dice otra regla.** Un día alguien arregla una copia y se olvida de la otra. Entonces las dos dicen cosas distintas y nadie sabe a cuál hacerle caso. Se pone un enlace a la otra (`ver 04·S4`) ([`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`M12`](reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)).
- **Nombres de herramientas.** Nada de nombrar un programa, una marca, un cliente. La regla tiene que servirle a cualquier proyecto, use lo que use. Se dice la idea, y después cada proyecto anota aparte con qué la cumple ([`M3`](reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)).
- **Explicar algo que explica otro capítulo.** Si el tema ya tiene dueño, se enlaza al dueño en vez de contarlo otra vez ([`M2`](reglas/M2-un-tema-un-capitulo-un-dueno.md)).

### 3 · Dependencia — solo hay tres, y se escriben

A veces una regla no se sostiene sola: necesita a otra. Eso se escribe entre paréntesis, dentro del cuerpo. Solo hay tres maneras ([`M7`](reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)):

| Forma | Significa | Ejemplo |
|---|---|---|
| `(extiende NN·ID)` | "Además de lo que ya pide la otra, esto." Las dos siguen mandando. | `18·DP1 extiende 09·G6` |
| `(depende de NN·ID)` | "Esto va después de aquello." Si lo otro no se hizo, esto no se puede hacer. | `13·DOC3 depende de 02·F2` |
| `(deroga NN·ID)` | "Esta reemplaza a aquella." De ahora en adelante manda la nueva. Se hace siguiendo [`M11`](reglas/M11-las-reglas-no-se-borran-se-derogan.md). | `G9 deroga G4` |

Dos cosas están prohibidas. **Dar vueltas en círculo:** si A necesita que B esté hecha, y B necesita que A esté hecha, no se puede empezar por ninguna — alguna de las dos está mal escrita. Y **mandar hacia arriba:** una regla normal no puede cambiar ni reemplazar una `[BLINDADA]`; esas están por encima de todo.

Si un capítulo entero se apoya en otro, se dice **una vez al principio del capítulo** y ya, no en cada regla.

### 4 · Excepción — dentro de la regla, con sus tres partes

Hay reglas que tienen un caso especial donde no aplican. Ese caso se escribe **dentro de la misma regla** ([`M8`](reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md)). Nunca en otro papel, y nunca solo dicho de palabra: lo que no está escrito, no existe. Y hay que decir tres cosas, las tres:

- **condición** — cuándo vale.
- **límite** — hasta dónde llega, y qué **no** permite.
- **autoriza** — quién tiene que dar el permiso.

La tercera es la que más se olvida, y es la más importante. **Si nadie tiene que dar permiso, la excepción se vuelve costumbre** y al final la regla no se cumple nunca.

No vale la excepción a medias, ni "solo por esta vez", ni "es que hay prisa". Si aparece un caso que necesita una excepción **que no está escrita**: se **para y se pregunta**. Si dicen que sí, se **escribe dentro de la regla** y se anota el cambio ([`M10`](reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

Las `[BLINDADA]` no aceptan ninguna excepción: eso es lo que quiere decir estar blindada. Y cuidado con confundirse: una regla `*opt-in*` **no es una excepción**. Es una regla que el proyecto enciende o no enciende; si la enciende, se cumple entera.

### 5 · Ejemplo — INCORRECTO / CORRECTO

Son dos renglones: uno con lo que se hace mal y otro con lo que hay que hacer.

Hay que ponerlo cuando la regla se puede entender de dos formas, o cuando el error se comete mucho. Si la regla es obvia, no hace falta ([`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)).

El renglón de INCORRECTO se escribe con **el error que la gente comete de verdad**. Si se pone uno exagerado, que nadie cometería, no sirve de nada: todos lo leen, piensan "yo no hago eso", y siguen cometiendo el error de siempre.

---

## Ejemplo completo — todas las partes

> Inventado. `R7` no existe.

````markdown
## R7 · Todo proceso por lotes declara su tamaño de tanda

Un proceso que recorre un conjunto de registros trata **N por tanda** y nunca
depende del tamaño total del conjunto (extiende `06·R2`). El valor de N lo
declara el proyecto (`.agente/stack.md`), no va escrito en el código.

**Excepción** — una migración de una sola ejecución puede ir sin tanda si el
conjunto está **contado y medido antes** (condición), **solo para esa ejecución**
y sin habilitar el patrón para procesos recurrentes (límite), y **lo autoriza
el usuario por operación** (`04·S11`) (autoriza).

```
INCORRECTO: recorrer "todos los pendientes" y confiar en que nunca serán muchos
CORRECTO:   tandas de N con registro de avance; N lo declara el proyecto
```
````

Ranura por ranura:

| Ranura | Qué quedó | Regla |
|---|---|---|
| PREFIJO | `R`, las letras del capítulo que habla de que las cosas vayan rápido | [`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) |
| `n` | `7`, porque ya estaban ocupados del [`R1`](../06-rendimiento.md#r1--evita-consultas-en-bucle-n1) al [`R6`](../06-rendimiento.md#r6--mide-antes-de-optimizar) | [`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) |
| Título | Manda, y se entiende sin leer nada más | [`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) |
| marca | Ninguna: no está blindada, no es opcional, no está jubilada | [`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) |
| cuerpo | Pide **una** sola cosa: decir de a cuántos se trabaja por vez | [`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) |
| sirve a cualquier proyecto | Dice "N" y "el proyecto lo decide"; no nombra ninguna herramienta | [`M3`](reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) |
| dependencia | `extiende 06·R2`, y [`R2`](../06-rendimiento.md#r2--nunca-cargues-conjuntos-sin-límite) sigue mandando | [`M7`](reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) |
| excepción | Con las tres partes: cuándo vale, hasta dónde, quién da permiso | [`M8`](reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) |
| ejemplo | Sí, porque ese error se comete mucho | [`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) |

## Ejemplo mínimo — lo que se puede omitir

Casi ninguna regla necesita todas las partes. La mayoría no tiene excepción, no se apoya en otra y ni siquiera necesita ejemplo. El molde **no obliga a rellenar lo que no hace falta**:

````markdown
## R8 · Mide antes de optimizar

Una optimización se justifica con una medición previa que señale el cuello de
botella. Sin medición, el cambio es una suposición y agrega complejidad sin
evidencia de que sirva.
````

Nombre y cuerpo: eso sí lo lleva toda regla, siempre.

---

## Lo que la regla obliga fuera de su propio texto

Escribir la regla no es el final. Faltan cuatro cosas, y se hacen **en el mismo rato**, no otro día ([`M9`](reglas/M9-toda-regla-declara-si-es-validable.md), [`M10`](reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)):

```
validadores/reglas-validables.md  → ¿un programa puede decir "sí se cumplió" o
                                    "no se cumplió", sin ponerse a opinar?
                                    Sí → se anota ahí y se programa.
                                    No → la revisa el agente leyéndola, y por
                                    eso hay que escribirla con más cuidado:
                                    si se puede discutir, ponle un ejemplo.  M9

CHANGELOG.md                      → se anota el cambio, y de qué tipo es:
                                    MAYOR  los que ya estaban al día tienen
                                           que ponerse a hacer algo nuevo
                                    MENOR  se agrega algo que no estorba a
                                           nadie (una regla opcional, un
                                           capítulo, una plantilla)
                                    PARCHE se explica mejor lo mismo; no
                                           cambia lo que hay que hacer      M10

VERSION                           → se sube el número, según ese tipo       M10

enlaces                           → mirar quién nombraba la regla que se tocó,
                                    y si algún número que se nombra ya no
                                    existe                                  M10
```

Una regla que un programa podría revisar, pero que nadie revisa, es una regla que no se cumple.

## Antes de escribir: el orden

```
1. buscar     ¿ya existe? ¿o basta con explicar mejor una que ya está?
              Es lo más barato, y casi siempre alcanza con eso.         M12
2. enrutar    ¿le sirve a cualquier proyecto, o solo a este?            M13
              ¿es de seguridad, de las que nadie puede saltarse?        M1
              ¿de qué capítulo es el tema?                              M2
3. universal  ¿se puede escribir sin nombrar ninguna herramienta?
              Si no se puede, no es del estándar: es de ese proyecto.   M3
4. número     el siguiente que esté libre en el capítulo                M4
5. escribir   con este molde, pidiendo una sola cosa                    M5
6. releer     el capítulo entero, no solo la regla nueva. ¿Se pelea con
              alguna? Se arregla ahora — no se deja para que después
              alguien tenga que adivinar cuál manda.                    M6
```

Por qué buscar es lo primero: si dos reglas dicen lo mismo con otras palabras, un día alguien arregla una y no la otra. Desde ese día el estándar se contradice solo.
