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

### H-22 · Donde una funcionalidad no hace nada es donde más falta hace que deje constancia

- **Qué pasó:** al traer un proyecto donde **nada** se reconocía, el módulo se salía temprano sin escribir el reporte ni dejar registro en la auditoría. Alguien traía, no entraba nada, y no quedaba rastro de que se hubiera intentado.
- **Por qué importa:** la salida temprana parece razonable y es al revés. Un usuario que trae y no ve nada necesita saber si la plataforma falló, si la carpeta estaba vacía, o si nada seguía un molde. Sin reporte, las tres se ven igual.
- **Qué lo soluciona:** se resolvió acá: traer sin que entre nada también es una traída, y deja las dos cosas.
- **Qué se decidió:** una salida temprana por «no hay nada que hacer» se mira dos veces. Si la función deja constancia o reporte, **el caso vacío también tiene que dejarlo**. Y las pruebas necesitan un caso donde el resultado sea cero.
- **Estado:** resuelto acá.
- **Responde a:** [EP-010](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/epica.md) · [HU-002](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-002-reportar-lo-no-reconocido/HU-002-reportar-lo-no-reconocido.md).
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el comentario en `traer`, y la señal `S-039`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

### H-23 · Un registro que dice cuántos sin decir cuáles no demuestra nada

- **Qué pasó:** después de traer 994 documentos, el registro de auditoría decía «994 reconocidos, 1 sin reconocer». Para saber cuál era había que volver a traer el proyecto entero.
- **Por qué importa:** un número es un resumen, y un resumen no es una prueba. La auditoría existe para rastrear cualquier cambio hasta su origen, y ahí el rastro se cortaba en el propio registro.
- **Qué lo soluciona:** se resolvió acá, con el reporte como documento propio y el registro enlazándolo.
- **Qué se decidió:** cuando un registro resume algo con detalle, el detalle va **en un documento aparte y el registro lo enlaza**. No se copia en los dos sitios. Meter la lista en el registro se descartó: un proyecto que siga el estándar a medias dejaría cientos de rutas y el registro quedaría ilegible justo cuando más falta hace.
- **Estado:** resuelto acá.
- **Responde a:** [EP-010](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/epica.md) · [HU-002](../../../documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-002-reportar-lo-no-reconocido/HU-002-reportar-lo-no-reconocido.md).
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el reporte enlazado desde el registro, y la señal `S-040`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-24 · La estación del commit casi nunca se marca, y el estado del proyecto sale falso

- **Qué pasó:** la plataforma calculó el estado de este repositorio y dijo **41 fases abiertas**. Al mirarlas una por una, **23 estaban cerradas de hecho**: su documento de cierre lleva tiempo guardado en git. Lo abierto de verdad son **17**.
- **Por qué importa:** un 58% de error en el único número que dice cuánto trabajo hay colgando. Y crece: la estación 9 es el commit, que ocurre **después** de que el agente termina de escribir, así que nadie vuelve al `estado-fase.md` a marcarla.
- **Qué lo soluciona:** se corrigieron las 23, con el hash sacado de `git log` sobre su propio documento de cierre — no de una suposición. Que no vuelva a pasar quedó anotado.
- **Qué se decidió:** se tocó **solo** `estado-fase.md`. Los documentos de cierre son de un molde anterior sin fila de commit: no mienten, simplemente no registran ese dato, y agregarles una fila sería reescribir un documento cerrado para meterle algo que su molde no pedía.
- **Estado:** resuelto acá lo de las 23; anotado lo de que se repita.
- **Responde a:** —
- **Dispara:** [pendiente 87](../../../pendientes/87-la-estacion-del-commit-casi-nunca-se-marca.md), con las tres salidas posibles sin elegir por el usuario.
- **Orden de resolución:** —
- **Dónde queda:** los 23 `estado-fase.md`, cada uno diciendo de dónde salió su hash.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-25 · Un validador que lo recorre todo termina juzgando lo que no es suyo

