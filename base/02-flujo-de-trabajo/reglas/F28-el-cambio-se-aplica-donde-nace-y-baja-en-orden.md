> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F28 · El cambio se aplica donde nace y baja en orden

Si cambia la necesidad, el cambio se escribe primero en el documento donde nace, aunque sea el planteamiento, y baja en orden por la épica, la HU, la especificación y el plan. Ningún documento de abajo cambia antes que el de arriba (extiende [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).

```
INCORRECTO: el usuario cambia lo que necesita y se corrige el plan; la HU
            sigue diciendo lo de antes
CORRECTO:   se corrige la HU, después la especificación y al final el plan
```

**Aplica a:** trabajar-cadena, escribir-documento

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v42.0.0**, el **2026-10-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 2 · se buscó por concepto y se leyó el capítulo entero.** [`F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) dice el orden de la cadena al construir, no cómo la recorre un cambio. El capítulo dice que el plan aprobado no se modifica para anotarle resultados, que es otro caso.

**Fila 16 · N/A:** no tiene excepción.

**Fila 17 · sin choque.** Cómo pasa el plan a su versión siguiente cuando el cambio llega hasta él es asunto de la HU-004 de EP-023 (análisis 1, punto 18).

**Fila 18 · no validable, y así queda registrada** en [validadores/reglas-validables.md](../../../validadores/reglas-validables.md): saber dónde nació un cambio exige leer la conversación que lo pidió.

Del [análisis 1](../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (conclusión 8) del pendiente «Lo que se construye se aparta de lo aprobado», fase `A` de la HU-002 de EP-023.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
