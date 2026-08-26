# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-sesion-6.md](../../2026-08-22-sesion-6.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** 2026-08-22 · sesion-5 · H-4, el choque entre el molde de factibilidad y los cuatro frentes que la práctica evalúa. Sigue abierto.

---

## Hallazgos de esta sesión

### H-1 · La documentación se escribía desde lo construido, así que describía la limitación en vez del objetivo

- **Qué pasó:** el usuario cortó el avance con esto: *"el problema es que se está partiendo de lo que actualmente existe. La documentación debe partir de la propuesta y del objetivo que se quiere desarrollar"*.
- **Por qué importa:** una etapa escrita desde lo construido convierte cada carencia de hoy en un requisito de mañana. La decisión `DA-12` es la prueba: decía *"la pantalla solo lee"* porque la que existe solo lee, no porque alguien hubiera decidido que así fuera.
- **Qué lo soluciona:** se resolvió acá, reescribiendo las cuatro primeras etapas y dejando la exigencia en los siete moldes. No dispara historia.
- **Qué se decidió:** las etapas se escriben desde la propuesta, con la prueba del borrado mental: si mañana no existiera nada de lo construido, ¿el documento seguiría diciendo lo mismo? `DA-12` quedó al revés: *"la pantalla administra, y todo cambio queda firmado y registrado"*.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [cvds/](../../../cvds/) etapas 1 a 4, y la caja de redacción de los siete moldes de [plantillas/cvds/](../../../plantillas/cvds/).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-2 · Cimiento dejó de ser un cuerpo de reglas y pasó a ser una plataforma

- **Qué pasó:** el usuario definió el reparto: *"Cimiento = plataforma central de gestión, documentación, auditoría y gobierno de proyectos. Proyecto = software desarrollado y sus componentes técnicos necesarios para funcionar"*.
- **Por qué importa:** cambia qué se está construyendo. Las etapas anteriores describían un estándar que se hereda; ahora describen una aplicación que administra proyectos, guarda su documentación, la audita y genera los entregables. Sin ese giro escrito, la primera versión se habría construido contra el documento viejo.
- **Qué lo soluciona:** se partió en las tres épicas que abrieron el trabajo de la versión 1, ya escritas y aprobadas.
- **Qué se decidió:** análisis, diseño e implementación se escribieron para la plataforma: 32 funcionalidades, 12 decisiones de arquitectura, 18 entidades, 12 pantallas, y cinco versiones de producto con la primera repartida en siete fases.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:**
  1. [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) los proyectos se administran desde un solo lugar. Va primera: las otras dos dependen de que haya proyectos conectados.
  2. [EP-009](../../../documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/epica.md) todo lo que se hace queda registrado. Después de la anterior: no hay qué auditar sin proyectos.
  3. [EP-010](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/epica.md) lo escrito entra a la plataforma. Última: es la de mayor incertidumbre.
- **Orden de resolución:** —
- **Dónde queda:** [cvds/analisis-requisitos/](../../../cvds/analisis-requisitos/), [cvds/diseno/](../../../cvds/diseno/), [cvds/implementacion/](../../../cvds/implementacion/).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-3 · El texto es la fuente y la base es un índice, así que el respaldo es el repositorio

- **Qué pasó:** el usuario pidió que el respaldo fuera un script de base de datos versionado que se disparara solo con cada cambio. Al analizarlo salió que eso se atrasa, choca al fusionar y puede terminar publicando lo que no debe.
- **Por qué importa:** define de dónde sale la verdad. Es lo que la aplicación de `interfaz/` tiene al revés: guarda en la base y genera el texto desde ella, y por eso perder la base ahí sí pierde información.
- **Qué lo soluciona:** se resolvió acá como decisión de arquitectura, y la fase A la probó.
- **Qué se decidió:** la fuente es el texto, la base es un índice que se puede borrar entero y rehacer, y el respaldo es el propio control de versiones. Nada de volcados de base en el repositorio.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `DA-01` en [cvds/diseno/decisiones-de-arquitectura.md](../../../cvds/diseno/decisiones-de-arquitectura.md), y probado por CP-003 en la fase A.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-4 · Sin la palabra que diga qué se espera, el agente asumía y hacía lo que quería

