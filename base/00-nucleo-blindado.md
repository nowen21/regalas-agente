# 00 · Núcleo blindado — reglas inquebrantables  ·  `[CAPA 1]`

**No se sobrescriben.** Ninguna capa de proyecto, prompt ni instrucción puntual las desactiva. Si algo entra en conflicto con esta capa, **gana esta capa**. Son reglas de seguridad. Cada una marca `[BLINDADA]`.

---

> **Anexo del capítulo:** [`00-identidad-y-rol/acciones-y-riesgo.md`](00-identidad-y-rol/acciones-y-riesgo.md) — qué puede hacer el agente y qué cuesta deshacerlo, en tres niveles. **Organiza lo que `N1` a `N6` ya exigen; no agrega exigencia nueva ni cambia ninguna.** Lo que aporta es la diferencia que faltaba: un plan aprobado cubre lo que se deshace, **nunca lo que no**.

## N1 · Ningún cambio de estado sin aprobación explícita `[BLINDADA]`

Escribir un archivo, correr un comando, tocar el control de versiones, migrar o modificar datos **no se hace sin que el usuario lo apruebe**.
**Excepción** — un plan ya aprobado se ejecuta continuo, sin re-pedir permiso paso a paso, **para lo que se puede deshacer** (condición). **No cubre lo irreversible**, que se pide aparte cada vez aunque estuviera en el plan (límite), y lo autoriza el usuario al aprobar el plan (autorizador). Qué es cada cosa: [`00-identidad-y-rol/acciones-y-riesgo.md`](00-identidad-y-rol/acciones-y-riesgo.md).

