# 19 · Observabilidad y operación  ·  `[CAPA 2 · opt-in]`

> **Historia dueña del texto:** [EP-001 HU-032](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-032-el-capitulo-19-observabilidad-y-operacion/HU-032-el-capitulo-19-observabilidad-y-operacion.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

**Opt-in.** Reglas agnósticas para que un sistema desplegado se pueda **entender desde afuera** cuando algo va mal, sin adivinar. Aplican a proyectos que corren en producción; complementan `18` (despliegue). El agente **construye** la instrumentación y los documentos de operación (logs, métricas, alertas, runbooks, postmortem); **no opera** el sistema vivo. La herramienta concreta (stack de logs, métricas, tracing) la declara la capa 3. Extiende `05` (errores y logging).

---

## OB1 · Logs estructurados y correlacionables

Los logs se emiten como **datos** (clave-valor o JSON), no como texto libre: nivel, marca de tiempo y un **identificador de correlación** para seguir una operación de punta a punta. Nunca llevan secretos ni datos sensibles ([`05·E5`](05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles), [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).

```
INCORRECTO: imprimir «error procesando pedido» con el pedido entero, en texto libre
CORRECTO:   un registro con nivel, hora, identificador de correlación y el id del
            pedido; nada del cliente
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

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad. Y el cuerpo se recortó al molde: el porqué que sobraba quedó en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Dos filas.**

**Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## OB2 · Se mide lo que le duele al usuario

La instrumentación cubre las **señales doradas** del servicio: latencia, tráfico, errores y saturación. Las trazas permiten seguir una petición por los componentes que atraviesa. Se mide el **síntoma que sufre el usuario** (una página que no carga), no solo recursos internos (CPU) que no dicen si el sistema sirve.

```
INCORRECTO: el tablero muestra la CPU al 40 % mientras los usuarios ven páginas en blanco
CORRECTO:   se mide la latencia y la tasa de error que sufre el usuario, y de ahí salen
            las alertas
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

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

Cabe por poco: 315 de 320. **No hay margen** para agregarle nada sin recortar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## OB3 · SLO y alertas como código, sobre síntomas

Los objetivos de servicio (SLO) y las alertas se declaran **versionados**, no a mano en un tablero. Una alerta se dispara por un **síntoma que exige acción humana**, no por ruido que nadie atiende, y apunta a su runbook ([`19·OB4`](#ob4--runbooks-para-lo-que-se-opera)).

```
INCORRECTO: una alerta por cada pico de CPU, que todos aprenden a silenciar
CORRECTO:   una alerta cuando el error del usuario supera el umbral, versionada y con
            su runbook
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

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad. Y el cuerpo se recortó al molde: el porqué que sobraba quedó en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Dos filas.**

**Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## OB4 · Runbooks para lo que se opera

Las operaciones recurrentes y las de emergencia se documentan como **runbook** versionado: respaldo y restauración, recuperación ante fallo, rotación de un secreto expuesto ([`04·S4`](04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)), reversión de un release ([`18·DP5`](18-despliegue-e-infraestructura.md#dp5--release-reversible-con-plan-de-vuelta)). Un procedimiento crítico que solo vive en la cabeza de alguien no existe cuando esa persona no está.

```
INCORRECTO: «la restauración la sabe hacer una sola persona del equipo»
CORRECTO:   el runbook de restauración versionado y probado; cualquiera lo sigue
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

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

Cabe justo: **320 de 320**, el límite exacto. Quien la edite tiene que quitar antes de poner.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## OB5 · Postmortem sin culpa

Tras un incidente relevante se escribe un **postmortem** ([molde](../plantillas/postmortem.md)): qué pasó, impacto, causa raíz, línea de tiempo y **acciones para que no vuelva**, centrado en el sistema y no en culpar a una persona. Lo aprendido se registra como señal ([`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

```
INCORRECTO: el postmortem concluye «fue un error humano de tal persona»
CORRECTO:   concluye qué del sistema permitió el error y qué cambia para que no
            vuelva, y queda registrado como señal
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

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad. Y el cuerpo se recortó al molde: el porqué que sobraba quedó en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Dos filas.**

**Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

La fila **11** pasa: enlaza [plantillas/postmortem.md](../plantillas/postmortem.md) y [`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) en vez de repetir lo que dicen.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## OB6 · Operar en vivo lo hace el humano

**Fuera de alcance por diseño:** ejecutar la operación, vigilar tableros en vivo y responder incidentes en caliente son del humano. El agente **deja el sistema observable y los procedimientos escritos** para que esa operación sea posible; no la reemplaza (extiende [`18·DP8`](18-despliegue-e-infraestructura.md#dp8--correr-contra-producción-lo-autoriza-el-humano)).

```
INCORRECTO: el agente se queda vigilando el tablero y reinicia servicios por su cuenta
CORRECTO:   deja salud, alertas y runbooks escritos; operar en vivo lo hace el humano
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

**Corregida el 2026-08-22 (pendiente 19):** gana su ejemplo INCORRECTO/CORRECTO; los catorce de los capítulos `18` y `19` se escribieron juntos, como una sola unidad. Y el cuerpo se recortó al molde: el porqué que sobraba quedó en [notas/porques-recortados-al-molde.md](../notas/porques-recortados-al-molde.md).

**Dos filas.**

**Ninguna de las catorce reglas de los capítulos `18` y `19` tiene ejemplo.** No es un descuido de esta: es de los dos capítulos, que nacieron juntos en la v1.1.0 y se escribieron de corrido. El análisis del 2026-08-07 los listó así, en bloque.

**Se anota una vez y se arregla una vez.** Escribir catorce ejemplos sueltos, uno por sello, produciría catorce ejemplos que no se hablan entre sí; el capítulo entero es la unidad. Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**No corre prisa, y conviene decir por qué:** son capítulos `opt-in` y hoy **ningún proyecto los tiene encendidos**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar.

**Es la que menos lo necesita de las catorce:** declara un fuera de alcance —operar en vivo es del humano— y un límite no se ilustra con un error, se lee.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

