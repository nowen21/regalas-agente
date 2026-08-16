# 02 · Flujo de trabajo  ·  `[CAPA 2]`

Cómo trabaja el agente: de la solicitud a la tarea terminada. La capa 3 define dónde viven los documentos y cómo se corren las pruebas.

**Una regla, un archivo.** Cada regla vive en su propio archivo dentro de [`reglas/`](reglas/), con el nombre `<PREFIJO><n>-<título>`. El prefijo del capítulo es **`F`** y es exclusivo suyo ([`20·M4`](../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)); el molde de cada regla es el de [`20·M5`](../20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md). En el archivo de la regla queda **solo la exigencia**; lo que la desarrolla, la ilustra o la justifica está aquí abajo, en [§ Detalle de cada regla](#detalle-de-cada-regla).

**Qué cumple cada regla y qué no:** cada una cierra con su resultado del [checklist del estándar](../20-meta-reglas/checklist.md). De las veintiuna vigentes, **diecisiete dan CUMPLE, tres no y una está pendiente de aplicar**: [`F4`](reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) por llevar dos exigencias, [`F5`](reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) porque el dueño del tema es otro capítulo, [`F12`](reglas/F12-relacion-y-nomenclatura-de-fases.md), y [`F13`](reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) que no lo trae aplicado. [`F6`](reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md) y [`F7`](reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md) quedaron **derogadas** en 4.0.0 a favor de [`13·DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md) y [`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md). Una auditoría posterior lo lee ahí y no las vuelve a analizar.

**La estructura se pone antes que todo.** [`F13`](reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) se aplica antes que [`F1`](reglas/F1-carga-el-contexto-antes-de-actuar.md) y que cualquier paso del flujo; el número es catálogo, no orden de ejecución. Su árbol de estructura está en [`estructura-base.md`](estructura-base.md).

---

## Las reglas de este capítulo

| Regla | Qué exige | Checklist |
|---|---|---|
| [`F0 · Recorre la cadena completa, sin saltar eslabones`](reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) | `planteamiento → épica → HU → especificación → plan → código`: ningún eslabón se salta por tamaño. | CUMPLE |
| [`F1 · Carga el contexto antes de actuar`](reglas/F1-carga-el-contexto-antes-de-actuar.md) | Revisar la documentación del proyecto antes de analizar, implementar o negar que algo exista. | CUMPLE |
| [`F2 · Sin especificación acordada no hay código`](reglas/F2-sin-spec-acordada-no-hay-codigo.md) | Sin especificación el código es opinión del agente; primero se acuerda, después se codifica. | CUMPLE |
| [`F3 · Ejecuta seguido el plan aprobado`](reglas/F3-ejecuta-seguido-el-plan-aprobado.md) | Todos los cambios seguidos; solo pausa lo que el plan no cubre. | CUMPLE |
| [`F4 · Todo plan lleva su plan de pruebas y su aprobación explícita`](reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) | Plan y pruebas presentados, y OK explícito antes de tocar código. | NO CUMPLE |
| [`F5 · Corre solo las suites que la fase toca`](reglas/F5-corre-solo-las-suites-que-la-fase-toca.md) | Corrida quirúrgica: el módulo, lo refactorizado y lo que la matriz señala. | NO CUMPLE |
| [`F6 · Persiste el trabajo y las decisiones antes de cerrar la fase`](reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md) | **Derogada en 4.0.0** → [`13·DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md). | DEROGADA |
| [`F7 · No cierres una fase con trazabilidad incompleta`](reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md) | **Derogada en 4.0.0** → [`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md). | DEROGADA |
| [`F8 · Edita solo los archivos que el plan aprobado declara`](reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) | El plan es contrato; el archivo que aparece de más detiene la ejecución. | CUMPLE |
| [`F9 · No subdividas ni renegocies un plan ya aprobado`](reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md) | Si el volumen amerita subfases, se proponen antes de aprobar, no después. | CUMPLE |
| [`F10 · Planifica la migración en vez de postergar por producción`](reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md) | Asumir "probablemente está en prod" y declarar la estrategia. | CUMPLE |
| [`F11 · Una fase solo modifica código de su propio módulo`](reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md) | Lo que toca a otro módulo se agenda como fase propia. | CUMPLE |
| [`F12 · Relación y nomenclatura de fases`](reglas/F12-relacion-y-nomenclatura-de-fases.md) | Épica → HU → Fases, con el identificador y la ruta física de la fase. | NO CUMPLE |
| [`F13 · Deja la estructura base puesta antes de trabajar`](reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) | La estructura se crea sola; qué va dentro de `proyectos/` lo decide el usuario. | pendiente |
| [`F14 · Responde las trece preguntas en todo plan de trabajo`](reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) | Las trece cierran la ambigüedad antes de escribir código. | CUMPLE |
| [`F15 · No saltes ni reordenes las once etapas de la fase`](reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) | El ciclo va en orden, de la declaración macro a la publicación. | CUMPLE |
| [`F16 · Declara los cinco componentes de cada intervención del plan`](reglas/F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md) | Qué, cómo, dónde, por qué y con qué impacto — sin verbos vagos. | CUMPLE |
| [`F17 · Verifica contra el proyecto real todo lo que el plan afirma`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) | Rutas y firmas comprobadas; nada aproximado ni `TBD`. | CUMPLE |
| [`F18 · Deriva el plan de los CA aprobados, no de la proactividad`](reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) | Cada intervención del plan rastrea a un criterio de aceptación. | CUMPLE |
| [`F19 · Implementa literal el criterio de aceptación`](reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) | Ni más ni menos que el CA; su redacción es la especificación. | CUMPLE |
| [`F20 · Para y propón lo que descubras fuera del CA`](reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) | Lo que "convendría" agregar se muestra y espera decisión. | CUMPLE |
| [`F21 · Un incumplimiento ya identificado no se repite en lo nuevo`](reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) | Lo que ya se sabe que está mal no se vuelve a producir. | CUMPLE |
| [`F22 · No avances de fase con una derogación sin adoptar`](reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) | Con una regla derogada sin adoptar, lo único que se abre es la fase que la adopta: una por cada HU que la implementaba. | CUMPLE |

**Derogadas** ([`20·M11`](../20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) — el texto se conserva y el ID no se reutiliza): [`F4.1`](reglas/F4.1-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) → [`F14`](reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) · [`F4.2`](reglas/F4.2-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) → [`F15`](reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) · [`F4.3`](reglas/F4.3-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) → [`F16`](reglas/F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md) y [`F17`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) · [`F4.4`](reglas/F4.4-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) → [`F18`](reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md) · [`F4.5`](reglas/F4.5-implementa-literal-el-ca-y-propon-lo-que-sobre.md) → [`F19`](reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) y [`F20`](reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md).

---

## El mapa del flujo — de la necesidad al cierre

Este capítulo detalla sobre todo **del plan hacia abajo**. Pero un desarrollo empieza **antes** del plan. Esta es la secuencia macro completa, con dónde vive la regla de cada paso — es un mapa para ubicarse, no una orden: la orden es [`F0`](reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md).

| # | Paso | Qué responde | Dónde está la regla |
|---|---|---|---|
| 0 | **Necesidad / idea** | qué quiere resolver el negocio | se escribe **siempre** como **planteamiento** (`plantillas/planteamiento.md` → `prompts/<slug>-planteamiento.md`) |
| 1 | **Análisis / contexto** | qué existe hoy, restricciones, normativa | [`F1`](reglas/F1-carga-el-contexto-antes-de-actuar.md) · [`F17`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) · skill `analizar-proyecto` |
| 2 | **Objetivo + criterio de éxito** | qué se logra y cómo se sabe que se logró | [`00 · Identidad y rol`](../00-identidad-y-rol/base.md) · skill `proponer-alcance` |
| 3 | **Alcance (qué SÍ / qué NO)** | el borde del trabajo | skill `proponer-alcance` · [`01·C3`](../01-conducta.md#c3--quédate-en-tu-tarea) |
| 4 | **Épica / Feature** | el bloque grande de funcionalidad | [`13·DOC16`](../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) |
| 5 | **HU** | la épica descompuesta en historias con criterios de aceptación | [`13·DOC15`](../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md) |
| 6 | **Fase (ejecución)** — especificación → plan → implementar → probar → cerrar → commit | cómo y cuándo se construye | [`F2`](reglas/F2-sin-spec-acordada-no-hay-codigo.md)–[`F11`](reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md) · las once etapas de [`F15`](reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md) |

**Épica, módulo y fase no son lo mismo.** La **épica** es unidad de *necesidad* —agrupa historias afines por el valor que entregan— y su definición vive en [`13·DOC16`](../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md). El **módulo** es unidad *técnica* y vive en [`13·DOC13`](../13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md). La **fase** es unidad de *ejecución* —un plan con su cierre y su commit— y su relación con la HU y su nomenclatura las fija [`F12`](reglas/F12-relacion-y-nomenclatura-de-fases.md), fuente única.

**Secuencia del plan hacia abajo:** contexto ([`F1`](reglas/F1-carga-el-contexto-antes-de-actuar.md)) → especificación ([`F2`](reglas/F2-sin-spec-acordada-no-hay-codigo.md)) → línea base verificada ([`F16`](reglas/F16-declara-los-cinco-componentes-de-cada-intervencion-del-plan.md) · [`F17`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)) → plan y pruebas ([`F4`](reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) que responden las trece preguntas ([`F14`](reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)) derivadas de los CA ([`F18`](reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)) → pausa y aprobación explícita ([`F4`](reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) → ejecutar ([`F3`](reglas/F3-ejecuta-seguido-el-plan-aprobado.md)), literal a los CA ([`F19`](reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) · [`F20`](reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)), solo los archivos del plan ([`F8`](reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)), completo ([`F9`](reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md)), dentro del módulo ([`F11`](reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md)) y con migración incremental cuando toca prod ([`F10`](reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)) → pruebas ([`F5`](reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)) → persistir ([`13·DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)) → trazabilidad ([`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md)) → cerrar.

---

## Detalle de cada regla

Lo que desarrolla, ilustra o justifica cada regla. La **exigencia** vive en su archivo de [`reglas/`](reglas/); esto es su explicación.

### F2 — el orden de los dos pasos

1. **¿Existe la especificación?** (la capa 3 dice dónde). Si no, ofrece redactar un borrador y hacerlo aprobar antes de tocar nada.
2. **¿El requerimiento ya está dentro?** Si está y falta implementarlo, se implementa donde debía ir. Si no está, **primero se actualiza la especificación** y después se codifica.

La capa 3 puede ajustar cuán estricta es la regla, pero viene **activada por defecto**.

### F4 — las plantillas y los cinco pasos de la aprobación

El `plan_trabajo` sigue `plantillas/planes/trabajo.md`; el `plan_pruebas` sigue `plantillas/planes/pruebas.md`, con trazabilidad CA→caso y el alcance de corrida de [`F5`](reglas/F5-corre-solo-las-suites-que-la-fase-toca.md). Ambos se guardan en la ruta de la fase ([`F12.13`](reglas/F12-relacion-y-nomenclatura-de-fases.md)). La capa 3 puede ajustar las secciones opcionales por proporcionalidad.

Lo que **se aprueba** son esos dos. Lo que pasa al ejecutarlos va en el `resultado_pruebas` (`plantillas/planes/resultados.md`), que se crea al correr la primera prueba y de donde sale el veredicto de la fase: **el plan aprobado no se modifica para anotarle resultados**, porque entonces se pierde contra qué comparar.

La aprobación no es un hito abstracto, es una secuencia operativa: **1)** redactar los dos documentos · **2)** PAUSAR, sin tocar código · **3)** presentarlos con un resumen corto de qué hará · **4)** esperar el OK explícito o la iteración de cambios · **5)** solo con el OK, implementar ([`F3`](reglas/F3-ejecuta-seguido-el-plan-aprobado.md)).

