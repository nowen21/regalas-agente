> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F26 · El inventario de funcionalidades aprobado es la puerta de las épicas

Ninguna épica se deriva sin el **inventario de funcionalidades** de la propuesta, aprobado por el usuario, con estado por ítem y lo no decidido marcado «por confirmar» ([`plantillas/inventario-funcionalidades.md`](../../../plantillas/inventario-funcionalidades.md)). Cada épica cita los ítems que cubre; la que no baje de ninguno no arranca (extiende [`02·F2`](F2-sin-especificacion-acordada-no-hay-codigo.md)).

**Excepción**: los encargos cuyas épicas ya estaban derivadas cuando el proyecto adoptó esta regla no se reabren (condición). No cubre épicas nuevas de ese mismo encargo, que entran por la puerta (límite). Lo acepta el usuario al adoptar la versión que la trae (autoriza).

```
INCORRECTO: el agente escribe el planteamiento asumiendo el techo del alcance y
            deriva tres épicas; la corrección del usuario llega con 21 historias
            ya escritas encima
CORRECTO:   la propuesta llega con su inventario; el usuario aprueba o corrige el
            alcance ahí, y las épicas se derivan citando los ítems que cubren
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v28.2.0**, el **2026-08-21**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.**

**Fila 2 · se buscó por concepto y el capítulo se leyó entero.** [`F2`](F2-sin-especificacion-acordada-no-hay-codigo.md) pone la puerta entre especificación y código; [`F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) exige recorrer la cadena pero no dice qué documento aprueba el alcance en su primer tramo; [`01·C21`](../../01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar) pide el dato ausente de un pedido, y el alcance asumido no era un dato ausente: el pedido estaba completo y el agente le puso techo por su cuenta. Ninguna regla ponía puerta entre la propuesta y las épicas.

**Fila 9 · una sola exigencia.** Lo que se exige es la puerta: inventario aprobado antes de derivar. Que cada épica cite sus ítems es cómo se comprueba que pasó por ella, no una segunda exigencia que se cumpla por separado.

**Fila 16 · la excepción está completa.** Condición (épicas ya derivadas al adoptar), límite (las nuevas entran por la puerta) y quién autoriza (el usuario, al adoptar la versión).

**El caso está medido y es real.** En `shopnest-mesa` el planteamiento nació con el alcance asumido (2026-08-15) y la corrección del usuario llegó el 2026-08-21, con tres épicas y 21 historias escritas. Con esta regla vigente, la derivación se habría detenido en la aprobación del inventario. Es el [pendiente 74](../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md), pedido explícito del usuario.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
