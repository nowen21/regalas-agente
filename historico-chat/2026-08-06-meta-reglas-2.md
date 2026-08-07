# 2026-08-06 — La regla de reglas (`base/00-meta-reglas.md`)

> Transcripción del diálogo. Las horas de los bloques 1–7 y 10–12 no se registraron y no se inventan.
> Los bloques 1–9 estuvieron condensados hasta la interacción 12; aquí quedan ya en su forma literal.

## Conversación

### 1 · Usuario — hora no registrada
> si quisiéramos crear una regla de reglas en dónde debería ir?

**Agente** — hora no registrada

Depende de cuál de las dos "reglas de reglas" quieras, y van en sitios distintos:

**1. Cómo el agente *interpreta* las reglas** (qué gana si dos chocan, qué hacer si un caso no está cubierto, cuándo preguntar en vez de inventar, cómo se activa un opt-in) → **`base/00-meta-reglas.md`**, etiqueta `[PREÁMBULO]`, al lado de `00-identidad-y-rol.md`.

- Se carga sola: el paso 3.1 de `CLAUDE.md.plantilla` manda leer *todos* los archivos numerados de `base/`.
- Alfabéticamente queda entre `identidad` y `nucleo-blindado` — correcto: se lee antes que las reglas que gobierna.
- No va dentro de `00-nucleo-blindado.md`: ese archivo es solo seguridad blindada, meterle meta-reglas le diluye el propósito.

**2. Cómo se *escribe/agrega/cambia* una regla del estándar** (formato del archivo, etiqueta de capa, ejemplo INCORRECTO/CORRECTO, si es validable, bump de `VERSION`+`CHANGELOG`, pasar por `pendientes/`) → **un `CLAUDE.md` en la raíz de este repo**, que hoy no existe.

Esto último es mantenimiento del estándar, no comportamiento en proyectos: si lo pones en `base/` viaja al contexto de todos los proyectos cliente y ahí no sirve de nada. Este repo es a su vez un proyecto cuyo dominio es "redactar reglas", así que su capa 3 propia es el lugar natural.

Mi recomendación si solo vas a crear una: la **1** en `base/00-meta-reglas.md`, porque es la que cambia el comportamiento del agente. ¿Cuál armamos?

### 2 · Usuario — hora no registrada
> y porqué no está grabando en el histórico?

**Agente** — hora no registrada

Porque nada lo obliga: es una preferencia mía, no una regla del sistema.

Concretamente:

- La regla vive en dos sitios blandos: mi memoria (`MEMORY.md` → `historico-chat.md`) y `historico-chat/README.md`. La memoria me llega como contexto de fondo (`<system-reminder>`), no como orden que se ejecuta.
- **No hay regla en `base/`** que lo mande, **no hay hook** que lo dispare, y este repo **no tiene `CLAUDE.md` propio** en la raíz — el mismo hueco del que hablamos hace un momento. Los hooks que sí existen (`.claude/settings.json`) solo revisan enlaces al editar `.md` y el estándar al abrir sesión.
- Encima, el README dice "se escribe **al cerrar** la sesión". Si la sesión no llega a un cierre explícito, nunca se dispara. La entrada de hoy la escribió la sesión anterior; esta todavía no ha escrito nada.

Para que deje de depender de que yo me acuerde, tres opciones de menor a mayor fuerza:

1. **Regla en el `CLAUDE.md` raíz de este repo** (el que no existe): "toda sesión escribe su entrada en `historico-chat/` antes de terminar, y si el trabajo ya quedó firme, antes". Es lo que más pega con lo que te respondí antes.
2. **Hook `Stop`** en `.claude/settings.json` que me recuerde al terminar el turno. El hook no puede redactar la entrada — solo avisar.
3. **Ambas**: la regla manda, el hook recuerda.

Yo iría por la 1 + 3 más adelante. ¿Escribo ya la entrada de esta sesión (decisión sobre dónde va la meta-regla) y de paso armamos el `CLAUDE.md` raíz?

### 3 · Usuario — hora no registrada
> pero en memory hay una regla

**Agente** — hora no registrada

Tienes razón: la regla está en memoria y sí se cargó. El fallo es mío — la traté como "al cerrar sesión" y esta sesión no tuvo cierre. Lo escribo ahora.

*(Escribe `historico-chat/2026-08-06-meta-reglas-2.md` y agrega la línea al índice del README.)*

Listo: `2026-08-06-meta-reglas-2.md` + línea en el índice del README.

