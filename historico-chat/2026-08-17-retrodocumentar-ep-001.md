<!-- sesion: 83f10a2f-6ed9-462c-be00-161912ea5244 -->
<!-- nombre: preguntado -->

# 2026-08-17 — Retrodocumentar ep 001

## Conversación

### 1 · Usuario — 2026-08-17 09:20:09
> cree el: plan_trabajo de las fases que no lo tienen parta de principio de que este es un proyecto que ya estaba y por lo tanto: plan_trabajo se crea es para documentar eso que ya esta

**Agente** — 2026-08-17 09:58:11
<!-- agente: 699b4a90-3a60-442c-ba28-bc0cc7685866 -->

Ya tengo el terreno verificado. Empiezo a escribir, en el orden del tablero del pendiente 48 (EP-001 primero).

Encontré un defecto mientras verificaba: `metareglas.py` no tiene punto de entrada — es el punto 2 del pendiente 53. Corrijo lo que yo mismo afirmé en el plan de HU-003.

Hecho lo de EP-001. Antes del detalle, una corrección al pedido: **ninguna fase estaba sin `plan_trabajo`** — las diecinueve que existían ya lo tenían todas. Lo que falta son las **51 HU sin ninguna fase**, así que abrí la fase y le escribí su plan, que es la columna `plan_trabajo` del tablero del pendiente [48](pendientes/48-inventario-hu.md).

## Lo que quedó escrito — 7 filas de 51

| HU | Fase | Qué es de verdad |
|---|---|---|
| [HU-003](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/plan_trabajo.md) | núcleo blindado | Retro-doc. Solo falta escribir el criterio de entrada al núcleo (RN-06) |
| [HU-004](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia/plan_trabajo.md) | conducta | **Híbrido.** Dos de sus siete RN no son regla: viven en la memoria |
| [HU-005](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-005-convenciones-de-ingenieria/A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas/plan_trabajo.md) | convenciones | Retro-doc puro. No toca `base/` |
| [HU-006](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/plan_trabajo.md) | capa del proyecto | Retro-doc puro |
| [HU-007](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla/plan_trabajo.md) | meta-reglas | Retro-doc puro |
| [HU-008](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-008-derogacion-sin-borrar/A-EP-001-HU-008-retrodocumentar-la-derogacion/plan_trabajo.md) | derogación | Retro-doc + dos pruebas: hoy nada comprueba que las ocho derogadas sigan ahí |
| [HU-010](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/plan_trabajo.md) | `F2` no dice cuándo no aplica | **Construcción.** Acá no hay nada que retro-documentar |

Cada carpeta lleva su `README.md` (`13·DOC17`), la §8 de cada HU nombra su fase y las dos casillas están marcadas en el 48. Los siete planes traen las catorce secciones de `F14`, sin marcas de incertidumbre y con cada tarea colgando de su CA: `validar.py flujo`, `fases`, `trazabilidad` y `estandar` dan **exactamente los mismos números que antes de empezar** — ni una falla ni un aviso nuevo.

## Tres cosas que salieron al verificar

1. **`metareglas.py` no se puede correr.** Escribí que comprobaba la fila 15 del checklist, fui a correrlo y sale en silencio con código 0, sin subcomando en `validar.py`. Corregí el plan y lo anoté como segundo caso del pendiente [53](pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md) — pesa más que `enlaces.py`: es el único que decide once de las veinte filas del checklist, y `M16`.
2. **El CA-02 de HU-010 hablaba de dos fases; son diecisiete.** Nueve se apoyan en su historia de usuario, ocho declararon la deuda. Seis de esas nueve nacieron hoy: retro-documentar EP-001 multiplicó por cuatro el caso que `F2` no cubre.
3. **La suite ya estaba roja.** 3 de 246 fallas y 3 en `validar.py estandar`, todas del cambio sin guardar de la sesión del 16 (índice de `pendientes/README.md` y un enlace roto). No lo toqué: es trabajo de otra sesión.

## Una salvedad sobre el orden, y lo que falta decidir