### F14 — las trece preguntas

Un plan de trabajo no es texto libre: es un contrato con el usuario y con quien continúe el proyecto. Un lector nuevo —otro dev, el futuro yo, el usuario en seis meses— tiene que leer solo el plan y saber qué se va a hacer, dónde queda visible, cómo se verifica y cómo se revierte, sin abrir código. Estas son las trece:

1. **¿Qué es esta fase y a qué módulo pertenece?** Código de fase, slug, fecha de apertura, referencia al especificación del módulo.
2. **¿Por qué nace esta fase?** Origen: funcionalidad nueva, modificación de una fase anterior, híbrido. Qué requerimiento, gap o hallazgo la dispara.
3. **¿Qué carencias documentadas del módulo cierra?** Puntero explícito al documento de origen.
4. **¿Qué entra en el alcance y qué NO?** Fuera-de-scope explícito.
5. **¿Qué cambia técnicamente?** Un bloque por artefacto —esquema, modelos, servicios, eventos, componentes, comandos— con su firma y la regla que aplica.
6. **¿Qué rutas o endpoints nuevos se exponen y con qué control de acceso?** Autenticación, permiso y alcance.
7. **¿Dónde queda accesible para el usuario final?** El punto de entrada en la interfaz. Si la fase no introduce navegación, se declara.
8. **¿Qué permisos o roles nuevos hay que sembrar?** Con la nomenclatura del proyecto.
9. **¿Qué archivos se crean o modifican?** Tabla `Archivo | Nuevo/Modificar | Nota`, con cada ruta verificada contra el proyecto real ([`F17`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)).
10. **¿Cómo se verifica que quedó bien?** Criterios de aceptación medibles.
11. **¿Cómo se revierte si algo sale mal?** Plan B concreto.
12. **¿Toca algo que puede estar en producción y cómo se migra sin bloquear?** ([`F10`](reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)).
13. **¿Qué reglas del estándar y del proyecto se aplican?** Lista por identificador.