Y matizo lo que te dije antes: el README ya contempla el caso ("se escribe al cerrar la sesión, **o antes si el trabajo ya quedó firme**"), así que el hueco no era el texto — era yo esperando un cierre que no llega. Lo que sí sigue siendo cierto es que nada lo fuerza: la regla vive solo en memoria y en ese README, sin respaldo en `base/`, sin `CLAUDE.md` raíz y sin hook.

Sin commitear. Pendiente de tu visto bueno para crear `base/00-meta-reglas.md` y el `CLAUDE.md` raíz.

### 4 · Usuario — hora no registrada
> respecto a la pregunta que le hice sea más claro en su respuesta

**Agente** — hora no registrada

**Va en un archivo nuevo: `base/00-meta-reglas.md`.**

Por qué ahí, en simple:

- Es una regla que el agente debe obedecer siempre → va en `base/`, como todas las demás.
- No es de un tema concreto (datos, git, pruebas…), sino que manda **sobre** los demás archivos → por eso no puede ser `20-…`, tiene que ir arriba, con el `00`.
- Se numera `00` y se marca `[PREÁMBULO]`, igual que `00-identidad-y-rol.md`. Así el agente la lee **antes** que las reglas que gobierna.
- Se carga sola: el `CLAUDE.md` de cada proyecto ya manda leer todos los archivos numerados de `base/`. No hay que tocar nada más.

Ahí adentro escribes cosas como: qué gana cuando dos reglas se contradicen, qué hace el agente si un caso no está cubierto por ninguna regla, cuándo debe preguntar en vez de decidir, cómo se activa una regla opt-in.

Lo único que **no** va ahí es el instructivo de cómo redactar una regla nueva de este repo (formato, subir `VERSION`, actualizar `CHANGELOG`). Eso es mantenimiento del estándar y solo importa cuando trabajas *en este repo*; si lo metes en `base/`, se le cuela a todos los proyectos que usan el estándar sin servirles de nada. Ese instructivo va en un `CLAUDE.md` en la raíz de este repo.

### 5 · Usuario — hora no registrada
> pero no está escribiendo el historial

**Agente** — hora no registrada

El archivo **sí está**: `2026-08-06-meta-reglas-2.md`, escrito a las 15:34 (2.2 KB). Lo que no pasa es que se **actualice solo** con cada mensaje: lo escribí una vez y ahí se quedó, así que ya está desactualizado respecto a lo último que hablamos.

*(Actualiza la entrada y corrige la regla en la memoria del agente.)*

Hecho, dos cosas:

1. **Actualicé la entrada** `2026-08-06-meta-reglas-2.md` con lo último: la respuesta final (`base/00-meta-reglas.md`) y el propio problema de la bitácora.
2. **Corregí la regla en mi memoria**: ya no dice "escribir antes de cerrar la sesión" sino **crear la entrada apenas hay una decisión y actualizarla cada vez que se cierra un tema**. Ese era el defecto: esperar un cierre que en un chat casi nunca ocurre.

Aun así sigue dependiendo de mi memoria. Para que quede amarrado de verdad falta lo que quedó abierto: la regla en el `CLAUDE.md` raíz de este repo. ¿Lo creamos, junto con `base/00-meta-reglas.md`?

### 6 · Usuario — hora no registrada
> no entiendo esto para qué es: 2026-08-06-meta-reglas-2.md ?

**Agente** — hora no registrada

Es la **bitácora de esta conversación**: un resumen de lo que hablamos hoy, guardado en el repo para que no se pierda cuando se cierre el chat.

El nombre se lee por partes:

- `2026-08-06` → la fecha de hoy.
- `meta-reglas` → el tema que tratamos (dónde va una "regla de reglas").
- `-2` → es la **segunda** sesión del día. La primera fue `2026-08-06-historico-chat.md`, la que tienes abierta ahora, donde se creó la carpeta y se trabajó despliegue/observabilidad.

¿Para qué sirve? Mañana o en un mes abres esa carpeta y ves, sin releer ningún chat: qué pediste, qué se hizo, qué se decidió y por qué, y qué quedó sin terminar. El chat se borra; el repo no.

Es la regla que tú mismo pediste en la sesión anterior: *"cree una carpeta historico-chat para que ahí se guarde todo lo que se va haciendo en cada una de las sesiones"*. El formato está definido en `historico-chat/README.md`.

Si te resulta ruidoso tener un archivo por sesión, la alternativa es un solo archivo por día con varias secciones. Dime si lo prefieres así y lo cambio.

### 7 · Usuario — hora no registrada
> pero nada de lo que yo pregunto y usted responde aparece y de eso se trata el histórico

**Agente** — hora no registrada

Entendido: quieres el **diálogo**, no un resumen. Lo reescribo con cada pregunta tuya y cada respuesta mía.

