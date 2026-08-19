> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC19 · Marca con `«…»` los espacios por llenar de un documento modelo

Todo espacio que quien usa un modelo tiene que reemplazar se marca `«…»`, la misma marca en todos los modelos del proyecto. Se marca lo que llena quien usa el modelo: la sintaxis de un comando que se copia y se pega la llena quien lo corre, así que no es un espacio por llenar. El porqué de esta marca y las que se descartaron: [`notas/marca-del-espacio-por-llenar.md`](../../../notas/marca-del-espacio-por-llenar.md).

```
INCORRECTO: un modelo marca sus huecos con [texto], otro con <texto> y un
            tercero con XXX · el corchete además es la sintaxis del enlace,
            así que no se sabe cuál hueco es hueco
CORRECTO:   los tres marcan «texto», que no es sintaxis de nada más
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v13.0.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia; [`DOC20`](DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) se apoyan en esta, pero la dependencia se declara en ellas, no acá · **16**: no tiene excepción. Fila 6: `DOC19` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, cuál es la marca; que un documento con marcas no esté terminado y que lo que no aplica se escriba `N/A` se cumplen por separado, y por eso son [`DOC20`](DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md). Fila 10: el porqué de la marca no cabía en el cuerpo y se fue a `notas/`, como manda la propia fila.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
