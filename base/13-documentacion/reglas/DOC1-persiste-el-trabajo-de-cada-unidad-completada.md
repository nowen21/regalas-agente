> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC1 · Persiste el trabajo de cada unidad completada

Al cerrar una unidad, deja en documentación versionada **qué se planeó**, **qué se probó** —incluidas las verificaciones manuales que el entorno automático no cubre ([`08·T4`](../../08-pruebas.md#t4--protege-los-datos-reales-al-probar))— y **qué quedó**: cómo usarlo, puntos de entrada, enlaces al código. El chat no sustituye los archivos.

```
INCORRECTO: implementar, mostrar todo en el chat y cerrar
CORRECTO:   implementar + persistir plan, pruebas y resultado
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Las filas 2 y 4 reprobaban mientras [`02·F6`](../../02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md) exigía lo mismo; [`F6`](../../02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md) quedó derogada en 4.0.0 a favor de esta ([`M11`](../../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
