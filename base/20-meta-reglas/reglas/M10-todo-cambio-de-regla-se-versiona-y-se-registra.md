> Regla del capítulo [`20 · Meta-reglas`](../base.md).

## M10 · Todo cambio de regla se versiona y se registra

Todo cambio del estándar o de la configuración de un proyecto sube **en el mismo movimiento** su versión, la del estándar o la del proyecto, y deja registro de quién, cuándo, antes, después y por qué. Ese registro vive en la base de datos del agente, o en `CHANGELOG.md` y `VERSION` si aún no guarda el estándar.

```
INCORRECTO: se cambia un ajuste de un proyecto y el valor viejo se pierde, sin
            versión ni registro
CORRECTO:   el ajuste nuevo sube la versión de ese proyecto y deja quién lo
            cambió, cuándo, el valor de antes, el de después y por qué
```

**Aplica a:** cambiar-estandar

**Autoriza escribir:** `CHANGELOG.md`, `VERSION`

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v56.0.0**, el **2026-10-06**. La vez anterior fue contra v48.0.0, el 2026-10-02.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** **N/A:** fila **14**, no declara dependencia `extiende`, `depende de` ni `deroga`; sus citas son referencia, que [`M5`](M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. Fila **15**, va con la 14. Fila **16**, no tiene excepción.

**Lo que cambió en v56.0.0.** La regla cubre también la configuración de cada proyecto, con su versión propia, y pone el registro en la base de datos del agente. Sale del [análisis 1 del pendiente 132](../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 1, 12, 13 y 14, por [EP-001·HU-041](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar/HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md). **Fila 5:** dice «base de datos del agente», sin nombrar la plataforma ni el motor. **Fila 8:** el título y el ancla se conservan porque los citan otras reglas y el checklist ([`M11`](M11-las-reglas-no-se-borran-se-derogan.md)). **Fila 9:** una sola exigencia, que todo cambio deje versión y registro; dónde vive el registro es el lugar, no otra exigencia. **Fila 10:** cabe en tres líneas.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
