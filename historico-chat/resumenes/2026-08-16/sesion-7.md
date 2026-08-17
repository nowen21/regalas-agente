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
- **Responde a:** el pendiente 35, cerrado en [hecho/renombrar-deja-el-resumen-coherente.md](../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md).
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
- **Estado:** **abierto** — falta crearle su pendiente.
- **Responde a:** —
- **Dispara:** —
- **Dónde queda:** §4 del [resultado de pruebas](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/resultado_pruebas.md) de la fase.
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** correr `validar.py estandar` sobre el repositorio y mirar cuántos validadores se pueden invocar solos.

### H-5 · Cerrar un pendiente rompe los enlaces que lo citaban

- **Qué pasó:** mover el archivo del 35 a `pendientes/hecho/` dejó 12 enlaces huérfanos. Nueve siguen rotos, en cuatro archivos que el plan de la fase no declaraba. **Y ya había pasado:** al cerrar el 45 quedó roto el enlace del `plan_trabajo` de su propia fase, y nadie lo vio.
- **Por qué importa:** es el mismo defecto que esta sesión acaba de cerrar para las sesiones renombradas, un piso más arriba. El backlog se cita a sí mismo —el 36 nombra al 34 y al 35, el 33 al 19 y al 31— y cada cierre rompe esas citas.
- **Qué lo soluciona:** lo mismo que el [punto 4 del pendiente 33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md): el modo de reparación de `citas.py`, aplicado también al mover un pendiente a `hecho/`.
- **Estado:** **abierto** — los nueve enlaces siguen rotos; el usuario decidió commitear antes de repararlos. Falta crearle su pendiente.
- **Responde a:** H-2
- **Dispara:** —
- **Dónde queda:** §4 del resultado de pruebas de la fase, y el punto 4 del 33 en el índice del backlog.
- **Nace en:** 2026-08-16 · sesión 7
- **Con qué se retoma:** los cuatro archivos están listados en el §3 del [estado de fase](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/estado-fase.md).

### H-6 · El validador de enlaces no respeta las comillas de código

- **Qué pasó:** marcó como rotas dos muestras escritas entre comillas invertidas dentro de un plan de pruebas, que nunca fueron enlaces sino el texto de lo que la prueba tiene que encontrar.
- **Por qué importa:** obliga a redactar torcido para que el validador no se queje, o enseña a ignorar sus hallazgos. Es de la misma familia que el punto 1 del 33, donde da por rotos los enlaces con espacios.
- **Qué lo soluciona:** que `enlaces.py` no busque enlaces dentro de un bloque ni de un tramo de código.
- **Estado:** **abierto** — falta crearle su pendiente. Conviene juntarlo con el punto 1 del 33: es el mismo archivo y la misma clase de falso positivo.
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

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2 y H-3 |
| Todo hallazgo abierto tiene su pendiente creado | ☐ **faltan tres**: H-4, H-5 y H-6 no tienen archivo propio todavía |
| Toda historia disparada está escrita en su épica | ☑ las siete del H-1 ya existían |
| Lo que se hizo está aprobado y guardado | ☑ v21.3.0 commiteada |

**La sesión no cierra todavía.** Faltan los tres pendientes del H-4, H-5 y H-6, y las cuatro decisiones del usuario (las tres del H-1 y la del H-7).

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_
