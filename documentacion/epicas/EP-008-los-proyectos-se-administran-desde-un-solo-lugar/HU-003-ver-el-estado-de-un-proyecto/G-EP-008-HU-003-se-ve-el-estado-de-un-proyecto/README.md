# G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y con qué decisiones |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se va a comprobar |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se corrió de verdad y qué salió |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó, qué no, y qué deuda deja |
| [estado-fase.md](estado-fase.md) | En qué estación va |
| [evidencias/](evidencias/) | Las salidas de las corridas, tal como salieron |

**Qué construye.** Que el usuario sepa en qué va cualquiera de sus proyectos sin entrar a su carpeta: qué etapas tienen documento, qué fases están abiertas, y qué está aprobado.

**Lo que encontró medir antes de planear.** Dos problemas. Uno es un **defecto de la fase E**, ya cerrada: las etapas del ciclo viven en `cvds/`, que no se traía **y no se declaraba como no mirada**. El otro es que la estación de una fase se escribe de doce formas distintas, y cinco no se dejan leer.

**Qué se decidió.** `cvds/` entra a lo que se trae. Y lo que no se pueda leer se dice, en vez de suponerlo.

**Qué quedó.** La plataforma dice en qué va cada proyecto sin abrir su carpeta. De este repositorio: **7 de 7 etapas con documento, 41 de 127 fases todavía abiertas, 228 de 994 documentos aprobados**, y cinco fases cuya estación no se deja leer, nombradas.

**Estado:** estación 9. Los nueve casos de prueba en verde y el cierre escrito. Falta el visto bueno para guardar.
