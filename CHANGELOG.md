# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo.

---

## 2.5.0 — 2026-08-07

**MENOR** (las diecinueve reglas del flujo pasan por el molde y por el checklist; ninguna cambia qué exige).

**El capítulo 02 se somete al estándar, como ya hizo el 20.** `M14` dice que ninguna regla nace fuera del procedimiento y que su cierre es el checklist. Se aplicó a `F0`–`F13`. **Resultado: 9 cumplen, 10 no** — y las diez reprueban por cosas que solo el usuario puede decidir.

**La regla se separó de su explicación.** Cada archivo de `reglas/` conserva **solo la exigencia**: encabezado, cuerpo de una a cuatro líneas, dependencia declarada, excepción con sus tres partes y ejemplo. Todo lo que desarrollaba, ilustraba o justificaba —la tabla de once etapas, la construcción de la línea base, la casuística de migración, el protocolo de `F8`, el mensaje de orientación de `F13`— pasó a `base.md`, a una sección `### F<n>` por regla. `F4.3`, que era la regla más larga del catálogo con 78 líneas, quedó en cinco.

- **`F0` toma el texto corregido que `estructura-regla.md` ya publicaba** desde la v2.2.0 sin que nadie lo aplicara. Convivían dos versiones de la misma regla y ninguna decía cuál mandaba.
- **Los títulos que contaban ahora mandan** (`M5`): `F0 · Recorre la cadena completa, sin saltar eslabones` · `F3 · Ejecuta seguido el plan aprobado` · `F5 · Corre solo las suites que la fase toca` · `F7 · No cierres una fase con trazabilidad incompleta` · `F9 · No subdividas ni renegocies un plan ya aprobado` · `F13 · Detente si el proyecto no tiene su estructura base`, entre otros. **Ningún ID cambió** (`M4`); los archivos se renombraron detrás del título.
- **`F13` pierde la marca inventada** `[GATE DE ARRANQUE · PRECONDICIÓN]`, que el propio `estructura-regla.md` usaba como anti-ejemplo literal. Que corra primero lo dice el capítulo, no una etiqueta.
- **Ocho excepciones que decían cuándo no aplican pero no hasta dónde ni quién autoriza** quedaron completas (`M8`): `F0`, `F2`, `F4`, `F4.2`, `F4.4`, `F9`, `F10`, `F11`.
- **Se rompió el ciclo de dependencias `F4.4 ↔ F4.5`** y la duplicación `F3`/`F9`, que ahora es `extiende 02·F3` (`M7`). El texto que `F5`, `F6` y `F7` copiaban de `08·T5`, `13·DOC1` y `13·DOC3` —ejemplo incluido, palabra por palabra— se reemplazó por el enlace (`M5`).

**Las diez que reprueban, y por qué.** No son defectos de redacción: son decisiones de catálogo, y el catálogo lo decide el usuario.

| Reglas | Fila | Qué falta decidir |
|---|---|---|
| `F4.1`–`F4.5` | 6 | el sub-ID decimal no lo contempla `M4`: legalizarlo o promoverlas a `F14`… |
| `F4`, `F4.3`, `F4.5` | 8 · 9 | llevan dos exigencias que se cumplen por separado; partirlas crea IDs nuevos |
| `F5`, `F6`, `F7` | 2 · 4 | el dueño del tema es `08` y `13`; derogarlas a favor de `T5`, `DOC1` y `DOC3` es `M11` |
| `F12` | 8 · 9 · 10 | su texto está **congelado por decisión del usuario** y el agente no lo reescribe |

Cada una lo dice en su propio archivo, con la marca *"regla vigente y reprobada"* que ya usa `M4`: siguen rigiendo (`M10` — un cambio de norma no reabre lo cerrado), pero no son conformes hasta que se resuelva.

## 2.4.0 — 2026-08-07

**MENOR** (el capítulo 02 pasa a carpeta; ninguna regla cambia qué exige ni qué ID tiene).

**`02 · Flujo de trabajo` se muda a su carpeta.** Era el archivo más grande del estándar —46 KB, catorce reglas y cinco subpartes en un solo `.md`— y ya tenía dos reglas viviendo aparte (`F12/`, `F13/`), así que el capítulo se leía en dos sitios a la vez. Ahora sigue el mismo molde que `00-identidad-y-rol/` y `20-meta-reglas/`: `base.md` es el índice y cada regla tiene su archivo en `reglas/`.

