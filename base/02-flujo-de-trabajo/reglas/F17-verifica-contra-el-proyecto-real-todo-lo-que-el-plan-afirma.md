> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F17 · Verifica contra el proyecto real todo lo que el plan afirma

Cada ruta, firma y dependencia que el plan nombra se comprueba antes contra el proyecto. Quedan prohibidas las marcas de incertidumbre («o donde esté», «o similar», «por confirmar»): lo que no se pueda verificar se declara pregunta abierta y espera al usuario, no se escribe como suposición (depende de [`02·F1`](F1-carga-el-contexto-antes-de-actuar.md)).

```
INCORRECTO: "el archivo de navegación de la carpeta de vistas (o donde esté)"
            → el plan admite que no verificó la ruta real
CORRECTO:   listar la carpeta → localizar el archivo → leerlo → plan dice
            "<ruta real>, sección <X>: agregar el ítem con permiso <permiso.ver>"
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

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Es la segunda de las dos exigencias que [`F4.3`](F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) tenía juntas; la primera es [`F16`](F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md).

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
