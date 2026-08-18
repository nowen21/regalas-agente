# 09 · Control de versiones  ·  `[CAPA 2]`

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 143 de 320.

**Su título lleva una «y» y aun así la fila 9 pasa**, y conviene decir por qué porque es el caso que [base/20-meta-reglas/estructura-regla.md](20-meta-reglas/estructura-regla.md) usa como ejemplo de «y» legítimo: qué y por qué no son dos exigencias sino las dos preguntas que un mensaje de commit responde. Un mensaje que dice qué sin decir por qué no cumple a medias — no cumple.

Está clasificada y con validador escrito —`commits.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G3 · Deja fuera del control de versiones los secretos y lo generado

Al archivo de exclusión (`.gitignore`): **secretos** (claves, tokens, entorno real — [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)), **datos sensibles/reales**, **artefactos generados** (dependencias, compilados, cachés, logs), **config local** de máquina/editor. Se versiona una **plantilla de ejemplo** sin valores.

```
INCORRECTO: commitear el archivo de entorno con la clave de producción
CORRECTO:   ignorar el real; versionar solo la plantilla sin secretos
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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 257 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G6 · Integración continua: el verde es automático, no manual

Las **pruebas y el linter** corren en un **pipeline reproducible** (CI), no dependen de que alguien se acuerde. La rama principal se protege: **no se integra algo que no está en verde**.

- El pipeline corre la suite y el linter en cada cambio propuesto (pull request / pre-merge); si algo falla, no se mergea.
- Los hooks locales (pre-commit) **complementan**, no reemplazan al CI. No se saltan ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
- Lo que el entorno de pruebas no cubre queda como verificación manual documentada ([`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)).

```
INCORRECTO: "corré las pruebas antes de mergear" dependiendo de que el dev lo haga
CORRECTO:   el CI corre pruebas + lint automáticamente; el merge exige verde
```

---

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

- **Fila 9 · son tres sub-exigencias:** que el pipeline exista y esté verde, que los enganches locales lo complementen sin reemplazarlo, y la verificación manual de lo que el pipeline no cubre. Se cumplen por separado — un proyecto puede tener el pipeline impecable y ninguna verificación manual escrita.
- **Fila 10 · no cabe:** 496 caracteres.

El análisis del 2026-08-07 dejaba las dos salidas abiertas: partirla, o declarar que son caras de un mismo invariante. **Acá no lo son**, a diferencia de [`08·T3`](08-pruebas.md#t3--aisladas-deterministas-repetibles) o [`06·R2`](06-rendimiento.md#r2--nunca-cargues-conjuntos-sin-límite): el pipeline y la verificación manual cubren cosas distintas y ninguna implica a la otra.

Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G7 · Todo commit se muestra al usuario y se aprueba antes de ejecutarlo

Antes de `git commit` (y del `push`), el agente **muestra al usuario el mensaje completo del commit y los archivos afectados**, y **espera aprobación explícita**. El usuario primero lee, luego aprueba; recién ahí se ejecuta.

Aceptar un cambio en los archivos **no** autoriza a commitearlo: son dos permisos distintos ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada) — autorización de un solo uso). No encadenar el commit en la misma acción que produjo el cambio.

```
INCORRECTO: hago el cambio y en el mismo paso hago commit/push · "ya que estaba, lo subí"
CORRECTO:   hago el cambio → muestro el mensaje + los archivos → espero "sube / aprobado" → recién ahí commit/push
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
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 10 · no cabe: 421 caracteres.** Es lo único que reprueba, y el análisis del 2026-08-07 la daba por cumplida: quinto caso en que esa fila estaba medida a ojo.

**La fila 9 sí pasa pese al «y» del título**, y el análisis lo dejó dicho: no se puede aprobar lo que no se mostró. Mostrar y aprobar son un solo acto en dos tiempos, como el qué y el porqué de `G2`.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G8 · El mensaje es del proyecto, no de la herramienta

El historial cuenta **qué se decidió y por qué**, no con qué se escribió. Dos consecuencias:

**El cuerpo arranca con la idea del usuario, y después lo que hizo el agente.** El origen del cambio es la necesidad, no la ejecución. Quien lea el historial mañana busca el porqué, no el cómo.

**Nunca se firman los commits con la herramienta.** Sin `Co-Authored-By`, sin líneas de "generado con", sin marcas de agente. El autor del commit ya lo dice el propio git.

```
INCORRECTO: "Agrega validación de saldo

            Se implementó el chequeo en el servicio.

            Co-Authored-By: <herramienta>"

CORRECTO:   "Agrega validación de saldo

            El usuario reportó que se podían registrar pagos mayores al
            saldo pendiente. Se agrega el chequeo en el servicio y su prueba."
```

Comprobable: `validadores/validar.py commit` (regla [`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto) para el idioma).

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

**Se autodeclara doble: dice literalmente «Dos consecuencias».**

- **Fila 9 · son dos**, y se cumplen por separado sin dificultad: un mensaje puede arrancar con la idea del usuario y traer la firma de la herramienta al final.
- **Fila 8 · el título nombra un principio**, no la exigencia. «El mensaje es del proyecto, no de la herramienta» es el porqué de las dos consecuencias.
- **Fila 10 · no cabe:** 532 caracteres.

**El análisis del 2026-08-07 propuso el corte y ya se hizo a medias:** decía *«`G8` orden del cuerpo · `G9` sin firma de herramienta»*, y hoy existe una `G9` — pero es otra cosa, la historia de usuario como unidad del commit. **El número que el análisis reservaba para la mitad de `G8` está ocupado.**

Eso hay que saberlo antes de partirla: la mitad que salga se lleva `G10`, no `G9`. Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## G9 · La historia de usuario es la unidad del commit

Lo que pertenece a una historia de usuario (su documento, sus fases, su código) se guarda en un commit que **no toca otra historia**, y lo que todavía no tiene su historia escrita no se sube: espera a tenerla.
Concreta a [`G1`](#g1--commits-atómicos-un-solo-propósito), que pide un propósito por commit: acá el propósito es la HU ([`02·F12`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)).
Excepción: lo que no es de ninguna HU y una HU necesita para no citar lo que no está (el planteamiento, el documento de su épica) sube con la primera que lo necesite.

```
INCORRECTO: un commit con HU-002, HU-003 y las épicas que todavía no
            tienen historias escritas
CORRECTO:   un commit por historia; la épica sin historias espera a tenerlas
```

Comprobable: un commit que toca dos carpetas de HU distintas se detecta comparando rutas.


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

**Fila 10 · no cabe: 552 caracteres.** Es lo único que reprueba.

**No estaba en el análisis del 2026-08-07 porque nació después**, y por eso su bloque se aplicó entero desde cero en vez de contrastarlo. Cabe anotar que una regla nueva llega igual de larga que las viejas: el molde de cuatro líneas no se respeta ni con el checklist recién escrito a la vista.

La fila **14** pasa y es de las pocas del cuerpo que declara dependencia en la forma que [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) admite: *«concreta a `G1`»*. Su excepción —lo que no es de ninguna historia sube con la primera que lo necesite— declara condición y límite; le falta el autorizador, pero es del mismo tipo que la de [`04·S9`](04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas), no de las tres que se autorizan solas.

Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `00` N2/N3/N6, `07` Q6 (lint), `08` (pruebas), `11` (config fuera del código), `13` (decisiones también en docs).
