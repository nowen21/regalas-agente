# 2026-08-07 — Análisis de cumplimiento de todas las reglas contra `20-meta-reglas`

## Conversación

### 1 · Usuario — hora no registrada
> # Prompt
>
> Cree una carpeta llamada **`analisis`**. Dentro de ella, genere un documento en formato **Markdown (.md)** que contenga el análisis de todas las reglas existentes en el agente, tomando como referencia las reglas definidas en **`20-meta-reglas`**.
>
> ## Objetivo
>
> Validar que todas las reglas del agente cumplan con los estándares, principios y lineamientos establecidos en **`20-meta-reglas`**, identificando fortalezas, incumplimientos y oportunidades de mejora.
>
> ## Actividades
>
> * Analizar todas las reglas existentes en el agente.
> * Evaluar cada regla contra los criterios definidos en **`20-meta-reglas`**.
> * Verificar que cada regla cumpla con el estándar establecido.
> * Identificar reglas incompletas, ambiguas, redundantes o que no se ajusten al estándar.
> * Detectar inconsistencias entre reglas.
> * Identificar reglas que deban unificarse, dividirse, complementarse o eliminarse.
> * Proponer las mejoras necesarias para que todas las reglas sean consistentes con el modelo definido en **`20-meta-reglas`**.
>
> ## Para cada regla analizada indicar, como mínimo:
>
> * Nombre de la regla.
> * Ubicación.
> * Estado de cumplimiento.
> * Meta-regla(s) utilizada(s) para la validación.
> * Criterios evaluados.
> * Hallazgos encontrados.
> * Incumplimientos identificados.
> * Recomendaciones de mejora.
> * Prioridad de la corrección (Alta, Media o Baja).
>
> ## Entregable
>
> Generar un informe de análisis que sirva como evidencia del nivel de cumplimiento del estándar de reglas del agente y como plan de trabajo para corregir las desviaciones encontradas.
>
> El objetivo es que todas las reglas del agente mantengan una estructura homogénea, sean coherentes entre sí y cumplan completamente con los estándares definidos en **`20-meta-reglas`**.

**Agente** — 2026-08-07 08:46:20

Se leyeron los 23 archivos de norma de `base/` (capítulos 00–20, más las fuentes únicas `F12/base.md`, `F13/base.md` y el anexo `estructura-regla.md`), y se contrastaron contra `validadores/reglas-validables.md`, `CHANGELOG.md` y `VERSION`.

**Archivos creados:**

- `analisis/base-2026-08-07-cumplimiento-meta-reglas.md` — el informe.
- `analisis/README.md` — índice de la carpeta y nomenclatura (`<ámbito>-AAAA-MM-DD-<tema>.md`, el patrón de `13·DOC6`).

**Resultado del conteo:** 170 reglas (+13 subpartes `F12.N` = 183 identificadores).

| Estado | Reglas | % |
|---|---|---|
| ✅ Cumple | 48 | 28 % |
| 🟡 Cumple con observaciones | 69 | 41 % |
| ❌ Incumple | 53 | 31 % |

**Diagnóstico de fondo:** el estándar está bien diseñado y desigualmente aplicado. Las 13 meta-reglas cubren lo que tienen que cubrir; el problema es de fecha — el capítulo 20 nació en 1.3.0 y las 157 reglas anteriores nunca se revisaron contra él. Ninguno de los 22 hallazgos pone en duda **qué** exige el estándar: todos son de forma (dónde está escrito, cuántas veces, con qué molde, si un programa puede comprobarlo).

**Los cinco hallazgos que mandan:**

