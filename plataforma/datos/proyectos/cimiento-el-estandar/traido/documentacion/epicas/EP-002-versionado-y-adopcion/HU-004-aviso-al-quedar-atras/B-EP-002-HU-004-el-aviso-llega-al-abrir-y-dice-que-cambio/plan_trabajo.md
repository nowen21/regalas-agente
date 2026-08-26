# Plan de Trabajo — Fase B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio (módulo Enganches de sesión)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio` |
| **Épica** | `EP-002` |
| **HU** | `HU-004` |
| **Módulo** | Enganches de sesión |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:** 📝 **Modifica fase.** Cierra en rojo lo que la fase A de esta misma historia dejó al ejecutarse el 2026-08-22, anotado entonces en el [pendiente 83](../../../../../pendientes/hecho/el-aviso-de-desfase-no-llega-al-abrir-sesion.md).

---

## 1. Objetivo y alcance

**El problema.** El aviso estaba construido y había que pedirlo a mano: el arranque de sesión no lo miraba. La funcionalidad central de esta historia se veía funcionar **solo en el repositorio del estándar**, donde el agente corre las comprobaciones de a una, y no llegaba nunca a un proyecto instalado. Además nombraba las dos versiones sin decir qué las separa.

**Lo que entra:**

- El arranque pregunta por la versión del proyecto y entrega lo que salga.
- El aviso dice qué cambió: versión, tipo y título, que es lo que fijó la decisión 24.
- Lo que obliga a migrar va primero, porque es lo único que cambia qué hacer.

**Fuera de alcance:** el aviso sigue sin decir qué hacer para subir. Es información y no procedimiento: subir es decisión del usuario, y así lo dice el mensaje.

---

## 2. Análisis previo — línea base verificada

Corrido sobre shopnest-mesa, el arranque pasó de **un** hallazgo a **tres**: el que ya daba, la falla de la versión contradictoria y el aviso de desfase con su tramo. Y el tramo, leído del registro real: **40 versiones, 5 de ellas obligan a migrar**.

### 2.1 Archivos que se crean o modifican

- `validadores/sesion.py`
- `validadores/version.py`
- `validadores/tests/test_el_aviso_de_desfase_llega_y_dice_que_cambio.py`

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El aviso se cuelga de la revisión de arranque | Un enganche nuevo | Esa revisión ya devuelve hallazgos que el arranque imprime; agregar uno no cambia el contrato de nadie |
| Primero conectar, después completar | Completar el mensaje primero | Conectar un aviso incompleto ya sirve; completar un aviso que nadie recibe, no |
| El detalle es versión, tipo y título | Contar el cambio con más detalle | Menos no ayuda a decidir; más obliga a mantener dos textos que dicen lo mismo, y el segundo envejece |

---

## 3. Verificación

Los casos del `resultado_pruebas` §2, y las suites que la fase toca. **La batería entera no**, que es lo que `02·F5` pone como INCORRECTO y que en esta misma jornada ya costó catorce minutos y once rojos que ya existían.

---

## 4. Reversión

Revertir el commit de la fase. Todo es aditivo sobre funciones que ya existían.

---

## 5. Reglas aplicadas

- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente baja a fase.
- [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), por el alcance de la corrida.
- [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), porque se midió antes de dejar el criterio.
- `20·M10`, por la versión y el registro.

---

## 6. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
