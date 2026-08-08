> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC8 · Cierra todo análisis con su tabla de decisiones

Un análisis persistido termina en un **archivo de cierre** con una fila por pregunta abierta o hallazgo: qué se preguntó, qué se decidió, en qué estado quedó y qué hueco dejó. Formato: [`plantillas/cierre-analisis.md`](../../../plantillas/cierre-analisis.md). El análisis original pasa a ser fotografía inmutable, con un aviso al inicio que apunta al cierre.

```
INCORRECTO: el análisis abre 15 preguntas, el usuario las responde en el chat
            y el archivo se queda como si nadie hubiera contestado
CORRECTO:   análisis → respuestas → archivo de cierre con la tabla + aviso en el original
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Fila 10: la ruta canónica, las columnas y el registro en el historial del documento vivo estaban en el cuerpo; viven en la plantilla, que es la fuente única del formato.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
