# Fase «A-EP01-HU03-Descripción de lo realizado»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Molde para crear una fase (unidad de ejecución). Las reglas de relación y nomenclatura que gobiernan esta plantilla tienen una fuente única, [`02·F12`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), y aquí **no** se duplican. La ruta de la carpeta de la fase es `02·F12.13`. Reemplaza los `«…»` y borra esta caja.

## 1. Identidad de la fase

> Identifica la fase dentro de su HU y su épica. El nombre sigue la nomenclatura `02·F12.6`, el orden o consecutivo `02·F12.7` y la variante de complemento `02·F12.12`.

| Campo | Valor |
|---|---|
| **Identificador** | `«A-EP01-HU03-Configuración de la estructura inicial»` |
| **Consecutivo** (orden dentro de la HU) | `«A»` (A, B, C, ..., Z, AA, AB, ...) |
| **Épica** | `EP«01»` |
| **HU** | `HU«03»` — **una sola** (`02·F12.1`) |
| **Descripción** | «qué se realiza en esta fase» |
| **Módulo** | «M» |

## 2. Origen  ·  [`13·DOC12`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

> Dice de dónde sale la fase. Se declara una de las tres opciones, con la regla de origen de `02·F12.8` (complementar, ampliar o continuar).

- Continúa / modifica fase(s) anterior(es): «cuál(es) de esta HU y qué retoma, complementa o amplía». Si **complementa**, el identificador usa el formato con complemento (`02·F12.12`).
- Funcionalidad nueva: «qué introduce que no cubrían las fases previas de la HU».
- Híbrido: las dos cosas.

## 3. Criterios de aceptación que cubre

> Son los CA de la HU que toca esta fase, y si cada uno se delimita o valida aparte en ella. Qué CA cubre una fase lo dice `02·F12.9`, y el principio de no crear una fase solo por nomenclatura, `02·F12.10`.

| CA de la HU | ¿Se delimita/valida aparte en esta fase? |
|---|---|
| CA-01 | sí / no |
| CA-02 | sí / no |

## 4. Artefactos de la fase

> Son los documentos que acompañan a la fase, cada uno con su plantilla.

La carpeta `documentacion/<modulo>/<identificador-de-fase>/` contiene:

```
<identificador-de-fase>/            # ej. A-EP01-HU03-configuracion-estructura-inicial
├── plan_trabajo.md                 # plantilla planes/trabajo.md (02·F4)
├── plan_pruebas.md                 # plantilla planes/pruebas.md (02·F4/F5)
├── funcionalidad_implementada.md   # plantilla funcionalidad-implementada.md (cierre · 13·DOC11)
└── estado-fase.md                  # plantilla estado-fase.md (checkpoint del orquestador)
```

## 5. Jerarquía y relación con la HU

> Ubica la fase en la cadena de la épica a sus fases, con las reglas que la atan a una sola HU.

`Épica → HU → Fases` (`02·F12.11`). Reglas relacionadas: una fase = una sola HU (`F12.1`), ningún identificador bajo dos HU (`F12.4`). Fuente única: `base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md`.