1. **`estructura-regla.md` diseca `F0`, publica la versión corregida completa, y nadie la aplicó.** `F0` sigue con sus 36 líneas, título nominal y excepción sin `autoriza`. Hoy conviven dos textos de `F0` y ninguno declara cuál manda — rompe `M2` en el peor sitio posible.
2. **Existe una cuarta forma de dependencia que `M7` no declara.** El bloque `**Encadenamiento:**` aparece 22 veces en 5 capítulos y es hoy la forma dominante. `M7` solo admite `extiende` / `depende de` / `deroga`. Como consecuencia, su prohibición de ciclos no es comprobable — y `F4.4`↔`F4.5` es un ciclo declarado en prosa.
3. **Cuatro reglas escondidas:** `CQ1`–`CQ4` usan `###`. `estructura-regla.md` nombra exactamente ese error: *"con tres, la regla se esconde: no sale en la lista y el programa que las revisa no la ve"*.
4. **`M8` se contradice con `N1`:** `M8` dice que las `[BLINDADA]` no admiten excepciones; `N1` es blindada y tiene una escrita. Por `M6` paso 6, eso es defecto del estándar y se reporta. El fondo es de vocabulario: `M8` no distingue *excepción* de *condición de autorización*, que es lo que las cuatro blindadas realmente declaran.
5. **`M9` incumplida para 27 reglas:** los capítulos 18, 19 y 20 no aparecen en `reglas-validables.md`, ni como validables ni como no validables.

**Segundo bloque, deuda estructural:** seis pares dicen lo mismo en dos capítulos — `F5`≡`T5` (ejemplo idéntico palabra por palabra), `F6`≡`DOC1`, `F7`≡`DOC3` (ejemplo idéntico), `S7`≡`DEP3`, `DP8`≡`OB6`, y `DOC11` repite entera la tabla de `DOC3` que dice extender.

**Un detalle que revela el método:** `estructura-regla.md` usa `[GATE DE ARRANQUE]` de `F13` como su ejemplo de "inventarse una etiqueta", y `F13` sigue con la marca. Igual que con `F0`: el diagnóstico estaba escrito, con la solución al lado, y el paso que faltó fue aplicarlo.

**Otros hallazgos** (los 22 están en §4 del informe): `base/` nombra tecnologías y rutas reales de un proyecto (`DOC14` con `GitHub`/`VSCode`/`documentacion/prompts/erp/...`, `S11` con `destroy()`/`SoftDeletes`, `D8` con código de un stack); el capítulo 16 se declara opt-in y su Parte A dice "siempre aplica", mientras Parte B prohíbe hardcodear el marco que `CQ3` y `CQ4` hardcodean; `DOC10` cita `P28` —regla de capa 3— desde capa 2, que es la dependencia hacia arriba que `M7` prohíbe; `C14` atribuye a `C1` un texto que `C1` no tiene; 34 reglas rompen "una sola exigencia" (cuatro se autodeclaran múltiples: `F4.5`, `S11`, `T7`, `G8`); `F4.3` tiene 78 líneas sin abrir subcarpeta; 13 de 15 excepciones no dicen quién autoriza; los capítulos 18 y 19 no tienen ni un solo ejemplo; hay 10 formas distintas de escribir la misma cita; el `CHANGELOG` registra el capítulo 20 como `00 · Meta-reglas`.

**Plan de corrección — 5 olas:**

| Ola | Qué | Versión |
|---|---|---|
| 1 | Arreglar las meta-reglas primero (`M8`, `M7`, `M5`, `M4`, `M2`, `M13`) | 1.3.1 PARCHE + 1.4.0 MENOR |
| 2 | Contradicciones y reglas escondidas (`CQ`, cap. 16, `F0`, `F13`, `C14`, `DOC10`) | 1.4.0 MENOR |
| 3 | Consolidar los duplicados — estrena `M11` (derogar, no borrar) | 2.0.0 MAYOR |
| 4 | Agnosticismo, partición de reglas múltiples, excepciones completas, títulos | 2.1.0 MENOR |
| 5 | `validadores/metareglas.py` — valida `M3`, `M4`, `M5`, `M7`, `M9` en seco sobre `base/` | 2.2.0 MENOR |

La Ola 1 va primero porque sin ella cada corrección posterior se hace contra una norma que se contradice. La Ola 5 es la que más importa a largo plazo: sin validador, este informe caduca en la próxima tanda de reglas — que es exactamente lo que `M9` previene cuando dice *"una regla validable que nadie valida es una regla que no se cumple"*.

