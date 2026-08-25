# H-EP-008-HU-004-un-proyecto-conectado-se-administra

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y con qué decisiones |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se va a comprobar |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se corrió de verdad y qué salió |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó, qué no, y qué deuda deja |
| [estado-fase.md](estado-fase.md) | En qué estación va |
| [evidencias/](evidencias/) | Las salidas de las corridas, tal como salieron |

**Qué construye.** Que equivocarse al conectar un proyecto deje de ser permanente: desconectar sin borrar, renombrar sin mover, y corregir la versión declarada. Con confirmación en los cuatro.

**De dónde sale.** De la fase B: al ver la primera pantalla funcionando se vio que conectar no tenía reversa, y que la especificación ya decidía cómo se comporta desconectar sin que ninguna funcionalidad lo pidiera.

**Qué la detenía.** Una duda, cerrada el 2026-08-25: un proyecto desconectado **libera su ruta**, y volver a conectar esa carpeta **reactiva el proyecto**, con su documentación. No se crea uno nuevo, porque eso dejaría la documentación del anterior sin dueño.

**Qué quedó.** Equivocarse al conectar dejó de ser permanente: desconectar deja la documentación, renombrar deja la carpeta, y corregir la versión la vuelve a comprobar. Los cambios preguntan antes, diciendo **qué va a pasar y qué no**.

**Estado:** cerrada, en el commit `5bf4ebb`.
