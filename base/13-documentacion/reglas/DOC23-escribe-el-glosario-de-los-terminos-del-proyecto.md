> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC23 · Escribe el glosario de los términos del proyecto

Todo proyecto mantiene el glosario de las palabras de su negocio: cada término en una línea, entendible por quien no conoce el dominio, y actualizado en el mismo cambio que introduce el término.
Dónde vive lo declara la capa 3; el modelo es el glosario del propio estándar ([`base/glosario.md`](../../glosario.md)).

```
INCORRECTO: dos documentos del mismo proyecto llaman "cliente" a cosas distintas
            y nadie lo nota hasta que el código ya está escrito
CORRECTO:   "cliente" definido en una línea en el glosario del proyecto, y los
            dos documentos usándolo igual
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v17.0.0**, el **2026-08-16**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia; su cita al glosario del estándar es referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **16**: no tiene excepción.

La fila **2** obligó a buscar dos veces. [`DOC10`](DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md) cataloga las **reglas** propias del proyecto y [`DOC13`](DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) sus **módulos**; ninguna toca las palabras. Lo más cercano era `plantillas/mapeo-nombres.md`, que traduce un concepto de la base al nombre que tiene acá —"catálogo" pasa a ser tal tabla—, y eso es otra cosa: acá se definen las palabras que el negocio ya trae y la base no nombra. La sección **Glosario** de `plantillas/dominio.md` existía desde antes; lo que no existía era la regla que obligara a llenarla.

La fila **4** se revisó contra el capítulo [`00 · Identidad y rol`](../../00-identidad-y-rol/base.md), dueño de cómo se escribe: [`ID7`](../../00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) exige que todo texto se entienda sin saber del tema, y esta exige que exista el documento donde viven las palabras. Son cosas distintas y se cumplen por separado.

La fila **5** no nombra sector ni cliente: el ejemplo usa "cliente" como palabra corriente, no como el negocio de nadie.

La fila **9** es una sola exigencia: que el glosario exista y esté al día. Que cada término quepa en una línea y se entienda no es una segunda exigencia, es cómo se cumple la primera.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
