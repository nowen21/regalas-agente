> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M15 · Toda cita a otra regla lleva su enlace

Citar una regla por su ID no basta: la cita se escribe como enlace al sitio exacto donde vive esa regla — el archivo, y el ancla de su encabezado si comparte archivo con otras (extiende [`M4`](M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), que fija el ID y la forma `NN·ID`). Una cita que obliga a salir a buscar es una dependencia que nadie comprueba.

```
INCORRECTO: No se saltan (`00` · N3).
CORRECTO:   No se saltan ([`00·N3`](../../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Cabe: 304 de 320.** Y vale contar cómo se supo, porque casi queda sellada al revés: la primera medición dio **373** y se escribió el bloque en NO CUMPLE. Ese número era del conteo viejo, el que cobraba el marcado de los enlaces — **corregido esta misma sesión, y `M15` es justamente la regla que obliga a poner esos enlaces**. La regla que más los pide era de las más castigadas por contarlos.

Se volvió a medir antes de dar el bloque por bueno. **Un sello que cita un número sin remedirlo es un sello que hereda el error de quien midió antes.**

**Era la última regla del cuerpo sin su bloque de checklist**, y no por descuido: nació el 2026-08-07 en el mismo cambio que trajo el validador de citas, cuando el procedimiento de [`M14`](M14-ninguna-regla-nace-fuera-del-procedimiento.md) todavía se estaba estrenando. Las 212 restantes ya lo tenían o lo ganaron hoy.

La fila **14** pasa con la dependencia declarada en su cuerpo —*«extiende [`M4`](M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)»*—, que es una de las tres formas que [`M7`](M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) admite. **Es de las pocas del estándar que la declara bien**, y por eso la fila 15 también pasa: `M4` no la extiende de vuelta.

**Su ejemplo es el mejor argumento de la propia regla**: muestra la misma cita escrita mal y bien, y la diferencia se ve sin explicación.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
