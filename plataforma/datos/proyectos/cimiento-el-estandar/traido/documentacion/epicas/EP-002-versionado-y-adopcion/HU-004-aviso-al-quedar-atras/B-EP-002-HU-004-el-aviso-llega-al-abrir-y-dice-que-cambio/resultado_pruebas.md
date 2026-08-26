# Resultado de Pruebas — Fase B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Qué se midió antes de dejarlo

Corrido sobre shopnest-mesa, el arranque pasó de **un** hallazgo a **tres**: el que ya daba, la falla de la versión contradictoria y el aviso de desfase con su tramo. Y el tramo, leído del registro real: **40 versiones, 5 de ellas obligan a migrar**.

---

## 2. Ejecución caso por caso

| Caso | Qué entra | Qué sale |
|---|---|---|
| El arranque pregunta por la versión | un proyecto instalado | lo hace, y antes no |
| Lo que devuelve llega sin perderse | un hallazgo cualquiera | aparece en la salida del arranque |
| El tramo son las de en medio y la de llegada | de `2.0.0` a `3.0.0` | `2.1.0` y `3.0.0` |
| La adoptada no entra en su propio tramo | ya la tiene | no se cuenta |
| Un proyecto al día tiene tramo vacío | declara la vigente | nada que resumir |
| Lo que obliga a migrar va primero | un tramo con una MAYOR | antes que los títulos |
| Sin registro no se inventa un tramo | carpeta sin registro de cambios | vacío |

**Buena parte de los casos son de lo que NO debe hacer.** Una comprobación que reprueba de más, o un enmascarador que tapa de más, se apaga a la semana, y entonces no queda nada.

---

## 3. Suites que la fase toca  ·  `02·F5`

| Suite | Cuántas |
|---|---|
| test_el_aviso_de_desfase_llega_y_dice_que_cambio | 9 pruebas |

Todas en verde.

---

## 4. Defectos encontrados

Ninguno propio.

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** lo que la fase A dejó en rojo quedó cerrado, comprobado sobre casos reales y no sobre ejemplos escritos para la ocasión.

**Lo que no cubre, dicho para que el «Cumple» no se lea de más:** el aviso sigue sin decir qué hacer para subir. Es información y no procedimiento: subir es decisión del usuario, y así lo dice el mensaje.

---

## 6. Evidencias

- `validadores/sesion.py`
- `validadores/version.py`
- `validadores/tests/test_el_aviso_de_desfase_llega_y_dice_que_cambio.py`
