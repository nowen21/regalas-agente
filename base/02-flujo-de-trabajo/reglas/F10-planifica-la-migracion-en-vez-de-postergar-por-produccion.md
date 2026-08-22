> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F10 · Planifica la migración en vez de postergar por producción

Cuando el cambio toca algo que está o puede estar en producción, el plan asume **«probablemente sí lo está»** y declara la estrategia de migración incremental que corresponde; no se posterga la fase preguntando si está en producción. La casuística: [`base.md`](../base.md) (extiende [`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 12).

**Excepción** — el cambio destructivo o con riesgo de pérdida (drop con datos, cambio de tipo o de restricción) se **avisa antes** con su riesgo concreto (condición). El aviso no reemplaza la migración reversible ([`03·D2`](../../03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)) ni habilita operar la base directamente ([`00·N4`](../../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)) (límite). Aplicarlo lo autoriza el usuario (autoriza).

```
INCORRECTO: "antes de arrancar la fase necesito confirmar si X está en producción"
            → fase bloqueada esperando información que se puede asumir
CORRECTO:   el plan asume "probablemente está en prod" y declara la estrategia
            (aditiva · rename reversible · drop con aviso · tipo con aviso)
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.** No modera [`00·N4`](../../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada): una regla de capa 2 no puede tocar una `[BLINDADA]` ([`M7`](../../20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)), y por eso el límite de la excepción lo dice explícito.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
