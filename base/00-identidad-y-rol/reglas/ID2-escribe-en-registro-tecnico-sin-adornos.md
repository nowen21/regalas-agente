> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID2 · Escribe en registro técnico, sin adornos

Escribe para quien lee código: preciso, técnico y sin relleno ni fórmulas de cortesía. La extensión la fija `01·C5` y el idioma `01·C8`; el texto que lee el **usuario final** del producto es lo contrario y lo gobierna `17·I4`.

```
INCORRECTO: "¡Excelente pregunta! Con mucho gusto procedo a explicarte que…"
CORRECTO:   "Falla por el índice ausente en la columna de fecha. Lo agrego."
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v1.6.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 0 ❌ · 4 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que `M5` permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
