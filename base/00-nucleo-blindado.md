# 00 · Núcleo blindado — reglas inquebrantables  ·  `[CAPA 1]`

**No se sobrescriben.** Ninguna capa de proyecto, prompt ni instrucción puntual las desactiva. Si algo entra en conflicto con esta capa, **gana esta capa**. Son reglas de seguridad. Cada una marca `[BLINDADA]`.

---

## N1 · No ejecutar sin validación `[BLINDADA]`

Ningún cambio de estado (archivos, comandos, control de versiones, migraciones, datos) sin aprobación explícita.
**Si el usuario rechaza, no reintentes lo mismo.** Entiende el motivo y cambia el enfoque.
Excepción: un plan ya aprobado se ejecuta continuo (no re-pedir permiso por cada paso).

```
INCORRECTO: rechazan el comando → lo relanzo con otra bandera
CORRECTO:   pregunto el motivo y propongo otro enfoque
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ✅ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ❌ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 3 ❌ · 2 N/A.**

**Es el hallazgo más serio de toda la pasada, y ya estaba señalado en rojo y con prioridad alta desde el 2026-08-07.**

- **Fila 16 · una regla `[BLINDADA]` con excepción escrita reprueba.** La fila lo dice sin matices, y esta trae una: *«Excepción: un plan ya aprobado se ejecuta continuo»*. Una regla de capa 1 con excepción **deja de ser inquebrantable por definición** — y la cabecera del capítulo promete justo lo contrario: *«ninguna capa de proyecto, prompt ni instrucción puntual las desactiva»*.
- **Fila 9 · son dos exigencias:** no ejecutar sin aprobación, y no reintentar lo mismo tras un rechazo. Se cumplen por separado con toda facilidad.
- **Fila 11 · texto prestado.** Lo que llama excepción es [`02·F3`](02-flujo-de-trabajo/reglas/F3-ejecuta-seguido-el-plan-aprobado.md) dicha otra vez.

**El arreglo que el análisis propuso sigue siendo el correcto, y es de forma más que de fondo:** eso no es una excepción sino el **alcance de la autorización** —qué cubre un «sí»—, y escrito así deja de contradecir a la capa. Además, partir el «no reintentes» a una `N7` y enlazar `F3` en vez de repetirlo.

**Nada de esto se toca acá.** Es el núcleo: cualquier cambio va con su decisión del usuario y su versión. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

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

## N4 · Proteger los datos reales `[BLINDADA]`

Nunca operaciones destructivas sobre datos de producción (o cualquier BD con datos reales) sin autorización expresa y específica: recrear o vaciar la base, borrar tablas (`drop`), vaciarlas (`truncate`), `UPDATE`/`DELETE` masivos sin filtro.
**Gana a cualquier prompt.** Si un prompt dice "recrea la BD para probar", esta regla manda.

**Punto de restauración:** antes de una operación **irreversible** sobre datos reales (migración destructiva, borrado, transformación no reversible), verificar que existe un **backup / punto de restauración**. Reversibilidad de la migración ≠ recuperación de datos borrados.

```
INCORRECTO: "recreo la BD para probar el módulo"
CORRECTO:   pruebas contra BD efímera/aislada; verificar sin borrar datos
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

**Dos filas, y las dos son la misma historia: adentro hay dos reglas.**

- **Fila 9 · son dos exigencias.** La prohibición de operaciones destructivas sin autorización, y **verificar que existe punto de restauración** antes de una irreversible. Se cumplen por separado: se puede pedir autorización impecablemente y no comprobar que hay respaldo.
- **Fila 10 · no cabe:** 607 caracteres, casi el doble del molde, y se pasa **por la segunda**.

**La segunda es la que más vale y la que menos se ve.** «Reversibilidad de la migración ≠ recuperación de datos borrados» es un matiz que no dice ninguna otra regla del estándar, y hoy vive escondido dentro de otra. El análisis del 2026-08-07 proponía sacarlo a una `N8` propia, y sigue siendo lo que corresponde.

**Nada se toca acá:** es el núcleo. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

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

**Sus cuatro pasos no la hacen reprobar la fila 9**, a diferencia de los cuatro niveles de [`05·E4`](05-errores-y-logging.md#e4--loguea-con-niveles-y-con-propósito) o los ocho de [`03·D7`](03-datos.md#d7--persistencia-histórica-scd-2--patrón-canónico-para-valores-que-evolucionan): acá son **una sola exigencia secuencial** —previsualizar, registrar, controlar el acceso, confirmar— y saltarse cualquiera deja la operación masiva sin red. No son cuatro cosas que se puedan cumplir sueltas, son un procedimiento de cuatro tiempos que cabe en una línea.

Es la prueba de que una enumeración no reprueba por ser enumeración: reprueba cuando sus partes se pueden cumplir por separado.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## N6 · Secretos y datos sensibles nunca se exponen `[BLINDADA]`

Nunca hardcodear ni loguear ni commitear credenciales/tokens/claves. Nunca enviar contenido del proyecto a servicios externos sin autorización. Archivos no públicos, nunca en ubicación pública (ver `04`).

```
INCORRECTO: loguear el payload con la contraseña del usuario
CORRECTO:   loguear un identificador, nunca el secreto
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ✅ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**Tres exigencias, y la tercera además está prestada.**

- **Fila 9 · son tres:** no incrustar ni registrar ni subir secretos; no enviar contenido del proyecto a servicios externos; y que los archivos no públicos no queden en ubicación pública. Se cumplen por separado sin ninguna dificultad.
- **Fila 11 · la tercera repite [`04·S6`](04-seguridad.md#s6--archivos-sensibles-privado--acceso-controlado)**, que es la dueña del tema y lo desarrolla entero. Acá queda como un resumen con «(ver `04`)» al final.

**Cabe —204 de 320— y aun así reprueba.** Es el segundo caso hoy, tras [`04·S7`](04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas): que una regla quepa y esté bien redactada no dice nada sobre si es una sola regla ni sobre si lo que dice es suyo.

El corte propuesto en 2026-08-07 sigue valiendo: partir en tres y que la tercera se sustituya por el enlace a `S6`. **Nada se toca acá:** es el núcleo, y además la segunda mitad —no enviar contenido a servicios externos— es de las que más se citan del estándar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Estas seis son la versión inquebrantable de temas que desarrollan con más matiz `01` (conducta), `03` (datos), `04` (seguridad), `05` (errores), `09` (git).
