> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M17 · La entrada del registro abre en castellano llano

La entrada de `CHANGELOG.md` abre con **qué cambió y por qué**, en dos frases que se entienden sin conocer el proyecto: sin identificador de regla, sin ruta y sin las palabras de la casa (extiende [`20·M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
El detalle va debajo, con sus enlaces, para quien los necesite.

```
INCORRECTO: **MENOR** — la fila 12 del checklist pide ejemplo en `plantillas/planes/resultados.md`
CORRECTO:   Al anotar que una prueba pasó ahora hay que decir con qué se probó.
            Antes se anotaba solo «aprobado», y así nadie podía repetirla.
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v23.8.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace de una prueba que salió mal.** El `CA-03` de [EP-002 · HU-002](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/HU-002-registro-de-cambios.md) exige que una entrada se entienda sin haber seguido el trabajo. Se le mostró al usuario la entrada de la `15.2.0` y respondió **«no entendí nada»**.

**Y no era una entrada mala: eran todas.** De las 83 del registro, **74 citan una ruta de archivo, 43 un identificador de regla, y ninguna tiene menos de tres marcas de jerga**. Están escritas para adentro.

**Fila 4 · el capítulo es este y no el `00`.** Escribir para que se entienda ya lo pide [`00·ID7`](../../00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md); lo que esta regla fija es **la forma de un documento concreto**, y el dueño del `CHANGELOG` es `M10`.

**Fila 11 · no es texto prestado.** `ID7` dice cómo se escribe cualquier cosa; esta dice **por dónde abre** una entrada del registro y qué va debajo. Es la parte propia.

**Por [`M10`](M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), las 83 viejas se quedan como están:** un cambio de norma no reabre lo cerrado. Reescribirlas es trabajo aparte y no urge — lo que urge es que la próxima nazca legible.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