Pedir el `plan_trabajo` de todas las fases es recorrer **la columna**; el paso 1 del tablero pide una fila a la vez. Lo hice como lo pidió y lo dejé registrado en el 48 con su costo: las siete filas quedan a medias hasta que les entren los otros cuatro documentos. Su instrucción también resuelve lo que la sesión anterior dejó abierto —con qué archivo se hace visible una fase recién abierta—: la carpeta nace con su plan, así que nunca existe vacía. Eso quedó escrito.

Falta que usted decida:

| # | Decisión | Recomendación |
|---|---|---|
| 1 | Poner al día el paso 2 de `plantillas/inventario-hu.md`, que todavía dice «se crea la carpeta y se marca Fase» | Hacerlo, pero con su propia entrada de `CHANGELOG` y subida de `VERSION` (`20·M10`) — no lo colé en esto |
| 2 | Si sigo con **EP-002** (6 filas) o para acá | Seguir por épica, en el orden del tablero: quedan 44 |
| 3 | Las dos exigencias de HU-004 que hoy son recuerdo — la pregunta que no es orden y el defecto que se corrige sin preguntar — ¿suben a regla del capítulo `01`? | Subirlas: un recuerdo no viaja a un proyecto que hereda `base/` |

Los siete planes están **sin aprobar**: `02·F4` no deja tocar nada de lo que planifican hasta que los lea. Nada está commiteado.

### 2 · Usuario — 2026-08-17 10:42:02
> menos es mas

**Agente** — 2026-08-17 10:42:46
<!-- agente: 6c86c28f-869e-4f6b-9b7f-af7f3820847b -->

Anotado en la memoria: es la segunda vez en dos días, y las dos reportando trabajo terminado.

Siete planes escritos (EP-001 completa), sin aprobar. Quedan 44 filas.

Falta que decida: si sigo con EP-002.

Esta sesión la guardo como `2026-08-17-retrodocumentar-ep-001.md` — los planes de trabajo de las siete HU de EP-001 que no tenían fase, ¿va?

### 3 · Usuario — 2026-08-17 10:48:40
> si

**Agente** — 2026-08-17 10:49:11
<!-- agente: 1ec7edc0-85d0-46f3-ae3b-55321101eb5c -->

Renombrada: `2026-08-17-retrodocumentar-ep-001.md`, índice al día y sin enlaces rotos nuevos.

Pegue esto para que la pestaña y `/resume` queden con el mismo nombre:

```
/rename retrodocumentar-ep-001
```

¿Sigo con EP-002 (6 filas)?

### 4 · Usuario — 2026-08-17 10:49:41
> complete la tarea no me pregunte más

**Agente** — 2026-08-17 11:46:42
<!-- agente: baf5004b-e749-4b58-acc4-7666663fce21 -->

Sigo con las 44 filas restantes, épica por épica.

Para las 31 filas restantes voy a generar los planes con un molde común, poniendo a mano el contenido verificado de cada HU.

Tarea completa: las 51 filas del tablero tienen su fase abierta y su `plan_trabajo` escrito.

| Épica | Filas | Qué son |
|---|---|---|
| EP-001 | 7 | 5 retro-doc · 1 híbrida · 1 construcción |
| EP-002 | 6 | 4 retro-doc · 1 híbrida · 1 construcción |
| EP-003 | 6 | 5 retro-doc · 1 híbrida |
| EP-004 | 13 | 6 retro-doc · 3 híbridas · 4 construcción |
| EP-005 | 8 | 4 retro-doc · 1 híbrida · 3 construcción |
| EP-006 | 7 | 6 retro-doc · 1 híbrida |
| EP-007 | 4 | 4 retro-doc |

**37 retro-documentan, 14 construyen.** El inventario dice «casi todo es retrodocumentación»; la cuenta real quedó escrita.

**Estado del revisor:** `fases` pasó de 19 HU sin fase a **cero**. `flujo`, `estandar` y `trazabilidad` dan los mismos números que antes de empezar — cero avisos nuevos por los 102 archivos que entraron. La suite sigue con las mismas 3 fallas de 246, todas del cambio sin guardar de otra sesión (índice de `pendientes/README.md`, un enlace roto y una cita sin enlace).

