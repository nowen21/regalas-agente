> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M20 · Antes de publicar una versión se barre lo que se pidió dos veces

Antes de publicar una versión se relee el tramo cerrado (resúmenes, pendientes y señales) y lo que el usuario pidió **dos veces o más** se escribe en el barrido de candidatas, con su salida: cubierta, regla nueva, afinar una, o no es regla (extiende [`01·C10`](../../01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla)). Molde: [`plantillas/candidatas-a-regla.md`](../../../plantillas/candidatas-a-regla.md).

```
INCORRECTO: el criterio se pidió en tres sesiones, nadie lo notó en el momento,
            y a la cuarta el usuario lo corrige otra vez
CORRECTO:   al cerrar la versión se barre el tramo, sale la candidata con las
            tres veces que se pidió, y el usuario decide si se escribe
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v30.9.1**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** **N/A** — **16**: no tiene excepción. Que el tramo no deje ninguna candidata no es un caso exento: el barrido se hace igual y su resultado es «ninguna», que es un dato.

**Fila 2 · se buscó por concepto antes de escribirla** ([`M12`](M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)). [`01·C10`](../../01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla) exige notar el patrón **en el momento** en que el pedido llega, y [`01·C26`](../../01-conducta.md#c26--la-regla-que-serviría-en-otra-empresa-va-a-la-base-común) decide dónde vive la regla que sale de ahí. Ninguna de las dos cubre lo que esta pide: **volver a mirar el tramo entero cuando ya pasó**, que es justo lo que atrapa lo que en el momento no se notó. Por eso extiende a `C10` en vez de afinarla: dentro de `C10` sería un «y además», que la fila 9 prohíbe.

**Fila 4 · el dueño del tema es este capítulo.** Cómo nace una regla es materia del `20` ([`M13`](M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)); el `01` es la conducta del agente frente al usuario, que es donde `C10` está bien.

**Fila 9 · una sola exigencia.** Barrer y escribir el resultado no se cumplen por separado: un barrido que no queda escrito no se puede contrastar ni volver a correr, y es exactamente lo que pasó con el único barrido que existía, hecho a mano el 2026-08-13 y sin nada que obligara al siguiente.

**Fila 19 · el disparo es el cierre de versión, y no es casual.** Es el único momento del flujo en que ya hay un tramo cerrado que releer, y coincide con [`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), que ya obliga a parar ahí a escribir la entrada del registro. Enganchar el barrido a un momento que no existe en el flujo lo habría dejado, otra vez, en «se hace cuando lo pidan».

**De dónde sale.** El punto 2 del [pendiente 33](../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), abierto desde el 2026-08-06: el barrido se había hecho **una vez**, salieron doce candidatas, y quedó sin molde y sin disparador. Lo que ese punto decía con sus palabras es lo que esta regla arregla: *«sin disparador, se hace cuando el usuario lo pida es un favor, no una norma»*.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
