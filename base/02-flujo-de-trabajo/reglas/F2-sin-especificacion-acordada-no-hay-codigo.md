> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F2 · Sin especificación acordada no hay código

Ningún desarrollo, refactor o migración sin **especificación acordada**: alcance, reglas, datos, pruebas y permisos. Si falta, el agente no toca código: ofrece el borrador y lo hace aprobar.
**Si el entregable no es código**, la especificación es la **historia con sus criterios de aceptación**.

**Excepción** — no requieren especificación la corrección trivial, el bugfix que solo realinea el código a la especificación vigente, la configuración local, el comando que el usuario pide y la lectura o investigación (condición). Cubren ese trabajo puntual; no habilitan funcionalidad nueva ni cambio de comportamiento (límite). Ante la duda de si el caso entra, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza).

```
INCORRECTO: "hacé que el módulo permita X" → escribo código directo
CORRECTO:   busco X en la especificación → si no está: "no está en la especificación; ¿lo agrego a la fase Y
            o es dominio nuevo?" → aprueban → actualizo especificación → implemento + pruebas
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v23.9.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A — **14** y **15**: no declara dependencia; sus citas son referencia. La excepción, que antes decía solo cuándo no aplica, ahora trae sus tres partes; el procedimiento de dos pasos está en [`base.md`](../base.md).

**Reaplicado al resolver el [pendiente 20](../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md).** La regla estaba escrita dando por hecho que lo que se construye es código, y dos fases de este repositorio se abrieron declarando que no tienen especificación aparte porque su entregable es texto normativo.

**Se eligió decir de qué está hecha la especificación, y no abrirle otra excepción.** Una excepción dice **cuándo no rige**; esto dice **dónde vive** lo que la regla exige — y así `F2` sigue exigiendo lo mismo en todos los casos. Abrirle una segunda excepción a una regla que ya tiene una es la puerta que después nadie cierra.

**Mide 294 caracteres**: entra en el molde después del cambio, y se acortó la primera frase para que quepa.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