- `base/02-flujo-de-trabajo.md` → `base/02-flujo-de-trabajo/base.md`. Queda como índice: la tabla de las catorce reglas con qué exige cada una, y la secuencia del flujo. De 494 líneas a 36.
- `base/02-flujo-de-trabajo/reglas/` — **una regla, un archivo `<ID>-<título>.md`**, igual que `ID1`–`ID6` y `M1`–`M15`: `F0`–`F13`, más las cinco partes `F4.1`–`F4.5`, con el texto sin reescribir. Sin subcarpetas: `F12/` y `F13/` colgaban del capítulo y eran las únicas reglas fuera del sitio de las reglas.
- `base/02-flujo-de-trabajo/estructura-base.md` — el anexo de `F13` (el árbol obligatorio) pasa a la raíz del capítulo, donde `20-meta-reglas/` ya tiene los suyos (`checklist.md`, `estructura-regla.md`).
- **Las citas se reenlazaron al archivo de destino**, no a un ancla del índice: `02·F5` ahora abre la regla `F5`, no un encabezado dentro de un archivo de 46 KB. Aplica `M15`.

**Efecto en el arranque:** el cargador inyecta el índice de los capítulos temáticos, no su texto. Antes el índice de `02` era una línea de 46 KB; ahora son quince líneas que dicen de qué trata cada regla, y el agente lee **solo la que va a tocar**. El gate `F13` se sigue cargando literal — cambió su ruta (`validadores/cargador.py`).

Lo que **no** cambió: ningún ID, ningún texto de regla, ninguna exigencia. `F12` conserva intacto el texto literal del usuario.

## 2.3.0 — 2026-08-07

**MENOR** (aditivo: una regla nueva y un validador; ningún proyecto que herede el estándar tiene que hacer nada).

**Toda cita a otra regla lleva su enlace.** Citar por ID —`M5`, `09·G6`— obliga a quien lee a salir a buscar: abrir el capítulo, encontrar el encabezado. Con 206 citas repartidas en 43 archivos eso es fricción suficiente para que nadie compruebe nada, y una cita que nadie sigue es una dependencia que nadie verifica.

- `base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md` — la regla. Extiende `M4`, que fija el ID y la forma `NN·ID`.
- **Las 206 citas de `base/` quedan enlazadas**, al archivo y al ancla del encabezado. Las que viven en su propio archivo enlazan al archivo, sin ancla: un ancla de más se rompe al renombrar el título.
- **De paso se normalizaron tres formatos que convivían** — `` `04·S4` ``, `` `00` · N3 `` y `` `00`·N3 `` — a la única forma que `M4` admite. No es un cambio de norma: es aplicar la que ya estaba escrita.

Lo cercado no se tocó: ahí las citas son el molde que alguien va a copiar, no citas a nadie.

Detrás: `validadores/citas.py` (nuevo) — indexa dónde vive cada regla leyendo `base/`, enlaza y valida. Entra en `validar.py estandar`, así que una cita suelta o un enlace a una regla inexistente se reportan solos. 11 pruebas nuevas (191 en total).

## 2.2.0 — 2026-08-07

**MENOR** (las catorce meta-reglas pasan a archivo propio y se les aplica el checklist; ninguna cambia qué exige).

**El capítulo 20 se somete a sí mismo.** `M14` dice que ninguna regla nace fuera del procedimiento y que su cierre es el checklist en `CUMPLE`. Se aplicó a `M1`–`M14`. **Resultado: 10 cumplen, 4 no** — y las cuatro reprueban la misma fila, la 17, que exige decisión del usuario.

**La regla se separó de su explicación.** Cada archivo de `reglas/` conserva **solo la exigencia**: encabezado, cuerpo de una a cuatro líneas, ejemplo y checklist. Lo que desarrollaba, ilustraba o justificaba la regla —tablas, listas de apoyo, el porqué— vuelve a `base.md`, a una sección `### M<n>` por regla, enlazada desde el cuerpo. Con eso las filas 9 (una sola exigencia) y 10 (de una a cuatro líneas) pasan a verde en `M2`, `M5`, `M7` y `M12`, que antes las reprobaban.

