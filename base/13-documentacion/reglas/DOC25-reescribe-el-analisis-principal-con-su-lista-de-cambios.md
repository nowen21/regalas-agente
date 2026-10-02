> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC25 · Reescribe el análisis principal con su lista de cambios

El análisis principal del proyecto o del módulo dice siempre lo que se va a construir hoy: cuando un análisis individual cambia algo, se reescribe y suma a su lista de cambios la fecha y el enlace a ese análisis (deroga [`13·DOC8`](DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)).

```
INCORRECTO: el principal dice «la clase con suma», un análisis individual
            agregó sus propiedades y el principal quedó congelado
CORRECTO:   el principal dice «la clase con suma y sus propiedades» y su
            lista de cambios enlaza el análisis que lo cambió
```

**Aplica a:** escribir-documento

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v40.0.0**, el **2026-10-01**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A, **16**: no tiene excepción. Fila 6: `DOC25` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, que el principal diga lo vigente con la traza de cada cambio; cómo cierra el análisis individual vive en [`DOC24`](DOC24-cierra-el-analisis-en-su-mismo-archivo.md). Fila 14: deroga `DOC8` junto con `DOC24`.

Nace en `EP-023·HU-001`, fase `A`, del análisis 1 del pendiente 103 (conclusión 32) y del análisis 5.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