*(Reescribe el archivo como diálogo, cambia la plantilla del README y la regla en memoria.)*

Corregido en los tres sitios:

1. **`2026-08-06-meta-reglas-2.md`** — reescrito como diálogo: tus 7 preguntas citadas literalmente, cada una con su respuesta debajo.
2. **`historico-chat/README.md`** — la plantilla ya no es "qué se pidió / qué se hizo"; ahora es `### N. Usuario` con la cita + `**Agente.**` con la respuesta.
3. **Memoria del agente** — la regla dice explícitamente "es el diálogo, no un resumen ejecutivo".

La respuesta va condensada (la decisión y el porqué), no copiada palabra por palabra, para que el archivo siga siendo leíble. Si lo quieres textual íntegro, dímelo y lo cambio.

Sin commitear.

### 8 · Usuario — 2026-08-06 16:01:44
> debe quedar fecha hora minutos y segundos para que así quede mejor el historial de cada una de las interacciones del usuario y de la IA

**Agente** — 2026-08-06 16:04:30

Agregada la marca de tiempo `AAAA-MM-DD HH:MM:SS` a cada interacción, la del usuario y la del agente. Cambios:

- `historico-chat/README.md` → nueva plantilla con encabezado `### N · Usuario — AAAA-MM-DD HH:MM:SS` y `**Agente** — AAAA-MM-DD HH:MM:SS`; regla explícita de que la hora **se lee del reloj del sistema** (`date "+%Y-%m-%d %H:%M:%S"`), nunca se inventa: una lectura al recibir el mensaje y otra al escribir la respuesta.
- Memoria del agente (`historico-chat.md`) → misma regla, para que aplique en toda sesión futura.
- Este archivo → reformateado. Los bloques 1–7 quedan como "hora no registrada": esas horas no se guardaron y ponerlas de memoria sería inventarlas.
- `2026-08-06-historico-chat.md` (sesión 1) → queda en el formato viejo con una nota que lo advierte; no se puede reconstruir el diálogo literal ni sus horas.

### 9 · Usuario — 2026-08-06 16:02:43
> volvamos a la regla de reglas en dónde iría?

**Agente** — hora no registrada

En **`base/00-meta-reglas.md`** — archivo nuevo, junto a los otros dos `00`.

```
base/
  00-identidad-y-rol.md      [PREÁMBULO]   ← quién es el agente
  00-meta-reglas.md          [PREÁMBULO]   ← NUEVO: cómo se leen las reglas
  00-nucleo-blindado.md      [CAPA 1]      ← seguridad innegociable
  01-conducta.md … 19-…      [CAPA 2]      ← las reglas por tema
```

Va con `00` porque manda **sobre** los otros archivos, así que tiene que leerse antes que ellos. No se carga nada aparte: cada proyecto ya lee todos los archivos numerados de `base/`.

Dentro iría: qué gana cuando dos reglas chocan, qué hace el agente si un caso no lo cubre ninguna regla, cuándo preguntar en vez de decidir solo, y cómo se activa una regla opt-in.

¿Lo creo?

### 10 · Usuario — hora no registrada
> Estoy construyendo la **"regla de reglas"**, es decir, el conjunto de lineamientos que definirá cómo deben estructurarse, organizarse y aplicarse todas las reglas de un agente de IA.
>
> ¿Cuál sería la estructura más adecuada para diseñar estas reglas de manera que el agente sea consistente, escalable, mantenible y fácil de evolucionar?
>
> Me interesa conocer una propuesta de estructura que defina, como mínimo:
>
> * La jerarquía de las reglas.
> * La organización por categorías o dominios.
> * La prioridad entre reglas cuando existan conflictos.
> * El formato estándar que debe tener cada regla.
> * La trazabilidad y versionamiento.
> * Las dependencias entre reglas.
> * Las excepciones y casos especiales.
> * Las buenas prácticas para mantener la coherencia del conjunto.
> * Recomendaciones para facilitar el crecimiento del agente sin generar reglas duplicadas o contradictorias.
>
> El objetivo es definir una arquitectura de reglas sólida que sirva como base para todas las instrucciones futuras del agente. En base/00-meta-reglas.md

**Agente** — 2026-08-06 16:03:55

Voy a escribirlo. Uso el prefijo `M` (libre: ya están ocupados A, C, CFG, D, DEP, DOC, DP, E, EST, F, G, I, IM, N, OB, P, PR, Q, R, S, T) y codifico las convenciones que el estándar ya usa de hecho, más lo que falta (desempate, dependencias, derogación, anti-duplicación).

