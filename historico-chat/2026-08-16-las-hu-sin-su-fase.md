<!-- sesion: 61d99512-c0ef-42f0-9b03-04b651c50149 -->
<!-- nombre: preguntado -->

# 2026-08-16 — Las hu sin su fase

## Conversación

### 1 · Usuario — 2026-08-16 21:06:20
> Analiza las HU e identifica aquellas a las que les falte algún elemento, información o requisito. Por cada HU que tenga algo pendiente por completar, crea un pendiente específico en la carpeta pendientes, indicando claramente qué le falta, qué se debe completar y a qué HU corresponde.
>
> primero deme ejmplo de cómo lo va hacer

### 2 · Usuario — 2026-08-16 21:08:53
> para qué lee la memoria para eso le di una instrucción

**Agente** — 2026-08-16 21:09:30
<!-- agente: f7b74805-8681-4420-a36f-8bba4070642d -->

Tiene razón. Va el ejemplo.

## Cómo lo voy a hacer

**1 · La rejilla de comprobación** — sale de [plantillas/ciclo-vida-proyectos/04-HU.md](plantillas/ciclo-vida-proyectos/04-HU.md) y de las reglas del estándar, no de mi criterio:

| # | Qué se mira | De dónde sale la exigencia |
|---|---|---|
| 1 | Marcadores `«…»` sin llenar y notas `>` de la plantilla sin borrar | `validadores/plantilla` (FALLA / AVISO) |
| 2 | Secciones 1–13 presentes, o ausentes con motivo | plantilla HU §1–13 |
| 3 | Cada CA con su bloque `Cómo validarlo` y su «Aprobado cuando» | plantilla §4 |
| 4 | CA de error y de caso borde, no solo camino feliz | plantilla §4 |
| 5 | RNF con identificador `RNF-0N` | plantilla §5 («sin número no se puede citar desde el plan ni desde las pruebas») |
| 6 | §8 con al menos una fase, enlazada en los dos lados | `02·F12.2`, `02·F12.1` |
| 7 | Estado de §1 coherente con lo que de verdad hay construido | `13·DOC` / el caso del pendiente 38 |
| 8 | Contradicciones internas (fuera de alcance vs. tareas, DoD vs. CA) | lectura |
| 9 | Reglas de negocio sin de-dónde-bajan | pendientes [43](pendientes/hecho/el-origen-de-la-regla-de-negocio.md) y [47](pendientes/47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md) |

Lo mecánico (1 y 2) lo corro con `validar.py plantilla` sobre las 66 HU. Lo demás es lectura: el validador compara títulos literales, así que un `CA-01 — Encuentra lo que…` le sale como «sección ausente» aunque esté bien. Eso ya lo comprobé.

**2 · Una pasada por épica**, EP-001 a EP-007, dejando la lista de huecos por HU antes de escribir nada.

**3 · Un archivo de pendiente por HU con huecos**, numerado desde el 48, con su línea en [pendientes/README.md](pendientes/README.md) y su `P`.

---

## El ejemplo, sobre una HU real

[EP-006 · HU-004 — Buscar por significado](documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md). Esto es lo que sale:

| # | Hueco | Evidencia |
|---|---|---|
| A | **Dice `Backlog` y está construida y cerrada.** §1 Estado = Backlog, §8 «Todavía no se descompuso en fases», DoD todo sin marcar, la carpeta no tiene fase | [hecho/memoria-semantica.md](pendientes/hecho/memoria-semantica.md) la cierra el 2026-08-06: `memoria/semantica.py`, `search` híbrida, 16 pruebas verdes |
| B | **Sin fase** (`02·F12.2` pide al menos una). Como el código existe, lo que falta es retrodocumentarla | igual que el [38](pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md) |
| C | **Los RNF no tienen ID.** §5 es `\| Categoría \| Requisito \|`; la plantilla exige `RNF-01`… | plantilla §5, línea 131 |
| D | **§3.3 se contradice con §7.** Fuera de alcance: «Elegir el modelo concreto en esta historia». §7 tarea: «Elegir y declarar el modelo local» | y de hecho lo eligió el cierre: `model2vec`/`potion-base-8M` |
| E | **Solo 2 CA, ninguno de caso borde** | plantilla §4 pide camino feliz, error y borde |
| F | **Las 5 reglas de negocio no dicen de dónde bajan** | mismo defecto del [47](pendientes/47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md) |

Y el archivo que escribiría — `pendientes/48-la-hu-de-la-busqueda-por-significado-esta-construida-y-dice-backlog.md`:

