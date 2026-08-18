> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F2 · Sin especificación acordada no hay código

Ningún desarrollo, refactor o migración sin una **especificación acordada** que lo respalde —alcance, reglas de negocio, datos, pruebas, permisos—. Si no existe, el agente **no toca código**: ofrece redactar el borrador y lo hace aprobar primero. Sin especificación, el código es opinión del agente.

**Excepción** — no requieren especificación la corrección trivial, el bugfix que solo realinea el código a la especificación vigente, la configuración local, el comando que el usuario pide y la lectura o investigación (condición). Cubren ese trabajo puntual; no habilitan funcionalidad nueva ni cambio de comportamiento (límite). Ante la duda de si el caso entra, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza).

```
INCORRECTO: "hacé que el módulo permita X" → escribo código directo
CORRECTO:   busco X en la especificación → si no está: "no está en la especificación; ¿lo agrego a la fase Y
            o es dominio nuevo?" → aprueban → actualizo especificación → implemento + pruebas
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A — **14** y **15**: no declara dependencia; sus citas son referencia. La excepción, que antes decía solo cuándo no aplica, ahora trae sus tres partes; el procedimiento de dos pasos está en [`base.md`](../base.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
