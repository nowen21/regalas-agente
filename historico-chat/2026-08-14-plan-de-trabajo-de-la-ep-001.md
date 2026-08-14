<!-- sesion: 6af31d2a-7bcb-4b27-b919-bbf0f4cd5655 -->
<!-- nombre: preguntado -->

# 2026-08-14 — Plan de trabajo de la EP 001

## Conversación

### 1 · Usuario — 2026-08-14 11:15:33
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\documentacion\epicas\EP-002-versionado-y-adopcion\HU-001-numero-de-version-y-que-significa\README.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> siga con la EP-001

### 2 · Usuario — 2026-08-14 11:16:28
> como propone que se llame la sesion?

**Agente** — 2026-08-14 11:16:48
<!-- agente: 00498aee-5578-4306-8f1a-c6945787b172 -->

Ya existe [2026-08-14-sesion.md](historico-chat/2026-08-14-sesion.md) con el ID de esta sesión, así que sería renombrarlo, no crear otro.

Propongo **`2026-08-14-fases-de-la-EP-001.md`** — el trabajo de hoy es bajar las HU de EP-001 a fases (HU-001 ya tiene su fase A; faltan las de HU-002 a HU-008).

Si el alcance termina siendo otro, dos alternativas: `2026-08-14-EP-001-cuerpo-de-reglas-heredable.md` (más amplia) o `2026-08-14-plan-de-trabajo-de-la-EP-001.md`.

¿Cuál dejo?

### 3 · Usuario — 2026-08-14 11:18:02
> 2026-08-14-plan-de-trabajo-de-la-EP-001.md

**Agente** — 2026-08-14 12:04:26
<!-- agente: de100e5f-d9c1-45e9-bfde-d8652d8028e6 -->

Renombrado — quedó `2026-08-14-plan-de-trabajo-de-la-ep-001.md` (el validador pasa el tema a minúsculas). Para que la pestaña y `/resume` digan lo mismo, pegue usted:

```
/rename plan-de-trabajo-de-la-EP-001
```

Ahora sigo con EP-001. Déjeme ver dónde quedó.

Ya tengo el patrón de la fase A. Escribo la fase de HU-002.

Ahora los dos enlaces de vuelta: la HU y el índice de su carpeta.

Hecho: HU-002 ya tiene su fase, con los mismos cuatro documentos de la fase A.

[A-EP-001-HU-002-capas-y-precedencia/](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-002-capas-y-precedencia/A-EP-001-HU-002-capas-y-precedencia/) — plan de trabajo (13 tareas, 19 h), plan de pruebas (8 casos, cobertura 100%), resultado de pruebas sin ejecutar y estado de fase en la estación 7. El enlace quedó en las dos vías: la HU la nombra en su §7 y el README de la carpeta también.

Tres cosas que decidí y conviene que revise:

- **Una sola fase para los tres criterios**, porque los tres se prueban sobre el mismo orden de precedencia (`02·F12.10`).
- **Las tres pruebas de conducta las corre usted**, no yo: si la IA se prueba a sí misma, la prueba no vale.
- **Tres dudas bloquean el arranque** (§2.7 del plan): si el preámbulo es una capa o queda fuera; cuántas capas hay contando la del proyecto; si "opcional" es una marca dentro de la capa o una capa aparte.

Validadores en `0 fallas`.

**Cómo propongo seguir con las seis HU que faltan**, para que lo apruebe antes de escribir 24 documentos más:

| HU | Fases | Por qué |
|---|---|---|
| HU-003 · núcleo | 1 | Los tres criterios se prueban sobre el mismo capítulo |
| HU-004 · conducta | 1 | Igual, más el anexo de marcas |
| HU-005 · convenciones | 3 | Es L: el mapa de temas, las convenciones escritas y el marcado de opcionales son trabajos separables y verificables aparte |
| HU-006 · capa de proyecto | 1 | Un solo mecanismo |
| HU-007 · regla de las reglas | 1 | Un solo procedimiento |
| HU-008 · derogación | 1 | S, tres criterios sobre la misma marca |

Dos observaciones, sin tocar nada:

- La fase A de HU-001 sale con aviso `DOC12`: escribió `**Origen:**` y la plantilla pide `**ORIGEN**`. Es una palabra. ¿La corrijo, aunque sea de otra sesión?
- Estas fases se escriben como plan pendiente, pero lo que planean —`base/00-nucleo-blindado.md`, `M6`, la tabla de capas— ya está escrito en el repo. Mantuve la forma de la fase A por consistencia, pero si la idea es documentar lo ya construido, el molde correcto sería otro (`plantillas/retrodocumentacion.md`). Dígame cuál de los dos es.

Nada commiteado.

### 4 · Usuario — 2026-08-14 12:06:37
> suba solo que le corresponde a esta sesion
