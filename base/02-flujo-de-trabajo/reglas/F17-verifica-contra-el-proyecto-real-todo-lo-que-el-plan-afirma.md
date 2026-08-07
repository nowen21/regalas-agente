> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F17 · Verifica contra el proyecto real todo lo que el plan afirma

Cada ruta, firma y dependencia que el plan nombra se comprueba antes contra el proyecto (depende de [`02·F1`](F1-carga-el-contexto-antes-de-actuar.md) · deroga [`02·F4.3`](F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)). Quedan prohibidas las marcas de incertidumbre —`(o donde esté)`, `(o similar)`, `(por confirmar)`, `TBD`, `?`—: lo que no se pueda verificar **no se escribe como suposición**, se declara pregunta abierta y espera la decisión del usuario. Cómo se construye la línea base, la matriz de dependencias del refactor y la proporcionalidad del análisis: [`base.md`](../base.md).

```
INCORRECTO: "el archivo de navegación de la carpeta de vistas (o donde esté)"
            → el plan admite que no verificó la ruta real
CORRECTO:   listar la carpeta → localizar el archivo → leerlo → plan dice
            "<ruta real>, sección <X>: agregar el ítem con permiso <permiso.ver>"
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.1.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Es la segunda de las dos exigencias que `F4.3` tenía juntas; la primera es [`F16`](F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
