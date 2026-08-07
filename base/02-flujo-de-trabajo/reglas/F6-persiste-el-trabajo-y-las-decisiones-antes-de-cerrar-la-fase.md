> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F6 · Persiste el trabajo y las decisiones antes de cerrar la fase

Ninguna fase se cierra sin dejar en documentación versionada qué se planeó, qué se probó, qué quedó y **las decisiones no obvias con su porqué** (depende de [`13·DOC1`](../../13-documentacion.md#doc1--persiste-el-trabajo-de-cada-unidad-completada), que fija el formato). El chat se pierde; los archivos quedan.

```
INCORRECTO: fase terminada y probada → commit → la decisión de por qué se eligió
            ese diseño vive solo en el chat, que mañana no existe
CORRECTO:   fase terminada → se escribe qué se planeó, qué se probó y por qué se
            decidió así → commit
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ❌ ✅ ❌ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 2 ❌ · 1 N/A.** N/A — **16**: no tiene excepción.

**❌** — **2** y **4**: [`13·DOC1`](../../13-documentacion.md#doc1--persiste-el-trabajo-de-cada-unidad-completada) ya exige lo mismo, y el dueño del tema *documentación* es el capítulo [`13`](../../13-documentacion.md) ([`M2`](../../20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md), [`M12`](../../20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md)). Lo que aporta `F6` es el momento —el cierre de la fase—, no la obligación. Derogarla a favor de [`13·DOC1`](../../13-documentacion.md#doc1--persiste-el-trabajo-de-cada-unidad-completada) lo decide el usuario ([`M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

> **Regla vigente y reprobada.** Sigue rigiendo hasta que el usuario decida la vía.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
