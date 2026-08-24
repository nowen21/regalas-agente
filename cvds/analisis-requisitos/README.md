# Análisis de requisitos: ¿qué debe hacer el sistema?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué** tiene que hacer el estándar de trabajo heredable, sin decir todavía cómo.

> **Escrito como si no hubiera nada construido**, que es lo que pide la etapa: sale del problema y de los doce objetivos de [cvds/planificacion/README.md](../planificacion/README.md), no del repositorio.

**Estado: BORRADOR** (2026-08-24, sin aprobar).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| El problema, el alcance y los doce objetivos | Planificación | Sí, el 2026-08-24 |
| Las restricciones: sin costo, sin plazo, `.md` como fuente y `.docx` como salida | Planificación | Sí, el 2026-08-24 |
| Los supuestos, con el de que el agente obedece lo que se le carga | Planificación | Sí, aunque el supuesto 2 sigue sin confirmarse |

## 2. De dónde salieron los requisitos

| Fuente | Quién | Técnica | Cuándo | Dónde quedó lo acordado |
|---|---|---|---|---|
| Quien usa el sistema a diario | El autor, que delega trabajo al agente | Observación de su propio trabajo: cada vez que el agente se desvió, quedó anotado | Desde el inicio, en cada sesión | [prompts/](../../prompts/), con sus palabras y sin reescribir |
| Lo que ya se intentó | El autor | Revisión de lo que falló: corregir por chat, y guardar preferencias en la herramienta | Antes de empezar | Sección 1 de [cvds/planificacion/README.md](../planificacion/README.md) |
| Lo que el usuario pidió dos veces | El autor | Barrido de lo repetido al cerrar cada versión | Periódico | Las candidatas a regla |
| Los proyectos que heredarían | Ninguno todavía | Sin consultar | — | Nada |

**Quién no se consultó, y por qué:** nadie ajeno al autor. No hay todavía un segundo usuario, y esa es la duda 1 de la sección 10. **Todos los requisitos de abajo salen de una sola persona**, y eso es un límite del análisis, no un detalle.

## 3. Los requisitos funcionales

> Prioridad en cuatro grados: **debe** (sin esto no sirve), **debería** (importante, opera sin ello), **podría** (si sobra tiempo), **no será** (excluido de esta versión).

| ID | Qué debe hacer el sistema | Quién lo necesita | Origen | Objetivo del que sale | Prioridad |
|---|---|---|---|---|---|
| RF-01 | Cargar las reglas al abrir la sesión, sin que nadie lo pida | El usuario | Observación del propio trabajo | 1 | Debe |
| RF-02 | Impedir que se cambie el estado del proyecto sin autorización | El usuario | Observación del propio trabajo | 6, 7 | Debe |
| RF-03 | Comprobar por sí solo lo que las reglas exigen | El usuario | Lo que ya se intentó y falló | 4 | Debe |
| RF-04 | Declarar como no verificado lo que no tenga prueba corrida | El usuario | Observación del propio trabajo | 4, 5 | Debe |
| RF-05 | Instalarse en un proyecto ajeno y decirle qué versión adoptó | El usuario | Lo que el usuario pidió dos veces | 2 | Debe |
| RF-06 | Avisar cuando la versión adoptada quede atrás, y qué cambió | El usuario | Lo que el usuario pidió dos veces | 2 | Debería |
| RF-07 | Escribir fuera del chat lo que cada sesión dejó | El usuario | Lo que ya se intentó y falló | 8 | Debe |
| RF-08 | Tapar toda credencial antes de que quede escrita | El usuario | Observación del propio trabajo | 9 | Debe |
| RF-09 | Exigir el documento del ciclo en el momento en que se construye | El usuario | Observación del propio trabajo | 10, 11 | Debe |
| RF-10 | Generar el `.docx` de cada documento desde su `.md` | Quien recibe el proyecto | Lo que el usuario pidió dos veces | 12 | Debería |
| RF-11 | Medir el tiempo que el usuario dedica a revisar | El usuario | Observación del propio trabajo | 3 | Podría |
| RF-12 | Mostrar en una pantalla los documentos del ciclo y lo que el agente guarda | El usuario | Lo que el usuario pidió dos veces | 14 | Debería |
| RF-13 | Guardar lo aprendido y poder consultarlo en la sesión siguiente | El usuario | Lo que ya se intentó y falló | 8, 14 | Debe |
| RF-14 | Comprobar que una pieza nueva no rompió lo que ya servía | El usuario | Observación del propio trabajo | 13 | Debe |

