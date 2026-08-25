# Implementación: ¿qué se toca, y en qué orden?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito en qué versiones se parte la construcción de Cimiento, qué unidad de trabajo cubre cada funcionalidad, en qué orden se hacen y cómo se deshace lo que salga mal. El detalle de cada unidad vive en su propia fase; acá queda el gobierno de todas.

> **Escrito desde la propuesta**, igual que el resto de [cvds/](../README.md). Sale de los doce módulos del [diseño](../diseno/README.md) y de las 32 fichas del [inventario](../analisis-requisitos/inventario-funcionalidades.md), aprobados el 2026-08-24.

**Estado: APROBADO** (2026-08-25, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Doce módulos con sus límites, y doce decisiones de arquitectura | Diseño | Sí, el 2026-08-24 |
| El inventario con 32 fichas, cada una con lo que la termina | Análisis | Sí, el 2026-08-24 |
| Los trece paquetes de trabajo y las 173 jornadas estimadas | Planificación | Sí, el 2026-08-24 |
| Las doce especificaciones de módulo | Diseño | **No: son la puerta para abrir código** (`02·F2`) |

## 2. Las versiones, y qué se puede hacer con cada una

> **Una versión no es un corte del trabajo: es algo que ya sirve.** Si al terminarla no se puede hacer nada nuevo, no era una versión, era una pausa. El orden elegido entrega valor al usuario desde la primera, y deja al agente trabajando como hoy hasta la tercera.

| Versión | Qué entra | Qué se puede hacer al terminarla |
|---|---|---|
| **1 · Ver lo que hay** | F-001, F-002, F-003, F-018, F-027, F-028, F-035 | Conectar los proyectos y **poder deshacerlo**, traer lo que ya tienen escrito, ver cómo va cada uno sin entrar, y que todo lo que se haga quede registrado |
| **2 · Entregar** | F-014, F-025, F-026, F-033, F-034 | Escribir los documentos desde la plataforma, **entregar el expediente el mismo día**, y ver qué correcciones se repiten |
| **3 · Gobernar al agente** | F-005 a F-010, F-020, F-021, F-022, F-031 | El agente recibe las reglas de la plataforma, lo exigido se comprueba solo, y nada se publica rompiendo lo anterior |
| **4 · Dejar constancia** | F-015, F-016, F-017, F-019, F-023, F-024 | Aprobaciones firmadas que caducan al cambiar el texto, auditoría consultable y memoria administrable |
| **5 · Operar el ciclo** | F-004, F-011, F-012, F-013, F-029, F-030, F-032 | Abrir y cerrar fases desde la plataforma, con sus puertas, avisos, reportes y medición |

**Por qué `F-018` está en la primera.** Registrar desde el principio cuesta poco; agregarlo en la cuarta obliga a decidir qué hacer con todo lo que pasó sin registro. Es la única funcionalidad que se adelantó por eso.

**Lo que la versión 1 no da, y conviene saberlo:** el agente sigue trabajando como hoy hasta la versión 3. La plataforma muestra y guarda, pero todavía no gobierna.

**Por qué `F-035` entró a la primera después de aprobado el plan.** Salió al ver la primera pantalla funcionando: conectar no tenía reversa. Un proyecto registrado con el nombre o la ruta equivocados quedaba así para siempre, y el único arreglo era editar a mano lo que la plataforma administra. Postergarlo acumula errores que después hay que limpiar de otra forma, así que entra a la versión 1 como fase H.

**Por qué `F-033` y `F-034` van en la segunda y no en la primera.** Entraron el 2026-08-25, después de aprobado el inventario. Postergarlas no pierde nada: las conversaciones ya están escritas y versionadas, así que se pueden indexar hacia atrás el día que se construya. Es lo contrario de `F-018`, que sí tuvo que adelantarse porque una acción no registrada en el momento no queda escrita en ninguna otra parte.

## 3. Con qué se trabaja

> **El entorno se deja escrito antes de la primera línea.** Lo que no está escrito acá se reconstruye a mano en cada máquina nueva, y nunca queda igual.

| Qué se define | Cómo queda |
|---|---|
| Versiones exactas de lo que se use | Fijadas, y guardadas junto al código |
| Cómo se levanta desde cero en una máquina limpia | Escrito paso a paso, y probado por alguien que no lo instaló antes |
| Qué datos de prueba se usan | Proyectos de mentira creados y borrados por la propia prueba |
| Dónde viven las credenciales | Fuera del repositorio, nunca en el código |

## 4. Cómo se parte el trabajo

> **Una fase es la unidad de ejecución de una historia:** cabe en una jornada, se entrega completa y se revierte sola. Lo que no cabe en una jornada no es una fase, son dos.

Cada funcionalidad del inventario baja a una historia, y cada historia se ejecuta en una o más fases. Acá va el mapa de la versión 1; las demás se abren al llegar a ellas, para no planear con detalle lo que va a cambiar.

**La versión 1 pasó de siete fases a ocho el 2026-08-25**, al entrar `F-035`. Las siete primeras no cambiaron.

| Fase | Funcionalidad que ejecuta | Módulos que toca | Depende de | Estado |
|---|---|---|---|---|
| A. La plataforma levanta y guarda | Base de F-001 | Proyectos | — | Cerrada el 2026-08-25, commit `26b2222` |
| B. Se conecta un proyecto | F-001 | Proyectos | A, D | Cerrada el 2026-08-25, commit `c1b9185` |
| C. La ruta perdida se avisa | F-002 | Proyectos | B | Cerrada el 2026-08-25 |
| D. Todo lo que se hace queda registrado | F-018 | Auditoría | A | Cerrada el 2026-08-25, commit `5231022` |
| E. Se trae un proyecto con lo que tenga escrito | F-027 | Importación | B | Sin abrir |
| F. Lo que no se reconoce se reporta | F-028 | Importación | E | Sin abrir |
| G. Se ve el estado de un proyecto | F-003 | Proyectos | E | Sin abrir |
| H. Un proyecto conectado se administra | F-035 | Proyectos | B | Cerrada el 2026-08-25, commit `5bf4ebb` |

## 5. El orden, y por qué ese

> El orden no es el del documento: es el de las dependencias y el del riesgo. Lo que más incertidumbre tiene va primero, mientras queda tiempo de cambiar de camino.

| Qué va primero | Por qué |
|---|---|
| A, la plataforma que levanta y guarda | Sin ella no hay dónde poner nada |
| D, el registro de auditoría | Registrar desde el primer día evita tener un tramo sin historia |
| E, traer un proyecto que ya existe | Es la fase de mayor incertidumbre de la versión 1: no se sabe cuánto de lo escrito se va a reconocer |
| G, ver el estado, al final de la versión 1 | Necesita que haya algo traído para mostrar; hacerla antes sería mostrar pantallas vacías |

## 6. Cómo se escribe el código

> Lo que se pone acá se exige al revisar. Lo que no está escrito es preferencia personal, y se discute en cada cambio.

| Qué se exige | Cómo se comprueba |
|---|---|
| Nombres y estilo, según lo acordado en el diseño | Revisión, y programa que lo revisa cuando se pueda |
| Prueba junto al código que la necesita | La fase no cierra sin veredicto |
| Sin credenciales ni rutas de una sola máquina | Comprobación que rechaza el guardado |
| Errores que dicen qué pasó y qué hacer | Revisión |
| Cambios pequeños, que se puedan leer de corrido | Revisión |
| Un componente nuevo no obliga a editar los otros | `DA-11`, y se mira en cada revisión |

## 7. Cómo se integra y quién lo revisa

| Qué se define | Cómo queda |
|---|---|
| Cómo se ramifica el trabajo | Una rama por fase, que se integra al cerrarla |
| Quién revisa antes de integrar | Hoy, el agente con una destreza de revisión. **Es la debilidad conocida: no hay una segunda persona** |
| Qué corre solo en cada integración | Las pruebas y las comprobaciones del estándar |
| Qué bloquea la integración | Una prueba en rojo, o una comprobación que reprueba |

## 8. Cómo se deshace lo que salga mal

| Si falla | Cómo se vuelve atrás | Qué se pierde |
|---|---|---|
| Una fase a medias | Se descarta su rama | Solo lo de esa jornada |
| Un cambio ya integrado | Se revierte y se publica una corrección | Nada, si la versión anterior sigue publicada |
| Algo que tocó la base | Se reconstruye el índice desde el texto | Nada: la base es índice, no fuente |
| Traer un proyecto salió mal | Se descarta lo traído | Nada del proyecto de origen: traer no lo modifica |

## 9. Qué se escribe mientras se construye

> **La documentación de esta etapa no se escribe al final.** El documento de la fase se llena en el momento, porque después nadie recuerda por qué se hizo así.

| Qué se escribe | Cuándo | Molde |
|---|---|---|
| Plan de trabajo de la fase | Antes de tocar nada | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) |
| Plan de pruebas | Junto con el plan de trabajo, y se aprueban juntos | [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md) |
| Estado de la fase | Al cambiar de estación | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) |
| Lo que la sesión dejó | En el momento en que aparece | El documento de señales |
| Qué trae la versión, para quien la usa | Al cerrar cada versión | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../plantillas/ciclo-vida-proyectos/19-notas-de-version.md) |

