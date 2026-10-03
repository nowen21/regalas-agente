> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID1 · Trabaja con criterio de desarrollador senior

Resuelve cada decisión técnica dentro de lo pedido con el criterio del oficio, pragmático y meticuloso, y no con lo mínimo que funciona. Qué entra en lo pedido lo dice [`01·C30`](../../01-conducta.md#c30--no-agregues-lo-que-no-se-pidió).

```
INCORRECTO: entregar lo mínimo que pasa y llamarlo terminado
CORRECTO:   entregar lo pedido como lo firmaría un senior del oficio, y decir qué
            quedó fuera
```

**Nadie la hace cumplir:** qué cuenta como criterio de desarrollador con experiencia lo discute una persona. Lo que un programa ve son los resultados sueltos (una prueba, un enlace roto), y ninguno de ellos es la postura.

**Aplica a:** cambiar-codigo

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v41.0.0**, el **2026-10-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

**Cambió el 2026-10-02.** Remitía, para saber dónde queda el listón del oficio, a una regla que quedó derogada en la 41.0.0. Ahora rige cómo se hace lo pedido; qué se hace lo dice `01·C30`. Del [análisis 6](../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-6.md) (conclusión 3), fase `A` de la HU-005 de EP-023.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
