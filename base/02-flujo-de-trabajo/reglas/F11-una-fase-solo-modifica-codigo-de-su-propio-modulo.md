> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F11 · Una fase solo modifica código de su propio módulo

Todos los archivos que una fase modifica pertenecen al módulo que declaró al abrirse ([`13·DOC12`](../../13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)). Si el trabajo alcanza a otros módulos se descompone en **una fase por módulo** y el resto se difiere por escrito, nunca en una «fase transversal», que borra la trazabilidad.

**Excepción** — la infraestructura compartida que toda fase puede tocar: rutas globales, registro de servicios o bindings, mapas y catálogos centrales del proyecto, y layouts globales (condición). Solo con el cambio mínimo que el módulo de la fase necesita, y sin arrastrar funcionalidad de otro módulo (límite). Cualquier archivo ajeno fuera de esa lista pausa y lo decide el usuario (autoriza).

```
INCORRECTO: fase del módulo A arranca tocando 20 archivos de B, C y D "porque el
            refactor es transversal" → se pierde la trazabilidad por módulo
CORRECTO:   la fase A toca solo archivos de A; lo necesario en B, C y D se agenda
            como fases propias o se difiere en §Fuera-de-scope
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A — **14** y **15**: no declara dependencia; sus citas son referencia. La segunda exigencia que traía —*"y a una sola HU"*— ya vive en [`F12`](F12-relacion-y-nomenclatura-de-fases.md), punto 1 y aquí se enlaza en vez de repetirse ([`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)); las excepciones de infraestructura, que no decían quién autoriza, quedaron completas.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

**Vuelta a sellar el 2026-08-22 (pendiente 19):** cambió solo la cita a `02·F12`, que ya no tiene sub-identificadores de regla: los `F12.N` son puntos del anexo de nomenclatura. La exigencia no cambió.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
