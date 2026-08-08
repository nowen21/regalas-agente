> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F0 · Recorre la cadena completa, sin saltar eslabones

Todo desarrollo —funcionalidad nueva o cambio de comportamiento— recorre `brief → épica → HU → spec → plan → código`, grande o chico. Ningún eslabón se salta, se fusiona ni se omite por tamaño. Si te piden un paso y falta el anterior, **PAUSAR y crearlo primero** (depende de [`02·F2`](F2-sin-spec-acordada-no-hay-codigo.md), [`13·DOC15`](../../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md)).

**Excepción** — lo que **no es desarrollo** queda fuera de la cadena: leer o investigar, configuración local, comandos que el usuario pide, y el arreglo que solo devuelve el código a lo que ya decía la spec (condición). Cubre ese trabajo puntual; no habilita a construir funcionalidad sin cadena (límite). Si hay duda de si el caso es desarrollo, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza).

```
INCORRECTO: llega una idea → se escribe el plan de trabajo directo
CORRECTO:   idea → análisis → objetivo y alcance → épica → HU → spec
            → plan → construir
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v2.5.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.** Es el texto corregido que [`estructura-regla.md`](../../20-meta-reglas/estructura-regla.md) ya publicaba como versión conforme; el mapa de siete pasos y el encadenamiento que antes vivían aquí están en [`base.md`](../base.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
