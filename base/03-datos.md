# 03 · Datos y persistencia  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-016](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-016-el-capitulo-03-datos-y-persistencia/HU-016-el-capitulo-03-datos-y-persistencia.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

Diseño y cambio del almacenamiento: esquema, migraciones, catálogos. La capa 3 declara los nombres concretos (motor, prefijos, tabla de catálogo, trait de auditoría).

---

## D1 · La tabla nueva nace normalizada

Un dato no se repite ni se guarda en montón: nada de columnas que contienen varios valores, nada de copiar atributos del padre, y nada de valores fijos incrustados en el tipo de la columna, que van a catálogo ([`D4`](#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)). Lo uno a muchos va en tabla hija; lo muchos a muchos, en una que las une.

```
INCORRECTO: una columna «etiquetas» con los valores separados por comas
CORRECTO:   una tabla de etiquetas y otra que la une con su dueño
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `03`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Partida el 2026-08-18, y eran tres.** Su cuerpo tenía tres párrafos en negrita —normalización, auditoría, integridad en el almacén— y **son tres exigencias que se cumplen por separado**: una tabla puede estar perfectamente normalizada y no llevar ninguna columna de auditoría, o llevarlas y no tener una sola restricción. Nacen [`D10`](#d10--toda-tabla-guarda-quién-la-tocó-y-cuándo) y [`D11`](#d11--la-integridad-vive-en-el-almacén-no-solo-en-la-aplicación). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D10 · Toda tabla guarda quién la tocó y cuándo

Cada tabla lleva **quién creó, quién editó por última vez, y cuándo** cada cosa. Las tablas de las que dependen cuentas, obligaciones o registros legales guardan además la baja como marca, no como borrado.

```
INCORRECTO: el registro cambió y nadie puede decir quién ni cuándo
CORRECTO:   la fila dice quién la creó, quién la tocó por última vez y en qué momento
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.24.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`D1`](#d1--la-tabla-nueva-nace-normalizada).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** La normalización es sobre **cómo se guarda el dato**; esta es sobre **qué se guarda además del dato**. Se olvida sola: nadie deja una tabla mal normalizada sin notarlo, y casi todos dejan una sin auditoría.

**La tabla que solo une dos tablas queda fuera**: no tiene contenido propio del que responder.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D11 · La integridad vive en el almacén, no solo en la aplicación

Las relaciones, la unicidad conceptual y los índices de lo que se filtra se declaran **en el propio almacén**. La aplicación puede comprobarlo también, pero no en su lugar: lo que solo vive en el código no protege a los datos que entran por otro camino.

```
INCORRECTO: la unicidad del documento se valida en el formulario y nada más
CORRECTO:   además, el almacén la declara y la rechaza aunque entre por otro lado
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.24.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`D1`](#d1--la-tabla-nueva-nace-normalizada).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** Es la que sostiene a [`03·D9`](#d9--dos-operaciones-simultáneas-no-se-pisan): sin la restricción en el almacén, dos procesos simultáneos insertan el mismo registro por más que la aplicación lo compruebe. Y se incumple con la mejor intención — *«ya lo valido yo»*.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D2 · Cada cambio de esquema es una migración reversible

Migración independiente, con aplicación y reversión funcionales. **Nunca modifiques una migración ya ejecutada** — crea una nueva. Documenta qué y por qué. Correrla contra datos reales requiere autorización ([`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).

```
INCORRECTO: falta una columna, así que se edita la migración que ya corrió en
            producción → las máquinas que ya la aplicaron nunca la ven
CORRECTO:   una migración nueva que agrega la columna; la vieja no se toca
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo, y el análisis del 2026-08-07 explicaba por qué hacía falta — *«editar una migración ya ejecutada es error frecuente»*. **No cambia qué exige la regla.**

Cabe de sobra: 217 de 320. **Es la única del capítulo que cabe**, y por eso conviene mirarla al reescribir las demás.

Está clasificada y con validador escrito —`migraciones.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D3 · Migraciones retrocompatibles con los datos existentes

Preservar datos y comportamiento sin intervención manual.

- Columna obligatoria nueva → con **default** equivalente al comportamiento previo.
- Enum → catálogo: crearlo, poblar mapeando cada valor viejo, y recién ahí exigirla.
- **Nunca borres datos históricos**; si la reversión no los recupera, documéntalo.

```
INCORRECTO: columna obligatoria sin default → falla si ya hay filas
CORRECTO:   default equivalente al comportamiento previo, luego endurecer
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.5**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 378 caracteres a 306**, para un molde de 320. Se apretó la redacción de los tres puntos. **Ninguno se fue**: los tres siguen, y el tercero conserva su exigencia de documentar cuando la reversión no recupera.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D4 · Lo que puede cambiar por decisión de alguien va a catálogo

Nada que pueda cambiar por decisión del negocio, de la ley o de la operación se escribe dentro del código: umbrales, listas de valores válidos, textos editables, interruptores de comportamiento. Va a un **catálogo consultable**, y si hace falta escribir uno, **primero se crea el catálogo**.

```
INCORRECTO: el descuento máximo es un número escrito en la condición
CORRECTO:   el descuento máximo se consulta del catálogo, y negocio lo cambia sin tocar código
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.24.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Decía dos cosas: **qué va al catálogo**, y **cómo se usa** el que ya existe — bifurcar por código y no por identificador. **Se cumplen por separado**, y la segunda es más traicionera: se puede tener todo en catálogos y aun así romper el sistema al pasarlo a otro entorno, porque el código decidía comparando identificadores. Es ahora [`D12`](#d12--el-código-decide-por-el-código-del-catálogo-no-por-su-identificador). Lo que quedó fuera —guardar los interruptores junto al catálogo, marcar como protegido lo que el código referencia, guardar en memoria lo que se consulta seguido— era **cómo hacerlo bien, no una exigencia**. Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D12 · El código decide por el código del catálogo, no por su identificador

Cuando el programa se bifurca según un valor del catálogo, compara **el código que significa algo** —`PENDIENTE`, `ANULADO`—, nunca el número que le tocó en la tabla: ese número cambia entre entornos y la comparación deja de valer sin avisar (extiende [`03·D4`](#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)).

```
INCORRECTO: si el estado es 3, no dejar editar
CORRECTO:   si el estado es «ANULADO», no dejar editar
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.24.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`D4`](#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `D4` es sobre **dónde vive** el valor; esta es sobre **cómo se lo mira**. Y es la que falla en producción: en el entorno donde se programó, el identificador 3 era el correcto.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D5 · Con la BD desplegada, la validación nueva va en la app

Si la base ya está en producción su estructura es un contrato: la validación nueva que no encaje limpio —limita el motor, choca con datos viejos, migrar sale caro— **no se fuerza ahí**, va al servicio, y ese servicio lleva **prueba dedicada**: sin ella se degrada en silencio. La migración anota por qué.
**Excepción** — en diseño desde cero el invariante sí va al esquema (condición); no vale con la base desplegada (límite) y lo decide quien modela (autorizador).
```
INCORRECTO: la migración falla contra los datos → editar la BD a la fuerza
CORRECTO:   validación en el servicio + prueba + nota en la migración
```

---

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.12.1**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.**

**Dos filas, y las dos ya estaban señaladas.**

- **Fila 16 · la excepción está incompleta.** «No aplica en diseño desde cero» es condición, y le faltan el límite y quién autoriza.
- **Fila 10 · no cabe:** 640 caracteres, el doble del molde.

Es la tercera excepción sin autorizador que aparece hoy —con [`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba) y `D4`—. **Conviene revisarlas juntas**, porque la pregunta de fondo es la misma: quién concede el permiso de no cumplir.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D6 · La operación repetida no duplica su efecto

Una operación que llega **dos veces** —doble clic, reintento, mensaje repetido— produce el mismo resultado que si hubiera llegado una: se identifica con una clave propia, o se comprueba el estado antes de aplicarla.

```
INCORRECTO: el usuario hace doble clic y quedan dos pagos idénticos
CORRECTO:   el segundo intento reconoce que ese pago ya se aplicó y no hace nada
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.23.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Su título decía dos cosas —*«concurrencia **e** idempotencia»*— y eran dos: que repetir no duplique, y que dos operaciones simultáneas no se pisen. **Se cumplen por separado**, y son problemas distintos: una es el mismo actor dos veces, la otra son dos actores a la vez. Lo segundo es ahora [`D9`](#d9--dos-operaciones-simultáneas-no-se-pisan). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D9 · Dos operaciones simultáneas no se pisan

Cuando dos procesos pueden tocar el mismo dato a la vez, la integridad se **protege en el almacén**: el valor compartido se actualiza de forma atómica o revalidando la versión al guardar, y la unicidad la garantiza una restricción del propio almacén, porque comprobarla antes de insertar no alcanza.

```
INCORRECTO: se lee el saldo, se resta en memoria y se guarda → dos ventas
            simultáneas dejan el saldo como si hubiera habido una
CORRECTO:   el descuento se hace en una sola operación atómica, o se revalida
            la versión al guardar y el segundo reintenta
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `03`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Nace el 2026-08-18 de partir [`D6`](#d6--la-operación-repetida-no-duplica-su-efecto).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `D6` es sobre **el mismo actor dos veces**; esta es sobre **dos actores a la vez**. La segunda es la que no se ve al probar: en una máquina sola nunca ocurre, y aparece el día que hay dos usuarios.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D7 · La consulta histórica lee la historia, no la recalcula

Cuando un valor **cambia con el tiempo** y alguien va a preguntar cómo estaba en una fecha, ese estado se **guarda cuando ocurre**, no se reconstruye después sumando lo que hay vivo hoy: reconstruir solo vale si el pasado no se toca.
Cómo se guarda y qué se prueba: [`notas/como-se-guarda-la-historia-de-un-valor.md`](../notas/como-se-guarda-la-historia-de-un-valor.md).
```
INCORRECTO: «el total de marzo» se calcula sumando lo que hoy está vivo
CORRECTO:   se lee el tramo que estaba vigente en marzo, con lo que valía entonces
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.26.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Reescrita el 2026-08-18, y no se partió: no eran dos exigencias.** Medía **3 839 caracteres** contra los 320 del molde —doce veces— porque **era un patrón entero metido dentro de una regla**: la tabla de tramos, la migración inicial, el aviso, quién lo escucha, la consulta, la interfaz, las pruebas obligatorias y la alternativa por volumen.

**La exigencia real cabía en tres líneas**, y es una sola: el estado se guarda cuando ocurre, no se recalcula después. Todo lo demás es **cómo**, y se fue a [`notas/`](../notas/como-se-guarda-la-historia-de-un-valor.md) — que es lo que la fila 10 manda hacer con lo que no cabe.

**También se fue el nombre del patrón del título.** Nombrar la técnica ata la regla a una forma de resolverlo; lo que se exige es el resultado, y la nota ya ofrece la alternativa para cuando el volumen no dé.

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D8 · Distingue pertenencia de autoría en el modelo de datos

El dato compartido lleva **dos columnas distintas**: **pertenencia** —a qué contenedor de negocio pertenece: `tenant_id`, `proyecto_id`— y **autoría** —quién lo tocó: `usercreate_id`—. Listados, permisos y ediciones se resuelven por pertenencia; la autoría solo audita ([por qué se confunden](../notas/pertenencia-y-autoria.md)).
**Excepción** — la entidad personal, como un borrador privado, lleva al usuario como pertenencia (condición); no vale para nada compartido (límite) y lo decide quien modela (autorizador).

```
INCORRECTO: listar las entidades del contenedor activo filtrando por «creada
            por el usuario actual» → el segundo usuario del mismo contenedor
            no ve nada
CORRECTO:   filtrar por la columna de pertenencia (el contenedor activo); la
            de autoría queda solo para auditoría
```

(extiende [`03·D1`](#d1--la-tabla-nueva-nace-normalizada); depende de [`03·D6`](#d6--concurrencia-e-idempotencia) y de [`04·S1`](04-seguridad.md#s1--autorización-en-cada-acción-sensible))

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Vuelta a aplicar el 2026-08-22 (pendiente 19):** su bloque `Encadenamiento` pasó a la forma de [`M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), entre paréntesis. La exigencia no cambió.

**La fila 5 reprobaba y se corrigió en esta pasada.** El ejemplo estaba escrito con el código de un stack concreto y una entidad de un proyecto real, y [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) manda que la base no nombre lenguaje, framework ni dominio. Reescrito en términos del propio estándar: contenedor, pertenencia, autoría. **No cambia qué exige la regla.**

**Vale anotar que ese ejemplo sobrevivió cuatro meses.** Es justo lo que la fila 5 existe para atrapar y lo que ningún lector nota, porque un ejemplo con código real se lee más fácil que uno abstracto — y por eso convence más.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `00` N4/N5 (datos reales, masivas), `04` (validación/authz), `05` E2 (transacciones), `06` (índices, N+1), `15` (registros inmutables).
