# Glosario del estándar

**Para qué sirve.** Cada palabra que el estándar usa con un significado propio, explicada en una línea. Sirve para entrar a leer las reglas sin ir preguntando qué significa cada término, y para que dos documentos no llamen distinto a la misma cosa.

**Qué es y qué no es.** Es un anexo, no una regla: acá no se exige nada. Por eso no lleva número de capítulo ni resultado del [checklist del estándar](20-meta-reglas/checklist.md). La exigencia siempre vive en la regla que se nombra en la columna **Regla**; acá solo se dice qué es la cosa.

**Cómo está armado.** Cuatro grupos, y dentro de cada uno los términos en orden alfabético:

1. [La cadena de trabajo](#1--la-cadena-de-trabajo), del pedido al código publicado.
2. [Las reglas](#2--las-reglas), cómo están hechas y cómo se cambian.
3. [Lo que comprueba](#3--lo-que-comprueba), los programas y las pruebas.
4. [Lo que se guarda](#4--lo-que-se-guarda), la memoria escrita del proyecto.

Al final está la [lista de lo que sigue en otro idioma](#lo-que-sigue-en-otro-idioma), que es lo que pide [`01·C20`](01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica).

**Qué entra.** Solo lo que aparece en una regla o en una plantilla. Una palabra del oficio que el estándar no usa no entra acá: para eso está el diccionario.

**Cómo se mantiene.** Cada entrada define y enlaza; nunca copia el texto de su regla. Dos copias de lo mismo terminan diciendo cosas distintas, y la que manda es la que nadie relee.

---

## 1 · La cadena de trabajo

El orden de la cadena lo fija [`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md): brief, épica, historia de usuario, especificación, plan, código. Ningún eslabón se salta.

| Término | Qué quiere decir el nombre | Qué es | Quién lo escribe | Dónde vive | Regla |
|---|---|---|---|---|---|
| **Brief** | En inglés, «breve». Es el encargo escrito corto | El primer papel: qué quiere resolver el negocio, antes de que exista ninguna solución | Agente, con lo que dice el usuario | `prompts/<slug>-brief.md` | [`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) |
| **Commit** | En inglés, «comprometer»: lo guardado queda firme en el historial | Guardar en el historial un paquete de cambios con un solo propósito y su explicación | Agente, y el usuario lo autoriza | El historial del repositorio | [`09·G1`](09-git.md#g1--commits-atómicos-un-solo-propósito), [`09·G7`](09-git.md#g7--todo-commit-se-muestra-al-usuario-y-se-aprueba-antes-de-ejecutarlo) |
| **Criterio de aceptación (CA)** | — | La frase que dice cuándo se puede decir que algo quedó hecho, escrita para poder comprobarla | Agente, en la historia de usuario | Dentro de la HU | [`02·F19`](02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) |
| **Épica** | Del relato largo: agrupa muchas historias | Un bloque grande de trabajo que agrupa historias de usuario parecidas | Agente | `documentacion/epicas/EP-NNN-<slug>/epica.md` | [`13·DOC16`](13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) |
| **Especificación** | — | El plano de un módulo: qué debe hacer, escrito y acordado antes de programarlo | Agente, y el usuario lo aprueba | Donde lo diga la capa de proyecto | [`02·F2`](02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md) |
| **Estación** | Como las de una línea de montaje: el trabajo pasa por cada una | Cada uno de los trece puestos por los que pasa una fase, del análisis a la publicación | Nadie: es el recorrido | Se anota en el estado de fase | [`02·F15`](02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) |
| **Estado de fase** | — | La hoja que dice en qué estación va la fase hoy y qué la tiene detenida | Agente, y la actualiza mientras trabaja | `estado-fase.md` de la fase | [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) |
| **Fase** | — | El pedazo de trabajo que de verdad se ejecuta: un plan, sus pruebas, su cierre y su commit | Agente | `documentacion/epicas/EP-NNN-<slug>/HU-NNN-<slug>/<letra>-EP-NNN-HU-NNN-<slug>/` | [`02·F12`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) |
| **Funcionalidad implementada** | — | El documento de cierre: qué quedó hecho de verdad, comparado contra lo que el plan prometió | Agente, al cerrar la fase | `funcionalidad_implementada.md` de la fase | [`13·DOC1`](13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md) |
| **Historia de usuario (HU)** | — | Una necesidad contada desde quien la va a usar, con lo que hace falta para darla por cumplida | Agente | `HU-NNN-<slug>.md`, dentro de su épica | [`13·DOC15`](13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md) |
| **Módulo** | — | Una pieza técnica del sistema, con su especificación y su nombre en el catálogo | Agente | `documentacion/<slug-del-módulo>/spec.md` | [`13·DOC13`](13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) |
| **Plan de pruebas** | — | Con qué casos se comprueba cada criterio de aceptación, escrito antes de correr la primera prueba | Agente, y el usuario lo aprueba | `plan_pruebas.md` de la fase | [`02·F4`](02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| **Plan de trabajo** | — | Qué se va a hacer, en qué orden y sobre qué archivos, respondiendo trece preguntas | Agente, y el usuario lo aprueba | `plan_trabajo.md` de la fase | [`02·F14`](02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) |
| **Puerta** | Se abre o no se abre: sin cumplirla no se pasa a la siguiente estación | La condición que hay que cumplir para pasar de una estación a la siguiente; varias piden el sí del usuario | Nadie: es el permiso de paso | Se anota en el estado de fase | [`02·F15`](02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) |
| **Publicación** | — | Sacar los cambios al servidor donde corren de verdad; es acción aparte del commit y se autoriza aparte | Usuario autoriza, agente ejecuta | El servidor del proyecto | [`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada) |
| **Resultado de pruebas** | — | Qué se ejecutó, con qué se probó y qué dio, sin tocar el plan que ya se aprobó | Agente, al correr las pruebas | `resultado_pruebas.md` de la fase | [`02·F12.13`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) |
| **Rol** | El papel que se hace en cada etapa, como en el teatro | El sombrero que el agente se pone según la etapa; cambia el foco del trabajo, nunca las reglas | Nadie: lo toma el agente | `skills/` | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md) |
| **Tarea** | — | El pedazo más chico del plan, de cuatro horas o menos, que rastrea a un criterio de aceptación | Agente, en el plan de trabajo | §3 del plan de trabajo | [`02·F18`](02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) |

---

## 2 · Las reglas

Cómo están hechas las reglas del estándar, cómo se citan y cómo se cambian. El capítulo dueño es [`20 · Meta-reglas`](20-meta-reglas/base.md).

| Término | Qué quiere decir el nombre | Qué es | Quién lo escribe | Dónde vive | Regla |
|---|---|---|---|---|---|
| **Anexo** | Va anexo al capítulo: pegado a él sin ser una de sus reglas | Una lista o un molde que no cabe dentro de una regla y vive al lado de su capítulo; no exige nada por sí solo | Agente | Junto al capítulo dueño | [`20·M2`](20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) |
| **Base** | Es la base sobre la que cada proyecto pone lo suyo | La carpeta con las reglas que sirven a cualquier proyecto; es lo que heredan los proyectos | Usuario decide, agente redacta | [`base/README.md`](README.md) | [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) |
| **Blindada** | Blindada contra cambios: ninguna capa la puede tocar | La marca de una regla de seguridad que ningún proyecto ni ninguna instrucción puede desactivar | Nadie: es una marca | Solo en la capa 1 | [`00 · Núcleo blindado`](00-nucleo-blindado.md) |
| **Capa** | Como las capas de una cebolla: cada una encima de la otra y ninguna borra la de abajo | Uno de los cuatro niveles en que están las reglas; cuando dos chocan, gana la de más arriba | Nadie: es el orden | Preámbulo, capa 1, capa 2 y capa 3 | [`20·M1`](20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) |
| **Capa de proyecto** | — | Las reglas propias de un proyecto: su lenguaje, su negocio, lo que decidió su equipo | Usuario del proyecto | `CLAUDE.md` y `.agente/` del proyecto | [`20·M16`](20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) |
| **Capítulo** | — | El archivo o la carpeta que agrupa las reglas de un mismo tema, con su número y su prefijo | Agente | `base/NN-<tema>` | [`20·M2`](20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) |
| **Checklist del estándar** | Del inglés «lista de chequeo»: se recorre marcando una por una | Las veinte preguntas con que se revisa si una regla quedó bien escrita; una sola en rojo y no se publica | Agente, al escribir la regla | [`base/20-meta-reglas/checklist.md`](20-meta-reglas/checklist.md) | [`20·M14`](20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) |
| **Cita `NN·ID`** | — | La forma de nombrar una regla desde otro lado: número del capítulo, punto medio, identificador, y su enlace | Agente | En cualquier documento | [`20·M4`](20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M15`](20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) |
| **CUMPLE / NO CUMPLE** | — | El resultado del checklist, escrito al final de la propia regla para no volver a revisarla | Agente | Al cierre del archivo de la regla | [`20·M14`](20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) |
| **Dependencia** | — | La relación entre dos reglas, y solo hay tres: `extiende`, `depende de` y `deroga` | Agente, dentro de la regla | En el cuerpo de la regla | [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) |
| **Derogar** | Palabra del derecho: la norma deja de regir y su texto se conserva | Sacar de circulación una regla dejando su texto puesto y marcado, porque hay commits que la citan | Agente | En el archivo de la propia regla | [`20·M11`](20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) |
| **Estándar** | — | El conjunto de reglas y moldes que este repositorio define y que otros proyectos heredan | Usuario decide, agente redacta | `base/` y `plantillas/` | [`20·M13`](20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) |
| **Excepción** | — | El caso en que una regla no aplica, escrito dentro de ella con su condición, su límite y quién lo autoriza | Agente, con el sí del usuario | Dentro de la regla que la admite | [`20·M8`](20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) |
| **Identificador** | — | El código corto de una regla, como `C20` o `F12`; no cambia nunca y no se reutiliza | Agente, al crear la regla | En el título de la regla | [`20·M4`](20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) |
| **Marca de espacio por llenar** | — | Las comillas angulares `«…»` que señalan un hueco de un molde; un documento que todavía las trae no está terminado | Agente, al escribir el molde | En las plantillas | [`13·DOC19`](13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md), [`13·DOC20`](13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) |
| **Marcador de generación automática** | Marca porque delata, como la huella que deja quien pasó | El rasgo que delata que un texto lo armó una máquina y no una persona | Nadie: es una lista cerrada | [`base/00-identidad-y-rol/marcadores-de-ia.md`](00-identidad-y-rol/marcadores-de-ia.md) | [`00·ID8`](00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) |
| **Meta-regla** | «Meta» acá es «sobre»: una regla sobre las reglas | Una regla cuyo tema son las reglas mismas: su sitio, su forma y su orden de prioridad | Agente | [`base/20-meta-reglas/base.md`](20-meta-reglas/base.md) | [`20 · Meta-reglas`](20-meta-reglas/base.md) |
| **Molde** | Como el molde de una torta: todas salen con la misma forma | La forma fija con que se escribe una regla: título, cuerpo de una a cuatro líneas y ejemplo | Agente | [`base/20-meta-reglas/estructura-regla.md`](20-meta-reglas/estructura-regla.md) | [`20·M5`](20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) |
| **N/A** | Abreviatura de «no aplica» | Lo que se escribe en la sección de un molde que no viene al caso, para no dejarla marcada ni borrarla | Agente, al llenar el documento | En el propio documento | [`13·DOC21`](13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) |
| **Núcleo blindado** | Núcleo porque está en el centro y todo lo demás se apoya en él | Las seis reglas de seguridad que no admiten excepción y que ninguna otra capa puede tocar | Usuario decide, agente redacta | [`base/00-nucleo-blindado.md`](00-nucleo-blindado.md) | [`00 · Núcleo blindado`](00-nucleo-blindado.md) |
| **Plantilla** | — | El esqueleto de un documento, con huecos por llenar; se parte de ella y no de memoria | Agente | `plantillas/` | [`13·DOC15`](13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) |
| **Regla** | — | Una exigencia, una sola, vaciada en el molde del estándar y acompañada de su ejemplo | Usuario decide, agente redacta | Un archivo por regla, en `reglas/` de su capítulo | [`20·M5`](20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) |
| **Registro de cambios** | — | La lista de qué cambió el estándar en cada versión y por qué | Agente | [`CHANGELOG.md`](../CHANGELOG.md) | [`20·M10`](20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) |
| **Validable** | Que se puede validar, o sea comprobar, sin opinar | Que un programa pueda decir sí o no sin opinar; cada regla declara si lo es | Agente, al escribir la regla | Se anota en [`validadores/reglas-validables.md`](../validadores/reglas-validables.md) | [`20·M9`](20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) |
| **Versión** | — | El número del estándar, en tres partes: obliga a cambiar, agrega sin obligar, o solo corrige redacción | Agente | [`VERSION`](../VERSION) | [`20·M10`](20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) |

---

## 3 · Lo que comprueba

Los programas que revisan que las reglas se cumplan, y las pruebas del trabajo.

| Término | Qué quiere decir el nombre | Qué es | Quién lo escribe | Dónde vive | Regla |
|---|---|---|---|---|---|
| **Alcance de corrida** | Hasta dónde alcanza la corrida: qué pruebas entran y cuáles no | Qué pruebas se corren en una fase: el módulo tocado y lo que la matriz de dependencias señale, no todo | Agente, en el plan de pruebas | §3.5 del plan de pruebas | [`02·F5`](02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) |
| **Cargador** | Carga las reglas, como quien carga el camión antes de salir | El programa que mete las reglas de `base/` en el contexto del agente al abrir la sesión | Agente | `validadores/cargador.py` | [`02·F1`](02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md) |
| **Caso de prueba** | — | Un escenario concreto con sus pasos y lo que se espera de cada uno | Agente, en el plan de pruebas | §6 del plan de pruebas | [`08·T7`](08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos) |
| **Enganche** | Traduce el inglés «hook»: el programa queda enganchado a un momento y se dispara solo | El disparador que hace correr un programa solo, sin que nadie se acuerde de llamarlo | Agente | `validadores/hook_*.py` | [`20·M9`](20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) |
| **Evidencia** | — | La prueba de que un criterio de aceptación quedó cumplido; sin ella no se marca cumplido | Agente | §5 del plan de trabajo, y el resultado de pruebas | [`13·DOC3`](13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md) |
| **Instalador** | — | El programa que deja el estándar puesto en un proyecto y su estructura creada | Agente | `validadores/instalar.py` | [`02·F13`](02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) |
| **Matriz de dependencias del refactor** | «Refactor» es reacomodar el código sin cambiar lo que hace | La tabla de qué se rompe cuando un archivo cambia lo que promete, y dónde se rompe | Agente, antes de escribir el plan | §2.2 del plan de trabajo | [`02·F17`](02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) |
| **Suite** | Del inglés «conjunto»: las pruebas que van juntas | Un conjunto de pruebas que se corren juntas, normalmente las de un módulo | Agente | Donde el proyecto guarde sus pruebas | [`02·F5`](02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) |
| **Trazabilidad** | De «trazar»: se puede seguir el trazo de una exigencia hasta lo construido | Poder seguir el hilo de cada exigencia hasta lo que se construyó, sin que falte ninguna | Agente, al cerrar | Tabla de cinco columnas del cierre | [`13·DOC3`](13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md), [`13·DOC11`](13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) |
| **Triangulación** | De la topografía: un punto se ubica mirándolo desde dos lados | Sacar el resultado esperado de una prueba por dos caminos distintos, en vez de adivinarlo | Agente, al armar las pruebas | El plan de pruebas | [`08·T7`](08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos) |
| **Validador** | — | Un programa corto que revisa una regla y dice si se cumple o no | Agente | `validadores/` | [`20·M9`](20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) |

---

## 4 · Lo que se guarda

La memoria escrita: lo que no se recupera leyendo el código.

| Término | Qué quiere decir el nombre | Qué es | Quién lo escribe | Dónde vive | Regla |
|---|---|---|---|---|---|
| **Análisis y su cierre** | — | Un estudio de algo, que no termina hasta que queda escrito qué se decidió | Agente | `analisis/`, con su tabla de decisiones | [`13·DOC8`](13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md) |
| **Bitácora** | Del cuaderno de a bordo de un barco: se anota cada cambio con su fecha | La tabla al final de un documento que dice quién lo cambió, cuándo y qué le cambió | Agente | Última sección del documento | [`13·DOC15`](13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md) |
| **Catálogo de módulos** | — | La lista de todas las piezas técnicas del proyecto, con su nombre y su especificación | Agente | `documentacion/` del proyecto | [`13·DOC13`](13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) |
| **Catálogo de reglas del proyecto** | — | La lista numerada de las reglas propias del proyecto, cada una nombrando el criterio de base que concreta | Agente | `.agente/reglas-proyecto.md` | [`13·DOC10`](13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md), [`20·M16`](20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) |
| **Hallazgo** | Lo que se halla trabajando, sin haberlo ido a buscar | Algo que aparece trabajando y que no se resuelve en el momento, anotado para que no se pierda | Agente, mientras aparece | El resumen de la sesión | [`13·DOC22`](13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) |
| **Histórico de sesiones** | — | La transcripción literal de cada conversación, con la hora leída del reloj del sistema | Agente, después de cada intercambio | `historico-chat/AAAA-MM-DD-<tema>.md` | [`13·DOC22`](13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) |
| **Mapa de dependencias** | — | Quién usa a quién dentro del proyecto; se consulta antes de planificar y se actualiza al cerrar | Agente | `documentacion/` del proyecto | [`13·DOC9`](13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md), [`13·DOC18`](13-documentacion/reglas/DOC18-actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad.md) |
| **Memoria del agente** | — | Cómo quiere el usuario que se trabaje, escrito en el repositorio y no en la herramienta | Agente, cuando el usuario lo indica | `historico-chat/memory/`, un archivo por recuerdo | [`01·C19`](01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) |
| **Nota** | — | Por qué se diseñó algo así, con las alternativas que se descartaron; no exige nada | Agente | `notas/` | [`20·M13`](20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) |
| **Pendiente** | — | Una mejora ya acordada que todavía no se hizo, versionada para que no dependa de que alguien la recuerde | Agente | `pendientes/` | [`20·M13`](20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) |
| **Resumen de sesión** | — | Lo que la sesión dejó: cada hallazgo con qué pasó, por qué importa y con qué se retoma | Agente, mientras aparece cada hallazgo | `historico-chat/resumenes/AAAA-MM-DD/` | [`13·DOC22`](13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) |
| **Retrodocumentación** | «Retro» es hacia atrás: se documenta después de construido | Escribirle la especificación a un módulo que ya está funcionando y nunca la tuvo, antes de tocarlo | Agente | Donde vivan las especificaciones del proyecto | [`13·DOC6`](13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md) |
| **Señal** | Como la señal de una carretera: avisa algo que no se ve desde el código | Lo aprendido que no se recupera leyendo el código: una decisión, un error resuelto, una trampa | Agente, al cerrar la unidad | `documentacion/senales.md` y la memoria buscable | [`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) |

---

## Lo que sigue en otro idioma

[`01·C20`](01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) pide que todo término se escriba traducido, y que el que no tenga traducción usada se deje tal cual y se explique la primera vez. Esta es la lista de los dos casos, verificada el 2026-08-14.

### Se quedan, porque no tienen traducción usada

| Término | Qué es | Por qué se queda |
|---|---|---|
| **commit** | Guardar en el historial un paquete de cambios | Es el nombre del comando y del objeto en toda herramienta de control de versiones. Nadie dice "confirmación" |
| **push** | Subir al repositorio compartido lo que se guardó | Igual que el anterior: es el comando |
| **endpoint** | La dirección de una aplicación que responde a una petición | "Punto final" significa otra cosa en español |
| **frontend** y **backend** | La parte que ve el usuario y la parte que corre en el servidor | Se usan así en todo el oficio hispanohablante |
| **lint** | Revisar el código en busca de errores de forma, sin ejecutarlo | Es el nombre de la clase de herramienta |
| **log** | El registro que un programa va dejando de lo que hace | "Bitácora" ya se usa acá para otra cosa: la tabla de cambios de un documento |
| **rollback** y **backfill** | Deshacer un cambio de datos, y rellenar hacia atrás lo que falta | Son los nombres de las maniobras en cualquier motor de base de datos |
| **slug** | El nombre corto y sin espacios con que se identifica algo en una ruta | No hay palabra en español que se use para esto |
| **opt-in** | La marca de un capítulo que solo aplica si el proyecto lo enciende | Es una marca del propio estándar. Está explicada donde aparece |
| **JSON**, **SQLite**, **FTS5**, **Gherkin**, **INVEST** | Nombres de formatos, programas y métodos | Son nombres propios. No se traducen |

### Falta traducirlos

Tienen traducción usada en español y siguen en inglés. **Cambiarlos es trabajo aparte**, con su propia historia de usuario: tocan los archivos de abajo y rompen las citas que los nombran. Esta tabla es el inventario, no la orden.

| Término | Cómo se diría | Dónde está hoy |
|---|---|---|
| **Explorer** | Explorador | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), `plantillas/estado-fase.md`, `notas/roles-especializados.md` |
| **Proposer** | Proponente | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), `plantillas/estado-fase.md`, `skills/proponer-alcance/SKILL.md` |
| **Épica Writer** y **HU Writer** | Quien escribe la épica, quien escribe la historia | `plantillas/estado-fase.md` |
| **Spec Writer** | Quien escribe la especificación | `plantillas/estado-fase.md`, `skills/generar-spec-modulo/SKILL.md` |
| **Designer** | Diseñador | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), `plantillas/estado-fase.md`, `skills/disenar-arquitectura/SKILL.md` |
| **Task Planner** | Planificador de tareas | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), `plantillas/estado-fase.md`, `skills/planificar-tareas/SKILL.md` |
| **Implementer** | Quien implementa | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), `plantillas/estado-fase.md`, `skills/implementar/SKILL.md` |
| **Verifier** | Verificador | [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md), `plantillas/estado-fase.md`, `skills/cerrar-fase/SKILL.md` |
| **Reviewer** | Revisor. El estándar ya lo llama Crítico en la mayoría de los sitios | `skills/revisar-critico/SKILL.md`, `notas/roles-especializados.md` |
| **Orchestrator** | Orquestador. [`00·ID6`](00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md) ya lo dice en español; las skills no | `skills/sdd-orchestrator/SKILL.md`, `notas/roles-especializados.md` |
| **Researcher** | Investigador | `notas/roles-especializados.md` |
| **spec** | Especificación. Se tradujo en el texto de las reglas el 2026-08-14, pero quedó en las descripciones de las skills y en nombres de archivo | `skills/*/SKILL.md`, `plantillas/plantilla-spec-modulo.md`, `documentacion/*/spec.md` |

**Cuántos archivos toca:** trece nombres en diez archivos entre [`base/README.md`](README.md), `plantillas/`, `skills/` y `notas/`, más los nombres de archivo que llevan `spec`. Renombrar un archivo rompe todo enlace que apunte a él, así que el cambio se hace de una vez y con su plan, no de a poco.
