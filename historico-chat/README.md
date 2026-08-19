# Histórico de sesiones

Registro de lo que se hizo en cada sesión de chat con el agente. Sirve para retomar el trabajo sin releer el chat y para saber por qué quedó algo como quedó.

No es parte del estándar (`base/`, `plantillas/`, `skills/`); es bitácora, igual que `notas/`.

## Cómo se escribe

- Un archivo por sesión: `AAAA-MM-DD-tema.md` (si hay dos sesiones el mismo día, `AAAA-MM-DD-tema-2.md`).
- **La que cruza la medianoche se queda entera**, con la fecha del día en que empezó. El archivo es de una conversación, no de un día, y el enganche la busca por su marca de sesión — partirla dejaría media conversación sin marca y la siguiente sesión no la encontraría. Ya pasó: [2026-08-06-la-anatomia-de-la-regla.md](2026-08-06-la-anatomia-de-la-regla.md) tiene 91 turnos del 06 y **27 del 07**, y cada uno lleva su hora real. El resumen sí va al día en que pasaron las cosas.
- **El nombre se pone en la sesión, no al final.** El enganche crea `AAAA-MM-DD-sesion.md` porque al abrir el chat todavía no se sabe el tema; apenas hay una respuesta, le recuerda al agente que proponga nombre y resumen —una sola vez— y el usuario aprueba. El cambio lo hace el comando, que mueve el archivo, cambia el título y corrige la línea del índice a la vez:

  ```sh
  python "<estándar>/validadores/historico.py" --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"
  ```

  Con el comando, el agente pasa también la línea `/rename <tema>` para que la sesión de Claude Code —la pestaña, la barra del prompt, `/resume`— se llame igual que el archivo. Esa la pega el usuario: `/rename` es un comando suyo.
- **La escribe el programa, no el agente.** [`hook_historico.py`](../validadores/hook_historico.py) anota cada mensaje del usuario apenas lo envía y cada respuesta del agente apenas termina, con la hora del reloj, y le pone su línea al índice. Queda registrada desde el primer mensaje, aunque sea un "hola".
- **El agente no la escribe a mano.** Hacerlo la duplica —la misma conversación dos veces— y le mete horas estimadas donde el enganche puso las reales.
- Es la **transcripción** del diálogo, no un resumen: van los dos lados literales, con tablas, código y ejemplos. Lo único que no entra es la salida cruda de herramientas, que no es diálogo.
- Los pendientes reales siguen viviendo en `pendientes/`; aquí solo se apunta a ellos.
- **El resumen de la sesión va aparte, en [historico-chat/resumenes/README.md/](resumenes/README.md).** Es parte del histórico y por eso vive dentro, pero no se mezcla con la transcripción: aquella guarda lo que se dijo, el resumen guarda lo que quedó — los hallazgos, su estado y la pregunta que sigue viva.

## Plantilla

```markdown
# AAAA-MM-DD — Tema

## Conversación

### 1 · Usuario — AAAA-MM-DD HH:MM:SS
> La pregunta, literal.

**Agente** — AAAA-MM-DD HH:MM:SS
La respuesta condensada: qué se decidió, por qué, qué se descartó
y qué archivo se tocó.

### 2 · Usuario — AAAA-MM-DD HH:MM:SS
> La siguiente pregunta, literal.

**Agente** — AAAA-MM-DD HH:MM:SS
…

## Abierto
- Lo que quedó sin cerrar, o "nada".
```

## Índice

Cada línea es una sesión: primero su transcripción, y después del `·` el enlace a **lo que dejó**, si ya tiene resumen ([`resumenes/`](resumenes/README.md)). Para retomar un tema se arranca por el resumen; la transcripción se abre cuando el resumen no alcanza.

