<!-- sesion: cb97c715-00ca-47bc-84f0-7f71dd3ef116 -->
<!-- nombre: preguntado -->

# 2026-08-17 — Plan de pruebas y estado de las 51 fases

## Conversación

### 1 · Usuario — 2026-08-17 12:10:59
> Crear el plan_pruebas y estado-fase.md de todas las fases que actualmente no los tengan.

### 2 · Usuario — 2026-08-17 14:10:20
> siga

**Agente** — 2026-08-17 15:13:25
<!-- agente: d0cb67eb-65cc-4b91-a1ba-5335228515a3 -->

Antes de seguir, dejo anotado en el resumen de sesión lo que va apareciendo.

Sigo con las 11 fases que faltan de EP-004.

26 de 51. Sigo.

31 de 51. Faltan tres de EP-004.

34 de 51 — EP-004 completa. Voy con EP-005.

38 de 51. Sigo con las cuatro que faltan de EP-005.

42 de 51 — EP-005 completa. Voy con EP-006.

45 de 51. Faltan cuatro de EP-006.

47 de 51 — EP-006 completa. Quedan las cuatro de EP-007.

Las 51 están escritas. Verifico y cierro los pendientes de coherencia.

Ahora las casillas del inventario, que llevan la cuenta.

Corro las comprobaciones para verificar que los enlaces que escribí resuelven.

Verifico que los enlaces relativos que escribí resuelven de verdad.

El defecto ya está anotado (pendiente 41). Agrego la medición al resumen de sesión.

Listo. Escribí el `plan_pruebas.md` y el `estado-fase.md` de las **51 fases** que no los tenían — las 70 del árbol ahora tienen los dos.

**Qué contiene cada uno**

El `plan_pruebas.md` sigue la [plantilla](plantillas/planes/pruebas.md) en su forma de fase chica (§3, 5, 6, 9 y 12), derivado del `plan_trabajo.md` de su fase: cada CA con al menos un caso, cobertura 100 %, y los riesgos del plan convertidos en criterios de defecto. Queda en **Borrador** — se aprueba junto con el plan de trabajo ([`02·F4`](base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

El `estado-fase.md` las sitúa en la **estación 4** (pausa y presentación), con veredicto «Todavía no se ejecutó», las tareas en Pendiente o **Bloqueada** con la duda que las bloquea, y qué falta para desbloquear.

**Lo que quedó a la vista al escribirlos**

- **La mayoría de las fases está bloqueada por una duda de §2.7 del plan**, no por falta de trabajo. En varias —[HU-010 de EP-001](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/estado-fase.md), [HU-006 de EP-002](documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/estado-fase.md), [HU-011 de EP-004](documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr/estado-fase.md)— está bloqueado *todo*. La §3 de cada estado-fase es la lista de lo que hay que decidir para que la épica avance.
- **Varios CA van a quedar en «No» y eso está declarado antes de correr**: el cambio sin entrada en el registro, la regla sin clasificar, el aviso de desfase que no dice qué cambió. Los casos están escritos afirmando la falta, para que el rojo sea el dato que la fase siguiente necesita y no parezca defecto de la fase que lo mide.
- **[A-EP-004-HU-011](documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr/estado-fase.md) desbloquea a otras**: media docena de fases cierran un CA «por lectura» solo porque `metareglas.py` no se puede correr.

**Coherencia**

Actualicé los 51 `README.md` de fase (tabla de contenido y la frase de lo que falta) y las casillas de `plan_pruebas` y `estado-fase` en el [inventario 48](pendientes/48-inventario-hu.md). Las cuentas de completas/incompletas no cambian: a esas HU les siguen faltando `resultado_pruebas.md` y `funcionalidad_implementada.md`, que **salen de ejecutar** — escribirlos ahora sería inventar el resultado.

**Comprobado**

`validar.py fases` en 0 fallas. De los 1438 enlaces relativos de los 140 documentos, **0 rotos en los 102 que escribí**; los 28 rotos que aparecen son el marcador `«RUTA-ESTANDAR»` sin resolver en las 19 fases previas — el pendiente [41](pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md), al que le dejé la medición en el [resumen de sesión](historico-chat/resumenes/2026-08-17/sesion-2.md). Las 4 fallas de `validar.py estandar` son previas y están en `pendientes/`, sin relación con esto.

No hice commit: queda para que lo leas y lo autorices.

### 3 · Usuario — 2026-08-17 15:14:46
> osea ya quedó todo y puedo cerrar?

**Agente** — 2026-08-17 15:15:02
<!-- agente: 777a2e00-13b5-4fe7-b5a7-8f301050e207 -->

Lo escrito, sí: las 51 fases quedaron con sus dos documentos, los README y el inventario coherentes, y las comprobaciones corridas.

**Pero cerrar ahora perdería el trabajo: nada está guardado.** Son 102 archivos nuevos más los 51 README y el inventario, todos sin commit. El [resumen de sesión](historico-chat/resumenes/2026-08-17/sesion-2.md) tiene tres de sus cuatro casillas marcadas; la que falta es justamente esa.

Para cerrar limpio faltan dos cosas, las dos tuyas:

1. **Leer el cambio y autorizar el commit.** Si querés revisar antes, el más representativo es [A-EP-001-HU-004/plan_pruebas.md](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia/plan_pruebas.md) con su [estado-fase.md](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia/estado-fase.md) al lado — los otros 50 pares siguen la misma forma.

2. **Ponerle nombre a la sesión**, que hoy se guarda como `2026-08-17-sesion-2.md` y no dice de qué trata. Propongo:

   `2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md` — se escribieron el plan de pruebas y el estado de fase de las 51 fases abiertas que no los tenían, y quedó a la vista que la mayoría está bloqueada por dudas sin responder.

   ¿Va? Si sí, yo corro el renombrado y vos pegás `/rename plan-de-pruebas-y-estado-de-las-51-fases`, que es lo que le pone el mismo nombre a la sesión en la pestaña y en `/resume` — ese comando no lo puedo escribir por vos.

Decime si autorizás el commit y si el nombre te sirve.

### 4 · Usuario — 2026-08-17 15:15:36
> 1. suba
> 2. /rename plan-de-pruebas-y-estado-de-las-51-fases
