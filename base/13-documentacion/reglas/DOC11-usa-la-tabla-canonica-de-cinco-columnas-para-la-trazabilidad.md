> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC11 · Usa la tabla canónica de cinco columnas para la trazabilidad

La verificación que exige [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) se escribe en el documento de cierre con la [tabla canónica de cinco columnas](../tabla-de-trazabilidad.md), y todo lo que no sea ✅ lleva su justificación escrita; el faltante que era de esta unidad se corrige acá, no se difiere.

```
INCORRECTO: cerrar con la tabla a medias o con un "N/A porque sí"
CORRECTO:   tabla completa · faltantes justificados · diferimientos con destino explícito
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Fila 11: la tabla estaba escrita entera en [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) y otra vez aquí; ahora vive **solo** aquí y [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) enlaza. Fila 10: la tabla es el formato que la regla exige, no cuerpo — el cuerpo son tres líneas.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