**Cinco huecos de fondo que salieron al verificar**, cada uno anotado en el plan de su fase: nada comprueba `20·M10` al guardar; las señales viven en una base binaria que el historial no puede leer; ningún modelo de cierre pide la versión; la lista de puntos de aprobación no está en `base/`; el aviso de desfase no dice qué cambió entre las dos versiones.

Nada está commiteado, y los 51 planes están sin aprobar.

### 5 · Usuario — 2026-08-17 11:47:06
> ya se puede cerrar la sesión?

**Agente** — 2026-08-17 11:47:49
<!-- agente: d53e5c23-22d0-4fc4-8924-827b767f79db -->

No. Falta una casilla de cuatro, y es suya:

| Para cerrar | Estado |
|---|---|
| Hallazgo resuelto con su decisión escrita | ☑ |
| Hallazgo abierto con su pendiente creado | ☑ |
| Historia disparada escrita en su épica | ☑ |
| **Lo que se hizo, aprobado y guardado** | **☐** |

Los 51 planes están escritos y sin aprobar. `02·F4` no deja ejecutar nada de lo que planifican hasta que usted los lea, y nada está commiteado.

Dos cosas por separado: si aprueba el trabajo, y si quiere que lo guarde.

### 6 · Usuario — 2026-08-17 11:50:12
> osea el plan de trabajo ya se encarga de crear el plan de prueba y el resto?

**Agente** — 2026-08-17 11:51:02
<!-- agente: e9003ac8-909a-47e7-8fb7-4a60df8bac35 -->

No. El `plan_trabajo` no crea nada: es solo el documento que dice qué se va a hacer. Los otros cuatro los escribe quien ejecuta la fase, cada uno en su momento.

| Documento | Cuándo se escribe |
|---|---|
| `plan_pruebas` | **Junto al plan de trabajo**, antes de aprobar |
| `estado-fase` | Mientras la fase corre |
| `resultado_pruebas` | Al correr las pruebas |
| `funcionalidad_implementada` | Al cerrar |

Y ahí hay un problema que su pregunta destapa: `02·F4` pide **los dos primeros juntos** — plan de trabajo y plan de pruebas —, después la pausa y el visto bueno. Llenar solo la columna `plan_trabajo` dejó las 51 filas **un documento antes de poder aprobarse**.

Falta que decida:

| Salida | Qué deja |
|---|---|
| **1 · De acá en adelante, fila por fila** | Cada fila queda con sus dos planes juntos y aprobables. Se avanza más lento pero cada fila sirve. |
| 2 · Los 51 `plan_pruebas` también por columna | Termina la columna, y las 51 filas siguen sin poder aprobarse hasta que entre el resto. |

Recomiendo la **1**: un plan de pruebas existe para correrse, y sin la aprobación no se corre nada.

### 7 · Usuario — 2026-08-17 12:01:46
> para que la fase esté para aprobarla que le falta?

**Agente** — 2026-08-17 12:02:25
<!-- agente: e96137f7-915a-4016-b0d0-efb19a1ade1f -->

Para aprobarla, a cada fase le falta:

| Qué | Por qué |
|---|---|
| **`plan_pruebas.md`** | `02·F4`: los dos planes se aprueban juntos. Es lo único obligatorio que falta. |
| **`estado-fase.md`** | Dice en qué estación va y qué la tiene detenida. En este repo las fases llegan a la aprobación con él escrito, en estación 7. |

Los otros dos van después: `resultado_pruebas` al correr las pruebas, `funcionalidad_implementada` al cerrar.

Y una cosa más, que no es documento: **26 de los 51 planes tienen dudas abiertas** que usted tiene que resolver. Esas no impiden aprobar el plan, pero sí arrancar las tareas que dependen de ellas.

Así que la fase queda aprobable con dos documentos por fila. Si va fila por fila, cada una sale completa hasta la puerta de aprobación.

### 8 · Usuario — 2026-08-17 12:04:08
> listo pero ya quedaron todos los planes de trabajo?

**Agente** — 2026-08-17 12:04:36
<!-- agente: e8825149-0218-4834-a487-57a3796c6cbc -->