Las trece son **genéricas**: aplican a cualquier proyecto. La capa 3 (`.agente/`) especializa **cómo** se responde cada una —qué archivo es la navegación, qué framework de permisos usa, dónde vive el plan—, pero no reduce la lista.

### F15 — las once etapas, quién actúa y qué cierra cada una

| # | Etapa | Quién actúa | Hito de cierre |
|---|---|---|---|
| 1 | **Declaración macro de la fase** en el especificación del módulo (§Fases) | Agente redacta · usuario aprueba la especificación en su momento | Bloque de fase con su identificador ([`F12.6`](reglas/F12-relacion-y-nomenclatura-de-fases.md)), origen, alcance macro y fuera-de-scope |
| 2 | **Disparo / autorización de inicio** | Usuario ("arranque con X") | El agente puede empezar a diseñar el plan detallado |
| 3 | **Diseño del plan detallado** — `plan_trabajo` + `plan_pruebas` | Agente | Documentos redactados. NO toca código todavía |
| 4 | **Pausa y presentación** al usuario | Agente | Mensaje con resumen y punteros a los documentos |
| 5 | **Aprobación del plan detallado** | Usuario | OK explícito → pasa a 6 · pide cambios → vuelve a 3 |
| 6 | **Ejecución continua** ([`F3`](reglas/F3-ejecuta-seguido-el-plan-aprobado.md)) | Agente | Plan implementado; pausa solo por descubrimiento genuino |
| 7 | **Pruebas** ([`F5`](reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)) | Agente | `resultado_pruebas` escrito, con veredicto por CA. Si falla: diagnostica, corrige, vuelve a correr y agrega el ciclo nuevo sin pisar el anterior |
| 8 | **Cierre documental** ([`13·DOC1`](../13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md), [`13·DOC3`](../13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md)) | Agente | Documentación completa; trazabilidad sin faltantes |
| 9 | **Commit único** de la fase | Agente | Mensaje que resume el porqué. Publicar es acción aparte |
| 10 | **Reporte al usuario** | Agente | Hash + resumen + estado de pruebas + próxima fase natural |
| 11 | **Publicación / despliegue** | Usuario autoriza → agente ejecuta | Cambios publicados. Requiere autorización explícita ([`00·N2`](../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)) |

