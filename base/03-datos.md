# 03 · Datos y persistencia  ·  `[CAPA 2]`

Diseño y cambio del almacenamiento: esquema, migraciones, catálogos. La capa 3 declara los nombres concretos (motor, prefijos, tabla de catálogo, trait de auditoría).

---

## D1 · Toda tabla nueva se normaliza y lleva auditoría

**Normalización (1FN/2FN/3FN).** No se acepta: columnas multivaluadas (listas/JSON/arrays serializados — el 1:N va en tabla hija con FK, el N:M en pivot), atributos duplicados del padre, dependencias transitivas, ni enums nativos (van a catálogo, D4).

**Auditoría** en toda tabla nueva (salvo pivots puras): quién creó, quién editó, timestamps de creación/actualización. Las tablas transaccionales/contables/legales llevan **soft delete**.

**Integridad en la BD** (no solo en la app): FK con política de borrado explícita; `UNIQUE` en columnas con unicidad conceptual; índices en lo que se filtra (FKs, fechas, estados).

```
INCORRECTO: guardar "Guantes,Mascarilla,Botas" como texto
CORRECTO:   tabla hija + FK

INCORRECTO: tabla sin auditoría "porque es un catálogo simple"
CORRECTO:   todas la llevan, salvo pivots puras
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**

**Era uno de los dos ❌ de prioridad alta del análisis del 2026-08-07, y lo sigue siendo.**

- **Fila 9 · son tres exigencias**, y el título las junta con una «y»: normalizar, llevar auditoría e indexar. Se cumplen por separado sin ninguna dificultad.
- **Fila 10 · no cabe:** 618 caracteres para un molde de 320.
- **Fila 11 · texto prestado.** Su bloque de índices repite [`06·R3`](06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena), que es la dueña del tema y está limpia.

El análisis proponía el corte —`D1` normalización · `D9` auditoría · `D10` índices— y que los índices **enlacen** a `R3` en vez de repetirla.

**Antes de partirla conviene probar lo que funcionó con [`08·T5`](08-pruebas.md#t5--ejecuta-y-reporta):** quizá no haga falta una `D10`, sino que el bloque de índices se comprima a un enlace. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D2 · Cada cambio de esquema es una migración reversible

Migración independiente, con aplicación y reversión funcionales. **Nunca modifiques una migración ya ejecutada** — crea una nueva. Documenta qué y por qué. Correrla contra datos reales requiere autorización ([`00·N4`](00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo, y el análisis del 2026-08-07 explicaba por qué hacía falta — *«editar una migración ya ejecutada es error frecuente»*. **No cambia qué exige la regla.**

Cabe de sobra: 217 de 320. **Es la única del capítulo que cabe**, y por eso conviene mirarla al reescribir las demás.

Está clasificada y con validador escrito —`migraciones.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D3 · Migraciones retrocompatibles con los datos existentes

Preservar datos y comportamiento sin intervención manual.

- Columna obligatoria nueva → con **default** equivalente al comportamiento previo.
- Enum → FK a catálogo: (1) crear el catálogo, (2) poblar la columna nueva mapeando cada valor viejo, (3) recién ahí hacerla obligatoria.
- **Nunca borres datos históricos** al migrar. Si la reversión no puede recuperar datos, documéntalo.

```
INCORRECTO: columna obligatoria sin default → falla si ya hay filas
CORRECTO:   default equivalente al comportamiento previo, luego endurecer
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 10 · el cuerpo no cabe: 378 caracteres para un molde de 320.**

El análisis del 2026-08-07 la daba por cumplida. Es el **tercer** caso —tras [`05·E4`](05-errores-y-logging.md#e4--loguea-con-niveles-y-con-propósito) y [`17·I1`](17-interfaz.md#i1--toda-vista-resuelve-sus-tres-estados)— en que esa fila se midió a ojo. A estas alturas no es un descuido suelto: **la fila 10 de aquel análisis no es fuente fiable y hay que recontarla entera.**

Lo demás pasa, y está clasificada con validador escrito —`esquema.py`—. Se pasa por poco y lo que sobra es explicación, no exigencia.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D4 · Valores configurables van a catálogo — cero hardcode

Nada que pueda cambiar por decisión del negocio, la ley o la operación se quema en el código (constantes, arrays, `switch`/`match`, literales en condiciones): umbrales, listas válidas, mapas por tipo, textos editables, flags de comportamiento. Va a un **catálogo** consultable.

Si necesitas escribir un mapa/array/switch con valores del dominio, **detente y crea el catálogo primero**.

- **Bifurca por código semántico**, no por id (los ids cambian entre entornos).
- Los flags de un tipo/estado viven **junto al catálogo** (metadata), no en el código.
- Los códigos que el código referencia se marcan **protegidos** (no borrables desde la UI).
- Cachea los catálogos que se consultan seguido.

Excepciones (cero hardcode ≠ cero literales): constantes técnicas (columnas, rutas, eventos), fórmulas matemáticas fijas, códigos externos estables por ley. Ante la duda, **inclínate al catálogo**.

**Cuando el catálogo genérico no cabe** — a veces el valor configurable tiene estructura propia (mapas por tipo, rangos numéricos con intervalos, relaciones internas entre valores) que no encaja en la tabla genérica de parámetros (típicamente `codigo` + `valor` + `flags`). En ese caso, **crear una tabla propia de dominio** para ese conjunto (`<dominio>_<subdominio>`) con auditoría estándar (D1), FKs a otros catálogos si aplica, y **seed inline en la migración**. Sigue siendo cero hardcode — el catálogo es específico, no genérico. Al detectar hardcode existente durante una unidad de trabajo, agregar tarea explícita al plan para migrarlo antes del cierre.

```
INCORRECTO: if (saldo < 100000)                          // umbral quemado
CORRECTO:   leer el umbral del catálogo

