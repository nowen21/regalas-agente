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

## Los entregables del expediente (12 a 22)

Los moldes 01 a 11 son el camino que **cada unidad de trabajo** recorre; estos son los entregables del **proyecto entero**, que se alimentan en su etapa y maduran hasta la entrega. El número dice el archivo, no el momento: la columna del medio dice a qué estación acompaña cada uno.

| # | Molde | Acompaña a | Qué entrega |
|---|---|---|---|
| 12 | [12-estudio-factibilidad.md](12-estudio-factibilidad.md) | 01, antes de comprometer trabajo | Si conviene hacerlo y por qué camino, con las alternativas descartadas |
| 13 | [13-acta-de-constitucion-y-plan-de-proyecto.md](13-acta-de-constitucion-y-plan-de-proyecto.md) | 01 y 02, al aprobarse | La autorización formal, los hitos y los riesgos del proyecto |
| 14 | [14-modelo-de-datos.md](14-modelo-de-datos.md) | 06, y madura con cada fase | Entidades, relaciones y el diccionario de cada campo |
| 15 | [15-diseno-de-interfaz.md](15-diseno-de-interfaz.md) | 06, y madura con cada fase | Navegación, inventario de pantallas y los flujos que importan |
| 16 | [16-documentacion-de-api.md](16-documentacion-de-api.md) | 06, y madura con cada fase | El contrato de la API para quien integra sin leer el código |
| 17 | [17-manual-de-instalacion.md](17-manual-de-instalacion.md) | Desde la primera fase | Levantar el sistema desde cero, literal y verificable |
| 18 | [18-manual-tecnico-y-de-operacion.md](18-manual-tecnico-y-de-operacion.md) | La entrega y la operación | Respaldos probados, monitoreo, y qué hacer cuando falla |
| 19 | [19-notas-de-version.md](19-notas-de-version.md) | Cada entrega | Qué trae cada versión, dicho para quien usa |
| 20 | [20-acta-de-entrega.md](20-acta-de-entrega.md) | Cada entrega | Qué se entregó, con qué evidencia, y la aceptación |
| 21 | [21-bitacora-de-operacion.md](21-bitacora-de-operacion.md) | La operación | Lo que le pasa al sistema en producción, en orden |
| 22 | [22-plan-de-mantenimiento.md](22-plan-de-mantenimiento.md) | Después de entregar | Las rutinas que lo sostienen y el fin de vida |

**Dos entregables no tienen molde a propósito.** El **manual de usuario** es el inventario (02) madurado: cada ítem construido gana ahí su descripción de uso, y ese documento *es* el manual. Y el **SRS consolidado**, la **matriz de trazabilidad de proyecto**, el **registro de defectos consolidado** y el **documento de arquitectura** son **vistas que se generan** desde lo que ya está escrito (épicas, HU, resultados de fase, ADR): escribirlas a mano sería duplicar lo que diverge solo. El generador es trabajo dimensionado en la [nota de entregables](../../notas/entregables-del-ciclo-de-vida.md).

**Lo que no está acá** vive en la raíz de [`plantillas/`](../README.md): los moldes de configuración del proyecto (stack, dominio, mapeo de nombres), los de operación (checklist de despliegue, postmortem), los transversales (ADR, señales, sesión) y las fuentes de generación. La lista completa de entregables del ciclo, incluidos los que aún no tienen molde, está en [notas/entregables-del-ciclo-de-vida.md](../../notas/entregables-del-ciclo-de-vida.md).
