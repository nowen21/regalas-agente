# 20 · Meta-reglas — cómo se estructuran, se leen y se aplican las reglas  ·  `[PREÁMBULO]`

Las reglas de los demás archivos dicen **qué hacer**. Este dice **cómo son las reglas**: dónde vive cada una, qué forma tiene, cuál gana cuando dos chocan, cómo se agrega una nueva sin duplicar ni contradecir lo que ya existe.

**Alcance y límite.** Estas meta-reglas son de **procedimiento** (cómo se lee y se escribe una regla), nunca de **fondo** (qué se permite hacer). No autorizan nada ni relajan nada. Si alguna vez una meta-regla parece habilitar algo que el núcleo (`00-nucleo-blindado.md`) prohíbe, **gana el núcleo** y la meta-regla está mal redactada: reportarlo.

Se lee **antes** que las reglas que gobierna. Se carga sola: cada proyecto ya lee todos los archivos numerados de `base/`.

---

**Una regla, un archivo.** Cada meta-regla vive en su propio archivo dentro de [`reglas/`](reglas/), con el nombre `<PREFIJO><n>-<título>`. El prefijo del capítulo es **`M`** y es exclusivo suyo ([`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).

| Regla | Qué dice |
|---|---|
| [`M1 · La jerarquía tiene cuatro niveles y un solo orden`](reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) | Cuatro niveles y un solo orden; un nivel nunca contradice al de arriba. |
| [`M2 · Un tema, un capítulo, un dueño`](reglas/M2-un-tema-un-capitulo-un-dueno.md) | Un tema, un capítulo, un dueño. Lo que ya dice otro capítulo se enlaza. |
| [`M3 · La base es agnóstica: sin stack y sin dominio`](reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) | La base sirve a cualquier proyecto: sin lenguaje, framework, sector ni cliente. |
| [`M4 · Cada regla tiene un identificador único, estable y prefijado`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) | `<PREFIJO><n>`, prefijo exclusivo del capítulo. El ID no cambia nunca. |
| [`M5 · Toda regla se escribe en el mismo formato`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) | Encabezado, cuerpo de 1 a 4 líneas, una sola exigencia, ejemplo y marca. |
| [`M6 · Ante un conflicto, el desempate es este y en este orden`](reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) | Seis pasos de desempate; si sigue empatado es defecto del estándar, no decisión del agente. |
| [`M7 · Las dependencias entre reglas se declaran, y solo hay tres`](reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) | `extiende` · `depende de` · `deroga`. Sin ciclos y nunca hacia arriba. |
| [`M8 · La excepción se escribe dentro de la regla que la admite`](reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) | Condición, límite y quién autoriza — dentro de la regla. Las `[BLINDADA]` no admiten. |
| [`M9 · Toda regla declara si es validable`](reglas/M9-toda-regla-declara-si-es-validable.md) | ¿Puede un script decir sí/no sin opinar? Se registra en `validadores/reglas-validables.md`. |
| [`M10 · Todo cambio de regla se versiona y se registra`](reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) | `CHANGELOG.md` + `VERSION` en el mismo movimiento. No reabre lo ya cerrado. |
| [`M11 · Las reglas no se borran: se derogan`](reglas/M11-las-reglas-no-se-borran-se-derogan.md) | Se marca `[DEROGADA]` y se conserva el texto; el ID no se reutiliza. |
| [`M12 · Antes de crear una regla, buscar — la duplicación es el defecto más caro`](reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md) | Buscar por concepto antes de crear: afinar, extender, y solo entonces crear. |
| [`M13 · Lo que no es regla del estándar tiene su propio sitio`](reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) | Antes de escribir en `base/`, verificar que ahí es donde va. |
| [`M14 · Ninguna regla nace fuera del procedimiento`](reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) | El acto completo: los nueve pasos, con el checklist en CUMPLE como cierre. |
| [`M15 · Toda cita a otra regla lleva su enlace`](reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) | Citar por ID no basta: la cita se escribe como enlace al sitio exacto. |
| [`M16 · Toda regla de proyecto nombra la regla de base que concreta`](reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) | La capa 3 concreta un criterio de la base; si no existe, se crea en la base primero. |

Además del catálogo, este capítulo tiene el molde de una regla parte por parte ([`estructura-regla.md`](estructura-regla.md)) y el instrumento con que se comprueba ([`checklist.md`](checklist.md)).

---

## Detalle de cada regla

Lo que desarrolla, ilustra o justifica cada meta-regla. La **exigencia** vive en su archivo de [`reglas/`](reglas/); esto es su explicación.

### M1 — los cuatro niveles

| Nivel | Qué es | Dónde vive | ¿Se ajusta? |
|---|---|---|---|
| **Preámbulo** | Quién es el agente y cómo funcionan las reglas | `base/00-identidad-y-rol/`, este capítulo | No: un proyecto no redefine quién es el agente ni el molde de las reglas. |
| **Capa 1 · Núcleo** | Seguridad innegociable. Cada regla marca `[BLINDADA]` | `base/00-nucleo-blindado.md` | **Nunca.** |
| **Capa 2 · Convenciones** | Buenas prácticas por dominio, agnósticas | `base/01`–`base/NN` | Solo la capa 3. |
| **Capa 3 · Proyecto** | Stack, dominio, sector, nombres propios, reglas del equipo | `CLAUDE.md` + `.agente/` de cada proyecto | Es la capa que ajusta. |

### M2 — cuándo nace un capítulo, y por qué los números no se reciclan

**Capítulo nuevo solo si** (las tres): ningún capítulo existente responde esa pregunta, hay al menos **tres** reglas que escribir, y el tema es un dominio de ingeniería —no un caso particular—. Si no se cumplen, la regla entra como una regla más de un capítulo existente.

**La numeración es historia, no prioridad.** Los capítulos se numeran en el orden en que nacen. Un número **no se reutiliza** ni se renumera el resto: los huecos se quedan. Un capítulo que solo aplica a cierta clase de proyecto se marca `[CAPA 2 · opt-in]` en su título y se declara con un toggle en `CLAUDE.md §5.1`.

Si una sola regla crece más de una página, se le abre subcarpeta (`base/02-flujo-de-trabajo/reglas/F12/`) y el capítulo deja el resumen y el enlace.

### M4 — cómo se cita, y por qué el ID no se toca

Se cita entre capítulos como `NN·ID` — [`00·N4`](../00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada), [`09·G6`](../09-git.md#g6--integración-continua-el-verde-es-automático-no-manual), [`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md).

El ID es la referencia que usan las specs, los planes, los commits, los validadores y las fases ya cerradas. Renumerar rompe el rastro de todo lo anterior. Si una regla se parte en dos, la original conserva su ID y la nueva toma el siguiente consecutivo libre.

### M5 — el molde, y sus cinco reglas de formato

````
## <PREFIJO><n> · <Título imperativo, entendible sin leer el cuerpo>   [·  `[BLINDADA]` | *opt-in*]

<Qué exige. Una a cuatro líneas, en presente e imperativo. Si extiende o depende
de otra, se declara aquí: (extiende 09·G6).>

```
INCORRECTO: <el error concreto que se ve en la práctica>
CORRECTO:   <qué se hace en su lugar>
```
````

- **Una exigencia por regla.** Si el cuerpo tiene un "y además", son dos reglas.
- **El título se sostiene solo.** Debe poder leerse en un índice y entenderse.
- **El ejemplo es obligatorio** cuando la regla se puede malinterpretar o cuando el error es frecuente. No cuando la regla es evidente.
- **Sin texto prestado.** Lo que ya dice otra regla se enlaza (`ver 04·S4`), no se copia: dos copias se desincronizan.
- **Marcas:** `[BLINDADA]` solo en capa 1; `*opt-in*` cuando la regla no aplica a todo proyecto; `[DEROGADA en X.Y.Z → ver ID]` cuando dejó de regir ([`M11`](reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

Desarrollado parte por parte, con la tabla de prefijos ocupados: [`estructura-regla.md`](estructura-regla.md).

### M7 — qué significa cada dependencia, y sus dos prohibiciones

- **`extiende ID`** — agrega detalle a otra sin contradecirla. La extendida sigue rigiendo (`18·DP1 extiende 09·G6`).
- **`depende de ID`** — no se puede cumplir si la otra no se cumplió antes (`13·DOC3 depende de 02·F2`).
- **`deroga ID`** — la reemplaza. Solo dentro de la misma capa y con [`M11`](reglas/M11-las-reglas-no-se-borran-se-derogan.md).

**Sin ciclos:** si A depende de B y B de A, una de las dos está mal partida. **Nunca hacia arriba:** una regla de capa 2 no puede extender ni derogar una `[BLINDADA]`.

Un capítulo que se apoya entero en otro lo dice en su encabezado, no regla por regla.

### M8 — qué no es una excepción, y qué hacer con una no escrita

- Las `[BLINDADA]` **no admiten excepciones**. Eso es lo que significa blindada.
- Un capítulo `*opt-in*` **no es una excepción**: es una regla que el proyecto activa o no.
- Si aparece un caso que pide una excepción **no escrita**: **PAUSAR y preguntar** ([`01·C7`](../01-conducta.md#c7--ante-dos-lecturas-pregunta), [`00·N1`](../00-nucleo-blindado.md#n1--no-ejecutar-sin-validación-blindada)). Si el usuario la aprueba, se **agrega a la regla** y se versiona ([`M10`](reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)). No existe la excepción tácita, ni "por esta vez", ni por urgencia.

### M9 — qué se sigue de cada respuesta

- **Sí** → se registra en `validadores/reglas-validables.md` y se implementa (o queda como pendiente ahí). Una regla validable que nadie valida es una regla que no se cumple.
- **No** → se queda como texto que interpreta el agente, y se escribe con más cuidado: un criterio discutible necesita ejemplo.

De ahí se sigue **preferir la redacción verificable**: "el plan lo aprueba el usuario antes de escribir código" se puede comprobar; "trabajar de forma ordenada" no.

### M10 — los tipos, qué más se revisa, y la retroactividad

- **MAYOR** — obliga a hacer algo para cumplir.
- **MENOR** — aditivo: regla opcional, capítulo opt-in, plantilla, validador.
- **PARCHE** — redacción o ejemplos.

Si la regla es nueva o cambió de exigencia, revisar además los enlaces que la citan y `validadores/reglas-validables.md`.

**Retroactividad:** un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. Lo nuevo aplica al trabajo en curso y al que viene. Cada proyecto fija la versión que sigue y el desfase **se avisa**, no se migra solo.

### M11 — por qué se derogan en vez de borrarse

Las fases cerradas, las specs y los commits antiguos citan la regla por su ID; borrarla deja huérfano ese rastro y hace imposible entender por qué algo se hizo así.

### M12 — el orden de búsqueda y el de decisión

Buscar, en este orden:

1. **Por concepto** en `base/` — no solo por la palabra: el mismo criterio puede estar escrito con otro término.
2. **El capítulo dueño del tema** ([`M2`](reglas/M2-un-tema-un-capitulo-un-dueno.md)), de arriba abajo.
3. **La memoria** (señales) y `pendientes/`: puede estar decidido o en cola.

Y decidir, en este orden de preferencia:

1. **Afinar** la redacción o el ejemplo de la regla existente ← lo más barato y lo más frecuente.
2. **Extender**la con una regla nueva que la referencia ([`M7`](reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)).
3. **Crear** una regla nueva solo si no hay dónde colgarla.

Dos reglas que dicen lo mismo con palabras distintas terminan contradiciéndose cuando una se actualiza y la otra no.

### M13 — dónde va cada cosa

| Si es… | Va en… |
|---|---|
| Regla que aplica a **cualquier** proyecto | `base/` (capa 1 o 2) |
| Regla de **este** proyecto (convención del equipo, regla de negocio) | `.agente/reglas-proyecto.md` del proyecto (capa 3) |
| Instructivo para **mantener el estándar** (cómo redactar, qué versionar) | `CLAUDE.md` raíz del repo del estándar |
| **Por qué** se diseñó algo así (razonamiento, alternativas) | `notas/` |
| Mejora acordada pero **aún no hecha** | `pendientes/` |
| Preferencia del usuario sobre cómo trabajar | memoria del agente |
| Qué pasó en una sesión | `historico-chat/` |

Meter en `base/` lo que no es regla universal la infla y se lo impone a todos los proyectos que heredan el estándar.

### M16 — el respaldo es del criterio, no del detalle

La base no puede llevar el detalle de un proyecto ([`M3`](reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)) y la capa 3 no puede inventar criterios que la base no tiene. Las dos cosas se sostienen porque cada una pone una mitad: la base dice **qué hay que decidir**, la regla `P` dice **con qué valor se decide aquí**.

| Capa | Qué pone | Ejemplo |
|---|---|---|
| Base (capa 2) | El criterio, sin valores ni nombres propios | [`06·R4`](../06-rendimiento.md#r4--cachea-lo-caro-y-estable-con-invalidación-clara) · lo caro y estable se cachea, con invalidación clara |
| Proyecto (capa 3) | El valor concreto, citando ese criterio | `P4` · el catálogo se cachea 10 minutos, y se invalida al publicar |

Cuando la regla que pide el proyecto no encaja en ningún criterio de la base, casi siempre es que el criterio sí es universal y todavía no está escrito: se escribe en `base/` sin el detalle del proyecto, y la `P` queda como su valor local. Si al quitarle el detalle no queda nada que valga para otro proyecto, no era una regla: era una decisión de configuración, y va donde va la configuración.

Esto también le pone freno a la capa 3. Un catálogo que crece con reglas sueltas termina siendo un estándar paralelo, sin checklist, sin versión y sin nadie que lo audite.

## Cómo se agrega una regla nueva (procedimiento)

1. **Buscar** si ya existe o si basta afinar una ([`M12`](reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)).
2. **Enrutar:** ¿va en `base/`? ([`M13`](reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)). ¿Capa 1 o 2? ([`M1`](reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)). ¿Qué capítulo? ([`M2`](reglas/M2-un-tema-un-capitulo-un-dueno.md)).
3. **Verificar que es agnóstica** de stack y dominio ([`M3`](reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)).
4. **Asignar ID** libre del prefijo del capítulo ([`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).
5. **Escribir** en el formato canónico, una sola exigencia ([`M5`](reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)).
6. **Declarar** dependencias ([`M7`](reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)) y excepciones, si las hay ([`M8`](reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md)).
7. **Decidir si es validable** y registrarlo ([`M9`](reglas/M9-toda-regla-declara-si-es-validable.md)).
8. **Versionar:** `CHANGELOG.md` + `VERSION` ([`M10`](reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
9. **Revisar el conjunto:** que no choque con nada; si choca, resolver el choque en el texto, no dejarlo para el desempate ([`M6`](reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md)).

## Checklist de la regla — qué cumple y qué no

El procedimiento de arriba dice cómo se agrega una regla. El **checklist** dice si quedó bien: veinte filas, cada una con la meta-regla que la respalda y su criterio de aprobado, y un resultado que dice **CUMPLE** o **NO CUMPLE**. Una sola fila en ❌ y la regla no se publica.

Instrumento completo (fuente única): [`checklist.md`](checklist.md).

Se aplica al escribir la regla —**paso 9** del procedimiento— y su resultado se escribe **dentro de la regla**, al final de su archivo, enlazando al instrumento. Así una auditoría posterior no vuelve a analizar lo ya verificado, y quien abre una regla suelta ve de dónde sale su evaluación. Editar la regla **anula** el resultado (`checklist.md` §3).

## Higiene del conjunto

- **Tamaño:** si un capítulo pasa de ~15 reglas, probablemente son dos dominios; partirlo ([`M2`](reglas/M2-un-tema-un-capitulo-un-dueno.md)).
- **Auditoría:** al cerrar un bloque de cambios, releer el capítulo tocado completo — no solo la regla nueva. Las contradicciones aparecen al leer seguido, no al escribir.
- **Enlaces:** una regla que cita a otra por ID depende de que el ID exista. El validador de enlaces lo detecta; no se ignora.
- **Lenguaje:** imperativo, corto y sin adornos, y en palabras de todos los días: la regla también se escribe para que la entienda quien no sabe del tema ([`00·ID7`](../00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)). El término técnico que no se pueda evitar se explica la primera vez, y la precisión no se sacrifica. Lo que lee el usuario final del producto tiene además su propia regla ([`17·I4`](../17-interfaz.md#i4--texto-para-el-usuario-no-jerga)).
