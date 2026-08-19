> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC7 · Registra el cruce en los dos documentos que se referencian

Cuando el documento de un módulo consume a otro, el que referencia declara **qué consume y por qué**, y el referenciado registra la recepción en su historial cruzado: fecha, de dónde vino, qué cambió. Los dos lados o ninguno — si solo se escribe en uno, el conocimiento queda atrapado ahí. No aplica a la mención de paso ("algo parecido se hizo en X"): eso es analogía, no dependencia.

```
INCORRECTO: el documento de A dice "ver B para más" · B no se entera
CORRECTO:   A declara qué consume de B y por qué · B lo registra en su historial cruzado
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: el "no aplica a la mención de paso" delimita el alcance de la exigencia, no es una excepción que alguien deba autorizar. Fila 9: es una sola exigencia —el cruce se registra en los dos lados—, no dos: registrarlo en uno solo no la cumple a medias, no la cumple.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
