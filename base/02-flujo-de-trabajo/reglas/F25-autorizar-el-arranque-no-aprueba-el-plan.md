> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F25 · Autorizar el arranque no aprueba el plan

Decir «arranque con X» autoriza **abrir la fase**, no ejecutar su plan detallado: son dos permisos distintos y el segundo se pide aparte, con el plan a la vista (extiende [`02·F4`](F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

```
INCORRECTO: «dale, arrancá con la fase B» → se escribe el plan y se ejecuta seguido
CORRECTO:   se abre la fase, se escribe el plan, se presenta, y se espera el segundo sí
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v23.23.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`F4`](F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md).** Del [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `F4` dice **que hace falta un OK**; esta dice **cuál OK no cuenta**. Nadie se salta la aprobación a propósito: lo que pasa es que se toma el permiso de arrancar por el permiso de ejecutar, y el trabajo avanza con la conciencia tranquila.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