```markdown
# Pendiente · La HU de la búsqueda por significado está construida y dice «Backlog»

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **HU** | [EP-006 · HU-004 — Buscar por significado](../documentacion/…/HU-004-busqueda-por-significado.md) |
| **Qué le falta** | seis puntos: A retrodocumentar la fase · B poner el estado real · C numerar los RNF · D resolver la contradicción §3.3/§7 · E el CA de borde · F el origen de las reglas de negocio |

## El problema
El pendiente 05 cerró el 2026-08-06 … la HU nunca se enteró.

## Por qué importa
[qué se pierde: la trazabilidad hacia abajo de `02·F12`, y el arranque cuenta una HU en Backlog que no lo está]

## Qué falta          ← punto por punto, con lo que hay que escribir en cada §
## Cómo se sabe que cerró
```

---

## Dos cosas que decidir antes de arrancar

**1 · Granularidad.** Usted pidió un pendiente por HU. Con 66 HU eso puede dejar 30–50 archivos nuevos en un backlog que hoy tiene 30 abiertos.

| | Qué deja |
|---|---|
| **A · Uno por HU**, como pidió | Cada HU tiene su ficha; el backlog crece a ~70 y su README se vuelve inmanejable |
| **B · Uno por HU, pero solo las que tengan huecos de fondo** (A, B, D del ejemplo), y **uno transversal** para lo mecánico y repetido (C, E, F) | Menos archivos, y lo mecánico se arregla de una pasada en vez de 40 veces |
| **C · Uno por épica**, siete archivos con el detalle por HU adentro | Barato de leer, pero cada uno mezcla cosas que se cierran por separado |

**Recomiendo la B**: los puntos C, E y F del ejemplo se van a repetir en casi todas las HU, y 40 pendientes que dicen lo mismo no se ejecutan nunca.

**2 · El inventario primero, o los archivos directo.** Puedo entregarle la tabla de las 66 HU con sus huecos para que usted vea el volumen y recién ahí escribir los pendientes. Recomiendo esto: sin ver la tabla, la decisión 1 se toma a ciegas.

Dígame y arranco.

### 3 · Usuario — 2026-08-16 21:10:36
> es que no tenga HU-fase-archivos

### 4 · Usuario — 2026-08-16 21:11:27
> deme el ejemplo

**Agente** — 2026-08-16 21:11:54
<!-- agente: 78f14e91-21d0-4d38-8521-0f1236deead3 -->

El criterio queda en uno solo: **la HU no tiene su fase, o la fase no tiene sus archivos.** Ya conté: de las 66 HU, **51 no tienen ni una carpeta de fase**; 15 sí.

Este sería el archivo, para una de esas 51 — `pendientes/48-la-hu-de-la-busqueda-por-significado-no-tiene-fase.md`:

```markdown
# Pendiente · La HU de la búsqueda por significado no tiene fase

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **HU** | [EP-006 · HU-004 — Buscar por significado](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md) |
| **Qué le falta** | la fase: la carpeta no tiene ninguna, y por lo tanto no hay `plan_trabajo`, `plan_pruebas`, `resultado_pruebas`, `estado-fase` ni `funcionalidad_implementada` |
| **Qué se debe completar** | retrodocumentar una fase `A-EP-006-HU-004-<slug>` con sus cinco documentos, porque el código ya existe |

## El problema

La carpeta de la HU tiene dos archivos —la HU y su `README`— y ninguna carpeta de fase.
Su §8 dice «Todavía no se descompuso en fases» y su §1 dice `Estado: Backlog`.

Pero está construida. El pendiente 05 cerró el 2026-08-06
([hecho/memoria-semantica.md](hecho/memoria-semantica.md)): `memoria/semantica.py`,
`search` híbrida en `memoria.py`, `requirements-semantica.txt` y 16 pruebas verdes.

O sea que no falta trabajo: falta el eslabón que dice **con qué plan se hizo,
con qué casos se probó y qué salió**.

## Por qué importa

1. **`02·F12.2` pide al menos una fase por HU**, y esta no la tiene.
2. **Nadie puede decir qué CA quedó cumplido.** El CA-01 y el CA-02 no tienen
   dónde estar marcados: no hay `resultado_pruebas` que los nombre.
3. **Es el mismo hueco del [38](hecho/el-validador-de-la-f22-tiene-su-fase.md)**, y allá
   se supo algo: al trabajo sin cadena no le faltaba documentación —la tenía—
   sino prueba. Acá tiene pruebas escritas, pero no un plan que las declare
   contra los CA.

## Qué falta

Una fase de retrodocumentación, sin tocar una línea de producción:

1. Crear `A-EP-006-HU-004-<slug>/` con sus cinco documentos.
2. `plan_trabajo.md` — ORIGEN = pendiente 05; qué archivos se tocaron; qué CA cubre.
3. `plan_pruebas.md` — los casos que ya corren en `memoria/`, atados a CA-01 y CA-02.
4. `resultado_pruebas.md` — qué se ejecutó y con qué resultado.
5. `funcionalidad_implementada.md` + `estado-fase.md` con el veredicto.
6. Escribir el enlace **en los dos lados**: la §8 de la HU nombra la fase, y
   la HU pasa de `Backlog` al estado real.

## Cómo se sabe que cerró

`python validadores/validar.py fases` y `… trazabilidad` no reportan nada sobre
esta HU, y su §8 nombra una fase que existe con sus cinco documentos.
```