- **Qué pasó:** la plataforma trajo 1005 documentos de un proyecto al repositorio, y los validadores del estándar los revisaron como documentación propia: **3840 enlaces rotos**. Ninguno lo estaba — son enlaces relativos que resuelven en el proyecto de origen.
- **Por qué importa:** la pregunta que abrió esto parecía de arquitectura — «¿lo traído se versiona?» — y no lo era. Ya estaba decidido: `DA-02` dice que **se clona la plataforma y está todo**, y `DA-10` aceptó la duplicación como costo declarado. Lo que faltaba decidir era **hasta dónde llega un validador**.
- **Qué lo soluciona:** se resolvió acá. Los tres recorridos que llegaban hasta ahí saltan `plataforma/datos/`.
- **Qué se decidió:** se salta por **ruta**, no por nombre. Saltar toda carpeta llamada `datos` escondería documentación de verdad: cualquier proyecto puede darle ese nombre a una carpeta suya. Se comprobó apagando el filtro: 3840 con él apagado, 0 con él puesto.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `EXCLUIDAS_POR_RUTA` y `es_dato_de_la_plataforma` en [validadores/comun.py](../../../validadores/comun.py), y la señal `S-041`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-26 · Arreglar un validador dejó una prueba comprobando el rechazo en vez de la regla

- **Qué pasó:** la prueba de que «una regla nueva sin clasificar se avisa» fallaba. No por la regla: al cerrarse el pendiente 81, `metareglas` dejó de juzgar carpetas que no son el estándar, y el árbol de mentira de la prueba **no lo parecía**. El validador respondía «esta carpeta no es el estándar» y la prueba comprobaba esa negativa.
- **Por qué importa:** la prueba seguía existiendo con su nombre intacto, así que leía como cobertura de algo que había dejado de comprobarse.
- **Qué lo soluciona:** se resolvió acá: el árbol de la prueba ahora trae `VERSION`, que es lo que `es_el_estandar` mira junto con `base/`.
- **Qué se decidió:** se corrigió **la prueba**, no el guárdian. El rechazo es correcto y es justo lo que pedía el pendiente 81.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el comentario junto al árbol de mentira, en [validadores/pruebas.py](../../../validadores/pruebas.py).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-27 · El inventario de historias contado a mano lleva 34 de retraso

- **Qué pasó:** el [pendiente 48](../../../pendientes/48-inventario-hu.md) dice **78 historias, 47 completas, 31 incompletas**. El programa cuenta **112, 69 y 43** sobre el árbol real. La prueba que compara los dos números es la que lo dijo.
- **Por qué importa:** el propio pendiente existe porque una cuenta a mano se desactualiza el día que alguien cierra algo y no vuelve ahí. Volvió a pasar, y esta vez con las cuatro épicas de la plataforma enteras por fuera.
- **Qué lo soluciona:** se resolvió acá, y **no corrigiendo los números**. Corregirlos habría movido la fecha del próximo desfase: el pendiente existía porque una cuenta a mano se desactualiza. Se le quitó la cuenta y la tabla, y ahora remite al comando que las calcula.
- **Qué se decidió:** no tocarlo de paso, y bajarlo por la cadena: `EP-004` · `HU-019` · fase `A`. **Que un programa reescribiera la tabla se descartó**: `EP-004 §10.2` dice que los programas reportan y no corrigen, y además dejaría dos copias con alguien teniendo que acordarse de correrlo.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** la [HU-019](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-019-inventario-que-no-se-mantiene-a-mano/HU-019-inventario-que-no-se-mantiene-a-mano.md), construida y cerrada el 2026-08-26.
- **Orden de resolución:** se pensó que dependía del pendiente 87, y **no dependía**: `fases.inventario` cuenta documentos presentes, no estaciones marcadas. Encadenarlos fue un error mío, corregido al verificarlo.
- **Dónde queda:** el pendiente [48](../../../pendientes/48-inventario-hu.md), de 148 líneas a 83, y `cuenta_escrita_a_mano` en [validadores/fases.py](../../../validadores/fases.py).
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-28 · Anidar la documentación de un proyecto dentro de otro la empuja fuera del tope de Windows