*(Escribe `base/00-meta-reglas.md`, actualiza `README.md`, `CHANGELOG.md` y `VERSION`.)*

Escrito `base/00-meta-reglas.md` — 13 meta-reglas con prefijo `M` (verifiqué que estuviera libre).

| Lo que pediste | Regla |
|---|---|
| Jerarquía | `M1` — cuatro niveles: preámbulo → núcleo blindado → convenciones → proyecto |
| Categorías / dominios | `M2` — un tema, un capítulo, un dueño; cuándo abrir capítulo nuevo; numeración que no se renumera |
| Prioridad en conflictos | `M6` — desempate determinista de 6 pasos, que **termina en pausa**, no en criterio del agente |
| Formato estándar | `M5` — plantilla canónica: ID · título · una sola exigencia · ejemplo INCORRECTO/CORRECTO |
| Trazabilidad y versionamiento | `M4` (ID estable), `M10` (CHANGELOG + VERSION obligatorios), `M11` (derogar, no borrar) |
| Dependencias | `M7` — solo tres: `extiende` / `depende de` / `deroga`; sin ciclos, nunca hacia el núcleo |
| Excepciones | `M8` — se escriben dentro de la regla con condición, límite y quién autoriza; las blindadas no admiten ninguna |
| Coherencia | `M3` (agnóstica), `M9` (validable o no) + sección de higiene |
| Crecer sin duplicar | `M12` (buscar antes de crear; afinar > extender > crear), `M13` (qué no va en `base/`) |

Las tres decisiones que sostienen el diseño:

- **Las meta-reglas son de procedimiento, no de fondo.** No autorizan nada. Si una parece habilitar algo que el núcleo prohíbe, gana el núcleo. Si no, el preámbulo se vuelve una puerta trasera sobre la capa blindada.
- **El agente no resuelve contradicciones en silencio.** El paso 6 de `M6` es pausar y reportar: un empate real es un defecto del estándar, no una decisión de ejecución.
- **Nada se renumera ni se borra.** Specs, planes, commits y fases cerradas citan por ID; renumerar destruye el rastro hacia atrás.

Cumplí `M10` con el propio cambio: `CHANGELOG.md` → **1.2.0** (MENOR, aditivo), `VERSION` → `1.2.0`, línea en el índice del README y bloque 9 en el histórico.

Sin commitear. Queda abierto el `CLAUDE.md` raíz del repo, que es donde va el instructivo de autoría (`M13`) — ¿lo hago?

### 11 · Usuario — hora no registrada
> según la regla de regla como quedaría una?

**Agente** — hora no registrada

Así. Ejemplo real: una regla nueva para el capítulo `08 · Pruebas` (última existente: `T7` → toca `T8`).

**El texto que se escribe en `base/08-pruebas.md`:**

````markdown
## T8 · Todo bug se arregla con una prueba que falla antes

Antes de tocar el código que causa el bug, escribe la prueba que lo reproduce
y compruébala en rojo. Recién ahí, el arreglo. Una prueba que nunca falló no
demuestra que el bug esté corregido. (depende de 02·F2)

**Excepción:** si el bug no es reproducible en el entorno de pruebas, se
documenta por qué en el cierre de la fase (13·DOC2) y lo aprueba el usuario.

```
INCORRECTO: arreglo el código, corro las pruebas, todas en verde, cierro
CORRECTO:   prueba que reproduce el bug → rojo → arreglo → verde → cierro
```
````

**Por qué queda así, meta-regla por meta-regla:**

| Meta-regla | Cómo se cumple |
|---|---|
| `M2` | El tema es pruebas → va en el capítulo dueño, no en uno nuevo |
| `M3` | No nombra pytest, JUnit ni framework: solo "prueba" |
| `M4` | `T8` = prefijo del capítulo + siguiente consecutivo libre |
| `M5` | Título que se entiende solo · una sola exigencia · ejemplo contrastado |
| `M7` | Declara `(depende de 02·F2)`: sin spec no hay bug definido |
| `M8` | La excepción va **dentro** de la regla, con condición y quién autoriza |
| `M9` | ¿Validable? Un script puede exigir que el commit del fix traiga prueba nueva → sí, entra a `validadores/reglas-validables.md` |
| `M10` | Al agregarla: `CHANGELOG.md` como **MAYOR** (obliga a hacer algo nuevo) + `VERSION` |

Lo que la haría **incorrecta**: poner "y además usa mocks para las dependencias externas" (serían dos reglas, `M5`), decir "usar pytest" (`M3`), o dejar la excepción como algo que se decide en el chat en vez de escrita (`M8`).

¿La agrego de verdad, o era solo para ver el molde?