Las etapas 4, 5, 10 y 11 son las que el flujo suele saltarse: separan el disparo macro (2) de la aprobación del plan detallado (5), y el commit (9) de la publicación (11).

### F16 — qué se espera de cada componente

**QUÉ** es la acción concreta —crear, modificar, eliminar, migrar—, no un verbo vago. **CÓMO** es el mecanismo técnico específico: agregar el campo `X` a la tabla `Y`, extender `foo()` con el parámetro `bar`, inyectar el servicio `Z` en el constructor. Con suficiente detalle para que otro dev lo ejecute igual. **DÓNDE** es la ruta exacta; si el archivo todavía no existe, "crear en `<ruta exacta>`". **POR QUÉ** es qué gap cierra, qué requerimiento cumple o qué defecto corrige. **IMPACTO** es qué más se ve afectado: consumidores del código tocado, pruebas que hay que actualizar, riesgos y reversibilidad.

### F17 — cómo se construye la línea base

Antes de redactar el plan (etapa 3 del ciclo):

1. **Cargar contexto** ([`F1`](reglas/F1-carga-el-contexto-antes-de-actuar.md)). El plan es el segundo paso, no el primero.
2. **Consultar el mapa de dependencias del proyecto**, si lo mantiene ([`13·DOC9`](../13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)): una lectura contra información ya organizada es mucho más rápida que escanear el proyecto entero. Si no existe, ir al punto 3.
3. **Descubrir sobre el código real** solo donde el mapa no cubra o lo contradiga: enumerar archivos, buscar símbolos, leer lo relevante, mirar el historial. Acotado a la duda concreta.
4. **Verificación cruzada.** Si el plan dice "extender el método `foo()`", abrir el archivo y comprobar que existe y cuál es su firma.
5. **Documentar el estado inicial** cuando ayude: "hoy tiene X, se agrega Y" es más útil que "agregar Y".
6. **Matriz de dependencias del refactor — obligatoria cuando el módulo cambia contratos de código existente.**

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Ubicación del rompimiento |
|---|---|---|---|
| `<archivo A>` | eliminar columna X · renombrar método Y · cambiar la cardinalidad de Z | `<archivo B> · <archivo C>` | `B: lee el atributo X` · `C: carga la relación Y` |

