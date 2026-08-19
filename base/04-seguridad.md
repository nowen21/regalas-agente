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
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 349 caracteres a 295**, para un molde de 320. Se fue la enumeración de qué es «dato de afuera» y los nombres de los ataques; lo que se escapa y contra qué sigue igual.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S3 · La entrada del usuario nunca se pega dentro de una instrucción

Lo que escribe el usuario **no se concatena** dentro de una consulta ni de un comando: va como **parámetro**, separado de la instrucción. Pegarlo deja que quien escribe elija qué se ejecuta.

```
INCORRECTO: la consulta se arma sumando el texto que llegó del formulario
CORRECTO:   la instrucción va fija y el texto viaja aparte, como dato
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Traía dos exigencias que se cumplen por separado: no pegar la entrada dentro de una instrucción, y declarar qué campos se pueden asignar. **Se puede parametrizar cada consulta y aun así dejar que un formulario escriba el campo que vuelve administrador a quien lo manda.** La segunda es ahora [`S16`](#s16--solo-se-asigna-lo-que-está-declarado). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S16 · Solo se asigna lo que está declarado

Al construir o actualizar un registro con lo que llegó de afuera, se **declara qué campos se pueden tocar**. Lo que no está declarado se ignora, aunque venga en el mensaje (extiende [`04·S3`](#s3--la-entrada-del-usuario-nunca-se-pega-dentro-de-una-instrucción)).

```
INCORRECTO: se vuelca todo lo que llegó sobre el registro, «que ya viene validado»
CORRECTO:   se toman los tres campos del formulario y el resto se descarta
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`S3`](#s3--la-entrada-del-usuario-nunca-se-pega-dentro-de-una-instrucción).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `S3` protege **la instrucción**; esta protege **el destino**. No hay concatenación de por medio: el dato llega limpio y el problema es que se escribe donde no debía. Se incumple sola y en silencio — nada falla, solo que alguien terminó con un permiso que nadie le dio.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S4 · Guarda los secretos fuera del código y rota el que se expuso

El mínimo está en [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada). Además:

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
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ❌ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 2 ❌ · 3 N/A.**

**La fila 8 reprobaba y se corrigió en esta pasada.** El título era «Gestión de secretos»: nombra un tema y no enuncia ninguna norma. Pasa a *Guarda los secretos fuera del código y rota el que se expuso*. **No cambia qué exige la regla.** Es el quinto título así corregido hoy.

**Quedan dos filas, y las dos ya estaban señaladas.**

- **Fila 11 · texto prestado.** Sus dos primeros puntos son [`11·CFG1`](11-configuracion-entornos.md#cfg1--la-configuración-vive-fuera-del-código) y [`11·CFG2`](11-configuracion-entornos.md#cfg2--el-entorno-real-no-se-versiona-sí-una-plantilla) dichas otra vez. Lo propio es **la rotación**: que un secreto expuesto se rota y no basta con borrarlo. Eso no lo dice nadie más.
- **Fila 10 · no cabe:** 324 caracteres, y se pasa **por lo prestado**.

**Es el mismo caso que [`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)**: quitar lo repetido la deja cabiendo sola. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S5 · La acción que cambia estado desde el navegador lleva su token

Toda petición que cambia algo y llega desde un navegador va con un **token contra la falsificación de peticiones**, y ese token no se desactiva por comodidad ni «solo en desarrollo».

```
INCORRECTO: se apaga la comprobación del token porque estorba al probar el formulario
CORRECTO:   la prueba obtiene el token como lo haría el navegador
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

**Nace el 2026-08-18 de partir `S5`**, cuyo título —*«CSRF, sesiones y transporte»*— **ya las enumeraba**. Un título que enumera es la señal de que son varias reglas: reprobaba las filas 8, 9, 10 y 12 a la vez, y las cuatro por lo mismo. Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Se quedó con el identificador viejo** porque es la mitad más citada: quien cita `04·S5` hoy casi siempre habla del token.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S13 · La sesión se cierra de verdad y no viaja al alcance de nadie

La sesión se **invalida al cerrarla** —no basta con borrarla del lado del navegador—, tiene vencimiento, y su identificador viaja de forma que ni un guion de la página ni la red puedan leerlo.

```
INCORRECTO: cerrar sesión borra la cookie en el navegador y el identificador
            sigue valiendo en el servidor
CORRECTO:   cerrar sesión la invalida en el servidor; la cookie ya no sirve
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

**Nace el 2026-08-18 de partir `S5`**, cuyo título —*«CSRF, sesiones y transporte»*— **ya las enumeraba**. Un título que enumera es la señal de que son varias reglas: reprobaba las filas 8, 9, 10 y 12 a la vez, y las cuatro por lo mismo. Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S14 · El dato sensible no viaja en claro

Todo dato sensible se transmite **cifrado de extremo a extremo del trayecto**, sin excepción por entorno: la red interna no cuenta como segura.

```
INCORRECTO: «esto va por la red interna, no hace falta cifrarlo»
CORRECTO:   se cifra igual, porque la red interna también se escucha
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

**Nace el 2026-08-18 de partir `S5`**, cuyo título —*«CSRF, sesiones y transporte»*— **ya las enumeraba**. Un título que enumera es la señal de que son varias reglas: reprobaba las filas 8, 9, 10 y 12 a la vez, y las cuatro por lo mismo. Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S15 · La contraseña se guarda irreversible y con sal

La contraseña se guarda con una función **pensada para ser lenta**, con sal por usuario, y nunca de forma que pueda deshacerse. Cifrarla no alcanza: lo que se cifra se descifra.

```
INCORRECTO: la contraseña se guarda cifrada, «que total está protegida»
CORRECTO:   se guarda su huella irreversible, con sal, y nadie la puede leer
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

**Nace el 2026-08-18 de partir `S5`**, cuyo título —*«CSRF, sesiones y transporte»*— **ya las enumeraba**. Un título que enumera es la señal de que son varias reglas: reprobaba las filas 8, 9, 10 y 12 a la vez, y las cuatro por lo mismo. Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Es la que menos se parecía a las otras tres.** `S5` la traía como cuarta viñeta —«hashing fuerte con salt»— entre cosas de transporte y sesión, y por eso [`12·PR3`](12-privacidad-datos.md#pr3--protégelos-en-reposo-y-en-tránsito) la citaba junto con el cifrado en tránsito, mezclando dos cosas distintas: **lo que se cifra se descifra; una contraseña no debe poder leerse nunca**.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
## S6 · El archivo no público se guarda privado y se sirve por un punto controlado

El archivo que no es público —financiero, jurídico, personal— se guarda **fuera de cualquier ubicación alcanzable por su dirección**, y se entrega solo a través de un punto que comprueba quién pide y si le corresponde.

```
INCORRECTO: el contrato queda en la carpeta pública con un nombre difícil de adivinar
CORRECTO:   queda en almacenamiento privado y se entrega tras comprobar el permiso
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Su cuerpo eran cinco viñetas y **dos exigencias distintas**: cómo se guarda y se entrega, y qué le pasa cuando su dueño se da de baja. **Se cumplen por separado** — se puede tener el archivo bien guardado y borrarlo físicamente al dar de baja la entidad padre, que es justo el caso que la segunda evita. Lo demás de esas viñetas —metadatos, copia de respaldo, lista blanca de tipos— era detalle de cómo, no exigencia, y se fue. La segunda es ahora [`S17`](#s17--el-archivo-sobrevive-a-la-baja-de-su-dueño). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S17 · El archivo sobrevive a la baja de su dueño

Dar de baja la entidad que referencia un archivo **no lo borra**. Quitarlo de verdad es una operación aparte, que se previsualiza antes de aplicarse ([`00·N5`](00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)).

```
INCORRECTO: se da de baja al proveedor y desaparecen sus facturas escaneadas
CORRECTO:   el proveedor queda de baja y sus archivos siguen ahí
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`S6`](#s6--el-archivo-no-público-se-guarda-privado-y-se-sirve-por-un-punto-controlado).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `S6` es sobre **el acceso**; esta es sobre **la permanencia**. Y es la que se incumple sin querer: la baja lógica del padre suele arrastrar sus archivos porque nadie pensó en ellos, y para cuando alguien los busca ya no están.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S7 · Dependencias sin vulnerabilidades conocidas  ·  `[DEROGADA en 23.17.0 → ver 10·DEP3]`

> **Dejó de regir: decía lo mismo que [`10·DEP3`](10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día)**, y las dos se citaban en círculo — `S7` remitía al capítulo `10` «para el detalle» y `DEP3` remitía de vuelta a `S7`. El dueño del tema *dependencias* es el capítulo `10` ([`20·M2`](20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)), así que se queda la de allá.
>
> **No se pierde nada:** `DEP3` ya exigía las dos cosas —auditar vulnerabilidades y no dejar una sin resolver— y agrega lo que `S7` no decía: que quedarse muy atrás vuelve caro e inseguro actualizar después.
>
> El texto original se conserva porque hay commits y fases que lo citan ([`20·M11`](20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

Mantén las dependencias al día y **audita vulnerabilidades** con la herramienta del ecosistema. No introduzcas una con vulnerabilidades sin resolver (detalle en `10`).

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ❌ N/A ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cabe —175 de 320—, tiene su ejemplo y dice lo suyo.

**El análisis del 2026-08-07 la marcaba por duplicar el tercer punto de [`05·E3`](05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico), y pedía elegir dueño. Ya está elegido, y es esta:** `E3` la **enlaza** como el motivo de que la traza no llegue al usuario, y se quedó con lo suyo —los dos niveles de mensaje—.

Se comprobó al sellar el capítulo `05` hoy, desde el otro lado, y coincide. **Es la misma solución que arregló [`08·T5`](08-pruebas.md#t5--ejecuta-y-reporta) y [`02·F5`](02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md):** no derogar ninguna, sino que la de al lado declare qué toma y se quede con lo que agrega.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S9 · No toques rutas del sistema fuera del proyecto · solo autorizadas exactas

El agente escribe **solo dentro de la carpeta del proyecto** o en rutas que el usuario autorizó **una por una y exactas**: autorizar un archivo no autoriza a su hermano ni a su carpeta padre. Leer fuera sí; escribir, no. Que el cambio «obviamente ayude» no es permiso ([qué rutas y por qué](../notas/rutas-fuera-del-proyecto.md)).
```
INCORRECTO: durante una fase, escribir en la carpeta home del usuario o en Program Files
            "porque es más práctico" → efecto lateral fuera del alcance del proyecto,
            imposible de auditar desde el repo
CORRECTO:   quedarse dentro del proyecto; si algo fuera realmente es necesario,
            reportarlo y esperar autorización de la ruta exacta
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

**Fila 10 · no cabe: 1278 caracteres, cuatro veces el molde.**

**Pero conviene leerla antes de acortarla, porque es el modelo de referencia del cuerpo entero.** El análisis del 2026-08-07 la señaló así: *«la excepción declara condición, límite y autorizador»* y recomendaba **usarla como plantilla**. Es la única del estándar que cumple [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) entera.

Eso importa hoy más que cuando se escribió: al aplicar el checklist aparecieron **tres excepciones sin autorizador** —[`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`03·D4`](03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo) y [`03·D5`](03-datos.md#d5--con-la-bd-desplegada-la-validación-nueva-va-en-la-app)— y esta es de dónde copiar la forma.

**Al acortarla, la excepción no se toca.** Lo que sobra es lo de alrededor.

**Fila 10 · arreglada el 2026-08-18.** Medía 1 278 caracteres para un molde de 320; ahora mide 290. Lo que sobraba era el **inventario de rutas prohibidas** y el desarrollo del principio — detalle, no exigencia. Se fue a [`notas/rutas-fuera-del-proyecto.md`](../notas/rutas-fuera-del-proyecto.md), con el caso que hace falta nombrar: *«te agrego una entrada al `hosts` para que funcione la prueba»*. Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S10 · No mates procesos globales · solo PID exacto y estrictamente necesario

El agente termina un proceso **por su identificador exacto**, y solo si es del proyecto y hace falta para la tarea — nunca por nombre ni por patrón, que tumba servicios que el usuario tiene abiertos en paralelo. Al arrancar algo persistente guarda su identificador, para poder cerrarlo después sin buscarlo.
**Excepción** — terminar por patrón se pide con el identificador y el motivo a la vista (condición); no vale nunca por defecto (límite) y lo autoriza el usuario, caso por caso (autorizador).
```
INCORRECTO: "hay procesos node colgados" → `killall node` → matas el IDE del usuario
            y los watchers de otros repos
CORRECTO:   identificar el PID exacto del proceso que arrancó la fase actual y matar
            solo ese PID
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

**Fila 10 · no cabe: 1029 caracteres.** Es lo único que reprueba.

**La fila 5 reprobaba por dos intérpretes nombrados, y se corrigió en esta pasada.** Sus ejemplos de patrón amplio decían `node` y `php`; ahora dicen «todos los procesos de tal intérprete», que es lo mismo sin nombrar ninguno. **No cambia qué prohíbe.**

**Lo que hay que anotar es cómo se le pasó.** El sello anterior sí argumentó la fila 5 —para defender `killall`, `pkill` y `taskkill`, que es lo llamativo— y **al hacerlo dio la fila por revisada**. Los dos intérpretes estaban tres líneas más arriba. Un argumento sobre una fila no es una revisión de la fila: quien lee el sello ve que alguien la miró, y no ve qué parte miró. Lo encontró la comprobación de [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), no una lectura.

**Los tres nombres del oficio se quedan**, y el motivo sigue valiendo: `killall`, `pkill` y `taskkill` no son producto ni framework sino cómo se llama la misma acción en cada sistema, y quitarlos dejaría la regla sin decir qué prohíbe. Es el mismo criterio con el que [`04·S11`](#s11--escritura-contra-el-almacén-productivo-requiere-autorización-por-operación) conserva el suyo.

Su excepción está completa, como la de `S9`.

**Fila 10 · arreglada el 2026-08-18.** Medía 1 029 caracteres para un molde de 320; ahora mide 307. **No hizo falta anexo:** las cinco viñetas eran una sola exigencia dicha cinco veces —por identificador exacto, solo si es del proyecto, solo si hace falta— más la lista de comandos prohibidos, que nombraba herramientas concretas y por [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no debía estar ahí. La excepción quedó escrita en la forma de [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S11 · Cada escritura contra datos reales se autoriza por separado

Cada `create`, `update` o `delete` contra el almacén productivo se autoriza **para esa operación puntual**: autorizar una no autoriza la siguiente, aunque sea del mismo tipo. Antes de pedirlo se describe qué operación, qué tabla, qué filas y qué campos (concreta [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).

```
INCORRECTO: «ya me autorizaste el UPDATE anterior, aprovecho y corro este otro»
CORRECTO:   «voy a correr UPDATE pedidos SET estado='X' WHERE id IN (12,13).
            ¿Autorizas?» — y se espera el sí para esa frase
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.20.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Partida el 2026-08-18, y su propio texto ya lo pedía.** Decía literalmente **«Regla 1»** y **«Regla 2»**: eran dos exigencias que se cumplen por separado —autorizar por operación, y contar el borrado lógico como escritura—, y la fila 9 las reprobaba. La segunda es ahora [`S12`](#s12--el-borrado-lógico-es-una-escritura).

**La fila 5 también estaba en ❌ y se arregló al partir.** El texto nombraba `destroy()` y `SoftDeletes`, que son de un framework concreto, y [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no lo admite en la base. **Toda esa parte se fue a `S12`**, escrita en concepto: «el método que suena a borrar y en realidad marca un campo». El nombre del método era el argumento, así que había que reescribirlo, no quitarlo — y eso solo se podía hacer partiendo.

**El detalle operativo dejó de estar aquí.** Qué se describe antes de pedir la autorización vive ahora en el cuerpo, en una línea, y lo largo se fue: era el desarrollo del motivo, no la exigencia.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## S12 · El borrado lógico es una escritura

El método que **suena a borrar y en realidad marca un campo** —una fecha de baja, un indicador de inactivo— escribe en el almacén productivo, y se autoriza igual que cualquier otra escritura (extiende [`04·S11`](#s11--cada-escritura-contra-datos-reales-se-autoriza-por-separado)). El nombre no cambia lo que hace.

```
INCORRECTO: «esto no borra nada, solo lo marca como inactivo» → se corre sin pedirlo
CORRECTO:   marcar la baja se describe y se autoriza como cualquier escritura
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.20.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`S11`](#s11--cada-escritura-contra-datos-reales-se-autoriza-por-separado)**, cuyo texto ya la llamaba «Regla 2». Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia y no una línea dentro de la otra.** `S11` dice **cuándo** se pide la autorización; esta dice **qué cuenta como escritura**. Se incumplen por separado: se puede pedir autorización por cada operación y aun así correr una baja lógica sin pedirla, creyendo que no escribe.

**Escrita en concepto, sin nombrar herramienta.** El original decía `destroy()`, `SoftDeletes`, `deleted_at`; [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no lo admite en la base, y **el nombre del método era el argumento** —que suene a borrar es justamente el peligro—, así que se reescribió en concepto en vez de quitarse.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