Sí. 70 carpetas de fase, 70 con su `plan_trabajo.md` y su `README.md`. Cero HU sin fase, y las 68 filas del tablero con **Fase** y **`plan_trabajo`** marcadas.

De esas 70: 19 ya existían, 51 se escribieron hoy.

Falta su aprobación, y nada está commiteado.

### 9 · Usuario — 2026-08-17 12:06:15
> cual fue la primer instrucción que le di?

**Agente** — 2026-08-17 12:06:33
<!-- agente: fcde8d56-156b-482f-904c-48e2097e6517 -->

Textual, a las 09:20:09:

> cree el: plan_trabajo de las fases que no lo tienen parta de principio de que este es un proyecto que ya estaba y por lo tanto: plan_trabajo se crea es para documentar eso que ya esta

Está en [historico-chat/2026-08-17-retrodocumentar-ep-001.md](historico-chat/2026-08-17-retrodocumentar-ep-001.md), que lo escribió el enganche.

### 10 · Usuario — 2026-08-17 12:07:39
> el: plan_pruebas.md lo crea es con base al pla de trabajo cierto?

**Agente** — 2026-08-17 12:08:02
<!-- agente: bd346d0c-fddf-4ca7-a44d-04b023380042 -->

No exactamente. Los dos salen de lo mismo: **los criterios de aceptación de la HU** (`02·F18`).

| Documento | De dónde sale | Qué responde |
|---|---|---|
| `plan_trabajo` | Los CA de la HU | Qué se hace, en qué orden, sobre qué archivos |
| `plan_pruebas` | Los CA de la HU | Con qué casos se comprueba cada CA, con qué datos y en qué ambiente |

Su exigencia central es que **ningún CA quede sin al menos un caso**.

Del plan de trabajo toma lo que ya quedó fijado ahí: la línea base verificada, los archivos, el ambiente y los identificadores de evidencia del §5. Por eso se escriben juntos — pero si el plan de trabajo se equivocó en un CA, el plan de pruebas no lo hereda: manda la HU.

### 11 · Usuario — 2026-08-17 12:08:40
> listo ya puedo cerrar la sesión)?

**Agente** — 2026-08-17 12:08:58
<!-- agente: fe10b148-35ba-442e-ab10-f23530cfd612 -->

Todavía no. Falta lo mismo de antes, y es suyo:

1. **Aprobar los 51 planes** (o no) — la cuarta casilla del cierre.
2. **Guardar**, que se pide aparte.
3. **La decisión del H-10:** el `plan_pruebas` por columna o fila por fila. Hoy vive solo en el resumen; si cierra sin decidirla, hay que bajarla al paso 3 del pendiente 48 para que no se pierda.

Con eso queda cerrada. Digo la palabra y lo hago.

### 12 · Usuario — 2026-08-17 12:17:12
> 1. la aprobación de los planes no hace parte de esta sesión se aprobaran a medida que que se vayan ejecutando
> 2. No entiendo elrequerimiento
> 3. Tampoco entiendo el requerimiento

**Agente** — 2026-08-17 12:17:53
<!-- agente: fb086c4a-c36a-4841-aca6-626b4cc59d1b -->

Anotado el 1: la aprobación no es de esta sesión, cada plan se aprueba cuando se vaya a ejecutar su fase. Eso cierra la cuarta casilla.

Los otros dos, en palabras simples:

**2 · Guardar** = hacer el commit. Los 102 archivos de hoy están escritos pero **solo en el disco**, sin entrar a git. Si no se guardan, otra sesión los puede pisar o se pierden. La pregunta es: ¿los commiteo?

**3 · Ya lo contestó usted sin darse cuenta.** Yo preguntaba si escribía ahora los 51 `plan_pruebas` de una, o uno por fase cuando le toque. Si cada plan se aprueba al ejecutar su fase, el plan de pruebas se escribe ahí mismo, junto a él. Queda decidido: fila por fila, en su momento. Lo dejo escrito así y no hay nada más que decidir.

Entonces solo falta el 2. ¿Commiteo?

### 13 · Usuario — 2026-08-17 12:22:22
> si
