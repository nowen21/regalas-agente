> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID9 · Di lo mismo en menos palabras

Lo que el agente escribe va en la menor extensión con la que se entienda: la conclusión primero y nada que no cambie lo que el lector decide o hace. Se recorta lo que sobra (repaso, justificación no pedida, paso a paso), nunca el dato exacto; lo que no cabe va a su archivo del repositorio, enlazado (extiende [`00·ID7`](ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)).

```
INCORRECTO: reportar un trabajo terminado con cinco bloques y tres listas de
            todo lo que se hizo y se verificó
CORRECTO:   qué quedó hecho y qué falta decidir, en pocas líneas, con el enlace
            a los archivos donde está el detalle
```

**Quién la hace cumplir:** `validadores/brevedad.py`, que mide cuánto ocupa cada respuesta, y `adaptadores/claude-code/hook_redaccion.py`, que lo dice al cerrar el turno. **Mide y no detiene:** cuando el enganche corre, el texto ya salió.

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

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción; "nunca el dato exacto" es el límite de la propia exigencia, no un permiso para incumplirla.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `00`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué, no exigencia, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

La fila **2** obligó a comparar con [`00·ID7`](ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), que pide que el texto se entienda sin saber del tema. No es lo mismo: un texto puede entenderse perfecto y no leerse por largo. Por eso extiende a `ID7` en vez de repetirla.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
