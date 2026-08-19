> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC18 · Actualiza el mapa de dependencias al cerrar la unidad

El mapa que [`DOC9`](DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) manda consultar se actualiza en el **mismo cambio** que cierra la unidad (extiende [`13·DOC9`](DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)): lo que se agregó, con qué se relaciona y quién lo consume. Un mapa que se actualiza "después" es un mapa que la próxima unidad ya no puede creer, y entonces vuelve a explorar de cero.

```
INCORRECTO: cerrar la unidad y dejar el mapa para más adelante
CORRECTO:   el cambio que cierra la unidad incluye el mapa al día
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Fila 6: `DOC18` es el siguiente consecutivo libre. La exigencia no es nueva: era la segunda mitad de [`DOC9`](DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md), que pedía dos cosas cumplibles por separado —se puede consultar el mapa y no actualizarlo— y por eso eran dos reglas.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
