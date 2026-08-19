> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F4 · Todo plan lleva su plan de pruebas y su aprobación explícita

Cada plan de trabajo se redacta junto a su plan de pruebas, se **presenta** al usuario y **no se toca código hasta un OK explícito** suyo ([`01·C17`](../../01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación)). Si no existe la HU con sus criterios que respalde el plan, **PAUSAR y retroceder** al eslabón que falta (depende de [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), [`02·F2`](F2-sin-especificacion-acordada-no-hay-codigo.md)).

**Excepción** — un cambio que no amerita prueba (visual o trivial) se entrega sin plan de pruebas si el plan lo **declara** ("Sin pruebas — cambio visual") (condición). No exime de la aprobación explícita ni cubre cambios con lógica, que siempre llevan prueba ([`08·T1`](../../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba)) (límite). Lo acepta el usuario al aprobar el plan (autoriza).

```
INCORRECTO: usuario dice "arranque con Fase X" → agente redacta plan + implementa
            todo seguido → reporta al final
CORRECTO:   usuario dice "arranque con Fase X" → agente redacta plan + pruebas →
            PAUSA + presenta → usuario aprueba (o pide cambios) → agente implementa
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v23.23.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.**

**Partida el 2026-08-18.** Traía dos exigencias: que el plan se presente y no se toque código sin el OK, y que **autorizar el arranque de una fase no sea aprobar su plan**. **Se cumplen por separado**, y la segunda es la que se incumple: nadie se salta el OK del plan a propósito — lo que pasa es que se toma el «arranque con X» por aprobación. Es ahora [`02·F25`](F25-autorizar-el-arranque-no-aprueba-el-plan.md). Del [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**❌** — **8** y **9**: el título lleva "y" porque el cuerpo lleva **dos exigencias** que se cumplen por separado —acompañar el plan con su plan de pruebas, y no ejecutar sin OK explícito—. Partirla exige un ID nuevo, y eso lo decide el usuario ([`M4`](../../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).

> **Regla vigente y reprobada.** Sigue rigiendo —[`M10`](../../20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado— pero no es conforme hasta partirla.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