Eso, por cada HU que le falte la cadena. Antes de escribir 51 archivos hay dos cosas que decidir:

| | |
|---|---|
| **A** | Un pendiente por HU — 51 archivos nuevos, numerados 48 en adelante |
| **B** | Un pendiente por épica — 7 archivos, con la lista de sus HU adentro |
| **C** | Uno solo, «las 51 HU sin fase», con la tabla completa |

Recomiendo **B**: las HU de una misma épica se retrodocumentan juntas o no se retrodocumenta ninguna, y 51 archivos que dicen lo mismo dejan el backlog ilegible. Pero si quiere ficha por HU, es la A y la escribo igual.

¿Con cuál sigo?

*(Aparte: esta sesión se guarda como `2026-08-16-sesion-8.md`, que no dice de qué trata. Propongo `2026-08-16-las-hu-sin-fase.md` — analizar qué HU están incompletas y abrir sus pendientes. ¿Va?)*

### 5 · Usuario — 2026-08-16 21:13:07
> la B y como quedar entonces la redacción?

### 6 · Usuario — 2026-08-16 21:13:29
> responda la preguta

**Agente** — 2026-08-16 21:13:55
<!-- agente: bdf81b9f-3dfa-44ea-a770-09eabf6b9f7a -->

Así — un archivo por épica, `pendientes/48-las-hu-de-la-memoria-no-tienen-fase.md`:

```markdown
# Pendiente · Las 7 HU de la memoria no tienen fase

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **Épica** | [EP-006 — Memoria de lo aprendido](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md) |
| **Qué le falta** | ninguna de sus 7 HU tiene carpeta de fase, así que ninguna tiene `plan_trabajo`, `plan_pruebas`, `resultado_pruebas`, `estado-fase` ni `funcionalidad_implementada` |
| **Qué se debe completar** | una fase por HU, retrodocumentada: el código ya existe |
| **Hermano de** | un pendiente igual por cada épica — el 49 al 54 |

## El problema

Las siete HU dicen `Estado: Backlog` y su §8 dice que todavía no se
descompusieron en fases. Pero la memoria está construida y cerrada: el
pendiente [05](hecho/memoria-semantica.md) el 2026-08-06, el
[02](hecho/vigencia-y-poda-de-memoria.md) el mismo día.

No falta trabajo. Falta el eslabón que dice con qué plan se hizo, con qué
casos se probó y qué salió.

| HU | Estado que declara | Fase | Qué falta |
|---|---|---|---|
| [HU-001 Qué se guarda](…) | Backlog | ninguna | los 5 documentos |
| [HU-002 Guardar en el repositorio](…) | Backlog | ninguna | los 5 documentos |
| [HU-003 Búsqueda por palabra](…) | Backlog | ninguna | los 5 documentos |
| [HU-004 Búsqueda por significado](…) | Backlog | ninguna | los 5 documentos · construida en el [05](hecho/memoria-semantica.md) |
| [HU-005 Aprendizaje y preferencia](…) | Backlog | ninguna | los 5 documentos |
| [HU-006 Sacar del almacén local](…) | Backlog | ninguna | los 5 documentos |
| [HU-007 Marcar lo que dejó de aplicar](…) | Backlog | ninguna | los 5 documentos |

## Por qué importa

1. **`02·F12.2` pide al menos una fase por HU**, y no hay ninguna en toda la épica.
2. **Ningún CA tiene dónde estar marcado.** Sin `resultado_pruebas` nadie puede
   decir cuál quedó cumplido — el trabajo está hecho y no hay cómo probarlo.
3. **Es el hueco del [38](hecho/el-validador-de-la-f22-tiene-su-fase.md)**, repetido
   siete veces: allá se supo que al trabajo sin cadena no le falta documentación,
   le falta prueba atada a su criterio.

## Qué falta

Por cada HU de la tabla, una fase de retrodocumentación sin tocar producción:

1. `A-EP-006-HU-00N-<slug>/` con sus cinco documentos.
2. `plan_trabajo.md` — ORIGEN, archivos tocados, qué CA cubre.
3. `plan_pruebas.md` — los casos que ya corren, atados a los CA.
4. `resultado_pruebas.md` — qué se ejecutó y qué salió.
5. `funcionalidad_implementada.md` y `estado-fase.md` con el veredicto.
6. El enlace en los dos lados, y el `Estado` de la §1 puesto en lo real.

**Se puede partir por HU**, y conviene: son siete cierres distintos. Pero se
abren juntas porque comparten el mismo código y las mismas pruebas.

## Cómo se sabe que cerró

`validar.py fases` y `validar.py trazabilidad` no reportan nada de EP-006, y la
§8 de cada HU nombra una fase que existe con sus cinco documentos.
```

