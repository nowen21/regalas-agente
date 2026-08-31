> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F12 · Nombra y ubica cada fase según la nomenclatura del anexo

Una fase pertenece a una sola historia, lleva consecutivo alfabético dentro de ella, se nombra `[Consecutivo]-EP-NNN-HU-NNN-[descripción]` y vive donde dice el anexo [base/02-flujo-de-trabajo/nomenclatura-de-fases.md](../nomenclatura-de-fases.md), fuente única de `F12.1` a `F12.13`; no se crea una fase solo por la nomenclatura (depende de [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).

```
INCORRECTO: la fase se llama «ajustes varios» y cuelga de dos historias a la vez
CORRECTO:   B-EP-001-HU-003-Implementación de la lógica de negocio, dentro de su HU,
            con sus cinco documentos en la ruta del anexo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ N/A ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 0 ❌ · 4 N/A.** N/A — **12**: la regla no se puede malinterpretar, y `F12.6` ya trae tres ejemplos de nombre · **14**, **15** y **16**: no declara dependencia ni excepción.

**Corregida el 2026-08-22 (pendiente 19), con la vía decidida por el usuario:** el texto literal que él escribió el 2026-08-03 se conserva entero, sin tocar, como [anexo del capítulo](../nomenclatura-de-fases.md), y la regla queda con una sola exigencia que cabe en el molde y un título que enuncia la norma. Los `F12.N` siguen siendo las anclas de referencia, ahora del anexo. Filas 8, 9 y 10 resueltas sin reescribir una palabra del usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