**Dos decisiones quedaron para el usuario, sin tocar nada:**

1. **`F12`** — su archivo declara *"Texto literal del usuario, 2026-08-03. No se reescribe, no se resume y no se interpreta."* Esa congelación es decisión del usuario y se respeta, pero hoy es una excepción **no escrita** al molde, y `M8` dice que ante una excepción no escrita se pausa y se pregunta. Dos vías: (a) `M5` incorpora la figura de "texto congelado del usuario" con su condición, límite y quién autoriza; (b) las 13 partes se envuelven en el molde `## F12.N · …` **sin tocar una palabra del texto**.
2. **`estructura-regla.md`** — está escrito en registro coloquial (*"Dos gatitos, siempre dos"*, *"como el número de la camiseta"*), y la Higiene del capítulo 20 exige *"imperativo, corto, técnico y sin adornos"*, con `17·I4` reservando el registro sencillo al usuario final. Además `M13` manda los instructivos de mantenimiento del estándar a `CLAUDE.md`, y este archivo se autodescribe como instructivo. Dos vías: se queda en `base/20-meta-reglas/` y se reescribe en registro técnico, o se mueve y el registro coloquial queda legítimo. La segunda decisión condiciona a la primera.

No se ejecutó ninguna corrección: el pedido fue el informe.

### 2 · Usuario — hora no registrada
> cree carpeta de identidad-y-rol

**Agente** — 2026-08-07 09:23:46

Hecho, siguiendo el patrón que ya usa `20-meta-reglas/`: el capítulo entero pasa a su carpeta con `base.md` dentro.

```
base/00-identidad-y-rol.md  →  base/00-identidad-y-rol/base.md
```

Se movió con `git mv`, así que el historial del archivo se conserva. **El texto no cambió** — solo dónde vive.

**Riesgo detectado antes de mover, y arreglado.** `validadores/cargador.py` decidía qué reglas van **literales en cada turno** por el **nombre del archivo**:

```python
if os.path.basename(rel).startswith(NUCLEO):   # NUCLEO = ("00-", "01-")
```

Con el capítulo en carpeta, el nombre pasa a ser `base.md`, que no empieza por `00-`. La identidad habría caído al índice y el agente arrancaría **sin saber quién es**, en silencio y sin señal. Ahora la comprobación mira el **primer tramo de la ruta**:

```python
if rel.split("/")[0].startswith(NUCLEO):
```

Así un capítulo del núcleo carga igual viva en archivo suelto o en carpeta. Comprobado ejecutando el cargador: siguen literales `00-identidad-y-rol/base.md`, `00-nucleo-blindado.md` y `01-conducta.md`, y el resto (23 archivos) sigue solo en índice. La identidad ahora carga **primera**, antes del núcleo, que es el orden correcto: preámbulo antes que capa 1.

**Referencias actualizadas** (las tres que nombraban la ruta vieja):

- `README.md:43` — era un enlace markdown real; se habría roto.
- `base/20-meta-reglas/base.md:15` — la tabla de `M1` (dónde vive el preámbulo).
- `anatomia/mapa-del-sitio.md:40` — el árbol del repo.

Las menciones de `02-flujo-de-trabajo.md` (líneas 15, 16, 42) dicen `` `00-identidad` `` sin ruta ni enlace: siguen válidas. Aparte, el informe de la sesión anterior ya las marcó como hallazgo **H-22** — `F0` las cita en la columna "Dónde está la regla" de un capítulo que **no tiene ninguna regla con ID**. Eso no se tocó: es corrección de la Ola 2, no de este movimiento.

**Versionado** (`M10`, no opcional): `VERSION` 1.3.0 → **1.3.1**, entrada **PARCHE** en `CHANGELOG.md` — no cambia qué se exige, solo dónde vive el texto.

**Comprobación:** `python validadores/validar.py estandar` → `OK: sin incumplimientos`. En la primera corrida salió un enlace roto, pero era del informe de la sesión anterior (una línea que citaba como ejemplo el enlace a añadir en `M5`, con ruta relativa a `base/20-meta-reglas/`, no a `analisis/`); se reescribió para que apunte de verdad.