Y en [pendientes/README.md](pendientes/README.md), una sección nueva con las siete líneas:

```markdown
### Las HU que se quedaron sin cadena (48–54)

De las 66 HU del repo, 51 no tienen ni una carpeta de fase. `02·F12.2` pide al
menos una. Un pendiente por épica, porque las HU de una misma épica se
retrodocumentan juntas o no se retrodocumenta ninguna.

| # | P | Pendiente | Cuántas HU sin fase |
|---|---|---|---|
| 48 | **P1** | Las HU de la memoria no tienen fase (EP-006) | 7 de 7 |
| 49 | **P1** | … (EP-005) | 8 de 10 |
| … | | | |
```

La `P` la pondría en **P1** para las épicas que ya están construidas —el documento afirma `Backlog` sobre algo que existe, que es la definición de P1— y en **P3** para las que de verdad no se han hecho, porque ahí no hay nada que retrodocumentar todavía.

¿Arranco con los siete archivos y su sección del README?

### 7 · Usuario — 2026-08-16 21:15:50
> no se riegue con tanta explicación es una tabla sesilla donde diga a qué HU está incompleta ,  que le hace falta y un campo para marcarla como completo o incompleto por cada uno de los faltantes

**Agente** — 2026-08-16 21:16:02
<!-- agente: 2e744c06-393c-4d89-8b81-d90a30e911d5 -->

```markdown
# Pendiente · HU incompletas de EP-006 — Memoria de lo aprendido

**Estado:** abierto · anotado 2026-08-16.

| HU | Qué le falta | ¿Completo? |
|---|---|:--:|
| HU-001 Qué se guarda | Carpeta de fase | ☐ |
| HU-001 Qué se guarda | `plan_trabajo.md` | ☐ |
| HU-001 Qué se guarda | `plan_pruebas.md` | ☐ |
| HU-001 Qué se guarda | `resultado_pruebas.md` | ☐ |
| HU-001 Qué se guarda | `estado-fase.md` | ☐ |
| HU-001 Qué se guarda | `funcionalidad_implementada.md` | ☐ |
| HU-002 Guardar en el repositorio | Carpeta de fase | ☐ |
| HU-002 Guardar en el repositorio | `plan_trabajo.md` | ☐ |
| … | … | ☐ |
```

Marcado: `☐` incompleto, `☑` completo.

Si prefiere una sola fila por HU y una columna por documento, queda más corta:

| HU | Fase | plan_trabajo | plan_pruebas | resultado_pruebas | estado-fase | func_implementada |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| HU-001 Qué se guarda | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| HU-002 Guardar en el repositorio | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| HU-003 Búsqueda por palabra | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

¿Cuál de las dos, y arranco con las siete épicas?

### 8 · Usuario — 2026-08-16 21:18:40
> me gusta la segunda deme el .md con esa estructura y el texto para que se cumpla el llenado de esa tabla

**Agente** — 2026-08-16 21:19:20
<!-- agente: a30cbd85-4228-4538-a305-a1390f40bbab -->

[pendientes/48-hu-incompletas-ep-006-memoria.md](pendientes/48-hu-incompletas-ep-006-memoria.md) — es el modelo, con EP-006 llena de verdad: sus 7 HU no tienen ni una carpeta de fase, y las 7 dicen `Backlog`.

Lo que hace cumplir el llenado son las seis líneas de **«Cómo se llena la tabla»**: una fila a la vez, orden fijo de columnas, la casilla se marca solo si el archivo existe, y al cerrar la fila se corrige la §8 y el Estado de la HU.

Si va así, replico las otras seis épicas (49–54) y agrego la sección al [README](pendientes/README.md). Falta contar los faltantes de las 15 HU que sí tienen fase — ahí la tabla no va toda en ☐.

