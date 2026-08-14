> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC3 · Verifica la trazabilidad especificación → implementación antes de cerrar

Antes de cerrar, revisa ítem por ítem que cada afirmación técnica de la especificación ([`02·F2`](../../02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md)) esté en el código, el esquema, las pruebas y los docs (depende de [`02·F2`](../../02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md)). Lo faltante se corrige o se justifica; no se cierra con huecos sin explicar. El formato de la tabla lo fija [`DOC11`](DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md).

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + tabla de trazabilidad sin faltantes → cierro"
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Las filas 2 y 4 reprobaban mientras [`02·F7`](../../02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md) exigía lo mismo con el ejemplo idéntico; [`F7`](../../02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md) quedó derogada en 4.0.0 a favor de esta ([`M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)). La tabla que se repetía aquí y en [`DOC11`](DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) quedó solo en [`DOC11`](DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) (fila 11).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
