# 07 · Calidad de código  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-020](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-020-el-capitulo-07-calidad-de-codigo/HU-020-el-capitulo-07-calidad-de-codigo.md). Todo cambio de este capítulo baja por ella (`02·F23`).

El código se lee más veces de las que se escribe: optimiza para el lector. La capa 3 declara linter, formateador y estilo.

---

## Q1 · Escribe como el código que lo rodea

El código nuevo imita al vecino: mismas convenciones, mismos nombres, mismo idioma ([`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto)). No metas un paradigma ajeno sin acordarlo. La consistencia vale más que la preferencia personal.

```
INCORRECTO: el archivo nuevo trae un estilo distinto al del módulo
CORRECTO:   se mimetiza con el código vecino
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

Cumplía en el análisis del 2026-08-07 y las once filas que se cuentan se volvieron a contar: 190 de 320.

La fila **5** pasa: la regla habla de «el código que lo rodea» sin nombrar ningún lenguaje, que es justo lo que la hace agnóstica — imitar al vecino significa algo distinto en cada stack y la regla no necesita saber cuál.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## Q2 · Nombres que dicen la intención

Nombres descriptivos por lo que representan o hacen, no por su tipo ni abreviados. Evita genéricos (`data`, `temp`, `proceso`). Funciones con verbo; booleanos como afirmación (`estaActivo`, `tienePermiso`). Un buen nombre ahorra un comentario.

```
INCORRECTO: function proc(d) { ... }
CORRECTO:   function calcularSaldoDisponible(cuenta) { ... }
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

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 243 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## Q3 · Funciones pequeñas, una responsabilidad

Cada función hace **una cosa**, a un solo nivel de abstracción. Si necesita comentarios que separan bloques, esos bloques son funciones. Usa retornos tempranos en vez de pirámides de `if`.

```
INCORRECTO: una función de 200 líneas que valida, calcula, guarda y notifica
CORRECTO:   una que orquesta validar(), calcular(), guardar(), notificar()
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

Cumplía en el análisis del 2026-08-07. Está clasificada y con validador escrito —`calidad.py`—, así que la fila **18** pasa con programa detrás y no solo con el registro.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## Q4 · No repitas (DRY), pero no abstraigas de más

Lógica de negocio duplicada se extrae a un punto único. **Pero** no abstraigas prematuro: dos usos parecidos no siempre son el mismo concepto. Duplicar una vez y esperar el patrón es válido.

```
INCORRECTO: la misma regla copiada en tres lados → se corrige en dos y se olvida el tercero
CORRECTO:   la regla en un servicio; los tres lo llaman
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

**El título lleva un «pero», y aun así la fila 9 pasa.** El análisis del 2026-08-07 la marcó como caso límite y dio la razón exacta: *«dos exigencias en tensión; la tensión **es** el contenido»*.

No abstraer de más no es una segunda exigencia sino **el límite** de la primera. Separarlas produciría dos reglas que se contradicen leídas por separado —una diría «extrae siempre», la otra «no extraigas»— y quien las lea sin la otra hará justo lo que la regla evita.

**La recomendación de entonces no se aplicó, y queda dicho por qué.** Era escribir la segunda mitad como excepción formal de [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), y `M8` pide **condición, límite y quién autoriza**. Acá no hay quién autorice: no es una excepción que alguien concede, es criterio de diseño que se ejerce al escribir. Forzarla al molde de la excepción diría algo falso.

Si más adelante se decide lo contrario, es cambio de regla y va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## Q5 · Comenta el porqué, no el qué

El código dice **qué**; el comentario, **por qué** (una decisión no obvia, un workaround). No comentes lo que el código ya dice. Las decisiones de diseño van a la documentación (`13`), no a un comentario que nadie relee.

```
INCORRECTO: i = i + 1 // incrementa i
CORRECTO:   // reintenta 3 veces porque el servicio externo falla intermitente
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

Cumplía en el análisis del 2026-08-07. Se volvió a contar: 220 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## Q6 · Linter y formateador automáticos

El estilo lo resuelve una **herramienta**, no el criterio manual. Entrega el código formateado y sin advertencias del linter. No desactives reglas para "que pase" ([`00·N3`](00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)); si una estorba, ajusta la config, no la silencies caso por caso.

```
INCORRECTO: el linter marca una regla molesta y se silencia con un comentario
            en cada uno de los doce sitios donde aparece
CORRECTO:   se decide si la regla aplica al proyecto; si no, se apaga en la
            config, una vez y a la vista de todos
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

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. El que se agregó es el error de verdad —silenciar la regla del linter en cada uno de los doce sitios en vez de decidir si aplica— y sale del propio cuerpo, que ya lo prohibía sin mostrarlo. **No cambia qué exige la regla.**

Está clasificada y con validador escrito —`herramientas.py`—, así que la fila **18** pasa con programa detrás.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## Q7 · Deja el código mejor, pero en tu alcance

Corregir algo pequeño y cercano está bien; mejorar de paso lo que no es de la tarea sale del alcance ([`01·C3`](01-conducta.md#c3--quédate-en-tu-tarea)) e infla el diff. Si algo cercano merece mejora, **dilo y déjalo para su tarea**.

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.3**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ N/A ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 0 ❌ · 4 N/A.**

**La fila 11 reprobaba y se corrigió en esta pasada.** Decía *«refactorizar de más o mejorar de paso fuera de la tarea, no»*, que es [`01·C3`](01-conducta.md#c3--quédate-en-tu-tarea) dicha otra vez: la enlazaba **y** la repetía, y la fila pide enlazar **en vez de** copiar.

**El modelo estaba al lado, en el mismo cuerpo.** [`14·EST3`](14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `C3` el mismo criterio de alcance y cumple: **la nombra entre paréntesis como el motivo** y todo lo demás que dice es suyo. `Q7` reformulaba el criterio entero antes de enlazarlo, y lo propio era una frase al final.

Ahora dice lo mismo en 191 caracteres — eran 211. **No cambia qué exige:** lo que se fue era la parte que ya regía por `C3`.

**Fila 12 · N/A.** Lo que hay que hacer y lo que no está dicho en la propia frase, y un ejemplo repetiría el texto.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
