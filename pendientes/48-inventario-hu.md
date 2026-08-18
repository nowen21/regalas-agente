# Inventario de HU — el estándar


| Items|Lo que se debe hacer |
|---|---|
| **Historia de usuario** | [EP-004 · HU-017 — Inventario de HU sin fase](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) — el inventario es esa historia, y las 42 dudas que lo detienen son el [59](59-las-42-dudas-que-detienen-26-fases.md) |
| **Qué pasa** | `02·F12.2` pide al menos una fase por HU, y cada fase deja cinco documentos. |
| **Qué se debe completar** | lo que esté en ☐ en la tabla |
| **Total de HU** | 74 |
| **Completas** | 33 |
| **Incompletas** | 41 |
| **Cierra cuando** | Incompletas = 0 ☐ |

**Los dos números se corrigen en la misma edición en que se marca la casilla.** Cuando una fila queda con sus seis ☑, **Completas** sube uno e **Incompletas** baja uno — nunca se toca una sola de las dos. Si hace falta recontar desde cero, se cuenta la tabla: fila con seis ☑ es completa, cualquier otra es incompleta.

*Anotado el 2026-08-16 sobre 66 HU —14 completas y 52 incompletas—, y ese mismo día nacieron [HU-017](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) y [HU-018](../documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md), que lo dejaron en 68 y 54. La HU-017 es la que hace esta cuenta sola.*

> **Los tres números cambiaron el 2026-08-17 y conviene leer por qué, o se leen como un retroceso.**
>
> **68 → 74 total.** Seis historias nuevas, escritas al enrutar el backlog: ningún pendiente podía quedar suelto y seis no tenían dónde caer. No son trabajo nuevo pendiente — son trabajo que ya existía y no tenía a quién rendirle cuentas.
>
> **39 → 31 completas.** Ocho historias que estaban completas ganaron una fase **sin terminar**, y una fase a medias vuelve incompleta a su historia. Seis vienen de la sesión que ejecutaba los 51 planes y quedó detenida; la séptima es la fase `B` de [EP-004 · HU-016](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/), que espera aprobación.
>
> **2026-08-18 · sube a 33.** La [EP-001 · HU-011](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md) —buscar en el repositorio antes de preguntar— cerró su fase `A` con los cinco documentos. Nació ayer al enrutar el backlog y se construyó hoy. Y la [EP-007 · HU-008](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) —el proyecto reporta lo que es del estándar y el estándar le avisa de vuelta— cerró la suya, también del día a la mañana siguiente.
>
> **Y las seis histórias nuevas entran a la tabla.** Contaban en el total desde ayer, pero no tenían fila: el total decía 74 y la tabla listaba 68. Un inventario al que hay que creerle el encabezado porque su propia tabla no lo respalda no sirve de inventario.
>
> **No se deshizo nada.** Las 39 que estaban cerradas siguen cerradas; lo que pasó es que se abrió trabajo encima. El número baja porque mide *historias sin nada pendiente*, no *trabajo hecho*.


## Qué le falta a cada HU

☐ incompleto · ☑ completo. Una casilla se marca ☑ **solo** cuando el archivo existe en la carpeta de la fase, no cuando se decidió hacerlo.

