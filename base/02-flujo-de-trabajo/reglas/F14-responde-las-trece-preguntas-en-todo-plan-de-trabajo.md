> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F14 · Responde las trece preguntas en todo plan de trabajo

Un plan de trabajo responde las **trece preguntas** del capítulo antes de que se escriba una línea de código. La que no aplique al alcance se deja con su encabezado y un «No aplica porque ...», no se omite; las trece están en [`base.md`](../base.md) (extiende [`02·F4`](F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) · deroga [`02·F4.1`](F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)).

```
INCORRECTO: plan que dice "creo el CRUD X" y omite dónde queda accesible al usuario
            → se implementa el CRUD y el usuario tiene que ir a la URL a mano
CORRECTO:   plan que responde las trece → nadie ejecuta a medias, porque hay que
            declarar cada respuesta antes de aprobar
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Toma el contenido de [`F4.1`](F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), cuyo ID decimal no admitía [`M4`](../../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md); la enumeración de las trece pasó a [`base.md`](../base.md), que es lo que le cerraba la fila 10.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
