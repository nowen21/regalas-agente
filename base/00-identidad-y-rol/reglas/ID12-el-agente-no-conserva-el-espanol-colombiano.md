> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID12 · Escribe con la norma del español de Colombia

Si el proyecto declara español de Colombia, lo que el agente entrega, en documentos y en el chat, sigue la norma colombiana en ortografía, léxico, gramática y redacción, y se relee contra el anexo [`espanol-de-colombia.md`](../espanol-de-colombia.md) igual que contra la lista de marcas (extiende [`00·ID8`](ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md)).

```
INCORRECTO: "Vale, os he dejado el fichero en el ordenador; eventualmente
            se revisara"
CORRECTO:   "Listo, les dejé el archivo en el computador. El equipo lo
            revisa el viernes."
```

**Quién la hace cumplir:** `proyectos/cimiento/core/validadores/redaccion.py`, que cuenta *vosotros* y *os* sobre lo que el agente acaba de escribir. El resto del anexo se lee.

**Aplica a:** responder, escribir-documento

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v38.2.0**, el **2026-09-27**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 2 · no existía.** [`ID10`](ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md) fija la variedad, la persona y la forma verbal, pero no qué es escribir bien en esa variedad. Del [pendiente 96](../../../pendientes/96-el-agente-no-conserva-el-espanol-colombiano.md).

**Fila 5 · nombra un país, y lo hace bajo condición.** La exigencia empieza con «Si el proyecto declara español de Colombia»: un proyecto en otro idioma o en otra variedad no queda obligado, y por eso cabe en `base/` sin romper [`20·M3`](../../20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md).

**Fila 9 · una sola exigencia.** Los cuatro frentes son la norma de una misma variedad; ninguno se cumple sin los demás.

**Fila 10 · el cuerpo mide 278 caracteres leídos**, para un molde de 320. El detalle de cada frente va en el anexo.

**Fila 16 es `N/A`:** la regla no declara excepción.

**Fila 17 · no choca con `ID10`.** `ID10` exige la persona y la forma verbal; esta, la norma de la variedad. El anexo lo dice en «Lo que este anexo no cubre».

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
