> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC9 · Consulta el mapa de dependencias antes de planificar

Al planificar una unidad de trabajo, lee primero el mapa de dependencias del proyecto —la ruta la declara la capa 3— y explora el código solo si el mapa no cubre la duda o si lo que dice no coincide con lo que hay. Es la fuente autoritativa de cómo está armado el sistema hoy; explorar de cero lo que ya está mapeado es releer quince archivos para saber lo mismo.

```
INCORRECTO: abrir la unidad y explorar el proyecto entero como si fuera la primera vez
CORRECTO:   leer el mapa → si hay duda puntual, verificarla en el archivo concreto
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Fila 9: la regla traía dos exigencias que su propio título anunciaba —consultar antes **y** actualizar después—; la segunda es ahora [`DOC18`](DOC18-actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
