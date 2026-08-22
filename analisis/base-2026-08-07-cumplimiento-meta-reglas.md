# Análisis de cumplimiento del estándar de reglas contra `20 · Meta-reglas`

> **Qué es esto.** Auditoría de las **170 reglas** de `base/` (capítulos 00–20) contra las **13 meta-reglas** de [`base/20-meta-reglas/base.md`](../base/20-meta-reglas/base.md) y el molde de [`base/20-meta-reglas/estructura-regla.md`](../base/20-meta-reglas/estructura-regla.md).
>
> **Para qué sirve.** Dos cosas: (1) evidencia del nivel de cumplimiento del propio estándar, (2) plan de trabajo priorizado para cerrar las desviaciones.
>
> **Alcance.** Solo `base/`. No se auditan `plantillas/`, `skills/`, `validadores/` ni la capa 3 de los proyectos.
>
> Estándar **v1.3.0** · análisis del **2026-08-07** · fotografía del estado en esa fecha (`M10`: al cambiar reglas, se revisa).

---

## 1 · Resumen ejecutivo

El estándar **define bien la norma y la cumple a medias**. Las meta-reglas son coherentes entre sí y el procedimiento de alta de regla está completo; lo que falla es la **aplicación retroactiva** del molde a las reglas que nacieron antes del capítulo 20.

| Estado | Reglas | % |
|---|---|---|
| ✅ **Cumple** — molde, tamaño, unicidad de exigencia y dependencias correctos | 48 | 28 % |
| 🟡 **Cumple con observaciones** — la exigencia es clara pero el molde se desvía (falta ejemplo, excede tamaño, solapa parcialmente otra) | 69 | 41 % |
| ❌ **Incumple** — rompe una meta-regla de forma que afecta cómo se lee o se aplica la regla | 53 | 31 % |

**Los cinco hallazgos que mandan** (detalle en §4):

1. **El capítulo 20 documenta una corrección que nunca se aplicó.** `estructura-regla.md` diseca `F0`, concluye que dentro hay una sola regla, y publica la versión corregida completa. `F0` en [`base/02-flujo-de-trabajo/reglas/F0…`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) sigue con sus 36 líneas originales. Hoy conviven **dos textos de `F0`** y ninguno declara cuál manda → rompe `M2` (fuente única) en el peor sitio posible.
2. **Existe una cuarta forma de dependencia que `M7` no declara.** El bloque `**Encadenamiento:**` aparece **22 veces** en 5 capítulos y es hoy la forma dominante de relacionar reglas. `M7` solo admite `extiende` / `depende de` / `deroga`, entre paréntesis, en el cuerpo. O `M7` la absorbe o 22 reglas migran.
3. **Cuatro reglas están escondidas.** `CQ1`–`CQ4` usan `###` en vez de `##`. `estructura-regla.md` nombra exactamente este error: *"con tres, la regla se esconde: no sale en la lista y el programa que las revisa no la ve"*.
4. **`M8` se contradice con `N1`.** `M8` dice que las `[BLINDADA]` no admiten excepciones; `N1` es `[BLINDADA]` y tiene una excepción escrita. Por `M6` paso 6, un choque irresoluble es **defecto del estándar** y se reporta, no se elige en silencio.
5. **`M9` está incumplida para 27 reglas.** Los capítulos **18**, **19** y **20** no aparecen en [`validadores/reglas-validables.md`](../validadores/reglas-validables.md) — ni como validables ni como no validables. `M9` exige que **toda** regla declare si lo es.

**Deuda estructural de fondo:** seis pares de reglas dicen lo mismo en dos capítulos (`F5`≡`T5`, `F6`≡`DOC1`, `F7`≡`DOC3`, `S7`≡`DEP3`, `DP8`≡`OB6`, `DOC3`⊂`DOC11`). `M12` avisa por qué importa: *"un día alguien arregla una copia y se olvida de la otra"*. `M11` da el mecanismo para consolidarlas sin romper citas: derogar, no borrar.

---

## 2 · Método

### 2.1 · Qué se leyó

Los 23 archivos de norma: `base/00-identidad-y-rol.md`, `base/00-nucleo-blindado.md`, `base/01`–`base/19`, `base/20-meta-reglas/{base.md, estructura-regla.md}`, y las fuentes únicas `base/02-flujo-de-trabajo/reglas/F12-…`, `base/02-flujo-de-trabajo/reglas/F13-…` y `base/02-flujo-de-trabajo/estructura-base.md`. Contraste contra `validadores/reglas-validables.md`, `CHANGELOG.md` y `VERSION`.

### 2.2 · Los criterios, derivados de cada meta-regla

Cada regla se evaluó contra estos 13 criterios verificables. Los marcados 🤖 se comprobaron mecánicamente (grep / conteo), el resto por lectura.

| Meta-regla | Criterio aplicado a cada regla |
|---|---|
| `M1` | ¿Su capa es la correcta y no contradice a la de arriba? ¿Marca `[BLINDADA]` solo si es capa 1? |
| `M2` | ¿El capítulo es el dueño del tema, o el tema ya tiene dueño en otro capítulo? ¿El capítulo pasa de ~15 reglas? ¿Si la regla pasa de una página, tiene subcarpeta? 🤖 |
| `M3` | ¿Nombra lenguaje, framework, motor, nube, sector, cliente, herramienta o ruta concreta? 🤖 |
| `M4` | ¿El ID es `<PREFIJO><n>`, con prefijo exclusivo del capítulo y consecutivo simple? 🤖 |
| `M5` | ¿`##` + ID + título imperativo autosuficiente? ¿Cuerpo de 1–4 líneas? ¿**Una** sola exigencia? ¿Ejemplo INCORRECTO/CORRECTO donde hace falta? ¿Marca de la lista cerrada de tres? ¿Sin texto copiado de otra regla? 🤖 |
| `M6` | ¿Choca con otra regla sin que el choque esté resuelto en el texto? |
| `M7` | ¿Sus dependencias usan `extiende` / `depende de` / `deroga`, entre paréntesis, en el cuerpo? ¿Sin ciclos? ¿Sin apuntar hacia arriba? 🤖 |
| `M8` | Si tiene excepción: ¿declara **condición**, **límite** y **quién autoriza**? ¿Es `[BLINDADA]` con excepción (prohibido)? |
| `M9` | ¿Está clasificada en `validadores/reglas-validables.md`? 🤖 |
| `M10` | ¿El capítulo/regla tiene entrada en `CHANGELOG.md` y `VERSION` acompañó? 🤖 |
| `M11` | ¿Hay reglas que debieron derogarse y siguen vigentes en paralelo? |
| `M12` | ¿Duplica el criterio de otra regla escrito con otras palabras? |
| `M13` | ¿Es realmente regla universal, o es capa 3 / nota / pendiente / instructivo del repo? |

### 2.3 · Escala de estado y de prioridad

- ✅ **Cumple** · 🟡 **Cumple con observaciones** · ❌ **Incumple**
- **Alta** — la desviación cambia qué se entiende que hay que hacer, esconde la regla, o hace que dos reglas se contradigan. Se corrige antes de la próxima fase que las use.
- **Media** — la regla se entiende, pero el molde roto encarece mantenerla (duplicación, tamaño, ID fuera de patrón).
- **Baja** — cosmético o de redacción. Se arregla al pasar por ahí.

---

## 3 · Comprobaciones mecánicas (evidencia)

| Comprobación | Resultado |
|---|---|
| Reglas totales en `base/` (encabezados `##` con ID) | **170** (+ 13 subpartes `F12.1`–`F12.13` = 183 identificadores) |
| Reglas escondidas con `###` | **4** — `CQ1`, `CQ2`, `CQ3`, `CQ4` |
| Bloques `**Encadenamiento:**` (forma de dependencia no declarada en `M7`) | **22** — `01`(4) `02`(9) `03`(2) `04`(1) `13`(6) |
| Variantes de formato de cita entre capítulos (`M4` fija `NN·ID`) | **≥10** — `` `00` · N4 ``, `` `02·F4` ``, `` `00` N4 ``, `` `13` DOC10 ``, `` `05`·E3 ``, … |
| IDs con numeración decimal (fuera de `M4`) | **18** — `F4.1`–`F4.5` y `F12.1`–`F12.13` |
| Capítulos que exceden el tamaño sugerido por `M2` (~15 reglas) | **3** — `01`(18) · `13`(16) · `02`(19 + 13 subpartes) |
| Reglas de más de una página sin subcarpeta (`M2` la exige) | `F4.3` (78 líneas) · `DOC14` (58) · `D7` (41) · `DOC12` (41) · `DOC13` (38) |
| Capítulos sin ningún ejemplo INCORRECTO/CORRECTO | **2** — `18` (8 reglas) · `19` (6 reglas) |
| Capítulos ausentes de `validadores/reglas-validables.md` | **3** — `18`, `19`, `20` (27 reglas) |
| Reglas marcadas `[DEROGADA]` | **0** (pese a 6 pares duplicados que lo requieren) |
| Número de capítulo usado dos veces | `00` — `00-identidad-y-rol.md` y `00-nucleo-blindado.md` |

---

## 4 · Hallazgos transversales

Cada hallazgo aplica a varias reglas a la vez. El inventario regla por regla (§5) los referencia por su código `H-nn`.

---

### H-01 · La corrección de `F0` está publicada pero no aplicada · **Alta**

**Meta-reglas:** `M2` (fuente única) · `M5` (formato) · `M8` (excepción completa) · `M10` (versionar el cambio)

