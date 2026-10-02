> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC24 · Cierra el análisis en su mismo archivo

Un análisis individual cierra al final de su mismo archivo, con sus conclusiones, sus lecciones y lo que se tiene que hacer, y desde que se aprueba no se reescribe: lo que aparezca después abre el análisis siguiente (deroga [`13·DOC8`](DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)).

```
INCORRECTO: el análisis se cierra en otro archivo con su tabla de decisiones,
            y meses después alguien le corrige una conclusión al original
CORRECTO:   las conclusiones van al final del mismo análisis; aprobado, queda
            como está, y el hallazgo nuevo abre analisis-2.md
```

**Aplica a:** escribir-documento

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v40.0.0**, el **2026-10-01**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A, **16**: no tiene excepción. Fila 6: `DOC24` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, dónde y cómo cierra un análisis individual; que el principal se reescriba es otra exigencia y vive en [`DOC25`](DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md) (análisis 5 del pendiente 103). Fila 14: deroga `DOC8` junto con `DOC25`, que cubre la otra mitad de lo que `DOC8` pedía.

Nace en `EP-023·HU-001`, fase `A`, del análisis 1 del pendiente 103 (conclusiones 4, 9 y 21) y del análisis 5.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
