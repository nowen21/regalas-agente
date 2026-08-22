# El ciclo de vida del proyecto: sus moldes, en orden

Los documentos que **todo** desarrollo recorre, sin importar envergadura, numerados en el orden del ciclo. La envergadura ajusta la profundidad de cada uno, nunca su existencia; el que no tenga materia se llena con «No aplica porque...» y su porqué. El porqué del ciclo completo está en la [guía de entrada](../../base/guia-de-entrada.md).

| # | Molde | Estación del ciclo | Puerta |
|---|---|---|---|
| 01 | [01-planteamiento.md](01-planteamiento.md) | Entender la necesidad | Se escribe con las palabras del usuario |
| 02 | [02-inventario-funcionalidades.md](02-inventario-funcionalidades.md) | El alcance completo, ítem por ítem | 👤 **El usuario lo aprueba**: sin esto no se derivan épicas ([`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)) |
| 03 | [03-epica.md](03-epica.md) | Los grupos de valor, cada uno citando sus ítems del inventario | 👤 Alcance aprobado |
| 04 | [04-HU.md](04-HU.md) | Las unidades con criterios de aceptación | 👤 HU aprobada |
| 05 | [05-fase.md](05-fase.md) | La unidad de ejecución de una HU ([`02·F12`](../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | (sin puerta) |
| 06 | [06-especificacion-modulo.md](06-especificacion-modulo.md) | Qué hace el módulo, antes del código ([`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)) | 👤 Acordada |
| 07 | [07-plan-trabajo.md](07-plan-trabajo.md) | Qué se toca, en qué orden, cómo se revierte ([`02·F14`](../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)) | 👤 Junto con el 08 ([`02·F4`](../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| 08 | [08-plan-pruebas.md](08-plan-pruebas.md) | Con qué casos se comprueba cada criterio | 👤 Junto con el 07 |
| 09 | [09-resultado-pruebas.md](09-resultado-pruebas.md) | Qué se ejecutó y qué dio; el veredicto por criterio | Lo decide la evidencia |
| 10 | [10-estado-fase.md](10-estado-fase.md) | En qué estación va la fase; sobrevive a la compactación | (sin puerta) |
| 11 | [11-funcionalidad-implementada.md](11-funcionalidad-implementada.md) | El cierre: qué quedó hecho, probado y qué deuda declaró | (sin puerta) |

**El ciclo es un anillo, no una línea:** el cierre (11) alimenta señales y pendientes que reentran por el planteamiento (01), y el inventario (02) madura con cada ítem construido hasta convertirse en el manual del producto.

**Lo que no está acá** vive en la raíz de [`plantillas/`](../README.md): los moldes de configuración del proyecto (stack, dominio, mapeo de nombres), los de operación (checklist de despliegue, postmortem), los transversales (ADR, señales, sesión) y las fuentes de generación. La lista completa de entregables del ciclo, incluidos los que aún no tienen molde, está en [notas/entregables-del-ciclo-de-vida.md](../../notas/entregables-del-ciclo-de-vida.md).
