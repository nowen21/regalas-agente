> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC26 · Cada análisis deja su pendiente en la versión siguiente

Desde el segundo análisis de un pendiente, aprobarlo pasa el pendiente a su versión siguiente en su mismo archivo: «De dónde sale» suma el hallazgo que abrió ese análisis, y «El problema» y «Por qué importa» recogen lo que el análisis precisó (complementa [`13·DOC24`](DOC24-cierra-el-analisis-en-su-mismo-archivo.md)).

```
INCORRECTO: el análisis 2 se aprueba y el pendiente sigue diciendo lo que
            decía antes del hallazgo que lo abrió
CORRECTO:   al aprobarse el análisis 2, el pendiente pasa a su versión
            siguiente con ese hallazgo en «De dónde sale»
```

**Aplica a:** escribir-documento

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v53.1.0**, el **2026-10-03**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A, **16**: no tiene excepción. Fila 4: va en el `13`, porque trata de un documento, el pendiente, y de cuándo se reescribe. Fila 6: `DOC26` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, pasar el pendiente a su versión siguiente al aprobar el análisis. Fila 17: complementa `DOC24`, que dice que el análisis aprobado no se reescribe; lo que se reescribe es el pendiente.

**Validable:** `proyectos/cimiento/core/enganches/analisis_en_curso.py` no deja aprobar un análisis, desde el segundo, cuyo hallazgo falta en «De dónde sale» del pendiente.

Nace en `EP-023`, del análisis 14 del pendiente 103 (acuerdos 3 y 11). Pone en el estándar lo que acordó el análisis 11 (acuerdo 5): la plantilla del análisis lo citaba, y ese análisis solo existe en este repositorio.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
