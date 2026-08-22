> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M19 · La regla se automatiza cuando ya se cumple a mano

Antes de construir el programa que comprueba una regla (extiende [`20·M9`](M9-toda-regla-declara-si-es-validable.md)), se deja escrito si hoy se cumple a mano, cuántas veces se incumplió y por qué, y cuántas falsas alarmas daría. Si se incumple porque está mal escrita, se corrige la regla; si lo único que falla es acordarse, se automatiza ya.

```
INCORRECTO: la regla se incumple seis veces porque exige dos cosas; se le construye
            el validador tal cual, y ahora falla sola en cada commit
CORRECTO:   se mira por qué se incumplió → estaba mal escrita → se parte en dos, y el
            validador se construye sobre la regla corregida
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v27.2.0**, el **2026-08-20**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** **N/A** — **16**: no tiene excepción. La última frase no lo es: es lo que se hace con la respuesta, y es la que impide usar la regla como excusa para no automatizar nunca.

**Fila 2 · se buscó por concepto y el capítulo se leyó entero.** [`M9`](M9-toda-regla-declara-si-es-validable.md) responde **si se puede** comprobar con un programa; no dice si **conviene** hacerlo ya. [`revision-de-vigencia.md`](../revision-de-vigencia.md) pregunta si una regla sigue sirviendo después de escrita, no antes de automatizarla. Y el criterio del backlog de automatizaciones —*si depende de leer o decidir lo hace el agente; si es una comparación, lo hace un programa*— reparte quién hace qué, no cuándo. Afinar `M9` no alcanzaba: la pregunta nueva sería un «y además» dentro de ella, que es lo que la fila 9 prohíbe. Por eso **extiende** y no afina.

**Fila 9 · una sola exigencia.** Lo que se exige es responder las tres preguntas **antes** de construir. La segunda frase dice qué se hace con cada respuesta; no se puede cumplir por separado, porque sin la respuesta no hay nada que seguir.

**Fila 17 · no choca con `M9`.** `M9` dice que una regla validable que nadie valida no se cumple; esta no dice que no se valide: dice qué va primero. El validador llega igual — sobre una regla que ya demostró servir.

**Los casos están medidos, y son del propio repositorio.** El ítem 06 del backlog de automatizaciones (la puerta [`F2`](../../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) mecánica) es de prioridad alta y quedó de penúltimo porque, sin las piezas que lo alimentan, su tasa de falsas alarmas lo volvía inservible: la tercera pregunta, descubierta caso por caso en vez de aplicada como regla. Y [`F4`](../../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) reprobó su propio checklist por exigir dos cosas, y de ahí salieron [`F4.1`](../../02-flujo-de-trabajo/reglas/F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) a [`F4.5`](../../02-flujo-de-trabajo/reglas/F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md): de haberse automatizado tal cual, el validador habría congelado la regla doble.

**El dato de la segunda pregunta ya existe.** Cuántos incumplimientos produce hoy cada regla lo lista `validar.py vigencia` ([`CA-04`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md#ca-04--se-sabe-qué-reglas-llevan-más-tiempo-sin-que-nadie-las-revise) de HU-007). Sin ese número la pregunta no se podía contestar, y era lo que dejaba el criterio en opinión.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