### 9 · Usuario — 2026-08-16 21:21:55
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\pendientes\48-hu-incompletas-ep-006-memoria.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> solo esas HU está incompletas?

**Agente** — 2026-08-16 21:22:55
<!-- agente: 1356dc3b-b11e-4ddb-9fec-2b3f48de6f9c -->

Falta la otra mitad: las 15 que sí tienen fase. Déjeme contarlas.

No. EP-006 es solo una de siete. El conteo completo:

| Épica | HU | Sin fase | Fase incompleta | **Incompletas** |
|---|--:|--:|--:|--:|
| EP-001 Cuerpo de reglas | 10 | 7 | 3 | **10** |
| EP-002 Versionado y adopción | 6 | 6 | 0 | **6** |
| EP-003 Documentos modelo | 10 | 6 | 0 | **6** |
| EP-004 Comprobación automática | 16 | 11 | 1 | **12** |
| EP-005 Automatismos | 10 | 8 | 0 | **8** |
| EP-006 Memoria | 7 | 7 | 0 | **7** |
| EP-007 Instalación | 7 | 4 | 0 | **4** |
| | **66** | **49** | **4** | **53** |

**53 de 66 HU incompletas.** 13 completas.

Las 4 que tienen fase pero le falta documento:

| Fase | Qué le falta |
|---|---|
| `A-EP-001-HU-001-molde-de-regla` | `funcionalidad_implementada` |
| `A-EP-001-HU-002-capas-y-precedencia` | `funcionalidad_implementada` |
| `A-EP-001-HU-009-clasificar-las-que-faltan` | `resultado_pruebas`, `estado-fase`, `funcionalidad_implementada` |
| `A-EP-004-HU-010-declaracion-y-comprobacion` | `funcionalidad_implementada` |

Dos cosas que vi al contar:

- **Los números se están moviendo mientras cuento.** `A-EP-001-HU-009` y `A-EP-004-HU-014` no existían en mi primer conteo de hace unos minutos y ahora sí — están fechadas 21:20 y 21:11. Hay otra sesión trabajando en el mismo repo. Cuando escriba las siete tablas vuelvo a contar.
- `HU-014-un-solo-veredicto-por-fase` no tiene `README.md`; todas las demás sí.

¿Escribo las siete tablas con estos números?

### 10 · Usuario — 2026-08-16 21:23:50
> complete la tabla

### 11 · Usuario — 2026-08-16 21:27:11
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\pendientes\48-hu-incompletas-ep-006-memoria.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> un solo archivo para qué tantos con solo leer esa tabla ya se saben cuales están incompletas

**Agente** — 2026-08-16 21:29:44
<!-- agente: f0463e60-c8d2-4104-b305-0737e4e521bd -->

Con razón. Una sola.

El `48` que había borrado reapareció, y el `52` lo acaba de tomar la otra sesión. Uso el `48` y borro mi borrador.

Listo — un solo archivo: [pendientes/48-las-hu-no-tienen-su-fase.md](pendientes/48-las-hu-no-tienen-su-fase.md), con las 66 HU en una tabla y su línea en el [README](pendientes/README.md).

**52 de 66 incompletas:** 49 sin ninguna fase, 3 con la fase a medias, 14 completas. Los números cambiaron dos veces mientras contaba —la otra sesión cerró `A-EP-001-HU-009` y tomó el número 52 del backlog—, así que la tabla es la foto de ahora.

Falta el resumen de la sesión, que el estándar exige. Lo escribo ya.

Queda:

- [pendientes/48-las-hu-no-tienen-su-fase.md](pendientes/48-las-hu-no-tienen-su-fase.md) — las 66 HU en una tabla, casilla por documento.
- Su línea en [pendientes/README.md](pendientes/README.md), con `P1`.
- [historico-chat/resumenes/2026-08-16/sesion-8.md](historico-chat/resumenes/2026-08-16/sesion-8.md) — dos hallazgos: la cuenta, y que otra sesión está tomando números del backlog al mismo tiempo.

Sin commit, esperando que lo lea. Dos cosas sin cerrar: las dos HU que dispararon los hallazgos no están escritas en EP-004, y la sesión sigue guardándose como `2026-08-16-sesion-8.md` — propongo renombrarla a `2026-08-16-las-hu-sin-su-fase.md`.

### 12 · Usuario — 2026-08-16 21:38:17
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\pendientes\48-las-hu-no-tienen-su-fase.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> acabo de modificar el encabezado del documento para que lo llene y se vaya llenando a me dida que se vayan completando

**Agente** — 2026-08-16 21:39:17
<!-- agente: c8532fd8-a867-4ed3-b2ab-056e44d475df -->