- [2026-08-06-historico-chat.md](2026-08-06-historico-chat.md) — se crea esta carpeta; queda el trabajo previo de despliegue y observabilidad (`base/18`, `base/19`). · [historico-chat/resumenes/2026-08-06/historico-chat.md](resumenes/2026-08-06/historico-chat.md)
- [2026-08-06-meta-reglas-2.md](2026-08-06-meta-reglas-2.md) — la regla de reglas (`base/00-meta-reglas.md`); formato del histórico: transcripción literal con marca de tiempo. · [historico-chat/resumenes/2026-08-06/meta-reglas-2.md](resumenes/2026-08-06/meta-reglas-2.md)
- [2026-08-06-el-torniquete-del-historico.md](2026-08-06-el-torniquete-del-historico.md) — el agente incumple la regla del histórico y nace el enganche que la ejecuta; de ahí salen el checklist y el stack de instalación. · [historico-chat/resumenes/2026-08-06/el-torniquete-del-historico.md](resumenes/2026-08-06/el-torniquete-del-historico.md)
- [2026-08-06-prueba-del-torniquete.md](2026-08-06-prueba-del-torniquete.md) — la prueba en vivo del enganche: un «hola» en una sesión nueva creó el archivo solo. · [historico-chat/resumenes/2026-08-06/prueba-del-torniquete.md](resumenes/2026-08-06/prueba-del-torniquete.md)
- [2026-08-06-la-anatomia-de-la-regla.md](2026-08-06-la-anatomia-de-la-regla.md) — el molde de cómo es una regla y el capítulo en carpeta; el barrido de candidatas, el sello de huella y las citas enlazadas (M15). · [historico-chat/resumenes/2026-08-06/la-anatomia-de-la-regla.md](resumenes/2026-08-06/la-anatomia-de-la-regla.md)
- [2026-08-06-no-se-puede-transcribir-audio.md](2026-08-06-no-se-puede-transcribir-audio.md) — el agente no recibe audio; transcribir lo hace un programa local y de ahí sale el texto. · [historico-chat/resumenes/2026-08-06/no-se-puede-transcribir-audio.md](resumenes/2026-08-06/no-se-puede-transcribir-audio.md)
- [2026-08-06-la-clase-del-diplomado-en-el-repositorio.md](2026-08-06-la-clase-del-diplomado-en-el-repositorio.md) — se transcriben doce imágenes de la clase a .md dentro del repositorio del estándar, donde no van. · [historico-chat/resumenes/2026-08-06/la-clase-del-diplomado-en-el-repositorio.md](resumenes/2026-08-06/la-clase-del-diplomado-en-el-repositorio.md)
- [2026-08-07-que-hace-el-agente-sin-ia.md](2026-08-07-que-hace-el-agente-sin-ia.md) — el inventario de lo que corre sin IA; nace anatomia/ con el mapa del sitio, y el backlog de 16 automatismos. · [historico-chat/resumenes/2026-08-07/que-hace-el-agente-sin-ia.md](resumenes/2026-08-07/que-hace-el-agente-sin-ia.md)
- [2026-08-07-la-carpeta-del-diplomado-sale-del-repositorio.md](2026-08-07-la-carpeta-del-diplomado-sale-del-repositorio.md) — el material de la clase se mueve fuera del estándar; mover carpetas ajenas no va al histórico. · [historico-chat/resumenes/2026-08-07/la-carpeta-del-diplomado-sale-del-repositorio.md](resumenes/2026-08-07/la-carpeta-del-diplomado-sale-del-repositorio.md)
- [2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md](2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md) — el análisis de cumplimiento, el capítulo 00 a carpeta, el checklist como estándar con su sello en cada regla, y M14. · [historico-chat/resumenes/2026-08-07/el-checklist-de-la-regla-y-la-carpeta-de-identidad.md](resumenes/2026-08-07/el-checklist-de-la-regla-y-la-carpeta-de-identidad.md)
- [2026-08-07-los-enganches-llegan-a-dos-proyectos.md](2026-08-07-los-enganches-llegan-a-dos-proyectos.md) — localhub y agro-system reciben el histórico corriendo el instalador; agro-system además queda sellado. · [historico-chat/resumenes/2026-08-07/los-enganches-llegan-a-dos-proyectos.md](resumenes/2026-08-07/los-enganches-llegan-a-dos-proyectos.md)
- [2026-08-07-reglas-con-expresiones-regulares.md](2026-08-07-reglas-con-expresiones-regulares.md) — qué parte de una regla puede comprobar un patrón y qué parte no; el texto es la regla, la regex es el candado. · [historico-chat/resumenes/2026-08-07/reglas-con-expresiones-regulares.md](resumenes/2026-08-07/reglas-con-expresiones-regulares.md)
- [2026-08-07-el-capitulo-02-al-molde.md](2026-08-07-el-capitulo-02-al-molde.md) — el capítulo del flujo pasa a carpeta y sus 19 reglas al molde (2.4.0 y 2.5.0); 10 reprueban el checklist y las F4.N se promueven a F14–F20. · [historico-chat/resumenes/2026-08-07/el-capitulo-02-al-molde.md](resumenes/2026-08-07/el-capitulo-02-al-molde.md)
- [2026-08-07-granularidad-de-la-fase.md](2026-08-07-granularidad-de-la-fase.md) — cuántos CA lleva una fase (F12.9 y F12.10) y dónde vive la dependencia entre CA. · [historico-chat/resumenes/2026-08-07/granularidad-de-la-fase.md](resumenes/2026-08-07/granularidad-de-la-fase.md)
- [2026-08-07-memoria-del-agente-en-el-repo.md](2026-08-07-memoria-del-agente-en-el-repo.md) — la memoria del agente pasa a `historico-chat/memory/`; el almacén de la herramienta queda vacío (`01·C19`, v3.0.0). · [historico-chat/resumenes/2026-08-07/memoria-del-agente-en-el-repo.md](resumenes/2026-08-07/memoria-del-agente-en-el-repo.md)
- [2026-08-07-por-que-pide-tanto-permiso.md](2026-08-07-por-que-pide-tanto-permiso.md) — las pantallas de permiso son por Bash, no por leer; y el commit que subió el trabajo de tres sesiones a la vez. · [historico-chat/resumenes/2026-08-07/por-que-pide-tanto-permiso.md](resumenes/2026-08-07/por-que-pide-tanto-permiso.md)
- [2026-08-07-instalacion-en-aspectos-legales.md](2026-08-07-instalacion-en-aspectos-legales.md) — el agente se instala en un proyecto del posgrado y se inicia git; queda 12 de 13 en el checklist. · [historico-chat/resumenes/2026-08-07/instalacion-en-aspectos-legales.md](resumenes/2026-08-07/instalacion-en-aspectos-legales.md)
- [2026-08-08-la-instalacion-se-hace-sola.md](2026-08-08-la-instalacion-se-hace-sola.md) — el CLAUDE.md pasa a ser el setup del agente: se quita el recuadro de pasos manuales y F13 deja de detener el arranque (5.0.0). · [historico-chat/resumenes/2026-08-08/la-instalacion-se-hace-sola.md](resumenes/2026-08-08/la-instalacion-se-hace-sola.md)
- [2026-08-08-la-documentacion-de-los-validadores.md](2026-08-08-la-documentacion-de-los-validadores.md) — 40 documentos en validadores/docs, uno por archivo, en lenguaje claro y con ejemplos de lo que retorna cada función. · [historico-chat/resumenes/2026-08-08/la-documentacion-de-los-validadores.md](resumenes/2026-08-08/la-documentacion-de-los-validadores.md)
- [2026-08-08-el-nombre-de-la-sesion-y-las-marcas-de-ia.md](2026-08-08-el-nombre-de-la-sesion-y-las-marcas-de-ia.md) — el histórico pide su nombre dentro de la sesión (6.1.0); nace ID8 y el anexo de las 62 marcas que delatan generación automática (7.0.0). · [historico-chat/resumenes/2026-08-08/el-nombre-de-la-sesion-y-las-marcas-de-ia.md](resumenes/2026-08-08/el-nombre-de-la-sesion-y-las-marcas-de-ia.md)
- [2026-08-08-escribir-para-que-lo-entienda-quien-no-sabe.md](2026-08-08-escribir-para-que-lo-entienda-quien-no-sabe.md) — nace ID7 y se deroga ID2 (6.0.0): todo lo que el agente escribe se entiende sin saber del tema, y se aplica a los 41 documentos de validadores. · [historico-chat/resumenes/2026-08-08/escribir-para-que-lo-entienda-quien-no-sabe.md](resumenes/2026-08-08/escribir-para-que-lo-entienda-quien-no-sabe.md)
- [2026-08-09-mensaje-sin-tema.md](2026-08-09-mensaje-sin-tema.md) — un mensaje suelto («fd») que no abrió ningún trabajo. · [historico-chat/resumenes/2026-08-09/mensaje-sin-tema.md](resumenes/2026-08-09/mensaje-sin-tema.md)
- [2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md](2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md) — nace 20·M16: ninguna regla de proyecto existe sin un criterio de la base que la respalde (8.0.0). · [historico-chat/resumenes/2026-08-12/regla-de-respaldo-de-las-reglas-de-proyecto.md](resumenes/2026-08-12/regla-de-respaldo-de-las-reglas-de-proyecto.md)
- [2026-08-13-del-brief-a-los-planes-de-la-fase-a.md](2026-08-13-del-brief-a-los-planes-de-la-fase-a.md) — nace el brief del agente y sus siete épicas; las ocho HU de EP-001 y la fase A de HU-001 con sus planes (8.0.1, 8.1.0, 8.2.0, 9.0.0). · [historico-chat/resumenes/2026-08-13/del-brief-a-los-planes-de-la-fase-a.md](resumenes/2026-08-13/del-brief-a-los-planes-de-la-fase-a.md)
- [2026-08-14-resultado-de-pruebas-y-cierre-de-fase.md](2026-08-14-resultado-de-pruebas-y-cierre-de-fase.md) — sigue la sesión anterior: el cierre verifica que el plan de trabajo se hizo, y la deuda técnica dice de dónde salió (9.1.0, 9.2.0). · [historico-chat/resumenes/2026-08-14/resultado-de-pruebas-y-cierre-de-fase.md](resumenes/2026-08-14/resultado-de-pruebas-y-cierre-de-fase.md)
- [2026-08-13-pendientes-del-diplomado-de-ia.md](2026-08-13-pendientes-del-diplomado-de-ia.md) — cinco pendientes (12–16) que salen de comparar los apuntes del diplomado de IA contra el estándar. · [historico-chat/resumenes/2026-08-13/pendientes-del-diplomado-de-ia.md](resumenes/2026-08-13/pendientes-del-diplomado-de-ia.md)
- [2026-08-13-hu-de-la-comprobacion-automatica.md](2026-08-13-hu-de-la-comprobacion-automatica.md) — las 12 HU de EP-004 y donde cae lo que falta del pendiente 01. · [historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md](resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md)
- [2026-08-14-plan-de-trabajo-de-la-ep-001.md](2026-08-14-plan-de-trabajo-de-la-ep-001.md) — el plan de trabajo de la EP-001: bajar sus HU a fases. · [historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md](resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md)
- [2026-08-14-molde-para-pedir-en-la-sesion.md](2026-08-14-molde-para-pedir-en-la-sesion.md) — analisis del prompt base del usuario: el molde obligatorio con que se le pide trabajo al agente. · [historico-chat/resumenes/2026-08-14/molde-para-pedir-en-la-sesion.md](resumenes/2026-08-14/molde-para-pedir-en-la-sesion.md)
- [2026-08-14-indice-tematico-del-historico.md](2026-08-14-indice-tematico-del-historico.md) — cargar el histórico al iniciar ya lo hace un hook; nace la idea de un índice por temáticas y qué manda entre el brief y el histórico. · [historico-chat/resumenes/2026-08-14/indice-tematico-del-historico.md](resumenes/2026-08-14/indice-tematico-del-historico.md)
- [2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md) — cerrar H-4 · No había dónde escribir lo aprendido: el resumen de sesión y su enganche. · [historico-chat/resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md)