**El alcance ítem por ítem, con la ficha de cada uno, está en [inventario-funcionalidades.md](inventario-funcionalidades.md)**: catorce funcionalidades, `F-001` a `F-014`, una por cada requisito de esta tabla. Esta tabla es el resumen que se acuerda; aquella es el detalle que se construye.

## 4. Los requisitos no funcionales

| ID | Frente | Exigencia, con su número | Cómo se comprueba |
|---|---|---|---|
| RNF-01 | Rendimiento | Lo que corre al abrir la sesión no puede demorarla más de dos segundos | Se mide el enganche de apertura sobre un repositorio de mil archivos |
| RNF-02 | Disponibilidad | Funciona sin red y sin servicio externo: todo vive en el repositorio | Se corre con la máquina desconectada |
| RNF-03 | Seguridad y acceso | Ninguna credencial queda escrita en ningún archivo del repositorio | Comprobación que rechaza el guardado si encuentra una |
| RNF-04 | Datos personales y normativa | El estándar no recoge ni almacena datos de personas | Revisión de lo que se escribe en cada documento |
| RNF-05 | Usabilidad | Lo entiende quien no conoce el proyecto: sin siglas sin explicar | Cada documento se lee de principio a fin sin abrir otro |
| RNF-06 | Compatibilidad | Corre con Python de la biblioteca estándar, sin instalar nada | Se ejecuta en una máquina recién formateada |
| RNF-07 | Portabilidad | Se instala en cualquier proyecto sin tocar su código | Instalación de prueba en un proyecto ajeno |
| RNF-08 | Compatibilidad hacia atrás | Una versión nueva no rompe lo que servía en la anterior, y si obliga a rehacer algo lo declara | Se corre lo que ya servía contra cada versión antes de publicarla |
| RNF-09 | Crecimiento | Una pieza nueva entra sin obligar a reescribir las anteriores | Agregar una pieza no cambia archivos de las otras |

## 5. Las reglas del negocio

| # | Regla | Quién la dicta | Qué pasa si se rompe |
|---|---|---|---|
| RN-1 | Lo que se acuerda se escribe en el repositorio, no en el chat | El usuario | La corrección se pierde y hay que darla de nuevo |
| RN-2 | Ningún cambio de estado sin aprobación explícita del usuario | El usuario | Se pierde trabajo que nadie autorizó, y con eso la confianza |
| RN-3 | Lo que no se puede deshacer se aprueba una por una | El usuario | Un plan aprobado termina cubriendo lo irreversible |
| RN-4 | No se afirma sobre lo que no se leyó | El usuario | Veredictos falsos, que hacen desconfiar de los verdaderos |
| RN-5 | El estado de una funcionalidad lo fija la prueba corrida, no la lectura | El usuario | Se entrega como terminado lo que nadie comprobó |
| RN-6 | Nada se renumera ni se borra: se deroga | El usuario | Se rompen las citas de documentos y trabajos ya cerrados |
| RN-9 | Una credencial no se escribe, no se registra y no se guarda | El usuario | Queda expuesta en un archivo que se versiona y se publica |

> La numeración salta porque es la misma del inventario: cada ficha cita sus reglas por este identificador.

## 6. Los actores y sus permisos

| Actor | Qué hace en el sistema | Qué no puede hacer |
|---|---|---|
| El usuario | Aprueba, corrige, adopta versiones | Nada le está vedado: es quien manda |
| El agente | Escribe, construye, comprueba y reporta | Cambiar el estado del proyecto sin aprobación, o declarar terminado lo no probado |
| El proyecto que hereda | Adopta una versión y recibe avisos | Modificar las reglas heredadas en su copia |

