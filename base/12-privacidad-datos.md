# 12 · Privacidad y datos personales  ·  `[CAPA 2]`

Cómo tratar los datos de las personas. Más allá de la seguridad técnica (`04`), es un compromiso y a menudo una obligación legal. La capa 3 declara el marco normativo y la retención concretos.

---

## PR1 · Recolecta solo lo necesario (minimización)

No pidas ni guardes datos personales que la función no necesita. Cada dato guardado es riesgo y responsabilidad. Prefiere el dato menos sensible que resuelva el problema.

```
INCORRECTO: guardar documento y dirección "por si acaso"
CORRECTO:   guardar solo lo que la función usa de verdad
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

El análisis del 2026-08-07 en [analisis/base-2026-08-07-cumplimiento-meta-reglas.md](../analisis/base-2026-08-07-cumplimiento-meta-reglas.md) ya la daba por cumplida, y se revisó fila por fila antes de sellar. Coincide.

El título lleva «(minimización)» entre paréntesis: es el nombre que el oficio le da a la exigencia, no una segunda exigencia. La fila **9** pasa.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## PR2 · Úsalos solo para lo que se recolectaron

Los datos se usan para el propósito con que se obtuvieron. No los reutilices para otro fin (analítica, marketing, terceros) sin base legítima y consentimiento. No los envíes a servicios externos sin autorización ([`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)).

```
INCORRECTO: los correos se pidieron para avisar del pedido y se usan para una
            campaña, porque «ya los tenemos»
CORRECTO:   para la campaña se pide consentimiento aparte, y quien no lo da
            sigue recibiendo el aviso del pedido
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

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. El que se agregó es el error de verdad —los correos que se pidieron para avisar del pedido y terminan en una campaña «porque ya los tenemos»—, no uno exagerado. **No cambia qué exige la regla.**

La fila **9** pasa: no reutilizar para otro fin y no enviar a terceros son la misma exigencia —el propósito manda— vista adentro y afuera del sistema.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## PR3 · Protégelos en reposo y en tránsito

Datos personales cifrados en tránsito ([`04·S5`](04-seguridad.md#s5--csrf-sesiones-y-transporte)) y, si son sensibles, en reposo o con acceso restringido ([`04·S6`](04-seguridad.md#s6--archivos-sensibles-privado--acceso-controlado)). Acceso limitado por **permiso y scope** ([`04·S1`](04-seguridad.md#s1--autorización-en-cada-acción-sensible)). Credenciales con hashing fuerte, nunca en claro ([`04·S5`](04-seguridad.md#s5--csrf-sesiones-y-transporte)).

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ✅ ❌ N/A ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 14 ✅ · 2 ❌ · 4 N/A.**

**Esta es la grave del capítulo, y el análisis del 2026-08-07 ya la tenía en rojo:** *«no exige nada propio: cuatro remisiones a `04`»*.

- **Fila 9 · una sola exigencia.** No tiene ninguna **propia**. Sus cuatro frases son cifrado en tránsito, cifrado en reposo, acceso por permiso y hashing de credenciales, y las cuatro remiten a [`04·S5`](04-seguridad.md#s5--csrf-sesiones-y-transporte), [`04·S6`](04-seguridad.md#s6--archivos-sensibles-privado--acceso-controlado) y [`04·S1`](04-seguridad.md#s1--autorización-en-cada-acción-sensible). Una regla que solo apunta a otras no exige: **es un índice con forma de regla**, y quien la cumple no hace nada distinto de cumplir el capítulo `04`.
- **Fila 11 · sin texto prestado.** Es la otra cara de lo mismo: enlaza bien, pero lo que queda entre los enlaces es la reformulación de lo enlazado.

**Qué habría que hacer, y no se hace acá.** O la regla se queda con lo que el capítulo `04` **no** dice —qué agrega la privacidad sobre la seguridad técnica: qué dato personal es «sensible», quién decide el nivel de protección, qué exige el marco normativo del proyecto— o **se deroga** y el capítulo remite al `04` en su cabecera, que ya lo hace. Las dos son cambio de regla y van al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

La fila **12** es N/A: sin exigencia propia no hay ejemplo que dar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## PR4 · No los expongas en logs, errores ni mensajes

Logs y errores sin datos personales más allá de lo imprescindible: usa identificadores, no el dato en claro ([`05·E5`](05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles)). Los mensajes a otros usuarios no filtran datos de terceros. Reportes y pantallas muestran datos solo a quien tiene derecho.

```
INCORRECTO: loguear nombre, correo y teléfono en cada operación
CORRECTO:   loguear un identificador; el dato queda en la BD con acceso controlado
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 11 · sin texto prestado.** «Logs y errores sin datos personales… usa identificadores, no el dato en claro» es [`05·E5`](05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles) dicha otra vez con otras palabras — y `E5`, a su vez, reformula [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada). **Tres capas del mismo criterio**, como decía el análisis del 2026-08-07.

Enlazarla no basta: la fila pide que lo que ya dice otra regla esté **enlazado en vez de copiado**, y acá está enlazado **y** copiado.

**Tiene parte propia, y es la que la salva de derogarse:** los mensajes a otros usuarios no filtran datos de terceros, y reportes y pantallas muestran datos solo a quien tiene derecho. Eso no lo dice `E5` — `E5` habla de logs, no de pantallas. **El arreglo es quedarse con esa mitad y enlazar la otra.** Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## PR5 · Define cuánto se conservan y qué pasa después

Define **cuánto tiempo** se conservan; no indefinido "porque sí". Prevé **borrado o anonimización** cuando ya no se necesitan o la persona lo pide. Si el registro tiene valor legal/contable que impide borrarlo (`15`), **anonimiza** los datos personales conservando el registro. Documenta la decisión.

```
INCORRECTO: conservar para siempre los datos de cuentas inactivas
CORRECTO:   retención definida + borrado/anonimización al cumplirse el plazo
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

**La fila 8 reprobaba y se corrigió en esta pasada.** El título era «Retención y borrado»: nombra un tema y no dice ninguna norma. Pasa a *Define cuánto se conservan y qué pasa después*. El cuerpo no se tocó, así que **no cambia qué exige la regla**. Es el mismo arreglo que se le hizo a [`15·IM2`](15-registros-inmutables.md#im2--guarda-los-tres-estados-y-la-trazabilidad-de-quien-anula) hoy.

La fila **9** pasa aunque el cuerpo diga tres cosas —plazo, borrado o anonimización, y documentar la decisión—: no se cumplen por separado. Un plazo sin qué hacer al cumplirse no es una política de retención, es una fecha.

La remisión a `15` cuando el registro tiene valor legal es un enlace al capítulo dueño, no una dependencia declarada: la fila **14** es N/A.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `04` (controles técnicos), `05` E5 (logs), `15` (anonimizar en vez de borrar), `00` N6.