**Efecto que conviene tener presente:** varias piezas movidas **mandan**, no solo explican — los tipos MAYOR/MENOR/PARCHE de `M10`, las dos prohibiciones de `M7` (sin ciclos, nunca hacia arriba), las tres aclaraciones de `M8`, el orden de búsqueda de `M12`, la tabla de destinos de `M13`. Siguen siendo texto del capítulo y el agente las lee igual, pero **ya no son texto de una regla citable por ID**. Si alguna debe poder citarse, se promueve a regla propia (`M15`…) — es decisión del usuario.

- `base/20-meta-reglas/reglas/` — las catorce, una por archivo, con el texto sin reescribir. `base.md` queda como capítulo e índice (de 204 líneas a 60).
- Se añadió el ejemplo INCORRECTO/CORRECTO que faltaba en nueve (`M2`, `M4`, `M5`, `M7`, `M9`, `M10`, `M11`, `M12`, `M13`) y el enlace de `M5` a su propio anexo `estructura-regla.md`, que no tenía — rompía la fuente única que `M2` exige.
- `validadores/reglas-validables.md` — las catorce clasificadas (`M9`). Siete se validan **en seco** sobre el propio estándar (`M3`, `M4`, `M5`, `M7`, `M9`, `M10`, `M14`): son las más rentables del catálogo y hoy no existe ninguna.
- `validadores/cargador.py` — el índice listaba las reglas nuevas como "(sin título)": un archivo de una sola regla no lleva `H1`, su encabezado es el `##` de la regla. Ahora lo usa como respaldo.
- `base/00-identidad-y-rol/reglas/` — corregida la aritmética de los seis sellos: eran `17 ✅ · 3 N/A`, no `16 ✅ · 4 N/A`.

**Las cuatro que no cumplen** quedan marcadas en su propio archivo, vigentes y reprobadas (`M10`: un cambio de norma no reabre lo cerrado). Las cuatro reprueban **solo la fila 17** — no choca con ninguna regla vigente:

| Regla | Con qué choca |
|---|---|
| `M2` | no contempla que el preámbulo comparta el número `00` con el núcleo |
| `M4` | no contempla los sub-ID decimales que el catálogo ya usa (`F4.1`–`F4.5`, `F12.1`–`F12.13`) |
| `M7` | el catálogo usa una cuarta forma de dependencia —el bloque `Encadenamiento`— 22 veces |
| `M8` | dice que las `[BLINDADA]` no admiten excepción, y `00·N1` es blindada y tiene una escrita |

Ninguna se puede cerrar sin decidir qué gana: o la meta-regla absorbe la práctica, o la práctica se corrige. Es del usuario.

## 2.1.0 — 2026-08-07

**MENOR** (aditivo: una regla nueva; ningún proyecto que herede el estándar tiene que hacer nada).

**`20·M14` · Ninguna regla nace fuera del procedimiento.** El capítulo tenía trece meta-reglas que gobernaban **cada pieza** de la creación de una regla —dónde va, qué ID lleva, qué forma tiene, cómo se versiona— pero ninguna gobernaba **el acto completo**. El procedimiento de nueve pasos existía como *sección*, sin identificador: no se podía citar desde un commit ni desde una spec, ni exigir por ID. `M14` cierra ese hueco.

Su cierre es el checklist en `CUMPLE`: sin eso la regla no se publica, se corrige o se retira.

- `base/20-meta-reglas/base.md` — la regla, con su checklist aplicado al pie. Se aplicó a sí misma: sería incoherente que la regla que exige el checklist naciera sin él.
- `validadores/reglas-validables.md` — `M14` clasificada (`M9`) como validable parcial: que la regla haya recorrido el procedimiento no lo decide un script, pero su cierre sí — la fila 19 ya la comprueba `version.py`, y la presencia del bloque de checklist es mecánica.

Queda anotado que las otras trece `M` siguen sin evaluar, igual que el resto del catálogo.

## 2.0.0 — 2026-08-07

**MAYOR** · `⚠ obliga a migrar`. Un proyecto al día tiene que correr el instalador **una vez**.

Nada de lo que un proyecto hereda del estándar puede quedarse viejo. Antes se intentaba detectar comparando títulos de sección y fechas de archivo, y las dos cosas fallan: un paso nuevo **dentro** de una sección que ya existía no cambia ningún título, y la fecha miente en cuanto alguien clona el repositorio o edita el archivo por cualquier motivo.