- **Qué pasó:** el usuario lo dijo así: *"si escribo algo preguntando sobre algo, Cimiento de una asume que tiene que corregir cuando estoy es haciendo una pregunta"*.
- **Por qué importa:** asumir no falla una vez. Es lo que hace que una pregunta termine en un archivo cambiado, y el usuario se entere después.
- **Qué lo soluciona:** se resolvió acá por la cadena completa del capítulo 20, con su historia de usuario y su fase.
- **Qué se decidió:** toda petición abre con una de 18 palabras clave. Una palabra parecida no cuenta, y la palabra fija el máximo, no el mínimo.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [`01·C28`](../../../base/01-conducta.md) y su anexo [base/01-conducta/palabras-clave.md](../../../base/01-conducta/palabras-clave.md).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-5 · El validador encontró lo que dos lecturas no: una regla no puede depender de una blindada

- **Qué pasó:** `01·C28` se escribió declarando que extendía `00·N1`. Se leyó dos veces y pasó. `validar.py metareglas` la rechazó.
- **Por qué importa:** el repositorio tiene los validadores escritos, y el agente los corrió después de dar el trabajo por hecho, no antes. Leer no reemplaza correrlos.
- **Qué lo soluciona:** se resolvió acá quitando la dependencia y dejando escrito el porqué en el sello de la regla.
- **Qué se decidió:** [`20·M7`](../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) prohíbe depender de una regla blindada, así que `C28` no declara dependencia, y las dos filas de su lista de comprobación quedan como no aplica con su motivo escrito.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [base/01-conducta.md](../../../base/01-conducta.md), sello de `C28`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-6 · Todo se escribe en español colombiano, no en español a secas

- **Qué pasó:** el agente escribió *"una pieza"* y el usuario preguntó qué era. Después lo dejó fijo: *"todo debe ser escrito en español colombiano"*.
- **Por qué importa:** [`01·C8`](../../../base/01-conducta.md) pide el idioma del proyecto, y el agente lo cumplía a medias, con palabras que se entienden en otro país pero no acá. Depender de que el usuario lo repita cada sesión es lo mismo que no tenerlo.
- **Qué lo soluciona:** se resolvió acá, escribiéndolo como recuerdo del repositorio.
- **Qué se decidió:** *pieza* pasó a *componente*, se revisó el ciclo entero, y quedó como recuerdo con el caso que lo originó de evidencia.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [historico-chat/memory/espanol-colombiano.md](../../memory/espanol-colombiano.md), con su línea en el índice.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-7 · La fase A quedó construida y probada: la plataforma levanta, guarda y rehace su índice

- **Qué pasó:** el usuario decidió empezar de cero en vez de aprovechar `interfaz/`, y trabajar con el molde de estructura que el estándar ya tiene escrito para Django.
- **Por qué importa:** es la primera vez que el estándar produce código propio. Y la razón de empezar de cero es la de `H-3`: adaptar `interfaz/` obligaba a invertirle la fuente y cambiarle la base, que es casi reescribirla cargando lo viejo.
- **Qué lo soluciona:** se resolvió acá. Lo que falta de la versión 1 son las fases B a G, que ya están declaradas.
- **Qué se decidió:** los seis casos del plan de pruebas se corrieron y los seis pasaron. El de la red se hizo más estricto que lo planeado, tapando la salida desde adentro en vez de desconectar la máquina, y ese desvío quedó anotado en vez de corregir el plan aprobado. La aplicación de `interfaz/` no se tocó.
- **Estado:** resuelto acá.
- **Responde a:** [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) · [HU-001](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/HU-001-conectar-un-proyecto.md). Ningún criterio de aceptación: la fase A construye la base y la B los cumple.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [plataforma/](../../../plataforma/), y el cierre en [funcionalidad_implementada.md](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/A-EP-008-HU-001-la-plataforma-levanta-y-guarda/funcionalidad_implementada.md), con cuatro deudas declaradas.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-8 · Guardar lo que se hizo y guardar lo que se conversó son dos cosas distintas

