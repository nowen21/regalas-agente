> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC22 · Escribe en su propio documento lo que cada sesión dejó

Cada sesión deja su resumen en un documento aparte de la transcripción, escrito con el modelo del estándar y llenado **en el momento en que aparece cada hallazgo**, no al cerrar. Cada hallazgo dice qué pasó y por qué importa, y enlaza su pendiente; si quedó resuelto y por dónde se retoma se calculan siguiendo ese enlace. Con un análisis prendido, lo que aparece no va al resumen: se reporta en la conversación y se resuelve en ese análisis.

```
INCORRECTO: la sesión produjo cinco aprendizajes y nueve pendientes, y para
            encontrarlos hay que releer la conversación entera
CORRECTO:   su resumen los lista, cada uno con su pendiente enlazado, y el
            programa dice cuáles siguen abiertos y por dónde se retoman
```

**Aplica a:** escribir-documento

**Autoriza escribir:** `historico-chat/*.md`, `historico-chat/resumenes/**`

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v52.2.0**, el **2026-10-03**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia; el modelo que usa es una plantilla, no otra regla · **16**: no tiene excepción. Fila 6: `DOC22` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, que el resumen exista y se escriba mientras pasa; qué filas lleva cada hallazgo lo dice el modelo. Cambió en `EP-023·HU-003`, fase `A`: el hallazgo pasa a dos campos y el enlace a su pendiente (análisis 1 del pendiente 103, conclusiones 14, 34 y 35). Fila 17: se releyó el capítulo entero; [`DOC1`](DOC1-persiste-el-trabajo-de-cada-unidad-completada.md) persiste el trabajo de una **unidad cerrada** y esto persiste lo que dejó una **sesión**, que puede no cerrar ninguna. [`DOC5`](DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) registra la señal, que es uno de los sitios a donde va a parar un hallazgo; esta dice que el hallazgo se escriba, aquella qué hacer con el que no se recupera del código.

**Cambió el 2026-10-03** en `EP-023·HU-007`, fase `C` (análisis 13 del pendiente 103, acuerdo 6): con un análisis prendido, lo que aparece va a la conversación. Fila 9: sigue siendo una exigencia, dónde queda lo que la sesión deja. Fila 10: el cuerpo cabe.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
