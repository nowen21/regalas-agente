> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID4 · Asume el ciclo completo, de entender a documentar

Asume la unidad de trabajo entera: entender el proyecto, proponer, redactar la especificación, diseñar, planificar, implementar con pruebas, verificar, revisar defectos y seguridad, documentar y mantener la memoria. No entregues media cadena esperando que alguien complete el resto.

```
INCORRECTO: implementar y devolverlo "para que alguien le ponga las pruebas y la doc"
CORRECTO:   la unidad se entrega con su especificación, su código, sus pruebas y su documentación
```

**Nadie la hace cumplir:** que el agente haya recorrido el ciclo entero se ve en lo que entregó, y cada tramo tiene su propia regla con su propio validador. El ciclo completo como exigencia única no lo cuenta ninguno.

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v1.6.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
