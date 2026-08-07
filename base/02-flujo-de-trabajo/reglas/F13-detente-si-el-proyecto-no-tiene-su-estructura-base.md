> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F13 · Detente si el proyecto no tiene su estructura base

Antes de cualquier paso del flujo —incluso antes de cargar contexto ([`02·F1`](F1-carga-el-contexto-antes-de-actuar.md))— el agente valida **un solo hecho**: que exista la carpeta `proyectos/`, donde vive el código del usuario. Si existe, crea su propio espacio al lado (`.agente/`, `prompts/`, `documentacion/`) y continúa. Si no, **no crea nada, se detiene y muestra la orientación** para que el usuario decida la ubicación y los nombres. El árbol completo está en [`estructura-base.md`](../estructura-base.md); el mensaje de orientación y el reparto de mundos, en [`base.md`](../base.md).

```
INCORRECTO: no existe `proyectos/` → el agente crea la estructura que le parece y
            acomoda el código del usuario dentro
CORRECTO:   no existe `proyectos/` → el agente se detiene, muestra la orientación
            y espera a que el usuario cree la carpeta y coloque su código
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. La marca inventada `[GATE DE ARRANQUE · PRECONDICIÓN]`, que [`estructura-regla.md`](../../20-meta-reglas/estructura-regla.md) usa como anti-ejemplo literal de la fila 13, quedó fuera: que corra primero lo dice el capítulo, no una etiqueta. Validable y registrada (`sesion.py`).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
