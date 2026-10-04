# Reglas de la tarea `trabajar-cadena`, parte 1 de 2

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## T1 · Todo cambio con lógica lleva prueba
Toda funcionalidad o corrección con lógica se acompaña de pruebas, y su plan se aprueba junto con el plan de trabajo ([`02·F4`](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).

Fuente: [08·T1](../08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba)

## G9 · La historia de usuario es la unidad del commit
Lo de una historia —documento, fases, código— va en un commit que **no toca otra**, y lo que aún no tiene historia espera a tenerla (concreta a [`G1`](../09-git.md#g1--commits-atómicos-un-solo-propósito)).
Excepción: lo que no es de ninguna historia sube con la primera que lo necesite.
Comprobable: un commit que toca dos carpetas de HU distintas se detecta comparando rutas.
```
INCORRECTO: un commit con HU-002, HU-003 y las épicas que todavía no
            tienen historias escritas
CORRECTO:   un commit por historia; la épica sin historias espera a tenerlas
```

Fuente: [09·G9](../09-git.md#g9--la-historia-de-usuario-es-la-unidad-del-commit)

## CQ1 · Sabe para quién construyes
Al iniciar un proyecto, identifica **sector**, **jurisdicción** y **marco aplicable** (lo declara la capa 3). Sin eso, no asumas requisitos ni los inventes: pregúntalos o pide la plantilla de marco normativo.
```
INCORRECTO: construir sin saber si es sector público, salud o privado
CORRECTO:   "¿Qué sector y jurisdicción? ¿Qué normas/frameworks aplican?" antes de decidir
```

Fuente: [16·CQ1](../16-cumplimiento-y-calidad.md#cq1--sabe-para-quién-construyes)

## CQ2 · Cumple por construcción y déjalo trazable
Traduce cada control del marco a una **decisión concreta** (esquema, validación, permiso, cifrado, log, retención) y verifícalo junto con la trazabilidad especificación→implementación ([`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md)). Si un requisito **no se puede cumplir**, avísalo — no lo omitas en silencio.
```
INCORRECTO: implementar y dar por hecho que "cumple"
CORRECTO:   mapear cada requisito del marco a un control real + evidencia en la trazabilidad
```

Fuente: [16·CQ2](../16-cumplimiento-y-calidad.md#cq2--cumple-por-construcción-y-déjalo-trazable)

## ID3 · No des por entregado lo que no está terminado
No des por entregado un cambio hasta que cumpla su especificación ([`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)), sus pruebas corran en verde ([`08·T5`](../08-pruebas.md#t5--ejecuta-y-reporta)), no rompa lo existente ([`02·F7`](../02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)) y deje rastro escrito para la próxima sesión ([`13·DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)). Si falta una de las cuatro, reporta qué falta — no cierres.
```
INCORRECTO: "listo" con las pruebas escritas pero sin correr, y la doc para después
CORRECTO:   "listo" = especificación cumplida + pruebas verdes 9/9 + nada roto + rastro escrito
```

Fuente: [00·ID3](../00-identidad-y-rol/reglas/ID3-no-des-por-entregado-lo-que-no-esta-terminado.md#id3--no-des-por-entregado-lo-que-no-está-terminado)

## ID4 · Asume el ciclo completo, de entender a documentar
Asume la unidad de trabajo entera: entender el proyecto, proponer, redactar la especificación, diseñar, planificar, implementar con pruebas, verificar, revisar defectos y seguridad, documentar y mantener la memoria. No entregues media cadena esperando que alguien complete el resto.
```
INCORRECTO: implementar y devolverlo "para que alguien le ponga las pruebas y la doc"
CORRECTO:   la unidad se entrega con su especificación, su código, sus pruebas y su documentación
```

Fuente: [00·ID4](../00-identidad-y-rol/reglas/ID4-asume-el-ciclo-completo-de-entender-a-documentar.md#id4--asume-el-ciclo-completo-de-entender-a-documentar)

## ID6 · Toma el rol especializado que pide la etapa
Toma el rol especializado que pida la etapa —Explorador, Escritor de especificación, Diseñador, Planificador de tareas, Implementador, Verificador, Crítico, Orquestador (`skills/`)—. El rol cambia el foco del trabajo, nunca la precedencia de las reglas ([`20·M1`](../20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)) ni el borde de [`ID5`](../00-identidad-y-rol/reglas/ID5-no-salgas-del-borde-del-rol.md).
```
INCORRECTO: "en modo Implementador voy directo al código; la especificación la vemos después"
CORRECTO:   el rol cambia qué se hace en esa etapa; las reglas que rigen son las mismas
```

Fuente: [00·ID6](../00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md#id6--toma-el-rol-especializado-que-pide-la-etapa)

## F0 · Recorre la cadena completa, sin saltar eslabones
Todo desarrollo, nuevo o cambio de comportamiento, recorre `planteamiento → épica → HU → especificación → plan → código`, con un análisis antes de las épicas, de las HU de cada épica y de cada pendiente. Ningún eslabón se salta ni se fusiona; si falta uno, se crea primero (depende de [`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md), [`13·DOC15`](../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md)).
```
INCORRECTO: llega una idea → se escribe el plan de trabajo directo
CORRECTO:   idea → análisis → objetivo y alcance → épica → HU → especificación
            → plan → construir
```

Fuente: [02·F0](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md#f0--recorre-la-cadena-completa-sin-saltar-eslabones)

## F1 · Carga el contexto antes de actuar
Antes de analizar o implementar, revisa la documentación del proyecto: qué existe, qué se decidió, qué está probado. Aplica también **antes** de afirmar que algo no existe: si el usuario menciona algo existente, primero búscalo.
```
INCORRECTO: "agregá validación X" → la diseño desde cero
CORRECTO:   reviso docs → ya hay un servicio que hace algo similar → propongo extenderlo
```

Fuente: [02·F1](../02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md#f1--carga-el-contexto-antes-de-actuar)

## F10 · Planifica la migración en vez de postergar por producción
Cuando el cambio toca algo que está o puede estar en producción, el plan asume **«probablemente sí lo está»** y declara la estrategia de migración incremental que corresponde; no se posterga la fase preguntando si está en producción. La casuística: [`base.md`](../02-flujo-de-trabajo/base.md) (extiende [`02·F14`](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 12).
```
INCORRECTO: "antes de arrancar la fase necesito confirmar si X está en producción"
            → fase bloqueada esperando información que se puede asumir
CORRECTO:   el plan asume "probablemente está en prod" y declara la estrategia
            (aditiva · rename reversible · drop con aviso · tipo con aviso)
```

Fuente: [02·F10](../02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md#f10--planifica-la-migración-en-vez-de-postergar-por-producción)

## F11 · Una fase solo modifica código de su propio módulo
Todos los archivos que una fase modifica pertenecen al módulo que declaró al abrirse ([`13·DOC12`](../13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)). Si el trabajo alcanza a otros módulos se descompone en **una fase por módulo** y el resto se difiere por escrito, nunca en una «fase transversal», que borra la trazabilidad.
```
INCORRECTO: fase del módulo A arranca tocando 20 archivos de B, C y D "porque el
            refactor es transversal" → se pierde la trazabilidad por módulo
CORRECTO:   la fase A toca solo archivos de A; lo necesario en B, C y D se agenda
            como fases propias o se difiere en §Fuera-de-scope
```

Fuente: [02·F11](../02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md#f11--una-fase-solo-modifica-código-de-su-propio-módulo)

## F12 · Nombra y ubica cada fase según la nomenclatura del anexo
Una fase pertenece a una sola historia, lleva consecutivo alfabético dentro de ella, se nombra `[Consecutivo]-EP-NNN-HU-NNN-[descripción]` y vive donde dice el anexo [base/02-flujo-de-trabajo/nomenclatura-de-fases.md](../02-flujo-de-trabajo/nomenclatura-de-fases.md), fuente única de `F12.1` a `F12.13`; no se crea una fase solo por la nomenclatura (depende de [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).
```
INCORRECTO: la fase se llama «ajustes varios» y cuelga de dos historias a la vez
CORRECTO:   B-EP-001-HU-003-Implementación de la lógica de negocio, dentro de su HU,
            con sus cinco documentos en la ruta del anexo
```

Fuente: [02·F12](../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md#f12--nombra-y-ubica-cada-fase-según-la-nomenclatura-del-anexo)

## F13 · Deja la estructura base puesta antes de trabajar
Antes de cualquier paso del flujo —incluso antes de cargar contexto ([`02·F1`](../02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md))— el agente crea las carpetas que la norma exige: `proyectos/` para el código del usuario y, al lado, `.agente/`, `prompts/` y `documentacion/`. Crearlas no es decisión suya; **qué va dentro sí**, y ahí no mueve nada.
```
INCORRECTO: existe código suelto en la raíz → el agente crea `proyectos/` y mueve
            el código del usuario adentro
CORRECTO:   existe código suelto en la raíz → el agente crea `proyectos/` vacía,
            avisa que hay código fuera y espera a que el usuario decida si lo mueve
```

Fuente: [02·F13](../02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md#f13--deja-la-estructura-base-puesta-antes-de-trabajar)

## F14 · Responde las trece preguntas en todo plan de trabajo
Un plan de trabajo responde las **trece preguntas** del capítulo antes de que se escriba una línea de código. La que no aplique al alcance se deja con su encabezado y un «No aplica porque ...», no se omite; las trece están en [`base.md`](../02-flujo-de-trabajo/base.md) (extiende [`02·F4`](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) · deroga [`02·F4.1`](../02-flujo-de-trabajo/reglas/F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)).
```
INCORRECTO: plan que dice "creo el CRUD X" y omite dónde queda accesible al usuario
            → se implementa el CRUD y el usuario tiene que ir a la URL a mano
CORRECTO:   plan que responde las trece → nadie ejecuta a medias, porque hay que
            declarar cada respuesta antes de aprobar
```

Fuente: [02·F14](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md#f14--responde-las-trece-preguntas-en-todo-plan-de-trabajo)

## F15 · No saltes ni reordenes las once etapas de la fase
Toda fase recorre las once etapas del ciclo —declaración macro, disparo, diseño del plan, pausa, aprobación, ejecución, pruebas, cierre documental, commit, reporte y publicación— en ese orden (extiende [`02·F4`](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) · deroga [`02·F4.2`](../02-flujo-de-trabajo/reglas/F4.2-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)). Quién actúa y qué hito cierra cada una: [`base.md`](../02-flujo-de-trabajo/base.md).
```
INCORRECTO: usuario dice "arranque con Fase X" → agente empieza a implementar
            (se salta las etapas 3, 4 y 5: plan, pausa y aprobación)
CORRECTO:   disparo → plan detallado → pausa y presentación → OK del usuario
            → ejecución
```

Fuente: [02·F15](../02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md#f15--no-saltes-ni-reordenes-las-once-etapas-de-la-fase)

## F16 · Declara los cinco componentes de cada intervención del plan
Cada intervención del plan dice **qué** se hace, **cómo**, **dónde** exactamente, **por qué** —qué hueco cierra— y con qué **impacto** en el resto. Fuera los verbos vagos y los alcances abiertos; qué se espera de cada componente, en [`base.md`](../02-flujo-de-trabajo/base.md) (extiende [`02·F14`](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) · deroga [`02·F4.3`](../02-flujo-de-trabajo/reglas/F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)).
```
INCORRECTO: "revisar el servicio de facturación y mejorar lo que haga falta"
CORRECTO:   "modificar `<ruta>`: agregar el parámetro `bar` a `foo()` para cerrar
            el gap-3; rompe los dos llamadores de `<ruta B>`, que también entran"
```

Fuente: [02·F16](../02-flujo-de-trabajo/reglas/F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md#f16--declara-los-cinco-componentes-de-cada-intervención-del-plan)

## F17 · Verifica contra el proyecto real todo lo que el plan afirma
Cada ruta, firma y dependencia que el plan nombra se comprueba antes contra el proyecto. Quedan prohibidas las marcas de incertidumbre («o donde esté», «o similar», «por confirmar»): lo que no se pueda verificar se declara pregunta abierta y espera al usuario, no se escribe como suposición (depende de [`02·F1`](../02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md)).
```
INCORRECTO: "el archivo de navegación de la carpeta de vistas (o donde esté)"
            → el plan admite que no verificó la ruta real
CORRECTO:   listar la carpeta → localizar el archivo → leerlo → plan dice
            "<ruta real>, sección <X>: agregar el ítem con permiso <permiso.ver>"
```

Fuente: [02·F17](../02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md#f17--verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma)

## F18 · Deriva el plan de los CA aprobados, no de la proactividad
Toda intervención listada en el plan —código, migración, seed, vista, prueba— rastrea de forma explícita al **criterio de aceptación** de la HU que la justifica (extiende [`02·F14`](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) · deroga [`02·F4.4`](../02-flujo-de-trabajo/reglas/F4.4-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)). Lo que no venga de un CA se retira del plan y se propone aparte ([`02·F20`](../02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).
```
INCORRECTO: §Alcance dice "también aprovechamos para limpiar el código legacy de Y"
            cuando ningún CA de la fase menciona Y
CORRECTO:   cada línea del plan muestra "intervención → CA"; lo de Y se propone
            como fase aparte con su propia HU
```

Fuente: [02·F18](../02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md#f18--deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad)

## F19 · Implementa literal el criterio de aceptación
La implementación hace **literal** lo que dice el CA aprobado: ni más, ni menos, ni "más seguro por si acaso" (extiende [`02·F18`](../02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) · deroga [`02·F4.5`](../02-flujo-de-trabajo/reglas/F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md)). La redacción del CA es la especificación funcional: el agente no la interpreta libremente ni la endurece por su cuenta.
```
INCORRECTO: el CA pide un listado de clientes, y se le agrega una exportación
            a hoja de cálculo «porque todo listado la trae»
CORRECTO:   se implementa el listado que el CA dice, tal cual
```

Fuente: [02·F19](../02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md#f19--implementa-literal-el-criterio-de-aceptación)

## F2 · Sin especificación acordada no hay código
Ningún desarrollo, refactor o migración sin una **especificación acordada** que lo respalde —alcance, reglas de negocio, datos, pruebas, permisos—. Si no existe, el agente **no toca código**: ofrece redactar el borrador y lo hace aprobar primero. Sin especificación, el código es opinión del agente.
```
INCORRECTO: "hacé que el módulo permita X" → escribo código directo
CORRECTO:   busco X en la especificación → si no está: "no está en la especificación; ¿lo agrego a la fase Y
            o es dominio nuevo?" → aprueban → actualizo especificación → implemento + pruebas
```

Fuente: [02·F2](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md#f2--sin-especificación-acordada-no-hay-código)

## F21 · Un incumplimiento ya identificado no se repite en lo nuevo
Desde que un incumplimiento queda registrado en un pendiente, un hallazgo o una señal, todo lo que se escriba de ahí en adelante nace cumpliendo. El pendiente guarda lo que ya estaba mal y se limpia aparte; no autoriza a producir más de lo mismo.
```
INCORRECTO: el pendiente dice que 354 enlaces no cumplen DOC14,
            y los documentos de hoy suman 122 más
CORRECTO:   los 354 siguen en su pendiente y los de hoy nacen bien
```

Fuente: [02·F21](../02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md#f21--un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo)

## F22 · No avances de fase con una derogación sin adoptar
Ninguna fase se abre ni se cierra mientras el proyecto declare una versión anterior a la que derogó una regla que ya cumplía. Lo único que se abre es la fase que la adopta, una por HU que la implementaba, y al cerrarla sube la versión declarada. Fuera de ahí el desfase se reporta y no detiene (depende de [`20·M11`](../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).
```
INCORRECTO: se sube la versión declarada y se sigue trabajando, sin tocar las
            HU que implementaban la regla derogada
CORRECTO:   se abre una fase por cada HU que la implementaba, se aplica la regla
            que la reemplazó, y al cerrarla se sube la versión declarada
```

Fuente: [02·F22](../02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md#f22--no-avances-de-fase-con-una-derogación-sin-adoptar)

## F23 · Ejecuta un pendiente como fase de una historia de usuario
Un hallazgo se anota como pendiente; el pendiente aprobado pasa por su análisis, baja a una historia de usuario hija de su épica y se construye como fase de esa historia. Que la mejora ya esté escrita no salta ningún eslabón: el pendiente dice **qué falta**, no cómo se construye ni se comprueba (extiende [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).
```
INCORRECTO: el pendiente dice qué hay que arreglar → se edita el código, se sube
            la versión y se marca hecho; como no hubo fase, nadie escribió el
            plan de pruebas y el arreglo se publicó sin probarse
CORRECTO:   el pendiente baja a HU → fase con su plan y sus pruebas → se
            construye, se prueba, y solo entonces el pendiente se marca hecho
```

Fuente: [02·F23](../02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md#f23--ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario)

## F24 · El defecto del estándar se reporta, no se corrige
Un proyecto que encuentra un defecto del estándar **no lo toca**: abre un pendiente allá, en la HU que citan la regla o el programa que fallan, o en el resumen del día si no la citan, que enlaza el hallazgo de acá; otro acá que enlaza el de allá, y sigue con lo suyo. El de acá cierra cuando le llega el aviso, que el estándar envía después de comprobar la corrección en el proyecto (extiende [`02·F23`](../02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).
```
INCORRECTO: se parchea el estándar en la copia local del proyecto → los otros
            proyectos siguen con el defecto y nadie se entera
CORRECTO:   se reporta en el estándar, se anota acá el seguimiento, y el
            proyecto sigue con su trabajo
```

Fuente: [02·F24](../02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md#f24--el-defecto-del-estándar-se-reporta-no-se-corrige)

## F25 · Autorizar el arranque no aprueba el plan
Decir «arranque con X» autoriza **abrir la fase**, no ejecutar su plan detallado: son dos permisos distintos y el segundo se pide aparte, con el plan a la vista (extiende [`02·F4`](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)).
```
INCORRECTO: «dale, arrancá con la fase B» → se escribe el plan y se ejecuta seguido
CORRECTO:   se abre la fase, se escribe el plan, se presenta, y se espera el segundo sí
```

Fuente: [02·F25](../02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md#f25--autorizar-el-arranque-no-aprueba-el-plan)

## F26 · El inventario de funcionalidades aprobado es la puerta de las épicas
Ninguna épica se deriva sin el **inventario de funcionalidades** aprobado por el usuario, con estado por ítem y lo no decidido marcado «por confirmar» ([`plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md`](../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md)). La épica que no baje de ningún ítem no arranca (extiende [`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)).
```
INCORRECTO: el agente escribe el planteamiento asumiendo el techo del alcance y
            deriva tres épicas; la corrección del usuario llega con 21 historias
            ya escritas encima
CORRECTO:   la propuesta llega con su inventario; el usuario aprueba o corrige el
            alcance ahí, y las épicas se derivan citando los ítems que cubren
```

Fuente: [02·F26](../02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md#f26--el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-épicas)

## F27 · Cada punto dice de qué punto del anterior sale
Cada punto de un documento de la cadena lleva «Sale de» con el punto del documento anterior: el pendiente, su hallazgo; el punto de «Lo acordado» del análisis, su turno; el criterio de la HU, su punto de «Lo que se tiene que hacer». Lo que no tiene origen no entra (extiende [`02·F18`](../02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).
```
INCORRECTO: la HU trae un CA-04 sin «Sale de», porque «se veía necesario»
CORRECTO:   el CA-04 dice «Sale de: análisis 6, punto 2», y ese punto existe
            en «Lo que se tiene que hacer» del análisis 6
```

Fuente: [02·F27](../02-flujo-de-trabajo/reglas/F27-cada-punto-dice-de-que-punto-del-anterior-sale.md#f27--cada-punto-dice-de-qué-punto-del-anterior-sale)

## F28 · El cambio se aplica donde nace y baja en orden
Si cambia la necesidad, el cambio se escribe primero en el documento donde nace, aunque sea el planteamiento, y baja en orden por la épica, la HU, la especificación y el plan. Cada uno cambia en su mismo archivo, que pasa a su versión siguiente; el análisis no se reescribe, se numera el siguiente (extiende [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).
```
INCORRECTO: el usuario cambia lo que necesita y se corrige el plan; la HU
            sigue diciendo lo de antes
CORRECTO:   se corrige la HU en su mismo archivo, después la especificación
            y al final el plan, cada uno en su versión siguiente
```

Fuente: [02·F28](../02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md#f28--el-cambio-se-aplica-donde-nace-y-baja-en-orden)

## F29 · El reporte de un proyecto se corrige para todos
Lo que un proyecto reporta al estándar es un defecto que ya está en todos los proyectos que lo usan. Se analiza buscando su causa en el estándar, se revisa en cada proyecto registrado y se corrige en la raíz. Antes de avisar, se comprueba en el proyecto que lo reportó, en el escenario donde se presentó (complementa [`02·F24`](../02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md)).
```
INCORRECTO: scilit reporta que el andamio no sirve desde un proyecto → se
            arregla para que funcione en scilit
CORRECTO:   se busca por qué el andamio supone estar dentro del estándar, se
            corrige ahí, se prueba en una copia de scilit y después se le avisa
```

Fuente: [02·F29](../02-flujo-de-trabajo/reglas/F29-el-reporte-de-un-proyecto-se-corrige-para-todos.md#f29--el-reporte-de-un-proyecto-se-corrige-para-todos)

## F3 · Ejecuta seguido el plan aprobado
Aprobado el plan, ejecuta **todos** sus cambios seguidos, sin pedir permiso por cada archivo. Solo pausa si surge algo **no cubierto** por el plan.
```
INCORRECTO: "hago el cambio 1, ¿procedo?" → "el 2, ¿procedo?" → ...
CORRECTO:   ejecuto todo el plan → reporto el resultado
```

Fuente: [02·F3](../02-flujo-de-trabajo/reglas/F3-ejecuta-seguido-el-plan-aprobado.md#f3--ejecuta-seguido-el-plan-aprobado)
