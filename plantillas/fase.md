# Fase «A-EP01-HU03-Descripción de lo realizado»   ·   `[CAPA 3]`

> Molde para **crear una fase** (unidad de ejecución). Las reglas de **relación y nomenclatura** que gobiernan esta plantilla son la **fuente única** `02·F12` → `base/02-flujo-de-trabajo/F12/base.md` (aquí **no** se duplican). La carpeta de la fase se guarda en `documentacion/<modulo>/<identificador-de-fase>/`. Reemplaza los `«…»` y borra esta caja.

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

> **El formato del nombre y sus reglas** (consecutivo alfabético, orden, variante de complemento) son la fuente única `02·F12`. Ej.: `A-EP01-HU03-Configuración de la estructura inicial`.

---

## 2. Origen  ·  `13·DOC12`

Declarar 1 de 3 (o híbrido) — las reglas de origen y complemento son la fuente única `02·F12`:

- 📝 **Continúa / modifica fase(s) anterior(es):** «cuál(es) de esta HU y qué retoma, complementa o amplía». Si **complementa**, el identificador usa el formato con complemento (`02·F12`).
- ✨ **Funcionalidad nueva:** «qué introduce que no cubrían las fases previas de la HU».
- 🔀 **Híbrido:** ambos.

---

## 3. Criterios de aceptación que cubre

Reglas sobre qué CA cubre una fase (y el principio "no crear una fase solo por nomenclatura"): fuente única `02·F12`.

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

## 5. Jerarquía y relación con la HU

`Épica → HU → Fases`. Las reglas (una fase = una sola HU, ningún identificador bajo dos HU, etc.) son la fuente única `02·F12` → `base/02-flujo-de-trabajo/F12/base.md`.
