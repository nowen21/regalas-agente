> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M8 · La excepción se escribe dentro de la regla que la admite

Una excepción no vive en otro documento ni en el chat: es **parte del texto de la regla**, y declara tres cosas — **condición** (cuándo aplica), **límite** (hasta dónde) y **quién la autoriza**. Qué no es excepción y qué hacer ante una no escrita: [`base.md`](../base.md).

```
INCORRECTO: "el test tarda mucho, esta vez lo salto y sigo"
CORRECTO:   reporto el costo, propongo el arreglo y espero; si se acepta un
            criterio nuevo, entra escrito en la regla
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

**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 17 reprobaba porque [`00·N1`](../../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada), blindada, traía una excepción escrita. Desde el 2026-08-18 [`N1`](../../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada) no tiene excepción (lo que parecía una era el alcance de la aprobación). Ninguna blindada contradice ya a `M8`.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
