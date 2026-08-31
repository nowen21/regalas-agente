# Nomenclatura y relación de las fases  ·  anexo de `02·F12`

> **Texto literal del usuario, 2026-08-03.** No se reescribe, no se resume y no se interpreta; cualquier ajuste lo hace el usuario (el 2026-08-22 autorizó cambiar las rayas de puntuación por dos puntos, y nada más). Es el anexo de [`02·F12`](reglas/F12-relacion-y-nomenclatura-de-fases.md): la regla queda con la exigencia y este anexo con el detalle, como el capítulo `00` hace con [base/00-identidad-y-rol/acciones-y-riesgo.md](../00-identidad-y-rol/acciones-y-riesgo.md). Los `F12.N` son **anclas de referencia** a las partes de este anexo, no identificadores de regla ([`20·M4`](../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)); al citar se referencia la parte.

* **F12.1**: **Una fase pertenece exclusivamente a una sola HU.**

* **F12.2**: **Una HU debe tener al menos una fase y puede tener múltiples fases.**

* **F12.3**: **Una misma fase no puede estar asociada a dos o más HU.**

* **F12.4**: **Ningún identificador de fase puede aparecer bajo dos HU diferentes.**

* **F12.5**: Las fases deben identificarse mediante un **consecutivo alfabético** dentro de cada HU:
  **A, B, C, ..., Z, AA, AB, AC, ..., AZ, BA, BB, ...**

* **F12.6**: El nombre de cada fase debe seguir la estructura:

  **`[Consecutivo alfabético] + [Número de Épica] + [Número de HU] + [Descripción de lo realizado en la fase]`**

  Por ejemplo:

  - **`A-EP-001-HU-003-Configuración de la estructura inicial`**
  - **`B-EP-001-HU-003-Implementación de la lógica de negocio`**
  - **`C-EP-001-HU-003-Validación de permisos`**

* **F12.7**: El consecutivo alfabético representa el **orden de las fases dentro de la HU**, por lo que no debe reiniciarse arbitrariamente ni repetirse dentro de la misma HU.

* **F12.8**: Una fase puede **complementar, ampliar o continuar el trabajo realizado en una fase anterior**. Por tanto, las fases no necesariamente representan actividades completamente independientes.

* **F12.9**: Una fase también puede corresponder directamente a un **criterio de aceptación (CA)** cuando su implementación pueda ser delimitada y validada de manera independiente.

* **F12.10**: Si una HU requiere varios criterios de aceptación, estos pueden materializarse en diferentes fases cuando corresponda. Sin embargo, **no se debe crear una fase únicamente por cumplir una estructura de nomenclatura**; cada fase debe representar un trabajo real, verificable y trazable.

* **F12.11**: La relación debe mantener siempre la jerarquía:

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
                ├── resultado_pruebas.md
                ├── funcionalidad_implementada.md
                └── estado-fase.md
```

> **`resultado_pruebas.md` lo agregó el usuario el 2026-08-13.** El plan de pruebas se aprueba **antes** de ejecutar; si los resultados se escriben encima, se pierde la línea base aprobada y no queda de dónde sacar el veredicto de la fase. Plantilla: [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md).

[`estructura-base.md`](estructura-base.md), [`13·DOC15`](../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) y las plantillas **referencian** esta ruta, no la duplican.
