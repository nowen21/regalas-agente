# 05 · Manejo de errores y logging  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-018](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-018-el-capitulo-05-manejo-de-errores-y-logging/HU-018-el-capitulo-05-manejo-de-errores-y-logging.md). Todo cambio de este capítulo baja por ella (`02·F23`).

Cómo tratar fallos y qué registrar, sin filtrar información ni ocultar problemas. La capa 3 declara el framework de logging y los destinos.

---

## E1 · No te tragues los errores en silencio

Un error capturado se maneja **visible y trazable**. Nada de `catch` vacío.

- Recuperable: manéjalo y deja constancia (log).
- No recuperable: déjalo **propagar** a un manejador central que lo registre y responda controlado.
- No lo conviertas en un retorno ambiguo (`null`/`false`) sin registrar la causa.

```
INCORRECTO: try { ... } catch (e) { }
CORRECTO:   try { ... } catch (e) { log.error(...); manejar o propagar }
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

El análisis del 2026-08-07 en [analisis/base-2026-08-07-cumplimiento-meta-reglas.md](../analisis/base-2026-08-07-cumplimiento-meta-reglas.md) ya la daba por cumplida. Coincide.

La fila **9** pasa aunque el cuerpo tenga tres viñetas: son **los tres caminos** de la misma exigencia —recuperable, no recuperable, y el retorno ambiguo que no vale como ninguno de los dos—, no tres exigencias. Un error no puede caer en dos a la vez.

Está clasificada y con validador escrito —`errores.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## E2 · Valida al entrar y aborta temprano

Las precondiciones se comprueban **al principio**, y si algo falta se aborta ahí con un mensaje que diga qué falta. Fallar a mitad deja el estado a medias, y arreglarlo cuesta más que no haber empezado.

> La variante destructiva —no saltarse el enganche, no borrar la prueba— está en [`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada).

```
INCORRECTO: se recorre la lista, se procesan cuatro y al quinto falta un dato
CORRECTO:   se comprueba que los cinco tengan el dato y, si no, no se procesa ninguno
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.21.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Traía dos exigencias que se cumplen por separado: validar al entrar, y envolver en transacción lo que toca varios registros. **Se puede validar todo al principio y aun así dejar tres registros escritos y el cuarto no.** La segunda es ahora [`E6`](#e6--lo-que-toca-varios-registros-va-en-transacción). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## E6 · Lo que toca varios registros va en transacción

La operación que deja **varios registros consistentes entre sí** se hace en una transacción: todo o nada. Si falla a la mitad, no queda la mitad (extiende [`05·E2`](#e2--valida-al-entrar-y-aborta-temprano)).

```
INCORRECTO: se descuenta del inventario y falla al escribir el movimiento
            → el inventario quedó mal y nadie lo sabe
CORRECTO:   las dos escrituras van juntas; si una falla, ninguna queda
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.21.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`E2`](#e2--valida-al-entrar-y-aborta-temprano).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `E2` evita **empezar** algo que no se puede terminar; esta evita **dejarlo a medias** cuando ya empezó. La citan por separado: [`15·IM3`](15-registros-inmutables.md#im3--la-anulación-revierte-todo-o-no-revierte-nada) remite aquí para exigir que la reversión sea atómica.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## E3 · Mensajes en dos niveles: usuario y diagnóstico

- **Al usuario:** claro, en su idioma, **accionable** ("Ese correo ya está registrado"), sin jerga ni internos.
- **Al log:** el detalle completo (excepción, contexto, id de correlación).
- **Nunca** trazas/consultas/rutas al usuario (es fuga de info — [`04·S8`](04-seguridad.md#s8--no-filtres-información-en-errores)).

```
INCORRECTO: al usuario: "SQLSTATE[23000]... INSERT INTO..."
CORRECTO:   al usuario: "Ese registro ya existe."  ·  al log: la excepción completa
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

**El análisis del 2026-08-07 la marcaba en amarillo por duplicar [`04·S8`](04-seguridad.md#s8--no-filtres-información-en-errores) en su tercer punto, y recomendaba enlazarla. Ya está enlazada** — se corrigió ese mismo día, en el cambio que trajo [`20·M15`](20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) y el validador de citas.

Se comprobó contra el texto de hoy y no contra la recomendación: la fila **11** pasa porque la regla **nombra** a `S8` como el motivo de que la traza no vaya al usuario, y lo suyo —los dos niveles, usuario y diagnóstico— no lo dice ninguna otra.

La fila **9** pasa: los dos niveles son una sola exigencia. Un mensaje al usuario sin su contraparte en el log deja el fallo sin diagnosticar, y al revés deja al usuario sin saber qué pasó.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## E4 · Loguea con niveles y con propósito

Cada registro lleva su nivel —**error** lo que pide atención, **warning** lo anómalo ya manejado, **info** el hito, **debug** el detalle, apagado en producción— y el contexto que lo hace rastreable: identificadores de entidad, usuario, correlación. Loguear de más entierra la señal.
```
INCORRECTO: log.error("error")
CORRECTO:   log.error("Falló causar factura", { factura_id, usuario_id, causa })
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.12.2**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Fila 10 · arreglada el 2026-08-18.** Medía 419 caracteres para un molde de 320; ahora mide 282.

Lo que sobraba era la **escala de niveles** en cuatro viñetas. No se movió a ningún anexo: **se dijo en una línea.** Las viñetas explicaban cuándo usar cada nivel con un ejemplo cada una, y el nombre del nivel ya lo dice — *error* es lo que pide atención, *debug* es el detalle. El ejemplo sobraba, no la escala.

**El análisis del 2026-08-07 la daba por cumplida en esta fila y se equivocaba**, o midió a ojo. Que un análisis anterior diga «cumple» no exime de volver a medir lo que un programa puede medir: sirve para las nueve filas que piden leer y entender, no para las que se cuentan.

La fila **9** pasa aunque el cuerpo enumere cuatro niveles y además pida contexto: los niveles son **la escala** con que se cumple la exigencia, y el contexto es lo que hace que un registro sirva para rastrear. Un log con nivel y sin contexto no cumple a medias — no cumple.

La remisión a [`00·N5`](00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada) dice qué operación hay que registrar sí o sí. Es un enlace al capítulo dueño, no una dependencia declarada: las filas **14 a 16** son N/A.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## E5 · Nunca registres secretos ni datos sensibles

Blindado en [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada). Los logs no llevan contraseñas, tokens, ni más datos personales de los necesarios. Enmascara o excluye. Trata el log como potencialmente público.

```
INCORRECTO: log.info("Login", { email, password })
CORRECTO:   log.info("Login", { usuario_id })
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

**El análisis del 2026-08-07 la marcaba por reformular [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada) en vez de enlazarla, y pedía «dejar el enlace y la aplicación al dominio de logs». Es exactamente lo que hace hoy**, desde el cambio de ese mismo día.

Abre remitiendo —«Blindado en `00·N6`»— y lo que sigue es lo que `N6` no dice: qué significa eso **en un log**. Enmascarar o excluir, y tratar el log como potencialmente público.

**Sirve de contraste con [`12·PR4`](12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes), que hoy reprueba esta misma fila.** Aquella dice otra vez, con otras palabras, lo que dice esta; esta remite y agrega. La diferencia entre enlazar y copiar se ve mejor con las dos al lado que con cualquier definición.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `00` N3/N5/N6, `04` S8 (no filtrar), `01` C9 (reportar, no esconder), `12` (privacidad en logs).
