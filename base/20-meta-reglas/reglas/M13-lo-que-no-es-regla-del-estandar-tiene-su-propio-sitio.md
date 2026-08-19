> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M13 · Lo que no es regla del estándar tiene su propio sitio

Antes de escribir en `base/`, verificar que ahí es donde va: solo la regla que aplica a **cualquier** proyecto. Dónde va todo lo demás: [`base.md`](../base.md).

```
INCORRECTO: la convención de un equipo entra en base/ como si aplicara a cualquier proyecto
CORRECTO:   entra en el catálogo de ese proyecto; base/ solo lleva lo universal
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v2.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
