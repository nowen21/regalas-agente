> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F30 · Toda acción trae su contraria

Lo que crea o cambia algo se entrega con la acción que lo deja como estaba, como crear y quitar. Sin ella no está terminado; el plan la declara y lleva prueba ([`08·T1`](../../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba)).

**Excepción:** lo que no tiene vuelta (condición) va sin contraria si el plan dice por qué (límite) y el usuario lo aprueba (autoriza).

```
INCORRECTO: la herramienta crea una carpeta y su fila en el índice; si se creó
            mal, hay que borrar la carpeta y la fila a mano
CORRECTO:   la misma herramienta trae «quitar», que borra las dos cosas juntas,
            y su prueba crea, quita y deja el índice como estaba
```

**Aplica a:** trabajar-cadena, cambiar-codigo

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v55.0.0**, el **2026-10-05**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A, **14** y **15**: no extiende, no depende ni deroga ninguna; cita `08·T1` para no repetir que la contraria lleva prueba. Fila 2: se buscó por concepto («contraria», «deshacer», «revertir», «reversión», «desinstalar»); solo [`03·D2`](../../03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible) se parece, y es un caso de esta para el esquema de datos. Fila 4: va en el `02` porque dice cuándo algo construido está terminado. Fila 6: `F30` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, entregar la contraria; la prueba la pide `08·T1` y la sección del plan es dónde se declara. Fila 17: el §7 del plan es la reversión del cambio si sale mal, no la acción contraria que se ofrece.

**No validable:** que la contraria sea la que corresponde es criterio. Lo que un programa podría ver, que el plan traiga la sección 2.8 llena, se automatiza cuando la regla demuestre que se cumple a mano ([`20·M19`](../../20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md)).

Nace del análisis 3 del pendiente 119 (acuerdo 2), cuando el andamio creó una historia con el número equivocado y no había cómo quitarla.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
