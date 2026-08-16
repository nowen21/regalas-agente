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

**Agente** — 2026-08-14 12:09:22
<!-- agente: c7d8de48-8965-41ed-80f1-7f2fe74bd04b -->

Commiteado `70fca40`, 9 archivos — solo lo de esta sesión:

- los cuatro documentos de la fase A de HU-002 y su README
- la HU-002 y el README de su carpeta, con el enlace a la fase
- la transcripción de hoy y su línea en el índice del histórico

Ese índice lo estaban tocando otras dos sesiones al mismo tiempo, así que preparé aparte la versión con **solo mi línea**. En el árbol de trabajo siguen sus dos líneas intactas, para que las commitee quien las escribió.

**El `push` no lo hice, y es por lo que usted mismo dijo.** En `main` hay tres commits sin publicar que no son de esta sesión:

```
2e49820 docs: las historias de usuario de EP-002 y EP-003
7b2b8da estandar: el termino de otro idioma se traduce o se explica (10.0.0)
597355c estandar: el cierre verifica que el plan de trabajo se hizo (9.1.0)
```

Git no publica un commit suelto: si subo el mío, suben esos tres. No hay forma de subir solo el mío sin reescribir la rama, y eso sí sería meterme con el trabajo de las otras sesiones.

¿Subo los cuatro, o lo dejo commiteado y el `push` lo hace usted cuando esas sesiones cierren?

### 5 · Usuario — 2026-08-14 13:07:27
> cual es el resumen de esta sesión ?

**Agente** — 2026-08-14 13:07:40
<!-- agente: c31345a6-b910-4703-b8ef-5f62d356b189 -->

Pregunta, así que solo respondo.

**Lo que pasó, en orden:**

1. Usted pidió seguir con EP-001. Estaba en que las ocho HU ya estaban escritas y solo HU-001 tenía fase; las otras siete decían "todavía no tiene fases".
2. Le puso nombre a la sesión: [2026-08-14-plan-de-trabajo-de-la-ep-001.md](historico-chat/2026-08-14-plan-de-trabajo-de-la-ep-001.md).
3. Escribí la **fase A de HU-002** — capas y precedencia — con sus cuatro documentos, siguiendo el mismo molde de la fase A de HU-001. Enlace en las dos vías, validadores en `0 fallas`.
4. Commiteé `70fca40` con solo lo de esta sesión. Sin `push`.

**Lo que quedó abierto y espera respuesta suya:**

| Qué | Por qué le toca a usted |
|---|---|
| El `push` | Subir el mío sube tres commits de otras sesiones |
| Cómo parto las seis HU restantes | Propuse 1 fase cada una, salvo HU-005 que van 3. Son 24 documentos más |
| Las tres dudas del plan de HU-002 | Bloquean el arranque de la fase: si el preámbulo es capa, cuántas capas hay, si "opcional" es marca o capa |
| El aviso `DOC12` de la fase A de HU-001 | Escribió `**Origen:**` y la plantilla pide `**ORIGEN**`. Es de otra sesión |
| Si estas fases son plan o retrodocumentación | Planean cosas que ya están escritas en `base/`. Mantuve la forma de la fase A, pero puede que el molde correcto sea otro |

Ese último punto es el que más pesa: si la respuesta es "retrodocumentación", los documentos de HU-002 hay que rehacerlos antes de escribir los de las otras seis.

### 6 · Usuario — 2026-08-14 22:53:18
> entonces que fue lo que hizo acá: hu-de-la-comprobacion-automatica?

**Agente** — 2026-08-14 22:53:53
<!-- agente: f7ee9ebe-6918-461b-9098-73f2f86b6d0c -->

Esa es otra sesión, en paralelo. Arrancó el 13 a las 23:12 preguntando qué faltaba del pendiente 01 y cerró hoy a las 16:43.

**Lo que hizo:**

1. **Se torció al principio.** El agente se puso a escribir validadores directo desde el pendiente, sin épica, sin historia y sin plan. Usted lo detectó y mandó encadenar. Ese código quedó **sin commitear**, como línea base, no como trabajo hecho.
2. **Escribió las 54 historias de usuario** de las siete épicas: 12 de EP-004 y las de EP-002, EP-003, EP-005, EP-006 y EP-007. Más la fase A de HU-010.
3. **Tradujo "spec" a "especificación"** en 53 archivos, y nació la regla `01·C20` — la palabra de otro idioma se traduce o se explica. Versión 10.0.0.
4. **Reforzó `01·C5 · Responde corto`**: "menos es más" ahora está escrito como norma.
5. **Creó el resumen de sesión** como cosa aparte del histórico: [plantillas/sesion.md](plantillas/sesion.md) y [historico-chat/resumenes/](historico-chat/resumenes/), una carpeta por día y un archivo por sesión. Doce campos por hallazgo, incluido el orden en que se resuelven.
6. **Dejó nueve hallazgos anotados**, cada uno con su pendiente enlazado, y el orden de lo que sigue: H-4 → H-8 → H-1 → H-7 → H-6 → H-9 → H-5.

