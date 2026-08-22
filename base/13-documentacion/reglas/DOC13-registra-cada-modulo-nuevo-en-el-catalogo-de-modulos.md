> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC13 · Registra cada módulo nuevo en el catálogo de módulos

Un módulo nuevo —dominio funcional propio, con su prefijo de rutas o su especificación separada— se registra en el catálogo de módulos **antes de cerrar** la unidad que lo creó, con lo que pide [`plantillas/catalogo-modulos.md`](../../../plantillas/catalogo-modulos.md). No cuentan la fase de un módulo que ya existe, el arreglo interno ni el componente hijo.

```
INCORRECTO: se crea un módulo · las sesiones siguientes asumen que el proyecto
            "solo tiene X e Y" porque el nuevo no está en el catálogo
CORRECTO:   al cerrar la unidad que lo creó, su entrada queda en el catálogo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción; lo que no cuenta como módulo nuevo delimita el alcance, no exime a nadie. Fila 10: el contenido mínimo de cada entrada pasó a la plantilla.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
