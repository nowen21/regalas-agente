> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F27 · Cada punto dice de qué punto del anterior sale

Cada punto de un documento de la cadena lleva «Sale de» con el punto del documento anterior: el pendiente, su hallazgo; la conclusión del análisis, su turno; el criterio de la HU, su punto de «Lo que se tiene que hacer». Lo que no tiene origen no entra (extiende [`02·F18`](F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).

**Excepción**: las épicas que no nacieron de un análisis no se reabren para agregarles «Sale de» (condición). No cubre los documentos nuevos de esas épicas, que la cumplen desde que nacen (límite). Lo acepta el usuario al adoptar la versión que la trae (autoriza).

```
INCORRECTO: la HU trae un CA-04 sin «Sale de», porque «se veía necesario»
CORRECTO:   el CA-04 dice «Sale de: análisis 6, punto 2», y ese punto existe
            en «Lo que se tiene que hacer» del análisis 6
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
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.**

**Fila 2 · se buscó por concepto y se leyó el capítulo entero.** [`F18`](F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) pide que cada tarea del plan cuelgue de un criterio, y no dice nada de los eslabones de arriba. [`F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) pide recorrer la cadena, no que cada punto cite su origen.

**Fila 9 · una sola exigencia.** Lo que se exige es citar el origen. Que lo que no lo tiene no entre es la consecuencia de no poder citarlo, no otra exigencia.

**Fila 16 · la excepción aplica** [`20·M10`](../../20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo que ya está cerrado.

**Fila 18 · validable, y así queda registrada** en [validadores/reglas-validables.md](../../../validadores/reglas-validables.md): la comprueba `validar.py origen`.

Del [análisis 1](../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (conclusiones 6, 28 y 39) del pendiente «Lo que se construye se aparta de lo aprobado», fase `A` de la HU-002 de EP-023.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