La carpeta queda con `base.md` solo. Si la idea es desarrollar el capítulo —darle reglas con ID, que hoy no tiene— los anexos entran al lado, como `estructura-regla.md` en `20-meta-reglas/`. Aviso de un efecto del cargador: **todo** `.md` que se ponga en esa carpeta se cargará literal en cada turno, porque el primer tramo empieza por `00-`. Para un anexo largo eso pesa; si se llega a ese caso, conviene decidir entonces si el anexo va ahí o fuera.

### 3 · Usuario — hora no registrada
> suba todo menos lo que dependa de los cambios realizado en base

**Agente** — 2026-08-07 09:30:01

Subido a `main` (`f6e3460..08fe06f`), en cuatro commits con un propósito cada uno (`09·G1`):

| Commit | Qué |
|---|---|
| `6dfeeb1` | `anatomia:` mapa del sitio y componentes del agente |
| `34fce01` | `pendientes:` backlog 09 — autonomía sin IA |
| `bdd4471` | `analisis:` auditoría de las 170 reglas contra las meta-reglas |
| `08fe06f` | `historico:` transcripciones del 06 y 07, memoria e índice |

**Qué quedó fuera, y por qué cada uno depende de `base/`:**

| Archivo | Por qué depende |
|---|---|
| `base/00-identidad-y-rol/base.md` | es el movimiento |
| `validadores/cargador.py` | el arreglo existe solo por el movimiento; sin él, sobra |
| `README.md` | su enlace apunta a la ruta nueva |
| `base/20-meta-reglas/base.md` | la tabla de `M1` nombra la ruta nueva |
| `CHANGELOG.md` · `VERSION` | la entrada 1.3.1 es exactamente ese movimiento |

**Un caso que hubo que deshacer:** el árbol de `anatomia/mapa-del-sitio.md` ya estaba editado con la carpeta nueva. Si subía así, el mapa describiría un repo que no es el que se sube. Se devolvió la línea a `00-identidad-y-rol.md` y el mapa quedó coherente con el `base/` publicado; se vuelve a cambiar cuando suba el movimiento.

**Comprobaciones antes de subir**, no después:

- `validar.py estandar` → `OK: sin incumplimientos` (ningún enlace roto entre lo que se sube y lo que se queda).
- `validar.py secretos` marcó 1 falla y 3 avisos, **todos en archivos ya commiteados** (`validadores/pruebas.py`, `validadores/secretos.py`): son los fixtures del propio validador de secretos. No entraban en esta subida. Queda anotado como cosa a revisar aparte — un fixture con forma de secreto real puede hacer que GitHub bloquee un push futuro.
- Los enganches del repo corrieron en cada commit (`versionado` y `commit`): OK las cuatro veces.
- Se revisó el contenido de cada archivo no rastreado antes de montarlo. Nada se subió sin leer.

También se corrigió una línea del histórico que decía "Commit no solicitado ni hecho" y ya no era cierta.

### 4 · Usuario — hora no registrada
> ajuste: 00-identidad-y-rol a: 20-meta-reglas y cada regla créela dento de la carpeta: 00-identidad-y-rol/reglas con su respectivo: <PREFIJO><n>-<Título> y cada regla va linkiada a 00-identidad-y-ro/base.md

*(y a continuación, dos veces)*

> el informe no lo toque solo agregue el link donde se corrige

**Agente** — 2026-08-07 09:40:39

El capítulo del preámbulo deja de ser prosa suelta y pasa a tener reglas con identificador.

**Prefijo elegido: `ID`.** Se verificó libre contra la tabla de letras ocupadas de `estructura-regla.md` antes de estrenarlo, como exige `M4`, y se registró ahí mismo — la tabla dice que un capítulo nuevo "elige unas letras que no estén en esta lista y **se agrega aquí**".

**Seis reglas, una por archivo**, en `base/00-identidad-y-rol/reglas/`:

| Archivo | Qué exige |
|---|---|
| `ID1-trabaja-con-criterio-de-desarrollador-senior.md` | resolver con el criterio del oficio, no con lo mínimo que funciona |
| `ID2-escribe-en-registro-tecnico-sin-adornos.md` | preciso y sin relleno; el texto del usuario final es lo contrario (`17·I4`) |
| `ID3-no-des-por-entregado-lo-que-no-esta-terminado.md` | spec cumplida + pruebas verdes + nada roto + rastro escrito |
| `ID4-asume-el-ciclo-completo-de-entender-a-documentar.md` | la unidad se entrega entera, no media cadena |
| `ID5-no-salgas-del-borde-del-rol.md` | seis cosas fuera por definición; cada una se autoriza aparte y cada vez |
| `ID6-toma-el-rol-especializado-que-pide-la-etapa.md` | el rol cambia el foco, nunca la precedencia ni el borde |

Cada archivo abre con una línea de vuelta a `../base.md` y sigue el molde de `M5`: encabezado `##` con ID y título imperativo, cuerpo de una a cuatro líneas, y ejemplo INCORRECTO/CORRECTO. `base.md` pasa a ser el capítulo con la tabla índice enlazada a las seis.

**El criterio que gobernó la partición fue `M5` "sin texto prestado".** La prosa original decía cosas que ya tienen dueño en otros capítulos: "en el idioma del proyecto" es `01·C8`, "pruebas en verde" es `08·T5`, "sin romper lo existente" es `02·F7`, "dejando rastro" es `13·DOC1`, y las cinco cosas del "No hace" son `C4`, `N4`, `N2`, `F2` y `S9`. Copiarlas habría creado seis duplicados nuevos — justo el defecto que el informe de esta misma sesión marca como el más caro. Se enlazan. Lo que cada regla aporta de propio es lo que solo este capítulo puede decir: la postura (`ID1`), el registro (`ID2`), la **conjunción** que define "entregado" (`ID3`), el alcance del rol (`ID4`), que el borde es del rol y no un permiso negociable (`ID5`), y que cambiar de rol no cambia las reglas (`ID6`).

**`M9`:** las seis quedan clasificadas en `validadores/reglas-validables.md` como criterio humano, con la nota de que `ID3` es parcial — sus cuatro condiciones ya se validan por separado; lo que ningún script comprueba es la conjunción.

**`M10`:** `VERSION` 1.3.1 → **1.4.0**, entrada **MENOR** en el `CHANGELOG` (aditivo: reglas nuevas donde no había ninguna).

**El informe no se tocó.** Solo se le agregó, al final del hallazgo **H-22**, una línea de "Corregido en" con el enlace al capítulo nuevo — y diciendo qué del hallazgo queda abierto: el número `00` sigue compartido con el núcleo y `F0` sigue citando skills y plantillas como si fueran reglas.

**Comprobado:** `validar.py estandar` → `OK: sin incumplimientos`. El cargador levanta las siete piezas literales en cada turno (`base.md` + las seis reglas), que es lo que corresponde a un preámbulo; el capítulo pasó de ~1 KB a ~4 KB de contexto por turno.

**Lo que quedó pendiente de decisión, y no se tocó:** `20·M1` clasifica el preámbulo como *"No: describe, no exige"*. Con `ID1`–`ID6` el capítulo ahora **sí exige**. Es un choque de los que `M6` manda reportar en vez de resolver en silencio, y arreglarlo significa elegir entre dos cosas — que `M1` acepte que el preámbulo tenga reglas propias, o que el capítulo deje de ser preámbulo y pase a capa 2. Lo segundo cambia la precedencia, así que es decisión del usuario.

### 5 · Usuario — hora no registrada
> en tres palabras que se ha trabajado en esta sesion?

**Agente** — hora no registrada

Auditar, reestructurar, publicar. Auditar las 170 reglas contra el capítulo 20; reestructurar `00-identidad-y-rol` en carpeta con seis reglas `ID1`–`ID6`; publicar seis commits hasta `cdf41e2` (v1.4.0).

