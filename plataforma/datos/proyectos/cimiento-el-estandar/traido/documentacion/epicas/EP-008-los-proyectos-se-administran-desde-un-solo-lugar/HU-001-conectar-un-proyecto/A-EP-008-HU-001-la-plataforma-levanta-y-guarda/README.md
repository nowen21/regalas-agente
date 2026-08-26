# A-EP-008-HU-001-la-plataforma-levanta-y-guarda

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y con qué decisiones |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se va a comprobar |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se corrió de verdad y qué salió |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó, qué no, y qué deuda deja |
| [estado-fase.md](estado-fase.md) | En qué estación va |
| [evidencias/](evidencias/) | Las salidas de las corridas, tal como salieron |

**Qué construye.** La base de la plataforma: levantar, guardar en texto, y reconstruir el índice desde ahí.

**Qué quedó.** La plataforma corre en la máquina sin salir a la red, guarda en archivos de texto y los vuelve a leer después de apagarla. El índice se puede borrar entero y rehacer sin perder nada. Todavía no conecta proyectos: eso es la fase B.

**Estado:** cerrada, en el commit `26b2222`.
