# 15 · Registros inmutables (patrón opt-in)  ·  `[CAPA 2 · opt-in]`

> **Historia dueña del texto:** [EP-001 HU-028](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-028-el-capitulo-15-registros-inmutables-patron-opt-in/HU-028-el-capitulo-15-registros-inmutables-patron-opt-in.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

**Opt-in.** Para registros cuyo hecho ya se materializó y tiene valor legal/contable/de auditoría: **no se editan ni se borran, se anulan con trazabilidad**. La capa 3 lo **activa** y dice a qué entidades aplica (documentos contables, transacciones, actas, comprobantes).

---

## IM1 · Un registro materializado es inmutable

Cuando un registro ya surtió efecto (movimiento contable generado, pago aplicado, saldo afectado, documento emitido), **no se edita ni se borra físico**. La única operación válida es **anular con motivo y trazabilidad**. En borrador (aún no materializado) sí se edita.

```
INCORRECTO: editar un documento materializado con un update, sin revertir su efecto
CORRECTO:   anularlo (con motivo, revirtiendo el efecto en transacción) y preservar la fila
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

La fila **8** pasa con un título declarativo, no imperativo. Es la misma forma que [`20·M11`](20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md), sellada en CUMPLE: el título **enuncia la norma** en vez de ordenarla, y se entiende leyéndolo en un índice. Lo que la fila no admite es un título que nombre un tema sin decir nada.

La fila **13** pasa sin marca propia: el `*opt-in*` está en la cabecera del capítulo y rige a las cinco reglas. Repetirlo en cada una sería el texto prestado que prohíbe la 11.

Las **14 a 16** son N/A: no declara dependencia en ninguna de las tres formas de [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), y no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IM2 · El registro tiene tres estados y solo uno es editable

El registro pasa por **borrador**, que se edita; **materializado**, que ya no; y **anulado**, que revierte el efecto **conservando la fila**. Nada se borra para corregirlo: se anula y se rehace.

```
INCORRECTO: la factura salió mal, se edita el registro ya emitido
CORRECTO:   se anula la emitida —queda su fila— y se emite otra
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

**Partida el 2026-08-18.** Su propio título decía dos cosas —*«los tres estados **y** la trazabilidad de quien anula»*— y se cumplen por separado: **se pueden tener los tres estados y anular sin guardar quién ni por qué**. Lo segundo es ahora [`IM6`](#im6--anular-deja-escrito-quién-cuándo-y-por-qué). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IM3 · La anulación revierte todo o no revierte nada

Anular comprueba primero que el estado lo permita, y después revierte **en una sola transacción** todos los efectos que el registro produjo — movimientos, saldos, derivados — junto con la marca de anulado. Si algo de la reversión falla, no queda nada a medias ([`05·E6`](05-errores-y-logging.md#e6--lo-que-toca-varios-registros-va-en-transacción)).

```
INCORRECTO: se marca anulado, se revierte el movimiento y falla el saldo
            → el registro dice anulado y el saldo dice que no
CORRECTO:   o se revierten los tres y la marca, o no se revierte ninguno
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

**Partida el 2026-08-18.** Sus cuatro pasos eran **dos exigencias**: revertir de forma atómica, y avisar a los demás módulos para que suelten lo que tenían calculado. **Se cumplen por separado**, y de hecho la segunda se olvida con la reversión perfecta: los saldos quedan bien en el almacén y mal en lo que alguien ya había calculado. Es ahora [`IM7`](#im7--al-anular-se-avisa-a-quien-tenía-el-dato-calculado). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IM7 · Al anular se avisa a quien tenía el dato calculado

La anulación **avisa** a los demás módulos para que descarten lo que tenían derivado de ese registro: totales, resúmenes, lo que se hubiera guardado calculado (extiende [`15·IM3`](#im3--la-anulación-revierte-todo-o-no-revierte-nada)).

```
INCORRECTO: la factura se anula y el total del mes la sigue contando
CORRECTO:   al anularla, lo que la había sumado se entera y se rehace
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

**Nace el 2026-08-18 de partir [`IM3`](#im3--la-anulación-revierte-todo-o-no-revierte-nada).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `IM3` deja el almacén correcto; esta deja correcto **lo que ya se había leído de él**. Se incumple sola y es la más difícil de notar: nada falla, solo que un número viejo sigue a la vista.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IM4 · Las consultas agregadoras excluyen los anulados

Toda consulta que sume/cuente/promedie **excluye** los anulados. Idealmente por **defecto** en el modelo/consulta, no confiando en que cada consulta lo recuerde.

```
INCORRECTO: un reporte que suma incluyendo anulados "y que el usuario tenga cuidado"
CORRECTO:   la consulta excluye anulados por defecto
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

Título declarativo, como el de `IM1`: enuncia la norma. La fila **9** pasa porque el «idealmente por defecto en el modelo» no es una segunda exigencia sino **cómo** cumplir la primera sin depender de que cada consulta se acuerde — que es la diferencia entre una regla que se cumple y una que se recuerda.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## IM5 · Permiso propio para anular

Anular pesa más que crear o editar: **permiso separado** del de eliminar, para roles con responsabilidad ([`04·S1`](04-seguridad.md#s1--autorización-en-cada-acción-sensible)). En la UI, los materializados ofrecen "Anular" (motivo obligatorio) en vez de "Eliminar"; los anulados quedan visibles, marcados y con su motivo.

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ N/A ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 0 ❌ · 4 N/A.**

El título dice la norma: **debe haber** un permiso propio. No nombra un tema.

La fila **9** pasa: lo de la interfaz —ofrecer «Anular» en vez de «Eliminar»— no es una exigencia aparte sino dónde se nota la primera. Sin permiso separado, la interfaz no tendría qué distinguir.

La fila **12** es N/A: la regla ya contrasta los dos comportamientos dentro de su propio cuerpo.

La cita a [`04·S1`](04-seguridad.md#s1--autorización-en-cada-acción-sensible) es el motivo de que el permiso sea propio, no una de las tres dependencias de [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md). Por eso las **14 a 16** son N/A.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `03` D1 (auditoría, soft delete), `05` E2 (transacción), `04` S1 (permiso/scope), `12` PR5 (anonimizar en vez de borrar).

## IM6 · Anular deja escrito quién, cuándo y por qué

La anulación guarda **quién la hizo, cuándo, y el motivo** — un motivo con sustancia, no una palabra. Sin eso la fila conservada dice que algo se revirtió y no dice nada más (extiende [`15·IM2`](#im2--el-registro-tiene-tres-estados-y-solo-uno-es-editable)).

```
INCORRECTO: motivo: «error»
CORRECTO:   motivo: «se emitió al cliente equivocado; se rehace con el 4021»
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

**Nace el 2026-08-18 de partir [`IM2`](#im2--el-registro-tiene-tres-estados-y-solo-uno-es-editable).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `IM2` dice **qué estados hay**; esta dice **qué queda escrito al pasar al último**. Se incumple sola, y es la que más se incumple: conservar la fila es fácil, escribir un motivo con sustancia no.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
