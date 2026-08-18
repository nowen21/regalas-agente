> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC11 · Usa la tabla canónica de cinco columnas para la trazabilidad

La verificación que exige [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) se escribe siempre con la misma tabla (extiende [`13·DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md)), en el documento de cierre de la unidad:

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la especificación) | (esquema · modelo · servicio · vista · prueba · permiso · ruta · doc) | (archivo real) | ✅ · ❌ · N/A · parcial | (prueba concreta o commit) |

Todo lo que no sea ✅ lleva justificación escrita: el ❌ dice a qué unidad se traslada, el parcial qué parte queda, el N/A por qué no aplica. Un faltante que debería estar en esta unidad se corrige aquí, no se difiere.

```
INCORRECTO: cerrar con la tabla a medias o con un "N/A porque sí"
CORRECTO:   tabla completa · faltantes justificados · diferimientos con destino explícito
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

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Fila 11: la tabla estaba escrita entera en [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) y otra vez aquí; ahora vive **solo** aquí y [`DOC3`](DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) enlaza. Fila 10: la tabla es el formato que la regla exige, no cuerpo — el cuerpo son tres líneas.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
