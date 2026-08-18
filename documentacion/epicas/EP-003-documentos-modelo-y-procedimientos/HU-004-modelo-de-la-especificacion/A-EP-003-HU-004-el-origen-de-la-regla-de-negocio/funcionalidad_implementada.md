# Funcionalidad implementada — Fase «A-EP-003-HU-004-el-origen-de-la-regla-de-negocio»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-003-HU-004-el-origen-de-la-regla-de-negocio` |
| **Épica / HU** | [EP-003](../../epica.md) · [HU-004](../HU-004-modelo-de-la-especificacion.md) |
| **Versión del estándar** | 21.3.1 → **22.0.0** (MAYOR) |
| **Fecha de cierre** | 2026-08-16 |

---

## 1. Qué quedó funcionando

**El §4 del modelo de especificación pide dos datos por regla, no uno.** Antes pedía `«Regla — por qué existe.»`: el porqué, nunca el de dónde. Ahora pide `«Regla — de dónde baja (el identificador del requisito, la historia o la decisión) — por qué existe.»`, y la nota de la sección dice qué hacer con la que no tenga procedencia: **no se escribe ahí**, se sube a la historia que corresponda y baja desde allá.

**Se pide un identificador, no una frase.** «Lo pidió el cliente» no se puede seguir hasta ninguna parte, y el programa que lo comprobará necesita algo que exista de verdad para poder buscarlo.

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`plantillas/plantilla-especificacion-modulo.md`](../../../../../plantillas/plantilla-especificacion-modulo.md) | El §4: el molde de la regla y la nota de la regla sin procedencia |
| [`HU-004-modelo-de-la-especificacion.md`](../HU-004-modelo-de-la-especificacion.md) | El `CA-04`, la fase en §8 y la bitácora |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · `VERSION` | 22.0.0 |

---

## 3. Cómo se comprueba

Se llenó el §4 con las dos reglas del caso real de `shopnest-mesa`: la que baja de `RF-13` y la que no baja de nada. La primera cabe; la segunda deja el hueco a la vista en medio de la frase, donde no se puede disimular. Está en el [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase.

---

## 4. Qué quedó fuera

- **El programa que lo comprueba.** Es la exigencia 2 del pendiente 43 y vive en otro módulo: va en su propia fase bajo EP-004.
- **Revisar los §4 ya escritos** en las especificaciones vivas. En `shopnest-mesa` fue una de seis en el primer módulo que se miró; acá no se contó ninguna.
- **La columna `Origen` de la tabla de campos** del §5.1, que el proyecto inventó por su cuenta. Es la misma idea en otra sección y merece su propia decisión.

---

## 5. Por qué es MAYOR

Un proyecto al día **tiene que hacer algo nuevo**: escribir la procedencia en cada regla de negocio que agregue. Eso es lo que [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) llama obligar, aunque el cambio sea de una plantilla y de una sola línea.

Lo que **no** obliga es a reescribir hacia atrás: las especificaciones ya escritas quedan selladas con la versión bajo la que se escribieron. Les falta un dato; no quedan inválidas.