- **El sello.** `CLAUDE.md`, `historico-chat/README.md` y `.agente/stack-instalacion.md` llevan al final `<!-- huella: … · estandar X.Y.Z -->` con la huella de **la plantilla contra la que se sincronizaron** —no la del archivo local, que cada proyecto llena con lo suyo—. Cualquier cambio de la plantilla rompe la coincidencia, venga por dentro o por fuera del documento.
- **Quedar viejo reprueba.** Era AVISO y el componente pasaba igual: un proyecto con el `CLAUDE.md` viejo figuraba como instalación completa.
- **El registro.** Cada actualización deja un `.md` en `documentacion/versiones/`: desde cuándo el proyecto usa esa versión, qué componentes se actualizaron con su huella antes y después, qué aplicó el instalador y qué quedó pendiente. Va en `documentacion/` y no en `.agente/` porque `.agente/` está en el `.gitignore`, y saber bajo qué versión cerró cada fase tiene que poder mirarse desde cualquier copia del repositorio. Componente nuevo del stack: `versiones`.
- **El número de versión deja de reprobar.** Al proyecto no le interesan todos los cambios del estándar, solo los que tiene que aplicar: que declare `1.8.0` con el central en `2.0.0` no obliga a nada por sí solo, y dejarlo en rojo por eso es ruido que enseña a ignorar la alerta. El desfase se informa al margen; `version` ahora solo exige que la versión adoptada esté **declarada**, porque sin ella no hay con qué sellar una fase cerrada.

**Cómo se migra** — la línea de siempre, la del paso 6:

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

Deja los sellos puestos y escribe el primer registro. Hasta que se corra, `claude-md`, `historico` y `stack-instalacion` salen en rojo: no porque el proyecto esté mal, sino porque todavía no declara contra qué versión se sincronizó.

Detrás: `validadores/versiones.py` (nuevo — sellos, comparación y registro), `checklist.py`, `instalar.py`, `validar.py versiones` para verlo a mano, y 19 pruebas nuevas (180 en total).

## 1.6.0 — 2026-08-07

**MENOR.** Ningún proyecto que herede el estándar tiene que hacer nada: la exigencia nueva recae sobre quien escribe reglas **del estándar**.

**El checklist respondido queda dentro del capítulo, en dos piezas.** En 1.5.0 la sección decía lo contrario —que no se persistía copia por regla, para no inflar `base/`—. Se cambia por una razón que pesa más: **que una auditoría posterior no vuelva a analizar lo ya verificado**. La regla cuyo sello dice `CUMPLE` contra la versión vigente se salta; el trabajo se concentra en las que no lo traen o lo traen anulado. Sin esto, cada auditoría reevalúa el catálogo entero desde cero.

Dos piezas, y cada una donde sirve:

1. **El instrumento — `base/20-meta-reglas/checklist.md`, archivo nuevo.** El checklist **es estándar**, así que vive con las meta-reglas, al lado de su `base.md` y como fuente única (`M2`): las 20 filas con su meta-regla y su criterio de aprobado, cómo se decide el resultado, el molde de cómo se aplica, la regla de caducidad, y qué filas puede decidir un script (once) y cuáles piden leer la regla (nueve).
2. **La evaluación — dentro de cada regla.** Al final de su archivo, como `###`: el veredicto, contra qué versión y en qué fecha, el resultado por bloque, las `N/A` justificadas, y **el enlace al instrumento** — para que quien abra una regla suelta sepa de dónde sale esa evaluación. No repite las 20 filas (`M5`).

- `base/20-meta-reglas/base.md` — la sección del checklist queda en resumen + enlace, como ya hacen `F12` y `F13` con sus fuentes únicas.
- `base/00-identidad-y-rol/reglas/` — las seis reglas quedan evaluadas: 16 ✅ · 0 ❌ · 4 N/A · **CUMPLE**.
- `base/00-identidad-y-rol/base.md` — el capítulo lo dice y enlaza el instrumento.

**Backlog que esto abre:** las otras 164 reglas de `base/` quedan **sin sellar**. No es incumplimiento retroactivo —`M10` dice que un cambio de norma no reabre lo cerrado— pero sí es la cola de trabajo: hasta que una regla se selle, sigue entrando en cada auditoría. Se salda por capítulos, no de una vez.

## 1.5.1 — 2026-08-07

**PARCHE** (redacción y una justificación que había quedado falsa; no cambia qué se exige).

