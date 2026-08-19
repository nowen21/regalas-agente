> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M6 · Ante un conflicto, el desempate es este y en este orden

1. **¿Una es `[BLINDADA]`?** → gana esa. Fin. No hay paso 2.
2. **¿Una es de capa 3 y la otra de capa 2?** → gana la de capa 3, **solo si** el proyecto la declaró como ajuste explícito (`CLAUDE.md §5.1` o `.agente/reglas-proyecto.md`). El silencio no es un ajuste.
3. **¿Una deroga expresamente a la otra?** → gana la que deroga.
4. **Misma capa:** gana la **más específica** — la que nombra el caso — sobre la general.
5. **Igual de específicas:** gana la **más restrictiva**, la que exige más. Ante la duda, el lado seguro.
6. **Sigue empatado** → es un **defecto del estándar**, no una decisión del agente: **PAUSAR**, reportar el choque al usuario y arreglar la regla. Prohibido elegir en silencio o inventar un tercer camino.

```
INCORRECTO: dos reglas se contradicen → elijo la que me deja avanzar y sigo
CORRECTO:   reporto "01·C3 y 02·F7 chocan en este caso" y espero la decisión
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v2.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A** — **14**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite · **15**: va con la 14 · **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
