> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F7 · No cierres una fase con trazabilidad incompleta

Antes de cerrar, revisa ítem por ítem que cada afirmación técnica de la spec esté en el código, el esquema, las pruebas y los docs, y no cierres con faltantes sin justificar (depende de [`13·DOC3`](../../13-documentacion.md#doc3--verifica-la-trazabilidad-spec--implementación-antes-de-cerrar), que fija el formato de la tabla de cierre).

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + trazabilidad sin faltantes → cierro"
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ❌ ✅ ❌ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 2 ❌ · 1 N/A.** N/A — **16**: no tiene excepción.

**❌** — **2** y **4**: [`13·DOC3`](../../13-documentacion.md#doc3--verifica-la-trazabilidad-spec--implementación-antes-de-cerrar) exige exactamente lo mismo —el ejemplo era idéntico palabra por palabra hasta esta versión— y el dueño del tema es el capítulo [`13`](../../13-documentacion.md) ([`M2`](../../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`M12`](../../20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)). Derogarla a favor de [`13·DOC3`](../../13-documentacion.md#doc3--verifica-la-trazabilidad-spec--implementación-antes-de-cerrar) lo decide el usuario ([`M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

> **Regla vigente y reprobada.** Sigue rigiendo hasta que el usuario decida la vía.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