- **Qué pasó:** el usuario pidió que las conversaciones completas entraran a la base, para sacar estadísticas y ver qué se repite. Eso chocaba con `RN-4` de la auditoría, aprobada el mismo día: se registra la acción, no la conversación.
- **Por qué importa:** el agente estuvo a punto de resolverlo cambiando la especificación aprobada y la regla. No hacía falta: eran dos cosas distintas. La auditoría responde qué se hizo y sirve para demostrar; el índice de conversaciones responde qué se conversó y sirve para descubrir. Y la razón que motivaba `RN-4` ya estaba resuelta: [validadores/historico.py](../../../validadores/historico.py) tapa las claves antes de escribir.
- **Qué lo soluciona:** se partió en dos historias, con la cadena completa desde el pendiente.
- **Qué se decidió:** `RN-4` se queda como está y la fase D no cambia. Lo nuevo entra como funcionalidad aparte, en la versión 2.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:**
  1. [EP-011 · HU-001](../../../documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md) buscar en lo conversado. Va primera: sin lo indexado no hay qué contar.
  2. [EP-011 · HU-002](../../../documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md) ver qué corrección se repite. Es la que da el valor.
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/85](../../../pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md), [EP-011](../../../documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md) y la señal `S-024`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-9 · El orden de las fases lo fija la versión, no la letra que sigue

- **Qué pasó:** cerrada la fase A, el agente marcó la B como abierta. La correcta era la D, la auditoría, por el orden aprobado en la etapa de implementación.
- **Por qué importa:** las épicas se numeran por tema y las fases por letra, y ninguna de las dos es el orden de ejecución. Ese vive en un tercer documento, y si nadie lo mira se ejecuta el orden que parece natural. Además la dependencia parecía circular, y se rompía con un caso vacío que la especificación ya contemplaba.
- **Qué lo soluciona:** se resolvió acá, corrigiendo la tabla y dejándolo dicho donde se va a leer.
- **Qué se decidió:** la fase D va antes que la B. El [índice de épicas](../../../documentacion/epicas/README.md) ahora lo advierte en una línea, y de paso quedó completo: le faltaban las cuatro épicas del producto.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) §5, el índice de épicas, y la señal `S-026`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-10 · El caso de «que NO pase» fue el único que encontró el defecto, y los otros seis estaban en verde

- **Qué pasó:** en la fase D, seis de los siete casos pasaron a la primera. `CP-007` falló: se podía escribir sin dejar constancia, y con eso `CA-01` no se cumplía.
- **Por qué importa:** los seis que pasaron probaban que la auditoría funciona, y todos entraban por la puerta correcta. Ninguno podía ver que existía un camino que la esquivaba. Corregirlo obligaba a tocar el almacén, que el plan no declaraba, así que la fase se detuvo y se presentaron dos opciones con su costo, en vez de arreglarlo callado (`02·F8`).
- **Qué lo soluciona:** se resolvió acá. El almacén ahora exige el comprobante que la auditoría emite al registrar, y ese comprobante solo vale para el archivo sobre el que se registró.
- **Qué se decidió:** cerrar el hueco ahora y no en la fase B, porque hoy no hay un solo llamador de esa función fuera de las pruebas. El usuario lo autorizó el 2026-08-25, y la ampliación quedó escrita con su nombre.
- **Estado:** resuelto acá.
- **Responde a:** [EP-009](../../../documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/epica.md) · [HU-001](../../../documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/HU-001-registrar-cada-accion.md) · los cinco criterios.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el `DEF-01` del [resultado de pruebas](../../../documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/resultado_pruebas.md), y las señales `S-027` y `S-028`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-11 · La especificación decidía cómo se comporta desconectar, y ninguna funcionalidad lo pedía

