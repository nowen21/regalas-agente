> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC4 · Documenta lo que producción necesita

Los pasos de despliegue —cambios de esquema, datos base, permisos, comandos posteriores— se documentan **auto-suficientes y ejecutables**: quien despliega lo hace leyendo el entregable, sin volver a mirar el código.

```
INCORRECTO: "aplicar las migraciones y listo" · el orden y los datos base se
            averiguan leyendo el código
CORRECTO:   la secuencia exacta, con cada comando, su orden y qué verificar
            después de cada uno
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Se le agregó el ejemplo que le faltaba (fila 12).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