**Lo que le toca a lo mío:** esa sesión creó `historico-chat/resumenes/` y la plantilla del resumen **después** de que yo escribí lo de HU-002. Esta sesión no tiene resumen escrito, y por ese criterio nuevo no estaría lista para cerrar.

Y ya subió a git — `f51962a` entre otros. Los tres commits que le mencioné hace un rato ya no son los mismos.

### 7 · Usuario — 2026-08-14 22:54:22
> perdón acá:
>
> h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido

**Agente** — 2026-08-14 22:54:56
<!-- agente: d2372dcc-e51c-4e0d-9cc7-8e25b6e9ab7b -->

Esa sí es la que cerró **H-4**: no había dónde escribir lo aprendido.

**Lo que hizo:** ejecutó las tres fases de la cadena y las cerró.

| Paso | Qué dejó | Commit |
|---|---|---|
| La marca del espacio por llenar | Reglas `13·DOC19`, `DOC20`, `DOC21`; 179 huecos convertidos en 13 plantillas | `b877f37` |
| El modelo del resumen | La plantilla del resumen de sesión | `e998cc2` |
| El enganche que lo sostiene | El resumen ya no depende de que alguien se acuerde | `40f9937` |

**Ocho hallazgos, cinco cerrados ahí mismo.** Los más gruesos:

- **`02·F21`** — un incumplimiento ya identificado no se repite en lo nuevo. Salió de su frase: *"yo antes escribía sin ortografía, pero a partir de que aprendí ya escribo con ortografía"*. Un pendiente sirve para limpiar lo viejo, no para autorizar más de lo mismo.
- **El paso 0 del `CLAUDE.md`** — este repo no exigía cargar `base/` al abrir sesión, y el `CLAUDE.md` que se instala en un proyecto heredero sí. El agente escribía el estándar sin haberlo leído.

**Tres quedaron abiertos:** buscar en el repositorio antes de preguntar (pendiente 24), corregir lo ya escrito con marcas de generación automática (pendiente 25) y `plantillas/` mezclando modelos con procedimientos (pendiente 23).

**Y me toca a mí.** Ese paso 0 se agregó hoy, después de que yo abrí sesión: mi contexto trae el `CLAUDE.md` viejo, sin él. Los cuatro documentos de la fase de HU-002 que commiteé están llenos de raya larga como inciso, que es justo lo que `00·ID8` prohíbe. Es el hallazgo H-6 de esa sesión, repetido por mí una hora después.

¿Los corrijo?

### 8 · Usuario — 2026-08-14 22:55:56
> esto: h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido logró el objetivo?

**Agente** — 2026-08-14 22:56:41
<!-- agente: f81c6288-5af5-4edd-a336-c5740a465e66 -->

Sí, pero con una salvedad que esta misma sesión demuestra.

**Lo que sí logró.** Las tres fases de la cadena están cerradas y commiteadas, el hallazgo quedó marcado resuelto en el resumen donde nació, y el mecanismo existe de verdad: [validadores/hook_resumen.py](validadores/hook_resumen.py) crea el archivo al abrir la sesión y avisa cuando le falta algo. Ya no depende de que el agente se acuerde.

**Dónde no llega, y lo verifiqué:**

1. **Esta sesión no tiene resumen.** Empezó a las 11:15; el enganche se instaló después. El archivo se crea en `SessionStart`, y el aviso solo habla si ese archivo ya existe. Como el mío nunca se creó, el aviso no puede sonar nunca. Una sesión que cruza la instalación queda ciega.

2. **Una sesión que solo escribe documentación no dispara el aviso.** `_produjo_algo` mira si hay cambios en `base/` o `plantillas/`, o algo preparado para guardar. Lo mío fue todo `documentacion/` sin preparar, así que no contaba como haber producido nada — hasta que commiteé.

El primero se arregla solo: la próxima sesión ya nace con el enganche. El segundo no, y es del mismo tipo de agujero que H-4 vino a tapar.
