> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC21 · Escribe `N/A` en la sección del modelo que no aplica

La sección de un modelo que no le aplica al caso se escribe `N/A`: no se deja con su marca ni se borra (depende de [`DOC19`](DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)). Dejarla con la marca la vuelve un hueco sin llenar; borrarla hace creer que el modelo nunca la pidió, y quien revise no sabrá si se leyó y no aplicaba o si nadie la miró.

```
INCORRECTO: la especificación no tiene interfaz, así que se borra la sección
            de interfaz · el que revisa no sabe si no aplicaba o si se olvidó
CORRECTO:   la sección se queda con su título y adentro dice N/A
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v13.0.0**, el **2026-08-14**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Fila 14: declara `depende de DOC19`, porque lo que se evita es dejar la marca puesta. Fila 15: no hay ciclo. Fila 17: se releyó el capítulo entero y no choca con ninguna vigente; el `N/A` con motivo que pide el [checklist del estándar](../../20-meta-reglas/checklist.md) es de ese instrumento y no de los modelos, así que son cosas distintas.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
