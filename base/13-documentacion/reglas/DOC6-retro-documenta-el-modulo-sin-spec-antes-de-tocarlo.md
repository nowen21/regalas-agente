> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC6 · Retro-documenta el módulo sin spec antes de tocarlo

Un módulo productivo sin spec —o con una spec más vieja que el código— se retro-documenta como **unidad de trabajo formal** antes de intervenirlo, siguiendo [`plantillas/retrodocumentacion.md`](../../../plantillas/retrodocumentacion.md). Queda en estado provisional: cierra en el primer audit profundo.

```
INCORRECTO: encontrar un módulo sin spec y decir "asumo que hace X" en la próxima fase
CORRECTO:   retro-documentarlo primero · el análisis persistido queda como fotografía
            del punto de partida
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Filas 9 y 10: el procedimiento de seis pasos que ocupaba el cuerpo pasó a la plantilla; la exigencia —retro-documentar antes de tocar— es una sola.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