## 10. Cómo se sabe cómo va

| Qué se mide | Cada cuánto | Quién lo mira |
|---|---|---|
| Fases cerradas contra fases abiertas de la versión | Al cerrar cada fase | El autor |
| Funcionalidades verificadas contra las de la versión | Al cerrar cada fase | El autor |
| Deuda declarada que sigue sin pagar | Al cerrar cada versión | El autor |
| Qué se atrasó, y qué lo atrasó | Al cerrar cada versión | El autor |

## 11. La deuda que se declara

> Deuda es lo que se decidió no hacer ahora, con conocimiento. Lo que se olvidó no es deuda: es un defecto. La deuda sin fecha ni dueño no se paga nunca.

| # | Qué queda sin hacer | Por qué se acepta | Quién la paga | Para cuándo |
|---|---|---|---|---|
| 1 | Nadie distinto del autor revisa el código | Hay una sola persona | El autor | Cuando haya alguien más |
| 2 | Sin medición del tiempo de revisión antes de empezar | No hay línea base, y el proyecto ya arrancó | El autor | Antes de afirmar que se redujo |
| 3 | El agente trabaja como hoy hasta la versión 3 | Entregar primero le da más valor al usuario | El autor | Versión 3 |
| 4 | La seguridad vale para un solo usuario en su máquina | Es lo que hay hoy | El autor | Antes de que la use alguien más |

