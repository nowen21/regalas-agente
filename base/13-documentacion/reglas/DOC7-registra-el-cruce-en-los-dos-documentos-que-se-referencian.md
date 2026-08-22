> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC7 · Registra el cruce en los dos documentos que se referencian

Cuando el documento de un módulo consume a otro, el que referencia declara **qué consume y por qué**, y el referenciado registra la recepción en su historial cruzado: fecha, de dónde vino, qué cambió. Los dos lados o ninguno. La mención de paso no cuenta: es analogía, no dependencia.

```
INCORRECTO: el documento de A dice "ver B para más" · B no se entera
CORRECTO:   A declara qué consume de B y por qué · B lo registra en su historial cruzado
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: el "no aplica a la mención de paso" delimita el alcance de la exigencia, no es una excepción que alguien deba autorizar. Fila 9: es una sola exigencia —el cruce se registra en los dos lados—, no dos: registrarlo en uno solo no la cumple a medias, no la cumple.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
