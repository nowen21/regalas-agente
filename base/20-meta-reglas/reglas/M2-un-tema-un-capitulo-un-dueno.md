> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M2 · Un tema, un capítulo, un dueño

Cada dominio tiene **un** archivo `NN-nombre.md` y ese archivo es la **fuente única** de su tema. Si una regla de otro capítulo necesita hablar del mismo tema, **enlaza**, no repite. El preámbulo del `00` comparte número con el núcleo porque lo anexa: no es otro capítulo ni otro dueño.

```
INCORRECTO: la regla de índices se escribe en el capítulo de datos y otra vez en el de rendimiento
CORRECTO:   vive en el de rendimiento; el de datos la enlaza
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

**Corregida el 2026-08-22 (pendiente 19):** la fila 17 reprobaba porque el preámbulo de identidad comparte el número `00` con el núcleo; ahora la regla lo dice: es un anexo, no un capítulo ni un dueño distinto.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
