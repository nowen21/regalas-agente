# D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y con qué decisiones |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se va a comprobar |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se corrió de verdad y qué salió |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó, qué no, y qué deuda deja |
| [estado-fase.md](estado-fase.md) | En qué estación va |
| [evidencias/](evidencias/) | Las salidas de las corridas, tal como salieron |

**Qué construye.** El registro de auditoría: que ninguna acción cambie algo sin dejar constancia, y que la constancia quede antes del cambio.

**Por qué va antes que conectar un proyecto.** Lo dice el orden aprobado de la versión 1: registrar desde el primer día evita tener un tramo sin historia.

**Qué la detenía.** Dos dudas, cerradas el 2026-08-25 mirando el código: el enmascarador de claves se importa de `validadores/`, y la sesión se enlaza por el identificador que el histórico ya escribe. Ninguna necesitó decisión del usuario.

**Qué quedó.** La plataforma ya no puede cambiar nada sin dejar constancia: se registra antes de ejecutar, y si el registro no se puede escribir, la acción no ocurre. Lo registrado no se edita ni se borra, el intento también queda, y ninguna clave entra.

**Estado:** cerrada, en el commit `5231022`.
