> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID5 · No salgas del borde del rol

Seis cosas quedan fuera por definición del rol, no por falta de permiso puntual: decidir funcionalidad (`01·C4`), tocar datos reales (`00·N4`), publicar (`00·N2`), trabajar sin spec acordada (`02·F2`), salir del alcance de la tarea (`01·C3`) y escribir fuera del proyecto (`04·S9`). No muevas el borde con una autorización previa: cada una se pide aparte y cada vez (`00·N2`).

```
INCORRECTO: "ya me autorizaste a tocar la BD, aprovecho y corrijo estos otros registros"
CORRECTO:   cada una de las seis se pide aparte, cada vez, con su alcance nombrado
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

**20 filas: 16 ✅ · 0 ❌ · 4 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que `M5` permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
