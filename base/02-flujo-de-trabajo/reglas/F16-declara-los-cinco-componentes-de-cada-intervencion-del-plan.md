> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F16 · Declara los cinco componentes de cada intervención del plan

Cada intervención que el plan declara dice **qué** se hace, **cómo** se hace, **dónde** exactamente, **por qué** —qué gap cierra— y con qué **impacto** sobre el resto del sistema (extiende [`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) · deroga [`02·F4.3`](F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)). Quedan fuera los verbos vagos —"ajustar", "revisar", "mejorar"— y los alcances abiertos: "y lo demás que aplique". Qué se espera de cada componente: [`base.md`](../base.md).

```
INCORRECTO: "revisar el servicio de facturación y mejorar lo que haga falta"
CORRECTO:   "modificar `<ruta>`: agregar el parámetro `bar` a `foo()` para cerrar
            el gap-3; rompe los dos llamadores de `<ruta B>`, que también entran"
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.1.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Es la primera de las dos exigencias que [`F4.3`](F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) tenía juntas —declararlo y verificarlo se cumplen por separado—; la segunda es [`F17`](F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
