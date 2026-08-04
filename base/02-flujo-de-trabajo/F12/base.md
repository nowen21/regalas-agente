# F12 · Regla de relación y nomenclatura de fases

> **Fuente única de la regla F12.** El índice `02-flujo-de-trabajo.md` solo la referencia; el detalle vive aquí. El molde para crear una fase es `plantillas/fase.md`, que apunta a este archivo.

> **Texto literal del usuario, 2026-08-03.** No se reescribe, no se resume y no se
> interpreta. Cualquier ajuste lo hace el usuario.

* **Una fase pertenece exclusivamente a una sola HU.**

* **Una HU debe tener al menos una fase y puede tener múltiples fases.**

* **Una misma fase no puede estar asociada a dos o más HU.**

* **Ningún identificador de fase puede aparecer bajo dos HU diferentes.**

* Las fases deben identificarse mediante un **consecutivo alfabético** dentro de cada HU:
  **A, B, C, ..., Z, AA, AB, AC, ..., AZ, BA, BB, ...**

* El nombre de cada fase debe seguir la estructura:

  **`[Consecutivo alfabético] + [Número de Épica] + [Número de HU] + [Descripción de lo realizado en la fase]`**

  Por ejemplo:

  **`A-EP01-HU03-Configuración de la estructura inicial`**
  **`B-EP01-HU03-Implementación de la lógica de negocio`**
  **`C-EP01-HU03-Validación de permisos`**

* El consecutivo alfabético representa el **orden de las fases dentro de la HU**, por lo que no debe reiniciarse arbitrariamente ni repetirse dentro de la misma HU.

* Una fase puede **complementar, ampliar o continuar el trabajo realizado en una fase anterior**. Por tanto, las fases no necesariamente representan actividades completamente independientes.

* Una fase también puede corresponder directamente a un **criterio de aceptación (CA)** cuando su implementación pueda ser delimitada y validada de manera independiente.

* Si una HU requiere varios criterios de aceptación, estos pueden materializarse en diferentes fases cuando corresponda. Sin embargo, **no se debe crear una fase únicamente por cumplir una estructura de nomenclatura**; cada fase debe representar un trabajo real, verificable y trazable.

* La relación debe mantener siempre la jerarquía:

  **Épica → HU → Fases**

  Una Épica puede contener múltiples HU, una HU puede contener múltiples fases, pero **una fase no puede ser compartida entre diferentes HU**.

---

**Complemento entre fases** (agregado por el usuario, 2026-08-03): cuando una fase **complementa** a otra, el nombre incluye el consecutivo de la fase complementada:

**`[Consecutivo] + [Consecutivo-fase-complementa] + [Número de Épica] + [Número de HU] + [Descripción]`**

Ej.: `D-B-EP01-HU03-Ajuste de la validación de permisos` (la fase `D` complementa a la `B`).
