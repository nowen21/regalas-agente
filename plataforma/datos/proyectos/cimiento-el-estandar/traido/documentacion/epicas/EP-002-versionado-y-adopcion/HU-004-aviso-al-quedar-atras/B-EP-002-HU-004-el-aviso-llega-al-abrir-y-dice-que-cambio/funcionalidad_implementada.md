# Funcionalidad implementada — Fase `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | La propia [HU-004](../HU-004-aviso-al-quedar-atras.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), abierto el 2026-08-22 |
| **HU / CA cubiertas** | [HU-004](../HU-004-aviso-al-quedar-atras.md): el `CA-01`, que la fase `A` dejó en rojo |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `a2d839d` |

> **Se ejecutó el 2026-08-22 y este documento se escribió el 2026-08-26.** Hasta entonces **era el molde sin llenar**. El trabajo estaba hecho y probado; lo que faltaba era decir qué quedó.

---

## 1. Qué se implementó — resumen

**El aviso de desfase llega al abrir la sesión, y antes no llegaba.** La fase `A` lo había dejado en rojo: la comprobación existía, pero **el arranque no preguntaba por ella**, así que un proyecto atrasado podía trabajar toda la sesión sin enterarse.

**Y el aviso dice qué cambió**, no solo que hay algo nuevo: resume el tramo entre la versión adoptada y la vigente, poniendo primero lo que obliga a migrar.

**Medido sobre un proyecto real:** el arranque de shopnest-mesa pasó de **un** hallazgo a **tres**.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` el aviso llega al abrir sesión | automatismo | El arranque, que ahora pregunta por la versión | ✅ | Sobre shopnest-mesa: de 1 hallazgo a 3 |
| Y dice **qué cambió** | servicio | El resumen del tramo | ✅ | De `2.0.0` a `3.0.0` da `2.1.0` y `3.0.0` |
| Lo que obliga a migrar va primero | servicio | El orden del resumen | ✅ | Un tramo con una MAYOR: antes que los títulos |

**La evidencia no es un caso fabricado:** es un proyecto de verdad cuyo arranque cambió de comportamiento.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho, comprobado sobre un proyecto real |
| Defectos propios | **Ninguno** |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cuatro días con su cierre en blanco.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |
| **Suite** | `test_el_aviso_de_desfase_llega_y_dice_que_cambio`: **9 pruebas, todas en verde** |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Siete casos, y varios son de lo que NO debe hacer:**

| Caso | Qué sale |
|---|---|
| El arranque pregunta por la versión | Lo hace, **y antes no** |
| Lo que devuelve llega sin perderse | Aparece en la salida del arranque |
| El tramo son las de en medio y la de llegada | De `2.0.0` a `3.0.0`: `2.1.0` y `3.0.0` |
| La adoptada **no** entra en su propio tramo | No se cuenta |
| Un proyecto al día tiene tramo vacío | Nada que resumir |
| Lo que obliga a migrar va primero | Antes que los títulos |
| Sin registro **no se inventa** un tramo | Vacío |

**El segundo caso es el que más importa y el más fácil de olvidar.** Que la comprobación devuelva algo no sirve si el arranque lo descarta: es el mismo hueco que la fase `A` había encontrado, y probarlo aparte es lo que impide que vuelva.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**No se usa: llega solo.** Al abrir sesión en un proyecto instalado, el arranque pregunta por la versión y muestra el aviso si está atrasado, con el resumen del tramo.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El tramo son **las de en medio y la de llegada**, no la de partida | La versión que ya se tiene no es novedad |
| **Lo que obliga a migrar va primero** | Es lo único del resumen que pide trabajo. Enterrarlo entre títulos lo vuelve invisible |
| Sin registro legible **no se inventa** un tramo | `04·R4`: no afirmar sobre lo que no se leyó |
| El aviso **informa y no dice cómo subir** | Subir es decisión del proyecto. Un aviso que además instruye se lee como una orden |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **El aviso no dice qué hacer para subir.** Es información, no procedimiento | **A propósito**, y dicho para que el «Cumple» no se lea de más |
| La fase quedó con su **cierre en blanco cuatro días**, contada como completa | **Corregido acá.** Es uno de los cuatro casos que destaparon `S-052` |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-004](../HU-004-aviso-al-quedar-atras.md): su §8 nombra esta fase.
- [x] El pendiente que la originó, en `pendientes/hecho/`.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** al abrir sesión, un proyecto atrasado **ahora se entera**, con el resumen de qué cambió.
- **Reversión:** se descarta el commit.
