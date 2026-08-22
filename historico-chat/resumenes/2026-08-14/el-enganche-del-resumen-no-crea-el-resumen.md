# 2026-08-14 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md](../../2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md), con la plantilla [`plantillas/sesion.md`](../../../plantillas/sesion.md). La conversación está allá; acá queda lo que la sesión dejó.

Se anotan todos, resueltos y abiertos.

**Viene de:** 2026-08-14 · hu-de-la-comprobacion-automatica · [H-4 · No había dónde escribir lo aprendido](hu-de-la-comprobacion-automatica.md#h-4--no-había-dónde-escribir-lo-aprendido), reabierto en esta sesión.

---

## Hallazgos de esta sesión

### H-1 · El enganche del resumen no crea el resumen

- **Qué pasó:** el enganche de apertura busca la transcripción de la sesión para saber cómo llamar al resumen ([hook_resumen.py:52](../../../validadores/hook_resumen.py)), y en ese momento la transcripción todavía no existe: la escribe `hook_historico.py` en el primer mensaje del usuario. Sin transcripción se sale sin crear nada, y el modo de aviso tampoco crea: si el archivo no está, también se sale.
- **Por qué importa:** era la mitad de H-4, la que decía *"que el resumen exista aunque nadie se acuerde"*. Los dos resúmenes que hay en el repositorio los escribió el agente a mano, no el programa. La prueba de que no funciona es esta misma sesión: su transcripción existe y su resumen no apareció.
- **Qué lo soluciona:** reabrir la fase A de EP-005 · HU-008. La historia ya existe y sus tres criterios ya están escritos; lo que falla es lo construido, no lo pedido.
- **Qué se decidió:** el usuario decidió **no abrir una fase nueva**: se reabre la que cerró mal, porque su documentación decía que estaba hecho y corregirlo en otra carpeta la habría dejado mintiendo. El archivo pasa a nacer en el primer mensaje de la sesión, que es cuando ya existe la conversación de donde sale su nombre.
- **Estado:** resuelto acá, salvo la comprobación en una sesión real.
- **Responde a:** [EP-005 · HU-008 · CA-01](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md), el archivo nace solo.
- **Dispara:** —. Es arreglar lo que una fase dio por hecho.
- **Orden de resolución:** 1 de 3 · mientras no se cree el archivo, el aviso y el propósito tampoco pueden funcionar: los dos leen ese archivo.
- **Dónde queda:** la [fase A de HU-008](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md), reabierta, con su ampliación y su corrida 2 · versión 15.4.0.
- **Nace en:** 2026-08-14 · el-enganche-del-resumen-no-crea-el-resumen.
- **Cerrado en:** —
- **Con qué se retoma:** falta la única prueba que no se puede simular: abrir una sesión nueva en este repositorio y ver si el archivo aparece solo.

### H-2 · Seis de nueve pruebas pasaron sobre un mundo que el agente montó

- **Qué pasó:** el caso [CP-001](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/plan_pruebas.md) decía *"correr el enganche de `SessionStart`"* y lo que se corrió fue `crear(raiz, "2026-08-14-maracuya.md")`, con la transcripción inventada. CP-002, CP-004, CP-005, CP-006 y CP-007 parten del mismo supuesto: que el archivo del resumen ya existe. Como nadie lo crea, ese estado no ocurre nunca.
- **Por qué importa:** los tres criterios de la HU quedaron en cumple sin estar probados, y la fase cerró. Una prueba que se salta el disparador no prueba nada: deja exactamente el hueco por donde el programa falla.
- **Qué se decidió:** el usuario lo dijo con el ejemplo del arroz: el resultado de pruebas es probar el arroz que salió, no uno cocinado aparte. Se descartó escribir una regla nueva de pruebas: primero la solución. Lo que sí quedó es el molde. El detalle de cada caso pasa a tener cinco partes fijas —el problema que resuelve, la precondición, qué hacer para que cumpla, con qué reprueba y los pasos que se siguieron de verdad—, y si lo ejecutado no son esos pasos, el caso no cumple aunque haya salido bien.
- **Estado:** resuelto acá.
- **Responde a:** EP-005 · HU-008, sus tres CA.
- **Dispara:** —. Por decisión del usuario, la regla del capítulo de pruebas queda sin escribir.
- **Orden de resolución:** 2 de 3 · se cerró con la corrida 2, que reemplaza al veredicto viejo.
- **Dónde queda:** [`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`](../../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) · la corrida 2 y la anulación de la corrida 1, en el [resultado de pruebas de la fase](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/resultado_pruebas.md) · versión 15.4.0.
- **Nace en:** 2026-08-14 · el-enganche-del-resumen-no-crea-el-resumen.
- **Cerrado en:** 2026-08-14 · el-enganche-del-resumen-no-crea-el-resumen.
- **Con qué se retoma:** —

### H-3 · En un proyecto que hereda, el resumen no tiene ni carpeta ni modelo

- **Qué pasó:** el programa no crea nada si falta `historico-chat/resumenes/` ([resumen.py:86](../../../validadores/resumen.py)), y [`validadores/instalar.py`](../../../validadores/instalar.py) nunca crea esa carpeta. Además, el encabezado que el programa escribe enlaza a `plantillas/sesion.md` con una ruta relativa que solo existe en este repositorio.
- **Por qué importa:** el estándar se hereda. Un proyecto instalado hoy recibe los dos enganches en su configuración, y los dos quedan mudos: exigen un paso a mano que nadie le dijo a nadie.
- **Qué lo soluciona:** que el instalador deje la carpeta puesta, como ya deja el histórico y la memoria, y que el encabezado del resumen apunte a algo que sí viaja al proyecto.
- **Qué se decidió:** se resolvió en la misma fase reabierta. El instalador deja la carpeta con su índice, y el encabezado del resumen enlaza el índice del histórico del propio proyecto, que sí viaja. La decisión vieja, *"el enganche no crea el resumen si no hay carpeta del día"*, se conserva: lo que cambia es que la carpeta llegue instalada.
- **Estado:** resuelto acá.
- **Responde a:** [EP-005 · HU-008 · CA-01](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md).
- **Dispara:** —
- **Orden de resolución:** 3 de 3 · sin lo de H-1 resuelto, instalar la carpeta no cambiaba nada.
- **Dónde queda:** [`validadores/instalar.py`](../../../validadores/instalar.py) y [`validadores/resumen.py`](../../../validadores/resumen.py) · versión 15.4.0.
- **Nace en:** 2026-08-14 · el-enganche-del-resumen-no-crea-el-resumen.
- **Cerrado en:** 2026-08-14 · el-enganche-del-resumen-no-crea-el-resumen.
- **Con qué se retoma:** —

### H-4 · Cimiento no cumple sus reglas porque no le llegan

- **Qué pasó:** al ofrecerle al usuario dos salidas donde [`02·F9`](../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md) manda reportar un hallazgo, se fue a mirar por qué. [`validadores/cargador.py`](../../../validadores/cargador.py) manda completo lo que empieza por `00-` y `01-`, 73 KB de 369, y todo lo demás llega como una línea de índice. El capítulo `02`, que gobierna cada movimiento de una fase, nunca llega escrito.
- **Por qué importa:** la línea del índice no sirve para cumplir. La de `F9` dice *"si el volumen amerita subfases, se proponen antes de aprobar"*, y lo que se incumplió fue *"se reporta como hallazgo derivado, no como opción a elegir"*, que solo está en el texto de la regla. Y le pasa igual a cualquier proyecto que herede a Cimiento: es el mismo programa el que carga.
- **Qué lo soluciona:**

  **EP-005 · HU nueva — la regla llega en el momento en que rige**
  - **Como** quien confía en que el agente cumple las reglas
  - **Quiero** que el texto del capítulo que gobierna lo que se está haciendo le llegue completo en ese momento
  - **Para** que no incumpla una regla que nunca leyó
  - **Contexto:** hoy van literales 3 KB de 369; el resto son títulos. Cargarlo todo no cabe, y cargar solo el índice ya se probó que no basta. El disparador existe: el enganche que corre al escribir un archivo sabe qué archivo es, así que al escribir un plan o un resultado de pruebas puede llegar el capítulo del flujo. Falta decidir qué capítulo va con qué archivo, y medir cuánto crece el arranque.

  **EP-004 · HU nueva — comparar el plan aprobado con lo que se hizo**
  - **Como** quien aprueba un plan
  - **Quiero** que un programa avise cuando lo hecho no es lo que el plan decía
  - **Para** no tener que revisarlo yo documento por documento
  - **Contexto:** las doce historias de EP-004 comprueban documentos contra su molde; ninguna compara dos documentos entre sí. Lo comparable ya está: los archivos que el plan declara contra los que cambiaron, los casos del plan contra los del resultado, los criterios contra sus casos ejecutados. Es comparar listas, no juzgar.
- **Qué se decidió:** al abrir la primera historia se verificó el programa y **la premisa era falsa**: el reparto ya mandaba completos `00` y `01` desde la versión 5.0.0, así que `ID8` llegaba entera y se incumplió igual. Con eso cambió todo el orden: que la regla llegue no alcanza, y lo que falta de verdad es el capítulo `02` y comprobar lo entregado. La primera historia pasó de construir a **retro-documentar** lo que ya corría, y su fase cerró el 2026-08-15.
- **Estado:** abierto.
- **Responde a:** EP-001 · HU-004, las reglas de conducta de la IA.
- **Dispara:**
  1. **[EP-005 · HU-009](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md) — lo que gobierna cada frase llega puesto.** Escrita, y **cerrada el 2026-08-15**: resultó que ya funcionaba, así que su fase documentó y probó lo que existía.
  2. **[EP-005 · HU-010](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md) — el capítulo que rige lo que se escribe llega al escribirlo.** Escrita, sin fase. Es la que evita lo que pasó con `F9`.
  3. **[EP-004 · HU-013](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md) — comparar el plan aprobado con lo que se hizo.** Escrita, sin fase. Sube de importancia: una regla que llega completa igual se incumple, y esto es lo único que lo caza.
  4. **[EP-005 · HU-003](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md), que ya existía:** se le agregó lo que le faltaba, `RN-06`, `RN-07` y `CA-03`, que dicen cuál hallazgo detiene y cuál solo avisa. No sale de este hallazgo; lo bloquea, porque sin eso lo que encuentre la comparación se queda en un mensaje.
- **Orden de resolución:** 1 de 1 · es el único abierto que no depende de nada.
- **Dónde queda:** las tres historias en sus épicas · la [fase A de HU-009](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/README.md), cerrada · el [pendiente 25](../../../pendientes/hecho/las-reglas-de-como-se-escribe-si-llegaban-puestas.md), cerrado por falso · versión 15.4.3.
- **Nace en:** 2026-08-14 · el-enganche-del-resumen-no-crea-el-resumen.
- **Cerrado en:** —
- **Con qué se retoma:** bajar `HU-010` a fase. Y la pregunta que dejó la verificación: si una regla que llega completa igual se incumple, ¿qué la hace cumplir? Lo único probado hasta hoy es que alguien lo vea y quede escrito.

---

## ¿Se puede cerrar la sesión?

**Sí.** Las cuatro condiciones están cumplidas.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2 y H-3 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-1 vive en la [fase A de HU-008](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md), detenida con su caso `CP-018` escrito. H-4 no necesita pendiente: sus tres historias ya están en sus épicas |
| Toda historia disparada está escrita en su épica | ☑ las tres de H-4, en EP-004 y EP-005 |
| Lo que se hizo está aprobado y guardado | ☑ `6391e79` y `cd94e5b`, los dos subidos |

**El propósito se cumplió a medias, y a propósito.** Lo que se vino a arreglar quedó arreglado y probado: el resumen nace solo, el instalador deja la carpeta y los enlaces no nacen rotos. Lo que falta no se puede hacer hoy: **abrir una sesión nueva y ver si el archivo aparece solo**. Eso es `CP-018`, y hasta que pase, la fase de HU-008 no cierra y H-1 se queda sin su «cerrado en».

**Lo que la sesión deja para la próxima**, en orden:

1. Mirar si el resumen de la sesión nueva apareció solo. Si sí, cierran `CP-018`, la fase de HU-008, H-1 y el H-4 del 2026-08-14 que se reabrió acá.
2. Bajar a fase [EP-005 · HU-010](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md), que es la que evita lo que pasó con `F9`.
3. Después [EP-004 · HU-013](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md), que es lo único que caza una regla incumplida habiendo llegado completa.
