# 2026-08-16 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-sesion-7.md](../../2026-08-16-sesion-7.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** la priorización del backlog de [la-prioridad-de-los-pendientes](la-prioridad-de-los-pendientes.md). El usuario pidió resolver los ocho pendientes marcados `P1`, recordando que cada uno tiene que pertenecer a una historia de usuario.

---

## Hallazgos de esta sesión

### H-1 · Los ocho `P1` tienen dónde entrar, y tres necesitan una decisión antes

- **Qué pasó:** se bajó cada uno a su historia. **35** → EP-005·HU-008 · **38** → EP-004·HU-015 · **43** → EP-003·HU-004 más un validador · **30** → EP-007·HU-007 · **19 y el punto 7 del 33** → EP-001·HU-009 · **27** → reabrir su propia fase · **28** → EP-004·HU-014. Ninguna historia hubo que inventarla: las siete ya existían.
- **Por qué importa:** [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) prohíbe construir desde el archivo del pendiente, y sin el mapa cada uno vuelve a empezar por preguntar dónde va.
- **Qué se decidió:** el orden es 35 → 38 → 43 → 30 → 19 → 33·7 → 27 → 28. Los cuatro primeros no dependen de nada.
- **Estado:** **abierto** — tres decisiones son del usuario y siguen sin respuesta: (1) qué se hace con las siete reglas publicadas en «no cumple»; (2) si el veredicto único se comprueba con un programa o el `estado-fase` deja de copiarlo; (3) quién lee el glosario para el `CP-006` del 27, o si se declara no corrido.
- **Responde a:** —
- **Dispara:** las siete fases del mapa. La primera ya está construida (H-2).
- **Dónde queda:** en esta sesión y en el [índice del backlog](../../../pendientes/README.md).
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** las tres decisiones. Sin la primera no arranca el 19; sin la segunda, el 28.

### H-2 · Renombrar una sesión dejaba a medias el resumen que arrastraba

- **Qué pasó:** `historico.py --renombrar` movía el resumen a su nombre nuevo pero no tocaba su contenido, así que el enlace de vuelta a la transcripción quedaba apuntando al archivo que ya no existía. Lo reportó `shopnest-mesa` y le pasó tres veces a esta casa el mismo día.
- **Por qué importa:** es el propio estándar el que pide ponerle nombre a la sesión, y el comando que ofrecía para hacerlo dejaba el repositorio con un enlace roto.
- **Qué se decidió:** se corrigen **las dos partes** del enlace, el texto visible y el destino, porque [`13·DOC14`](../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) pide que el texto diga dónde vive el archivo. Se reemplaza el par exacto, para no tocarle el enlace a otra sesión que el resumen nombre.
- **Estado:** **resuelto acá** — v21.3.0, veredicto Cumple, 22 pruebas en verde. El arreglo se vio fallar a propósito antes de darlo por bueno.
- **Responde a:** el pendiente 35, cerrado en [pendientes/hecho/renombrar-deja-el-resumen-coherente.md](../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md).
- **Dispara:** —
- **Dónde queda:** fase [`B-EP-005-HU-008`](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/), `_reenlazar()` en `historico.py` y la primera suite de pruebas de ese programa.
- **Nace en:** 2026-08-16 · sesión 7
- **Cerrado en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** falta avisarle a `shopnest-mesa`, que tiene su pendiente de seguimiento abierto.

### H-3 · La HU-008 exigía el arrastre y ningún criterio suyo lo medía