Se aplicó el checklist recién agregado a las seis reglas de `00 · Identidad y rol`. **En la primera pasada ninguna cumplía.** El resultado quedó dentro de cada regla, en [`base/00-identidad-y-rol/reglas/`](base/00-identidad-y-rol/reglas/).

- `base/20-meta-reglas/base.md` — la tabla de `M1` describía el preámbulo como *"No: describe, no exige"*. Desde que el capítulo tiene reglas (`ID1`–`ID6`, v1.4.0) esa frase era falsa, y las seis reglas chocaban con `M1` — la fila 17 del checklist. La columna es **¿Se ajusta?**: la respuesta sigue siendo **No** y la precedencia no cambia; lo que se corrigió es la justificación, que ahora dice *"un proyecto no redefine quién es el agente ni el molde de las reglas"*.
- `base/00-identidad-y-rol/reglas/` — `ID1` y `ID6` repetían texto de `01·C14` y de `20·M1` además de enlazarlo (fila 11, `M5` sin texto prestado): ahora difieren en vez de reformular. `ID1`–`ID4` pasaron de tercera persona descriptiva a presente imperativo, que es lo que pide `M5`. `ID5` gana el enlace a `00·N2`, de donde sale que la autorización sea de un solo uso.

Sigue disponible, y es decisión pendiente del usuario, la otra vía para el choque: que el capítulo deje de ser preámbulo y pase a **capa 2**. Eso sí movería la precedencia, y por eso no se tomó por cuenta propia.

## 1.5.0 — 2026-08-07

**MENOR** (aditivo: agrega una comprobación, no cambia ninguna exigencia existente).

- `base/20-meta-reglas/base.md` — sección nueva **«Checklist de la regla — qué cumple y qué no»**, entre el procedimiento de alta y la higiene del conjunto. Veinte filas agrupadas en cinco bloques (dónde va · cómo se identifica · cómo está escrita · cómo se relaciona · qué obliga fuera de su texto), cada una con su meta-regla y su criterio de aprobado, y un resultado al final que dice **CUMPLE** o **NO CUMPLE**.

El criterio de resultado es binario a propósito: una sola fila en ❌ y la regla no se publica. No hay "cumple parcial" — una regla a medias es la que después nadie sabe si rige. Solo cuatro filas admiten `N/A` (ejemplo, dependencias, ciclos y excepción), y siempre con motivo escrito.

Por qué ahí y no en `estructura-regla.md`: el checklist verifica `M1`–`M13` completas, y el anexo solo desarrolla `M5`. Además no cabía dentro de `M5`, que exige cuerpo de una a cuatro líneas.

La sección deja anotado cuáles de las veinte filas puede decidir un script solo (once) y cuáles piden leer la regla (nueve). Esa división es la especificación del validador de meta-reglas que falta.

## 1.4.0 — 2026-08-07

**MENOR** (aditivo: reglas nuevas en un capítulo que no las tenía; nada de lo que ya se cumplía deja de valer).

El capítulo del preámbulo se ajusta al capítulo 20: deja de ser prosa y pasa a tener reglas con identificador.

- `base/00-identidad-y-rol/reglas/` — seis reglas nuevas, **una por archivo**, nombradas `<PREFIJO><n>-<título>`: `ID1` criterio de desarrollador senior · `ID2` registro técnico sin adornos · `ID3` qué cuenta como entregado · `ID4` el ciclo completo de entender a documentar · `ID5` el borde del rol (seis cosas fuera por definición) · `ID6` los roles por etapa no cambian la precedencia.
- `base/00-identidad-y-rol/base.md` — pasa a ser el capítulo con el índice enlazado a las seis. El texto que antes era prosa suelta queda repartido en las reglas; lo que ya decía otro capítulo se enlaza en vez de repetirse (`20·M5`).
- `base/20-meta-reglas/estructura-regla.md` — el prefijo **`ID`** se registra en la tabla de letras ocupadas, como exige `M4` antes de estrenar un prefijo.
- `validadores/reglas-validables.md` — `ID1`–`ID6` clasificadas (criterio humano, `M9`). `ID3` se anota como caso parcial: sus cuatro condiciones ya se validan por separado; lo que no se valida es la conjunción.

Con esto queda cerrada la primera mitad del hallazgo **H-22** del informe de `analisis/`: el capítulo que `02·F0` citaba como fuente de reglas ya tiene reglas citables. Sigue abierto que el número `00` esté compartido con el núcleo.

## 1.3.1 — 2026-08-07

