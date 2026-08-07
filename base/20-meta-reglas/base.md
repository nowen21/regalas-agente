# 20 · Meta-reglas — cómo se estructuran, se leen y se aplican las reglas  ·  `[PREÁMBULO]`

Las reglas de los demás archivos dicen **qué hacer**. Este dice **cómo son las reglas**: dónde vive cada una, qué forma tiene, cuál gana cuando dos chocan, cómo se agrega una nueva sin duplicar ni contradecir lo que ya existe.

**Alcance y límite.** Estas meta-reglas son de **procedimiento** (cómo se lee y se escribe una regla), nunca de **fondo** (qué se permite hacer). No autorizan nada ni relajan nada. Si alguna vez una meta-regla parece habilitar algo que el núcleo (`00-nucleo-blindado.md`) prohíbe, **gana el núcleo** y la meta-regla está mal redactada: reportarlo.

Se lee **antes** que las reglas que gobierna. Se carga sola: cada proyecto ya lee todos los archivos numerados de `base/`.

---

## M1 · La jerarquía tiene cuatro niveles y un solo orden

| Nivel | Qué es | Dónde vive | ¿Se ajusta? |
|---|---|---|---|
| **Preámbulo** | Quién es el agente y cómo funcionan las reglas | `base/00-identidad-y-rol.md`, este archivo | No: describe, no exige. |
| **Capa 1 · Núcleo** | Seguridad innegociable. Cada regla marca `[BLINDADA]` | `base/00-nucleo-blindado.md` | **Nunca.** |
| **Capa 2 · Convenciones** | Buenas prácticas por dominio, agnósticas | `base/01`–`base/NN` | Solo la capa 3. |
| **Capa 3 · Proyecto** | Stack, dominio, sector, nombres propios, reglas del equipo | `CLAUDE.md` + `.agente/` de cada proyecto | Es la capa que ajusta. |

Un nivel **nunca** contradice al de arriba. La capa 3 puede ajustar una convención; ninguna capa toca el núcleo.

```
INCORRECTO: el proyecto declara "aquí sí se puede hacer push sin pedir" (ajusta 00·N2)
CORRECTO:   el proyecto declara "los commits van en inglés" (ajusta 09·G2)
```

## M2 · Un tema, un capítulo, un dueño

Cada dominio tiene **un** archivo `NN-nombre.md` y ese archivo es la **fuente única** de su tema. Si una regla de otro capítulo necesita hablar del mismo tema, **enlaza**, no repite.

**Capítulo nuevo solo si** (las tres): ningún capítulo existente responde esa pregunta, hay al menos **tres** reglas que escribir, y el tema es un dominio de ingeniería —no un caso particular—. Si no se cumplen, la regla entra como una regla más de un capítulo existente.

**La numeración es historia, no prioridad.** Los capítulos se numeran en el orden en que nacen. Un número **no se reutiliza** ni se renumera el resto: los huecos se quedan. Un capítulo que solo aplica a cierta clase de proyecto se marca `[CAPA 2 · opt-in]` en su título y se declara con un toggle en `CLAUDE.md §5.1`.

Si una sola regla crece más de una página, se le abre subcarpeta (`base/02-flujo-de-trabajo/F12/`) y el capítulo deja el resumen y el enlace.

## M3 · La base es agnóstica: sin stack y sin dominio

Una regla de capa 1 o 2 sirve a **cualquier** proyecto. No nombra lenguaje, framework, motor de base de datos, nube, sector ni cliente. Lo concreto se declara en capa 3 (`.agente/stack.md`, `dominio.md`, `mapeo-nombres.md`, `marco-normativo.md`) y la regla lo referencia como concepto.

Si una regla no se puede escribir sin nombrar una tecnología, **no es regla de la base**: es capa 3.

```
INCORRECTO: "usar pytest con cobertura mínima de 80%"
CORRECTO:   "toda unidad entregada lleva pruebas automáticas; el marco y el
             umbral los declara el proyecto (.agente/stack.md)"
```

## M4 · Cada regla tiene un identificador único, estable y prefijado

Formato `<PREFIJO><n>`: prefijo de letras del capítulo + consecutivo (`N4`, `C7`, `G6`, `DOC12`, `DP8`). El prefijo es **exclusivo** de un capítulo; antes de elegir uno nuevo, verificar que esté libre.

Se cita entre capítulos como `NN·ID` — `00·N4`, `09·G6`, `13·DOC3`.

