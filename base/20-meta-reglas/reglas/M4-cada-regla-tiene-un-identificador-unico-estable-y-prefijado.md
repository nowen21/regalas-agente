> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M4 · Cada regla tiene un identificador único, estable y prefijado

Formato `<PREFIJO><n>`: prefijo de letras del capítulo más consecutivo. El prefijo es **exclusivo** de un capítulo. **El ID no cambia nunca** — ni al reescribir la regla, ni al moverla, ni al cambiarle el título. Cómo se cita y por qué no cambia: [`base.md`](../base.md).

```
INCORRECTO: se borra la R3 y se corre la R4 a R3 "para dejarlo ordenado"
CORRECTO:   el hueco se queda; la regla nueva toma el siguiente consecutivo libre
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v2.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ❌ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

**❌** — **17**: no contempla los sub-ID decimales que el catálogo todavía usa en [`F12.1`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)-[`F12.13`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md). Los de [`F4.1`](../../02-flujo-de-trabajo/reglas/F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)-[`F4.5`](../../02-flujo-de-trabajo/reglas/F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md) dejaron de chocar en la 3.1.0, promovidos a [`F14`](../../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)-[`F20`](../../02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md); los de [`F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) no, porque su texto está congelado por decisión del usuario.

> **Regla vigente y reprobada.** Sigue rigiendo —[`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado— pero no es conforme hasta resolver el choque, y eso es decisión del usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
