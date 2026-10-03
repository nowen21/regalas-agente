> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC25 · Reescribe el análisis principal con su lista de cambios

El análisis principal del proyecto o del módulo se forma con lo que aportan los análisis individuales: cada uno que se aprueba se anota en él, aunque no cambie el sistema, y lo que suma pasa tal cual a su redacción, con la fecha, el resultado y el enlace en su lista de análisis (deroga [`13·DOC8`](DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md)).

```
INCORRECTO: un análisis solo confirmó que «la clase con suma» estaba bien
            entendida, y no se anotó porque no cambió nada
CORRECTO:   su frase pasa tal cual al principal, y la lista de análisis
            dice la fecha, «Ratifica» y el enlace
```

**Aplica a:** escribir-documento

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v44.0.0**, el **2026-10-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A, **16**: no tiene excepción. Fila 6: `DOC25` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, que todo análisis aprobado quede anotado en el principal con lo que aportó; cómo cierra el análisis individual vive en [`DOC24`](DOC24-cierra-el-analisis-en-su-mismo-archivo.md). Fila 14: deroga `DOC8` junto con `DOC24`.

Nace en `EP-023·HU-001`, fase `A`, del análisis 1 del pendiente 103 (conclusión 32) y del análisis 5. Cambia en la fase `D`, por el análisis 9 (puntos 1 a 5 de «Lo acordado»).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
