> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M8 · La excepción se escribe dentro de la regla que la admite

Una excepción no vive en otro documento ni en el chat: es **parte del texto de la regla**, y declara tres cosas — **condición** (cuándo aplica), **límite** (hasta dónde) y **quién la autoriza**. Qué no es excepción y qué hacer ante una no escrita: [`base.md`](../base.md).

```
INCORRECTO: "el test tarda mucho, esta vez lo salto y sigo"
CORRECTO:   reporto el costo, propongo el arreglo y espero; si se acepta un
            criterio nuevo, entra escrito en la regla
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

**❌** — **17**: dice que las `[BLINDADA]` no admiten excepción, y [`00·N1`](../../00-nucleo-blindado.md#n1--no-ejecutar-sin-validación-blindada) es blindada y tiene una escrita.

> **Regla vigente y reprobada.** Sigue rigiendo —[`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado— pero no es conforme hasta resolver el choque, y eso es decisión del usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
