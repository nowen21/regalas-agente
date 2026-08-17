# A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Construcción: acá no hay nada que retro-documentar.** Los validadores cuentan fallas y avisos del total, y ninguno agrupa por regla. [`metricas/`](../../../../../metricas/README.md) mide señales del proceso, no hallazgos.

**La parte delicada es el CA-02:** un registro de hallazgos puede terminar guardando el contenido de lo revisado. Se guarda el identificador de la regla y el número, nunca el texto.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md` — la fila de HU-009 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Dos dudas bloquean casi toda la fase, incluida si va después de la corrida completa de HU-008.
