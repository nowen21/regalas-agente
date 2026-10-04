# Reglas de la tarea `trabajar-cadena`, parte 2 de 2

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## F4 · Todo plan lleva su plan de pruebas y su aprobación explícita
Cada plan de trabajo se redacta junto a su plan de pruebas, se **presenta** al usuario y **no se toca código hasta un OK explícito** suyo ([`01·C17`](../01-conducta.md#c17--ante-un-pedido-que-admite-dos-lecturas-reformula-antes-de-mover-nada)). Si no existe la HU con sus criterios que respalde el plan, **PAUSAR y retroceder** al eslabón que falta (depende de [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), [`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)).
```
INCORRECTO: usuario dice "arranque con Fase X" → agente redacta plan + implementa
            todo seguido → reporta al final
CORRECTO:   usuario dice "arranque con Fase X" → agente redacta plan + pruebas →
            PAUSA + presenta → usuario aprueba (o pide cambios) → agente implementa
```

Fuente: [02·F4](../02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md#f4--todo-plan-lleva-su-plan-de-pruebas-y-su-aprobación-explícita)

## F5 · Corre solo las suites que la fase toca
La ejecución que cierra una fase alcanza la suite del módulo de la fase, las suites que la fase refactorizó y las que dependen de los archivos tocados según la matriz de [`02·F17`](../02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) — no la suite completa del proyecto (extiende [`08·T5`](../08-pruebas.md#t5--ejecuta-y-reporta), que ya obliga a correrlas y a reportar el conteo).
```
INCORRECTO: al terminar la fase, correr toda la suite del proyecto "por si acaso"
            → cientos de pruebas, minutos de espera y rojos que ya existían antes
CORRECTO:   correr la suite del módulo + las declaradas en el plan + las que la
            matriz de dependencias señala
```

Fuente: [02·F5](../02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md#f5--corre-solo-las-suites-que-la-fase-toca)

## F8 · Edita solo los archivos que el plan aprobado declara
Se editan únicamente los archivos de la tabla del plan aprobado ([`02·F14`](../02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 9). Descubrir a mitad que hace falta otro **detiene la ejecución** y vuelve al análisis: el plan pasa a su versión siguiente con aprobación nueva. Que el cambio sea obvio no autoriza; la aprobación sí ([`base.md`](../02-flujo-de-trabajo/base.md)).
```
INCORRECTO: durante la ejecución el agente descubre que también hay que editar el
            archivo Y → lo edita en el mismo commit "porque era necesario"
CORRECTO:   descubre Y → se detiene → vuelve al análisis → el plan pasa a
            su versión siguiente y el usuario la aprueba → sigue
```

Fuente: [02·F8](../02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md#f8--edita-solo-los-archivos-que-el-plan-aprobado-declara)

## F9 · No subdividas ni renegocies un plan ya aprobado
Aprobado un plan, se entrega **completo**: no se parte en sub-fases nuevas, no se vuelve a preguntar por decisiones que ya cabían dentro ni se ofrecen opciones sobre detalles ya resueltos con criterio profesional. Si el volumen pide subdividir, se propone **antes** de aprobar (extiende [`02·F3`](../02-flujo-de-trabajo/reglas/F3-ejecuta-seguido-el-plan-aprobado.md)).
```
INCORRECTO: usuario aprueba el plan → agente lo divide en 4 sub-fases y vuelve a
            pedir 4 aprobaciones "para hacerlo manejable"
CORRECTO:   si el volumen era problema, la subdivisión se propone ANTES de aprobar;
            después, ejecución continua
```

Fuente: [02·F9](../02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md#f9--no-subdividas-ni-renegocies-un-plan-ya-aprobado)

## DOC1 · Persiste el trabajo de cada unidad completada
Al cerrar una unidad, deja en documentación versionada **qué se planeó**, **qué se probó** —incluidas las verificaciones manuales que el entorno automático no cubre ([`08·T4`](../08-pruebas.md#t4--protege-los-datos-reales-al-probar))— y **qué quedó**: cómo usarlo, puntos de entrada, enlaces al código. El chat no sustituye los archivos.
```
INCORRECTO: implementar, mostrar todo en el chat y cerrar
CORRECTO:   implementar + persistir plan, pruebas y resultado
```

Fuente: [13·DOC1](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md#doc1--persiste-el-trabajo-de-cada-unidad-completada)

## DOC11 · Usa la tabla canónica de cinco columnas para la trazabilidad
La verificación que exige [`DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) se escribe en el documento de cierre con la [tabla canónica de cinco columnas](../13-documentacion/tabla-de-trazabilidad.md), y todo lo que no sea ✅ lleva su justificación escrita; el faltante que era de esta unidad se corrige acá, no se difiere.
```
INCORRECTO: cerrar con la tabla a medias o con un "N/A porque sí"
CORRECTO:   tabla completa · faltantes justificados · diferimientos con destino explícito
```

Fuente: [13·DOC11](../13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md#doc11--usa-la-tabla-canónica-de-cinco-columnas-para-la-trazabilidad)

## DOC12 · Declara el ORIGEN de cada fase al abrirla
Toda fase nueva abre declarando de dónde sale, en una de tres formas: **modifica** fases anteriores, nombrándolas; **agrega** lo que no existía; o **ambas**. El formato del bloque está en [`plantillas/ciclo-vida-proyectos/05-fase.md`](../../plantillas/ciclo-vida-proyectos/05-fase.md) y la carpeta de la fase repite el ORIGEN de su especificación.
```
INCORRECTO: "Fase 7 — cambios menores" · quien lee no sabe si continúa la 6
            o reacciona a un análisis
CORRECTO:   ORIGEN declarado: qué fase modifica y qué defecto retoma, o qué agrega
```

Fuente: [13·DOC12](../13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md#doc12--declara-el-origen-de-cada-fase-al-abrirla)

## DOC13 · Registra cada módulo nuevo en el catálogo de módulos
Un módulo nuevo —dominio funcional propio, con su prefijo de rutas o su especificación separada— se registra en el catálogo de módulos **antes de cerrar** la unidad que lo creó, con lo que pide [`plantillas/catalogo-modulos.md`](../../plantillas/catalogo-modulos.md). No cuentan la fase de un módulo que ya existe, el arreglo interno ni el componente hijo.
```
INCORRECTO: se crea un módulo · las sesiones siguientes asumen que el proyecto
            "solo tiene X e Y" porque el nuevo no está en el catálogo
CORRECTO:   al cerrar la unidad que lo creó, su entrada queda en el catálogo
```

Fuente: [13·DOC13](../13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md#doc13--registra-cada-módulo-nuevo-en-el-catálogo-de-módulos)

## DOC15 · Crea la Historia de Usuario desde la plantilla central
Toda HU se parte de [`plantillas/ciclo-vida-proyectos/04-HU.md`](../../plantillas/ciclo-vida-proyectos/04-HU.md), leída del estándar **cada vez**, y se guarda versionada donde fija [`02·F12`](../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13. Se rellena con contenido real: rol concreto, criterios que cubran camino feliz, error y caso borde, sin secciones a medio llenar.
```
INCORRECTO: escribir la HU de memoria, o copiar la plantilla dentro del proyecto
            "para tenerla a mano" — la copia queda vieja y nadie se entera
CORRECTO:   leer la plantilla central → rellenarla con datos reales → guardarla
            donde manda la nomenclatura de fases
```

Fuente: [13·DOC15](../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md#doc15--crea-la-historia-de-usuario-desde-la-plantilla-central)

## DOC16 · Crea la Épica desde la plantilla central
Toda épica se parte de [`plantillas/ciclo-vida-proyectos/03-epica.md`](../../plantillas/ciclo-vida-proyectos/03-epica.md), leída del estándar cada vez, y se guarda donde fija [`02·F12`](../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13. Sus criterios son de resultado, no de pantalla, y el enlace con cada HU se escribe en los dos lados (depende de [`02·F0`](../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).
```
INCORRECTO: la épica lista sus HU, pero ninguna HU declara a qué épica pertenece
CORRECTO:   la épica lista sus HU y cada HU nombra su épica · al mover una, se
            actualizan los dos
```

Fuente: [13·DOC16](../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md#doc16--crea-la-épica-desde-la-plantilla-central)

## DOC17 · Mantén un `README.md` en cada nivel del árbol de trabajo
Ninguna carpeta del árbol de épicas, HU y fases ([`02·F12`](../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13) queda muda: cada una tiene un `README.md` que lista **su contenido inmediato**, no el árbol entero, con una frase de qué es cada cosa. Se actualiza en el mismo cambio que crea, mueve o cierra algo.
```
INCORRECTO: la carpeta de la épica tiene ocho HU dentro y ningún índice ·
            hay que abrirlas una por una para saber qué hay
CORRECTO:   su README lista las ocho, cada una con su título y su estado
```

Fuente: [13·DOC17](../13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md#doc17--mantén-un-readmemd-en-cada-nivel-del-árbol-de-trabajo)

## DOC18 · Actualiza el mapa de dependencias al cerrar la unidad
El mapa que [`DOC9`](../13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) manda consultar se actualiza en el **mismo cambio** que cierra la unidad (extiende [`13·DOC9`](../13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)): lo que se agregó, con qué se relaciona y quién lo consume. Un mapa que se actualiza "después" es un mapa que la próxima unidad ya no puede creer, y entonces vuelve a explorar de cero.
```
INCORRECTO: cerrar la unidad y dejar el mapa para más adelante
CORRECTO:   el cambio que cierra la unidad incluye el mapa al día
```

Fuente: [13·DOC18](../13-documentacion/reglas/DOC18-actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad.md#doc18--actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad)

## DOC3 · Verifica la trazabilidad especificación → implementación antes de cerrar
Antes de cerrar, revisa ítem por ítem que cada afirmación técnica de la especificación ([`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)) esté en el código, el esquema, las pruebas y los docs (depende de [`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)). Lo faltante se corrige o se justifica; no se cierra con huecos sin explicar. El formato de la tabla lo fija [`DOC11`](../13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md).
```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + tabla de trazabilidad sin faltantes → cierro"
```

Fuente: [13·DOC3](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md#doc3--verifica-la-trazabilidad-especificación--implementación-antes-de-cerrar)

## DOC6 · Retro-documenta el módulo sin especificación antes de tocarlo
Un módulo productivo sin especificación —o con una especificación más vieja que el código— se retro-documenta como **unidad de trabajo formal** antes de intervenirlo, siguiendo [`plantillas/retrodocumentacion.md`](../13-documentacion/retrodocumentacion.md). Queda en estado provisional: cierra en el primer audit profundo.
```
INCORRECTO: encontrar un módulo sin especificación y decir "asumo que hace X" en la próxima fase
CORRECTO:   retro-documentarlo primero · el análisis persistido queda como fotografía
            del punto de partida
```

Fuente: [13·DOC6](../13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md#doc6--retro-documenta-el-módulo-sin-especificación-antes-de-tocarlo)

## DOC9 · Consulta el mapa de dependencias antes de planificar
Al planificar una unidad de trabajo se lee primero el mapa de dependencias del proyecto, cuya ruta declara la capa 3, y se explora el código solo si el mapa no cubre la duda o no coincide con lo que hay. El mapa es la fuente autoritativa de cómo está armado el sistema hoy.
```
INCORRECTO: abrir la unidad y explorar el proyecto entero como si fuera la primera vez
CORRECTO:   leer el mapa → si hay duda puntual, verificarla en el archivo concreto
```

Fuente: [13·DOC9](../13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md#doc9--consulta-el-mapa-de-dependencias-antes-de-planificar)
