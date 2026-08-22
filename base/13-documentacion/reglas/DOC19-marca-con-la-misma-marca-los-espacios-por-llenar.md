> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC19 · Marca con `«…»` los espacios por llenar de un documento modelo

Todo espacio que quien usa un modelo tiene que reemplazar se marca `«…»`, la misma marca en todos los modelos del proyecto. Se marca lo que llena quien usa el modelo: la sintaxis de un comando que se copia y se pega la llena quien lo corre, y no es un espacio por llenar.

```
INCORRECTO: un modelo marca sus huecos con [texto], otro con <texto> y un
            tercero con XXX · el corchete además es la sintaxis del enlace,
            así que no se sabe cuál hueco es hueco
CORRECTO:   los tres marcan «texto», que no es sintaxis de nada más
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia; [`DOC20`](DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) se apoyan en esta, pero la dependencia se declara en ellas, no acá · **16**: no tiene excepción. Fila 6: `DOC19` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, cuál es la marca; que un documento con marcas no esté terminado y que lo que no aplica se escriba `N/A` se cumplen por separado, y por eso son [`DOC20`](DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) y [`DOC21`](DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md). Fila 10: el porqué de la marca no cabía en el cuerpo y se fue a `notas/`, como manda la propia fila.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
