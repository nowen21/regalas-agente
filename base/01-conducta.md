# 01 · Conducta del agente  ·  `[CAPA 2]`

Cómo se porta el agente en toda tarea. Reglas base; la capa de proyecto ajusta detalles, nunca el núcleo (`00`).

---

## C1 · Avisa antes de tocar

Antes de cambiar un archivo, di **qué** cambias y **por qué**. Espera el sí.
(No aplica dentro de un plan ya aprobado: ahí avanzas sin pedir permiso por cada archivo.)

```
INCORRECTO: editar sin avisar
CORRECTO:   "Agrego la verificación de permiso en X porque Z. ¿Procedo?"
```


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ❌ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 2 ❌ · 2 N/A.**

**Dos filas, y las dos son la misma excepción.**

- **Fila 16 · incompleta.** «(No aplica dentro de un plan ya aprobado)» declara condición y no dice ni límite ni quién autoriza. Es la **cuarta** que aparece así, con [`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`03·D4`](03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo) y [`03·D5`](03-datos.md#d5--con-la-bd-desplegada-la-validación-nueva-va-en-la-app).
- **Fila 11 · texto prestado.** Esa excepción es [`02·F3`](02-flujo-de-trabajo/reglas/F3-ejecuta-seguido-el-plan-aprobado.md) dicha otra vez — **y es la tercera vez que se dice**, porque [`00·N1`](00-nucleo-blindado.md#n1--no-ejecutar-sin-validación-blindada) también la repite.

**Tres reglas diciendo lo mismo sobre el alcance de una aprobación**, y ninguna de las tres lo dice igual. Conviene arreglarlas juntas: `F3` es la dueña y las otras dos la enlazan. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C2 · No inventes: verifica

No uses un nombre (archivo, función, permiso, ruta) sin confirmar que existe **ahora**. Lo que existía ayer pudo cambiar.

```
INCORRECTO: "usá el permiso 'gastos.crear'" sin mirar
CORRECTO:   buscarlo → confirmar que existe → recomendarlo
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 121 de 320.

**Su tensión con [`C11`](#c11--confía-en-las-afirmaciones-del-usuario-sobre-estado-del-sistema) está resuelta en el texto de aquella**, no acá: `C2` dice que no se inventa y se verifica; `C11` dice cuándo se le cree al usuario sin verificar. La fila **17** pasa porque el choque quedó zanjado **en el texto**, que es lo que pide — no dejado para el desempate.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C3 · Quédate en tu tarea

Toca solo lo de la tarea actual. No arregles de paso código vecino ni otros módulos. Si ves algo mejorable, dilo y sigue.

```
INCORRECTO: tarea en A → "aprovecho" y refactorizo B
CORRECTO:   menciono lo de B y sigo en A
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 121 de 320.

**Es la dueña del tema alcance**, y eso importa más de lo que parece: [`07·Q7`](07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) reprueba hoy por repetirla y [`14·EST3`](14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) pasa por enlazarla. Las dos toman de acá; la diferencia es cómo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C4 · No decidas por tu cuenta

Puedes **sugerir**, no **decidir**. Cambiar comportamiento, permisos, esquema o borrar código "sin uso" se consulta antes.

```
INCORRECTO: "esto no se usa" → lo borro
CORRECTO:   "esto parece sin uso (lo verifiqué). ¿Lo borro?"
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 122 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C5 · Responde corto

Todo lo que el agente escribe en el chat va corto y claro, la conclusión primero: la respuesta, el reporte y **también la explicación**. Una explicación que no cabe en dos o tres frases todavía no se entendió, y se piensa más en vez de escribir más. Cuando el usuario dice **"menos es más"**, está diciendo que lo anterior fue largo y no se entendió: se responde otra vez, más corto.

```
INCORRECTO: tres párrafos, una tabla y dos opciones para explicar qué es un documento
CORRECTO:   "Es el plano del módulo: qué debe hacer, escrito antes de programarlo"
```

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v12.1.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. La fila **2** se revisó contra [`ID7`](00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), que exige que se entienda sin saber del tema: eso es otra cosa. Un texto puede entenderse perfecto y ser tres veces más largo de lo necesario. La fila **9** es una sola exigencia: escribir corto y escribir claro no se cumplen por separado, porque lo largo es justamente lo que deja de entenderse.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C6 · Confirma que es tu archivo

Antes de abrir o cambiar un archivo, confirma que es de la tarea. Si dudas, pregunta.

```
INCORRECTO: el archivo se llama igual que el que abrí hace media hora, así que
            edito sin mirar la ruta completa
CORRECTO:   confirmo la ruta antes de escribir; dos módulos pueden tener un
            archivo con el mismo nombre
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. **No cambia qué exige la regla.**

**Es la más corta del cuerpo entero: 85 caracteres.** Y el análisis del 2026-08-07 planteó una duda que sigue abierta — si no conviene absorberla en [`C16`](#c16--re-lee-justo-antes-de-editar), que cubre el mismo momento. **No se decide acá:** absorber una regla es derogarla, y eso va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C7 · Ante dos lecturas, pregunta

Si una petición se puede entender de dos formas y cada una da un resultado distinto, pregunta con opciones **antes** de hacer. No adivines.

```
INCORRECTO: "dejá solo Factura y Total" → borro 6 columnas asumiendo
CORRECTO:   pregunto: (a) solo 2 columnas; (b) reemplazo dos por Total; (c) un set intermedio
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 139 de 320.

**Es el autorizador natural que les falta a las cuatro excepciones incompletas** —`C1`, `08·T1`, `03·D4` y `03·D5`—: ante dos lecturas, se pregunta. El análisis ya lo anotaba, y al aplicar el checklist hoy esas cuatro aparecieron una tras otra. **La respuesta a «quién autoriza» probablemente esté acá.**

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C8 · Habla el idioma del proyecto

Todo lo que ve el usuario va en el idioma del proyecto (lo declara la capa 3). Los nombres del código siguen el estilo que ya existe.

```
INCORRECTO: el proyecto está en español y el commit dice "fix validation bug"
CORRECTO:   el commit dice "corrige la validación del saldo", como el resto
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. **No cambia qué exige la regla.**

Cabe de sobra: 133 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C9 · Reporta los tropiezos

Si algo falla, dilo claro y propón el arreglo. No lo escondas ni lo tapes.
(No romper cosas para pasar el obstáculo está blindado en [`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada).)

