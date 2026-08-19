> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M18 · Lo compartido se lee un instante antes de escribirlo

Todo archivo que otra sesión puede estar tocando —`VERSION`, el registro de cambios, un índice, una numeración— se **relee en el momento de escribirlo**, nunca desde lo que se leyó al abrir (extiende [`20·M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)). Decidirlo antes es apostar a que nadie más guarde primero.

```
INCORRECTO: a media sesión se sube VERSION a 10.0.0 y se sigue trabajando dos horas
CORRECTO:   el número se lee de lo guardado y se sube en el mismo movimiento
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v23.10.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** **N/A** — **16**: no tiene excepción.

**Los casos están medidos, y son cuatro, en tres archivos distintos.** El 2026-08-14 dos sesiones dejaron dos numeraciones vivas: una escribió la `10.0.0` mientras la otra subía la `9.0.0`, la `9.1.0` y la `9.2.0`. El 2026-08-16 se crearon **tres pendientes con el número `48`**, y una escritura de un índice compartido falló y hubo que rehacerla. Ese mismo día, una sesión iba a ejecutar un pendiente **que otra ya había hecho entero** sin guardar. Y quedó rastro fijo: el registro tiene **dos entradas para la `15.4.0`**.

**Fila 2 · `M10` ya existía y no alcanzaba.** Dice que el cambio, su entrada y la subida van *«en el mismo movimiento»*, y eso es cierto y no basta: no dice **cuándo se lee** lo que se va a escribir. Una sesión que sube `VERSION` a las once y guarda a las siete cumple `M10` al pie de la letra y deja el cruce igual.

**Fila 17 · no choca con `M10`, la concreta.** `M10` pide que vayan juntos; esta dice en qué momento se mira lo compartido. Por eso `extiende` y no `deroga` — nada de lo que `M10` exige deja de exigirse.

**Por qué no se acotó a `VERSION`.** Los cuatro casos son el mismo defecto en archivos distintos, y una regla que solo nombrara la versión dejaría fuera al número del pendiente y a los índices, que ya se rompieron. Además **quita la pregunta de encima**: releyendo al escribir no hace falta enterarse de que hay otra sesión viva.

**Lo que no arregla.** Dos sesiones que escriben **en el mismo segundo** siguen pudiendo chocar: esto reduce la ventana de horas a instantes, no la cierra. Lo que quede del cruce sobre la numeración lo ve `validar.py versionado`.

**Los números ya repetidos se quedan.** Por [`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) un cambio de norma no reabre lo cerrado, y renumerar una versión que un proyecto pudo haber adoptado le movería el piso sin que se entere: se marcan en el registro y se ven como aviso.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