- **Qué pasó:** al guardar lo traído, `git add` se negó con **`Filename too long`**. El prefijo `plataforma/datos/proyectos/<identificador>/traido/` le suma 54 caracteres a cada ruta, y eso puso **59 archivos** por encima del tope de 260 de Windows — el más largo, **307**. En su sitio de origen las mismas rutas caben.
- **Por qué importa:** el que se pasa no es un archivo, es **la suma**: carpeta de historia con nombre descriptivo, más carpeta de fase que repite el identificador, más el prefijo. Cada tramo es razonable por separado. Y no salta al escribir —la plataforma copió los 1005 sin quejarse— sino **al guardar**, cuando ya estaba todo lo demás decidido.
- **Qué lo soluciona:** se resolvió acá, por la cadena: `EP-007` · `HU-009` · fase `A`. **El instalador lo deja puesto**, sin pisar un `false` que alguien haya decidido y sin tocar la configuración de la máquina.
- **Qué se decidió:** dejarlo escrito en el commit y en la señal en vez de darlo por resuelto. **No lo está del todo:** es configuración local, así que quien clone en Windows tiene que activarla o le faltarán esos 59 archivos — justo lo que `DA-02` promete al decir que se clona la plataforma y está todo.
- **Estado:** resuelto acá lo que se puede resolver. **Lo de quien clone y no instale no tiene arreglo desde el repositorio**, y por eso quedó escrito qué hacer en el documento de despliegue.
- **Responde a:** —
- **Dispara:** la [HU-009](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-009-las-rutas-largas-no-detienen-el-guardado/HU-009-las-rutas-largas-no-detienen-el-guardado.md), construida y cerrada el 2026-08-26. **Acortar nombres se descartó midiendo**: la holgura del peor caso son 8 caracteres y anidar necesita 55; acortar la convención ahorra 14. Ninguna combinación crea los 55 que faltan.
- **Orden de resolución:** —
- **Dónde queda:** `_rutas_largas` en [validadores/instalar.py](../../../validadores/instalar.py), la §3.1 del documento de [despliegue](../../../cvds/despliegue/README.md), y las señales `S-042` y `S-051`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Y algo mayor que apareció al medir:** este repositorio ya está al borde **en su propio sitio**, sin plataforma de por medio. Su ruta más larga mide **252 de 260**, y **81 archivos** están a menos de 55 del tope. La carpeta de fase repite el identificador de la épica y de la historia que ya vienen en las dos carpetas de encima. Anidar solo reveló el problema; no lo causó.
- **Con qué se retoma:** —

---

### H-29 · Una comprobación puede estar bien escrita y no estar conectada, y sus pruebas no lo notan

- **Qué pasó:** la fase construyó una comprobación con seis pruebas encima. Un sabotaje la **descolgó de la corrida** —le quitó la llamada desde `validar`— y **las seis siguieron en verde**. La función existía, funcionaba, y por el comando que la gente corre no salía nada.
- **Por qué importa:** las seis la llamaban **directo**, que es lo natural al escribirlas: se prueba lo que se acaba de escribir. Ninguna preguntaba si alguien la llama. Es un modo de fallar que las pruebas de la propia función **no pueden ver por construcción**.
- **Qué lo soluciona:** se resolvió acá, con una prueba que busca el aviso **a través de `validar`**, no llamando a la función.
- **Qué se decidió:** que toda comprobación nueva lleve una prueba que la busque **por el punto de entrada de verdad**. Y que la forma de descubrir que falta es **sabotear la conexión, no el cuerpo**.
- **Estado:** resuelto acá.
- **Responde a:** [EP-004](../../../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) · HU-019.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `test_el_aviso_sale_en_la_corrida_de_fases` y la señal `S-043`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-30 · El guion de sabotaje dijo «suite completa en verde» sin haber corrido una sola prueba