## 7. Los casos de uso

| # | Caso de uso | Actor | Precondición | Qué debe quedar al terminar | Flujos alternos y de error |
|---|---|---|---|---|---|
| CU-01 | Abrir una sesión de trabajo | El usuario | El proyecto tiene el estándar instalado | Las reglas cargadas, y el aviso de qué versión rige | Sin reglas en la ruta: lo dice y la sesión sigue sin ellas · Con versión atrasada: avisa qué cambió · Con una regla ilegible: la nombra y carga el resto |
| CU-02 | Pedirle al agente un cambio | El usuario | Sesión abierta | El cambio hecho, o detenido con el motivo | Acción irreversible: se aprueba aparte, aunque estuviera en el plan · Sin aprobación: queda detenido · Falla a mitad: se revierte y se dice qué quedó a medias |
| CU-03 | Cerrar una unidad de trabajo | El agente | La unidad tiene plan y pruebas aprobados | El veredicto por criterio y el documento de cierre | Sin prueba corrida: queda «sin verificar» y no cierra · Prueba fallida: queda «no cumple» con lo que falló · Documento con espacios sin llenar: no se da por entregado |
| CU-04 | Instalar el estándar en otro proyecto | Quien instala | El proyecto está en control de versiones y sin cambios sin guardar | Los archivos agregados y la versión adoptada anotada | El proyecto ya tiene archivos con esos nombres: avisa y se detiene · Sin aprobación: no instala · Falla a mitad: se quita lo agregado y nada suyo se tocó |
| CU-05 | Pasarle una credencial al agente | El usuario | Sesión abierta | El trabajo hecho, y la clave tapada en todo lo que se guardó | Clave sin comillas: se tapa igual · Palabra que solo parece clave: queda tal cual · Clave ya escrita antes: se rota y se limpia el rastro |
| CU-06 | Recibir el entregable de ofimática | Quien recibe el proyecto | Los documentos del ciclo están escritos | El `.docx` generado desde el `.md` | Documento con espacios sin llenar: avisa antes de generar · Documento sin su molde: no se genera |
| CU-07 | Revisar desde la pantalla qué hay y qué guardó el agente | El usuario | La interfaz local está levantada | Lo que buscaba, leído sin abrir archivo por archivo | Sin base de datos: muestra los documentos y avisa que la memoria no está · Documento borrado del disco: lo dice en vez de mostrarlo vacío |
| CU-08 | Recuperar en una sesión lo aprendido en otra | El agente | Hay algo guardado de antes | Lo aprendido, disponible sin que el usuario lo repita | Nada guardado sobre el tema: lo dice, no inventa · Guardado que ya no es cierto: se corrige y queda la corrección |
| CU-09 | Publicar una versión nueva | El autor | Lo nuevo está construido y probado | La versión publicada, con lo que cambió | Rompe algo que servía: no se publica hasta corregirlo · Obliga a rehacer algo: se declara antes de publicar |

## 8. La trazabilidad

| Requisito | Funcionalidad que lo ejecuta | Módulo que lo implementa | Caso de prueba que lo demuestra |
|---|---|---|---|
| RF-01 | F-001 | Cargador de sesión | Abrir con reglas, sin ellas, y con una rota |
| RF-02 | F-002 | Enganches | Borrado sin aprobar, con aprobación, y acción fuera del plan |
| RF-03 | F-003 | Comprobaciones | Documento que cumple, uno que no, y uno a medio llenar |
| RF-04 | F-004 | Comprobaciones | Con prueba, sin prueba, y con prueba fallida |
| RF-05 | F-005 | Instalador | Proyecto vacío, y proyecto con archivos propios |
| RF-06 | F-006 | Instalador | Versión igual, anterior, posterior e inexistente |
| RF-07 | F-007 | Enganches | Sesión de un mensaje, larga, e interrumpida |
| RF-08 | F-008 | Enganches | Clave con comillas, sin comillas, y palabra que solo lo parece |
| RF-09 | F-009 | Moldes del ciclo | Trabajo sin su documento, y documento con espacios sin llenar |
| RF-10 | F-010 | Generador de entregables | Documento completo, y documento con espacios sin llenar |
| RF-11 | F-011 | Comprobaciones | Sin línea base inicial, la medición no puede comparar |
| RF-12 | F-012 | Interfaz local | Con base de datos y sin ella; documento borrado del disco |
| RF-13 | F-013 | Memoria | Guardar, recuperar en otra sesión, y corregir lo que dejó de ser cierto |
| RF-14 | F-014 | Comprobaciones | Versión que rompe algo, versión que no, y versión que obliga a rehacer |