<!-- huella: 8a05613563b8 · estandar 24.4.0 -->
- [2026-08-14-h-8-la-traduccion-quedo-a-medias.md](2026-08-14-h-8-la-traduccion-quedo-a-medias.md) — solución del hallazgo H-8: se abre la fase A de EP-003 · HU-010, el glosario de la terminología, con sus dos planes escritos y a la espera de aprobación. · [historico-chat/resumenes/2026-08-14/h-8-la-traduccion-quedo-a-medias.md](resumenes/2026-08-14/h-8-la-traduccion-quedo-a-medias.md)
- [2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md](2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md) — por qué lo de H-4 no funciona: el enganche nunca crea el resumen y la prueba lo dio por bueno. · [historico-chat/resumenes/2026-08-14/el-enganche-del-resumen-no-crea-el-resumen.md](resumenes/2026-08-14/el-enganche-del-resumen-no-crea-el-resumen.md)
- [2026-08-15-la-plantilla-del-resultado-de-pruebas.md](2026-08-15-la-plantilla-del-resultado-de-pruebas.md) — cada sección de la plantilla dice qué pregunta responde; aplicarla destapa que una fase cerrada no cumplía. · [historico-chat/resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md](resumenes/2026-08-15/la-plantilla-del-resultado-de-pruebas.md)
- [2026-08-15-los-resumenes-que-faltan.md](2026-08-15-los-resumenes-que-faltan.md) — el inventario del histórico: cuántas sesiones no tienen resumen y qué bloquea escribirlos. · [historico-chat/resumenes/2026-08-15/los-resumenes-que-faltan.md](resumenes/2026-08-15/los-resumenes-que-faltan.md)
- [2026-08-16-sesion.md](2026-08-16-sesion.md) — sesión del 2026-08-16.
- [2026-08-16-la-prioridad-de-los-pendientes.md](2026-08-16-la-prioridad-de-los-pendientes.md) — se analizaron los 28 pendientes abiertos y se les dio un orden de prioridad. · [historico-chat/resumenes/2026-08-16/la-prioridad-de-los-pendientes.md](resumenes/2026-08-16/la-prioridad-de-los-pendientes.md)
- [2026-08-16-que-pendientes-trabajamos.md](2026-08-16-que-pendientes-trabajamos.md) — qué hay que hacer con los P0 del backlog; se cierran el 39 y el punto 2 del 29. · [historico-chat/resumenes/2026-08-16/que-pendientes-trabajamos.md](resumenes/2026-08-16/que-pendientes-trabajamos.md)
- [2026-08-16-por-que-dice-instalacion-incompleta.md](2026-08-16-por-que-dice-instalacion-incompleta.md) — por que el checklist marca «falta» cuando lo que hay son copias viejas del estandar. · [historico-chat/resumenes/2026-08-16/por-que-dice-instalacion-incompleta.md](resumenes/2026-08-16/por-que-dice-instalacion-incompleta.md)
- [2026-08-16-un-pendiente-no-es-un-plan.md](2026-08-16-un-pendiente-no-es-un-plan.md) — el backlog se ejecutaba sin cadena, y por eso un arreglo se publico sin probarse. · [historico-chat/resumenes/2026-08-16/un-pendiente-no-es-un-plan.md](resumenes/2026-08-16/un-pendiente-no-es-un-plan.md)
- [2026-08-16-que-pendiente-sigue.md](2026-08-16-que-pendiente-sigue.md) — Consulta del backlog y ejecucion de los dos P0: el 42 y el 44. · [historico-chat/resumenes/2026-08-16/que-pendiente-sigue.md](resumenes/2026-08-16/que-pendiente-sigue.md)
- [2026-08-16-sesion-7.md](2026-08-16-sesion-7.md) — sesión del 2026-08-16.
- [2026-08-16-las-hu-sin-su-fase.md](2026-08-16-las-hu-sin-su-fase.md) — inventario de las 66 HU: 52 sin su fase completa, y la plantilla del tablero. · [historico-chat/resumenes/2026-08-16/las-hu-sin-su-fase.md](resumenes/2026-08-16/las-hu-sin-su-fase.md)
- [2026-08-16-el-inventario-de-hu.md](2026-08-16-el-inventario-de-hu.md) — el inventario de las HU sin fase: se renombra el pendiente 48, y la casilla Fase queda a la espera de una decision. · [historico-chat/resumenes/2026-08-16/el-inventario-de-hu.md](resumenes/2026-08-16/el-inventario-de-hu.md)
- [2026-08-17-retrodocumentar-ep-001.md](2026-08-17-retrodocumentar-ep-001.md) — los planes de trabajo de las siete HU de EP-001 que no tenían fase. · [historico-chat/resumenes/2026-08-17/retrodocumentar-ep-001.md](resumenes/2026-08-17/retrodocumentar-ep-001.md)
- [2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md](2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md) — se escribieron el plan de pruebas y el estado de fase de las 51 fases abiertas que no los tenian, y quedo a la vista que la mayoria esta bloqueada por dudas sin responder. · [historico-chat/resumenes/2026-08-17/plan-de-pruebas-y-estado-de-las-51-fases.md](resumenes/2026-08-17/plan-de-pruebas-y-estado-de-las-51-fases.md)
- [2026-08-17-sesion-3.md](2026-08-17-sesion-3.md) — sesión del 2026-08-17.
- [2026-08-17-sesion-4.md](2026-08-17-sesion-4.md) — sesión del 2026-08-17.
