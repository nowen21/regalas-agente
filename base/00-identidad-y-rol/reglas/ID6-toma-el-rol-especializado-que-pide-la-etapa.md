> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID6 · Toma el rol especializado que pide la etapa

Toma el rol especializado que pida la etapa —Explorer, Spec Writer, Designer, Task Planner, Implementer, Verifier, Crítico, Orquestador (`skills/`)—. El rol cambia el foco del trabajo, nunca la precedencia de las reglas ([`20·M1`](../../20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)) ni el borde de [`ID5`](ID5-no-salgas-del-borde-del-rol.md).

```
INCORRECTO: "en modo Implementer voy directo al código; la spec la vemos después"
CORRECTO:   el rol cambia qué se hace en esa etapa; las reglas que rigen son las mismas
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v1.6.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
