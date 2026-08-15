> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F21 · Un incumplimiento ya identificado no se repite en lo nuevo

Desde que un incumplimiento queda registrado en un pendiente, un hallazgo o una señal, todo lo que se escriba de ahí en adelante nace cumpliendo. El pendiente guarda lo que ya estaba mal y se limpia aparte; no autoriza a producir más de lo mismo.

```
INCORRECTO: el pendiente dice que 354 enlaces no cumplen DOC14,
            y los documentos de hoy suman 122 más
CORRECTO:   los 354 siguen en su pendiente y los de hoy nacen bien
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v15.0.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia; nombra el pendiente y la señal, que son sitios, no reglas · **16**: no tiene excepción. Fila 6: `F21` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, que lo nuevo nazca cumpliendo lo que ya se sabe. Fila 17: se releyó el capítulo entero. [`F20`](F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) manda parar y proponer lo que aparece fuera del criterio de aceptación, y esta manda no producirlo: no chocan, porque una habla de lo que se encuentra y la otra de lo que se escribe.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