**Qué se encontró.** [`estructura-regla.md:109-170`](../base/20-meta-reglas/estructura-regla.md#L109) toma `F0` como caso de estudio, la descompone en 7 trozos, concluye que **solo dos son regla** y publica la versión corregida completa: título imperativo (*"Recorre la cadena completa, sin saltar eslabones"*), cuerpo de doce líneas, excepción con sus tres partes, y el destino de cada trozo sobrante. El texto cierra: *"El número sigue siendo `F0`. Eso no se toca nunca."*

`F0` en [`base/02-flujo-de-trabajo/reglas/F0…`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) no cambió: 36 líneas, título nominal (*"La secuencia completa — de la necesidad al cierre"*), la tabla-mapa de 7 pasos dentro de la regla, las definiciones de épica/módulo/fase que pertenecen a otros capítulos, la repetición del trozo 5 (*"Sin atajos por tamaño"*, que ya dice el trozo 2), y la excepción sin `autoriza`.

**Incumplimientos.** Dos textos de `F0` conviven sin declarar cuál rige (`M2`). El vigente tiene título no imperativo, cuerpo de 36 líneas y ≥2 exigencias (`M5`), excepción incompleta (`M8`), y explica temas de otros capítulos (`M2`).

**Por qué es Alta.** No es una regla más: es la regla que abre el flujo de trabajo, y el defecto está documentado en el propio estándar con la solución escrita al lado. Un lector que llegue por `estructura-regla.md` y otro que llegue por `02-flujo-de-trabajo.md` leen dos reglas distintas.

**Recomendación.** Aplicar literalmente el texto corregido de `estructura-regla.md:143-162`. Mover el trozo 1 (tabla de 7 pasos) y el 7 (encadenamiento) al encabezado del capítulo 02. Reemplazar los trozos 3 y 4 por enlaces a `13·DOC15`, `13·DOC16` y `F12`. Borrar el trozo 5. Versionar como **PARCHE** (no cambia qué se exige, solo dónde está escrito).

---

### H-02 · `M7` no declara la forma de dependencia que el estándar realmente usa · **Alta**

**Meta-reglas:** `M7` (solo tres dependencias) · `M5` (formato del cuerpo) · `M6` (choque sin resolver)

**Qué se encontró.** `M7` admite exactamente tres dependencias — `extiende ID`, `depende de ID`, `deroga ID` — y fija dónde van: *"Se escriben en el cuerpo de la regla, entre paréntesis."* En la práctica, **22 reglas** cierran con un bloque `**Encadenamiento:**` en prosa, después del ejemplo, que mezcla las tres formas con relaciones que no son ninguna de las tres (*"balancea"*, *"refuerza"*, *"es la aplicación puntual de"*, *"es la primera defensa contra"*, *"mismo espíritu"*).

Reglas afectadas: `C15`, `C16`, `C17`, `C18`, `F0`, `F4.4`, `F4.5`, `F8`, `F9`, `F10`, `F11`, `D7`, `D8`, `S11`, `DOC11`, `DOC12`, `DOC13`, `DOC14`, `DOC15`, `DOC16` (y dos más en `02`).

**Incumplimientos.** Forma de dependencia no declarada (`M7`), ubicada fuera del cuerpo (`M5`), con verbos de relación abiertos que ningún validador puede interpretar (`M9`).

**Por qué importa.** `M7` prohíbe ciclos y dependencias hacia arriba. Esas dos prohibiciones solo son comprobables si las dependencias están en las tres formas cerradas. Con `Encadenamiento` en prosa, nadie puede afirmar que no hay ciclos — y de hecho `F4.4`→`F4.5`→`F4.4` es un ciclo declarado en prosa (`F4.4` dice *"F4.5 — lo que convendría agregar sigue la ruta de propuesta"*; `F4.5` dice *"F4.4 — proveedor del plan deriva de CA"*).

**Recomendación.** Elegir una de dos, no ambas:

- **(a) Absorber** — `M7` reconoce un cuarto tipo, `**Encadenamiento:**`, define su semántica (*"relación de contexto, sin obligación de cumplimiento"*), fija su posición (después del ejemplo) y aclara que **no** sustituye a las tres formas normativas: si hay dependencia real, va en el cuerpo entre paréntesis. Versión **MENOR**.
- **(b) Migrar** — las 22 reglas convierten su `Encadenamiento` en `(extiende …)` / `(depende de …)` dentro del cuerpo, y lo que no encaje en ninguna se borra o se manda a `notas/` (`M13`). Versión **PARCHE**, pero toca 22 reglas.

Recomendado: **(a)**. El bloque `Encadenamiento` aporta valor real de navegación y lo barato es legalizarlo, no borrarlo.

---

### H-03 · Cuatro reglas escondidas con `###` · **Alta**

**Meta-reglas:** `M5` (encabezado `##`) · `M9` (validable)

**Qué se encontró.** `CQ1`, `CQ2`, `CQ3` y `CQ4` en [`base/16-cumplimiento-y-calidad.md:11,20,29,33`](../base/16-cumplimiento-y-calidad.md#L11) usan `###`. Los `##` del capítulo los ocupan dos encabezados de sección: `## Parte A — Universal (capa 2)` y `## Parte B — Gancho a capa 3`.

`estructura-regla.md:56` nombra exactamente este fallo: *"`### R7 · Mide antes…` — con tres, la regla se esconde: no sale en la lista y el programa que las revisa no la ve."*

**Incumplimientos.** Nivel de encabezado fuera del molde (`M5`). Consecuencia comprobada: un conteo de reglas por `^## ` devuelve **2** para el capítulo 16 en vez de **4**.

**Recomendación.** Subir `CQ1`–`CQ4` a `##`. La partición Parte A / Parte B se resuelve con texto de encabezado del capítulo, no con encabezados `##` que compiten con las reglas. Versión **PARCHE**.

---

### H-04 · `M8` se contradice con `N1` · **Alta**

**Meta-reglas:** `M8` (excepción dentro de la regla) · `M1` (el núcleo no se ajusta) · `M6` (desempate)

**Qué se encontró.** `M8` afirma: *"Las `[BLINDADA]` **no admiten excepciones**. Eso es lo que significa blindada."* `N1 · No ejecutar sin validación `[BLINDADA]`` cierra con: *"Excepción: un plan ya aprobado se ejecuta continuo (no re-pedir permiso por cada paso)."*

El choque no se resuelve por `M6`: el paso 1 (*"¿una es `[BLINDADA]`?"*) daría la razón a `N1`, pero `M8` **es sobre** `N1`, no compite con ella. Por `M6` paso 6, esto es un **defecto del estándar**.

**Análisis del fondo.** La contradicción es de vocabulario, no de criterio. `M8` usa "excepción" para dos cosas distintas:

- **Excepción propiamente dicha** — un caso donde la regla **no se cumple**. Eso es lo que las blindadas no admiten.
- **Condición de autorización** — la regla se cumple; lo que varía es **quién** y **cuándo** da el permiso. `N1` (plan aprobado), `N2` (autorización de un solo uso), `N4` (*"sin autorización expresa y específica"*) y `N5` (*"confirmación explícita"*) son todas de este segundo tipo. Las cuatro blindadas están escritas alrededor de una puerta autorizada.

**Recomendación.** Ampliar `M8` con el párrafo que distingue las dos figuras, y renombrar en `N1` la palabra "Excepción" por "**Alcance de la autorización:**". Ninguna exigencia cambia. Versión **PARCHE** en `M8` y `N1`.

```
INCORRECTO: N1 [BLINDADA] · "Excepción: un plan ya aprobado se ejecuta continuo"
CORRECTO:   N1 [BLINDADA] · "Alcance de la autorización: aprobar un plan autoriza
            todos sus pasos; no hace falta re-pedir permiso por cada uno (ver 02·F3)."
```

---

### H-05 · `M9` incumplida para 27 reglas · **Alta**

**Meta-reglas:** `M9` (toda regla declara si es validable) · `M10` (revisar `reglas-validables.md` al cambiar reglas)

**Qué se encontró.** `validadores/reglas-validables.md` está fechado **2026-08-05** y clasifica los capítulos `00`–`17`. Los capítulos **18** (`DP1`–`DP8`), **19** (`OB1`–`OB6`) y **20** (`M1`–`M13`) no aparecen en ninguna de las tres listas (✅ validadas · 🟡 pendientes · 🔴 no validables). Son **27 reglas sin clasificar**.

Los tres capítulos entraron en la versión **1.3.0** (`CHANGELOG.md:34,42,43`), posterior a la foto. `M10` punto 3 obliga a revisar `reglas-validables.md` en el mismo movimiento; no se hizo.

**Observación adicional sobre el mecanismo.** `M9` se titula *"Toda regla **declara** si es validable"*, pero ninguna regla lo declara **en su propio texto** — la declaración vive centralizada en `reglas-validables.md`. El cuerpo de `M9` sí admite ese mecanismo (*"se registra en `validadores/reglas-validables.md`"*), así que el título promete más de lo que el cuerpo exige. Redacción confusa, no incumplimiento.

**Recomendación.** Clasificar las 27 reglas. Evaluación preliminar de este análisis:

| Regla | Clasificación propuesta | Con qué se comprobaría |
|---|---|---|
| `18·DP1` | 🟡 validable | existe pipeline/manifiesto versionado en el repo |
| `18·DP2` | 🟡 validable | existen archivos de IaC declarados |
| `18·DP3` | 🔴 criterio humano | "un solo build promovido" no se lee del repo |
| `18·DP4` | 🟡 validable | el artefacto no contiene variables de entorno horneadas |
| `18·DP5` | 🔴 criterio humano | el plan de vuelta es narrativa |
| `18·DP6` | ✅ validable ya | completitud contra `plantillas/checklist-despliegue.md` (`plantillas.py`) |
| `18·DP7` | 🟡 validable | existe endpoint de health/readiness declarado |
| `18·DP8` | 🔴 criterio humano | conducta del agente |
| `19·OB1` | 🟡 validable | los logs se emiten estructurados (patrón por stack) |
| `19·OB2`–`OB3` | 🔴 criterio humano | qué se mide y qué alerta es juicio |
| `19·OB4` | 🟡 validable | existen runbooks versionados para las operaciones nombradas |
| `19·OB5` | ✅ validable ya | completitud contra `plantillas/postmortem.md` |
| `19·OB6` | 🔴 criterio humano | conducta del agente |
| `20·M1`, `M2`, `M6`, `M8`, `M11`–`M13` | 🔴 criterio humano | routing y desempate son juicio |
| `20·M3` | 🟡 validable | listado negro de tecnologías nombradas en `base/` |
| `20·M4` | 🟡 validable | ID único, prefijo exclusivo del capítulo, sin huecos |
| `20·M5` | 🟡 validable | encabezado `##`, marca de la lista cerrada, presencia de ejemplo, tamaño del cuerpo |
| `20·M7` | 🟡 validable | dependencias citadas apuntan a IDs existentes, sin ciclos |
| `20·M9` | 🟡 validable | toda regla de `base/` aparece en `reglas-validables.md` |
| `20·M10` | ✅ validable ya | `version.py` (CHANGELOG + VERSION suben juntos) |

Las siete `M` marcadas 🟡 son las más rentables del conjunto: **se validan en seco sobre el propio estándar**, sin necesitar un proyecto real. Un validador `metareglas.py` cerraría de una vez H-03, H-06, H-07, H-09 y H-11.

---

### H-06 · Seis pares de reglas dicen lo mismo en dos capítulos · **Alta**

**Meta-reglas:** `M2` (un tema, un dueño) · `M5` (sin texto prestado) · `M12` (buscar antes de crear) · `M11` (derogar, no borrar)

| Par | Qué duplican | Dueño que debe quedar | Evidencia |
|---|---|---|---|
| `02·F5` ≡ `08·T5` | correr las pruebas y reportar el conteo | **`08·T5`** (el capítulo de pruebas) | Ejemplo **idéntico palabra por palabra** en ambas: *"implementar + escribir pruebas + 'listo'"* / *"Verdes 4/4"* |
| `02·F6` ≡ `13·DOC1` | persistir el trabajo al cerrar | **`13·DOC1`** | Misma exigencia, misma justificación (*"el chat se pierde; los archivos quedan"*) |
| `02·F7` ≡ `13·DOC3` | trazabilidad spec→implementación antes de cerrar | **`13·DOC3`** | Ejemplo idéntico: *"pruebas verdes → cierro"* / *"pruebas verdes + trazabilidad sin faltantes → cierro"* |
| `04·S7` ≡ `10·DEP3` | auditar vulnerabilidades de dependencias | **`10·DEP3`** | Cada una remite a la otra: `S7` dice *"detalle en `10`"*, `DEP3` dice *"(`04`·S7)"* — círculo sin dueño |
| `18·DP8` ≡ `19·OB6` | operar producción es del humano, no del agente | **`18·DP8`** | Ambas cierran con *"la identidad es desarrollador senior, no SRE"* |
| `13·DOC3` ⊂ `13·DOC11` | la tabla de trazabilidad de 5 columnas | **`13·DOC11`** (fija el formato) | `DOC11` se declara *"extiende DOC3"* y luego **repite entera** la tabla que `DOC3` ya trae |

**Incumplimientos.** `M2`: dos capítulos dueños del mismo tema. `M5`: texto copiado en vez de enlazado. `M12`: la duplicación es *"el defecto más caro"*.

**Recomendación.** Consolidar por `M11` — **derogar, no borrar**, porque las specs y fases cerradas citan por ID:

```
## F5 · Ejecuta las pruebas antes de dar por terminado   ·  `[DEROGADA en 1.4.0 → ver 08·T5]`
```

y bajo la marca, el texto original intacto. Para `DOC3`/`DOC11`, `DOC3` conserva el principio (una línea + enlace) y `DOC11` conserva la tabla — ninguna se deroga, se reparten. Versión **MAYOR** en el par `F5`/`F6`/`F7` (un proyecto al día que citaba `F5` tiene que empezar a citar `T5`).

---

### H-07 · `base/` nombra tecnologías, herramientas y rutas de un proyecto concreto · **Alta**

**Meta-reglas:** `M3` (la base es agnóstica) · `M13` (lo concreto es capa 3)

`M3` es tajante: *"Si una regla no se puede escribir sin nombrar una tecnología, **no es regla de la base**: es capa 3."*

| Regla | Qué nombra | Gravedad |
|---|---|---|
| `13·DOC14` | `GitHub` · `GitLab` · `VSCode` · `Ctrl+Click` · `404` · "route" · "framework corriendo" · y **rutas reales de un proyecto**: `documentacion/prompts/erp/analisis/multitenancy.md`, `documentacion/organizacion-jerarquica/fase-hg-slug/plan_trabajo.md` | **Alta** — los ejemplos son de un cliente, no inventados |
| `04·S11` | `destroy()` · `SoftDeletes` · `deleted_at` · `activo=false` · "trait de soft-delete" | **Alta** — API de un framework concreto |
| `03·D8` | `Aporte::where('usercreate_id', Auth::id())` · `proyecto_id` | **Alta** — código de un stack + entidad de un dominio concreto |
| `13·DOC5` | `SQLite+FTS5` · skill `usar-memoria` · carpeta `memoria/` | **Media** — motor concreto donde bastaba "base local buscable" |
| `01·C10` | `SQLite in-memory` · `MariaDB` · `React + Django` · *"el rol id=2 es X en este ERP"* | **Media** — se usan como ejemplo de lo que **no** va en base, pero quedan escritos en base |
| `01·C15` | *"módulo Aportes"* | **Media** — nombre propio de un proyecto |
| `01·C16` | `git status --short` · `git diff` · herramientas `Read`/`Edit` · aviso `ide_opened_file` | **Media** — herramientas del agente, no del proyecto; frontera discutible |
| `16·CQ3`, `16·CQ4` | `OWASP` (ASVS + Top 10) · `ISO/IEC 25010` | **Alta por contradicción** — ver H-08 |
| `04·S10` | `killall` · `pkill -f` · `taskkill /IM` | **Baja** — son los tres SO principales; nombrarlos es lo que hace la regla accionable |

**Recomendación.** Reescribir el cuerpo en concepto y mover lo concreto al ejemplo o a la capa 3:

```
INCORRECTO (S11): "`destroy()`, `SoftDeletes`, `archivar`, `desactivar` y equivalentes
                   que marcan un campo (`deleted_at`, `activo=false`) son escrituras"
CORRECTO (S11):   "Toda operación que modifica una fila del almacén productivo cuenta
                   como escritura, aunque el nombre del método sugiera 'eliminar' y
                   el borrado sea lógico. El proyecto declara qué mecanismos de borrado
                   lógico usa (`.agente/stack.md`)."
```

`DOC14` requiere trato aparte: sus ejemplos deben pasar a rutas ficticias (`documentacion/<área>/<unidad>/plan_trabajo.md`) y su segunda mitad —el pseudocódigo del route que atrapa `.md`— es **requisito de infraestructura del proyecto**, no regla de redacción de enlaces. Se parte (ver H-09).

---

### H-08 · El capítulo 16 se contradice consigo mismo · **Alta**

**Meta-reglas:** `M6` (choque sin resolver = defecto) · `M2` (opt-in se marca en el título) · `M3`

**Tres contradicciones internas en 60 líneas:**

1. **Opt-in vs. universal.** El título dice `[CAPA 2 · opt-in]` y la línea 3 confirma *"Opt-in: la capa 3 activa esta sección"*. La línea 5 dice lo contrario: *"lo **universal** (capa 2, **siempre aplica**)"*. Una regla no puede ser a la vez opcional y de aplicación permanente. `M2` marca el opt-in a nivel de **capítulo**, no de mitad de capítulo — la partición Parte A/Parte B no cabe en el mecanismo.
2. **Parte B vs. `CQ3`/`CQ4`.** Parte B declara: *"el agente **no hardcodea** el marco en el código ni asume uno por defecto. Lee el declarado en capa 3."* `CQ3` hardcodea **OWASP** y `CQ4` hardcodea **ISO/IEC 25010** como línea base obligatoria. La regla del capítulo prohíbe lo que dos de sus cuatro reglas hacen.
3. **`CQ1` vs. `M2`.** `CQ1` exige identificar sector y jurisdicción *"al iniciar un proyecto"* — pero el capítulo es opt-in, así que en un proyecto que no lo active `CQ1` nunca corre, y aun así el resto del estándar (`12·PR5`, `04·S6`) asume que el marco normativo se conoce.

**Recomendación.** Partir el capítulo:

- `16` queda **capa 2, no opt-in**, con `CQ1` (identificar el marco) y `CQ2` (cumplir por construcción + trazabilidad). Ambas son universales de verdad: todo proyecto tiene *algún* marco, aunque sea "ninguno declarado".
- `CQ3` (OWASP) y `CQ4` (ISO 25010) pasan a `*opt-in*` **a nivel de regla** (marca que `M5` sí admite) o —mejor— se reescriben como concepto (*"toma como línea base un catálogo reconocido de controles de código seguro; cuál, lo declara la capa 3"*) con OWASP e ISO 25010 nombrados en `plantillas/marco-normativo.md`, que es donde `M13` los manda.
- Parte A / Parte B dejan de ser encabezados `##` (H-03).

Versión **MENOR**.

---

### H-09 · 34 reglas rompen "una sola exigencia" · **Alta / Media**

**Meta-reglas:** `M5` (*"Si el cuerpo tiene un 'y además', son dos reglas"*) · `M4` (la partida conserva el ID original)

`estructura-regla.md:96-105` da seis pistas para detectarlo. Aplicadas al catálogo:

**Grupo A — el título lleva "y"** (pista más directa):

| Regla | Exigencias dentro | Partición propuesta |
|---|---|---|
| `03·D1 · Toda tabla nueva se normaliza **y** lleva auditoría` | normalización · auditoría · integridad en BD (FK/UNIQUE/índices) | `D1` normaliza · `D9` auditoría · `D10` integridad |
| `02·F4 · Todo plan lleva su plan de pruebas **y** su aprobación explícita` | plan de pruebas · aprobación explícita · verificar la cadena que respalda el plan | `F4` aprobación · `F14` plan de pruebas · `F15` cadena previa |
| `07·Q4 · No repitas (DRY), **pero** no abstraigas de más` | extraer duplicado · no abstraer prematuro | Una sola con la tensión explícita (excepción de `Q4`), o `Q4`/`Q8` |
| `04·S5 · CSRF, sesiones **y** transporte` | CSRF · cookies de sesión · HTTPS · hashing de contraseñas | `S5` CSRF · `S12` sesiones · `S13` transporte · `S14` credenciales |
| `03·D6 · Concurrencia **e** idempotencia` | idempotencia · lost update · duplicados por carrera | `D6` idempotencia · `D11` concurrencia · `D12` unicidad en BD |

**Grupo B — la regla se autodeclara múltiple:**

| Regla | Autodeclaración textual |
|---|---|
| `02·F4.5` | *"**Dos partes indivisibles.** (1) Ejecución literal de los CA. (2) Descubrimientos fuera de CA → proponer"* |
| `04·S11` | *"**Regla 1** — Autorización por operación. **Regla 2** — El borrado lógico cuenta como escritura"* |
| `08·T7` | *"se aplica en **dos frentes**: de dónde salen los casos y de dónde sale el resultado esperado"* |
| `09·G8` | *"**Dos consecuencias:** el cuerpo arranca con la idea del usuario. Nunca se firman los commits con la herramienta"* |

Las cuatro pasan la prueba de `estructura-regla.md`: *"¿se pueden cumplir por separado? Sí → son dos."* Se puede ejecutar literal los CA (F4.5-1) y aun así actuar sobre un descubrimiento (F4.5-2). Se puede escribir el cuerpo del commit con la idea del usuario (G8-1) y firmarlo con la herramienta (G8-2).

**Grupo C — restantes detectadas:** `00·N1`, `00·N4`, `00·N6`, `01·C10`, `01·C14`, `01·C17`, `02·F2`, `02·F4.1`, `02·F4.3`, `02·F11`, `04·S3`, `04·S6`, `05·E2`, `08·T3`, `09·G6`, `13·DOC14`, `13·DOC15`, `14·EST2`, `15·IM2`, `15·IM5`, `17·I3`, `18·DP8`, `20·M2`, `20·M5`.

**Caso destacado — `13·DOC15`:** la regla es *"Historias de Usuario desde plantilla central"* y a mitad de cuerpo introduce, con negrita propia, *"**Índice `README.md` en cada nivel del árbol**"* — una exigencia de otra naturaleza (mantener índices navegables), fulfillable por separado, que además `DOC16` referencia como si ya fuera regla propia (*"Índice vivo: el árbol sigue el mismo README.md por nivel de DOC15"*). Debe ser `DOC17`.

**Caso destacado — `02·F4.3`:** 78 líneas con **cuatro** exigencias independientes: (1) el plan se construye sobre línea base verificada, (2) los 5 componentes QUÉ/CÓMO/DÓNDE/POR QUÉ/IMPACTO, (3) la matriz de dependencias del refactor con su regla derivada de coherencia de tests, (4) la proporcionalidad del análisis y el filtro de decisiones antes de escalar. Por `M2` debió abrirse subcarpeta `base/02-flujo-de-trabajo/F4.3/` hace tiempo.

**Recomendación.** Partir por olas, empezando por el Grupo B (las que ya se autodeclaran múltiples: el trabajo de análisis está hecho). En cada partición, **la original conserva su ID** (`M4`) y la nueva toma el siguiente consecutivo libre del capítulo. Versión **MENOR** por ola (aditiva: no cambia qué se exige, reparte dónde está escrito).

---

### H-10 · `13·DOC10` cita una regla de capa 3 desde capa 2 · **Alta**

**Meta-reglas:** `M1` (un nivel nunca contradice al de arriba) · `M7` (*"Nunca hacia arriba"*) · `M3` · `M12`

**Qué se encontró.** `DOC10` dice: *"**Cuando una regla P se promueve a la base común** (por **P28**): dejar banner 'promovida a base'…"*. `P28` es una regla del catálogo de **un proyecto** (capa 3). Una regla de `base/` (capa 2) depende de un identificador que solo existe en un proyecto concreto.

**Segundo defecto en la misma regla.** `DOC10` cierra con una enumeración congelada: *"Para el conjunto de reglas **C1-C10 · DOC1-DOC10 · F1-F5** (y demás secciones de la base)"*. Hoy son `C1`–`C18`, `DOC1`–`DOC16`, `F0`–`F13`. La enumeración quedó vieja y sugiere que las reglas fuera del rango no son citables — lo contrario de lo que `M4` garantiza.

**Recomendación.** Reescribir el punto de promoción en concepto (*"cuando una regla del catálogo del proyecto se promueve a la base común"*), sin ID de capa 3. Sustituir la enumeración congelada por *"toda regla de `base/` tiene ID estable y es citable desde el catálogo del proyecto (`M4`)"*. Versión **PARCHE**.

---

### H-11 · `F12` y `F13` viven fuera del molde · **Alta**

**Meta-reglas:** `M4` (ID) · `M5` (encabezado, marcas, molde) · `M2` (un tema, un dueño)

**`F12` — 13 subpartes bajo un ID, sin encabezados.** [`reglas/F12-relacion-y-nomenclatura-de-fases.md`](../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) no tiene **ningún** encabezado `##`: las 13 partes son viñetas `* **F12.1** — …`. El archivo declara la razón: *"Texto literal del usuario, 2026-08-03. No se reescribe, no se resume y no se interpreta."*

Esa congelación es **decisión del usuario y se respeta** — pero hoy es una excepción **no escrita** al molde, y `M8` es explícita: *"Si aparece un caso que pide una excepción **no escrita**: PAUSAR y preguntar."*

Además, bajo el mismo ID conviven tres temas distintos que `M2` separaría: relación fase↔HU (`F12.1`–`F12.4`, `F12.11`), nomenclatura (`F12.5`–`F12.7`, `F12.12`), y **ruta física en disco** (`F12.13`, que además es la fuente única que `DOC15`, `DOC16` y `F13` referencian).

**`F13` — marca inventada.** El encabezado es:

```
## F13 · Estructura base obligatoria del proyecto   ·   `[GATE DE ARRANQUE · PRECONDICIÓN]`
```

`M5` cierra la lista de marcas en tres: `[BLINDADA]`, `*opt-in*`, `[DEROGADA …]`. Y `estructura-regla.md:60` usa **este caso exacto** como su ejemplo de qué no hacer: *"Inventarse una etiqueta: `## F13 · … · [GATE DE ARRANQUE]`. Si de verdad hace falta una nueva, primero se agrega a la lista de `M5`."*

El anti-ejemplo del manual es la regla real del catálogo, sin corregir.

**Recomendación.**

- **`F12`:** preguntar al usuario cuál de las dos vías prefiere — (a) `M5` incorpora una marca/figura de *"texto congelado del usuario"* con su condición, límite y quién autoriza (`M8`), o (b) las 13 partes se envuelven en el molde (`## F12.1 · …`) **sin tocar una palabra del texto**, que es lo que la congelación protege. Es decisión del usuario, no del agente.
- **`F13`:** quitar la marca. El hecho de que corra primero ya está dicho en el cuerpo y en `CLAUDE.md §3`; no necesita etiqueta en el encabezado. Añadir en el archivo fuente única el encabezado de regla que hoy falta. Versión **PARCHE**.
- **`F12.13`:** promoverla a regla propia del capítulo 02 con su ID libre (p. ej. `F14`), porque es la fuente única de la ruta física y la citan cuatro reglas de otros capítulos. Que la ruta canónica dependa de una subparte de una regla congelada es frágil.

---

### H-12 · Excepciones incompletas: 13 de 15 no dicen quién autoriza · **Media**

**Meta-regla:** `M8` (condición + límite + **autoriza**)

`estructura-regla.md:202` explica por qué la tercera es la que importa: *"Si nadie tiene que dar permiso, la excepción se vuelve costumbre y al final la regla no se cumple nunca."*

| Regla | Excepción escrita | condición | límite | autoriza |
|---|---|---|---|---|
| `04·S9` | ampliar rutas autorizadas | ✅ | ✅ | ✅ **usuario en el chat** |
| `04·S10` | matar por patrón en caso extremo | ✅ | ✅ | ✅ **usuario, con PID y motivo** |
| `02·F0` | lo que no es desarrollo queda fuera de la cadena | ✅ | 🟡 | ❌ |
| `02·F2` | correcciones triviales, bugfix, config local, lectura | ✅ | ❌ | ❌ |
| `02·F4.2` | trabajos triviales con flujo abreviado | ✅ | 🟡 | 🟡 *"si el proyecto lo permite"* |
| `02·F11` | infraestructura compartida | ✅ | ✅ | 🟡 (solo en la vía B) |
| `03·D1` | *"salvo pivots puras"* | ✅ | ❌ | ❌ |
| `03·D4` | constantes técnicas, fórmulas, códigos por ley | ✅ | 🟡 | ❌ |
| `03·D5` | *"No aplica en diseño desde cero"* | ✅ | ❌ | ❌ |
| `03·D7` | cuándo NO aplica SCD-2 (4 casos) | ✅ | ❌ | ❌ |
| `03·D8` | entidades genuinamente personales | ✅ | ❌ | ❌ |
| `01·C1` | *"(No aplica dentro de un plan ya aprobado)"* | ✅ | ❌ | ❌ |
| `01·C17` | lista "NO aplica a" (3 casos) | ✅ | ❌ | ❌ |
| `08·T1` | *"si no amerita (visual/trivial), decláralo"* | ✅ | ❌ | ⚠️ el propio agente |
| `00·N1` | plan aprobado | — | — | — **y es `[BLINDADA]`** (H-04) |

**Recomendación.** `S9` y `S10` son el modelo a copiar. Para el resto, añadir la línea de autorización. En varios casos el autorizador natural es **el usuario por `01·C7`** (ante dos lecturas, pregunta) y basta citarlo. El caso `T1` merece atención: hoy el agente se autoriza a sí mismo a no probar, lo que `M8` describe como la excepción que se vuelve costumbre. Versión **PARCHE** (no cambia qué se exige, cierra quién puede saltárselo).

---

### H-13 · Títulos que cuentan en vez de mandar · **Media**

**Meta-regla:** `M5` (*"título imperativo, entendible sin leer el cuerpo"*)

| Regla | Título actual | Propuesta |
|---|---|---|
| `02·F0` | La secuencia completa — de la necesidad al cierre | Recorre la cadena completa, sin saltar eslabones *(ya escrita en `estructura-regla.md`)* |
| `03·D6` | Concurrencia e idempotencia | Protege el dato que dos operaciones pueden tocar a la vez |
| `04·S4` | Gestión de secretos | Mantén los secretos fuera del código y rótalos si se exponen |
| `04·S5` | CSRF, sesiones y transporte | *(se parte — H-09)* |
| `09·G3` | Qué nunca se versiona | Excluye del control de versiones secretos, datos y artefactos |
| `12·PR5` | Retención y borrado | Define cuánto se conservan los datos y bórralos o anonimízalos al vencer |
| `16·CQ4` | Atributos de calidad como checklist (ISO/IEC 25010) | Evalúa el cambio contra los atributos de calidad y nombra los trade-offs |
| `02·F12` | Relación y nomenclatura de fases | *(depende de H-11)* |
| `02·F13` | Estructura base obligatoria del proyecto | Valida la estructura base antes de cualquier otro paso |
| `13·DOC5` | Registrar señales (memoria) | Registra como señal lo que no se puede recuperar del código |

Los títulos de `M1`–`M13` son descriptivos a propósito y **no** son hallazgo: `M1` clasifica el preámbulo como *"No: describe, no exige"*.

---

### H-14 · Reglas sin ejemplo donde `M5` lo exige · **Media**

**Meta-regla:** `M5` (*"El ejemplo es obligatorio cuando la regla se puede malinterpretar o cuando el error es frecuente"*)

**Capítulos enteros sin un solo ejemplo:** `18` (`DP1`–`DP8`) y `19` (`OB1`–`OB6`). Son 14 reglas seguidas, todas de dominios donde el error es frecuente y caro (click-ops, secretos horneados en la imagen, release sin rollback, alertas que nadie atiende).

**Reglas sueltas donde el error es notoriamente frecuente y no hay ejemplo:**

| Regla | Error frecuente que el ejemplo evitaría |
|---|---|
| `03·D2` | editar una migración ya ejecutada en vez de crear una nueva |
| `04·S7` / `10·DEP3` | dar por auditada una dependencia porque "la instaló el framework" |
| `08·T4` | apuntar la config de pruebas a la BD de desarrollo con datos reales |
| `09·G4` | trabajar directo sobre la rama principal "porque es un cambio chico" |
| `11·CFG3` | aplicar en producción un ajuste "de memoria" que nunca se documentó |
| `11·CFG4` | dejar una bandera de feature encendida para siempre |
| `15·IM2`, `15·IM5` | usar "Eliminar" donde el registro exige "Anular" |
| `17·I3`, `I5`, `I6` | transmitir estado solo por color; inventar componentes fuera del sistema de diseño |
| `20·M2`, `M4`, `M7`, `M9`, `M10`, `M12`, `M13` | las meta-reglas se aplican mal más que ninguna, y siete de trece no traen ejemplo |

**Recomendación.** Añadir el par INCORRECTO/CORRECTO. Regla de calidad del ejemplo, de `estructura-regla.md:214`: *"El renglón de INCORRECTO se escribe con el error que la gente comete de verdad. Si se pone uno exagerado, que nadie cometería, no sirve de nada."* Versión **PARCHE**.

---

### H-15 · Reglas que exceden una página sin abrir subcarpeta · **Media**

**Meta-regla:** `M2` (*"Si una sola regla crece más de una página, se le abre subcarpeta y el capítulo deja el resumen y el enlace"*) · `M5` (cuerpo de 1–4 líneas)

Solo `F12` y `F13` aplicaron el mecanismo. Las que debían y no lo hicieron:

| Regla | Líneas | Acción |
|---|---|---|
| `02·F4.3` | **78** | subcarpeta + partir en 4 (H-09) |
| `13·DOC14` | **58** | partir en formato de enlace + requisito de render (H-09), y limpiar `M3` (H-07) |
| `03·D7` | **41** | subcarpeta: el patrón SCD-2 de 8 pasos es un anexo, la regla son 3 líneas |
| `13·DOC12` | **41** | el formato canónico del bloque de fase es anexo |
| `13·DOC13` | **38** | el contenido mínimo del catálogo es anexo o plantilla |
| `02·F0` | 36 | ver H-01 |
| `02·F4.5` | 35 | partir (H-09) |
| `02·F11` | 34 | resumir; las excepciones al anexo |
| `02·F10` | 33 | resumir |
| `02·F4.4` | 32 | resumir |
| `04·S11` | 30 | partir (H-09) |
| `01·C14` | 29 | resumir; la lista de dominios al anexo |

`M5` pide **1 a 4 líneas de cuerpo**. Ninguna de las 12 se acerca. `estructura-regla.md:172` dice qué hacer: *"Si no cabe, casi siempre pasa una de dos: hay dos órdenes juntas, o se está contando **por qué** existe la regla — y el porqué se guarda en `notas/`, no aquí."*

**Observación de rendimiento, no solo de estética:** `base/` se carga entero en cada sesión. `02-flujo-de-trabajo.md` son 45 KB y `13-documentacion.md` 30 KB — juntos, más de la mitad del contexto que consumen las reglas. Adelgazarlos con anexos enlazados es también trabajo de eficiencia.

---

### H-16 · Numeración decimal fuera de `M4` · **Media**

**Meta-regla:** `M4` (`<PREFIJO><n>`, consecutivo, prefijo exclusivo)

**18 identificadores decimales:** `F4.1`, `F4.2`, `F4.3`, `F4.4`, `F4.5` y `F12.1`–`F12.13`.

`M4` no contempla sub-IDs. Tres consecuencias reales:

1. **Sugieren jerarquía que no existe.** `F4.2` (ciclo de 11 etapas) y `F4.3` (línea base verificada) no son detalles de `F4` (aprobación del plan): son reglas independientes con exigencias propias. `M4` es explícita: *"Si una regla se parte en dos, la original conserva su ID y la nueva toma el siguiente consecutivo libre."* El consecutivo libre era `F14`, no `F4.1`.
2. **Sugieren orden de ejecución.** `M2` dice *"La numeración es historia, no prioridad"*, y `F13` tuvo que escribir un descargo explícito (*"el ID `F13` es solo catálogo, no orden"*) precisamente porque el decimal ya había instalado la idea contraria.
3. **Rompen la tabla de prefijos.** `estructura-regla.md:64-86` lista los prefijos ocupados; ninguna entrada contempla decimales, así que un validador de IDs escrito contra esa tabla los rechazaría.

**Recomendación.** Dos vías; la segunda es la barata:

- **(a)** Renumerar a consecutivo — **descartada**: `M4` prohíbe renumerar y decenas de citas (`02·F4.3`, `F12.6`, `F12.13`) quedarían huérfanas. El daño supera el beneficio.
- **(b) Legalizar** — `M4` reconoce el sub-ID `<PREFIJO><n>.<m>` con una condición: **solo cuando la subparte no se puede cumplir sin la parte**. Bajo esa condición `F12.1`–`F12.13` califican (son la misma decisión del usuario) y `F4.1`–`F4.5` **no** (se cumplen por separado) → estas cinco se marcan como deuda a partir en su próxima revisión, conservando sus IDs por compatibilidad y sumando alias. Versión **MENOR** en `M4`.

---

### H-17 · Diez formas de escribir la misma cita · **Media**

**Meta-regla:** `M4` (*"Se cita entre capítulos como `NN·ID`"*) · higiene de enlaces

Variantes encontradas en `base/`: `` `00` · N4 ``, `` `00·N4` ``, `` `00` N4 ``, `` 00 N4 ``, `` `13` DOC10 ``, `` `02` F4.3 ``, `` `05`·E3 ``, `` `04·S4` ``, `` `18·DP1` ``, `` (ver `04·S4`) ``.

**Por qué importa más de lo que parece.** `validadores/enlaces.py` ya existe y la Higiene del conjunto lo declara obligatorio: *"una regla que cita a otra por ID depende de que el ID exista. El validador de enlaces lo detecta; no se ignora."* Con diez formatos, el validador o falla en detectar citas o produce falsos positivos. Normalizar a `NN·ID` es requisito para que el validador sirva.

**Caso especial — cita rota.** `01·C14` dice: *"Refuerza `00 N3` (no atajos no profesionales) y `01 C1` (**no ofrecer opciones claramente subóptimas**)."* `C1` es *"Avisa antes de tocar"*. La glosa no corresponde a `C1` ni a ninguna regla del capítulo 01. Y `N3` es *"No romper cosas para pasar un obstáculo"*, que tampoco es *"no atajos no profesionales"*. Dos citas mal atribuidas en una línea. **Prioridad Alta** para esta corrección puntual.

**Recomendación.** Normalizar con un pase mecánico a `` `NN·ID` `` y activar `enlaces.py` sobre `base/` en el hook de sesión. Versión **PARCHE**.

---

### H-18 · Tres capítulos exceden el tamaño que `M2` sugiere · **Media**

**Meta-regla:** `M2` (*"si un capítulo pasa de ~15 reglas, probablemente son dos dominios; partirlo"*)

| Capítulo | Reglas | Los dos dominios que contiene |
|---|---|---|
| `01 · Conducta` | **18** | (a) conducta y alcance del agente: `C1`–`C9`, `C11`–`C12`, `C16` · (b) protocolo de interacción y aprobación: `C7`, `C10`, `C13`, `C14`, `C15`, `C17`, `C18` |
| `13 · Documentación` | **16** | (a) qué se documenta al entregar: `DOC1`–`DOC5`, `DOC14` · (b) artefactos de proceso y sus índices vivos: `DOC6`–`DOC13`, `DOC15`, `DOC16` |
| `02 · Flujo de trabajo` | **19** (+13 subpartes) | (a) el flujo: `F0`–`F3`, `F5`–`F7` · (b) planificación y contrato del plan: `F4`–`F4.5`, `F8`–`F11` |

**Recomendación.** Partir es **caro** (`M2` prohíbe renumerar; los IDs viajarían al capítulo nuevo conservando su prefijo, lo que rompe *"el prefijo es exclusivo de un capítulo"*). Dos salidas:

- **Barata, recomendada:** no partir. Mantener el prefijo y el ID, y reorganizar el capítulo **por secciones internas** con encabezado, dejando constancia en `M2` de que el umbral de ~15 se relaja cuando partir obligaría a mover prefijos. Es un ajuste de `M2`, no una violación a perpetuidad.
- **Cara:** partir de verdad, aceptando que `01` y `01b` compartan el prefijo `C`, lo que exigiría relajar `M4`.

Se recomienda la primera y **escribirla en `M2`**, para que deje de figurar como incumplimiento permanente de tres capítulos.

---

### H-19 · Reglas que solo son enlaces · **Baja**

**Meta-reglas:** `M2` (enlaza, no repitas) · `M5` (una exigencia propia)

`12·PR3 · Protégelos en reposo y en tránsito` no exige nada propio: sus cuatro afirmaciones remiten a `04·S5`, `04·S6`, `04·S1` y `04·S5`. Es un índice con formato de regla. Casos parecidos, menos extremos: `12·PR4` (remite a `05·E5`), `08·T4` (remite a `00·N4`), `05·E5` (remite a `00·N6`), `04·S8` (remite a `05`).

**Recomendación.** No borrarlas — cumplen función de puerta de entrada desde el capítulo de privacidad. Reescribirlas para que su exigencia propia sea la **aplicación al dominio del capítulo** (*"los datos personales heredan los controles de `04`; además, el proyecto declara cuáles se cifran en reposo"*), no la repetición. Versión **PARCHE**.

---

### H-20 · Defectos de registro en `M10` y `M13` · **Media**

**`M10` — el CHANGELOG registra mal el capítulo 20.** `CHANGELOG.md:34` anuncia el capítulo como **`00 · Meta-reglas`**; el capítulo entregado es **`20 · Meta-reglas`**. Un lector que busque `00 · Meta-reglas` encuentra `00-identidad-y-rol.md` y `00-nucleo-blindado.md`, ninguno de los dos. Corregir la entrada del CHANGELOG (**PARCHE**).

**`M13` — la tabla de enrutamiento no cubre el repo real.** La tabla lista 7 destinos: `base/`, `.agente/reglas-proyecto.md`, `CLAUDE.md`, `notas/`, `pendientes/`, memoria del agente, `historico-chat/`. El repo tiene además `plantillas/`, `skills/`, `validadores/`, `memoria/`, `metricas/`, `interfaz/`, `prompts/`, `analisis/` y `anatomia/` — nueve carpetas sin fila. Cuando alguien produce un artefacto nuevo, `M13` no le dice dónde va, y por eso es previsible que termine en `base/`, que es justo lo que `M13` quiere evitar.

**Recomendación.** Ampliar la tabla de `M13` con las carpetas reales. La zonificación de [`anatomia/mapa-del-sitio.md`](../anatomia/mapa-del-sitio.md) (Norma · Herramientas · Bitácora · Apoyo) ya resuelve el criterio: importarlo a `M13` como agrupador. Versión **MENOR**.

**`M11` — nunca ejercida.** Cero reglas marcadas `[DEROGADA]`, con seis pares duplicados esperando consolidación (H-06). No es incumplimiento hoy, pero indica que el mecanismo está sin estrenar: la primera derogación conviene hacerla con cuidado y dejarla como referencia.

---

### H-21 · `estructura-regla.md` viola la regla de lenguaje del propio estándar · **Media**

**Meta-reglas:** Higiene del conjunto (*"Lenguaje: imperativo, corto, técnico y sin adornos. Lo que el usuario final lee es otra cosa (`17·I4`); estas reglas las lee el agente"*) · `M13` · `M2`

**Qué se encontró.** El archivo está escrito en registro deliberadamente coloquial: *"Dos gatitos, siempre dos"*, *"es como el número de la camiseta: aunque el jugador se corte el pelo, sigue siendo el 7"*, *"lo más barato, y casi siempre alcanza con eso"*. `17·I4` marca la frontera al revés y en el mismo repo: el registro sencillo es **para el usuario final**; las reglas del agente son técnicas.

**Tres cuestiones aparte, en el mismo archivo:**

1. **`M5` no lo enlaza.** El archivo dice *"En `base.md` queda el resumen; el detalle está solo aquí"*, pero `M5` en `base.md` no menciona su existencia. El enlace es de una sola dirección: quien lee `M5` nunca se entera de que hay un molde desarrollado. Rompe `M2` (fuente única con resumen **y enlace**).
2. **Puede estar mal enrutado.** `M13` manda el *"instructivo para mantener el estándar (cómo redactar, qué versionar)"* a `CLAUDE.md`. El archivo se autodescribe así: *"Quien vaya a escribir una regla nueva, copia el molde y lo rellena."* Es instructivo, no norma — y viaja a todos los proyectos que heredan `base/`, que nunca escriben reglas del estándar.
3. **Tabla de prefijos con deriva de nombres.** Lista `E · 05 · Errores y registro` (el capítulo es *"Manejo de errores y logging"*) e `IM · 15 · Registros que no se borran` (el capítulo es *"Registros inmutables"*). Divergencia menor pero es la tabla que se consulta para no repetir prefijos.

**Recomendación.** Es la corrección de **menor coste y mayor efecto** de todo el informe:

- Añadir a `M5` una línea que enlace al molde desarrollado — [`base/20-meta-reglas/estructura-regla.md`](../base/20-meta-reglas/estructura-regla.md), que desde `base.md` es un enlace relativo a `estructura-regla.md` a secas.
- Decidir con el usuario si el archivo se queda en `base/20-meta-reglas/` (y entonces se reescribe en registro técnico) o si se mueve a `CLAUDE.md` / `notas/` (y entonces el registro coloquial es legítimo, porque el lector es el humano que mantiene el estándar). **Son dos decisiones distintas y la segunda condiciona a la primera** — se pregunta antes de tocar.
- Alinear los nombres de la tabla de prefijos con los títulos reales de los capítulos.

---

### H-22 · Dos capítulos comparten el número `00` · **Baja**

**Meta-regla:** `M2` (*"Cada dominio tiene **un** archivo `NN-nombre.md`"* · *"Un número no se reutiliza"*)

`00-identidad-y-rol.md` (Preámbulo) y `00-nucleo-blindado.md` (Capa 1) comparten el `00`. `M1` los separa por capa, así que la convivencia es intencional, pero `M2` no la contempla y el efecto colateral es real: **`00-identidad-y-rol.md` no tiene ninguna regla con ID** (0 encabezados `##`) y sin embargo `F0` lo cita dos veces en la columna *"Dónde está la regla"* de su tabla de pasos (pasos 2 y 3). Se cita como fuente de regla algo que no tiene reglas citables.

En la misma columna, `F0` cita como "regla" a `plantillas/ciclo-vida-proyectos/01-planteamiento.md`, `skill analizar-proyecto` y `skill proponer-alcance`. Ninguno es regla con ID.

**Recomendación.** Dos cosas pequeñas: (a) `M2` reconoce que el preámbulo no consume número de capítulo (o se le da uno propio), (b) `F0` renombra la columna a *"Dónde se define"* y, para los pasos 2 y 3, se crean reglas con ID donde hoy hay prosa — o se acepta que esos pasos los gobiernan las skills y se dice así.

> **Corregido en** [`base/00-identidad-y-rol/`](../base/00-identidad-y-rol/base.md) — el capítulo tiene ahora seis reglas con ID (`ID1`–`ID6`), una por archivo en [`reglas/`](../base/00-identidad-y-rol/reglas/), con el prefijo `ID` registrado en la tabla de letras ocupadas. Queda abierto lo demás del hallazgo: el número `00` sigue compartido y `F0` sigue citando skills y plantillas como si fueran reglas.

---

## 5 · Inventario regla por regla

**Leyenda.** ✅ cumple · 🟡 cumple con observaciones · ❌ incumple. La columna **Hallazgos** remite a §4. **Ubicación** es `archivo:línea`.

### 5.1 · `00 · Núcleo blindado` — 6 reglas · [`base/00-nucleo-blindado.md`](../base/00-nucleo-blindado.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `N1 · No ejecutar sin validación` | `:7` | ❌ | `M5` `M8` `M1` `M12` | excepción / unicidad / duplicación | H-04, H-09 · `[BLINDADA]` con excepción escrita; dos exigencias (no ejecutar sin aprobación + no reintentar tras rechazo); la excepción repite `02·F3` | Renombrar la excepción a "Alcance de la autorización"; partir el "no reintentes" a `N7`; enlazar `F3` en vez de repetirlo | **Alta** |
| `N2 · Control de versiones solo bajo pedido` | `:18` | ✅ | `M5` `M8` | molde / ejemplo | Cumple. La "autorización de un solo uso" es límite de la misma exigencia, no una segunda | — | — |
| `N3 · No romper cosas para pasar un obstáculo` | `:28` | ✅ | `M5` | molde / ejemplo | Cumple. Modelo de regla blindada bien escrita | — | — |
| `N4 · Proteger los datos reales` | `:37` | 🟡 | `M5` `M8` | unicidad | H-09 · dos exigencias: prohibición de destructivas + verificar punto de restauración | Partir el punto de restauración a `N8` | Media |
| `N5 · Operaciones masivas: previsualizar antes de aplicar` | `:49` | ✅ | `M5` | molde / ejemplo | Cumple. Los 4 pasos son una sola exigencia secuencial | — | — |
| `N6 · Secretos y datos sensibles nunca se exponen` | `:58` | ❌ | `M5` `M2` `M12` | unicidad / duplicación | H-06, H-09 · tres exigencias (no incrustar/loguear/commitear · no enviar a externos · archivos no públicos); la tercera duplica `04·S6` | Partir en tres; la tercera se sustituye por enlace a `S6` | Media |

### 5.2 · `01 · Conducta` — 18 reglas · [`base/01-conducta.md`](../base/01-conducta.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `C1 · Avisa antes de tocar` | `:7` | 🟡 | `M8` `M12` | excepción / duplicación | H-12 · la excepción entre paréntesis no dice quién autoriza; repite `02·F3` por tercera vez (con `N1`) | Enlazar `F3`; completar la excepción | Baja |
| `C2 · No inventes: verifica` | `:17` | ✅ | `M5` `M6` | molde / choque | Cumple. Su tensión con `C11` está resuelta en el texto de `C11` | — | — |
| `C3 · Quédate en tu tarea` | `:26` | ✅ | `M5` `M2` | molde / dueño | Cumple. Es el dueño del tema alcance; `07·Q7` y `14·EST3` lo replican (ver sus filas) | — | — |
| `C4 · No decidas por tu cuenta` | `:35` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `C5 · Responde corto` | `:44` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `C6 · Confirma que es tu archivo` | `:54` | 🟡 | `M5` `M12` | ejemplo / duplicación | H-14 · sin ejemplo; solapa parcialmente `C2` y `C16` | Añadir ejemplo o absorber en `C16` | Baja |
| `C7 · Ante dos lecturas, pregunta` | `:58` | ✅ | `M5` | molde / ejemplo | Cumple. Es el autorizador natural que le falta a muchas excepciones (H-12) | — | — |
| `C8 · Habla el idioma del proyecto` | `:67` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo | Añadir ejemplo | Baja |
| `C9 · Reporta los tropiezos` | `:71` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `C10 · Cada mensaje del usuario se evalúa como posible mejora del setup` | `:81` | ❌ | `M3` `M5` `M12` | agnosticismo / unicidad / tamaño | H-07, H-09, H-15 · 21 líneas; nombra `SQLite`, `MariaDB`, `React`, `Django`, "este ERP"; tres exigencias (aplicar · evaluar alcance · proponer absorción); solapa `13·DOC10` | Reescribir a concepto; llevar los ejemplos de stack a `plantillas/`; partir la absorción | Media |
| `C11 · Confía en las afirmaciones del usuario sobre estado del sistema` | `:103` | 🟡 | `M5` `M6` | tamaño / choque | H-15 · 10 líneas; la tensión con `C2` está declarada y resuelta (buen ejemplo de `M6` bien aplicado) | Comprimir a 4 líneas | Baja |
| `C12 · No agregues calificativos al nombre del artefacto` | `:114` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `C13 · Preguntas de análisis van en chat abierto, no en formulario cerrado` | `:125` | 🟡 | `M5` | tamaño | H-15 · 15 líneas para una sola exigencia bien delimitada | Comprimir | Baja |
| `C14 · Aplicar el estándar profesional del dominio como default` | `:142` | ❌ | `M7` `M5` `M3` | dependencias / tamaño / agnosticismo | **H-17 (cita rota)**, H-09, H-15 · atribuye a `01·C1` un texto que `C1` no tiene y glosa mal `00·N3`; 29 líneas; enumera sectores (`M3` borderline) | Corregir las dos citas **ya**; comprimir; mover la casuística de sectores a anexo | **Alta** |
| `C15 · Al replicar un patrón, replicar la paridad completa` | `:172` | ❌ | `M3` `M7` `M5` | agnosticismo / dependencias / tamaño | H-02, H-07, H-15 · nombra "módulo Aportes"; `Encadenamiento` fuera de `M7`; 24 líneas | Sustituir el nombre propio por `<módulo referente>`; normalizar dependencia | Media |
| `C16 · Re-lee justo antes de editar` | `:196` | ❌ | `M3` `M7` `M5` `M12` | agnosticismo / dependencias / tamaño | H-02, H-07, H-15 · nombra `git status --short`, `git diff`, herramientas `Read`/`Edit`, `ide_opened_file`; 24 líneas; su propio `Encadenamiento` admite que duplica `C2` | Reescribir el procedimiento en concepto; declarar `(extiende 01·C2)` | Media |
| `C17 · Confirma tu entendimiento antes de ejecutar` | `:221` | ❌ | `M5` `M7` `M8` | unicidad / dependencias / excepción | H-02, H-09, H-12 · 26 líneas; tres exigencias (confirmar · qué cuenta como aprobación · formato); la lista "NO aplica a" no dice quién autoriza | Partir "qué cuenta como aprobación" a regla propia (la citan `F4`, `F9`, `F4.4`) | Media |
| `C18 · Auto-sincronización del `CLAUDE.md` con la plantilla central` | `:247` | 🟡 | `M5` `M7` `M9` | tamaño / dependencias | H-02, H-15 · 20 líneas; `Encadenamiento` fuera de `M7`. Validable y **registrada** (`sesion.py`) ✅ | Comprimir; el porqué de vivir en `base/` va a `notas/` | Baja |

### 5.3 · `02 · Flujo de trabajo` — 19 reglas (+13 subpartes) · [`base/02-flujo-de-trabajo/`](../base/02-flujo-de-trabajo/base.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `F0 · La secuencia completa` | `:7` | ❌ | `M2` `M5` `M8` | fuente única / molde / excepción | **H-01** (corrección publicada sin aplicar), H-13, H-22 · 36 líneas; título nominal; excepción sin `autoriza`; cita como reglas a `00-identidad` y dos skills, que no tienen ID | Aplicar el texto corregido de `estructura-regla.md:143` | **Alta** |
| `F1 · Carga el contexto antes de actuar` | `:44` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `F2 · Sin spec acordada no hay código` | `:54` | 🟡 | `M8` `M5` | excepción / unicidad | H-09, H-12 · excepciones sin límite ni autorizador; el procedimiento de 2 puntos es una segunda exigencia | Completar la excepción; partir el procedimiento | Media |
| `F3 · Plan aprobado = ejecución continua` | `:71` | 🟡 | `M2` `M12` | duplicación | H-06 · el mismo criterio aparece en `N1` (excepción), `C1` (paréntesis) y `F9`. `F3` es el dueño legítimo | Que `N1`, `C1` y `F9` enlacen aquí | Media |
| `F4 · Todo plan lleva su plan de pruebas y su aprobación explícita` | `:80` | ❌ | `M5` `M2` | unicidad / título con "y" | H-09 · tres exigencias (plan de pruebas · verificar la cadena previa · aprobación explícita en 5 pasos); 30 líneas; el plan de pruebas es tema de `08` | Partir en tres; el plan de pruebas enlaza a `08·T1` | **Alta** |
| `F4.1 · Preguntas que TODO plan debe responder` | `:112` | ❌ | `M4` `M5` | ID / tamaño | H-15, H-16 · ID decimal; 28 líneas. La exigencia ("responder las 13") es única y legítima | Legalizar el sub-ID o promover a `F14`; llevar las 13 preguntas a `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` y dejar el enlace | Media |
| `F4.2 · Ciclo consolidado de una fase — 11 etapas` | `:143` | ❌ | `M4` `M5` `M8` | ID / molde / excepción | H-09, H-16 · ID decimal; la tabla de 11 etapas es mapa, no orden (pista de `estructura-regla.md`); la excepción de trabajos triviales no fija límite | Mover la tabla al encabezado del capítulo; dejar la exigencia ("ninguna etapa se salta ni se reordena") en 3 líneas | Media |
| `F4.3 · Plan sobre línea base verificada` | `:165` | ❌ | `M2` `M4` `M5` | subcarpeta / ID / unicidad | **H-15** (78 líneas, la mayor del catálogo), H-09, H-16 · cuatro exigencias independientes | Abrir `base/02-flujo-de-trabajo/F4.3/`; partir en 4 | **Alta** |
| `F4.4 · `plan_trabajo` se deriva de los CA de la HU` | `:244` | ❌ | `M4` `M7` `M5` | ID / dependencias / tamaño | H-02, H-15, H-16 · 32 líneas; `Encadenamiento` con ciclo declarado hacia `F4.5` | Fusionar con `F4.5` o declarar la dependencia en una sola dirección | Media |
| `F4.5 · Ejecutar LITERAL los CA` | `:276` | ❌ | `M5` `M4` `M7` | unicidad autodeclarada | **H-09** (*"Dos partes indivisibles"*), H-02, H-16 · 35 líneas | Partir en dos; resolver el ciclo con `F4.4` | **Alta** |
| `F5 · Ejecuta las pruebas antes de dar por terminado` | `:312` | ❌ | `M2` `M5` `M12` | dueño / texto prestado | **H-06** · duplica `08·T5` con ejemplo idéntico palabra por palabra | Derogar → `08·T5`; el alcance quirúrgico de la corrida se traslada a `08` | **Alta** |
| `F6 · Persiste el trabajo y las decisiones` | `:337` | ❌ | `M2` `M12` | dueño | **H-06** · duplica `13·DOC1` | Derogar → `13·DOC1` | **Alta** |
| `F7 · Verifica trazabilidad spec → implementación` | `:341` | ❌ | `M2` `M5` `M12` | dueño / texto prestado | **H-06** · duplica `13·DOC3`, ejemplo incluido | Derogar → `13·DOC3` | **Alta** |
| `F8 · Solo se tocan archivos declarados en el plan` | `:350` | 🟡 | `M5` `M7` | tamaño / dependencias | H-02, H-15 · 26 líneas; `Encadenamiento`. Exigencia única y bien delimitada | Comprimir a 4 líneas + protocolo en anexo | Media |
| `F9 · Plan aprobado se ejecuta completo` | `:377` | ❌ | `M2` `M12` `M7` | duplicación | H-02, H-06 · su propio `Encadenamiento` admite que `F3` *"es el enunciado base"*; 28 líneas | Fusionar con `F3` o declarar `(extiende 02·F3)` y comprimir | Media |
| `F10 · Producción no bloquea el desarrollo` | `:406` | 🟡 | `M5` `M7` | tamaño | H-02, H-15 · 33 líneas; la casuística por tipo de cambio es anexo | Comprimir; casuística a anexo | Media |
| `F11 · Una fase solo modifica código de su propio módulo` | `:440` | ❌ | `M5` `M8` `M7` | unicidad / excepción | H-02, H-09, H-12 · dos exigencias (un módulo **y** una sola HU); excepciones de infraestructura sin autorizador; 34 líneas | Partir la condición "una sola HU" (ya vive en `F12.1`) → enlazar; completar excepción | Media |
| `F12 · Relación y nomenclatura de fases` | `:480` → [`reglas/F12-…`](../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) | ❌ | `M4` `M5` `M2` `M8` | ID / molde / dueño | **H-11** · 13 subpartes sin encabezado ni molde; congelación no escrita como excepción; mezcla relación + nomenclatura + ruta física | Preguntar al usuario la vía (envolver en molde sin tocar texto, o legalizar la congelación en `M5`) | **Alta** |
| `F13 · Estructura base obligatoria del proyecto` | `:484` → [`reglas/F13-…`](../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) | ❌ | `M5` `M13` | marca / molde | **H-11** · marca inventada `[GATE DE ARRANQUE · PRECONDICIÓN]`, que es el anti-ejemplo literal de `estructura-regla.md:60`; el archivo fuente única no tiene encabezado de regla | Quitar la marca; añadir encabezado de regla en la fuente única. Validable y registrada (`sesion.py`) ✅ | **Alta** |
| `F12.1`–`F12.13` | `reglas/F12-…` | ❌ | `M4` `M5` | ID / molde | H-11 · viñetas sin encabezado; `F12.13` (ruta física) es un tema distinto al de las otras doce y es fuente única citada por `DOC15`, `DOC16`, `F13` | Promover `F12.13` a regla propia del capítulo | **Alta** |

### 5.4 · `03 · Datos y persistencia` — 8 reglas · [`base/03-datos.md`](../base/03-datos.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `D1 · Toda tabla nueva se normaliza y lleva auditoría` | `:7` | ❌ | `M5` `M2` | título con "y" / unicidad / dueño | H-06, H-09 · tres exigencias; el bloque de índices duplica `06·R3` | Partir en `D1`/`D9`/`D10`; los índices enlazan a `06·R3` | **Alta** |
| `D2 · Cada cambio de esquema es una migración reversible` | `:23` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo, y "editar una migración ya ejecutada" es error frecuente. Validable y registrada (`migraciones.py`) ✅ | Añadir ejemplo | Baja |
| `D3 · Migraciones retrocompatibles` | `:27` | ✅ | `M5` | molde / ejemplo | Cumple. Validable y registrada (`esquema.py`) ✅ | — | — |
| `D4 · Valores configurables van a catálogo` | `:40` | 🟡 | `M5` `M8` | tamaño / excepción | H-12, H-15 · 25 líneas; excepciones sin autorizador; el bloque "cuando el catálogo genérico no cabe" es exigencia aparte | Completar excepción; partir el caso de tabla propia | Media |
| `D5 · Con la BD desplegada, la validación nueva va en la app` | `:66` | 🟡 | `M8` | excepción | H-12 · el "No aplica en diseño desde cero" no fija límite ni autorizador | Completar | Baja |
| `D6 · Concurrencia e idempotencia` | `:83` | ❌ | `M5` | título nominal / unicidad | H-09, H-13 · tres exigencias (idempotencia · lost update · duplicados por carrera) | Partir en tres con títulos imperativos | Media |
| `D7 · Persistencia histórica SCD-2` | `:96` | ❌ | `M2` `M5` `M7` | subcarpeta / tamaño | H-02, H-15 · 41 líneas; patrón de 8 pasos + alternativa de volumen dentro de la regla | Abrir anexo `F.../D7/`; dejar 3 líneas + enlace | Media |
| `D8 · Distinguir pertenencia de autoría` | `:138` | ❌ | `M3` `M5` `M7` | agnosticismo / tamaño | H-02, H-07, H-15 · ejemplo con código de un stack y entidad concreta (`Aporte::where('usercreate_id', Auth::id())`); 26 líneas | Reescribir el ejemplo en pseudocódigo agnóstico | Media |

### 5.5 · `04 · Seguridad de la aplicación` — 11 reglas · [`base/04-seguridad.md`](../base/04-seguridad.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `S1 · Autorización en cada acción sensible` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `S2 · Valida y sanea toda entrada externa` | `:20` | ✅ | `M5` | molde / ejemplo | Cumple. Validable y registrada (`seguridad.py`) ✅ | — | — |
| `S3 · Nunca construyas consultas ni comandos por concatenación` | `:34` | 🟡 | `M5` | unicidad | H-09 · tres frentes (BD · shell · asignación masiva); el tercero no es concatenación | Partir la asignación masiva a `S12` | Baja |
| `S4 · Gestión de secretos` | `:48` | 🟡 | `M5` `M2` `M13` | título nominal / dueño | H-06, H-13 · duplica `11·CFG1`/`CFG2` y `09·G3`. Validable y registrada (`secretos.py`) ✅ | Título imperativo; repartir dueños con `11` | Media |
| `S5 · CSRF, sesiones y transporte` | `:61` | ❌ | `M5` | título con "y" / unicidad / ejemplo | H-09, H-13, H-14 · cuatro exigencias; sin ejemplo | Partir en cuatro | Media |
| `S6 · Archivos sensibles: privado + acceso controlado` | `:68` | 🟡 | `M5` `M12` | unicidad / duplicación | H-06, H-09 · cinco sub-exigencias; solapa `00·N6` | Partir preservación y backup; `N6` enlaza aquí | Media |
| `S7 · Dependencias sin vulnerabilidades conocidas` | `:83` | ❌ | `M2` `M12` | dueño | **H-06** · duplica `10·DEP3` en referencia circular; sin ejemplo | Derogar → `10·DEP3` | Media |
| `S8 · No filtres información en errores` | `:87` | 🟡 | `M2` `M12` | dueño | H-06 · duplica `05·E3` (tercer punto) | Que `E3` enlace aquí, o al revés; un solo dueño | Baja |
| `S9 · No toques rutas del sistema fuera del proyecto` | `:96` | ✅ | `M5` `M8` | excepción completa | **Modelo de referencia**: la excepción declara condición, límite y autorizador | Usar como plantilla para H-12 | — |
| `S10 · No mates procesos globales` | `:115` | 🟡 | `M3` `M8` | agnosticismo | H-07 (baja) · nombra `killall`/`pkill`/`taskkill`, defendible; excepción con autorizador ✅ | Mantener | Baja |
| `S11 · Escritura contra el almacén productivo requiere autorización por operación` | `:134` | ❌ | `M5` `M3` `M7` | unicidad autodeclarada / agnosticismo | **H-07, H-09** · se autodeclara *"Regla 1"* y *"Regla 2"*; nombra `destroy()`, `SoftDeletes`, `deleted_at`; 30 líneas | Partir en dos; reescribir en concepto | **Alta** |

### 5.6 · `05 · Errores y logging` — 5 reglas · [`base/05-errores-y-logging.md`](../base/05-errores-y-logging.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `E1 · No te tragues los errores en silencio` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple. Validable y registrada (`errores.py`) ✅ | — | — |
| `E2 · Falla controlado, no rodees el problema` | `:20` | 🟡 | `M5` | unicidad | H-09 · dos exigencias (abortar temprano · transacción) | Partir la transacción a `E6` (la citan `15·IM3`, `13`…) | Baja |
| `E3 · Mensajes en dos niveles: usuario y diagnóstico` | `:32` | 🟡 | `M2` | dueño | H-06 · su tercer punto duplica `04·S8` | Enlazar `S8` | Baja |
| `E4 · Loguea con niveles y con propósito` | `:43` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `E5 · Nunca registres secretos ni datos sensibles` | `:57` | 🟡 | `M5` `M12` | texto prestado | H-06 · reformula `00·N6` en vez de solo enlazarlo; y `12·PR4` la reformula a su vez | Dejar el enlace y la aplicación al dominio de logs | Baja |

### 5.7 · `06 · Rendimiento` — 6 reglas · [`base/06-rendimiento.md`](../base/06-rendimiento.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `R1 · Evita consultas en bucle (N+1)` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple. Validable y registrada (`rendimiento.py`) ✅ | — | — |
| `R2 · Nunca cargues conjuntos sin límite` | `:16` | ✅ | `M5` | unicidad | Cumple: paginar/lotes/columnas son caras de la misma exigencia. Validable ✅ | — | — |
| `R3 · Índices en lo que se filtra y ordena` | `:27` | 🟡 | `M2` `M12` | dueño | H-06 · duplica el tercer bloque de `03·D1` | Un solo dueño: `R3`; `D1` enlaza | Media |
| `R4 · Cachea lo caro y estable, con invalidación clara` | `:36` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `R5 · Trabajo pesado fuera del ciclo de petición` | `:45` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `R6 · Mide antes de optimizar` | `:54` | ✅ | `M5` | molde / ejemplo | Cumple. Es la regla que `estructura-regla.md` usa como modelo de "ejemplo mínimo" | — | — |

### 5.8 · `07 · Calidad de código` — 7 reglas · [`base/07-calidad-de-codigo.md`](../base/07-calidad-de-codigo.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `Q1 · Escribe como el código que lo rodea` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `Q2 · Nombres que dicen la intención` | `:16` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `Q3 · Funciones pequeñas, una responsabilidad` | `:25` | ✅ | `M5` | molde / ejemplo | Cumple. Validable y registrada (`calidad.py`) ✅ | — | — |
| `Q4 · No repitas (DRY), pero no abstraigas de más` | `:34` | 🟡 | `M5` | título con "pero" / unicidad | H-09 · dos exigencias en tensión. Caso límite: la tensión **es** el contenido | Mantener como una, pero escribir la segunda mitad como excepción formal (`M8`) de la primera | Baja |
| `Q5 · Comenta el porqué, no el qué` | `:43` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `Q6 · Linter y formateador automáticos` | `:52` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo. Validable y registrada (`herramientas.py`) ✅ | Añadir ejemplo | Baja |
| `Q7 · Deja el código mejor, pero en tu alcance` | `:56` | 🟡 | `M2` `M12` | dueño | H-06 · replica `01·C3`, igual que `14·EST3` | Comprimir a enlace + la aplicación propia al refactor | Baja |

### 5.9 · `08 · Estrategia de pruebas` — 7 reglas · [`base/08-pruebas.md`](../base/08-pruebas.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `T1 · Todo cambio con lógica lleva prueba` | `:7` | 🟡 | `M8` `M5` | excepción / ejemplo | H-12, H-14 · el "si no amerita, decláralo" deja al agente autorizándose a sí mismo; sin ejemplo | Fijar autorizador (usuario) y límite; añadir ejemplo | Media |
| `T2 · Prueba el comportamiento, no la implementación` | `:11` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `T3 · Aisladas, deterministas, repetibles` | `:20` | 🟡 | `M5` | unicidad | H-09 · tres exigencias. Validable y registrada (`aislamiento.py`) ✅ | Partir en tres o declarar que son caras de un mismo invariante | Baja |
| `T4 · Protege los datos reales al probar` | `:31` | 🟡 | `M5` `M12` | texto prestado / ejemplo | H-06, H-14 · reformula `00·N4`; sin ejemplo pese a ser error frecuente | Enlazar `N4`; añadir ejemplo | Media |
| `T5 · Ejecuta y reporta` | `:36` | ❌ | `M2` `M5` | dueño / texto prestado | **H-06** · idéntica a `02·F5`, ejemplo incluido. `T5` es el dueño correcto | Recibir lo que hoy está en `F5` (alcance quirúrgico de la corrida) tras derogarla | **Alta** |
| `T6 · Cobertura con criterio, no por porcentaje` | `:45` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `T7 · Triangulación: derivar los casos, no adivinarlos` | `:54` | ❌ | `M5` | unicidad autodeclarada / tamaño | H-09, H-15 · declara *"dos frentes"*; 26 líneas; el título nombra solo el primero | Partir: `T7` derivar casos · `T8` triangular el resultado esperado | Media |

### 5.10 · `09 · Control de versiones` — 8 reglas · [`base/09-git.md`](../base/09-git.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `G1 · Commits atómicos, un solo propósito` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `G2 · Mensajes que explican qué y por qué` | `:16` | ✅ | `M5` | "y" que no cuenta | Cumple: `estructura-regla.md:107` la cita como el caso de "y" legítimo. Validable y registrada (`commits.py`) ✅ | — | — |
| `G3 · Qué nunca se versiona` | `:28` | 🟡 | `M5` `M2` | título nominal / dueño | H-06, H-13 · solapa `11·CFG2` y `04·S4`. Validable ✅ | Título imperativo; repartir dueños | Media |
| `G4 · Trabaja en ramas, integra limpio` | `:36` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo. Validable y registrada (`rama.py`) ✅ | Añadir ejemplo | Baja |
| `G5 · No reescribas historia compartida` | `:40` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `G6 · Integración continua: el verde es automático` | `:51` | 🟡 | `M5` | unicidad | H-09 · tres sub-exigencias (pipeline · hooks complementan · verificación manual). Validable ✅ | Partir o declarar caras del mismo invariante | Baja |
| `G7 · Todo commit se muestra al usuario y se aprueba` | `:66` | ✅ | `M5` | molde / ejemplo | Cumple pese al "y" del título: no se puede aprobar lo que no se mostró | — | — |
| `G8 · El mensaje es del proyecto, no de la herramienta` | `:79` | ❌ | `M5` | título nominal / unicidad autodeclarada | H-09, H-13 · declara *"Dos consecuencias"*, y ambas se cumplen por separado | Partir: `G8` orden del cuerpo · `G9` sin firma de herramienta. Ambas ya validadas (`commits.py`) | Media |

### 5.11 · `10 · Dependencias` — 5 reglas · [`base/10-dependencias.md`](../base/10-dependencias.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `DEP1 · Agregar una dependencia es una decisión` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `DEP2 · Versiones fijadas y reproducibles` | `:16` | ✅ | `M5` | molde / ejemplo | Cumple. Validable y registrada (`dependencias.py`) ✅ | — | — |
| `DEP3 · Audita vulnerabilidades y mantén al día` | `:25` | ❌ | `M2` `M12` `M5` | dueño / ejemplo | **H-06** · duplica `04·S7`; sin ejemplo. `DEP3` es el dueño correcto | Recibir el tema tras derogar `S7`; añadir ejemplo | Media |
| `DEP4 · No versiones lo instalado` | `:29` | ✅ | `M5` | molde / ejemplo | Cumple. Validable ✅ | — | — |
| `DEP5 · Aísla la dependencia que puede cambiar` | `:38` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo | Añadir ejemplo | Baja |

### 5.12 · `11 · Configuración y entornos` — 4 reglas · [`base/11-configuracion-entornos.md`](../base/11-configuracion-entornos.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `CFG1 · La configuración vive fuera del código` | `:7` | 🟡 | `M2` `M12` | dueño | H-06 · solapa `04·S4`; la nota que la separa de `03·D4` está bien resuelta | Declarar el reparto de dueños con `04` | Media |
| `CFG2 · El entorno real no se versiona; sí una plantilla` | `:18` | 🟡 | `M2` `M12` | dueño | H-06 · solapa `09·G3` y `04·S4`. Validable ✅ | Un solo dueño; los otros enlazan | Media |
| `CFG3 · Paridad entre entornos` | `:27` | 🟡 | `M5` | unicidad / ejemplo | H-09, H-14 · tres exigencias; sin ejemplo | Partir; añadir ejemplo | Baja |
| `CFG4 · Cambios de comportamiento tras banderas` | `:31` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo, y la bandera eterna es error frecuente | Añadir ejemplo | Baja |

### 5.13 · `12 · Privacidad` — 5 reglas · [`base/12-privacidad-datos.md`](../base/12-privacidad-datos.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `PR1 · Recolecta solo lo necesario` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `PR2 · Úsalos solo para lo que se recolectaron` | `:16` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo | Añadir ejemplo | Baja |
| `PR3 · Protégelos en reposo y en tránsito` | `:20` | ❌ | `M5` `M2` | exigencia propia | **H-19** · no exige nada propio: cuatro remisiones a `04` | Reescribir con la exigencia propia del dominio de privacidad | Baja |
| `PR4 · No los expongas en logs, errores ni mensajes` | `:24` | 🟡 | `M12` | texto prestado | H-06 · reformula `05·E5`, que a su vez reformula `00·N6` — tres capas del mismo criterio | Dejar enlace + la parte propia (reportes y pantallas) | Baja |
| `PR5 · Retención y borrado` | `:33` | ✅ | `M5` | molde / ejemplo | Cumple (título nominal, H-13, es lo único) | Título imperativo | Baja |

### 5.14 · `13 · Documentación` — 16 reglas · [`base/13-documentacion/`](../base/13-documentacion/base.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `DOC1 · Persiste el trabajo de cada unidad completada` | `:7` | ❌ | `M2` `M12` | dueño | **H-06** · duplicada por `02·F6`. `DOC1` es el dueño correcto | Mantener; derogar `F6` | **Alta** |
| `DOC2 · Documenta las decisiones no obvias y su porqué` | `:16` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `DOC3 · Verifica la trazabilidad spec → implementación` | `:26` | ❌ | `M2` `M5` `M12` | dueño / texto prestado | **H-06** · duplicada por `02·F7`; su tabla se repite entera en `DOC11` | Conservar el principio; la tabla queda solo en `DOC11`; derogar `F7` | **Alta** |
| `DOC4 · Documenta lo que producción necesita` | `:43` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo | Añadir ejemplo | Baja |
| `DOC5 · Registrar señales (memoria) — *opt-in*` | `:47` | ❌ | `M3` `M13` | agnosticismo | H-07 · nombra `SQLite+FTS5`, la skill `usar-memoria` y la carpeta `memoria/`. Marca `*opt-in*` correctamente usada ✅ | Reescribir el backend en concepto; los motores concretos a capa 3 | Media |
| `DOC6 · Retro-documentar módulos existentes sin spec` | `:66` | ❌ | `M5` | tamaño / unicidad | H-15 · 19 líneas; procedimiento de 6 pasos dentro de la regla | Procedimiento a `plantillas/`; dejar 3 líneas + enlace | Media |
| `DOC7 · Referencias entre docs con historial cruzado` | `:86` | 🟡 | `M5` | tamaño | H-15 · 19 líneas. Marcada 🟡 validable pendiente en `reglas-validables.md` ✅ | Comprimir | Media |
| `DOC8 · Cierre de análisis con tabla de trazabilidad` | `:106` | 🟡 | `M5` | tamaño | H-15 · 20 líneas. Validable y registrada (`plantillas.py`) ✅ | Comprimir; formato a plantilla | Media |
| `DOC9 · Mapa de dependencias vivo` | `:127` | 🟡 | `M5` | tamaño / unicidad | H-09, H-15 · 18 líneas; dos exigencias (consultar antes · actualizar después), como dice su propio título | Partir en dos | Media |
| `DOC10 · Catálogo de reglas del proyecto sincronizado con la memoria` | `:146` | ❌ | `M1` `M7` `M3` `M12` | dependencia hacia arriba | **H-10** · cita `P28`, regla de capa 3, desde capa 2; enumeración congelada `C1-C10 · DOC1-DOC10 · F1-F5` desactualizada; solapa `01·C10` | Quitar la cita a `P28`; sustituir la enumeración por la garantía de `M4` | **Alta** |
| `DOC11 · Tabla canónica de trazabilidad (extiende DOC3)` | `:165` | ❌ | `M5` `M2` | texto prestado | **H-06** · declara `extiende DOC3` y luego repite entera su tabla; 27 líneas | Que `DOC3` conserve el principio y `DOC11` la tabla, sin solape | **Alta** |
| `DOC12 · Cada fase declara ORIGEN al abrirse` | `:193` | ❌ | `M5` `M8` `M7` | tamaño / excepción | H-02, H-12, H-15 · 41 líneas; el "cuándo NO aplica" no fija autorizador. Validable y registrada (`trazabilidad.py`) ✅ | Formato canónico a plantilla; completar excepción | Media |
| `DOC13 · Catálogo de módulos vivo` | `:235` | ❌ | `M5` `M7` | tamaño | H-02, H-15 · 38 líneas; el contenido mínimo es plantilla. Validable y registrada (`plantillas.py`) ✅ | Comprimir + enlace a plantilla | Media |
| `DOC14 · Referencias a `.md`: path relativo + route "atrapa .md"` | `:274` | ❌ | `M3` `M13` `M5` | agnosticismo / unicidad | **H-07, H-09, H-15** · 58 líneas; nombra GitHub/GitLab/VSCode/404/route y **rutas reales de un proyecto**; dos exigencias (formato del enlace · requisito de infraestructura del proyecto) | Partir; ejemplos a rutas ficticias; el route al anexo o a capa 3 | **Alta** |
| `DOC15 · Historias de Usuario desde plantilla central` | `:333` | ❌ | `M5` | unicidad | **H-09** · dos exigencias: HU desde plantilla **y** `README.md` índice en cada nivel del árbol — la segunda ya se cita como si fuera regla propia desde `DOC16` | Partir el índice a `DOC17`. Validable y registrada (`plantillas.py`) ✅ | Media |
| `DOC16 · Épicas desde plantilla central` | `:360` | 🟡 | `M5` `M7` | tamaño | H-02, H-15 · 18 líneas. Validable y registrada (`trazabilidad.py`) ✅ | Comprimir | Media |

### 5.15 · `14 · Estructura del código` — 3 reglas · [`base/14-estructura-codigo.md`](../base/14-estructura-codigo.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `EST1 · Organiza el código nuevo por módulo` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple. 🟡 validable pendiente (necesita que el proyecto declare su convención) ✅ | — | — |
| `EST2 · Nomenclatura consistente` | `:17` | 🟡 | `M5` | unicidad | H-09 · dos exigencias (convención uniforme · límites de longitud del motor). Validable parcial ✅ | Partir los límites de longitud a `EST4` | Baja |
| `EST3 · Respeta el legacy` | `:29` | 🟡 | `M2` `M12` | dueño | H-06 · tercera copia del criterio de alcance (`01·C3`, `07·Q7`) | Comprimir a enlace + la parte propia (migrar legacy es tarea acordada) | Baja |

### 5.16 · `15 · Registros inmutables` *(opt-in)* — 5 reglas · [`base/15-registros-inmutables.md`](../base/15-registros-inmutables.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `IM1 · Un registro materializado es inmutable` | `:7` | ✅ | `M5` `M2` | molde / opt-in | Cumple. El opt-in está marcado a nivel de capítulo, como pide `M2` ✅ | — | — |
| `IM2 · Estados y campos de anulación` | `:16` | 🟡 | `M5` | unicidad / ejemplo | H-09, H-14 · dos exigencias (tres estados · campos de anulación); sin ejemplo. 🟡 validable pendiente ✅ | Partir; añadir ejemplo | Baja |
| `IM3 · Anular revierte el efecto en transacción` | `:20` | ✅ | `M5` | molde | Cumple: los 4 pasos son una exigencia secuencial | — | — |
| `IM4 · Las consultas agregadoras excluyen los anulados` | `:29` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `IM5 · Permiso propio para anular` | `:38` | 🟡 | `M5` | unicidad / ejemplo | H-09, H-14 · dos exigencias (permiso separado · comportamiento de la UI); sin ejemplo | Partir la UI (es tema de `17`); añadir ejemplo | Baja |

### 5.17 · `16 · Cumplimiento y calidad` *(opt-in)* — 4 reglas · [`base/16-cumplimiento-y-calidad.md`](../base/16-cumplimiento-y-calidad.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `CQ1 · Sabe para quién construyes` | `:11` | ❌ | `M5` `M6` | encabezado `###` / opt-in | **H-03, H-08** · escondida con `###`; el capítulo se declara opt-in y su Parte A "siempre aplica". Validable y registrada (`plantillas.py`) ✅ | Subir a `##`; mover a capa 2 no opt-in | **Alta** |
| `CQ2 · Cumple por construcción y déjalo trazable` | `:20` | ❌ | `M5` `M6` | encabezado `###` / opt-in | **H-03, H-08** | Subir a `##`; capa 2 no opt-in | **Alta** |
| `CQ3 · Seguridad de software por defecto (OWASP)` | `:29` | ❌ | `M5` `M3` `M6` | encabezado `###` / agnosticismo / contradicción | **H-03, H-07, H-08** · escondida; hardcodea OWASP, que la Parte B del propio capítulo prohíbe hardcodear; sin ejemplo | Subir a `##`; reescribir en concepto y llevar OWASP a `plantillas/marco-normativo.md` | **Alta** |
| `CQ4 · Atributos de calidad como checklist (ISO/IEC 25010)` | `:33` | ❌ | `M5` `M3` `M6` `M13` | encabezado `###` / agnosticismo / título | **H-03, H-07, H-08, H-13** · escondida; hardcodea ISO/IEC 25010; título nominal | Subir a `##`; título imperativo; norma concreta a capa 3 | **Alta** |

### 5.18 · `17 · Interfaz` *(opt-in)* — 6 reglas · [`base/17-interfaz.md`](../base/17-interfaz.md)

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `I1 · Toda vista resuelve sus tres estados` | `:7` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `I2 · Feedback de validación claro` | `:20` | ✅ | `M5` | molde / ejemplo | Cumple | — | — |
| `I3 · Accesibilidad mínima` | `:29` | 🟡 | `M5` | unicidad / ejemplo | H-09, H-14 · cuatro exigencias; sin ejemplo | Partir o declarar checklist; añadir ejemplo | Baja |
| `I4 · Texto para el usuario, no jerga` | `:38` | ✅ | `M5` | molde / ejemplo | Cumple. Fija la frontera de registro que `estructura-regla.md` cruza (H-21) | — | — |
| `I5 · Consistencia con el sistema de diseño` | `:47` | 🟡 | `M5` | ejemplo | H-14 · sin ejemplo | Añadir ejemplo | Baja |
| `I6 · Adaptable` | `:51` | 🟡 | `M5` | título / ejemplo | H-13, H-14 · título de una palabra, no imperativo; sin ejemplo | Título imperativo + ejemplo | Baja |

### 5.19 · `18 · Despliegue e infraestructura` *(opt-in)* — 8 reglas · [`base/18-despliegue-e-infraestructura.md`](../base/18-despliegue-e-infraestructura.md)

> **Transversal a las 8:** ninguna tiene ejemplo INCORRECTO/CORRECTO (H-14) y ninguna está clasificada en `validadores/reglas-validables.md` (**H-05**). El capítulo tampoco tiene línea `Ver:` de cierre, a diferencia de los capítulos `03`–`17`.

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `DP1 · El despliegue es un artefacto versionado` | `:7` | 🟡 | `M5` `M9` | ejemplo / validable | H-05, H-14. La dependencia `extiende 09·G6` está declarada **en el encabezado del capítulo**, que es la forma que `M7` admite ✅ | Ejemplo + clasificar | Media |
| `DP2 · Infraestructura como código` | `:11` | 🟡 | `M5` `M9` `M13` | ejemplo / título | H-05, H-13, H-14 · título nominal | Ejemplo + título imperativo + clasificar | Media |
| `DP3 · Build una vez, promover el mismo artefacto` | `:15` | 🟡 | `M5` `M9` | ejemplo | H-05, H-14 | Ejemplo + clasificar | Media |
| `DP4 · Config por entorno, fuera del artefacto` | `:19` | 🟡 | `M5` `M9` `M12` | ejemplo / duplicación | H-05, H-14 · solapa `11·CFG1` (enlazada correctamente) | Ejemplo + clasificar | Media |
| `DP5 · Release reversible, con plan de vuelta` | `:23` | 🟡 | `M5` `M9` | ejemplo | H-05, H-14 | Ejemplo + clasificar | Media |
| `DP6 · Checklist de despliegue` | `:27` | 🟡 | `M5` `M9` | ejemplo / título | H-05, H-13, H-14 · título nominal | Ejemplo + título + clasificar (validable: completitud contra plantilla) | Media |
| `DP7 · La app expone su salud` | `:31` | 🟡 | `M5` `M9` | ejemplo | H-05, H-14 | Ejemplo + clasificar | Media |
| `DP8 · Correr contra producción lo autoriza el humano` | `:35` | ❌ | `M2` `M5` `M9` `M12` | dueño / unicidad | **H-06, H-09** · duplica `19·OB6` casi literal; dos exigencias (autorización · fuera de alcance operativo) | Conservar como dueño del tema; derogar `OB6`; partir el "fuera de alcance" | **Alta** |

### 5.20 · `19 · Observabilidad y operación` *(opt-in)* — 6 reglas · [`base/19-observabilidad-y-operacion.md`](../base/19-observabilidad-y-operacion.md)

> **Transversal a las 6:** sin ejemplos (H-14), sin clasificar en `reglas-validables.md` (**H-05**), sin línea `Ver:` de cierre.

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `OB1 · Logs estructurados y correlacionables` | `:7` | 🟡 | `M5` `M9` | ejemplo / título | H-05, H-13, H-14 · título nominal. `extiende 05` declarado en el encabezado del capítulo ✅ | Ejemplo + título + clasificar | Media |
| `OB2 · Se mide lo que le duele al usuario` | `:11` | 🟡 | `M5` `M9` | ejemplo | H-05, H-14 | Ejemplo + clasificar | Media |
| `OB3 · SLO y alertas como código, sobre síntomas` | `:15` | 🟡 | `M5` `M9` | ejemplo / unicidad | H-05, H-09, H-14 · dos exigencias (versionar SLO/alertas · alertar sobre síntomas) | Partir + ejemplo + clasificar | Media |
| `OB4 · Runbooks para lo que se opera` | `:19` | 🟡 | `M5` `M9` | ejemplo | H-05, H-14 | Ejemplo + clasificar | Media |
| `OB5 · Postmortem sin culpa` | `:23` | 🟡 | `M5` `M9` | ejemplo | H-05, H-14 (validable: completitud contra `plantillas/postmortem.md`) | Ejemplo + clasificar | Media |
| `OB6 · Operar en vivo lo hace el humano` | `:27` | ❌ | `M2` `M12` `M9` | dueño | **H-06** · duplica `18·DP8`, incluida la frase de cierre | Derogar → `18·DP8` | **Alta** |

### 5.21 · `20 · Meta-reglas` — 13 reglas · [`base/20-meta-reglas/base.md`](../base/20-meta-reglas/base.md)

> Las meta-reglas son preámbulo (`M1`: *"describe, no exige"*), así que el título nominal **no** es hallazgo. Sí lo son el ejemplo ausente, la cobertura incompleta y las contradicciones con el catálogo real.

| Regla | Ubic. | Estado | Meta-reglas | Criterios evaluados | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|---|---|
| `M1 · La jerarquía tiene cuatro niveles y un solo orden` | `:11` | ✅ | `M5` | molde / ejemplo | Cumple. Tabla + ejemplo | — | — |
| `M2 · Un tema, un capítulo, un dueño` | `:27` | 🟡 | `M5` | ejemplo / unicidad / cobertura | H-14, H-18, H-22 · sin ejemplo; cuatro criterios (fuente única · capítulo nuevo · numeración · subcarpeta); su umbral de ~15 lo incumplen 3 capítulos de forma permanente; no contempla que el preámbulo comparta el `00` | Añadir ejemplo; escribir la salida al umbral (H-18); reconocer el preámbulo | Media |
| `M3 · La base es agnóstica` | `:37` | ✅ | `M5` | molde / ejemplo | Cumple. Es la meta-regla más incumplida por el catálogo (H-07), no por defecto propio | Considerar validador de tecnologías nombradas | — |
| `M4 · Cada regla tiene un identificador único, estable y prefijado` | `:49` | 🟡 | `M5` | ejemplo / cobertura | H-14, H-16 · sin ejemplo; no contempla los 18 sub-IDs decimales que el estándar usa | Añadir ejemplo; legalizar el sub-ID con condición | Media |
| `M5 · Toda regla se escribe en el mismo formato` | `:57` | ❌ | `M2` `M5` | fuente única / cobertura | **H-02, H-21** · no enlaza a `estructura-regla.md`, que es su detalle; no contempla el bloque `Encadenamiento` (22 usos), ni el formato del encabezado de **capítulo** (`[CAPA 1]`, `[CAPA 2 · opt-in]`, `[PREÁMBULO]`), ni la congelación de `F12` | Añadir el enlace; absorber las tres formas faltantes | **Alta** |
| `M6 · Ante un conflicto, el desempate es este y en este orden` | `:79` | ✅ | `M5` | molde / ejemplo | Cumple. Los 6 pasos son una exigencia secuencial | — | — |
| `M7 · Las dependencias entre reglas se declaran, y solo hay tres` | `:93` | ❌ | `M5` `M6` | cobertura / ejemplo | **H-02** · el catálogo usa una cuarta forma 22 veces; sin ejemplo; su prohibición de ciclos no es comprobable mientras las dependencias vivan en prosa (y `F4.4`↔`F4.5` es un ciclo) | Absorber `Encadenamiento` con semántica definida | **Alta** |
| `M8 · La excepción se escribe dentro de la regla que la admite` | `:103` | ❌ | `M6` `M1` | contradicción | **H-04** · afirma que las `[BLINDADA]` no admiten excepciones, y `N1` tiene una; no distingue *excepción* de *condición de autorización*, que es lo que las cuatro blindadas realmente declaran | Añadir la distinción; renombrar en `N1` | **Alta** |
| `M9 · Toda regla declara si es validable` | `:117` | ❌ | `M9` `M10` | cobertura | **H-05** · 27 reglas (`18`, `19`, `20`) sin clasificar; el título dice "declara" y el mecanismo es un registro externo | Clasificar las 27; alinear título y cuerpo; crear `metareglas.py` | **Alta** |
| `M10 · Todo cambio de regla se versiona y se registra` | `:126` | 🟡 | `M10` `M5` | registro / ejemplo | **H-20** · el `CHANGELOG` registra el capítulo 20 como `00 · Meta-reglas`; sin ejemplo. Validable y registrada (`version.py`) ✅ | Corregir la entrada del CHANGELOG; añadir ejemplo | Media |
| `M11 · Las reglas no se borran: se derogan` | `:136` | 🟡 | `M11` | ejercicio | H-06 · nunca ejercida; 6 pares duplicados esperan derogación | Estrenarla con el par `F5`/`T5` y dejarlo como referencia | Media |
| `M12 · Antes de crear una regla, buscar` | `:146` | ✅ | `M5` | molde | Cumple. Sin ejemplo, pero la regla es evidente (`M5` no lo exige entonces) | — | — |
| `M13 · Lo que no es regla del estándar tiene su propio sitio` | `:162` | 🟡 | `M13` `M5` | cobertura / ejemplo | **H-20** · la tabla cubre 7 destinos y el repo tiene 9 carpetas más (`plantillas/`, `skills/`, `validadores/`, `memoria/`, `metricas/`, `interfaz/`, `prompts/`, `analisis/`, `anatomia/`); sin ejemplo | Ampliar la tabla con la zonificación de `anatomia/mapa-del-sitio.md` | Media |

### 5.22 · Anexo del capítulo 20 · [`estructura-regla.md`](../base/20-meta-reglas/estructura-regla.md)

| Documento | Estado | Meta-reglas | Hallazgos e incumplimientos | Recomendación | Prio. |
|---|---|---|---|---|---|
| `20 · Anatomía de una regla — el molde` | 🟡 | `M2` `M13` `M5` · Higiene | **H-21** · registro coloquial contra *"Lenguaje: imperativo, corto, técnico y sin adornos"*; `M5` no lo enlaza (fuente única a media vía); es instructivo, que `M13` manda a `CLAUDE.md`; la tabla de prefijos tiene nombres de capítulo derivados; viaja a todos los proyectos que heredan `base/` sin servirles | Enlazar desde `M5`; decidir con el usuario si se queda (y se reescribe en registro técnico) o se mueve; alinear los nombres de la tabla | Media |

---

## 6 · Inconsistencias entre reglas

Choques que `M6` clasifica como **defecto del estándar** — se resuelven en el texto, no en el desempate.

| # | Reglas que chocan | En qué chocan | Resolución propuesta |
|---|---|---|---|
| 1 | `20·M8` ↔ `00·N1` | `M8` prohíbe excepciones en `[BLINDADA]`; `N1` es blindada y tiene una | H-04 · distinguir excepción de condición de autorización |
| 2 | `16` encabezado ↔ `16` Parte A | El capítulo es `opt-in`; Parte A dice *"siempre aplica"* | H-08 · partir: `CQ1`/`CQ2` capa 2 fija, `CQ3`/`CQ4` opt-in |
| 3 | `16` Parte B ↔ `16·CQ3`/`CQ4` | Parte B prohíbe hardcodear el marco; `CQ3` y `CQ4` lo hardcodean | H-08 · reescribir en concepto |
| 4 | `20·M7` ↔ 22 reglas del catálogo | `M7` cierra en tres dependencias; el catálogo usa una cuarta | H-02 · absorber |
| 5 | `20·M5` ↔ `02·F13` | `M5` cierra en tres marcas; `F13` inventa `[GATE DE ARRANQUE · PRECONDICIÓN]` | H-11 · quitar la marca |
| 6 | `20·M5` ↔ `02·F12` | `M5` fija el molde; `F12` declara que su texto no se toca | H-11 · **decisión del usuario** |
| 7 | `20·M4` ↔ `F4.1`–`F4.5`, `F12.1`–`F12.13` | `M4` fija `<PREFIJO><n>`; 18 IDs son decimales | H-16 · legalizar con condición |
| 8 | `20·M2` (~15 reglas) ↔ `01`(18), `13`(16), `02`(19) | Umbral incumplido de forma permanente por tres capítulos | H-18 · escribir la salida en `M2` |
| 9 | `estructura-regla.md` ↔ Higiene *"lenguaje técnico"* y `17·I4` | El anexo del capítulo de estilo escribe en el registro que ese estilo reserva al usuario final | H-21 · **decisión del usuario** |
| 10 | `estructura-regla.md` (F0 corregida) ↔ `02·F0` (vigente) | Dos textos de la misma regla | H-01 · aplicar el corregido |
| 11 | `02·F4.4` ↔ `02·F4.5` | Ciclo de dependencia declarado en prosa (`M7` prohíbe ciclos) | H-02 · dirección única o fusión |
| 12 | `01·C2` ↔ `01·C11` | Verificar siempre vs. confiar en el usuario | **Ya resuelto en el texto de `C11`** — modelo de cómo se hace |
| 13 | `01·C14` → `01·C1`, `00·N3` | Cita atribuye a `C1` y `N3` textos que no tienen | H-17 · corregir las dos citas |
| 14 | `13·DOC10` → `P28` | Capa 2 depende de un ID de capa 3 (`M7`: *"nunca hacia arriba"*) | H-10 · quitar la cita |
| 15 | `02·F3` ↔ `02·F9` ↔ `00·N1` ↔ `01·C1` | El mismo criterio ("plan aprobado = ejecución continua") en cuatro sitios | H-06 · `F3` es el dueño; los otros enlazan |

---

## 7 · Qué unificar, partir, complementar o derogar

### 7.1 · Unificar (derogar una y quedarse con la otra)

| Se deroga | Queda | Versión | Motivo |
|---|---|---|---|
| `02·F5` | `08·T5` | MAYOR | Texto y ejemplo idénticos; `08` es el capítulo dueño de pruebas |
| `02·F6` | `13·DOC1` | MAYOR | Misma exigencia; `13` es el dueño de documentación |
| `02·F7` | `13·DOC3` | MAYOR | Texto y ejemplo idénticos |
| `04·S7` | `10·DEP3` | MENOR | Referencia circular sin dueño; `10` es el dueño de dependencias |
| `19·OB6` | `18·DP8` | MENOR | Texto casi literal |

> El capítulo `02` conserva su secuencia con enlaces (`ver 08·T5`, `ver 13·DOC1`, `ver 13·DOC3`) — no pierde legibilidad, pierde el texto duplicado.

### 7.2 · Repartir (sin derogar: cada una se queda con su mitad)

| Reglas | Reparto |
|---|---|
| `13·DOC3` / `13·DOC11` | `DOC3` el principio (trazabilidad antes de cerrar) · `DOC11` el formato tabular. La tabla desaparece de `DOC3` |
| `03·D1` / `06·R3` | `D1` normalización y auditoría · `R3` índices (único dueño) |
| `04·S4` / `09·G3` / `11·CFG1` / `11·CFG2` | `S4` el secreto en sí y su rotación · `CFG1` config fuera del código · `CFG2` plantilla vs. real · `G3` qué se excluye del control de versiones. Enlaces cruzados, sin repetir cuerpo |
| `01·C3` / `07·Q7` / `14·EST3` | `C3` el principio de alcance · `Q7` la aplicación al refactor · `EST3` la aplicación al legacy. Las dos últimas comprimidas a 2 líneas + enlace |
| `00·N6` / `04·S6` / `05·E5` / `12·PR4` | `N6` el principio blindado · las otras tres solo su aplicación al dominio, sin reformular |
| `02·F3` / `02·F9` / `00·N1` / `01·C1` | `F3` el dueño · `F9` solo la parte propia (no subdividir post-aprobación) · `N1` y `C1` enlazan |

### 7.3 · Partir (una regla → dos o más; la original conserva su ID por `M4`)

| Regla | Se parte en | Prio. |
|---|---|---|
| `02·F4.5` | ejecución literal de CA · descubrimientos se proponen *(ya se autodeclara doble)* | Alta |
| `04·S11` | autorización por operación · el borrado lógico cuenta como escritura *(ya se autodeclara doble)* | Alta |
| `08·T7` | derivar los casos · triangular el resultado esperado *(ya se autodeclara doble)* | Media |
| `09·G8` | orden del cuerpo del commit · sin firma de herramienta *(ya se autodeclara doble)* | Media |
| `03·D1` | normalizar · auditar · integridad en BD | Alta |
| `02·F4` | aprobación explícita del plan · plan de pruebas · verificar la cadena previa | Alta |
| `02·F4.3` | línea base verificada · los 5 componentes · matriz de dependencias · proporcionalidad | Alta |
| `13·DOC14` | formato del enlace `.md` · requisito de render local del proyecto | Alta |
| `13·DOC15` | HU desde plantilla · `README.md` índice por nivel del árbol | Media |
| `00·N1`, `00·N4`, `00·N6` | ver §5.1 | Media |
| `04·S5` | CSRF · sesiones · transporte · credenciales | Media |
| `03·D6` | idempotencia · actualización concurrente · unicidad en BD | Media |
| `13·DOC9` | consultar el mapa antes · actualizarlo después | Media |
| `19·OB3` | SLO/alertas versionadas · alertar sobre síntomas | Media |
| `01·C17` | confirmar entendimiento · qué cuenta como aprobación | Media |

### 7.4 · Complementar (falta una pieza del molde)

| Qué falta | Reglas | Prio. |
|---|---|---|
| Ejemplo INCORRECTO/CORRECTO | los 8 `DP` · los 6 `OB` · `D2` `S5` `S7` `T1` `T4` `Q6` `G4` `DEP3` `DEP5` `CFG3` `CFG4` `PR2` `DOC4` `IM2` `IM5` `I3` `I5` `I6` `C6` `C8` · `M2` `M4` `M7` `M9` `M10` `M13` | Media |
| Quién autoriza la excepción | `F0` `F2` `F4.2` `F11` `D1` `D4` `D5` `D7` `D8` `C1` `C17` `T1` | Media |
| Clasificación de validable | los 8 `DP` · los 6 `OB` · las 13 `M` | **Alta** |
| Enlace desde `M5` a `estructura-regla.md` | `M5` | **Alta** |
| Encabezado de regla en la fuente única | `reglas/F12-…` · `reglas/F13-…` | **Alta** |
| Título imperativo | `F0` `D6` `S4` `S5` `G3` `PR5` `CQ4` `DOC5` `DP2` `DP6` `OB1` `I6` `F12` `F13` | Media |

### 7.5 · Eliminar

**Ninguna.** `M11` es categórica: las reglas no se borran. Todo lo que sobra se deroga con marca y su texto se conserva debajo, porque las specs, commits y fases cerradas las citan por ID.

Sí se **borra texto dentro de reglas**: las repeticiones internas (el trozo 5 de `F0`), los cuerpos duplicados (la tabla de `DOC3` que repite `DOC11`), y las explicaciones que pertenecen a otro capítulo (las definiciones de épica/módulo/fase dentro de `F0`).

---

## 8 · Plan de trabajo

Cinco olas. Cada una es un bloque de cambios con su versión, y al cerrarla se relee el capítulo completo tocado — no solo la regla nueva (Higiene del conjunto: *"Las contradicciones aparecen al leer seguido, no al escribir"*).

### Ola 1 — Arreglar las meta-reglas primero · `1.3.1` **PARCHE** + `1.4.0` **MENOR**

Sin esto, cada corrección posterior se hace contra una norma que se contradice.

| # | Acción | Hallazgo | Meta-regla |
|---|---|---|---|
| 1 | `M8` distingue *excepción* de *condición de autorización*; `N1` renombra su "Excepción" | H-04 | `M8` `M6` |
| 2 | `M7` absorbe `**Encadenamiento:**` como cuarta forma, con semántica y posición definidas | H-02 | `M7` |
| 3 | `M5` enlaza a `estructura-regla.md` y absorbe: formato del encabezado de capítulo, y la figura de texto congelado (o se decide `F12` por la otra vía) | H-11, H-21 | `M5` `M2` |
| 4 | `M4` legaliza el sub-ID `<PREFIJO><n>.<m>` con la condición "no se cumple sin la parte" | H-16 | `M4` |
| 5 | `M2` escribe la salida al umbral de ~15 reglas y reconoce el preámbulo sin número | H-18, H-22 | `M2` |
| 6 | `M13` amplía la tabla con las 9 carpetas del repo, agrupadas por zona | H-20 | `M13` |
| 7 | Corregir en `CHANGELOG.md` la entrada `00 · Meta-reglas` → `20 · Meta-reglas` | H-20 | `M10` |
| 8 | Añadir ejemplo a `M2`, `M4`, `M7`, `M9`, `M10`, `M13` | H-14 | `M5` |

### Ola 2 — Cerrar contradicciones y reglas escondidas · `1.4.0` **MENOR**

| # | Acción | Hallazgo | Prio. |
|---|---|---|---|
| 9 | `CQ1`–`CQ4` de `###` a `##` | H-03 | Alta |
| 10 | Partir el capítulo 16: `CQ1`/`CQ2` capa 2 fija · `CQ3`/`CQ4` opt-in y en concepto | H-08 | Alta |
| 11 | Aplicar a `F0` el texto corregido de `estructura-regla.md`; reubicar sus 5 trozos sobrantes | H-01 | Alta |
| 12 | Quitar la marca inventada de `F13`; añadir encabezado de regla en su fuente única | H-11 | Alta |
| 13 | Corregir las dos citas mal atribuidas de `C14` | H-17 | Alta |
| 14 | Quitar de `DOC10` la cita a `P28` y la enumeración congelada | H-10 | Alta |
| 15 | Preguntar al usuario la vía para `F12` (molde sin tocar texto vs. legalizar la congelación) y la de `estructura-regla.md` (se queda y se reescribe vs. se mueve) | H-11, H-21 | Alta |

### Ola 3 — Consolidar duplicados · `2.0.0` **MAYOR**

Es MAYOR porque un proyecto al día que cite `F5`, `F6` o `F7` tiene que empezar a citar `T5`, `DOC1` y `DOC3`. Estrena `M11`.

| # | Acción | Hallazgo |
|---|---|---|
| 16 | Derogar `F5` → `08·T5`, trasladando el alcance quirúrgico de la corrida | H-06 |
| 17 | Derogar `F6` → `13·DOC1` · `F7` → `13·DOC3` | H-06 |
| 18 | Derogar `S7` → `10·DEP3` · `OB6` → `18·DP8` | H-06 |
| 19 | Repartir `DOC3`/`DOC11` (la tabla queda solo en `DOC11`) | H-06 |
| 20 | Repartir `D1`/`R3`, el bloque de secretos y el bloque de alcance (§7.2) | H-06 |
| 21 | Actualizar todas las citas a los IDs derogados en `base/`, `plantillas/`, `skills/` y `validadores/` | Higiene |

### Ola 4 — Agnosticismo y partición · `2.1.0` **MENOR**

| # | Acción | Hallazgo |
|---|---|---|
| 22 | Reescribir en concepto `DOC14`, `S11`, `D8`, `DOC5`, `C10`, `C15`, `C16`; ejemplos a rutas y pseudocódigo ficticios | H-07 |
| 23 | Partir las 4 reglas que se autodeclaran múltiples: `F4.5`, `S11`, `T7`, `G8` | H-09 |
| 24 | Partir `D1`, `F4`, `F4.3`, `DOC14`, `DOC15` | H-09 |
| 25 | Abrir subcarpeta/anexo para `F4.3`, `D7`, `DOC12`, `DOC13` y comprimir el cuerpo a 1–4 líneas | H-15 |
| 26 | Completar las 12 excepciones sin autorizador, tomando `S9` y `S10` como modelo | H-12 |
| 27 | Títulos imperativos en las 14 reglas de H-13 | H-13 |

### Ola 5 — Validación automática · `2.2.0` **MENOR**

| # | Acción | Hallazgo |
|---|---|---|
| 28 | Clasificar en `reglas-validables.md` las 27 reglas de `18`, `19` y `20` | H-05 |
| 29 | Crear `validadores/metareglas.py` — valida `M3`, `M4`, `M5`, `M7`, `M9` **en seco** sobre `base/`: encabezado `##`, marca de la lista cerrada, ID único con prefijo del capítulo, presencia de ejemplo, tamaño del cuerpo, tecnologías nombradas, citas que resuelven, ausencia de ciclos, y toda regla clasificada | H-03, H-05, H-06, H-07, H-09, H-11, H-13, H-14, H-16 |
| 30 | Normalizar las citas a `` `NN·ID` `` y activar `enlaces.py` sobre `base/` en el hook de sesión | H-17 |
| 31 | Añadir ejemplo a las reglas de §7.4 | H-14 |
| 32 | Añadir a `reglas-validables.md` la fecha de la nueva foto y el conteo actualizado | `M9` `M10` |

> El punto 29 es el que cambia el régimen: mientras las meta-reglas solo las verifique una lectura, este informe habrá que repetirlo a mano. Con `metareglas.py` en el hook, nueve de los veintidós hallazgos dejan de poder repetirse.

---

## 9 · Conclusión

**El estándar está bien diseñado y desigualmente aplicado.** Las 13 meta-reglas cubren lo que tienen que cubrir —jerarquía, dueño único, agnosticismo, ID estable, formato, desempate, dependencias, excepciones, validación, versionado, derogación, búsqueda previa y enrutamiento— y el procedimiento de alta de regla no tiene huecos. El problema es de fecha: el capítulo 20 nació en la versión 1.3.0 y las 157 reglas anteriores nunca se revisaron contra él.

De los 22 hallazgos, **ninguno pone en duda qué exige el estándar**. Todos son de forma: dónde está escrito, cuántas veces, con qué molde, si un programa puede comprobarlo. Eso es una buena noticia — la corrección es mecánica y no reabre decisiones.

**Dos hallazgos merecen atención especial por lo que revelan del método**, no por su tamaño:

- `estructura-regla.md` diseca `F0`, publica la versión corregida y nadie la aplicó (**H-01**).
- `estructura-regla.md` usa `[GATE DE ARRANQUE]` de `F13` como su ejemplo de marca inventada, y `F13` sigue con la marca (**H-11**).

En los dos casos el diagnóstico estaba escrito, con la solución al lado, y el paso que faltó fue aplicarlo. Eso es exactamente lo que `M9` previene cuando dice: *"Una regla validable que nadie valida es una regla que no se cumple."* La conclusión operativa del informe es esa: **la Ola 5 (validador `metareglas.py`) importa más que las cuatro anteriores**, porque sin ella este análisis caduca en la próxima tanda de reglas.

**Dos decisiones son del usuario y no se tocan hasta que responda:** la vía para `F12` (texto congelado) y el destino de `estructura-regla.md` (registro y ubicación). Todo lo demás de la Ola 1 y 2 puede ejecutarse.

---

> **Cómo se mantiene este informe.** Es una fotografía del **2026-08-07** sobre `VERSION 1.3.0`. Cada ola cerrada actualiza la tabla de §1 y marca las filas resueltas en §5. Al terminar la Ola 5, `metareglas.py` reemplaza la parte mecánica de este documento y aquí queda solo lo que exige criterio.
