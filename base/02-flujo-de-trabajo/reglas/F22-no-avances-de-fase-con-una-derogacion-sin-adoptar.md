> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F22 · No avances de fase con una derogación sin adoptar

Ninguna fase se abre ni se cierra mientras el proyecto declare una versión anterior a la que derogó una regla que ya cumplía. Lo único que se abre es la fase que la adopta, una por HU que la implementaba, y al cerrarla sube la versión declarada. Fuera de ahí el desfase se reporta y no detiene (depende de [`20·M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

```
INCORRECTO: se sube la versión declarada y se sigue trabajando, sin tocar las
            HU que implementaban la regla derogada
CORRECTO:   se abre una fase por cada HU que la implementaba, se aplica la regla
            que la reemplazó, y al cerrarla se sube la versión declarada
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14**: no declara `extiende`/`depende de`/`deroga`; sus citas a [`02·F12`](F12-relacion-y-nomenclatura-de-fases.md) y [`20·M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) son referencia, que [`20·M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción; la fase que adopta no es un permiso para incumplir, es la forma de cumplir.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

La fila **9** se revisó dos veces: abrir la fase y subir la versión declarada parecen dos exigencias, pero no se pueden cumplir por separado — subir el número sin la fase deja la regla nueva sin aplicar, y la fase sin subir el número deja el desfase en pie. Adoptar es una sola cosa.

La fila **4** también: el tema parece del capítulo [`20`](../../20-meta-reglas/base.md) porque habla de derogación, pero lo que la regla exige es cuándo se abre y se cierra una fase, y de eso es dueño este capítulo. Las meta-reglas son de procedimiento y nunca de fondo.

La fila **17** obligó a corregir dos textos que decían lo contrario: la nota de retroactividad de [`20 · base.md`](../../20-meta-reglas/base.md) y [`plantillas/stack-instalacion.md`](../../../plantillas/stack-instalacion.md), que daban el desfase como aviso siempre.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