## 12. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Fase, una por historia | [plantillas/ciclo-vida-proyectos/05-fase.md](../../plantillas/ciclo-vida-proyectos/05-fase.md) | Equipo | Pendiente |
| Plan de trabajo y plan de pruebas | Moldes 07 y 08 | Usuario, se aprueban juntos | Pendiente |
| Estado de cada fase | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) | Equipo | Pendiente |
| Notas de cada versión | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../plantillas/ciclo-vida-proyectos/19-notas-de-version.md) | Usuario | Pendiente |
| Cómo se levanta el proyecto | Sección 3 de este documento | Quien instale | Pendiente |
| La plataforma construida | No aplica | Usuario | Pendiente |

## 13. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Tocar código de un módulo | su especificación esté acordada | [`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Ejecutar un plan | esté aprobado junto con su plan de pruebas | [`02·F4`](../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Dar una fase por cerrada | su resultado de pruebas tenga veredicto por criterio | El estado lo fija la prueba, no la lectura |
| Cerrar una versión | cada funcionalidad suya esté verificada o su deuda declarada | Sección 11 de este documento |

## 14. La decisión de cierre

**Aprobada el 2026-08-25.** La etapa queda abierta y sus cinco versiones fijadas; lo que falta para tocar código es la puerta de la especificación.

Falta la puerta: la especificación de los módulos que toca la versión 1, que son **Proyectos, Auditoría e Importación**. Las de los otros nueve módulos se escriben al llegar a su versión, para no documentar hoy lo que va a cambiar en meses.

**Las cinco versiones y su orden quedan fijados acá.** Un cambio de orden se anota como cambio a la línea base, no se hace en silencio.