| Épica | HU | Fase | `plan_trabajo` | `plan_pruebas` | `resultado_pruebas` | `estado-fase` | `funcionalidad_implementada` |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| EP-001 | [HU-001 — Formato único para escribir una regla](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-001-formato-unico-de-regla/HU-001-formato-unico-de-regla.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☐ |
| EP-001 | [HU-002 — Capas de reglas y orden de precedencia](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-002-capas-y-precedencia/HU-002-capas-y-precedencia.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☐ |
| EP-001 | [HU-003 — El núcleo de reglas que no se sobrescribe](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-001 | [HU-004 — Reglas de conducta de la IA](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/HU-004-conducta-de-la-ia.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-001 | [HU-005 — Convenciones de ingeniería agnósticas](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-005-convenciones-de-ingenieria/HU-005-convenciones-de-ingenieria.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-001 | [HU-006 — La capa propia de cada proyecto](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/HU-006-capa-propia-del-proyecto.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-001 | [HU-007 — La regla que gobierna cómo se escriben las reglas](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-001 | [HU-008 — Derogar una regla sin borrarla ni renumerarla](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-008-derogacion-sin-borrar/HU-008-derogacion-sin-borrar.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-001 | [HU-009 — Poner al día las reglas que no pasan su propio checklist](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-001 | [HU-010 — Cuándo no aplica la exigencia de especificación](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-001 | [HU-011 — Buscar en el repositorio antes de preguntar](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-001 | [HU-012 — Inventario de las acciones del agente y su riesgo](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md) | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| EP-001 | [HU-013 — Capítulos opt-in de dominio](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| EP-002 | [HU-001 — Fijar el número de versión y qué significa cada parte](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-001-numero-de-version-y-que-significa/HU-001-numero-de-version-y-que-significa.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-002 | [HU-002 — Llevar el registro de qué cambió en cada versión](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/HU-002-registro-de-cambios.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-002 | [HU-003 — Declarar en el proyecto la versión adoptada y la fecha](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-002 | [HU-004 — Avisar al abrir sesión cuando el proyecto quedó atrás](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/HU-004-aviso-al-quedar-atras.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-002 | [HU-005 — Sellar el trabajo cerrado con su versión](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/HU-005-sellar-el-trabajo-cerrado.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-002 | [HU-006 — Quién sube la versión cuando hay dos sesiones abiertas](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-003 | [HU-001 — Definir cómo se marca un espacio por llenar en un modelo](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/HU-001-marca-de-espacio-por-llenar.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-003 | [HU-002 — Crear los modelos del encargo: brief, épica, historia de usuario](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-003 | [HU-003 — Crear los modelos de la fase: plan de trabajo, plan de pruebas, cierre](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-003-modelos-de-la-fase/HU-003-modelos-de-la-fase.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-003 | [HU-004 — Crear el modelo de la especificación de un módulo](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/HU-004-modelo-de-la-especificacion.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-003 | [HU-005 — Crear los modelos de la capa de proyecto: stack, dominio, nombres propios](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-005-modelos-de-la-capa-de-proyecto/HU-005-modelos-de-la-capa-de-proyecto.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-003 | [HU-006 — Escribir los procedimientos de cada rol del trabajo](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-006-procedimientos-por-rol/HU-006-procedimientos-por-rol.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-003 | [HU-007 — Escribir el procedimiento que dirige a los demás y controla los cortes](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-007-procedimiento-que-dirige/HU-007-procedimiento-que-dirige.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-003 | [HU-008 — Declarar los puntos donde aprueba una persona](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-008-puntos-de-aprobacion/HU-008-puntos-de-aprobacion.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-003 | [HU-009 — Crear el modelo del resumen de sesión](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-009-modelo-del-resumen-de-sesion/HU-009-modelo-del-resumen-de-sesion.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-003 | [HU-010 — Crear el glosario de la terminología del estándar](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-001 — Fijar el criterio de qué se comprueba con un programa](../documentacion/epicas/EP-004-comprobacion-automatica/HU-001-criterio-de-lo-comprobable/HU-001-criterio-de-lo-comprobable.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-002 — Marcar en cada regla si es comprobable](../documentacion/epicas/EP-004-comprobacion-automatica/HU-002-marca-de-comprobable-en-cada-regla/HU-002-marca-de-comprobable-en-cada-regla.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-003 — Definir el formato de un hallazgo y su severidad](../documentacion/epicas/EP-004-comprobacion-automatica/HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-004 — Comprobar la forma de los documentos y sus espacios sin llenar](../documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-005 — Comprobar los enlaces y las citas a reglas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-006 — Comprobar la nomenclatura y la estructura de carpetas del trabajo](../documentacion/epicas/EP-004-comprobacion-automatica/HU-006-nomenclatura-y-estructura/HU-006-nomenclatura-y-estructura.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-007 — Comprobar que no salgan claves ni datos sensibles](../documentacion/epicas/EP-004-comprobacion-automatica/HU-007-claves-y-datos-sensibles/HU-007-claves-y-datos-sensibles.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-008 — Correr todas las comprobaciones de una sola vez](../documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-009 — Registrar cuántos hallazgos hubo por regla](../documentacion/epicas/EP-004-comprobacion-automatica/HU-009-conteo-por-regla/HU-009-conteo-por-regla.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-010 — Comprobar el código contra la convención que el proyecto declara](../documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/HU-010-convencion-declarada-por-el-proyecto.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☐ |
| EP-004 | [HU-011 — Comprobar que cada regla del estándar cumple su propio molde](../documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/HU-011-molde-de-las-reglas.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-012 — Comprobar las marcas de generación automática en lo que se entrega](../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/HU-012-marcas-de-generacion-automatica.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-013 — Comparar el plan aprobado con lo que se hizo](../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-014 — Un solo veredicto por fase](../documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-015 — Derogación sin adoptar](../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-016 — Comprobar que el pendiente cerrado nombra su fase](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-004 | [HU-017 — Decir cuántas HU quedan sin su fase completa](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-004 | [HU-018 — Avisar cuando dos pendientes se disputan el mismo número](../documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-005 | [HU-001 — Escribir la sesión a medida que pasa, con hora del reloj](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-005 | [HU-002 — Enmascarar una clave antes de que quede escrita](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-005 | [HU-003 — Disparar las comprobaciones al escribir un archivo](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-005 | [HU-004 — Controlar el mensaje con que se guarda un cambio](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-004-control-del-mensaje-de-cambio/HU-004-control-del-mensaje-de-cambio.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-005 | [HU-005 — Impedir guardar un cambio de reglas sin versión ni registro](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-005 | [HU-006 — Correr la batería completa antes de publicar](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-006-bateria-antes-de-publicar/HU-006-bateria-antes-de-publicar.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-005 | [HU-007 — Recoger al abrir sesión lo que quedó guardado por fuera del repositorio](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-005 | [HU-008 — El enganche que sostiene el resumen de la sesión](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-005 | [HU-009 — Lo que gobierna cada frase llega puesto al abrir la sesión](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-005 | [HU-010 — El capítulo que rige lo que se escribe llega al escribirlo](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md) | ☑ | ☑ | ☑ | ☐ | ☑ | ☐ |
| EP-005 | [HU-011 — Dónde termina el estándar y dónde empieza el adaptador](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| EP-005 | [HU-012 — Hacer cumplir lo que hoy solo se recuerda](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| EP-006 | [HU-001 — Definir qué se guarda, con qué tipos y qué alcances](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-001-que-se-guarda-tipos-y-alcances/HU-001-que-se-guarda-tipos-y-alcances.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-006 | [HU-002 — Guardar lo aprendido en el repositorio](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-002-guardar-en-el-repositorio/HU-002-guardar-en-el-repositorio.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-006 | [HU-003 — Buscar por palabra sin instalar nada](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-003-busqueda-por-palabra/HU-003-busqueda-por-palabra.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-006 | [HU-004 — Buscar por significado con un modelo local y opcional](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-004-busqueda-por-significado/HU-004-busqueda-por-significado.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-006 | [HU-005 — Separar lo que el proyecto aprendió de cómo el usuario quiere trabajar](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-006 | [HU-006 — Sacar del almacén local lo que deba vivir en el repositorio](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-006-sacar-del-almacen-local/HU-006-sacar-del-almacen-local.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-006 | [HU-007 — Marcar lo que dejó de aplicar sin borrarlo](../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-007-marcar-lo-que-dejo-de-aplicar/HU-007-marcar-lo-que-dejo-de-aplicar.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-001 — Instalar todo con una sola línea](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/HU-001-instalar-con-una-linea.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-002 — Mostrar qué va a hacer antes de hacerlo](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-002-mostrar-antes-de-hacer/HU-002-mostrar-antes-de-hacer.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-003 — Crear la estructura de carpetas del trabajo](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-003-estructura-de-carpetas/HU-003-estructura-de-carpetas.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-004 — Generar y poner los automatismos](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-004-generar-los-automatismos/HU-004-generar-los-automatismos.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-005 — No pisar lo que escribió la persona](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-006 — Poner al día lo ya instalado](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/HU-006-poner-al-dia.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-007 — Revisar qué le falta al proyecto](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/HU-007-revisar-que-falta.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |
| EP-007 | [HU-008 — El proyecto reporta lo que es del estándar, y el estándar le avisa de vuelta](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |

## Cómo se llena la tabla

1. **Una fila a la vez**, de arriba abajo. No se abren dos en paralelo.
2. Se crea la carpeta `<letra>-EP-0NN-HU-0NN-<slug>` dentro de la carpeta de la HU (`02·F12.6`) y se marca **Fase**.
3. Los documentos se escriben **en el orden de las columnas**: el `resultado_pruebas` no se marca antes que el `plan_pruebas`, y ninguno antes que el `plan_trabajo`.
4. Cada archivo sale de su plantilla de [`plantillas/`](../plantillas/) — la estructura no se inventa.
5. Al marcar la última casilla de una fila se corrige la **§8 de la HU**, que hoy dice que no se descompuso en fases, y su **Estado** de la §1.
6. La casilla la marca quien escribió el archivo, en la misma sesión. Una fila a medias no se deja sin que `estado-fase` diga qué la tiene detenida.

**El paso 2 quedó decidido el 2026-08-17: la carpeta nace con su `plan_trabajo.md` adentro.** Git no guarda carpetas vacías, así que una fase abierta y todavía sin plan existe en la máquina donde se creó y en ninguna otra: no entra en ningún commit, un clon no la ve, y `fases.py` tampoco, porque lee el disco. La salida que eligió el usuario es que el problema no se presente — no hay momento en que la carpeta exista vacía, y las casillas **Fase** y **`plan_trabajo`** se marcan juntas.

De las tres salidas que estaban sobre la mesa —`.gitkeep` en cada carpeta, carpeta sola, o escribir ya el plan— se tomó la tercera. No hacen falta archivos de 0 bytes, y la columna **Fase** no queda afirmando nada que no se pueda comprobar en un clon.

**El paso 2 de la plantilla [`inventario-hu.md`](../plantillas/inventario-hu.md) todavía dice «se crea la carpeta y se marca Fase», sin más.** Ponerlo al día es cambio de `plantillas/`: suma entrada en el [CHANGELOG](../CHANGELOG.md) y sube [VERSION](../VERSION) (`20·M10`), y por eso no se hizo junto con esto.

**Y el orden de llenado cambió a propósito.** El paso 1 pide una fila a la vez, de arriba abajo. El 2026-08-17 el usuario pidió el `plan_trabajo` de todas las fases que no lo tienen, que es recorrer la columna en vez de la fila. Se hizo así, y tiene un costo: cada fila abierta queda a medias hasta que le entren los otros cuatro documentos, y el paso 6 pide que una fila a medias no se deje sin que su `estado-fase` diga qué la tiene detenida. Mientras esos `estado-fase` no existan, lo que dice qué falta es el `README.md` de cada carpeta de fase.

## Casi todo es retrodocumentación

No falta trabajo: falta la cadena. La memoria, el versionado, los validadores y los enganches **ya están construidos y cerrados** — los pendientes [02](hecho/vigencia-y-poda-de-memoria.md), [04](hecho/version-del-estandar.md), [05](hecho/memoria-semantica.md) y [validadores-y-hooks](hecho/validadores-y-hooks.md). Lo que no existe es el documento que diga con qué plan se hizo, con qué casos se probó y qué salió.

Por eso las filas se escriben contra lo que ya está en el repo, sin tocar una línea de producción. Es lo mismo que se hizo en el [38](hecho/el-validador-de-la-f22-tiene-su-fase.md), donde se supo que al trabajo sin cadena no le faltaba documentación: le faltaba prueba atada a su criterio.

## Cómo se sabe que cerró

No queda ni un ☐ en la tabla, y `python validadores/validar.py fases` y `… trazabilidad` no reportan HU sin fase.
