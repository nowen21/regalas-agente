> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M3 · La base es agnóstica: sin stack y sin dominio

Una regla de capa 1 o 2 sirve a **cualquier** proyecto: no nombra lenguaje, framework, motor de base de datos, nube, sector ni cliente. Lo concreto se declara en capa 3 y la regla lo referencia como concepto.

Si una regla no se puede escribir sin nombrar una tecnología, **no es regla de la base**: es capa 3.

```
INCORRECTO: "usar pytest con cobertura mínima de 80%"
CORRECTO:   "toda unidad entregada lleva pruebas automáticas; el marco y el
             umbral los declara el proyecto (.agente/stack.md)"
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