### 6 · Usuario — hora no registrada
> En **`20-meta-reglas`**, agregue una tabla para que cada regla creada tenga un **checklist** que permita validar qué partes del estándar de la regla cumple y cuáles no. […] Además, antes de implementarla, indique en qué parte de **`20-meta-reglas`** considera que debería ubicarse esta tabla […] justificando brevemente la propuesta.

**Agente** — hora no registrada

**Ubicación propuesta e implementada:** `base/20-meta-reglas/base.md`, sección nueva entre «Cómo se agrega una regla nueva (procedimiento)» y «Higiene del conjunto». Cuatro razones: (1) el checklist verifica `M1`–`M13` completas y solo `base.md` las tiene —`estructura-regla.md` solo desarrolla `M5`—; (2) el procedimiento dice cómo se agrega y el checklist cómo se comprueba: norma → procedimiento → verificación, y la higiene cierra porque habla del conjunto, no de la regla; (3) no cabía dentro de `M5`, que exige cuerpo de 1 a 4 líneas — la regla del formato incumpliría su propio formato; (4) el destino de `estructura-regla.md` es decisión abierta del usuario (H-21), y anclar ahí un mecanismo nuevo obligaría a moverlo otra vez.

**Veinte filas en cinco bloques:** dónde va (`M13` `M12` `M1` `M2`) · cómo se identifica (`M3` `M4`) · cómo está escrita (`M5`, siete filas) · cómo se relaciona (`M7` `M8` `M6`) · qué obliga fuera de su texto (`M9` `M10` `M4`). Resultado binario: una sola ❌ y la regla no se publica. `N/A` solo en cuatro filas y siempre con motivo. Se anotó cuáles once puede decidir un script y cuáles nueve piden leer la regla — esa división es la especificación del validador que falta.

`M10`: v1.5.0 **MENOR**.

### 7 · Usuario — hora no registrada
> listo aplíquela la nueva actualización a 00-identidad-y-rol

**Agente** — 2026-08-07 11:07:39

Checklist aplicado a `ID1`–`ID6`. **En la primera pasada ninguna de las seis cumplía.**

**Fila 17 (`M6`, no choca con ninguna regla vigente) — reprobaba las seis.** `20·M1` describía el preámbulo como *"No: describe, no exige"* en la columna **¿Se ajusta?**. Desde que el capítulo tiene reglas, esa frase era falsa. La fila no pide elegir bando: pide que el choque quede resuelto **en el texto**. Arreglo mínimo — la respuesta sigue siendo **No** y la precedencia no se movió; se corrigió la justificación, que era la parte falsa:

```
INCORRECTO: | Preámbulo | … | No: describe, no exige. |
CORRECTO:   | Preámbulo | … | No: un proyecto no redefine quién es el agente
                               ni el molde de las reglas. |
```

**Fila 11 (`M5`, sin texto prestado) — dos reglas.** `ID1` parafraseaba `01·C14` **y además** la enlazaba (enlazar y repetir sigue siendo repetir); ahora difiere: *"Dónde queda ese listón cuando el dominio ya lo tiene fijado, lo dice `01·C14`"*. `ID6` reescribía el orden de `20·M1`; ahora queda solo el enlace.

**De paso, redacción:** cuatro cuerpos estaban en tercera persona descriptiva donde `M5` pide presente imperativo (`ID1`–`ID4`). `ID2` repetía "relleno" dos veces. `ID5` ganó el enlace a `00·N2`.

**Resultado tras corregir: las seis CUMPLEN** — 16 ✅, 0 ❌, 4 N/A cada una. Las `N/A` son las que el checklist admite: 14 y 15 (no declaran dependencia `extiende`/`depende de`/`deroga` — sus citas son referencias, que `M5` permite) y 16 (ninguna tiene excepción).

**Constancia** en [`analisis/identidad-y-rol-2026-08-07-checklist.md`](../analisis/identidad-y-rol-2026-08-07-checklist.md), que es donde la propia sección del checklist manda dejarla cuando se evalúa un bloque de reglas — no dentro de `base/`, que se inflaría.