La tabla de archivos del plan ([`F14`](reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) pregunta 9) es la unión de {archivos del refactor} ∪ {dependientes **directos** que rompen} — nunca solo el primer conjunto. Lo que no se pueda refactorizar en esta fase se declara en §Fuera-de-scope con su "queda para Fase X"; nunca se ignora en silencio.

**No se encadenan dependencias transitivas.** Si A depende de B, ajustar B es necesario o se difiere explícitamente; pero no se sigue la cadena B→C→D, que expande la fase infinitamente. Cuando un archivo se difiere, **todo lo que depende de él se difiere con él** — incluidas sus pruebas. De ahí la regla derivada: una prueba refactorizada solo puede depender de código refactorizado en la misma fase o del código base ya estable. Jamás se refactoriza una prueba esperando que quede verde contra algo que se difirió.

**Proporcionalidad.** El análisis se escala con el número de archivos que rompen: **≤ 5** análisis mínimo (mapa + verificación puntual) · **6–15** análisis medio (verificación dirigida de cada archivo que rompe) · **> 15** análisis exhaustivo justificado.

**Qué se escala al usuario y qué no.** Se cierran con criterio profesional las decisiones puramente técnicas —nomenclatura de rutas, orden de migración, cascadas en claves foráneas, cardinalidad, código idiomático del framework— y se declaran en el plan. Se escalan las que impactan la interfaz visible, el contrato de una API, los cambios destructivos de datos, el alcance de la fase o la deuda estructural. Listar diez decisiones cuando siete son triviales sobrecarga al usuario y retrasa la fase.

### F18 — las dos rutas del ítem sin CA

Un ítem que no rastrea a ningún criterio de aceptación tiene **dos salidas y solo dos**: es **soporte técnico obligatorio** —sin él el CA no funciona—, y entonces se declara en §Alcance con su justificación; o es **proactividad**, y entonces se retira del plan y se propone como fase separada con su propia HU.

Anti-patrones: escribir el plan antes de tener los CA aprobados · tocar código antes de que el plan esté persistido y aprobado · agregar "también aprovechamos para X" · ceñirse a lo que el agente infirió cuando el usuario dio N criterios concretos.

### F19 y F20 — los tres momentos donde el agente se desvía

Al **construir el plan**, un ítem que "conviene técnicamente" pero no viene de CA se propone antes de agregarlo. Al **escribir código**, la implementación cumple el CA sin agregar guards, validaciones o efectos que el CA no pide. Al **responder una pregunta**, la pregunta se responde: no se convierte en autorización para editar, corregir o refactorizar ([`01·C3`](../01-conducta.md#c3--quédate-en-tu-tarea)).

Anti-patrones concretos: agregar un guard en el servidor cuando el CA solo pide ocultar un botón · interpretar "¿de dónde sale X?" como orden de corregir · "aprovechamos y limpiamos el legacy" · "el CA dice X pero conviene X + Y" · "es defensa en profundidad, es buena práctica" — aunque lo sea, si no está en el CA se propone, no se actúa.

**Las tres respuestas posibles a una propuesta de [`F20`](reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md).** *"Sí, agrégalo"* → o entra como CA nuevo de la HU antes de continuar (lo recomendable si es funcional), o se declara soporte técnico obligatorio de un CA existente ([`F18`](reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)) con su justificación. *"No"* → se descarta y no se vuelve a mencionar. *"Después"* → se anota como brecha en el especificación del módulo y se retoma en fase futura.

### F5 — qué no se corre por defecto

Fuera de la corrida quedan la suite completa del proyecto "por si acaso", las suites de módulos que no aparecen en la matriz de dependencias, y las que solo comparten infraestructura —base de datos, autenticación— sin tocar el código refactorizado. El anti-patrón es correr todo al terminar: cientos de pruebas, varios minutos, más memoria y ruido de rojos que ya existían antes de la fase.

### F8 — el protocolo al descubrir un archivo fuera del plan

**1)** PAUSAR, sin editar ese archivo · **2)** reportar qué archivo, qué hallazgo lo hace necesario y qué impacto tiene ignorarlo · **3)** proponer la ampliación del plan, actualizando la tabla de archivos y el §Alcance si cambia · **4)** esperar el OK explícito · **5)** solo con el OK, retomar.

