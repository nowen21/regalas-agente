> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F19 · Implementa literal el criterio de aceptación

La implementación hace **literal** lo que dice el CA aprobado: ni más, ni menos, ni "más seguro por si acaso" (extiende [`02·F18`](F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) · deroga [`02·F4.5`](F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md)). La redacción del CA es la especificación funcional: el agente no la interpreta libremente ni la endurece por su cuenta.

```
INCORRECTO: el CA pide un listado de clientes, y se le agrega una exportación
            a hoja de cálculo «porque todo listado la trae»
CORRECTO:   se implementa el listado que el CA dice, tal cual
```

**Aplica a:** trabajar-cadena, cambiar-codigo

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v41.0.0**, el **2026-10-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Es la primera de las dos partes que [`F4.5`](F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md) declaraba *"indivisibles"* y no lo eran: se puede implementar de menos sin haber descubierto nada. La segunda es [`F20`](F20-para-y-propon-lo-que-descubras-fuera-del-ca.md).

**El ejemplo cambió el 2026-10-02.** El anterior ponía como incorrecto revisar el permiso en el servidor cuando el CA pedía ocultar un botón, y eso lo exige [`04·S1`](../../04-seguridad.md#s1--autorización-en-cada-acción-sensible). Lo que exige la regla no cambió. Del [análisis 6](../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-6.md) (conclusión 6), fase `A` de la HU-005 de EP-023.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
