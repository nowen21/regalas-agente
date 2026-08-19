> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F18 · Deriva el plan de los CA aprobados, no de la proactividad

Toda intervención listada en el plan —código, migración, seed, vista, prueba— rastrea de forma explícita al **criterio de aceptación** de la HU que la justifica (extiende [`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) · deroga [`02·F4.4`](F4.4-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)). Lo que no venga de un CA se retira del plan y se propone aparte ([`02·F20`](F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

**Excepción** — un ítem sin CA propio se admite como **soporte técnico** cuando sin él el CA es imposible de cumplir (condición). Se declara en §Alcance como "soporte de CA-X" con su justificación, y no alcanza a limpiezas ni mejoras que el CA no necesita (límite). Lo autoriza el usuario al aprobar el plan (autoriza).

```
INCORRECTO: §Alcance dice "también aprovechamos para limpiar el código legacy de Y"
            cuando ningún CA de la fase menciona Y
CORRECTO:   cada línea del plan muestra "intervención → CA"; lo de Y se propone
            como fase aparte con su propia HU
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.1.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.** Toma el contenido de [`F4.4`](F4.4-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md), cuyo ID decimal no admitía [`M4`](../../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) — era su único ❌.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
