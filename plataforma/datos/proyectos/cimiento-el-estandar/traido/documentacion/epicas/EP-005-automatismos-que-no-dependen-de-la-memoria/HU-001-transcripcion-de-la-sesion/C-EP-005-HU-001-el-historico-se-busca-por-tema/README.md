# C-EP-005-HU-001-el-historico-se-busca-por-tema

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se hizo, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), anotado el 2026-08-14: «una sesión trata varios temas y por el título no se encuentran»

**El histórico ya se puede buscar por tema.** Una sesión trata varios asuntos y su nombre solo dice uno; con 59 resúmenes, encontrar dónde se decidió algo era abrirlos uno por uno. Los temas ya estaban escritos en los hallazgos de cada resumen, así que se recogen: **345 hallazgos en un archivo**, cada uno enlazado a donde vive. Nace [`validadores/temas.py`](../../../../../validadores/temas.py), el subcomando `validar.py temas` y siete casos de prueba.

**Estado:** cerrada el 2026-08-22 (v31.4.0). Veredicto **Cumple**.
