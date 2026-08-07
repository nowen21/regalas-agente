> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M7 · Las dependencias entre reglas se declaran, y solo hay tres

Una regla que se apoya en otra lo declara **en su cuerpo, entre paréntesis**, con una de tres formas: `extiende ID` · `depende de ID` · `deroga ID`. No hay una cuarta. Qué significa cada una y sus dos prohibiciones: [`base.md`](../base.md).

```
INCORRECTO: la regla cierra con un párrafo en prosa que "se relaciona con" media docena de reglas
CORRECTO:   (extiende 09·G6), en el cuerpo y entre paréntesis
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v2.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ❌ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

**❌** — **17**: el catálogo usa una cuarta forma —el bloque `Encadenamiento`— 22 veces, y `M7` solo admite tres.

> **Regla vigente y reprobada.** Sigue rigiendo —[`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado— pero no es conforme hasta resolver el choque, y eso es decisión del usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