Encabezado lleno: **66 HU · 14 completas · 52 incompletas** (49 sin ninguna fase, 3 a medias), con la fecha del conteo.

Le cambié una cosa de lo que escribió: `Incompletas-Completas=0` nunca da cero —hoy 52−14=38, y al terminar sería 0−66=−66—, así que quedó **`Incompletas = 0`**.

Y agregué la regla que hace que se vaya llenando: al marcar la última casilla de una fila, Completas sube uno e Incompletas baja uno **en la misma edición**; si se pierde la cuenta, se recuenta mirando la tabla — fila con seis ☑ es completa.

También dejé dicho en el resumen que la sesión no se puede cerrar todavía: faltan las dos HU disparadas en EP-004 y su aprobación.

### 13 · Usuario — 2026-08-16 21:45:04
> crear este: 48-las-hu-no-tienen-su-fase.md archivo también como una plantilla:inventario-hu.md

**Agente** — 2026-08-16 21:46:51
<!-- agente: 146a8427-f5a6-4e9b-9bbd-7cc08e48ce2e -->

Hecho. Cuatro cosas:

- [plantillas/inventario-hu.md](plantillas/inventario-hu.md) — el molde: la tabla de meta con los contadores, la tabla de una fila por HU y una casilla por documento, las seis reglas de llenado, y un apartado nuevo que separa **construcción** de **retrodocumentación** (que es casi todo lo que falta acá).
- [anatomia/mapa-del-sitio.md](anatomia/mapa-del-sitio.md) — el árbol pasa de 23 a 24 moldes, con su línea.
- [CHANGELOG.md](CHANGELOG.md) + [VERSION](VERSION) → **23.2.0**, MENOR: es aditivo, no cambia qué se exige.

`validar.py estandar` sale con 3 fallas, todas de antes y ninguna de estos archivos: los dos índices que el pendiente [46](pendientes/46-el-registro-de-version-dice-que-falta-escribirse.md) ya deja anotados, y un enlace roto del 44.

Dos avisos míos: la otra sesión publicó la **23.1.1** hace un rato, así que tomé la **23.2.0** sin saber si ya la están usando — es exactamente el hallazgo H-2. Y el pendiente 48 quedó escrito antes que su plantilla; si quiere que sea el primer documento que la cita, le agrego la línea que la nombra.

### 14 · Usuario — 2026-08-16 21:48:20
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\inventario-hu.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> ya se puede cerrar?

**Agente** — 2026-08-16 21:48:50
<!-- agente: abd95e6a-8af8-4fd1-bd0e-a80851d321c4 -->

No todavía. Dos de las cuatro casillas siguen en ☐:

| Para cerrar | |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ |
| **Toda historia disparada está escrita en su épica** | ☐ |
| **Lo que se hizo está aprobado y guardado** | ☐ |

Falta:

1. **Las dos HU que dispararon los hallazgos no existen en EP-004** — «el revisor cuenta las HU sin fase» y «nadie toma un número de pendiente que ya exista». Están escritas como narrativa dentro del resumen, no como historias en la épica.
2. **Nada está commiteado.** Cambié `VERSION`, `CHANGELOG.md`, el mapa del sitio, el README de pendientes, y creé la plantilla y el pendiente 48.

Y una corrección al resumen: la plantilla que acabamos de crear no está anotada ahí. La agrego.

Para cerrar hacen falta dos pasos, y ninguno lo hago sin que usted diga:

1. **Escribir las dos HU en EP-004** — es media hora, y son las que evitan que esta cuenta se vuelva a levantar a mano.
2. **Commit.** Le muestro el diff completo antes.

También queda sin hacer lo que ya le había propuesto: renombrar la sesión de `2026-08-16-sesion-8.md` a `2026-08-16-las-hu-sin-su-fase.md`, que es lo único que la próxima sesión va a ver de esta.

¿Sigo con las dos HU, o prefiere cerrar acá y dejarlas anotadas como están?

### 15 · Usuario — 2026-08-16 21:49:26
> si siga con ellas y las agrega al inventario

**Agente** — 2026-08-16 21:55:12
<!-- agente: 5f9833e2-2fe9-457d-a010-c3c6e9449605 -->

El validador ya hace parte de lo que la HU-017 dice que falta. Lo compruebo antes de dejarla escrita.

Encontré algo que cambia la HU-017: `validar.py fases` **ya reporta** las HU sin fase (`F12.2`) y los documentos que le faltan a cada fase (`F12.13`) — 54 avisos ahora mismo. Lo único que no hace es dar el total. La reescribo a lo que de verdad falta.

Las dos HU quedaron escritas:

- **[HU-017 — Decir cuántas HU quedan sin su fase completa](documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md)**
- **[HU-018 — Avisar cuando dos pendientes se disputan el mismo número](documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md)**

Con su `README`, su línea en la [épica](documentacion/epicas/EP-004-comprobacion-automatica/epica.md), la fase 9 en la hoja de ruta, y sus dos filas en el inventario — que pasó a **68 HU · 14 completas · 54 incompletas**.

**Un error mío que corregí antes de dejarlo escrito:** la HU-017 nació pidiendo que un validador listara las HU sin fase. Corrí `validar.py fases` y ya lo hace — reporta la HU sin fase (`F12.2`) y el documento que le falta a cada fase (`F12.13`), 54 avisos ahora mismo. Lo único que no da es el total, así que la recorté a eso. Queda anotado en el resumen y en su bitácora: se dio por hecho sin comprobar, y se comprobó tarde.

La sesión ya tiene tres de las cuatro casillas. Falta la suya: aprobar y commitear. ¿Le muestro el diff?

### 16 · Usuario — 2026-08-16 22:00:12
> ya se puede cerrar?

**Agente** — 2026-08-16 22:00:52
<!-- agente: d702e138-c254-4a2e-a173-36650e8f847e -->

No. Queda una casilla, y es suya: **aprobar y guardar**. Las otras tres están.

No, y el commit no es simple: **el árbol mezcla las dos sesiones**.

`VERSION` en git es `21.3.0`. Sin commitear hay siete versiones: `21.3.1`, `22.0.0`, `22.1.0`, `23.0.0`, `23.1.0`, `23.1.1` y la mía, `23.2.0`. Las seis primeras son de la otra sesión. Lo mismo en `CHANGELOG.md`, y hay 30 archivos más movidos que no toqué.

Tres salidas:

| | Qué deja |
|---|---|
| **A · Esperar** a que la otra sesión commitee lo suyo, y después commitear lo mío encima | Cada commit dice lo que hizo su sesión. Es lo limpio, pero depende de esa sesión |
| **B · Commitear solo mis rutas** — el pendiente 48, la plantilla, las dos HU, la épica, el mapa, el resumen — y `VERSION`/`CHANGELOG` por trozos | Sale hoy, pero `VERSION` sube de 21.3.0 a 23.2.0 en un commit que no explica las seis versiones del medio |
| **C · Un solo commit con todo** | Rápido y mentiroso: el mensaje tendría que contar trabajo que no es de esta sesión |

Recomiendo la **A**: es exactamente el caso que la HU-018 y el pendiente 22 describen, y hacer la B o la C sería dejar el defecto escrito en el historial.

Mientras tanto la sesión queda con tres casillas de cuatro, y nada se pierde: todo está en archivos.

### 17 · Usuario — 2026-08-16 22:03:37
> solamente su sesion

**Agente** — 2026-08-16 22:06:37
<!-- agente: 2706b100-878a-44ea-95a8-43a646032dec -->

El usuario renombró el pendiente a `48-inventario-hu.md`. Primero arreglo los enlaces que quedaron apuntando al nombre viejo.

Staging solo lo mío. `VERSION`, `CHANGELOG.md` y `pendientes/README.md` los está escribiendo también la otra sesión, así que de esos tomo únicamente mis líneas.

Cinco borrados de la otra sesión ya estaban en el índice desde antes. Los saco.

Índice limpio: **12 archivos, todos de esta sesión**. Nada de la otra.

```
 CHANGELOG.md                    |  11 +     (solo el bloque 23.2.0)
 VERSION                         |   2 +-
 anatomia/mapa-del-sitio.md      |   3 +-
 EP-004/HU-017-…  (HU + README)  | 235 +++
 EP-004/HU-018-…  (HU + README)  | 215 +++
 EP-004/epica.md                 |   3 +
 resumenes/2026-08-16/sesion-8.md|  66 +++
 pendientes/48-inventario-hu.md  | 109 +++
 pendientes/README.md            |   8 +     (solo mi sección)
 plantillas/inventario-hu.md     |  56 +++
```

El mensaje que propongo:

```
Deja inventariadas las HU que no tienen su fase

Pedido: analizar las HU, ver a cuáles les falta algo y dejar por escrito
qué le falta a cada una. Una sola tabla y no un archivo por HU: con leerla
ya se sabe cuáles están incompletas. El encabezado con los contadores se
llena y se va llenando a medida que se completen. Y que esa forma quede
también como plantilla reusable.

De las 66 HU, 52 no tienen su fase completa: 49 sin ninguna carpeta y 3 a
medias. Casi todas están construidas, así que lo que falta es
retrodocumentar, no construir.

- pendientes/48 — la tabla: una fila por HU, una casilla por documento
- plantillas/inventario-hu.md — el molde (v23.2.0, MENOR)
- EP-004 · HU-017 y HU-018 — las dos historias que dispararon los hallazgos
- resumen de la sesión con los dos hallazgos

La HU-017 nació pidiendo lo que `validar.py fases` ya hace —listar las HU
sin fase y los documentos que faltan— y se recortó a lo único que no da:
la cuenta.

VERSION salta de 21.3.0 a 23.2.0 porque las seis versiones del medio son
de otra sesión que todavía no ha commiteado lo suyo.
```

¿Lo commiteo así?

### 18 · Usuario — 2026-08-16 22:06:53
> si

**Agente** — 2026-08-16 22:07:21
<!-- agente: 0cff3487-5c1c-4d6e-87f6-e62f26031b54 -->

Commiteado: **`333c3a1`** — 12 archivos, todos de esta sesión. Los dos validadores de commit pasaron sin incumplimientos.

Las cuatro casillas quedaron marcadas, así que **sí, ya se puede cerrar.**

Queda en el árbol lo de la otra sesión, intacto: sus 30 archivos, sus seis versiones del `CHANGELOG` y los cinco borrados de `pendientes/` que devolví al estado en que estaban.

Lo único suelto es el nombre de la sesión: sigue guardándose como `2026-08-16-sesion-8.md`. Si quiere renombrarla:

```
python "C:/Ing. Jose/ia/agente/validadores/historico.py" --renombrar "C:/Ing. Jose/ia/agente/historico-chat/2026-08-16-sesion-8.md" --tema "las-hu-sin-su-fase" --resumen "inventario de las 66 HU: 52 sin su fase completa, y la plantilla del tablero"
```

Y en el chat, `/rename las-hu-sin-su-fase` — ese lo tiene que escribir usted.

### 19 · Usuario — 2026-08-17 08:56:35
> ya se puece cerrar?

**Agente** — 2026-08-17 08:58:49
<!-- agente: cb91a5bd-cc34-482a-b42e-2b5b24ef7588 -->

Falta lo que `/rename` no toca: el archivo del histórico. Lo corro.

Subió de 3 fallas a 5. Miro qué se rompió con el renombrado.

Casi. El renombrado dejó tres cosas sin guardar, y una era un defecto:

**Renombrar rompió dos enlaces de fuera.** El resumen pasó de `sesion-8.md` a `las-hu-sin-su-fase.md`, y los dos `README` de las HU nuevas lo citaban por el nombre viejo — el revisor subió de 3 fallas a 5. Los arreglé; ya volvió a 3, que son las de antes y ninguna mía.

Es el punto 4 del pendiente [33](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), pasando a los diez minutos de que el mismo comando dijera «índice al día». Lo dejé como hallazgo H-3 en el resumen, con evidencia, y sin abrir pendiente nuevo: sería el tercero sobre lo mismo.

Falta un segundo commit con esos tres archivos:

```
 EP-004/HU-017-…/README.md   (enlace corregido)
 EP-004/HU-018-…/README.md   (enlace corregido)
 resumenes/2026-08-16/las-hu-sin-su-fase.md → renombrado, + H-3
```

Más el archivo de la transcripción, que el renombrado movió. Mensaje: `Corrige los enlaces que rompió renombrar la sesión`.

¿Lo commiteo y con eso cierra?

### 20 · Usuario — 2026-08-17 09:00:08
> si

**Agente** — 2026-08-17 09:01:56
<!-- agente: 9be961fd-27df-4b88-a053-c4d93201e02f -->

Sí, ya se puede cerrar.

**`3b51065`** — el renombrado y los dos enlaces corregidos. Los dos validadores de commit, limpios. Las cuatro casillas del resumen marcadas.

Lo que deja la sesión:

| | |
|---|---|
| [pendientes/48-inventario-hu.md](pendientes/48-inventario-hu.md) | 68 HU en una tabla · 14 completas, 54 no |
| [plantillas/inventario-hu.md](plantillas/inventario-hu.md) | el molde, v23.2.0 |
| [EP-004 · HU-017](documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) y [HU-018](documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md) | las dos historias, fase 9 de la épica |
| [el resumen](historico-chat/resumenes/2026-08-16/las-hu-sin-su-fase.md) | tres hallazgos: H-1 y H-2 abiertos, H-3 resuelto |

Dos cosas para la próxima, que están en el resumen: por cuál fila del inventario empezar, y que el trabajo de la otra sesión sigue sin commitear en el árbol.
