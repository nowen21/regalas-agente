> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M4 · Cada regla tiene un identificador único, estable y prefijado

Formato `<PREFIJO><n>`: prefijo de letras del capítulo más consecutivo. El prefijo es **exclusivo** de un capítulo. **El ID no cambia nunca** — ni al reescribir la regla, ni al moverla, ni al cambiarle el título. Cómo se cita y por qué no cambia: [`base.md`](../base.md).

```
INCORRECTO: se borra la R3 y se corre la R4 a R3 "para dejarlo ordenado"
CORRECTO:   el hueco se queda; la regla nueva toma el siguiente consecutivo libre
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

**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 17 reprobaba por los sub-identificadores decimales `F12.1` a `F12.13`. Desde hoy esos son anclas del [anexo de nomenclatura de fases](../../02-flujo-de-trabajo/nomenclatura-de-fases.md), no identificadores de regla; [`F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) es una sola regla con un solo ID. Nada del catálogo contradice ya a `M4`.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
