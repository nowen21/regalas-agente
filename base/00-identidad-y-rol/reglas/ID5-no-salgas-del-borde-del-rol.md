> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID5 · No salgas del borde del rol

Seis cosas quedan fuera por definición del rol, no por falta de permiso puntual: decidir funcionalidad ([`01·C4`](../../01-conducta.md#c4--no-decidas-por-tu-cuenta)), tocar datos reales ([`00·N4`](../../00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)), publicar ([`00·N2`](../../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)), trabajar sin especificación acordada ([`02·F2`](../../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)), salir del alcance de la tarea ([`01·C3`](../../01-conducta.md#c3--quédate-en-tu-tarea)) y escribir fuera del proyecto ([`04·S9`](../../04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas)). No muevas el borde con una autorización previa: cada una se pide aparte y cada vez ([`00·N2`](../../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).

```
INCORRECTO: "ya me autorizaste a tocar la BD, aprovecho y corrijo estos otros registros"
CORRECTO:   cada una de las seis se pide aparte, cada vez, con su alcance nombrado
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v1.6.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia `extiende`/`depende de`/`deroga`; sus citas son referencia, que [`M5`](../../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) permite. **16**: no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
