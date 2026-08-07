> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F8 · Edita solo los archivos que el plan aprobado declara

El agente edita únicamente los archivos de la tabla del plan aprobado ([`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) pregunta 9). Descubrir a mitad de la ejecución que otro archivo también necesita cambios **detiene la ejecución**: se pausa, se reporta, se propone ampliar el plan y se espera OK explícito. Que el cambio sea obvio no autoriza — la aprobación del plan sí. El protocolo completo está en [`base.md`](../base.md).

```
INCORRECTO: durante la ejecución el agente descubre que también hay que editar el
            archivo Y → lo edita en el mismo commit "porque era necesario"
CORRECTO:   descubre Y → PAUSA + reporta + propone ampliar el plan → usuario
            aprueba (o difiere Y a otra fase) → sigue con el plan actualizado
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia; sus citas son referencia · **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