INCORRECTO: validar: modalidad ∈ {'efectivo','especie'}   // lista fija quemada en el código
CORRECTO:   validar contra los códigos leídos del catálogo

INCORRECTO: if (tipo_id === 3)                            // id opaco
CORRECTO:   if (tipo_codigo === 'especie')               // código semántico
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ❌ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**

**1546 caracteres: casi cinco veces el molde.**

- **Fila 10 · no cabe.**
- **Fila 9 · hay una exigencia escondida.** El bloque «cuando el catálogo genérico no cabe» —tabla propia con sus columnas— es otra regla, no una aclaración de esta.
- **Fila 16 · la excepción está incompleta.** Declara condición y no dice ni límite ni quién autoriza, igual que [`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba).

**La fila 16 es la que más pesa:** una excepción sin autorizador es un permiso que se concede quien la usa. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D5 · Con la BD desplegada, la validación nueva va en la app

Si la BD ya está en producción, su estructura es un contrato vigente. Una validación nueva que no encaje limpio (limita el motor, choca con datos legacy, migrar es caro) **no se fuerza en la BD**: va al servicio/observer/regla.

- Si una restricción falla al aplicarse o exigiría borrar/modificar filas históricas, se **descarta en BD** (salvo autorización para limpiar datos) y queda en el servicio.
- El servicio que sostiene la validación lleva **prueba dedicada** (sin ella, se degrada en silencio).
- Documenta en la migración por qué no vive en la BD.

**No aplica** en diseño desde cero (sin datos aún): ahí el invariante sí va al esquema.

```
INCORRECTO: la migración falla contra los datos → editar la BD a la fuerza
CORRECTO:   validación en el servicio + prueba + nota en la migración
```

---

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ❌ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**Dos filas, y las dos ya estaban señaladas.**

- **Fila 16 · la excepción está incompleta.** «No aplica en diseño desde cero» es condición, y le faltan el límite y quién autoriza.
- **Fila 10 · no cabe:** 640 caracteres, el doble del molde.

Es la tercera excepción sin autorizador que aparece hoy —con [`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba) y `D4`—. **Conviene revisarlas juntas**, porque la pregunta de fondo es la misma: quién concede el permiso de no cumplir.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D6 · Concurrencia e idempotencia

Cuando dos operaciones pueden tocar el mismo dato a la vez, protegé la integridad — no confíes en que "no va a pasar".

- **Idempotencia:** una operación repetida (doble clic, doble submit, reintento) no debe duplicar efectos. Usá una clave de idempotencia o verificá el estado antes de aplicar.
- **Actualización concurrente (lost update):** al modificar un valor compartido (un saldo, un contador), usá **bloqueo optimista** (una versión / `updated_at` que se revalida al guardar) o una operación **atómica** en la BD; nunca leer-modificar-escribir sin control.
- **Duplicados por carrera:** una restricción `UNIQUE` en la BD es la **única** garantía real contra dos inserciones simultáneas del mismo registro; la validación en la app no alcanza (dos procesos la pasan a la vez).

