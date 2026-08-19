> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M2 · Un tema, un capítulo, un dueño

Cada dominio tiene **un** archivo `NN-nombre.md` y ese archivo es la **fuente única** de su tema. Si una regla de otro capítulo necesita hablar del mismo tema, **enlaza**, no repite.

```
INCORRECTO: la regla de índices se escribe en el capítulo de datos y otra vez en el de rendimiento
CORRECTO:   vive en el de rendimiento; el de datos la enlaza
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v2.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ❌ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

**❌** — **17**: no contempla que el preámbulo comparta el número `00` con el núcleo.

> **Regla vigente y reprobada.** Sigue rigiendo —[`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado— pero no es conforme hasta resolver el choque, y eso es decisión del usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
