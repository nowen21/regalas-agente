# Fase «A-EP01-HU03-Descripción de lo realizado»   ·   `[CAPA 3]`

> Molde para **crear una fase** (unidad de ejecución). Las reglas de **relación y nomenclatura** que gobiernan esta plantilla están en `02·F12` (autoridad — aquí no se duplican). La carpeta de la fase se guarda en `documentacion/<modulo>/<identificador-de-fase>/`. Reemplaza los `«…»` y borra esta caja.

---

## 1. Identidad de la fase

| Campo | Valor |
|---|---|
| **Identificador** | `«A-EP01-HU03-Configuración de la estructura inicial»` |
| **Consecutivo** (orden dentro de la HU) | `«A»` (A, B, C, …, Z, AA, AB, …) |
| **Épica** | `EP«01»` |
| **HU** | `HU«03»` — **una sola** (`02·F12`) |
| **Descripción** | «qué se realiza en esta fase» |
| **Módulo** | «M» |

> **Nombre = `[Consecutivo]-[EP]-[HU]-[Descripción]`** (`02·F12`). Ej.: `A-EP01-HU03-Configuración de la estructura inicial`. El consecutivo alfabético **no se reinicia ni se repite** dentro de la HU y representa el **orden** de las fases.
>
> **Si la fase complementa a otra fase**, el nombre incluye el consecutivo de la fase complementada: **`[Consecutivo]-[Consecutivo-fase-complementa]-[EP]-[HU]-[Descripción]`**. Ej.: `D-B-EP01-HU03-Ajuste de la validación de permisos` (la fase `D` complementa a la `B`).

---

## 2. Origen  ·  `13·DOC12`

Una fase puede ser independiente o **complementar / ampliar / continuar** una fase anterior de la **misma HU** (`02·F12`). Declarar 1 de 3 (o híbrido):

- 📝 **Continúa / modifica fase(s) anterior(es):** «cuál(es) de esta HU y qué retoma, complementa o amplía». Si **complementa** una fase, el identificador usa el formato con la fase complementada (ver §1: `[Consecutivo]-[Consecutivo-fase-complementa]-[EP]-[HU]-…`).
- ✨ **Funcionalidad nueva:** «qué introduce que no cubrían las fases previas de la HU».
- 🔀 **Híbrido:** ambos.

---

## 3. Criterios de aceptación que cubre

Una fase puede corresponder a un **CA** cuando su implementación se pueda **delimitar y validar de forma independiente** (`02·F12`). No crear una fase solo por nomenclatura — cada fase es **trabajo real, verificable y trazable**.

| CA de la HU | ¿Se delimita/valida aparte en esta fase? |
|---|---|
| CA-01 | sí / no |
| CA-02 | sí / no |

---

## 4. Artefactos de la fase

La carpeta `documentacion/<modulo>/<identificador-de-fase>/` contiene:

```
<identificador-de-fase>/            # ej. A-EP01-HU03-configuracion-estructura-inicial
├── plan_trabajo.md                 # plantilla planes/trabajo.md (02·F4)
├── plan_pruebas.md                 # plantilla planes/pruebas.md (02·F4/F5)
├── funcionalidad_implementada.md   # plantilla funcionalidad-implementada.md (cierre · 13·DOC11)
└── estado-fase.md                  # plantilla estado-fase.md (checkpoint del orquestador)
```

---

## 5. Jerarquía  ·  `02·F0` / `F12`

`Épica → HU → Fases`. Una fase pertenece **exclusivamente a una HU**; ningún identificador de fase aparece bajo dos HU distintas. Una HU tiene **al menos una** fase y puede tener varias.
