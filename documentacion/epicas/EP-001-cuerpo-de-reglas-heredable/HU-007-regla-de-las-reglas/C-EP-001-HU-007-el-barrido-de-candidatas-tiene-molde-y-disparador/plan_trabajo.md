# Plan de Trabajo — Fase C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-007](../HU-007-regla-de-las-reglas.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-007 La regla de las reglas](../HU-007-regla-de-las-reglas.md), una sola |
| **Módulo** | Cuerpo de reglas, capítulo `20` y moldes del estándar |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva**, y 📝 **modifica** la fase `B`: la `B` trajo `20·M19` para el momento de automatizar una regla; esta trae el momento **anterior**, cuando la regla ni siquiera se ha propuesto.

**De dónde sale:** el punto 2 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), abierto desde el 2026-08-06. El usuario ordenó resolverlo el 2026-08-22.

**CA que cubre:** el `CA-06`, que nace con esta fase.

### 0.1 El criterio nace con la fase, y eso hay que decirlo

`HU-007` tenía cinco criterios y **ninguno cubría el barrido**: los tres primeros revisan una regla que alguien ya decidió escribir, el cuarto pregunta si sigue sirviendo y el quinto si conviene automatizarla. El propio pendiente 33 lo había medido y dejó la salida en dos: *«falta un criterio, o una historia propia»*.

**Se eligió el criterio, no la historia**, porque el tema es el mismo que esta historia ya posee, cómo nace una regla ([`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)); una historia aparte partiría el tema en dos dueños. La decisión se le muestra al usuario al reportar la fase: si prefiere historia propia, el `CA-06` se mueve entero.

## 1. Objetivo y alcance

**Objetivo:** que lo que el usuario pidió dos veces no se pierda entre sesiones, con un molde para escribirlo y un momento fijo del flujo que obligue a hacerlo.

**El defecto, con sus palabras:** *«sin disparador, se hace cuando el usuario lo pida es un favor, no una norma»*. El barrido se hizo **una vez**, el 2026-08-13, salieron 27 fichas analizadas, y nadie volvió a hacerlo en nueve días.

**Fuera de alcance:**

- **Correr el barrido del tramo actual.** Esta fase construye el molde y la regla; el primer barrido real lo dispara la próxima publicación, que es lo que la regla exige.
- **Un programa que compruebe el barrido.** Por [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), la regla se automatiza cuando ya se cumple a mano, y esta todavía no se cumplió ninguna vez.
- **Reabrir las 27 fichas del barrido de 2026-08-13**, que ya tienen su salida escrita.

## 2. Análisis previo, línea base verificada

| Qué se verificó | Resultado |
|---|---|
| ¿Existe una regla que ya exija esto? | **No.** [`01·C10`](../../../../../base/01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla) exige notar el patrón **en el momento**; [`01·C26`](../../../../../base/01-conducta.md#c26--la-regla-que-serviría-en-otra-empresa-va-a-la-base-común) decide dónde vive la regla que salga. Ninguna manda releer el tramo pasado |
| ¿Existe el molde? | **No.** El barrido de 2026-08-13 se escribió a mano, sin plantilla |
| ¿Hay un momento del flujo donde enganchar? | **Sí:** publicar la versión, que [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) ya obliga a atravesar |
| ¿Cuál es el identificador libre del capítulo `20`? | `M20`; el último ocupado es `M19` |

### 2.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| [`plantillas/candidatas-a-regla.md`](../../../../../plantillas/candidatas-a-regla.md) | Nuevo: el molde del barrido, con las cuatro salidas |
| [`base/20-meta-reglas/reglas/M20-...md`](../../../../../base/20-meta-reglas/reglas/M20-antes-de-publicar-una-version-se-barre-lo-que-se-pidio-dos-veces.md) | Nuevo: la regla que lo exige antes de publicar |
| [`base/20-meta-reglas/base.md`](../../../../../base/20-meta-reglas/base.md) | La fila de `M20` en el índice del capítulo |
| [`plantillas/README.md`](../../../../../plantillas/README.md) | La fila del molde nuevo |
| [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) | `M20` clasificada, y por qué no es validable |
| `HU-007-regla-de-las-reglas.md` | El `CA-06` |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |

### 2.2 Las trece preguntas, en corto

| # | Respuesta |
|---|---|
| 1-3 | Un molde y una regla, para que lo pedido dos veces no se pierda; lo usa cualquier proyecto que herede `base/` |
| 4-5 | §1; fuera queda correr el barrido y automatizarlo |
| 6-8 | No hay datos ni interfaz: el entregable es texto del estándar |
| 9 | §2.1 |
| 10 | En `base/20-meta-reglas/`, que se carga al abrir sesión, y en `plantillas/` |
| 11 | No aplica porque no hay ejecución ni permisos |
| 12 | **Sí hay migración de norma:** es MAYOR, un proyecto al día tiene que barrer antes de publicar. No obliga a barrer hacia atrás |
| 13 | [plan_pruebas.md](plan_pruebas.md) |

### 2.3 Dudas por resolver

**Ninguna abierta.** La única que había —criterio nuevo o historia propia— se decidió en §0.1 y se le muestra al usuario con el reporte.

## 3. Tareas

| # | Tarea | Estado |
|---|---|---|
| T-01 | Escribir el molde del barrido con las cuatro salidas excluyentes | ☑ |
| T-02 | Escribir `M20` con su checklist aplicado y su cuerpo dentro del molde | ☑ |
| T-03 | Registrarla en el índice del capítulo, en `plantillas/README.md` y en `reglas-validables.md` | ☑ |
| T-04 | Agregar el `CA-06` a la historia | ☑ |
| T-05 | Correr las pruebas del [plan_pruebas.md](plan_pruebas.md) | ☑ |
| T-06 | Versionar y cerrar | ☑ |

## 4. Riesgos

| # | Riesgo | Cómo se ataca |
|---|---|---|
| C-01 | Que la regla nueva repita a `01·C10` | El sello de `M20` responde la fila 2 y la 17: `C10` es el momento, esta es el repaso |
| C-02 | Que el barrido se vuelva un trámite vacío | El molde exige decir **qué se leyó** y cuántas veces se pidió cada cosa; un barrido sin fuentes no se puede contrastar |
| C-03 | Que se use para colar reglas sin aprobación | El molde lo dice en su §4: ninguna candidata se convierte en regla desde ahí; eso lo decide el usuario |
