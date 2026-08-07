> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F5 · Corre solo las suites que la fase toca

La corrida que cierra una fase alcanza la suite del módulo de la fase, las suites que la fase refactorizó y las que dependen de los archivos tocados según la matriz de [`02·F17`](F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) — no la suite completa del proyecto (extiende [`08·T5`](../../08-pruebas.md#t5--ejecuta-y-reporta), que ya obliga a correrlas y a reportar el conteo).

**Excepción** — la corrida global se hace cuando se declara **explícitamente** como "regresión total pre-release" (condición). No entra en el flujo normal de fase (límite) y la pide el usuario (autoriza).

```
INCORRECTO: al terminar la fase, correr toda la suite del proyecto "por si acaso"
            → cientos de pruebas, minutos de espera y rojos que ya existían antes
CORRECTO:   correr la suite del módulo + las declaradas en el plan + las que la
            matriz de dependencias señala
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ❌ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 1 ❌ · 0 N/A.**

**❌** — **4**: el dueño del tema *pruebas* es el capítulo [`08`](../../08-pruebas.md) ([`M2`](../../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)). El texto duplicado —"se corren, no solo se escriben", con su ejemplo palabra por palabra— ya se reemplazó por el enlace a [`08·T5`](../../08-pruebas.md#t5--ejecuta-y-reporta), pero mover el alcance quirúrgico de la corrida al capítulo 08 y derogar `F5` lo decide el usuario ([`M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

> **Regla vigente y reprobada.** Sigue rigiendo hasta que el usuario decida la vía.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
