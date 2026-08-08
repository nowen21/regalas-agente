> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F12 · Relación y nomenclatura de fases

> **Texto literal del usuario, 2026-08-03.** No se reescribe, no se resume y no se
> interpreta. Cualquier ajuste lo hace el usuario. Por eso esta regla conserva la forma que él le dio y no el molde de [`20·M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md). Los `F12.N` son solo **anclas de referencia**; no cambian el texto. Al citar se referencia **la parte** (ej. `F12.9`), no toda la regla.

* **F12.1** — **Una fase pertenece exclusivamente a una sola HU.**

* **F12.2** — **Una HU debe tener al menos una fase y puede tener múltiples fases.**

* **F12.3** — **Una misma fase no puede estar asociada a dos o más HU.**

* **F12.4** — **Ningún identificador de fase puede aparecer bajo dos HU diferentes.**

* **F12.5** — Las fases deben identificarse mediante un **consecutivo alfabético** dentro de cada HU:
  **A, B, C, ..., Z, AA, AB, AC, ..., AZ, BA, BB, ...**

* **F12.6** — El nombre de cada fase debe seguir la estructura:

  **`[Consecutivo alfabético] + [Número de Épica] + [Número de HU] + [Descripción de lo realizado en la fase]`**

  Por ejemplo:

  - **`A-EP-001-HU-003-Configuración de la estructura inicial`**
  - **`B-EP-001-HU-003-Implementación de la lógica de negocio`**
  - **`C-EP-001-HU-003-Validación de permisos`**

* **F12.7** — El consecutivo alfabético representa el **orden de las fases dentro de la HU**, por lo que no debe reiniciarse arbitrariamente ni repetirse dentro de la misma HU.

* **F12.8** — Una fase puede **complementar, ampliar o continuar el trabajo realizado en una fase anterior**. Por tanto, las fases no necesariamente representan actividades completamente independientes.

* **F12.9** — Una fase también puede corresponder directamente a un **criterio de aceptación (CA)** cuando su implementación pueda ser delimitada y validada de manera independiente.

* **F12.10** — Si una HU requiere varios criterios de aceptación, estos pueden materializarse en diferentes fases cuando corresponda. Sin embargo, **no se debe crear una fase únicamente por cumplir una estructura de nomenclatura**; cada fase debe representar un trabajo real, verificable y trazable.

* **F12.11** — La relación debe mantener siempre la jerarquía:

  **Épica → HU → Fases**

  Una Épica puede contener múltiples HU, una HU puede contener múltiples fases, pero **una fase no puede ser compartida entre diferentes HU**.

---

**F12.12 · Complemento entre fases** (agregado por el usuario, 2026-08-03): cuando una fase **complementa** a otra, el nombre incluye el consecutivo de la fase complementada:

**`[Consecutivo] + [Consecutivo-fase-complementa] + [Número de Épica] + [Número de HU] + [Descripción]`**

Ej.: `D-B-EP-001-HU-003-Ajuste de la validación de permisos` (la fase `D` complementa a la `B`).

---

**F12.13 · Materialización física** (fuente única de la ruta):

```
documentacion/
└── epicas/
    └── EP-001-«slug»/                          # Épica
        ├── epica.md
        └── HU-003-«slug»/                      # HU (dentro de su épica)
            ├── HU-003-«slug».md
            └── A-EP-001-HU-003-«slug»/           # Fase (dentro de su HU · identificador F12)
                ├── plan_trabajo.md
                ├── plan_pruebas.md
                ├── funcionalidad_implementada.md
                └── estado-fase.md
```

[`estructura-base.md`](../estructura-base.md), [`13·DOC15`](../../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) y las plantillas **referencian** esta ruta — no la duplican.

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ❌ ✅ N/A ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 13 ✅ · 3 ❌ · 4 N/A.** N/A — **12**: la regla no se puede malinterpretar, y `F12.6` ya trae tres ejemplos de nombre · **14**, **15** y **16**: no declara dependencia ni excepción.

**❌** — **8**: el título es nominal, no imperativo · **9**: trece exigencias bajo un ID, y `F12.13` (la ruta física) es además un tema distinto del resto · **10**: no cabe en cuatro líneas.

> **Regla vigente y reprobada, y así se queda.** El texto está **congelado por decisión del usuario**: es suyo, literal, y el agente no lo reescribe. Las tres ❌ son consecuencia de esa congelación, no un defecto por corregir por cuenta propia — se resuelven el día que el usuario decida la vía (envolverlo en el molde, o legalizar la congelación en [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