**El ID no cambia nunca.** Ni al reescribir la regla, ni al moverla de sección, ni al cambiarle el título. Es la referencia que usan las specs, los planes, los commits, los validadores y las fases ya cerradas. Renumerar rompe el rastro de todo lo anterior. Si una regla se parte en dos, la original conserva su ID y la nueva toma el siguiente consecutivo libre.

## M5 · Toda regla se escribe en el mismo formato

````
## <PREFIJO><n> · <Título imperativo, entendible sin leer el cuerpo>   [·  `[BLINDADA]` | *opt-in*]

<Qué exige. Una a cuatro líneas, en presente e imperativo. Si extiende o depende
de otra, se declara aquí: (extiende 09·G6).>

```
INCORRECTO: <el error concreto que se ve en la práctica>
CORRECTO:   <qué se hace en su lugar>
```
````

Reglas del formato:

- **Una exigencia por regla.** Si el cuerpo tiene un "y además", son dos reglas.
- **El título se sostiene solo.** Debe poder leerse en un índice y entenderse.
- **El ejemplo es obligatorio** cuando la regla se puede malinterpretar o cuando el error es frecuente. No cuando la regla es evidente.
- **Sin texto prestado.** Lo que ya dice otra regla se enlaza (`ver 04·S4`), no se copia: dos copias se desincronizan.
- **Marcas:** `[BLINDADA]` solo en capa 1; `*opt-in*` cuando la regla no aplica a todo proyecto; `[DEROGADA en X.Y.Z → ver ID]` cuando dejó de regir (`M11`).

## M6 · Ante un conflicto, el desempate es este y en este orden

1. **¿Una es `[BLINDADA]`?** → gana esa. Fin. No hay paso 2.
2. **¿Una es de capa 3 y la otra de capa 2?** → gana la de capa 3, **solo si** el proyecto la declaró como ajuste explícito (`CLAUDE.md §5.1` o `.agente/reglas-proyecto.md`). El silencio no es un ajuste.
3. **¿Una deroga expresamente a la otra?** → gana la que deroga.
4. **Misma capa:** gana la **más específica** — la que nombra el caso — sobre la general.
5. **Igual de específicas:** gana la **más restrictiva**, la que exige más. Ante la duda, el lado seguro.
6. **Sigue empatado** → es un **defecto del estándar**, no una decisión del agente: **PAUSAR**, reportar el choque al usuario y arreglar la regla. Prohibido elegir en silencio o inventar un tercer camino.

```
INCORRECTO: dos reglas se contradicen → elijo la que me deja avanzar y sigo
CORRECTO:   reporto "01·C3 y 02·F7 chocan en este caso" y espero la decisión
```

## M7 · Las dependencias entre reglas se declaran, y solo hay tres

- **`extiende ID`** — agrega detalle a otra sin contradecirla. La extendida sigue rigiendo (`18·DP1 extiende 09·G6`).
- **`depende de ID`** — no se puede cumplir si la otra no se cumplió antes (`13·DOC3 depende de 02·F2`).
- **`deroga ID`** — la reemplaza. Solo dentro de la misma capa y con `M11`.

Se escriben en el cuerpo de la regla, entre paréntesis. **Sin ciclos:** si A depende de B y B de A, una de las dos está mal partida. **Nunca hacia arriba:** una regla de capa 2 no puede extender ni derogar una `[BLINDADA]`.

Un capítulo que se apoya entero en otro lo dice en su encabezado, no regla por regla.

## M8 · La excepción se escribe dentro de la regla que la admite

Una excepción no vive en otro documento ni en el chat: es **parte del texto de la regla**, y declara tres cosas: **condición** (cuándo aplica), **límite** (hasta dónde) y **quién la autoriza**.

- Las `[BLINDADA]` **no admiten excepciones**. Eso es lo que significa blindada.
- Un capítulo `*opt-in*` **no es una excepción**: es una regla que el proyecto activa o no.
- Si aparece un caso que pide una excepción **no escrita**: **PAUSAR y preguntar** (`01·C7`, `00·N1`). Si el usuario la aprueba, se **agrega a la regla** y se versiona (`M10`). No existe la excepción tácita, ni "por esta vez", ni por urgencia.

```
INCORRECTO: "el test tarda mucho, esta vez lo salto y sigo"
CORRECTO:   reporto el costo, propongo el arreglo y espero; si se acepta un
            criterio nuevo, entra escrito en la regla
```

