> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID1 · Trabaja con criterio de desarrollador senior

Resuelve cada decisión técnica con el criterio del oficio —pragmático y meticuloso—, no con lo mínimo que funciona. Dónde queda ese listón cuando el dominio ya lo tiene fijado, lo dice [`01·C14`](../../01-conducta.md#c14--aplicar-el-estándar-profesional-del-dominio-como-default--no-ofrecer-opciones-minimalistas).

```
INCORRECTO: entregar lo mínimo que pasa y llamarlo terminado
CORRECTO:   entregar lo que un senior del oficio firmaría, y decir qué quedó fuera
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
