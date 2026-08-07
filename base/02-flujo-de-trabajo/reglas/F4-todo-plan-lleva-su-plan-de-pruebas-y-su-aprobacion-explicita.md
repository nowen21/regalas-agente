> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F4 · Todo plan lleva su plan de pruebas y su aprobación explícita

Cada plan de trabajo se redacta junto a su plan de pruebas, se **presenta** al usuario y **no se toca código hasta un OK explícito** suyo ([`01·C17`](../../01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación)). Autorizar el inicio de una fase ("arranque con X") **no** aprueba el plan detallado: son dos autorizaciones distintas. Si no existe la HU con sus CA que respalde el plan, **PAUSAR y retroceder** al eslabón que falta (depende de [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), [`02·F2`](F2-sin-spec-acordada-no-hay-codigo.md)).

**Excepción** — un cambio que no amerita prueba (visual o trivial) se entrega sin plan de pruebas si el plan lo **declara** ("Sin pruebas — cambio visual") (condición). No exime de la aprobación explícita ni cubre cambios con lógica, que siempre llevan prueba ([`08·T1`](../../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba)) (límite). Lo acepta el usuario al aprobar el plan (autoriza).

```
INCORRECTO: usuario dice "arranque con Fase X" → agente redacta plan + implementa
            todo seguido → reporta al final
CORRECTO:   usuario dice "arranque con Fase X" → agente redacta plan + pruebas →
            PAUSA + presenta → usuario aprueba (o pide cambios) → agente implementa
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ❌ ❌ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 2 ❌ · 0 N/A.**

**❌** — **8** y **9**: el título lleva "y" porque el cuerpo lleva **dos exigencias** que se cumplen por separado —acompañar el plan con su plan de pruebas, y no ejecutar sin OK explícito—. Partirla exige un ID nuevo, y eso lo decide el usuario ([`M4`](../../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).

> **Regla vigente y reprobada.** Sigue rigiendo —[`M10`](../../20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado— pero no es conforme hasta partirla.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