Si el análisis previo ([`F17`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)) fue insuficiente, la ampliación es la corrección — no un atajo silencioso. [`F17`](reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) es la primera defensa: reduce los descubrimientos. [`F8`](reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) es la segunda: cuando ocurren igual, no se procesan en silencio.

### F9 — por qué la pausa es la excepción

El usuario aprobó porque confía en que la ejecución es coherente con lo pactado. Cada pregunta nueva después de "aprobado" rompe esa confianza y le devuelve un peso decisional que ya estaba resuelto. Entregar "a medias" por volumen es la misma falla: la solución se entrega funcional, no en pedacitos que dejan al usuario decidiendo cada micro-paso.

### F10 — la estrategia según el tipo de cambio

| Tipo de cambio | Estrategia |
|---|---|
| **Aditivo** (columna nueva, tabla nueva) | Migración nueva, con backfill dentro del script si aplica. Nada destructivo. |
| **Rename** (columna, tabla, artefacto persistente) | Migración nueva reversible. **No** se edita la migración original de una fase cerrada. |
| **Drop con datos** | Avisar el riesgo específico antes de aplicar. Con el OK, migración con reversa que reconstruye el tipo original. |
| **Cambio de tipo o restricción** | Avisar el riesgo específico (truncamiento, incompatibilidad). Con el OK, estrategia sin downtime documentada. |
| **Refactor grande sobre varias tablas** | Dividir en fases ordenadas por seguridad: aditivas primero, destructivas al final con backfill previo. |

No es válido preguntar "¿está en producción?" para decidir **si** hacer el trabajo, postergar una fase sin haber propuesto migración, ni editar la migración de una fase cerrada asumiendo que no está en producción. Sí es válido preguntarlo para **elegir estrategia**: ambas rutas producen el resultado correcto. El sistema es vivo; preguntar antes de cada cambio y postergar por miedo convierte el desarrollo en parálisis.

### F11 — qué hacer cuando aparece un archivo ajeno

Si durante la ejecución aparece un archivo de otro módulo que rompería por la fase actual, se pausa ([`F8`](reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)), se notifica y se proponen dos opciones: **A)** documentar el break como esperado en el especificación del módulo dueño y agendar su fase propia · **B)** hacer el cambio mínimo indispensable con nota explícita en el commit y registro en el especificación del dueño. **Decide el usuario, no el agente.**

Trabajo adelantado que "se metió" en una fase por error: si el usuario lo aprueba después, se mantiene y se documenta con nota en el especificación del módulo dueño ([`13·DOC7`](../13-documentacion/reglas/DOC7-registra-el-cruce-en-los-dos-documentos-que-se-referencian.md)), pero **no** se documenta como cerrado — cada módulo tendrá su fase formal cuando le toque.

### F13 — el alcance de la estructura y quién decide qué

**Solo pone estructura.** No detecta el stack, no conoce el propósito, el dominio ni la funcionalidad del proyecto. Si al crear la estructura el agente usa información del stack o del dominio, el flujo está mal: eso corresponde a etapas posteriores.

**Dos mundos separados.** `proyectos/` es del usuario: el agente crea la **carpeta** —la exige la norma, no es una decisión— pero **nunca toca su contenido**: no lo modifica, no lo reestructura, no asume su organización, no mueve código adentro. `.agente/`, `prompts/` y `documentacion/` son el espacio del agente, que él crea y gestiona al lado. Organizar `proyectos/` corresponde **exclusivamente al usuario**.

**Quién crea la estructura.** El instalador del estándar (`validadores/instalar.py`), en el primer paso de cada sesión. Crearla es parte de la instalación, no una tarea que se le encarga al usuario: pedirle que hiciera a mano una carpeta que la norma ya exige dejaba la instalación parada en el primer paso, y un proyecto a medio instalar es un proyecto sin reglas.

**Cuando hay código fuera de `proyectos/`,** el agente crea la carpeta vacía, avisa qué encontró afuera y **no mueve nada**: si el código se muda o se queda es decisión del usuario, y moverlo rompe rutas, importaciones y despliegues que el agente no conoce.

---

Molde para crear una fase: `plantillas/fase.md`.