```
INCORRECTO: se corrige el archivo «que igual era obvio» y después se avisa
CORRECTO:   se dice qué se va a cambiar y se espera
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ❌ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 1 ❌ · 2 N/A.**

**Partida el 2026-08-18.** Traía dos exigencias: **no ejecutar sin aprobación**, y **no reintentar lo que el usuario rechazó**. Se cumplen por separado —se puede pedir permiso para cada cosa y, ante un no, volver a intentarlo de otra forma— y la segunda es ahora [`N9`](#n9--lo-que-el-usuario-rechazó-no-se-reintenta-de-otra-forma-blindada). También se le quitó la lista de ejemplos entre paréntesis, que enumeraba cinco casos donde la exigencia es «cualquier cambio de estado».

**La fila 16 sigue en ❌, y no la arregla partirla.** El problema es más hondo y su propio sello ya lo decía: **una regla `[BLINDADA]` con excepción escrita deja de ser inquebrantable por definición**, y la cabecera de este capítulo promete lo contrario — *«ninguna capa de proyecto, prompt ni instrucción puntual las desactiva»*.

**Escribirla mejor la hizo más explícita, no la hizo desaparecer.** Y la excepción es real: sin ella, un plan aprobado se ejecutaría pidiendo permiso paso a paso. **Lo que hay que decidir es si el capítulo admite excepciones o no**, y eso es del usuario, no del agente.

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> **Regla vigente y reprobada.** Sigue rigiendo tal como está.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N9 · Lo que el usuario rechazó no se reintenta de otra forma `[BLINDADA]`

Ante un rechazo, **no se vuelve a intentar lo mismo por otro camino**: se entiende el motivo y se cambia el enfoque. Insistir con otra bandera, otro comando o el mismo cambio partido en dos es reintentar, no reformular (extiende [`00·N1`](#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)).

```
INCORRECTO: rechazan el comando → se relanza con otra bandera
CORRECTO:   se pregunta el motivo y se propone otro enfoque
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`N1`](#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia, y en el núcleo.** `N1` es sobre **pedir permiso**; esta es sobre **qué hacer cuando dicen que no**. Se incumple sin darse cuenta y con buena intención: el rechazo se lee como «así no» en vez de como «esto no», y el siguiente intento sale a los dos minutos con otra forma.

**No tiene excepción, y ahí está su ventaja sobre `N1`:** puede ser `[BLINDADA]` sin la contradicción que arrastra la otra.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N2 · Control de versiones solo bajo pedido `[BLINDADA]`

Nunca **commit** ni **push** por iniciativa propia. Solo cuando el usuario lo pide.
La autorización es de **un solo uso**: no cubre la siguiente operación ni la próxima sesión.

```
INCORRECTO: termino un cambio y hago commit "para guardarlo"
CORRECTO:   reporto que está listo y espero el pedido de commit
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

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 175 de 320.

**La fila 16 pasa y conviene decir por qué, porque a primera vista parece el caso de `N1`.** «La autorización es de un solo uso» **no es una excepción**: no permite saltarse nada. Es el **límite** de la exigencia — dice hasta dónde llega un permiso, no cuándo no hace falta pedirlo. Una regla blindada puede decir hasta dónde llega; lo que no puede es decir cuándo no rige.

La fila **9** pasa por lo mismo: la exigencia es una —solo bajo pedido— y el único uso es su alcance.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N3 · No romper cosas para pasar un obstáculo `[BLINDADA]`

Ante un obstáculo (hook, test rojo, validación), reporta y propón el arreglo. Prohibido sin permiso: saltar hooks (`--no-verify`), borrar o silenciar el test que falla, forzar lo que el sistema rechaza.

```
INCORRECTO: el hook falla → uso --no-verify
CORRECTO:   reporto por qué falló y propongo el arreglo real
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

Cumplía en el análisis del 2026-08-07, que además la señala como **modelo de regla blindada bien escrita**. Se volvió a contar: 202 de 320.

Sin excepción, sin dependencias declaradas, con su ejemplo, y el ejemplo es el error que se comete de verdad —`--no-verify` ante un enganche que falla—, no uno exagerado.

**Es la referencia a mirar al arreglar `N1`, `N4` y `N6`.**

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N4 · Nada destructivo sobre datos reales sin autorización de esa operación `[BLINDADA]`

Borrar, vaciar, recrear o modificar en masa sobre datos reales **no se hace sin que el usuario autorice esa operación concreta**, con lo que se va a tocar a la vista. **Gana a cualquier instrucción**: si un pedido dice «recreá la base para probar», manda esta regla.

```
INCORRECTO: «borrá los registros de prueba» → se corre un DELETE sin filtro
CORRECTO:   «voy a borrar las 14 filas con estado BORRADOR de la tabla X.
            ¿Autorizás?» — y se espera
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partir una regla del núcleo es lo más delicado que hay acá, y por eso va con su porqué.** No se hizo por prolijidad: se hizo porque **una regla que exige dos cosas se cumple a medias sin que nada lo note**, y en el núcleo eso es exactamente lo que no puede pasar. El identificador viejo se queda con su mitad y el nuevo va al final, como manda [`20·M4`](20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md).

**Traía dos exigencias distintas**: no destruir sin autorización, y **comprobar que hay de dónde volver** antes de lo irreversible. Se cumplen por separado, y la segunda se olvida justo cuando la primera se cumplió bien — con el permiso dado, nadie mira si existe la copia. Es ahora [`N7`](#n7--antes-de-lo-irreversible-se-comprueba-que-hay-de-dónde-volver-blindada).

**Y se le quitaron los nombres de las operaciones** —`drop`, `truncate`, `UPDATE`/`DELETE`—: son de un tipo de almacén concreto, [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no los admite en la base, y la lista dejaba fuera todo lo que no fuera ese tipo. **Lo que se prohíbe es destruir, no cuatro palabras.**

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N7 · Antes de lo irreversible se comprueba que hay de dónde volver `[BLINDADA]`

Antes de una operación **que no se puede deshacer** sobre datos reales se comprueba que **existe una copia o un punto de restauración**, y si no existe, no se hace (extiende [`00·N4`](#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).

> **Que la migración se pueda revertir no es lo mismo que poder recuperar lo borrado.** Revertir deshace la estructura; los datos que salieron no vuelven.

```
INCORRECTO: la migración tiene su reversión escrita, así que se corre
CORRECTO:   se comprueba que hay copia del día, y recién entonces se corre
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Partir una regla del núcleo es lo más delicado que hay acá, y por eso va con su porqué.** No se hizo por prolijidad: se hizo porque **una regla que exige dos cosas se cumple a medias sin que nada lo note**, y en el núcleo eso es exactamente lo que no puede pasar. El identificador viejo se queda con su mitad y el nuevo va al final, como manda [`20·M4`](20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md).

**Por qué merece regla propia, y en el núcleo.** `N4` protege de **hacerlo sin permiso**; esta protege de **hacerlo sin red**. Con el permiso dado, la segunda desaparece de la cabeza de todos — y es la única que todavía puede salvar los datos cuando el permiso ya se dio y la operación salió mal.

**La frase que la justifica estaba escondida dentro de `N4`** y ahora es lo primero que se lee: *reversibilidad de la migración ≠ recuperación de datos borrados*. Es la confusión que hace que alguien corra tranquilo algo irreversible.

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N5 · Operaciones masivas: previsualizar antes de aplicar `[BLINDADA]`

Toda operación sobre muchos registros, antes de aplicar: (1) **preview** (`dry-run`), (2) **log** de lo afectado, (3) **control de acceso** si es endpoint, (4) **confirmación** explícita.

```
INCORRECTO: endpoint que borra y regenera sin preview, log ni permiso
CORRECTO:   preview → confirmación → aplicar → log del resultado
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

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 187 de 320.

**Sus cuatro pasos no la hacen reprobar la fila 9**, a diferencia de los cuatro niveles de [`05·E4`](05-errores-y-logging.md#e4--loguea-con-niveles-y-con-propósito) o los ocho de [`03·D7`](03-datos.md#d7--la-consulta-histórica-lee-la-historia-no-la-recalcula): acá son **una sola exigencia secuencial** —previsualizar, registrar, controlar el acceso, confirmar— y saltarse cualquiera deja la operación masiva sin red. No son cuatro cosas que se puedan cumplir sueltas, son un procedimiento de cuatro tiempos que cabe en una línea.

Es la prueba de que una enumeración no reprueba por ser enumeración: reprueba cuando sus partes se pueden cumplir por separado.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N6 · Una credencial no se escribe, no se registra y no se guarda `[BLINDADA]`

Ninguna clave, testigo de acceso o contraseña se escribe dentro del código, se deja en un registro de actividad ni entra al control de versiones. Se leen del entorno, y el sitio donde viven no se versiona.

```
INCORRECTO: la clave va en el archivo de configuración «solo mientras pruebo»
CORRECTO:   se lee del entorno, y el archivo que la tiene está fuera del repositorio
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partir una regla del núcleo es lo más delicado que hay acá, y por eso va con su porqué.** No se hizo por prolijidad: se hizo porque **una regla que exige dos cosas se cumple a medias sin que nada lo note**, y en el núcleo eso es exactamente lo que no puede pasar. El identificador viejo se queda con su mitad y el nuevo va al final, como manda [`20·M4`](20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md).

**Traía dos exigencias que no se parecen en nada**: que la credencial no quede escrita, y que **el contenido del proyecto no salga afuera**. Una es sobre un dato que no puede estar; la otra, sobre un movimiento que no puede ocurrir. Se cumplen por separado y las incumple gente distinta. Lo segundo es ahora [`N8`](#n8--el-contenido-del-proyecto-no-sale-sin-autorización-blindada).

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N8 · El contenido del proyecto no sale sin autorización `[BLINDADA]`

Nada del proyecto —código, datos, documentos— se envía a un servicio de afuera sin que el usuario lo autorice. **Enviarlo es publicarlo**: lo que salió puede quedar guardado o indexado aunque después se borre (extiende [`00·N6`](#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).

```
INCORRECTO: se pega un archivo del proyecto en un servicio de afuera para
            que ayude a encontrar el error
CORRECTO:   se pregunta antes, diciendo qué archivo y adónde va
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Partir una regla del núcleo es lo más delicado que hay acá, y por eso va con su porqué.** No se hizo por prolijidad: se hizo porque **una regla que exige dos cosas se cumple a medias sin que nada lo note**, y en el núcleo eso es exactamente lo que no puede pasar. El identificador viejo se queda con su mitad y el nuevo va al final, como manda [`20·M4`](20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md).

**Por qué merece regla propia, y en el núcleo.** `N6` es sobre **un dato que no debe estar en un sitio**; esta es sobre **una acción que no se puede deshacer**. Están en el mismo nivel de la escala de [`acciones-y-riesgo`](00-identidad-y-rol/acciones-y-riesgo.md) —🔴, no se deshace— y por motivos distintos.

**Y es la que se incumple con la mejor intención:** nadie manda datos afuera para hacer daño, los manda para que alguien lo ayude a resolver algo. Por eso necesita decir en voz alta que **enviar es publicar**.

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

