# B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se hizo, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: el punto 8 del [pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), donde quedó preguntado si el mapa del sitio se comprueba o se actualiza a mano

**El mapa del sitio ya no envejece en silencio.** Se decidió comprobarlo con un programa en vez de actualizarlo a mano, y la primera corrida encontró cuatro carpetas que existían sin estar en el mapa y una que el mapa nombraba y ya no existe: decía doce y son dieciséis. Nace [`validadores/sitio.py`](../../../../../validadores/sitio.py), el subcomando `validar.py sitio` y siete casos de prueba.

**Estado:** cerrada el 2026-08-22 (v31.2.0). Veredicto **Cumple**.