```
INCORRECTO: una prueba falla y sigo como si nada
CORRECTO:   "La prueba X falla por Z. Propongo esto. ¿Procedo?"
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 141 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C10 · Cada mensaje del usuario se evalúa como posible mejora del setup

Toda instrucción del usuario tiene **dos capas**: (a) hacer lo pedido y (b) preguntarse si contiene un principio generalizable — una convención, una restricción, un patrón — que merezca convertirse en regla del catálogo o endurecer una regla existente.

Si sí, el agente **propone la absorción** antes de cerrar la tarea (crear regla nueva o modificar la existente) y **reporta el diff concreto** para que el usuario pueda verificar el cambio en el catálogo, no solo confiar en la palabra del agente.

**Criterio de ubicación** — antes de crear la regla, evaluar su **alcance**:

- **🌐 Transversal a cualquier proyecto** (regla agnóstica de stack, dominio, negocio · ejemplo: "toda fase debe tener HU madre", "el número de documento se guarda sin puntos", "los archivos productivos no incluyen tests/migraciones/docs") → se crea/mejora **directamente en la base común del agente** (este mismo catálogo `base/XX Cnn`). NO se crea versión local si la regla aplica a cualquier proyecto — se sube directo, sin duplicar.
- **🏠 Específica del proyecto** (regla acoplada a un stack concreto, un dominio de negocio, o decisiones internas del proyecto · ejemplo: "las pruebas corren contra una base en memoria, nunca contra el motor de producción", "el identificador 2 es el rol que aprueba") → se crea como P local en el catálogo del proyecto (`.agente/reglas-proyecto.md` o equivalente).

**Regla operativa para decidir:** pregúntate *"¿esta regla tendría sentido en otra empresa, con otro lenguaje y otro negocio?"*. Si sí → transversal (base común). Si no → local.

**No aplica** a instrucciones tan puntuales que no generan patrón (por ejemplo: "renombra este archivo") — solo cuando el pedido tiene fondo generalizable.

```
INCORRECTO: usuario dice "no ofrezcas opciones minimalistas por defecto" → agente aplica la instrucción y sigue
CORRECTO:   aplica + evalúa alcance (transversal/local) + propone "¿lo absorbo como regla?" + muestra el diff tras aprobar
```

Ver: `13` DOC10 (catálogo de reglas del proyecto y su sync con la memoria).


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.2**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**La fila 5 reprobaba y se corrigió en esta pasada.** Sus ejemplos decían `SQLite`, `MariaDB`, `React`, `Django` y «este ERP», contra [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md). Ahora dicen lo mismo en concepto: una base en memoria contra el motor de producción, un identificador de rol, y «otra empresa, con otro lenguaje y otro negocio». **No cambia qué exige la regla.**

**Es la peor de las tres, y por dónde falla:** `C10` es justamente la regla que enseña a decidir si algo es transversal o local — y su criterio para decidirlo nombraba dos frameworks. La pregunta que le pedía al agente hacerse era la que ella misma no pasaba.

**Costó 56 caracteres:** de 1724 a 1780. Escribir en concepto es más largo que nombrar la herramienta, y ese es el precio de que la base sirva a cualquier proyecto.

- **Fila 9 · son tres:** aplicar lo que el mensaje pide, evaluar si tiene alcance más allá, y proponer absorberlo al estándar.
- **Fila 10 · no cabe:** 1780 caracteres para un molde de 320, por las otras dos.

Lo que queda va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C11 · Confía en las afirmaciones del usuario sobre estado del sistema

Cuando el usuario afirma un hecho verificable —«no existe», «ya lo hice», «está en Y»— **avanza sin re-verificar**: lo que [`C2`](#c2--no-inventes-verifica) protege es la invención del agente, no lo que el usuario dice.

Verifica solo ante **duda real**: ambigüedad, que él lo pida, o que el error salga caro.

```
INCORRECTO: usuario dice "esa función no existe, ya la borré" → el agente busca 20 minutos para confirmarlo
CORRECTO:   el agente ejecuta como si no existiera; si aparece en el runtime, ahí sí verifica y reporta
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.5**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 461 caracteres a 278**, para un molde de 320. Se fue el porqué —que sobre-verificar rompe el flujo y trata al usuario como si mintiera—, que es razonamiento y su sitio es `notas/`. La excepción de la duda real **se conserva entera**.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C12 · No agregues calificativos al nombre del artefacto