**Ningún requisito quedó sin funcionalidad, y ninguna funcionalidad sin requisito.** Los módulos de la tercera columna son los que propone el [diseño](../diseno/README.md); si esa etapa los cambia, esta tabla se rehace.

## 9. El glosario del proyecto

| Término | Qué significa acá | Cómo NO se llama |
|---|---|---|
| Regla | Una exigencia con identificador, que se cita y no se borra | Norma, política, lineamiento |
| Molde | El documento modelo que alguien copia y llena | Formato, machote |
| Fase | La unidad de trabajo que cabe en una jornada y se revierte | Tarea, sprint |
| Señal | Lo que no se recupera leyendo el código y por eso se escribe | Nota, apunte |
| Desfase | La distancia entre la versión adoptada y la publicada | Actualización pendiente |
| Derogar | Marcar una regla como sin vigencia, dejándola escrita | Borrar, eliminar |
| Línea base | Lo aprobado en una fecha, contra lo cual se mide todo cambio posterior | Versión congelada |

## 10. Lo que se preguntó y no tiene respuesta

| # | Duda | Quién responde | Se necesita antes de | Estado |
|---|---|---|---|---|
| 1 | ¿Sirve para alguien que no sea el autor, o es una preferencia personal? | Un usuario ajeno | Declarar el estándar como tal | Abierta |
| 2 | ¿Cuántas reglas admiten comprobación mecánica y cuántas piden criterio? | El autor, escribiéndolas | Estimar el paquete 3 | Abierta |
| 3 | ¿El `.docx` conserva la numeración del `.md` o la del cliente? | Quien reciba el entregable | Construir el generador | Abierta, es la P-1 del inventario |

## 11. Cómo se pide un cambio a lo ya acordado

| Quién pide | Por dónde entra | Quién evalúa el impacto | Quién aprueba |
|---|---|---|---|
| El usuario | Como pendiente escrito | El agente, diciendo a qué funcionalidades le pega | El usuario |
| Un proyecto que hereda | Como pendiente, con el caso que lo motivó | El agente, diciendo si sirve a cualquier proyecto o solo a ese | El usuario |
| El agente, al toparse con un vacío | Como pendiente, en el momento | El agente, diciendo si es requisito nuevo o interpretación de uno existente | El usuario |

**Desde que este documento se apruebe, lo escrito acá es la línea base de requisitos.** Un cambio no se discute contra lo que alguien recuerde, sino contra esta versión.

## 12. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Inventario de funcionalidades | [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) | Usuario, se aprueba | Escrito en [inventario-funcionalidades.md](inventario-funcionalidades.md), 14 fichas; sin aprobar |
| Épicas | [plantillas/ciclo-vida-proyectos/03-epica.md](../../plantillas/ciclo-vida-proyectos/03-epica.md) | Equipo | Pendiente: la puerta es el inventario aprobado |
| Historias de usuario con criterios | [plantillas/ciclo-vida-proyectos/04-HU.md](../../plantillas/ciclo-vida-proyectos/04-HU.md) | Usuario, una por una | Pendiente: salen del «Terminada cuando» de cada ficha |
| Requisitos funcionales | Sección 3 de este documento | Usuario | Listo, catorce con identificador, origen y prioridad |
| Requisitos no funcionales | Sección 4 de este documento | Usuario | Listo, nueve con su número y su comprobación |
| Casos de uso | Sección 7 de este documento | Usuario y quien prueba | Listo, nueve con sus flujos de error |
| Reglas del negocio | Sección 5 de este documento | Equipo | Listo, siete |
| Trazabilidad | Sección 8 de este documento | Equipo y quien prueba | Listo, sin requisitos huérfanos |
| Glosario | Sección 9 de este documento | Ambos | Listo, con siete términos |