**La fila discutible:** `ID3` exige cuatro cosas (spec, pruebas, nada roto, rastro) y la prueba de la fila 9 —"¿se pueden cumplir por separado?"— da sí. Se resolvió como **una** porque las cuatro ya son reglas con dueño (`02·F2`, `08·T5`, `02·F7`, `13·DOC1`) y partirla crearía cuatro duplicados; lo que `ID3` aporta y ninguna aporta es **la conjunción**. Queda anotado en el análisis por si el criterio se endurece.

**Lo que demostró el ejercicio:** las 9 filas de criterio encontraron los dos defectos; las 11 mecánicas estaban en verde desde el principio. Un validador automático habría dado luz verde a un capítulo que no cumplía.

`M10`: v1.5.1 **PARCHE**. `validar.py estandar` → OK.

### 8 · Usuario — hora no registrada
> no entiendo que fue lo que hizo porque no hizo lo que le pedí. Dígame lo que le pedí

**Agente** — hora no registrada

Se le repitió el pedido literal y las dos lecturas posibles: (a) usar el checklist para **evaluar** `ID1`–`ID6` —lo que se hizo—, o (b) que el checklist quedara **dentro** de `00-identidad-y-rol`. Se listó todo lo que se había tocado, incluidas las correcciones a las seis reglas y a `M1` que no se habían pedido, y se preguntó cuál de las dos era.

### 9 · Usuario — hora no registrada
> pero es que el check list debe estar en la regala con el fin de que si se vuelve a correr un una análisis no se vuelva analizar esas reglas

**Agente** — 2026-08-07 11:15:23

Era la lectura (b), y el **para qué** es lo que faltaba entender: el checklist es un **sello** dentro de la regla, para que una auditoría posterior la vea verificada y la salte.

Eso contradecía lo que se había escrito en 1.5.0 —"no se persiste una copia por regla, veinte checklists inflarían `base/`"—. La razón del usuario pesa más: sin el sello dentro de la regla, **cada auditoría reevalúa el catálogo entero desde cero**. Se cambió la sección.

**Lo hecho:**

- `base/20-meta-reglas/base.md` — la sección del checklist trae ahora el **molde del sello** y tres reglas sobre él: va al final del archivo de la regla; el encabezado es `###` y no `##` (con `##`, un conteo de reglas lo contaría como una regla más); y **editar la regla anula el sello**, aunque el cambio parezca de redacción, porque las filas 8, 9, 10 y 11 se juzgan sobre ese texto.
- Las seis reglas `ID1`–`ID6` quedan selladas: `16 ✅ · 0 ❌ · 4 N/A · RESULTADO: CUMPLE`, con las `N/A` justificadas una por una.
- `analisis/identidad-y-rol-2026-08-07-checklist.md` pasa a ser fotografía: guarda el **razonamiento** (qué falló en la primera pasada, el caso límite de `ID3`), no el estado. El estado vive en el sello. Es el mismo patrón que ya usa `13·DOC8` con los análisis cerrados.

**`M10`:** v1.6.0 **MENOR** — ningún proyecto que herede el estándar tiene que hacer nada; la exigencia recae sobre quien escribe reglas del estándar.

**Lo que esto abre, y quedó dicho en el CHANGELOG:** las otras **164 reglas de `base/` quedan sin sellar**. No es incumplimiento retroactivo (`M10`: un cambio de norma no reabre lo cerrado), pero sí es la cola: hasta que una regla se selle, sigue entrando en cada auditoría.

**Costo que conviene tener presente:** `00-identidad-y-rol/` se carga **literal en cada turno** (es preámbulo), así que los seis sellos viajan en el contexto de todas las sesiones — unos 2 KB que solo sirven para mantener el estándar, no para aplicarlo. Con seis reglas no molesta; si el sello se extiende a los otros 20 capítulos, el cargador tendrá que aprender a recortarlo.

### 10 · Usuario — hora no registrada
> deje el checklist en reglas

> perdon como hermano de base

> si el sello va dentro de cada regla pero el check list va como hermano de base para que cada regla sepa de donde se se que se saca esa evaluación