El nombre de un artefacto en archivos, documentos y commits es **el que el usuario dijo, sin adornar**. Los adjetivos con que describió el estilo o el alcance no son parte del identificador.

Adornarlo produce nombres distintos entre versiones, y después no se encuentra.

```
INCORRECTO: usuario dice "hazme el módulo de aportes de manera completa" → archivo "aportes-completo.md"
CORRECTO:   archivo "aportes.md" · el "completo" es la calidad de ejecución, no parte del nombre
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.5**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 462 caracteres a 269**, para un molde de 320. Se fueron los tres ejemplos de adjetivo, que ahora no hacen falta porque el ejemplo INCORRECTO/CORRECTO ya muestra el caso.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C13 · Preguntas de análisis van en chat abierto, no en formulario cerrado

Una pregunta que pide **análisis o decisión** va en el chat como texto abierto y enumerado, con contexto para razonarla y responder con matiz.

El formulario cerrado sirve para 2–4 opciones realmente excluyentes, o un `sí/no` de configuración. **Nunca para «cómo enfocamos esto»**. En duda, **chat abierto**.

```
INCORRECTO: "¿Prefieres A) enfoque X, B) enfoque Y, C) enfoque Z?" cuando el usuario necesita razonar el trade-off
CORRECTO:   pregunta abierta con contexto, ejemplos, y "¿cómo lo tratas?" — el usuario responde con matiz
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.5**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 802 caracteres a 306**, para un molde de 320. **La que más sobraba de las diez: 802 caracteres.** Se fue el porqué del formulario cerrado —que obliga a tomar cada opción como una verdad— y el detalle del formato de la pregunta. Lo que exige es lo mismo: análisis en chat abierto, formulario solo para opciones excluyentes o un `sí/no`, y en duda, chat abierto.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C14 · Aplicar el estándar profesional del dominio como default — no ofrecer opciones minimalistas

Cada dominio (SaaS, ERP, banca, salud, e-commerce, reservas, logística) tiene un **estándar profesional** con expectativas mínimas bien establecidas por la industria. Cuando la especificación del proyecto pertenece a un dominio con estándar reconocido, **aplícalo directo como default** — no ofrezcas "opciones minimalistas" que reducen el alcance al mínimo aceptable.

**Cuándo aplicar el estándar directo (sin preguntar):**