- **Qué pasó:** el guion termina corriendo la suite entera, que es lo que dice si algo quedó saboteado. Usaba `unittest discover`, **encontró cero pruebas**, y reportó `OK`. La salida decía `Ran 0 tests in 0.000s` seguida de `OK`.
- **Por qué importa:** el veredicto que cierra una fase salía de una corrida vacía. **Cero pruebas y `OK` se ven igual**, y el guion existe justamente para no confiar en que las pruebas sirven: que él mismo mintiera es el mismo error un nivel más arriba.
- **Qué lo soluciona:** se resolvió acá: lanza el programa en vez de `discover`, y **se cae con error si la corrida final dice `Ran 0`**.
- **Qué se decidió:** que una corrida de pruebas se valida por **dos** cosas, no una: que no haya fallas **y que haya corrido algo**.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la señal `S-044`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-31 · La plantilla del inventario sigue enseñando el defecto que el estándar acaba de quitarse

- **Qué pasó:** al reescribir el pendiente del inventario apareció que [`plantillas/inventario-hu.md`](../../../plantillas/inventario-hu.md) sigue describiendo la tabla a mano que acá se quitó.
- **Por qué importa:** **un proyecto que herede el estándar arma su inventario a mano**, con el mismo defecto que este repositorio acaba de dejar atrás después de que se le desfasara tres veces. El estándar estaría repartiendo lo que él mismo dejó de hacer.
- **Qué lo soluciona:** se resolvió acá, por la cadena: `HU-020` y su fase `A`. La plantilla remite al comando en vez de pedir la cuenta, y el estándar subió a `34.2.0`. **Y apareció una segunda mitad que nadie había declarado:** la comprobación que impedía que la copia volviera miraba `pendientes/48-inventario-hu.md` escrito fijo, así que en un proyecto no veía nada. La guardia protegía al estándar y a nadie más.
- **Qué se decidió:** reportarlo en vez de tocarlo de paso, y bajarlo por la cadena. La segunda mitad no se descubrió leyendo: salió de preguntarse, al abrir la historia, **si un proyecto podía siquiera correr el comando**. La pregunta era sobre otra cosa.
- **Estado:** resuelto acá.
- **Responde a:** [EP-004](../../../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) · HU-020.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** [plantillas/inventario-hu.md](../../../plantillas/inventario-hu.md) reescrita, `CARPETAS_DEL_INVENTARIO` en [validadores/fases.py](../../../validadores/fases.py), y la señal `S-045`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-32 · El mismo defecto tiene dos formas, y una sola expresión no caza las dos

- **Qué pasó:** la comprobación busca el rótulo de la cuenta **con un número al lado**, porque en un inventario de verdad el defecto es un número escrito. Un sabotaje devolvió el campo a la **plantilla** y la suite quedó en verde: ahí el mismo defecto viene como `«N»`, el hueco por llenar. Sin número, no había coincidencia.
- **Por qué importa:** era invisible **justo en el archivo donde más caro sale**. La plantilla es la que se copia, así que un defecto ahí se multiplica por cada proyecto que la use.
- **Qué lo soluciona:** se resolvió acá, con una prueba que en la plantilla busca **el rótulo como campo, valga lo que valga**.
- **Qué se decidió:** **no** aflojar la expresión. Que el inventario de verdad exija un número es correcto: su narrativa tiene cifras y marcarlas volvería el aviso ruido. Son dos comprobaciones con dos formas, no una mal escrita.
- **Estado:** resuelto acá.
- **Responde a:** [EP-004](../../../documentacion/epicas/EP-004-comprobacion-automatica/epica.md) · HU-020.
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `test_la_plantilla_no_trae_campos_de_cuenta` y la señal `S-046`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-33 · «No dupliques lo derivable» no aplica a un hecho histórico