```
INCORRECTO: leer saldo → sumar en memoria → guardar   (dos procesos se pisan, se pierde una suma)
CORRECTO:   incrementar el saldo de forma atómica en la BD, o bloqueo optimista con revalidación
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**

**Título nominal y tres exigencias adentro.**

- **Fila 8 · «Concurrencia e idempotencia»** nombra dos temas y no enuncia ninguna norma. Es el cuarto título así que aparece hoy, tras [`15·IM2`](15-registros-inmutables.md#im2--guarda-los-tres-estados-y-la-trazabilidad-de-quien-anula), [`12·PR5`](12-privacidad-datos.md#pr5--define-cuánto-se-conservan-y-qué-pasa-después) e [`17·I6`](17-interfaz.md#i6--funciona-en-los-tamaños-de-pantalla-que-el-proyecto-soporta).
- **Fila 9 · son tres:** idempotencia, la actualización perdida y los duplicados por carrera. Se cumplen por separado — reintentar sin duplicar efectos no protege de dos escrituras simultáneas.
- **Fila 10 · no cabe:** 777 caracteres.

El análisis proponía partirla en tres con títulos imperativos, y sigue siendo lo que corresponde.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D7 · Persistencia histórica SCD-2 — patrón canónico para valores que evolucionan

Complementa `D5` (validación en la app cuando la BD ya está desplegada). Aplica cuando un valor de negocio **cambia con el tiempo** y las consultas históricas necesitan saber **"cómo estaba X en fecha Y"**, no solo "cómo está X hoy".

Los cálculos al vuelo dan siempre el estado actual — pierden la historia. Auditorías, informes legales, disputas, reportes retrospectivos necesitan el estado histórico real. La estrategia "reconstruir sumando datos vivos hasta fecha X" **solo funciona si el pasado es inmutable**; en cuanto haya anulaciones diferidas, ediciones bajo ventana, reversiones o cambios de relación, la reconstrucción al vuelo devuelve el estado teórico, no el histórico real.

**Cuándo aplica:**

- Cálculos derivados de datos operativos que cambian (participación, saldos por período, totales acumulados).
- Relaciones que evolucionan y afectan cálculos históricos (jerarquía padre/hijo, asignación a responsable, categoría del cliente).
- Estados de entidades que se referencian en reportes históricos.
- Cualquier valor que pueda aparecer en una demanda, auditoría o disputa con la pregunta "¿cuánto era esto en fecha X?".

**Cuándo NO aplica:**

- Datos de configuración estáticos (catálogos que no cambian con el uso).
- Cálculos sin relevancia histórica (estadísticas del día actual, dashboards operativos en tiempo real).
- Datos ya inmutables por diseño (snapshots firmados · registros congelados por regla del dominio · ver `15` registros inmutables).
- Reportes de "estado actual" donde una consulta con soft-delete + timestamps es suficiente y auditable.

**Patrón canónico (SCD-2 · tramos con `desde_at` / `hasta_at`):**

1. **Tabla `<entidad>_historial`** con: PK · FK a la entidad fuente · las columnas del estado que se congelan · `desde_at NOT NULL` · `hasta_at NULL` (null = tramo vigente) · `motivo` corto que identifica el evento que abrió el tramo · auditoría estándar (D1) · índice `(fuente_id, desde_at)`.
2. **Backfill en la migración**: por cada registro fuente existente, insertar tramo inicial con `desde_at = fuente.created_at`, `hasta_at = NULL`, motivo `"backfill migración inicial"`.
3. **Evento de dominio por cada cambio significativo** en la entidad fuente (creado/actualizado/eliminado/cualquier acción del negocio que cambie los valores del tramo).
4. **Listener dedicado** que, dentro de transacción, (a) cierra el tramo vigente afectado (`hasta_at = ahora`) y (b) inserta el tramo nuevo con los valores del nuevo estado.
5. **Consulta canónica** en el modelo / servicio: `estadoEn(fecha) → valores del tramo vigente en esa fecha`.
6. **UI — línea de tiempo visible** en la ficha de la entidad, para que el usuario final audite la evolución sin salir del sistema.
7. **Tests obligatorios**: backfill correcto · evento dispara actualización · estado en fecha pasada devuelve valor histórico (no el actual) · un solo tramo vigente por entidad a la vez.
8. **Cascada de eliminación cuidadosa**: la entidad fuente NO se hard-delete si tiene historial; solo soft-delete. El historial sobrevive.

**Consideración de volumen** — SCD-2 puro puede generar N filas por evento si el evento afecta a N entidades relacionadas. Cuando el volumen sea prohibitivo, alternativa: **snapshot vector** (una fila por evento con el mapa completo del estado en un campo estructurado). Se decide al abrir la unidad con datos reales, no anticipadamente.

**Anti-patrón rechazado:** "calcular al vuelo y ya, es más simple". Simple hoy, incorrecto mañana. Consulta histórica → lee historial persistido. Consulta actual → puede leer estado directo. No mezclar.

```
INCORRECTO: "totalHoy" y "totalEnFecha(X)" leen del mismo estado vivo · el segundo devuelve valor teórico si el pasado se editó
CORRECTO:   tabla historial con tramos + consulta canónica estadoEn(fecha) → valor congelado que refleja lo que era realmente ese día
```

**Encadenamiento:** `D1` (auditoría toda tabla nueva) — la tabla historial también lleva audit · `D5` (validación en la app cuando la BD está desplegada) — SCD-2 vive fuera del modelo original, no invade su esquema · `15` (registros inmutables) — el tramo cerrado es inmutable por diseño.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**3839 caracteres: doce veces el molde. Es la regla más larga del cuerpo entero**, por delante de [`08·T7`](08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos).

Adentro hay un patrón de ocho pasos y una alternativa por volumen. **Eso no es una regla: es un manual con encabezado de regla.**

La salida ya está probada esta misma sesión: **abrir su anexo al lado y dejar en la regla tres líneas y el enlace**, como [base/13-documentacion/retrodocumentacion.md](13-documentacion/retrodocumentacion.md), que se mudó a su capítulo hoy.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## D8 · Distinguir pertenencia de autoría en el modelo de datos

En proyectos con múltiples usuarios trabajando sobre entidades compartidas (multi-tenant, multi-proyecto, multi-organización), el modelo debe distinguir explícitamente **dos conceptos**:

- **Pertenencia** — a quién pertenece el dato como entidad de negocio: `tenant_id`, `organizacion_id`, `proyecto_id`, `cuenta_id`, `equipo_id`, etc. Ancla la entidad al contenedor de negocio que lo posee.
- **Autoría** — quién manipuló el dato: `usercreate_id` / `userupdate_id` (o los equivalentes del stack). Es auditoría, no pertenencia.

**No confundir los dos.** La confusión típica es anclar la entidad al `usuario que la creó` (`Auth::id()` / `usercreate_id`) y filtrar los listados por autoría. Esto rompe el sistema en cuanto un segundo usuario del mismo tenant/proyecto edita, o el usuario original se va y otro debe operar sobre las mismas entidades.

**Consecuencias operativas del modelo correcto:**

- **Consultas de listado** filtran por **pertenencia** (según el acceso del usuario actual a tenants/proyectos), no por autoría.
- **Permisos + scope** validan el acceso: "el usuario X tiene permiso Y sobre el tenant Z", no "el usuario X es el creador del registro".
- **Ediciones** no requieren ser "el creador" — cualquier usuario con acceso al contenedor y permiso puede operar.
- **Reportes de auditoría** usan la columna de autoría (quién hizo qué), no la de pertenencia.

**Excepción legítima:** entidades genuinamente personales del usuario (favoritos, borradores privados, preferencias de UI). Ahí la pertenencia sí es `user_id`. Cuando lo dudes, preguntá: "¿esto es del usuario, o del tenant/proyecto donde el usuario está trabajando?"

```
INCORRECTO: listar las entidades del contenedor activo filtrando por «creada
            por el usuario actual» → el segundo usuario del mismo contenedor
            no ve nada