- Features cuyo estándar del sector es conocido y estable: notificaciones críticas → dashboard + email (+ push si aplica); reportes fiscales/regulatorios → generar + firmar + enviar + reintentar + trazar; cancelaciones con impacto financiero → cancelar + reembolsar + notificar + registrar motivo; multi-tenant → scope aislado por tenant en cada consulta.
- Cumplimiento normativo obligatorio del dominio (protección de datos, integridad contable, auditoría legal).
- Buenas prácticas técnicas ya universales del stack (tests, migraciones reversibles, transacciones cuando la operación toca varios registros).

**Cuándo SÍ preguntar (no confundir con opciones minimalistas):**

- Preferencias de UX (color, densidad, orden de columnas).
- Reglas de negocio específicas del cliente (política de mora, criterios de crédito, escalado de aprobaciones internas).
- Decisiones arquitectónicas de alto costo con trade-offs reales (multi-tenant N:M vs FK vs schema-per-tenant · self-hosted vs SaaS · elección de proveedor externo).

**Anti-patrones rechazados:**

- Ofrecer "solo dashboard" cuando la industria del dominio espera "dashboard + email + push".
- Ofrecer "solo la interfaz mínima" cuando el estándar espera además exportación, filtro y auditoría.
- Justificar la opción minimalista con "MVP" o "ahorra tiempo" cuando el proyecto es un sistema productivo, no un prototipo desechable.
- Dividir en opciones lo que debería ser un solo default: "¿implementar 4 features del módulo o solo 1?" cuando el estándar profesional del dominio son las 4.

Refuerza [`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada): ante un obstáculo la salida es el arreglo real, no el atajo. **No ofrecer opciones claramente subóptimas es exigencia de esta regla**, no de otra. El estándar del dominio es información del contexto — usarlo como default es tratar al usuario como profesional del sector, no como aprendiz que debe elegir cada micro-detalle.

```
INCORRECTO: "¿las alertas van solo al dashboard o también por email?" — cuando el estándar del sector espera ambos
CORRECTO:   el plan aplica "dashboard + email + push" como default · pregunta solo si hay tradeoff real que no puedas resolver profesionalmente
```


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**Tenía una cita falsa, y se corrigió en esta pasada.** Decía *«refuerza `01·C1` (no ofrecer opciones claramente subóptimas)»*, y `C1` no dice eso: dice «avisa antes de tocar». **Un documento del estándar atribuyendo a una regla algo que no dice.** El análisis del 2026-08-07 lo marcó como cita rota y pidió corregirlo *ya*; llevaba once días.

Ahora refuerza a [`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada) —que sí es lo que glosa— y **declara como suya** la exigencia de no ofrecer opciones subóptimas, que era de ella desde el principio.

**Quedan dos filas:**

- **Fila 9 · son dos exigencias:** aplicar el estándar del dominio como opción por defecto, y no ofrecer alternativas claramente peores. Se cumplen por separado.
- **Fila 10 · no cabe:** 2231 caracteres, siete veces el molde. Lo que sobra es la casuística por sector, que es material de anexo.

Van al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C15 · Al replicar un patrón, replicar la paridad completa

Cuando el usuario dice "hazlo como en X" o "replica el patrón de Y", implica **paridad completa** con el referente, no solo la lógica de datos.

**Qué incluye la paridad completa** (según lo que tenga el referente):

- **UI/UX** — tooltips y textos explicativos, popovers, botón `+` para crear inline, feedback visual, mensajes de éxito y error, atajos de teclado, animaciones y transiciones, layout responsive equivalente.
- **Interacciones** — mismo comportamiento en errores, misma validación cliente/servidor, mismo flujo de creación/edición/eliminación, mismos permisos mínimos.
- **Datos** — no solo el modelo, también sus relaciones consumidas por la UI referente, sus scopes de consulta, sus caches, sus eventos.
- **Tests** — el patrón replicado también replica su cobertura mínima.

**Cuándo pedir aclaración**: si el referente tiene algo que **no aplica** al nuevo caso (por ejemplo, una ayuda contextual con un dato que no existe en el nuevo dominio), preguntar antes de omitirlo — no dar por asumido que "no hace falta".

**Anti-patrón rechazado:** "implementé la lógica igual que X, la UX la vemos después" — divide el patrón en dos entregas parciales que rompen la referencia. La paridad se replica en la misma unidad de trabajo, no en fases sucesivas.

