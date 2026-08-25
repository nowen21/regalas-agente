# C-EP-008-HU-002-la-ruta-perdida-se-avisa

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y con qué decisiones |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se va a comprobar |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se corrió de verdad y qué salió |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó, qué no, y qué deuda deja |
| [estado-fase.md](estado-fase.md) | En qué estación va |
| [evidencias/](evidencias/) | Las salidas de las corridas, tal como salieron |

**Qué construye.** Que el usuario no descubra que movió la carpeta de un proyecto el día que necesita trabajar en él: el aviso con la ruta que se buscó, y poder corregirla.

**Lo que hay que saber antes de leer el plan.** Media fase ya estaba construida: `ruta_viva` y el aviso salieron de la fase B sin que nadie estuviera pensando en esta historia. Lo que falta de verdad es **corregir la ruta**, que no existe, y la medición de `RNF-02`.

**Qué quedó.** Cuando la carpeta de un proyecto deja de estar donde estaba, la plataforma lo dice **y dice dónde la buscó**. Desde ahí se corrige la ruta, con confirmación y registro de dónde a dónde. Listar cincuenta proyectos tarda 0.010 s.

**Estado:** estación 9. Los siete casos de prueba en verde y el cierre escrito. Falta el visto bueno para guardar.