> el checklist es el standard que debe estar en 20-meta-reglas/checklist.md y cada regla lo aplica como evaluación

**Agente** — 2026-08-07 12:13:46

Cuatro correcciones seguidas porque el agente entendió mal dos veces. El error de fondo: *"hermano de base"* se leyó como el `base.md` del **capítulo evaluado**, cuando era el `base.md` de **`20-meta-reglas`**. De ahí salió un `base/00-identidad-y-rol/checklist.md` que no debía existir.

**Estructura final:**

```
base/20-meta-reglas/
├── base.md          ← M1–M13; la sección del checklist queda en resumen + enlace
├── checklist.md     ← EL INSTRUMENTO · las 20 filas, sus criterios, cómo se aplica
└── estructura-regla.md

base/00-identidad-y-rol/
├── base.md
└── reglas/
    └── ID1…ID6      ← cada una cierra con SU EVALUACIÓN, enlazando al instrumento
```

**Por qué el instrumento va en `20-meta-reglas/`:** el checklist **es estándar**, no resultado. Vive donde vive la norma que comprueba, como fuente única (`M2`), igual que `F12` y `F13` tienen la suya. `base.md` deja solo el resumen y el enlace, que es lo que `M2` manda cuando algo crece más de una página.

**Qué lleva cada regla:** veredicto, contra qué versión y fecha, resultado por bloque, `N/A` justificadas, y **el enlace al instrumento** — que era exactamente el pedido: *"para que cada regla sepa de dónde se saca esa evaluación"*. No repite las 20 filas (`M5`).

**Lo que se deshizo por el camino:** el `checklist.md` del capítulo y el archivo de `analisis/` con el mismo contenido. Los dos eran copias de lo mismo en sitios distintos — el defecto que `M12` llama el más caro. Queda una sola fuente para el instrumento y una sola para cada evaluación.

`validar.py estandar` → OK, tras arreglar dos enlaces que quedaron colgando de los archivos borrados.

**Nota de contexto:** mientras tanto la otra sesión publicó su trabajo — `VERSION` está en **2.0.0** (sellos de instalación, `versiones.py`). No choca con esto: son cambios en archivos distintos. Las evaluaciones dicen "contra v1.6.0" y eso es correcto — es la versión bajo la que se comprobaron, y 2.0.0 no tocó las meta-reglas.

## Abierto

- **Evaluar los otros 20 capítulos** (164 reglas). Se salda por capítulos, no de una vez.
- **Si el sello se generaliza, el cargador debe recortarlo** al inyectar las reglas: es información de mantenimiento, no de aplicación.
- **Sigue disponible la otra vía para el choque de `M1`:** que `00 · Identidad y rol` deje de ser preámbulo y pase a **capa 2**. Eso sí mueve la precedencia (pasaría a ser ajustable por la capa 3), y por eso no se tomó por cuenta propia. El arreglo de v1.5.1 no la cierra.
- Si el checklist debe ser **regla citable** (`M14 · Toda regla nueva pasa su checklist antes de publicarse`) en vez de sección. Hoy es sección, como «Cómo se agrega una regla nueva».
- Decisión del usuario sobre `F12` (texto congelado) y sobre `estructura-regla.md` (registro y ubicación). Hasta que responda, la Ola 2 queda incompleta.
- Aprobación para ejecutar las olas 1 y 2, que sí pueden arrancar sin esas dos respuestas.
- **En el árbol de trabajo, sin subir:** el movimiento de identidad-y-rol, sus seis reglas nuevas, el arreglo de `cargador.py`, las referencias (`README.md`, `20-meta-reglas/base.md`, `estructura-regla.md`), `reglas-validables.md`, el enlace de H-22 en el informe, y `CHANGELOG.md` + `VERSION` 1.4.0. Falta el visto bueno del usuario y volver a poner el árbol de `anatomia/` con la carpeta nueva en ese mismo commit.
- Los fixtures con forma de secreto real en `validadores/pruebas.py` y `validadores/secretos.py`.