**PARCHE** (no cambia qué se exige; solo dónde vive el texto).

- `base/00-identidad-y-rol.md` pasa a `base/00-identidad-y-rol/base.md`. El capítulo del preámbulo queda con carpeta propia, como `20-meta-reglas/`, para poder crecer con anexos sin inflar el archivo que se carga en cada turno. El texto no cambió.

Detrás: `validadores/cargador.py` decidía qué se carga **literal en todos los turnos** por el nombre del archivo (`00-`, `01-`). Con el capítulo en carpeta, el nombre pasa a ser `base.md` y la identidad del agente habría caído al índice — es decir, el agente arrancaría sin saber quién es. Ahora la comprobación mira el **primer tramo de la ruta**, así que un capítulo del núcleo carga igual viva en archivo suelto o en carpeta.

## 1.3.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). El histórico de sesiones deja de depender de que el agente se acuerde de escribirlo:

- Plantilla nueva: `historico-chat.md` — el `README.md` de la carpeta `historico-chat/` de cada proyecto.
- `CLAUDE.md.plantilla`: punto **2.3** (la carpeta, quién la escribe, se versiona, y cómo excluirla si el chat maneja datos sensibles) y punto **6** ampliado: el instalador es el camino por el que **toda** herramienta nueva del estándar llega al proyecto, sin pasos manuales. Si algo exige configurar a mano, es defecto del estándar.

Detrás: `validadores/hook_historico.py` (enganches `UserPromptSubmit` y `Stop`) e `instalar.py`, que los deja puestos y crea la carpeta. Un proyecto al día no tiene que hacer nada: los recibe la próxima vez que corra el paso 6.

Y el **stack de instalación**: la lista de todo lo que un proyecto debe tener para que el agente esté completo.

- Plantilla nueva: `stack-instalacion.md` — los 11 componentes, qué es cada uno y cómo se instala. Se copia a `./.agente/` de cada proyecto, sellada con la huella del original: si el estándar agrega un componente, la copia deja de coincidir y eso se reporta como actualización pendiente.
- `CLAUDE.md.plantilla`: punto **2.1** (los dos archivos que el estándar escribe en `.agente/` y no se editan a mano) y paso **8** — mientras exista `.agente/INSTALACION-INCOMPLETA.md`, el agente no está completo y debe decir qué falta en cada respuesta. No bloquea: el único gate sigue siendo `F13`.

Detrás: `validadores/checklist.py` (la comprobación de cada componente; la lista se lee de la plantilla, no se duplica en código), `hook_checklist.py` en `UserPromptSubmit`, y `validar.py checklist --raiz` para verlo a mano.

## 1.2.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Un capítulo de **preámbulo**:

- `00 · Meta-reglas` — la regla de reglas: jerarquía de cuatro niveles, organización por dominio con fuente única, orden determinista de desempate ante conflicto, formato canónico de una regla, ID estable, dependencias declaradas (`extiende` / `depende de` / `deroga`), excepciones escritas dentro de la regla, criterio de validable, versionamiento obligatorio, derogación en vez de borrado, y procedimiento para agregar una regla sin duplicar ni contradecir.

No cambia ninguna regla existente: **formaliza** las convenciones que la base ya usaba de hecho y cubre lo que no estaba escrito (desempate, dependencias, derogación, anti-duplicación).

## 1.1.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Dos capítulos **opt-in** de dominio DevOps:

- `18 · Despliegue e infraestructura` — despliegue como artefacto versionado, IaC, build-una-vez, config por entorno fuera del artefacto, release reversible, checklist de despliegue, health/readiness, y correr contra producción gateado por el usuario. Extiende `09·G6`.
- `19 · Observabilidad y operación` — logs estructurados, señales doradas + trazas, SLO/alertas como código sobre síntomas, runbooks, postmortem sin culpa. Extiende `05`.

Plantillas nuevas: `checklist-despliegue.md`, `postmortem.md`. Toggles en `CLAUDE.md.plantilla §5.1`.

## 1.0.0 — 2026-08-06

Primera versión sellada del estándar. Línea base: núcleo blindado (`00`), conducta y flujo (`01`–`02`), buenas prácticas (`03`–`17`), plantillas de capa 3, memoria por señales con vigencia y ciclo de deuda, y la capa de validadores automáticos + hooks.

A partir de aquí, cada cambio de `base/` o `plantillas/` suma una entrada con su tipo.
