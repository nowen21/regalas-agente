> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M12 · Antes de crear una regla, buscar — la duplicación es el defecto más caro

Antes de escribir una regla nueva, **buscar por concepto** en `base/` y leer entero el capítulo dueño. Si ya existe se afina; si casi existe se extiende; crear es lo último. El orden completo de búsqueda y de decisión: [`base.md`](../base.md).

```
INCORRECTO: se escribe una regla nueva sin abrir el capítulo dueño, y termina diciendo lo que ya decía otra
CORRECTO:   se busca por concepto → ya existe → se afina la que está
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v2.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
