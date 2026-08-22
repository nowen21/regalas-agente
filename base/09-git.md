# 09 · Control de versiones  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-022](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-022-el-capitulo-09-control-de-versiones/HU-022-el-capitulo-09-control-de-versiones.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

El mínimo está en [`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada): **commit** y **push** solo bajo pedido explícito, autorización de un solo uso. Aquí, cómo hacerlo bien cuando toca.

---

## G1 · Commits atómicos, un solo propósito

Un commit = un cambio coherente (una feature, un fix, un refactor). No mezcles cosas sin relación. Debe poder revertirse solo, sin arrastrar lo ajeno.

```
INCORRECTO: un commit "varios cambios" con feature + fix + reformateo
CORRECTO:   uno por la feature, otro por el fix, otro por el formateo
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

Cumplía en el análisis del 2026-08-07 y se volvió a contar: **150 de 320, la más corta del capítulo**. Es también la que más se concreta desde otras: `G9` la nombra para decir que el propósito de un commit es la historia de usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G2 · Mensajes que explican qué y por qué

Primera línea breve e imperativa; si hace falta, un cuerpo con el **por qué** (el qué ya está en el diff). En el idioma del proyecto ([`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto)).

```
INCORRECTO: "cambios", "fix", "wip"
CORRECTO:   "Corrige el saldo cuando hay documentos anulados

            Se sumaban al total; ahora se excluyen en la consulta."
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

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 143 de 320.

**Su título lleva una «y» y aun así la fila 9 pasa**, y conviene decir por qué porque es el caso que [base/20-meta-reglas/estructura-regla.md](20-meta-reglas/estructura-regla.md) usa como ejemplo de «y» legítimo: qué y por qué no son dos exigencias sino las dos preguntas que un mensaje de commit responde. Un mensaje que dice qué sin decir por qué no cumple a medias — no cumple.

Está clasificada y con validador escrito —`commits.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G3 · Deja fuera del control de versiones los secretos y lo generado

Al archivo de exclusión (`.gitignore`): **secretos** (claves, tokens, entorno real — [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)), **datos sensibles/reales**, **artefactos generados** (dependencias, compilados, cachés, logs), **config local** de máquina/editor. Se versiona una **plantilla de ejemplo** sin valores.

```
INCORRECTO: commitear el archivo de entorno con la clave de producción
CORRECTO:   ignorar el real; versionar solo la plantilla sin secretos
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

**La fila 8 reprobaba y se corrigió en esta pasada.** El título era «Qué nunca se versiona»: nombra un tema y no enuncia ninguna norma. Pasa a *Deja fuera del control de versiones los secretos y lo generado*. **No cambia qué exige la regla.** Es el sexto título así corregido hoy.

La fila **11** pasa aunque solape con [`11·CFG2`](11-configuracion-entornos.md#cfg2--el-entorno-real-no-se-versiona-sí-una-plantilla) y [`04·S4`](04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso): esta dice **qué se excluye** —la lista completa, no solo secretos— y aquellas dicen qué se versiona en su lugar. Son caras distintas, y el análisis del 2026-08-07 pedía «repartir dueños», que es lo que ya está.

Cabe: 279 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G4 · Trabaja en ramas, integra limpio

El trabajo va en una **rama** dedicada (salvo que la capa 3 diga otra cosa). Mantenla al día con la principal. La rama principal queda siempre **funcional**.

```
INCORRECTO: se trabaja directo sobre la principal «porque es un cambio chico»
CORRECTO:   rama para el cambio, al día con la principal, y la principal
            siempre en verde
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

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. **No cambia qué exige la regla.**

Cabe de sobra —157 de 320— y está clasificada con validador escrito, `rama.py`.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G5 · No reescribas historia compartida ni fuerces sin necesidad

Reescribir historia (rebase, enmienda, purga) y **push forzado** solo sobre historia no compartida, o con acuerdo explícito si ya es pública (afecta a quien la clonó). Cada una requiere autorización ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)). No fuerces con banderas destructivas ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).

```
INCORRECTO: rechazan el push → hago push --force por mi cuenta
CORRECTO:   reporto el rechazo, explico la causa y espero decisión
```

---

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

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 257 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G6 · Las pruebas y el linter corren solos en cada cambio propuesto

La suite y el linter corren en un **entorno reproducible que no depende de que alguien se acuerde**, sobre cada cambio propuesto, y la rama principal no admite lo que no está en verde.

```
INCORRECTO: «las corrí en mi máquina y pasaban» → se integra
CORRECTO:   corren solas sobre el cambio propuesto, y si algo falla no entra
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

**Partida el 2026-08-18.** Decía dos cosas: que la comprobación corra sola, y que lo local complemente sin reemplazarla. **Se cumplen por separado** — se puede tener todo automatizado y aun así saltarse el enganche local, o al revés, confiar en el enganche y no tener nada corriendo solo. Lo segundo es ahora [`G11`](#g11--lo-que-corre-en-tu-máquina-complementa-no-reemplaza). Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G11 · Lo que corre en tu máquina complementa, no reemplaza

El enganche local es una ayuda para no mandar lo evidente, **no la comprobación**: no la sustituye y no se salta ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)). Lo que el entorno automático no puede cubrir queda como comprobación manual escrita ([`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)).

```
INCORRECTO: se salta el enganche local «porque el pipeline igual lo va a revisar»
CORRECTO:   se arregla lo que el enganche señaló, y el pipeline vuelve a mirarlo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.23.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`G6`](#g6--las-pruebas-y-el-linter-corren-solos-en-cada-cambio-propuesto).** Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**Por qué merece regla propia.** `G6` es sobre **que exista** la comprobación automática; esta es sobre **no confundirla con la de tu máquina**. Es la que se incumple con una excusa razonable — *«el pipeline igual lo revisa»*—, y esa excusa es exactamente lo que `00·N3` prohíbe.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G7 · Todo commit se muestra al usuario y se aprueba antes de ejecutarlo

Antes de confirmar y de publicar, el agente **muestra el mensaje completo y los archivos afectados** y **espera aprobación explícita**. Primero se lee, después se aprueba, y recién ahí se ejecuta.

Aceptar el cambio **no** autoriza a guardarlo: son dos permisos ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

```
INCORRECTO: hago el cambio y en el mismo paso hago commit/push · "ya que estaba, lo subí"
CORRECTO:   hago el cambio → muestro el mensaje + los archivos → espero "sube / aprobado" → recién ahí commit/push
```

---

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

**La fila 10 reprobaba y se corrigió en esta pasada: de 421 caracteres a 270**, para un molde de 320. Se fueron los nombres de las órdenes, que además reprobaban la fila 5 en otras reglas del cuerpo. **Los dos permisos separados siguen siendo el corazón de la regla.**

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G8 · El cuerpo del commit abre con la idea del usuario

El cuerpo arranca con **lo que el usuario quiso**, y después con lo que hizo el agente. El origen del cambio es la necesidad, no la ejecución: quien lea el historial mañana busca el porqué.

```
INCORRECTO: «Se agregó validación en el servicio y se actualizaron 3 pruebas.»
CORRECTO:   «Pediste que no se pudiera cerrar una venta sin cliente. Va la
            validación en el servicio, con sus tres casos.»
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.20.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18, y su propio texto ya lo pedía:** decía *«Dos consecuencias»* y las enumeraba. Eran dos exigencias que se cumplen por separado —se puede abrir el cuerpo con la idea del usuario y aun así firmar el commit con la herramienta—, y las filas 8, 9 y 10 lo reprobaban. La segunda es ahora [`G10`](#g10--el-commit-no-se-firma-con-la-herramienta).

**El título también cambió.** *«El mensaje es del proyecto, no de la herramienta»* describía **las dos mitades a la vez** y no se sostenía solo en un índice, que es lo que pide la fila 8. Ahora cada una dice lo suyo.

Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G10 · El commit no se firma con la herramienta

El mensaje no lleva **ninguna marca de con qué se escribió**: ni coautoría de la herramienta, ni línea de «generado con», ni firma de agente. Quién hizo el commit ya lo dice el propio control de versiones (extiende [`09·G8`](#g8--el-cuerpo-del-commit-abre-con-la-idea-del-usuario)).

```
INCORRECTO: al final del mensaje, una línea que declara la herramienta como coautora
CORRECTO:   el mensaje termina en lo último que había que contar del cambio
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

**Nace el 2026-08-18 de partir [`G8`](#g8--el-cuerpo-del-commit-abre-con-la-idea-del-usuario)**, cuyo texto ya la llamaba la segunda de *«dos consecuencias»*. Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**Por qué merece regla propia.** `G8` dice **por dónde abre** el mensaje; esta dice **qué no puede llevar**. Se incumplen por separado, y de hecho la segunda es la que se incumple sola: un mensaje puede abrir perfectamente con la idea del usuario y traer la firma pegada al final.

**Escrita sin nombrar la herramienta**, que era la otra mitad del defecto: el texto anterior decía el nombre literal de la línea de coautoría, y [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no lo admite en la base. Lo que se exige es que **no haya marca de herramienta**, cualquiera que sea — la lista de nombres concretos envejece con cada versión.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G9 · La historia de usuario es la unidad del commit

Lo de una historia —documento, fases, código— va en un commit que **no toca otra**, y lo que aún no tiene historia espera a tenerla (concreta a [`G1`](#g1--commits-atómicos-un-solo-propósito)).
Excepción: lo que no es de ninguna historia sube con la primera que lo necesite.

```
INCORRECTO: un commit con HU-002, HU-003 y las épicas que todavía no
            tienen historias escritas
CORRECTO:   un commit por historia; la épica sin historias espera a tenerlas
```

Comprobable: un commit que toca dos carpetas de HU distintas se detecta comparando rutas.


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

**La fila 10 reprobaba y se corrigió en esta pasada: de 552 caracteres a 319**, para un molde de 320. Se apretó la redacción y se fue la cita a [`02·F12`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), que no aportaba exigencia. **La excepción conserva su condición y su límite**, que es lo único que no se podía tocar.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
