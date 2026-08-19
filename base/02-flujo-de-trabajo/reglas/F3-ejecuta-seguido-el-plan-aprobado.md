> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F3 · Ejecuta seguido el plan aprobado

Aprobado el plan, ejecuta **todos** sus cambios seguidos, sin pedir permiso por cada archivo. Solo pausa si surge algo **no cubierto** por el plan.

```
INCORRECTO: "hago el cambio 1, ¿procedo?" → "el 2, ¿procedo?" → ...
CORRECTO:   ejecuto todo el plan → reporto el resultado
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Es el dueño del criterio: [`F9`](F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md) lo extiende en vez de repetirlo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