```
INCORRECTO: "hazlo como el módulo de referencia" → solo se implementa el modelo y el
            alta/baja básicos, sin las ayudas ni el alta rápida que el referente sí tiene
CORRECTO:   listar lo que el referente tiene (pantalla, interacciones, pruebas) y
            replicarlo entero · si algo no aplica, preguntar antes de omitir
```

**Encadenamiento:** `C14` (estándar profesional del dominio como default) — la paridad completa es la aplicación puntual de C14 cuando existe un referente concreto en el mismo proyecto.


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.2**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ❌ N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 2 ❌ · 2 N/A.**

**La fila 5 reprobaba y se corrigió en esta pasada.** Nombraba «el módulo Aportes», de un proyecto real, contra [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md). Pasa a «el módulo de referencia», que es lo que la regla quería decir. **No cambia qué exige.**

**Fila 10 · no cabe:** 1441 caracteres.

**Fila 14 ·** su bloque `Encadenamiento` declara relaciones **fuera de las tres formas** que [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) admite. Es un formato propio que aparece en cuatro reglas —`C15`, `C16`, `C18` y [`03·D8`](03-datos.md#d8--distingue-pertenencia-de-autoría-en-el-modelo-de-datos)— y conviene normalizarlo de una vez, no regla por regla.

Lo que queda va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C16 · Re-lee justo antes de editar — nunca sobre contexto viejo

Antes de editar un archivo que el usuario abrió, mostró en el editor, o pudo modificar entre lecturas, verifica el estado actual. Editar sobre contexto viejo sobrescribe en silencio los cambios que no viste — el usuario los pierde sin aviso.

**Siempre aplica cuando:**
- El control de versiones lo da por modificado o sin rastrear (cambios sin confirmar).
- El usuario lo tiene abierto en el editor, o mostró un extracto reciente.
- La sesión se reanudó tras compactación (el estado leído en el turno viejo pudo haber cambiado).
- Han pasado varios turnos u otras ediciones entre la última lectura y la próxima escritura del mismo archivo.

**Cómo:**
1. Pregúntale al control de versiones si ese archivo tiene cambios sin confirmar.
2. Si los tiene, mira **qué** cambió y decide si tu edición sigue valiendo o hay que rehacerla.
3. Relee la sección que vas a tocar — confirma que el texto que vas a reemplazar sigue siendo literalmente el que existe.
4. Solo entonces edita.

```
INCORRECTO: editar sobre una lectura de hace veinte turnos, sin verificar los
            cambios que el usuario haya hecho a mano en ese archivo
CORRECTO:   estado → diferencias (si las hay) → releer el bloque exacto → editar
            contra el texto verificado
```

**Encadenamiento:** `C2` (no inventar, verificar) — C16 es la aplicación puntual de C2 al ciclo de edición.


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.2**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ❌ N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 3 ❌ · 2 N/A.**

**La fila 5 reprobaba y se corrigió en esta pasada**, y era la peor del capítulo: el procedimiento entero estaba escrito en nombres de herramienta —las órdenes de lectura y edición del agente, y dos órdenes del control de versiones—. Ahora dice el paso, no la orden.

**Lo del control de versiones se comprobó antes de tocarlo.** El capítulo `09` se titula **Control de versiones**, no por el nombre de la herramienta, y **ninguna otra regla del cuerpo nombraba una orden concreta**: `C16` era la única. Nombrarlas no era la costumbre de la casa, era su excepción.

- **Fila 10 · no cabe:** 1070 caracteres.
- **Fila 11 · texto prestado**, y lo admite ella misma: su `Encadenamiento` dice que duplica [`C2`](#c2--no-inventes-verifica).
- **Fila 14 · el `Encadenamiento` no es una de las tres formas** de [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md). Lo que corresponde es declarar `(extiende C2)`.

**Que una regla declare por escrito que duplica a otra y siga publicada es lo llamativo**, y sigue igual: el aviso estaba dentro de la propia regla. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C17 · Confirma tu entendimiento antes de ejecutar — solo palabra afirmativa del USUARIO cuenta como aprobación

Ante un pedido que admita más de una lectura razonable, **antes** de mover código, escribir un plan largo o hacer más de un tool call estructural: escribe **1-3 líneas explicando qué interpretaste** y espera OK explícito del usuario. Una mala interpretación cuesta: (a) tu tiempo haciendo lo incorrecto, (b) tiempo del usuario corrigiéndote, (c) riesgo de romper código que funcionaba.

**Aplica siempre cuando:**
- Abres una nueva fase ([`F15`](02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) etapa 1-3): confirma el CORE del alcance antes de escribir `plan_trabajo`.
- Vas a hacer cambios de código no triviales (nuevos métodos, refactor, nuevo componente).
- El pedido admite múltiples lecturas razonables (dos interpretaciones válidas, o el objetivo real depende de un matiz).
- Una mala lectura implicaría retrabajo o romper algo que funcionaba.

**NO aplica a:**
- Trabajo mecánico obvio (grep, listar archivos, leer un log solicitado, correr un comando específico).
- Continuar una fase ya aprobada por el usuario ([`F9`](02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md)).
- Correcciones tipo (rename puntual, ajuste explícito con contexto claro).

**Qué cuenta como aprobación:**
- Palabras afirmativas del USUARIO: "sí", "ok", "hazlo", "adelante", "aprobado", "correcto", "arranque", "hágale", "procede", "dale".
- **NO cuenta:** tu propia pregunta "¿es claro?", "¿confirmas?", "¿procedo?". Tú preguntas, el usuario responde — no al revés.
- **NO cuenta:** silencio, cambio de tema, o respuesta que agrega matiz. Un matiz nuevo obliga a reformular y volver a pedir.

**Formato de la reformulación:**

> "Entiendo que quieres [X con matiz Y]. ¿Confirmas antes de tocar código?"

**Encadenamiento:** balancea `C1` (avisa antes de tocar) con la ejecución fluida — la aprobación previa evita el ciclo *"tocar → corregir → deshacer"*. Encadena con [`F18`](02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) (plan_trabajo derivado de los CA aprobados): la confirmación previa asegura que los CA reflejen el pedido REAL antes de derivar el plan.


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ❌ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ❌ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 4 ❌ · 2 N/A.**

**Cuatro filas.**

- **Fila 9 · son tres exigencias:** confirmar el entendimiento, qué cuenta como aprobación, y en qué formato. Se cumplen por separado.
- **Fila 16 · la lista «NO aplica a» no dice quién autoriza.** Quinta excepción incompleta de la pasada.
- **Fila 12 · sin ejemplo.**
- **Fila 10 · no cabe:** 1796 caracteres.

**La mitad que hay que sacar ya se usa como si fuera regla propia:** *qué cuenta como aprobación* la citan [`02·F4`](02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F9`](02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md) y [`02·F4.4`](02-flujo-de-trabajo/reglas/F4.4-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md). **Es el mismo caso de [`05·E2`](05-errores-y-logging.md#e2--valida-al-entrar-y-aborta-temprano)**, y el mismo cuidado: al partirla hay que llevar esas citas a la mitad nueva.

Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C18 · Auto-sincronización del `CLAUDE.md` con la plantilla central

El `CLAUDE.md` de cada proyecto es una **copia local** de `plantillas/CLAUDE.md.plantilla`. Cuando el estándar mejora la plantilla (un paso nuevo en §3, una sección nueva), el `CLAUDE.md` del proyecto queda **viejo**. Esta regla vive en `base/` **a propósito**: `base/` se carga siempre, así que corre **aunque el `CLAUDE.md` local esté desactualizado** (no puede vivir dentro del propio `CLAUDE.md` — un `CLAUDE.md` viejo no la tendría).

**Al iniciar cada sesión** corre el instalador del estándar, que:

1. **Compara** el `CLAUDE.md` local contra `plantillas/CLAUDE.md.plantilla` (central).
2. Si el local **no existe**, lo genera desde la plantilla con las rutas de la máquina, el nombre y el slug del proyecto y la versión del estándar. Nada de eso es una decisión: no se pregunta.
3. Si la plantilla tiene **secciones o pasos nuevos** que el local no tiene, los **agrega**, y llena los marcadores que hayan quedado sin valor.
4. **Preserva** siempre lo específico del proyecto: rutas, ajustes de §5.1, slug, secciones propias y todo valor ya llenado. Es **aditivo**: nunca sobrescribe, reordena ni borra lo escrito.
5. **Dice qué agregó.** Aplicar sin avisar no es lo mismo que aplicar en silencio: el paso queda listado en la salida del instalador y en el registro de `documentacion/versiones/`.

Así, un cambio a `CLAUDE.md.plantilla` **se propaga solo** a cada proyecto en su próxima sesión — sin edición manual proyecto por proyecto y sin una pregunta cuya única respuesta útil es "sí".

```
INCORRECTO: se mejora CLAUDE.md.plantilla · el agente pregunta en cada proyecto si aplica
            lo que el estándar ya decidió, y hasta que no contesten queda viejo
CORRECTO:   se mejora la plantilla una vez · cada proyecto lo aplica al arrancar
            (aditivo, preservando lo propio) y reporta qué agregó
```

**Encadenamiento:** complementa el paso de arranque de `CLAUDE.md §3` (que cubre los 4 archivos de `.agente/`); `C18` cubre el **propio `CLAUDE.md`** y vive en `base/` porque el `CLAUDE.md` local puede estar viejo.


---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ❌ N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 2 ❌ · 2 N/A.**

**Fila 10 · no cabe: 533 caracteres**, y su `Encadenamiento` queda fuera de las tres formas de [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), como en `C15` y `C16`.

Está clasificada y con validador escrito —`sesion.py`—, así que la fila **18** pasa con programa detrás.

El análisis del 2026-08-07 anotaba algo que sigue valiendo: **el porqué de que esta regla viva en `base/` es razonamiento y va a `notas/`**, no dentro de la regla. Es parte de lo que la hace no caber.

Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C19 · Escribe la memoria del agente dentro del repositorio del proyecto

Lo que el agente deba recordar entre sesiones —cómo quiere el usuario que se trabaje— va a `historico-chat/memory/` del proyecto, **un archivo por recuerdo**, y el almacén de la herramienta queda **vacío**: lo que aparezca ahí se mueve.

No es la memoria por señales ([`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)), que guarda lo que aprendió el proyecto.

```
INCORRECTO: guardar el recuerdo en el almacén de la herramienta — o dejar allá
            un puntero al archivo del repositorio
CORRECTO:   el recuerdo entero en `historico-chat/memory/<nombre>.md`, versionado,
            y el almacén de la herramienta vacío
```


---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.5**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 533 caracteres a 317**, para un molde de 320. Se fue el porqué —que lo no versionado no se revisa, no viaja y se pierde al clonar—, que ya está dicho en el índice de la memoria.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C20 · La palabra de otro idioma se traduce, y si no se puede, se explica

Todo término que no esté en el idioma del proyecto se escribe traducido (extiende [`C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto)). El que no tenga traducción usada se deja tal cual y se explica **la primera vez que aparece**, en una frase.

```
INCORRECTO: "sin spec acordada no hay código"
CORRECTO:   "sin especificación acordada no hay código"
CORRECTO:   "se guarda en formato JSON, que es texto que un programa lee como
            datos" — se queda en inglés porque no tiene traducción usada
```

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v10.0.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Que el término sin traducción se deje en su idioma no es un permiso para incumplir, es hasta dónde llega la exigencia. La fila **2** se revisó contra [`C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto), que exige el idioma y no dice nada de los términos que no lo tienen; son dos cosas que se cumplen por separado, así que son dos reglas. La fila **5** no nombra ninguna tecnología: "el idioma del proyecto" lo declara la capa 3.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C21 · Pide el dato que falte antes de arrancar

Un pedido de trabajo declara cuatro cosas: **sobre qué** (el archivo, la carpeta o el tema, con nombre), **qué quiere** (responder, opinar o ejecutar), **qué debe quedar hecho** y **qué no se toca**. El mensaje que solo pide información declara las dos primeras. Si falta alguna, pregunta por esa, en una línea, y no toques nada mientras esperas; nunca la supongas (extiende [`C7`](01-conducta.md#c7--ante-dos-lecturas-pregunta)).

```
INCORRECTO: "arregle eso" → el agente deduce a qué apunta "eso" y edita
CORRECTO:   "¿sobre qué archivo?" y no toca nada hasta la respuesta
```

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v11.0.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción; el pedido que solo busca información no es un caso exento, es el mismo pedido con dos campos en vez de cuatro. La fila **2** se revisó contra [`C7`](01-conducta.md#c7--ante-dos-lecturas-pregunta) y [`C17`](01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación), que cubren el pedido que admite **dos lecturas**; este cubre el que no trae el dato, donde no hay dos lecturas sino ninguna. La fila **9** pide una sola exigencia, y la exigencia es una: no arrancar sin el dato. Los cuatro campos no son cuatro órdenes, son qué cuenta como pedido completo. La fila **17** se resolvió releyendo el capítulo: [`C4`](01-conducta.md#c4--no-decidas-por-tu-cuenta) prohíbe decidir por cuenta propia y esta dice qué hacer en su lugar cuando lo que falta es un dato del pedido.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C22 · Ante un comando rechazado, corrige el comando — la orden sigue en pie

Cuando el usuario rechaza una llamada a herramienta, rechaza **cómo** el agente iba a hacerlo, no lo que pidió. El agente corrige la llamada y vuelve a intentar, o pregunta en una línea qué cambiarle; no da la orden por retirada ni la reemplaza por una explicación. La orden solo la retira el usuario, diciéndolo (extiende [`C17`](01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación)).

```
INCORRECTO: se rechaza el comando que renombra el archivo → el agente da el
            encargo por cancelado y responde explicando por qué no lo hizo
CORRECTO:   "se rechazó el comando; ¿le cambio el resumen y lo vuelvo a correr?"
            — y si no hay nada que cambiarle, lo reintenta
```

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v12.0.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción; que el agente pueda preguntar en vez de reintentar no es un caso exento, son las dos formas de cumplir lo mismo. La fila **2** se buscó por concepto y se leyó el capítulo entero: [`C1`](01-conducta.md#c1--avisa-antes-de-tocar) y [`C17`](01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación) fijan qué cuenta como **aprobación**, y ninguna dice qué significa un rechazo; son cosas distintas y se cumplen por separado. La fila **9** pide una sola exigencia, y es una: no dar por retirado lo que el usuario no retiró. La fila **17** no choca con `C1`: esta no autoriza a seguir sin el sí, dice hasta dónde llega el no.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## C23 · Busca en el repositorio antes de preguntar

Lo ya decidido no se pregunta otra vez. Antes de pedir una decisión se busca si está escrita —la historia y su §9, la épica, el resumen de sesión, el histórico, la memoria— y si está, se sigue **citando dónde** —o se muestra, si contradice lo pedido—. Si no, se pregunta diciendo dónde se buscó (extiende [`C7`](01-conducta.md#c7--ante-dos-lecturas-pregunta)).

```
INCORRECTO: "¿en qué orden trabajo estas dos historias?" — y la §9 de una de
            ellas ya declaraba que depende de la otra
CORRECTO:   "voy por HU-009 primero: la §9 de HU-008 la declara como
            dependencia con impacto alto"
```

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**El orden de búsqueda se recortó del cuerpo y no se perdió**, que es lo que la fila 10 pide cuando algo no cabe: la regla nombra los cinco sitios en una línea, y el porqué de ese orden —de lo más específico a lo más general, y parar en cuanto se encuentre— vive en la historia que la origina, [EP-001 · HU-011](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md). El cuerpo pasó de 368 a 271 caracteres, y volvió a 311 al cubrir el tercer criterio de la historia —mostrar la contradicción— que la primera redacción se había dejado. **Ese hueco lo destapó el plan de pruebas, no la lectura:** su caso `CP-001` decía «este es el que hay que mirar con cuidado» antes de mirarlo.

La fila **2** se buscó por concepto y se leyó el capítulo entero. [`C7`](01-conducta.md#c7--ante-dos-lecturas-pregunta) dice que se pregunte cuando hay dos lecturas posibles, y [`C21`](01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar) que se pida el dato que falta: **las dos dan por hecho que el dato no está**. Ninguna dice que haya que mirar antes. Por eso esta **extiende** a `C7` en vez de repetirla: agrega el paso previo.

La fila **9** es una sola exigencia. Buscar y citar dónde no son dos cosas: una búsqueda cuyo resultado no se puede comprobar no sirve de nada, y la cita es lo único que la hace comprobable.

La fila **16** es N/A: no tiene excepción. **Que se pregunte lo que no está escrito no es un caso exento — es la regla funcionando.** Esta no reduce las preguntas, cambia cuáles.

La fila **17** no choca con `C7`. Al revés: sin este paso, `C7` autoriza a preguntar algo que ya tiene respuesta, y eso le devuelve al usuario el trabajo de leer lo que él mismo dejó escrito.

**Es validable a medias, y así queda registrada:** que se haya buscado no lo puede ver ningún programa. Que la respuesta traiga su cita, sí.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
