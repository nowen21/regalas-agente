> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC17 · Mantén un `README.md` en cada nivel del árbol de trabajo

Ninguna carpeta del árbol de épicas, HU y fases ([`02·F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13) queda muda: cada una tiene un `README.md` que lista **su contenido inmediato** —lo que cuelga directo de ella, no el árbol entero— con una frase de qué es cada cosa. Se actualiza en el mismo cambio que crea, mueve o cierra algo; no es la foto de una fecha.

```
INCORRECTO: la carpeta de la épica tiene ocho HU dentro y ningún índice ·
            hay que abrirlas una por una para saber qué hay
CORRECTO:   su README lista las ocho, cada una con su título y su estado
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Fila 6: `DOC17` es el siguiente consecutivo libre. La exigencia no es nueva —vivía dentro de [`DOC15`](DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), y [`DOC16`](DOC16-crea-la-epica-desde-la-plantilla-central.md) ya la citaba como si fuera regla propia—; lo nuevo es que ahora se puede citar por su ID.

**Vuelta a sellar el 2026-08-22 (pendiente 19):** cambió solo la cita a `02·F12`, que ya no tiene sub-identificadores de regla: los `F12.N` son puntos del anexo de nomenclatura. La exigencia no cambió.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
