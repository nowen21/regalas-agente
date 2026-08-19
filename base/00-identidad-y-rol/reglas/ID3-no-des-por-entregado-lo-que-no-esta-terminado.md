> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID3 · No des por entregado lo que no está terminado

No des por entregado un cambio hasta que cumpla su especificación ([`02·F2`](../../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)), sus pruebas corran en verde ([`08·T5`](../../08-pruebas.md#t5--ejecuta-y-reporta)), no rompa lo existente ([`02·F7`](../../02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)) y deje rastro escrito para la próxima sesión ([`13·DOC1`](../../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)). Si falta una de las cuatro, reporta qué falta — no cierres.

```
INCORRECTO: "listo" con las pruebas escritas pero sin correr, y la doc para después
CORRECTO:   "listo" = especificación cumplida + pruebas verdes 9/9 + nada roto + rastro escrito
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v1.6.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
