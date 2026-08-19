# 04 · Seguridad de la aplicación  ·  `[CAPA 2]`

Seguridad más allá de los archivos. El núcleo (`00`) blinda los mínimos; aquí el detalle. La capa 3 declara los mecanismos concretos (permisos, plantillas, almacenamiento).

---

## S1 · Autorización en cada acción sensible

Toda acción que lee o cambia datos no públicos verifica **autenticación y permiso en el servidor**. Ocultar un botón es apariencia, no seguridad.

- El permiso se comprueba en el punto de entrada.
- Y el **alcance**: el usuario solo llega a sus registros.
- Anular, eliminar y las masivas llevan **permiso propio**.

```
INCORRECTO: oculto el botón "Eliminar" y confío en que no llamen al endpoint
CORRECTO:   verifico permiso en el servidor + valido el scope del registro
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

**La fila 10 reprobaba y se corrigió en esta pasada: de 437 caracteres a 311**, para un molde de 320. Se fueron los paréntesis que enumeraban dónde comprobar y qué cuenta como registro propio. Los tres puntos siguen, y el **alcance** —que no baste el permiso genérico— sigue dicho.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S2 · Valida y sanea toda entrada externa

Todo dato de afuera es **no confiable** hasta validarlo.

- Tipo, rango, formato y valores permitidos, **en el servidor**.
- Escapado según el destino: pantalla, consulta, ruta de archivo, orden del sistema.
- **Lista blanca** antes que lista negra.
- Archivos: tipo real y tamaño; nunca ejecutables.

```
INCORRECTO: renderizar directo lo que escribió el usuario
CORRECTO:   escapar la salida al renderizar (XSS)
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

**La fila 10 reprobaba y se corrigió en esta pasada: de 349 caracteres a 295**, para un molde de 320. Se fue la enumeración de qué es «dato de afuera» y los nombres de los ataques; lo que se escapa y contra qué sigue igual.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S3 · Nunca construyas consultas ni comandos por concatenación

- **BD:** consultas parametrizadas / ORM. Nunca concatenar entrada en la consulta (inyección SQL).
- **Shell:** evita comandos con entrada del usuario; si es inevitable, separa comando y argumentos y escapa (inyección de comandos).
- **Asignación masiva:** declara qué campos son asignables; no vuelques todo el payload al modelo (evita que seteen `es_admin`).

```
INCORRECTO: "SELECT * FROM users WHERE email = '" + input + "'"
CORRECTO:   consulta parametrizada con el input como parámetro

INCORRECTO: crear el registro volcando todo el payload de la petición
CORRECTO:   asignar solo los campos permitidos explícitamente
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

**Dos filas.**

- **Fila 9 · son tres frentes**, y el análisis del 2026-08-07 nombró el que sobra: la **asignación masiva** no es concatenación. Los otros dos —consultas y comandos de shell— sí son la misma exigencia vista en dos sitios.
- **Fila 10 · no cabe:** 358 caracteres, y se pasa por el tercer frente.

El corte propuesto entonces sigue valiendo: la asignación masiva a una `S12` propia.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S4 · Guarda los secretos fuera del código y rota el que se expuso

El mínimo está en [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada). Además:

- Secretos (claves, credenciales, tokens) en **configuración de entorno**, fuera del código (ver `11`).
- El archivo de entorno real está **ignorado** por el control de versiones; se versiona solo una plantilla sin valores.
- Un secreto expuesto por accidente se **rota** (no basta borrarlo).

```
INCORRECTO: const API_KEY = "sk-live-abc123"
CORRECTO:   leerla de la configuración de entorno; el valor real no se versiona
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**La fila 8 reprobaba y se corrigió en esta pasada.** El título era «Gestión de secretos»: nombra un tema y no enuncia ninguna norma. Pasa a *Guarda los secretos fuera del código y rota el que se expuso*. **No cambia qué exige la regla.** Es el quinto título así corregido hoy.

**Quedan dos filas, y las dos ya estaban señaladas.**