## M9 · Toda regla declara si es validable

Al escribirla, responder: **¿puede un script decir sí/no sin opinar?**

- **Sí** → se registra en `validadores/reglas-validables.md` y se implementa (o queda como pendiente ahí). Una regla validable que nadie valida es una regla que no se cumple.
- **No** → se queda como texto que interpreta el agente, y se escribe con más cuidado: un criterio discutible necesita ejemplo.

Regla derivada: **preferir la redacción verificable**. "El plan lo aprueba el usuario antes de escribir código" se puede comprobar; "trabajar de forma ordenada" no.

## M10 · Todo cambio de regla se versiona y se registra

Cambiar `base/` o `plantillas/` obliga, en el mismo movimiento, a:

1. Entrada en `CHANGELOG.md` con su tipo — **MAYOR** (obliga a hacer algo para cumplir), **MENOR** (aditivo: regla opcional, capítulo opt-in, plantilla, validador), **PARCHE** (redacción o ejemplos).
2. Actualizar `VERSION`.
3. Si la regla es nueva o cambió de exigencia, revisar los enlaces que la citan y `validadores/reglas-validables.md`.

**Retroactividad:** un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. Lo nuevo aplica al trabajo en curso y al que viene. Cada proyecto fija la versión que sigue y el desfase **se avisa**, no se migra solo.

## M11 · Las reglas no se borran: se derogan

Una regla que deja de regir se **marca**, no se elimina:

```
## G4 · Trabaja en ramas, integra limpio   ·  `[DEROGADA en 2.0.0 → ver G9]`
```

Se conserva el texto original debajo de la marca. Motivo: las fases cerradas, las specs y los commits antiguos la citan por su ID; borrarla deja huérfano ese rastro y hace imposible entender por qué algo se hizo así. El ID derogado **no se reutiliza**.

## M12 · Antes de crear una regla, buscar — la duplicación es el defecto más caro

Antes de escribir una regla nueva, en este orden:

1. **Buscar por concepto** en `base/` (no solo por la palabra: el mismo criterio puede estar escrito con otro término).
2. **Revisar el capítulo dueño del tema** (`M2`) de arriba abajo.
3. **Consultar la memoria** (señales) y `pendientes/`: puede estar decidido o en cola.

Y decidir en este orden de preferencia:

1. **Afinar** la redacción o el ejemplo de la regla existente ← lo más barato y lo más frecuente.
2. **Extender**la con una regla nueva que la referencia (`M7`).
3. **Crear** una regla nueva solo si no hay dónde colgarla.

Dos reglas que dicen lo mismo con palabras distintas terminan contradiciéndose cuando una se actualiza y la otra no.

## M13 · Lo que no es regla del estándar tiene su propio sitio

Antes de escribir en `base/`, verificar que ahí es donde va:

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

---

## Cómo se agrega una regla nueva (procedimiento)

1. **Buscar** si ya existe o si basta afinar una (`M12`).
2. **Enrutar:** ¿va en `base/`? (`M13`). ¿Capa 1 o 2? (`M1`). ¿Qué capítulo? (`M2`).
3. **Verificar que es agnóstica** de stack y dominio (`M3`).
4. **Asignar ID** libre del prefijo del capítulo (`M4`).
5. **Escribir** en el formato canónico, una sola exigencia (`M5`).
6. **Declarar** dependencias (`M7`) y excepciones, si las hay (`M8`).
7. **Decidir si es validable** y registrarlo (`M9`).
8. **Versionar:** `CHANGELOG.md` + `VERSION` (`M10`).
9. **Revisar el conjunto:** que no choque con nada; si choca, resolver el choque en el texto, no dejarlo para el desempate (`M6`).

## Higiene del conjunto

- **Tamaño:** si un capítulo pasa de ~15 reglas, probablemente son dos dominios; partirlo (`M2`).
- **Auditoría:** al cerrar un bloque de cambios, releer el capítulo tocado completo — no solo la regla nueva. Las contradicciones aparecen al leer seguido, no al escribir.
- **Enlaces:** una regla que cita a otra por ID depende de que el ID exista. El validador de enlaces lo detecta; no se ignora.
- **Lenguaje:** imperativo, corto, técnico y sin adornos. Lo que el usuario final lee es otra cosa (`17·I4`); estas reglas las lee el agente.