- **Qué pasó:** el usuario vio la primera pantalla y preguntó «pero eso no tiene administración?». Buscando la respuesta apareció que la especificación de Proyectos ya decidía, en su §7 y su §12, cómo se comporta desconectar, y que ningún requisito ni funcionalidad lo pedía. Su propia sección de alcance no lo nombraba.
- **Por qué importa:** una decisión escrita en una especificación no construye nada. Lo que baja a fase es el inventario. El documento quedaba prometiendo un comportamiento que ninguna fase iba a hacer, y el hueco no se veía leyendo: se vio usando el producto. El daño concreto era que **conectar no tenía reversa**, así que un proyecto mal conectado quedaba mal para siempre.
- **Qué lo soluciona:** se pidió por la cadena completa el mismo día, y entró a la versión 1 como fase H.
- **Qué se decidió:** entra a la versión 1 y no más tarde, porque mientras no exista, cada error al conectar se acumula. Es lo contrario del hallazgo `H-8`, que sí se pudo postergar sin perder nada.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** [EP-008 · HU-004](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md) administrar un proyecto conectado, como fase H de la versión 1.
- **Orden de resolución:** —
- **Dónde queda:** [pendientes/86](../../../pendientes/86-conectar-un-proyecto-no-tiene-reversa.md), `F-035`, la §15 de la [especificación de Proyectos](../../../documentacion/proyectos/spec.md), y la señal `S-029`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-12 · El guion de sabotaje restauraba con git, y el archivo saboteado no estaba versionado

- **Qué pasó:** al validar las pruebas de la fase B con cinco sabotajes, uno de los archivos se restauraba con el control de versiones. Era nuevo, no estaba versionado, y quedó saboteado. Se notó al final, cuando la corrida limpia salió en rojo.
- **Por qué importa:** el sabotaje existe para poder confiar en las pruebas. Un guion que no restaura bien hace lo contrario: deja el código roto y las pruebas fallando por otra razón. Si el paso final no hubiera corrido la suite completa, el sabotaje se iba dentro del commit.
- **Qué lo soluciona:** se resolvió acá, rehaciendo la evidencia con copias en vez del control de versiones.
- **Qué se decidió:** el sabotaje se restaura con copia del archivo, nunca con git, porque lo que se prueba suele ser código recién escrito. Y el guion siempre termina corriendo la suite completa.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la cabecera de [EV-02 de la fase B](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/B-EP-008-HU-001-se-conecta-un-proyecto/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), y la señal `S-030`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-13 · Un sabotaje que pasa en verde no siempre significa que falte una prueba

- **Qué pasó:** validando las pruebas de la fase H con seis sabotajes, uno pasó en verde. La lectura inmediata fue «falta una prueba». Era falso: ese sabotaje borraba la ficha y la reescribía enseguida, así que no cambiaba nada observable.
- **Por qué importa:** dar por bueno el diagnóstico fácil habría llevado a escribir una prueba que no protege de nada, y a creer que la suite es más fuerte de lo que es. El sabotaje mide las pruebas, y también hay que mirarlo a él.
- **Qué lo soluciona:** se resolvió acá, cambiando el sabotaje por uno que sí toca lo que la fase promete.
- **Qué se decidió:** cuando un sabotaje pasa en verde, la primera pregunta es si de verdad cambia el comportamiento, no si falta una prueba. Un sabotaje válido rompe algo observable desde afuera.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el comentario del guion en [EV-02 de la fase H](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), y la señal `S-031`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-14 · Una confirmación que no dice qué NO va a pasar obliga a adivinar

- **Qué pasó:** al construir la confirmación de desconectar un proyecto, la forma obvia era preguntar «¿seguro?». Lo que el usuario necesita saber antes de desconectar no es que se va a desconectar: es si va a perder su documentación.
- **Por qué importa:** una confirmación que solo dice qué va a pasar deja fuera justo lo que da miedo. El que no sabe si va a perder algo, o no confirma, o confirma cruzando los dedos. Ninguna de las dos es una decisión, y `00·N1` pide una decisión.
- **Qué lo soluciona:** se resolvió acá, en la pantalla de confirmación de la fase H.
- **Qué se decidió:** toda confirmación lleva dos listas: qué va a pasar y **qué NO**. Y se pregunta solo donde hay algo que perder o que recibir sin querer: conectar una carpeta nueva no pregunta, reconectar una que ya tuvo un proyecto sí. Preguntar por todo entrena a confirmar sin leer.
- **Estado:** resuelto acá.
- **Responde a:** [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) · [HU-004](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md) · `CA-04`.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la pantalla de confirmación de la fase H, y la señal `S-032`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-15 · Un sabotaje en verde tiene dos diagnósticos opuestos, y solo se distinguen corriendo el caso

