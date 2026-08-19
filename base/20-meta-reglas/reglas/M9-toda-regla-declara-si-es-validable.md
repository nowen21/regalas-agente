> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M9 · Toda regla declara si es validable

Al escribir la regla, responder **¿puede un script decir sí/no sin opinar?** y registrar la respuesta en `validadores/reglas-validables.md`. Qué se sigue de cada respuesta: [`base.md`](../base.md).

```
INCORRECTO: la regla se escribe y nadie decide si un script puede comprobarla
CORRECTO:   se responde al escribirla y queda registrada en validadores/reglas-validables.md
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
