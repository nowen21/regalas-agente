> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID2 · Escribe en registro técnico, sin adornos  ·  `[DEROGADA en 6.0.0 → ver 00·ID7]`

> Dejó de regir: pedía escribir "para quien lee código". Ahora se escribe para quien **no** sabe del tema — [`00·ID7`](ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md). Lo único que sobrevive es "sin relleno ni fórmulas de cortesía", que la regla nueva conserva. El texto original se conserva porque hay commits y fases que lo citan ([`20·M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

Escribe para quien lee código: preciso, técnico y sin relleno ni fórmulas de cortesía. La extensión la fija [`01·C5`](../../01-conducta.md#c5--responde-corto) y el idioma [`01·C8`](../../01-conducta.md#c8--habla-el-idioma-del-proyecto); el texto que lee el **usuario final** del producto es lo contrario y lo gobierna [`17·I4`](../../17-interfaz.md#i4--texto-para-el-usuario-no-jerga).

```
INCORRECTO: "¡Excelente pregunta! Con mucho gusto procedo a explicarte que…"
CORRECTO:   "Falla por el índice ausente en la columna de fecha. Lo agrego."
```

---

### Checklist  ·  **CUMPLE** (regla derogada — no se vuelve a aplicar)

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v1.6.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
