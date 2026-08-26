# B-EP-005-HU-008-renombrar-deja-el-resumen-coherente

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada exigencia |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: el [pendiente 35](../../../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md). `historico.py --renombrar` arrastraba el resumen de la sesión a su nombre nuevo pero dejaba adentro el enlace apuntando al viejo, así que nombrar una sesión —lo que el propio enganche pide— dejaba el repositorio con un enlace roto.

**Estado:** estación 8 de las once, en la [v21.3.0](../../../../../CHANGELOG.md). Veredicto **Cumple**, 22 pruebas del repositorio en verde. **Detenida** en una ampliación de plan ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)): cerrar el pendiente dejó enlaces rotos en cuatro archivos que el plan no declara.