- **Qué pasó:** al cerrar la fase anterior se escribió, en «Versión del estándar al cerrar», **«la que declara `VERSION`»** en vez del número. Al subir `VERSION` a `34.2.0` una hora después, ese cierre pasó a afirmar que cerró bajo una versión **que no existía cuando cerró**.
- **Por qué importa:** es el error **inverso** al que se acababa de arreglar, cometido por aplicar bien la regla en el sitio equivocado. La cuenta de historias es derivable y el puntero la mejora; **la versión al cerrar es una foto**, y el puntero la falsifica el día que la fuente cambia.
- **Qué lo soluciona:** se resolvió acá. Se paró, se reportó, **el usuario autorizó ampliar el plan**, y se corrigió. El cierre dice ahora `34.1.0`, con la nota de por qué cambió.
- **Qué se decidió:** parar y pedir permiso antes de tocar, aunque fuera una línea y estuviera claro que había que corregirla. **El orden importa**: no se editó primero para pedir perdón después.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** el cierre de la `HU-020` §6, y la señal `S-047`.
- **Nace en:** 2026-08-22 · sesion-6
- **Cerrado en:** 2026-08-22 · sesion-6
- **Con qué se retoma:** —

---

### H-34 · Se citó cuatro veces una historia como «abierta» sin leer su estado, y estaba cerrada

> **Este hallazgo decía otra cosa hasta el 2026-08-26**, y lo que decía era falso. Se deja reescrito, no borrado: el error importa más que la conclusión que traía.

- **Qué pasó:** cuatro fases seguidas declararon no llevar especificación aparte, y las cuatro lo justificaron diciendo que la [EP-001 · HU-010](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) **estaba abierta esperando escribir esa regla**. Sobre eso se levantó este hallazgo, que concluía «cuatro ya no es un caso suelto: es la regla que falta». **Esa historia dice `Estado: Done`**, cerró el 2026-08-18, y su pendiente está en `hecho/`.
- **Por qué importa:** cerró **diciendo lo contrario**: «nada nuevo, y ese es el resultado». La regla ya existía dos reglas más abajo en el mismo capítulo, [`02·F19`](../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md): *«la redacción del CA es la especificación funcional»*. Y en su momento se intentó agregar otra que decía lo mismo y **chocaba con `02·F0`**. Se iba a rehacer un trabajo ya hecho **y descartado con razón**.
- **Qué lo soluciona:** se corrigieron los cinco documentos, cada uno diciendo qué afirmaba y por qué era falso.
- **Qué se decidió:** citar `02·F19`, que es la regla de verdad. Y no borrar lo que se dijo mal: queda tachado y explicado, porque el error enseña más que la conclusión.
- **Cómo se cometió, que es lo que vale:** se leyó la **narrativa** de la historia, que describe el problema en presente porque se escribió antes de resolverlo. **Nadie miró el campo `Estado`, que está en su primera tabla.** Y el error se cometió una vez y se **copió tres**: cada fase tomó la redacción de la anterior sin volver a la fuente, y la repetición lo hizo parecer más establecido, no menos.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** los cinco documentos corregidos y la señal `S-048`.
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
| Todo hallazgo abierto tiene su pendiente creado | ☑ · no queda ninguno abierto |
| Toda historia disparada está escrita en su épica | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ |

**Tres marcadas, una no.** **`H-27` y `H-31` cerraron**, los dos por la cadena completa: el inventario dejó de mantenerse a mano, adentro y en lo que el estándar reparte. **`H-33` también cerró**, con el plan ampliado y autorizado. **`H-28` también cerró**, y con él **todos los hallazgos de la sesión**. El tope de ruta se resolvió por la cadena, después de medir que ningún cambio de nombres alcanzaba. **No queda ninguno abierto**, así que no falta ningún pendiente por escribir. Mientras eso no ocurra, **la sesión no cierra**. Lo construido en esta sesión quedó guardado en quince commits, y el último es la fase F en `4573a15`, con la que **terminó la versión 1 del producto**. Los anteriores: la fase A en `26b2222`, la cadena de EP-011 en `7cfcf5d`, la fase D en `5231022` con su hash en `d261ab1`, y la fase B con la cadena de la HU-004 en `c1b9185`.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
