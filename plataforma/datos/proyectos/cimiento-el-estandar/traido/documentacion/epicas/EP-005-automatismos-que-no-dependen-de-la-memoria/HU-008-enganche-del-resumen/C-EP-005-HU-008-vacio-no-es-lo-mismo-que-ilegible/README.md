# C-EP-005-HU-008-vacio-no-es-lo-mismo-que-ilegible

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba cada exigencia |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: **el propio enganche, diciendo algo que parecía falso.** Avisó *«el resumen de esta sesión sigue vacío»* sobre un archivo con quince hallazgos escritos. No se equivocaba al mirar: estaban como `### 1 ·` y el molde pide `### H-1 ·`.

**Tres resúmenes, 29 hallazgos que el programa no veía**, y los tres de la misma jornada — una forma que se adoptó en una sesión y se copió a la siguiente porque nada la contradijo.

**El defecto se tapaba a sí mismo por tres caminos:** el resumen se contaba como vacío, la comprobación del cierre nunca corría —necesita encontrar un hallazgo antes de mirar— y el aviso se marca como ya dado, así que se ve una vez y calla.

**Estado:** estación 8 de las once. Veredicto **Cumple**, 9 de 9 casos. Sin cambio de versión: no se toca `base/` ni `plantillas/`.