- **Qué pasó:** su `RN-06` dice que el enganche «crea, avisa y **arrastra**», pero los tres criterios de aceptación miraban solo lo primero y lo segundo. Sin criterio no hay de dónde derivar un plan ([`02·F18`](../../../base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).
- **Por qué importa:** una regla de negocio escrita en la historia y sin criterio que la mida no se construye nunca, y nadie lo nota: la historia se cierra con todos sus criterios en verde.
- **Qué se decidió:** la exigencia sube a la historia como `CA-04` y el plan baja de ella. Se aprobó junto con el plan.
- **Estado:** resuelto acá
- **Responde a:** H-2
- **Dispara:** conviene mirar si otras historias tienen reglas de negocio sin criterio. No se revisó.
- **Dónde queda:** [HU-008](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) §4.
- **Nace en:** 2026-08-16 · sesión 7
- **Cerrado en:** 2026-08-16 · sesión 7

### H-4 · `enlaces.py` termina en silencio sin comprobar nada

- **Qué pasó:** `python validadores/enlaces.py --raiz .` no tiene punto de entrada: sale con código 0 y sin imprimir. Esta sesión lo corrió y leyó ese silencio como «cero enlaces rotos». El entrypoint real es `validar.py estandar`, y corriéndolo aparecieron 20.
- **Por qué importa:** un validador que calla sin haber mirado es peor que ninguno — el silencio es exactamente la señal de que todo está bien. La métrica de una fase quedó escrita mal por eso, y se corrigió.
- **Qué lo soluciona:** que el programa tenga punto de entrada, o que se muera diciendo por dónde se corre. Conviene revisar si los demás validadores tienen el mismo hueco.
- **Estado:** **anotado** → [pendiente 53](../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)
- **Responde a:** —
- **Dispara:** —
- **Dónde queda:** §4 del [resultado de pruebas](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/resultado_pruebas.md) de la fase.
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** correr `validar.py estandar` sobre el repositorio y mirar cuántos validadores se pueden invocar solos.

### H-5 · Cerrar un pendiente rompe los enlaces que lo citaban

- **Qué pasó:** mover el archivo del 35 a `pendientes/hecho/` dejó 12 enlaces huérfanos. Nueve siguen rotos, en cuatro archivos que el plan de la fase no declaraba. **Y ya había pasado:** al cerrar el 45 quedó roto el enlace del `plan_trabajo` de su propia fase, y nadie lo vio.
- **Por qué importa:** es el mismo defecto que esta sesión acaba de cerrar para las sesiones renombradas, un piso más arriba. El backlog se cita a sí mismo —el 36 nombra al 34 y al 35, el 33 al 19 y al 31— y cada cierre rompe esas citas.
- **Qué lo soluciona:** lo mismo que el [punto 4 del pendiente 33](../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md): el modo de reparación de `citas.py`, aplicado también al mover un pendiente a `hecho/`.
- **Estado:** **anotado** → [pendiente 54](../../../pendientes/hecho/cerrar-un-pendiente-arrastra-sus-citas.md). Los nueve enlaces de ese primer cierre ya se corrigieron a mano; la causa sigue.
- **Responde a:** H-2
- **Dispara:** —
- **Dónde queda:** §4 del resultado de pruebas de la fase, y el punto 4 del 33 en el índice del backlog.
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** los cuatro archivos están listados en el §3 del [estado de fase](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/estado-fase.md).

### H-6 · El validador de enlaces no respeta las comillas de código

- **Qué pasó:** marcó como rotas dos muestras escritas entre comillas invertidas dentro de un plan de pruebas, que nunca fueron enlaces sino el texto de lo que la prueba tiene que encontrar.
- **Por qué importa:** obliga a redactar torcido para que el validador no se queje, o enseña a ignorar sus hallazgos. Es de la misma familia que el punto 1 del 33, donde da por rotos los enlaces con espacios.
- **Qué lo soluciona:** que `enlaces.py` no busque enlaces dentro de un bloque ni de un tramo de código.
- **Estado:** **anotado** → [pendiente 55](../../../pendientes/hecho/los-enlaces-de-ejemplo-no-son-enlaces.md). Conviene con el punto 1 del 33: mismo archivo, misma clase de falso positivo.
- **Responde a:** —
- **Dispara:** —
- **Dónde queda:** este resumen.
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** las dos muestras se reescribieron para esquivarlo; el defecto sigue.

### H-7 · El índice del backlog se contradice sobre si queda algún `P0`

- **Qué pasó:** la cabecera dice «**Ya no queda ningún `P0`**: lo más urgente hoy son los `P1`», y la fila del pendiente 36 sigue marcada `P0`.
- **Por qué importa:** es un documento del estándar afirmando algo que no es cierto, que es justo lo que la `P1` define. Y decide qué se trabaja primero.
- **Qué lo soluciona:** una de dos: bajar el 36 a `P1` y borrar la contradicción, o quitar la frase. Es del usuario, porque es su priorización.
- **Estado:** **abierto** — preguntado dos veces en esta sesión, sin respuesta.
- **Responde a:** —
- **Dispara:** —
- **Dónde queda:** [pendientes/README.md](../../../pendientes/README.md), cabecera y fila del 36.
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** una línea de respuesta.

### H-8 · Al trabajo sin cadena no le faltaba documentación, le faltaba prueba

- **Qué pasó:** el pendiente 38 decía que el validador de la `F22` había quedado «sin el registro que dice por qué es como es». Al retrodocumentarlo se vio que `validadores/docs/version.md` ya lo explicaba con ejemplos. Lo que no existía era una sola prueba.
- **Por qué importa:** cambia qué se pierde cuando alguien se salta la fase. La explicación se puede escribir después; la evidencia de que funcionaba el día que se escribió, no.
- **Estado:** resuelto acá — v21.3.1, fase `A-EP-004-HU-015`, cuatro casos contra las derogaciones reales del estándar.
- **Dónde queda:** [pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md](../../../pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md)
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-9 · Dos reglas que dicen casi lo mismo, y solo una baja de algún lado

- **Qué pasó:** al fijar el molde nuevo del §4 se escribieron las dos reglas del caso de `shopnest-mesa`. «Un problema **registra** causa raíz y solución» baja de `RF-13`; «un problema **no se cierra** sin causa raíz ni solución» no baja de ninguna parte. Con el molde viejo se veían igual de bien escritas.
- **Por qué importa:** es el argumento entero del pendiente 43 en dos líneas. La segunda llegó hasta un criterio de aceptación.
- **Estado:** resuelto acá — v22.0.0 el molde, v22.1.0 el validador.
- **Dónde queda:** [pendientes/hecho/el-origen-de-la-regla-de-negocio.md](../../../pendientes/hecho/el-origen-de-la-regla-de-negocio.md)
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-10 · Un `spec.md` no se comparaba contra ninguna plantilla

- **Qué pasó:** el validador de forma no sabía qué molde le correspondía a un archivo llamado `spec.md`, así que el documento más importante de un módulo era invisible para él. Se descubrió construyendo el validador del 43: sin arreglarlo, la comprobación nueva no se habría disparado nunca.
- **Estado:** resuelto acá — v22.1.0.
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-11 · El estándar no cumple la regla que acaba de escribir

- **Qué pasó:** el validador nuevo, corrido por primera vez sobre esta casa, encontró **31 reglas de negocio sin origen** — 16 en `automatismos/spec.md` y 15 en `documentos-modelo/spec.md`.
- **Por qué importa:** no se apagó la comprobación para que el número diera cero, pero mientras no se limpien, el estándar les exige a los proyectos algo que él no cumple.
- **Estado:** **anotado** → [pendiente 47](../../../pendientes/hecho/el-origen-de-las-reglas-de-negocio.md)
- **Nace en:** 2026-08-16 · sesión 7

### H-12 · Lo que faltaba no era dejar el planteamiento puesto: era decir que falta

- **Qué pasó:** la revisión de instalación decía «13 de 13, instalación completa» a un proyecto con código commiteado, `prompts/` vacía y ninguna épica. Ahora la lista tiene 14 puntos y el nuevo mira si la cadena de `02·F0` arrancó.
- **Qué se decidió:** entra como punto de la revisión y **no** lo instala el instalador — es el único así, y su fila lo dice. Copiar la plantilla del planteamiento con los marcadores crudos habría sido peor: parecería un planteamiento y la revisión lo daría por cumplido.
- **Estado:** resuelto acá — v23.0.0, fase `A-EP-007-HU-007`.
- **Dónde queda:** [pendientes/hecho/la-revision-ve-la-cadena.md](../../../pendientes/hecho/la-revision-ve-la-cadena.md)
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-13 · Esta casa tampoco tiene planteamiento

- **Qué pasó:** el punto nuevo, corrido contra el propio estándar, reprueba: `prompts/` tiene 40 archivos y ninguno es un planteamiento.
- **Por qué importa:** el trabajo del estándar también es desarrollo, así que `02·F0` le aplica igual. Ojo con leer mal el «6 de 14» que sale acá: el estándar no se instala a sí mismo y ocho de esos puntos no le corresponden. El de la cadena sí.
- **Estado:** **anotado** → [pendiente 56](../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md). Escribirlo es decidir qué es este proyecto, y eso sale de una conversación.
- **Nace en:** 2026-08-16 · sesión 7

### H-14 · El caso que «no puede correr el agente» corrió solo

- **Qué pasó:** el `CP-006` de la fase del glosario pedía un lector que no lo hubiera escrito, y llevaba dos ciclos sin ejecutarse. Se ejecutó el día que el usuario leyó el glosario para otra cosa, no entendió la entrada **Brief** y preguntó tres veces. Las tres preguntas eran, palabra por palabra, lo que el paso 4 del caso mandaba anotar.
- **Por qué importa:** un caso que depende de una persona no se marca «no ejecutable». Se deja escrito qué anotar cuando ocurra, porque ocurre.
- **Estado:** resuelto acá — el pendiente 27 cierra. Lo que faltaba el 2026-08-16 era más chico: la cabecera del resultado decía «ciclo 1» con el cuerpo ya en el ciclo 3.
- **Dónde queda:** [pendientes/hecho/el-veredicto-de-la-fase-a-de-hu-010.md](../../../pendientes/hecho/el-veredicto-de-la-fase-a-de-hu-010.md)
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-15 · La comprobación del veredicto llegó tarde a su propio caso

- **Qué pasó:** el programa que compara el `resultado_pruebas` con el `estado-fase` no encontró ninguna contradicción en el repositorio — porque la única conocida se había corregido unas horas antes, al cerrar el 27.
- **Por qué importa:** su valor no es lo que encuentra hoy. Es que la próxima no dependa de que alguien reescriba un resultado de pruebas y note la diferencia, que fue exactamente como se encontró esta.
- **Qué se decidió:** de las dos salidas del pendiente 28 se tomó la que **no cambia ningún molde**. La otra —que el `estado-fase` enlace en vez de copiar— obligaría a reescribir todas las fases cerradas; si algún día se hace, esta comprobación se retira.
- **Estado:** resuelto acá — v23.1.0.
- **Dónde queda:** [pendientes/hecho/un-solo-veredicto-por-fase.md](../../../pendientes/hecho/un-solo-veredicto-por-fase.md)
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-16 · Quince reglas figuraban sin clasificar estando clasificadas

- **Qué pasó:** el registro de lo validable decía `C1–C17`, un rango, y el programa que comprueba `20·M9` busca cada identificador literal. Quince reglas de conducta llevaban desde el 2026-08-05 apareciendo como sin clasificar.
- **Por qué importa:** cambia el diagnóstico del pendiente 19. Su tercera deuda no eran «33 que nadie clasificó»: eran **18 de verdad** y **15 mal escritas para quien las lee**. Y un hallazgo del que se duda se termina ignorando junto con los que sí eran ciertos.
- **Qué se decidió:** un documento que alimenta a un programa se escribe **como el programa lee**.
- **Estado:** resuelto acá — v23.1.1, las 33 a cero. Los capítulos `18` y `19`, que no aparecían ni una vez, quedaron clasificados: ser opt-in no exime.
- **Responde a:** el pendiente 19, que **sigue abierto** con sus otras dos deudas.
- **Nace y cierra en:** 2026-08-16 · sesión 7

### H-17 · Dos sesiones se pisaron el número de pendiente

- **Qué pasó:** esta sesión creó el pendiente `48` y otra sesión abierta al mismo tiempo creó otros dos con ese mismo número. Se le cedió el número y este se corrió al `52`.
- **Por qué importa:** es el [pendiente 22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md) —dos sesiones versionando a la vez— pasando en vivo, y ahora sobre el backlog en vez de sobre el `CHANGELOG`. Se resolvió a mano porque nada lo impide.
- **Estado:** **anotado** → suma su tercer caso al [pendiente 22](../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), que queda ampliado: lo que dos sesiones se pisan no es solo la versión, es cualquier numeración que se calcule mirando lo que ya existe.
- **Nace en:** 2026-08-16 · sesión 7

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2, H-3, H-8, H-9, H-10, H-12, H-14, H-15 y H-16 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ los cinco quedaron anotados: 53, 54, 55, 56 y el tercer caso del 22. El H-11 tiene el 47, y el punto 7 del 33 se promovió al 52 |
| Toda historia disparada está escrita en su épica | ☑ las siete del H-1 ya existían |
| Lo que se hizo está aprobado y guardado | ☑ v21.3.0 commiteada |

**La sesión se puede cerrar**, con dos cosas que quedan esperando al usuario y que **no la bloquean**, porque están anotadas y no se pierden:

- Qué se hace con las **siete reglas publicadas en «no cumple»** — es el `CA-01` del [19](../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que sigue abierto.
- La **contradicción del `P0`** en la cabecera del índice del backlog (H-7).

**De los ocho `P1` que dispararon la sesión, siete quedaron resueltos** —35, 38, 43, 30, 27, 28 y el punto 7 del 33, este último promovido al [52](../../../pendientes/hecho/el-sello-del-checklist-se-comprueba.md)—. El **19** cerró su parte mecánica y sigue abierto por las otras dos, que no dependen de trabajo sino de una decisión y de tiempo por capítulo.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
