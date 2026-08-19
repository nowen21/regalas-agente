> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC13 · Registra cada módulo nuevo en el catálogo de módulos

Un módulo nuevo —dominio funcional propio, con su prefijo de rutas o su especificación separada— se registra en el catálogo de módulos del proyecto **antes de cerrar** la unidad que lo creó, con el contenido que pide [`plantillas/catalogo-modulos.md`](../../../plantillas/catalogo-modulos.md). No cuentan como módulo nuevo una fase de uno existente, un arreglo interno ni un componente hijo. Sin el catálogo, la próxima sesión planifica creyendo que el sistema es solo lo que alcanzó a leer.

```
INCORRECTO: se crea un módulo · las sesiones siguientes asumen que el proyecto
            "solo tiene X e Y" porque el nuevo no está en el catálogo
CORRECTO:   al cerrar la unidad que lo creó, su entrada queda en el catálogo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción; lo que no cuenta como módulo nuevo delimita el alcance, no exime a nadie. Fila 10: el contenido mínimo de cada entrada pasó a la plantilla.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
