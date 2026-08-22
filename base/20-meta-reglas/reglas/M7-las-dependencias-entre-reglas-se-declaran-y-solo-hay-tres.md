> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M7 · Las dependencias entre reglas se declaran, y solo hay tres

Una regla que se apoya en otra lo declara **en su cuerpo, entre paréntesis**, con una de tres formas: `extiende ID` · `depende de ID` · `deroga ID`. No hay una cuarta. Qué significa cada una y sus dos prohibiciones: [`base.md`](../base.md).

```
INCORRECTO: la regla cierra con un párrafo en prosa que "se relaciona con" media docena de reglas
CORRECTO:   (extiende 09·G6), en el cuerpo y entre paréntesis
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 17 reprobaba porque cuatro reglas ([`01·C15`](../../01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa), [`01·C16`](../../01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo), [`01·C18`](../../01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central), [`03·D8`](../../03-datos.md#d8--distingue-pertenencia-de-autoría-en-el-modelo-de-datos)) usaban un bloque `Encadenamiento` que no es ninguna de las tres formas. Las cuatro declaran hoy su dependencia entre paréntesis, en el cuerpo. No queda ninguna cuarta forma en el catálogo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