- **Fila 11 · texto prestado.** Sus dos primeros puntos son [`11·CFG1`](11-configuracion-entornos.md#cfg1--la-configuración-vive-fuera-del-código) y [`11·CFG2`](11-configuracion-entornos.md#cfg2--el-entorno-real-no-se-versiona-sí-una-plantilla) dichas otra vez. Lo propio es **la rotación**: que un secreto expuesto se rota y no basta con borrarlo. Eso no lo dice nadie más.
- **Fila 10 · no cabe:** 324 caracteres, y se pasa **por lo prestado**.

**Es el mismo caso que [`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)**: quitar lo repetido la deja cabiendo sola. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S5 · CSRF, sesiones y transporte

- **CSRF:** token anti-falsificación en acciones que cambian estado por navegador; no lo desactives por comodidad.
- **Sesiones:** cookies `HttpOnly` y `Secure`; invalidar al cerrar sesión; expiración razonable.
- **Transporte:** datos sensibles siempre por HTTPS.
- **Contraseñas:** hashing fuerte con salt, nunca en texto plano.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ❌ ✅ ❌ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 13 ✅ · 4 ❌ · 3 N/A.**

**Tres filas, y el análisis del 2026-08-07 ya la tenía en rojo.**

- **Fila 8 · el título junta cuatro temas con comas y una «y»:** CSRF, sesiones, transporte. Y adentro hay una cuarta que el título ni nombra — el hashing de contraseñas.
- **Fila 9 · son cuatro exigencias** y se cumplen por separado con toda facilidad: un sistema puede tener el token anti-falsificación puesto y las contraseñas en texto plano.
- **Fila 12 · sin ejemplo.**

**No se le agregó el ejemplo, y es a propósito:** con cuatro exigencias adentro, cualquier ejemplo cubre una y deja tres sin ilustrar. El ejemplo llega cuando se sepa con qué se queda cada regla. Partirla en cuatro va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S6 · Archivos sensibles: privado + acceso controlado

Todo archivo no público (financiero, jurídico, personal):

- **Almacenamiento privado**, nunca en ubicación pública ni con URL adivinable.
- Acceso por un **punto controlado** (auth + permiso + scope); forzar descarga.
- Guarda metadatos (ubicación, tipo, tamaño) para poder migrar de almacenamiento sin tocar código.
- **Preservación:** al borrar (lógico) la entidad padre, el archivo **no se elimina físico**. La purga física es operación admin con preview ([`00·N5`](00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)).
- **Backup** junto con la BD. Carga con lista blanca de tipos y tamaño máximo.

```
INCORRECTO: documento sensible en carpeta pública con URL directa
CORRECTO:   almacenamiento privado + endpoint con auth/permiso/scope
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

**Fila 9 · cinco sub-exigencias**, y la fila **10** en consecuencia: 542 caracteres.

El análisis del 2026-08-07 proponía sacar de ahí la **preservación** y el **respaldo**, que son otro tema —qué pasa con el archivo después—, y dejar la regla con lo suyo: que el archivo sensible nace privado y se sirve con control de acceso.

También solapa con [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada). Ahí la salida es la de siempre: que el núcleo **enlace** hacia acá, no que esta repita al núcleo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S7 · Dependencias sin vulnerabilidades conocidas

Mantén las dependencias al día y **audita vulnerabilidades** con la herramienta del ecosistema. No introduzcas una con vulnerabilidades sin resolver (detalle en `10`).

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ❌ N/A ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 1 ❌ · 4 N/A.**

**Fila 11 · texto prestado, y en referencia circular.** Esta regla y [`10·DEP3`](10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día) dicen lo mismo y se citan entre sí. El análisis del 2026-08-07 fue explícito sobre cuál sobra: **`DEP3` es el dueño** —una vulnerabilidad de una dependencia es asunto de dependencias— y la salida es **derogar esta**.

**Es la otra mitad de lo que ya quedó anotado al sellar `DEP3` hoy.** Las dos reprueban la misma fila por el mismo motivo, y la única forma de arreglarlas es la misma: una de las dos deja de existir.

**Cabe de sobra —167 de 320— y aun así no se puede quedar.** Que una regla esté bien escrita no la salva de sobrar.

Derogarla va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), y no es lo mismo que borrarla: [`20·M11`](20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) fija cómo se hace sin romper las citas.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S8 · No filtres información en errores

Los errores de cara al usuario no exponen internos (trazas, consultas, rutas, versiones). El detalle va al log; al usuario, un mensaje genérico y accionable (detalle en `05`).

```
INCORRECTO: mostrar la traza y el SQL en una página de error
CORRECTO:   loguear el detalle; al usuario, mensaje claro sin internos
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

Cabe —175 de 320—, tiene su ejemplo y dice lo suyo.

**El análisis del 2026-08-07 la marcaba por duplicar el tercer punto de [`05·E3`](05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico), y pedía elegir dueño. Ya está elegido, y es esta:** `E3` la **enlaza** como el motivo de que la traza no llegue al usuario, y se quedó con lo suyo —los dos niveles de mensaje—.

Se comprobó al sellar el capítulo `05` hoy, desde el otro lado, y coincide. **Es la misma solución que arregló [`08·T5`](08-pruebas.md#t5--ejecuta-y-reporta) y [`02·F5`](02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md):** no derogar ninguna, sino que la de al lado declare qué toma y se quede con lo que agrega.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S9 · No toques rutas del sistema fuera del proyecto · solo autorizadas exactas

El agente **solo escribe, mueve, elimina o modifica archivos dentro de la carpeta del proyecto** o dentro de rutas **explícitamente autorizadas** por el usuario (ubicaciones estándar declaradas en la capa 3, como la carpeta central de la base común del agente).

- **Rutas del sistema operativo prohibidas por defecto:** carpetas de usuario ajenas al proyecto, ubicaciones globales del OS (Program Files, `/usr/`, `/etc/`, `%SystemRoot%`, `%APPDATA%` de otros programas), carpetas de terceros (otros proyectos del usuario, IDEs, entornos virtuales de otros repos).
- **Ruta autorizada = ruta exacta**, no "una ruta parecida" ni "un padre común". Si el usuario autoriza `C:\proyectos\repo-A\config.json`, no se autoriza `C:\proyectos\repo-B\config.json` ni `C:\proyectos\`.
- **Lectura permitida** sin autorización cuando el archivo es de referencia declarada (docs abiertas del usuario, path que el usuario mencionó). Escritura NO.
- **Ampliación de rutas autorizadas** requiere autorización explícita del usuario en el chat. No se infiere de "es evidente que también necesito Y".

Este comportamiento aplica incluso cuando el cambio "obviamente ayuda" ("agrego una entrada a tu `hosts` para que funcione la prueba"). La disponibilidad técnica no autoriza — la aprobación explícita sí.

```
INCORRECTO: durante una fase, escribir en la carpeta home del usuario o en Program Files
            "porque es más práctico" → efecto lateral fuera del alcance del proyecto,
            imposible de auditar desde el repo
CORRECTO:   quedarse dentro del proyecto; si algo fuera realmente es necesario,
            reportarlo y esperar autorización de la ruta exacta
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

**Fila 10 · no cabe: 1278 caracteres, cuatro veces el molde.**

**Pero conviene leerla antes de acortarla, porque es el modelo de referencia del cuerpo entero.** El análisis del 2026-08-07 la señaló así: *«la excepción declara condición, límite y autorizador»* y recomendaba **usarla como plantilla**. Es la única del estándar que cumple [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) entera.

Eso importa hoy más que cuando se escribió: al aplicar el checklist aparecieron **tres excepciones sin autorizador** —[`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`03·D4`](03-datos.md#d4--valores-configurables-van-a-catálogo--cero-hardcode) y [`03·D5`](03-datos.md#d5--con-la-bd-desplegada-la-validación-nueva-va-en-la-app)— y esta es de dónde copiar la forma.

**Al acortarla, la excepción no se toca.** Lo que sobra es lo de alrededor.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S10 · No mates procesos globales · solo PID exacto y estrictamente necesario

El agente **no mata procesos** del sistema operativo con criterios amplios (por nombre de binario, por patrón, "todos los procesos de tal intérprete"). Matar procesos globales puede tumbar servicios que el usuario está usando en paralelo (otras terminales, IDEs, servidores de desarrollo de otros proyectos, tareas de fondo del OS).

**Reglas:**

- Matar procesos por **PID exacto**, no por nombre ni patrón.
- Solo cuando el proceso a matar sea **claramente del proyecto** y su terminación sea **estrictamente necesaria** para la tarea (por ejemplo, un servidor de desarrollo que arrancó el agente en la fase actual y quedó colgado).
- **Prohibido** por defecto: `killall`, `pkill -f <patrón>`, `taskkill /IM <binario> /F`, "matar todos los procesos de X".
- Si es realmente necesario terminar por patrón (caso extremo), **pausar y pedir autorización explícita** al usuario indicando qué PID/nombre y por qué.
- Al arrancar un proceso persistente (servidor, watcher), guarda el PID para poder terminarlo puntualmente al cerrar la tarea.

```
INCORRECTO: "hay procesos node colgados" → `killall node` → matas el IDE del usuario
            y los watchers de otros repos
CORRECTO:   identificar el PID exacto del proceso que arrancó la fase actual y matar
            solo ese PID
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.2**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 10 · no cabe: 1029 caracteres.** Es lo único que reprueba.

**La fila 5 reprobaba por dos intérpretes nombrados, y se corrigió en esta pasada.** Sus ejemplos de patrón amplio decían `node` y `php`; ahora dicen «todos los procesos de tal intérprete», que es lo mismo sin nombrar ninguno. **No cambia qué prohíbe.**

**Lo que hay que anotar es cómo se le pasó.** El sello anterior sí argumentó la fila 5 —para defender `killall`, `pkill` y `taskkill`, que es lo llamativo— y **al hacerlo dio la fila por revisada**. Los dos intérpretes estaban tres líneas más arriba. Un argumento sobre una fila no es una revisión de la fila: quien lee el sello ve que alguien la miró, y no ve qué parte miró. Lo encontró la comprobación de [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), no una lectura.

**Los tres nombres del oficio se quedan**, y el motivo sigue valiendo: `killall`, `pkill` y `taskkill` no son producto ni framework sino cómo se llama la misma acción en cada sistema, y quitarlos dejaría la regla sin decir qué prohíbe. Es el mismo criterio con el que [`04·S11`](#s11--escritura-contra-el-almacén-productivo-requiere-autorización-por-operación) conserva el suyo.

Su excepción está completa, como la de `S9`.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S11 · Escritura contra el almacén productivo requiere autorización por operación

`00 N4` cubre el principio general de proteger los datos reales. S11 lo refina con dos matices operativos que evitan escapes silenciosos.

**Regla 1 — Autorización por operación, no por sesión.** Cada `create/update/delete` contra el almacén productivo requiere **autorización explícita del usuario para esa operación puntual**. Autorizar una operación previa **no** autoriza las siguientes, aunque sean del mismo tipo. La autorización viaja con la acción, no con la sesión.

**Motivo:** una autorización de sesión abre la puerta a que el agente encadene operaciones no previstas ("ya que estamos, aprovecho y también"), rompiendo el control. Por operación fuerza a que cada acción tenga su OK, con el archivo/tabla/filas concretas nombrados.

**Regla 2 — El borrado lógico cuenta como escritura.** `destroy()`, `SoftDeletes`, `archivar`, `desactivar` y equivalentes que en realidad marcan un campo (`deleted_at`, `activo=false`, `archivado_at`, etc.) son **escrituras** contra el almacén productivo. Requieren autorización explícita como cualquier `update`, aunque el nombre del método sugiera "eliminar".

**Motivo:** el nombre del método puede ocultar la naturaleza de escritura. `destroy()` en un modelo con trait de soft-delete no borra físicamente pero sí modifica una fila productiva — cuenta.

**Antes de escribir contra el almacén productivo:**

- Describir en el chat: qué operación, qué tabla, qué filas concretas (`WHERE ...` o el subconjunto), qué campos.
- Esperar OK explícito del usuario para esa descripción concreta.
- No encadenar operaciones "aprovechando que ya me autorizó lo anterior".

```
INCORRECTO: usuario autoriza "corregí el estado del registro X" → agente aprovecha y
            también corrige los registros Y y Z que "estaban con el mismo bug"
CORRECTO:   agente ejecuta solo X · reporta el hallazgo de Y y Z como recomendación ·
            espera OK explícito antes de tocar cada uno

INCORRECTO: "vamos a limpiar los registros huérfanos con destroy()" — se ejecuta sin
            aviso porque "no es delete físico, es solo soft-delete"
CORRECTO:   `destroy()` con soft-delete = escritura productiva · describir cuántas
            filas afecta + esperar OK
```

**Encadenamiento:** `00 N4` (protege los datos reales) es el principio blindado · `S11` es la especificación operativa · `01 C1` (avisa antes de tocar) — en el contexto de BD productiva, "avisar" significa autorización explícita por operación, no permiso de sesión.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ❌ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ❌ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 13 ✅ · 4 ❌ · 3 N/A.**

**Era el otro ❌ de prioridad alta del análisis del 2026-08-07, junto con [`03·D1`](03-datos.md#d1--toda-tabla-nueva-se-normaliza-y-lleva-auditoría).**

- **Fila 9 · se autodeclara doble.** Dice literalmente *«Regla 1»* y *«Regla 2»* dentro de su propio cuerpo. Cuando una regla necesita numerar sus partes, ya son dos: la autorización por operación y que el borrado lógico cuenta como escritura.
- **Fila 5 · nombra un stack.** `destroy()`, `SoftDeletes` y `deleted_at` son de un framework concreto. Es el segundo caso hoy, tras [`03·D8`](03-datos.md#d8--distingue-pertenencia-de-autoría-en-el-modelo-de-datos), y aquí **no se corrigió**: a diferencia de aquel, el ejemplo no es un añadido sino que el nombre del método **es el argumento** —el punto de la regla es que `destroy()` suena a borrar y escribe—. Reescribirlo en concepto es parte de partirla, no un arreglo aparte.
- **Fila 10 · no cabe:** 1859 caracteres.

Va entera al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). **Su segunda mitad es la que más vale:** que el borrado lógico cuente como escritura es el matiz que evita el escape silencioso, y ninguna otra regla lo dice.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `00` N6 (secretos), `03` (integridad de datos), `05` (errores), `10` (dependencias), `12` (privacidad).