CORRECTO:   filtrar por la columna de pertenencia (el contenedor activo); la
            de autoría queda solo para auditoría
```

**Encadenamiento:** `D1` (auditoría toda tabla nueva) — la columna de autoría es parte de la auditoría estándar · `D6` (concurrencia) — múltiples usuarios operando el mismo tenant refuerza la necesidad de este modelo · `04 S1` (autorización con scope) — la validación de scope opera sobre la columna de pertenencia, no de autoría.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**La fila 5 reprobaba y se corrigió en esta pasada.** El ejemplo estaba escrito con el código de un stack concreto y una entidad de un proyecto real, y [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) manda que la base no nombre lenguaje, framework ni dominio. Reescrito en términos del propio estándar: contenedor, pertenencia, autoría. **No cambia qué exige la regla.**

**Fila 10 · sigue sin caber: 1962 caracteres, seis veces el molde.** Lo que sobra son las cuatro consecuencias operativas y el encadenamiento con otras reglas — material de anexo, como `D7`.

**Vale anotar que ese ejemplo sobrevivió cuatro meses.** Es justo lo que la fila 5 existe para atrapar y lo que ningún lector nota, porque un ejemplo con código real se lee más fácil que uno abstracto — y por eso convence más.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `00` N4/N5 (datos reales, masivas), `04` (validación/authz), `05` E2 (transacciones), `06` (índices, N+1), `15` (registros inmutables).