### 12 · Usuario — hora no registrada
> era para ver el ejemplo de la regla

**Agente** — hora no registrada

Perfecto — era solo el molde, no toco nada.

Resumen de la sesión, para cerrar:

- **Creado**: `base/00-meta-reglas.md` con las 13 meta-reglas (`M1`–`M13`).
- **Actualizado**: `README.md` (índice), `CHANGELOG.md` → `1.2.0` MENOR, `VERSION` → `1.2.0`, e `historico-chat/2026-08-06-meta-reglas-2.md`.
- **Sin commitear**: esto y el trabajo de despliegue/observabilidad de la sesión anterior.
- **Abierto**: el `CLAUDE.md` raíz del repo (instructivo de autoría de reglas + obligación del histórico).

### 13 · Usuario — hora no registrada
> no es resumen es cada una de la cosas que escribo y lo que responde la IA

**Agente** — 2026-08-06 16:11:29

Corregido. El histórico deja de ser diálogo condensado y pasa a ser **transcripción literal**: cada mensaje del usuario tal como lo escribió y cada respuesta del agente tal como la dio, con sus tablas, bloques de código y ejemplos completos. Lo único que se omite es la salida cruda de herramientas, que no es diálogo.

Cambios:

- `historico-chat/README.md` → la regla ahora dice "transcripción del diálogo, no un resumen" y exige que **ambos lados vayan literales**, sin condensar ni parafrasear.
- Memoria del agente (`historico-chat.md`) → misma corrección.
- Este archivo → reescrito completo. Los bloques 1–12, que estaban condensados, quedan con la respuesta íntegra que se dio en el chat.

### 14 · Usuario — hora no registrada
> acá tambien actuliza?

**Agente** — 2026-08-06 16:17:52

*(Pregunta a cuál archivo se refiere; el usuario responde: `2026-08-06-historico-chat.md`.)*

Sí. Pasé la entrada de la sesión 1 al mismo formato de transcripción: el mensaje del usuario literal (*"cree una carpeta: historico-chat…"*) y mi respuesta literal debajo.

Dos límites, dichos sin maquillar:

- Las horas de esa sesión no se registraron → quedan como "hora no registrada".
- El trabajo de despliegue/observabilidad (`base/18`, `base/19`) es **anterior** a esa sesión y a la regla del histórico: no existe transcripción de él. Queda como inventario de archivos, con una nota al principio que lo advierte. Reconstruir ese diálogo sería inventarlo.

También actualicé las dos líneas del índice del `README.md` para que coincidan con los títulos nuevos.

### 15 · Usuario — hora no registrada
> pero cada que abra una sesion le tengo que decir que grabe lo que interactuamos?

**Agente** — 2026-08-06 16:20:19

No. Y hasta ahora dependía de que yo me acordara, que es exactamente por qué falló hoy tres veces.

*(Crea `CLAUDE.md` en la raíz del repo.)*

Creado **`CLAUDE.md`** en la raíz. Claude Code lo lee solo al abrir sesión en esta carpeta, así que la obligación entra al contexto sin que el usuario diga nada. Antes la regla vivía en dos sitios blandos: mi memoria (contexto de fondo, no orden) y `historico-chat/README.md` (que no se lee salvo que alguien lo abra).

Por qué el hook `SessionStart` no bastaba: `validadores/hook_sesion.py` sale con `return 0` cuando la raíz es la del propio estándar (línea 43) — el estándar no se revisa a sí mismo como si fuera un proyecto. En este repo ese hook no inyecta nada.

Lo que quedó escrito en el `CLAUDE.md` raíz:

| Sección | Contenido |
|---|---|
| 1 | El histórico es obligatorio: crear apenas hay una decisión, actualizar **después de cada intercambio**, transcripción literal, marca de tiempo leída del reloj, `hora no registrada` cuando no se tomó |
| 2 | Autoría de reglas: el procedimiento de `00-meta-reglas.md`, y que `CHANGELOG` + `VERSION` no son opcionales (`M10`) |
| 3 | Tabla de enrutamiento: qué va en `base/`, `notas/`, `pendientes/`, `historico-chat/`, memoria |
| 4 | No commitear sin aprobación; formato del cuerpo del commit |

Con esto se cierra el pendiente que arrastraba la sesión desde el bloque 2.

Queda opcional el hook `Stop` como recordatorio, pero ya no hace falta para que la regla exista: el hook solo avisa, no redacta.

## Abierto

- Opcional: hook `Stop` en `.claude/settings.json` como recordatorio del histórico (el hook avisa, no redacta).
- Sin commitear: todo lo de hoy más el trabajo de despliegue/observabilidad de la sesión anterior.
