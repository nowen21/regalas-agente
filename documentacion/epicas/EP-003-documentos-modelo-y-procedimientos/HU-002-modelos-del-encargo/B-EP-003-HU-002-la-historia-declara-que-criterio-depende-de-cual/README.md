# B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se hizo, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: el punto 8 del [pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), abierto desde el 2026-08-07

**Una historia ya puede decir qué criterio depende de cuál.** La tabla de fases decía qué CA cubre cada fase, pero no si un CA no se puede comprobar mientras otro no esté cumplido; sin eso, dos fases se ordenan al revés y se descubre al probar. Se resolvió con una columna, no con una sección: la historia sin dependencias la deja vacía y no paga nada.

**Estado:** cerrada el 2026-08-22 (v31.1.0). Veredicto **Cumple**.
