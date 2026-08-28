# Plan de Pruebas — Fase `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio`   ·   `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó y se cerró el 2026-08-22 y **este documento se quedó siendo la plantilla en blanco**: 363 líneas de molde con 36 marcadores sin reemplazar. Lo destapó la [HU-022](../../../EP-004-comprobacion-automatica/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md).
>
> **No se inventa nada.** Los casos salen del [resultado_pruebas.md](resultado_pruebas.md), que sí se escribió y documenta qué entró y qué salió en cada uno, y de las 9 pruebas que quedaron en el repositorio. **Lo que no se puede reconstruir —qué se pensó antes de ejecutar— no se escribe.**

---

## 1. Propósito y alcance

Comprobar que **el aviso de desfase llega solo al abrir la sesión**, y que dice **qué cambió**.

El aviso estaba construido y había que pedirlo a mano. Se veía funcionar **solo en el repositorio del estándar**, donde el agente corre las comprobaciones de a una, y **no llegaba nunca a un proyecto instalado** — que es el único sitio donde hace falta.

**Entra:** que el arranque pregunte por la versión y entregue lo que salga; que el aviso diga versión, tipo y título; y que **lo que obliga a migrar vaya primero**.

**No entra:** decir **qué hacer** para subir. Es información y no procedimiento: subir lo decide el usuario, y el mensaje lo dice así.

---

## 2. Estrategia

**Unitario** sobre registros de cambios de mentira, y **de sistema** sobre `shopnest-mesa` sin tocarlo.

**Se prueba el arranque entero, no la función suelta.** El defecto de esta fase no era que la función estuviera mal: era que **nadie la llamaba**. Una prueba que invoque el aviso directamente pasaría en verde con el defecto puesto.

---

## 3. Casos de prueba

| Caso | Qué entra | Qué debe salir |
|---|---|---|
| **CP-001** · el arranque pregunta por la versión | un proyecto instalado | **Lo hace, y antes no** |
| **CP-002** · lo que devuelve llega sin perderse | un hallazgo cualquiera | Aparece en la salida del arranque |
| **CP-003** · el tramo son las de en medio y la de llegada | de `2.0.0` a `3.0.0` | `2.1.0` y `3.0.0` |
| **CP-004** · la adoptada no entra en su propio tramo | ya la tiene | **No se cuenta** |
| **CP-005** · un proyecto al día tiene tramo vacío | declara la vigente | Nada que resumir |
| **CP-006** · lo que obliga a migrar va primero | un tramo con una MAYOR | Antes que los títulos |
| **CP-007** · sin registro no se inventa un tramo | carpeta sin registro de cambios | Vacío |

**El `CP-001` es el que define la fase.** Es el que distingue «la funcionalidad existe» de «la funcionalidad llega», y era exactamente lo que faltaba.

**El `CP-004` es el borde que se cuela:** incluir la versión que ya se tiene infla el tramo y hace que un proyecto al día parezca atrasado en uno.

---

## 4. Criterio de aprobación

- Los siete casos, ejecutados.
- **El arranque corrido sobre un proyecto real instalado**, no sobre el repositorio del estándar.
- La suite en verde.

---

## 5. Qué se ejecutó, y con qué resultado

Está en el [resultado_pruebas.md](resultado_pruebas.md). En corto: sobre `shopnest-mesa` el arranque pasó de **un** hallazgo a **tres** — el que ya daba, la falla de la versión contradictoria y el aviso de desfase con su tramo. El tramo, leído del registro real: **40 versiones, 5 de ellas obligan a migrar**. La suite `test_el_aviso_de_desfase_llega_y_dice_que_cambio` dio **9 pruebas en verde**.

---

## 6. Herramientas y datos

`unittest`, y `shopnest-mesa` como proyecto real sin modificar. **Ninguna prueba usa credenciales** (`00·N6`).

---

## 7. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | **Retrodocumentado.** La fase cerró el 2026-08-22 sin este documento |