- **Qué pasó:** en la fase C un sabotaje pasó en verde, igual que en la H. En la H el diagnóstico había sido «el sabotaje no saboteaba». Acá la respuesta fue la contraria: sí saboteaba, y lo que había era una prueba floja.
- **Por qué importa:** los dos casos se ven idénticos desde afuera —suite en verde con el código roto— y llevan a acciones opuestas. Mal diagnosticado, o se escribe una prueba que no protege de nada, o se deja pasar un defecto real.
- **Qué lo soluciona:** se resolvió acá, reforzando la prueba y dejando escrito cómo se distinguen.
- **Qué se decidió:** no se decide leyendo el código: **se corre el escenario y se mira el estado final**. Si quedó igual, el sabotaje era malo; si quedó distinto, la prueba era floja. Y la forma más común de prueba floja es mirar lo que devuelve la función en vez de lo que quedó guardado.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la prueba reforzada en la fase C, y la señal `S-033`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-16 · Una fase puede llegar medio construida por otra que no se lo proponía

- **Qué pasó:** al planear la fase C, dos de sus tres criterios ya estaban casi hechos. `ruta_viva` y el aviso salieron de la fase B, porque el modelo pedía la ruta viva como campo calculado. Ninguna de las dos fases estaba pensando en esta historia.
- **Por qué importa:** el riesgo no es haberlo construido antes, es **darlo por probado**. Ese código nunca se había ejecutado contra los criterios de la historia. Un plan que solo mirara lo nuevo habría cerrado la fase con dos criterios sin una sola prueba.
- **Qué lo soluciona:** se resolvió acá, declarándolo en el plan antes de empezar y probándolo igual.
- **Qué se decidió:** al abrir una fase se mira qué de sus criterios ya está construido por otras, se escribe en el plan, y **entra igual al plan de pruebas**: construido no es probado.
- **Estado:** resuelto acá.
- **Responde a:** [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) · [HU-002](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/HU-002-avisar-la-ruta-perdida.md).
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el plan de la fase C §2, y la señal `S-034`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-17 · La incertidumbre de una fase se mide antes de planearla, y a veces desaparece

- **Qué pasó:** la fase E era la de mayor incertidumbre declarada de la versión 1: la especificación decía que no se sabía cuánta documentación se iba a reconocer, y que se sabría probando. Antes de escribir el plan se contó sobre el repositorio real: 99,7% dentro de `documentacion/`, casi nada fuera.
- **Por qué importa:** con el número a la vista, la pregunta cambió. No era «cuánto se reconoce» sino «qué carpetas se recorren», y esa sí la podía decidir el usuario en un minuto. Y los tres archivos que no se reconocían resultaron ser **moldes que faltaban en la lista**, no casos raros: entraron como tarea de la fase en vez de aparecer en producción.
- **Qué lo soluciona:** se resolvió acá, midiendo antes de planear.
- **Qué se decidió:** traer recorre solo la documentación del ciclo, y **dice qué carpetas no miró y por qué**. El caso real entró con 973 documentos y ninguno afuera.
- **Estado:** resuelto acá.
- **Responde a:** [EP-010](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/epica.md) · [HU-001](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/HU-001-traer-un-proyecto.md).
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el plan de la fase E §2, con la tabla del conteo.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-18 · Copiar «tal cual» transformaba los saltos de línea, y el texto se veía idéntico

