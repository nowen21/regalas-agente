# B-EP-001-HU-007-primero-que-el-proceso-sirva

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba el `CA-05` |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó y con qué resultado |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | El cierre: qué quedó hecho, probado y versionado |

**De dónde nace.** Del [pendiente 16](../../../../../pendientes/hecho/primero-que-el-proceso-sirva.md): el backlog de automatizaciones sabía decidir **si se puede** automatizar una regla, pero no **si conviene ya**. Una regla mal escrita se automatiza perfectamente, y el resultado es que falla sola, en cada commit, sin que nadie la haya vuelto a leer.

**Qué entrega.** El `CA-05` de [HU-007](../HU-007-regla-de-las-reglas.md) y la meta-regla [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md): antes de construir el validador de una regla se responden por escrito tres preguntas — ¿se cumple hoy a mano?, ¿cuántas veces se incumplió y por qué?, ¿cuántas falsas alarmas daría? Si se incumplió por mal escrita, primero se corrige la regla; si lo único que falla es acordarse, se automatiza ya.

**Cómo llegó.** La sesión 4 del 2026-08-20 escribió la regla y el criterio, y quedó cortada sin los documentos de la fase. La sesión del 2026-08-21 los escribió declarando lo hecho como línea base — el detalle está en el §0 del plan de trabajo.

**Estado:** cerrada el 2026-08-21 — **Cumple**, con los tres casos del `CA-05` aprobados y la versión 28.1.0. El usuario confirmó la opción 1 del pendiente (CA nuevo en HU-007) y aprobó plan y pruebas; falta solo el commit, que se autoriza aparte.