## 13. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Derivar épicas | el inventario esté aprobado por el usuario | [`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) |
| Pasar a diseño | cada funcionalidad tenga su «Terminada cuando» verificable | Cumplido: las once lo tienen |
| Pasar a diseño | ningún requisito quede con palabras sin medida | Cumplido: los siete no funcionales llevan número |

## 14. La decisión de cierre

**Se pasa a diseño cuando el inventario esté aprobado**, decidido por el autor el 2026-08-24.

Lo que la etapa tenía que producir está escrito: catorce requisitos funcionales con su origen, nueve no funcionales con su número, nueve casos de uso con sus flujos de error, siete reglas del negocio, la trazabilidad sin huérfanos y el inventario con sus catorce fichas.

**Las tres dudas de la sección 10 siguen abiertas y no detienen el paso a diseño**, salvo la 3, que solo detiene a `F-010`. La duda 1 es la que puede cambiar el proyecto entero: si no sirve para nadie más, lo que se construye es una preferencia personal y no un estándar. Se responde instalándolo fuera, no discutiéndolo.

## 15. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. El resumen de las siete etapas, y lo que ese análisis no puede decir, están en [cvds/README.md](../README.md).

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| De dónde salió cada requisito | Lo que el usuario pidió, con sus palabras y sin reescribir | [prompts/](../../prompts/) |
| Las reglas del negocio | Las seis del núcleo blindado, que ninguna otra puede contradecir | [base/00-nucleo-blindado.md](../../base/00-nucleo-blindado.md) |
| Los actores y sus permisos | Qué puede hacer el agente, qué no, y qué cuesta deshacer cada acción | [base/00-identidad-y-rol/acciones-y-riesgo.md](../../base/00-identidad-y-rol/acciones-y-riesgo.md) |
| El glosario del proyecto | Los términos del estándar, con una definición cada uno | [base/glosario.md](../../base/glosario.md) |
| Las dudas abiertas | Las preguntas se escriben y detienen el trabajo en vez de resolverse inventando | Las 42 dudas que detuvieron 26 fases, en [pendientes/hecho/](../../pendientes/hecho/) |
| La trazabilidad | Tabla de cinco columnas obligatoria, y comprobación antes de cerrar | `13·DOC11` y `13·DOC3` |
| Control de cambios sobre lo acordado | Todo cambio versiona, y nada se borra: se deroga | `M10` y `M11`, con [CHANGELOG.md](../../CHANGELOG.md) |

**Los cinco hallazgos de esta etapa, y qué se escribió para cada uno**

| # | Hallazgo del análisis | Qué se escribió | Dónde quedó |
|---|---|---|---|
| 1 | Los requisitos existían como historias, sin catálogo con identificador ni prioridad | Once requisitos con `RF-01` a `RF-11`, su origen, el objetivo del que salen y su prioridad en cuatro grados | Sección 3 |
| 2 | Los casos de uso no se escribieron como tales | Seis casos, cada uno con sus flujos alternos y de error, que es de donde salen las validaciones | Sección 7 |
| 3 | No había requisitos no funcionales | Siete, cada uno con su número y con cómo se comprueba | Sección 4 |
| 4 | El proyecto no tenía inventario de funcionalidades, que es la puerta que le exige a los demás | Once fichas completas, con lo que las termina, de qué dependen y qué las gobierna | [inventario-funcionalidades.md](inventario-funcionalidades.md) |
| 5 | No había línea base aprobada | Escrito cómo entra un cambio y contra qué se mide, listo para regir en cuanto se apruebe | Sección 11 |

**Lo único que sigue abierto**

| Qué | Por qué no lo puede cerrar quien escribe |
|---|---|
| Ni este documento ni el inventario están aprobados | La aprobación es del usuario, y el inventario aprobado es lo que abre la puerta de las épicas |

**Aprobado por: «quién», el «AAAA-MM-DD».**