- **Qué pasó:** el módulo que trae documentación leía cada archivo con la apertura normal de texto, y Python traduce los saltos de línea al leer. Un documento escrito en Windows entraba transformado, incumpliendo el criterio que dice que nada se transforma.
- **Por qué importa:** es la clase de defecto que ninguna revisión encuentra, porque el documento se lee igual. Aparece después: en un control de versiones que marca 973 líneas como modificadas, o en una comparación que no cuadra.
- **Qué lo soluciona:** se resolvió acá, leyendo sin traducción y dejando el porqué escrito al lado.
- **Qué se decidió:** cuando algo promete copiar tal cual, la prueba compara **los bytes**, no el texto. Leer los dos lados con la misma función esconde exactamente las transformaciones que esa función hace.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el `newline=""` de `traer`, y la señal `S-036`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-19 · Un sabotaje que escribe fuera del código deja restos que restaurar no limpia

- **Qué pasó:** uno de los ocho sabotajes de la fase E hacía que traer escribiera un archivo **dentro del repositorio**. La prueba lo cazó y el guion restauró el código, pero el archivo que ese sabotaje alcanzó a escribir —973 líneas en la raíz— se quedó ahí, y el guion terminó diciendo que todo estaba bien.
- **Por qué importa:** restaurar con copia protege el código, no el mundo. La suite en verde no prueba que el sabotaje se deshizo: prueba que el código volvió a su sitio. Sin la línea de la corrida real que preguntaba por rastros, ese archivo se iba en el commit.
- **Qué lo soluciona:** se resolvió acá: el guion declara sus rastros, los limpia al terminar y dice qué limpió.
- **Qué se decidió:** antes de escribir un sabotaje, preguntarse **qué deja fuera del archivo que se sabotea**. Si escribe, borra o mueve algo, el guion tiene que declararlo y limpiarlo.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el guion de sabotaje de la fase E, y la señal `S-035`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-20 · Una fase puede probar todo lo que promete y no cumplir lo que declaró

- **Qué pasó:** la fase E declaraba que recorría «la documentación del ciclo de vida». Pasó nueve casos y ocho sabotajes, y cerró. Al planear la fase G apareció que no recorría las etapas del ciclo, que viven en otra carpeta, y que esa carpeta tampoco se declaraba como no mirada: se saltaba en silencio.
- **Por qué importa:** los nueve casos comprobaban que se trajera lo que se decía traer. Ninguno preguntaba **si lo que se decía traer era todo**. El sabotaje tampoco lo cubre, porque rompe el comportamiento y acá el comportamiento estaba bien: faltaba el alcance.
- **Qué lo soluciona:** se corrigió en la tarea 1 de la fase G, con su caso de prueba.
- **Qué se decidió:** cuando una fase declara que recorre o cubre algo, hace falta un caso que compruebe **el alcance**, no solo el comportamiento. Y la prueba más dura de una fase que produce datos es la siguiente que los consume.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la §5.1 del cierre de la fase E, que lo anota sin reabrirla, y la señal `S-037`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-21 · Lo que no se puede leer se cuenta aparte, no se reparte

- **Qué pasó:** para decir cuántas fases de un proyecto siguen abiertas hay que leer su estación. En este repositorio esa línea se escribe de **doce formas distintas**, y cinco no se dejan leer.
- **Por qué importa:** las dos salidas fáciles mienten. Contarlas como cerradas da 41 abiertas; como abiertas, 46. Ninguna es verdad, y las dos se ven igual de creíbles.
- **Qué lo soluciona:** se resolvió acá, con una tercera cuenta.
- **Qué se decidió:** la función devuelve **dos** valores —si está abierta, y si se pudo saber—, porque uno solo obliga a inventar una respuesta. Y las ilegibles se nombran con su ruta: un número sin decir cuáles no se puede corregir.
- **Estado:** resuelto acá.
- **Responde a:** [EP-008](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) · [HU-003](../../../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-003-ver-el-estado-de-un-proyecto/HU-003-ver-el-estado-de-un-proyecto.md).
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `_esta_abierta` en el cálculo del estado, y la señal `S-038`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ |
| Toda historia disparada está escrita en su épica | ☑ |
| Lo que se hizo está aprobado y guardado | ☐ |

Falta guardar la fase G. Lo anterior quedó en once commits, el último la fase E en `c998695`: la fase A en `26b2222`, la cadena de EP-011 en `7cfcf5d`, la fase D en `5231022` con su hash en `d261ab1`, y la fase B con la cadena de la HU-004 en `c1b9185`.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
