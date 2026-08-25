# Análisis de requisitos: ¿qué debe hacer el sistema?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué** tiene que hacer Cimiento, sin decir todavía cómo. Confundir las dos cosas acá es el error caro del ciclo: un requisito escrito como solución cierra opciones antes de haberlas mirado.

> **Escrito desde la propuesta, no desde lo que hoy existe.** Sale del problema y de los quince objetivos de [cvds/planificacion/README.md](../planificacion/README.md). Reescrito el 2026-08-24, cuando el producto pasó de ser un estándar que viaja dentro de cada proyecto a una plataforma que los administra.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| El problema, el alcance y los quince objetivos | Planificación | Sí, el 2026-08-24 |
| Las restricciones: la fuente en texto, la base como índice, sin servicio ajeno | Planificación | Sí, el 2026-08-24 |
| Los cinco supuestos, con el de que el agente obedece lo que la plataforma le entrega | Planificación | Sí, aunque ninguno se ha confirmado todavía |

## 2. De dónde salieron los requisitos

| Fuente | Quién | Técnica | Cuándo | Dónde quedó lo acordado |
|---|---|---|---|---|
| Quien usa el sistema a diario | El autor, que administra varios proyectos | Observación de su propio trabajo, y de lo que le falta al hacerlo | Permanente | [prompts/](../../prompts/), con sus palabras |
| Lo que ya se intentó | El autor | Revisión de lo que falló: documentar dentro de cada proyecto, corregir por chat | Antes de empezar | Sección 1 de [planificación](../planificacion/README.md) |
| El giro de producto | El autor | Conversación del 2026-08-24: qué debe llegar a ser Cimiento, no qué es hoy | 2026-08-24 | Sección 19 de [planificación](../planificacion/README.md) |
| Los proyectos que administra | Ninguno consultado como tal | Sin consultar | — | Nada |

**Quién no se consultó, y por qué:** nadie ajeno al autor. **Todos los requisitos salen de una sola persona**, y eso es un límite del análisis, no un detalle.

## 3. Los requisitos funcionales

> Prioridad en cuatro grados: **debe** (sin esto no sirve), **debería** (importante, opera sin ello), **podría** (si sobra tiempo), **no será** (excluido de esta versión).

| ID | Qué debe hacer el sistema | Quién lo necesita | Origen | Objetivo del que sale | Prioridad |
|---|---|---|---|---|---|
| RF-01 | Registrar un proyecto, con su nombre y dónde vive su código | El usuario | Observación del propio trabajo | 1 | Debe |
| RF-02 | Avisar cuando la ruta de un proyecto deja de existir | El usuario | El giro de producto | 14 | Debe |
| RF-03 | Mostrar el estado de cualquier proyecto sin entrar a su carpeta | El usuario | El giro de producto | 1 | Debe |
| RF-04 | Configurar por proyecto qué reglas y qué moldes rigen | El usuario | El giro de producto | 1 | Debería |
| RF-05 | Crear, editar y derogar reglas desde la plataforma | El usuario | El giro de producto | 1 | Debe |
| RF-06 | Asignar el identificador de una regla sin reutilizar ninguno | El usuario | Lo que ya se intentó | 1 | Debe |
| RF-07 | Aplicar el checklist a una regla y guardar su resultado | El usuario | Observación del propio trabajo | 4 | Debería |
| RF-08 | Publicar una versión del cuerpo de reglas, con su registro de qué cambió | El usuario | Observación del propio trabajo | 1 | Debe |
| RF-09 | Entregarle al agente las reglas al abrir sesión, en cualquier proyecto | El usuario | El giro de producto | 2, 6 | Debe |
| RF-10 | Avisar a un proyecto cuando la versión que adoptó quedó atrás, y qué cambió | El usuario | Lo que el usuario pidió dos veces | 14 | Debería |
| RF-11 | Crear épicas, historias y fases desde la plataforma, con su molde | El usuario | El giro de producto | 1, 10 | Debe |
| RF-12 | Mostrar en qué estación va cada fase y qué puerta falta | El usuario | El giro de producto | 1 | Debe |
| RF-13 | Impedir avanzar de estación sin la puerta cumplida | El usuario | Observación del propio trabajo | 5 | Debe |
| RF-14 | Llenar cada documento del ciclo desde la plataforma, sin crear archivos a mano | El usuario | El giro de producto | 10 | Debe |
| RF-15 | Registrar una aprobación con quién, cuándo y sobre qué texto exacto | El usuario | El giro de producto | 7 | Debe |
| RF-16 | Mostrar qué está aprobado y qué sigue en borrador | El usuario | El giro de producto | 7 | Debe |
| RF-17 | Marcar como no aprobado lo que cambió después de haberse aprobado | El usuario | Observación del propio trabajo | 7 | Debe |
| RF-18 | Registrar cada acción sobre proyectos, documentos y reglas | El usuario | El giro de producto | 8 | Debe |
| RF-19 | Consultar lo registrado por proyecto, por fecha y por tipo de acción | El usuario | El giro de producto | 8 | Debería |
| RF-20 | Comprobar por sí sola lo que las reglas exigen | El usuario | Lo que ya se intentó | 4 | Debe |
| RF-21 | Declarar como no verificado lo que no tenga prueba corrida | El usuario | Observación del propio trabajo | 4, 5 | Debe |
| RF-22 | Comprobar que una versión nueva no rompió lo que ya servía | El usuario | Observación del propio trabajo | 15 | Debe |
| RF-23 | Guardar lo aprendido y devolverlo en la sesión siguiente | El usuario | Lo que ya se intentó | 2 | Debe |
| RF-24 | Consultar, corregir y dar de baja lo guardado en la memoria | El usuario | El giro de producto | 2 | Debería |
| RF-25 | Armar el expediente completo de un proyecto cuando se pida | El usuario | El giro de producto | 9 | Debe |
| RF-26 | Generar el entregable de ofimática desde la fuente en texto | Quien recibe el proyecto | Lo que el usuario pidió dos veces | 9, 11 | Debe |
| RF-27 | Traer un proyecto que ya existe, con lo que tenga escrito | El usuario | El giro de producto | 13 | Debe |
| RF-28 | Reportar qué de lo traído no sigue ningún molde conocido | El usuario | El giro de producto | 13 | Debería |
| RF-29 | Avisar deuda vencida, historia sin fase y respaldo sin probar | El usuario | Observación del propio trabajo | 14 | Debería |
| RF-30 | Reportar cómo va cada proyecto, y compararlos entre sí | El usuario | El giro de producto | 1 | Debería |
| RF-31 | Tapar toda credencial antes de que quede escrita | El usuario | Observación del propio trabajo | 12 | Debe |
| RF-32 | Medir el tiempo que el usuario dedica a revisar | El usuario | Observación del propio trabajo | 3 | Podría |

**El alcance ítem por ítem, con la ficha de cada uno, está en [inventario-funcionalidades.md](inventario-funcionalidades.md).** Esta tabla es el resumen que se acuerda; aquel es el detalle que se construye.

## 4. Los requisitos no funcionales

> **Un requisito no funcional es una exigencia sobre cómo se comporta el sistema**, no sobre qué hace. Se escribe con número: «rápido» no es un requisito.

| ID | Frente | Exigencia, con su número | Cómo se comprueba |
|---|---|---|---|
| RNF-01 | Rendimiento | Entregarle las reglas al agente no demora la apertura de la sesión más de dos segundos | Se mide con el cuerpo de reglas completo |
| RNF-02 | Rendimiento | Listar los proyectos y su estado responde en menos de un segundo con cincuenta proyectos | Se mide con cincuenta proyectos de prueba |
| RNF-03 | Disponibilidad | Funciona sin red: todo lo que necesita está en la máquina | Se corre con la máquina desconectada |
| RNF-04 | Recuperación | Perder la base no pierde información: se reconstruye desde la fuente en texto | Se borra la base y se reconstruye |
| RNF-05 | Seguridad | Ninguna credencial queda escrita en ningún archivo ni en la base | Comprobación que rechaza el guardado si encuentra una |
| RNF-06 | Datos personales | No se recogen ni se almacenan datos de personas | Revisión del modelo de datos y de lo que se guarda |
| RNF-07 | Usabilidad | Lo entiende quien no conoce el proyecto: sin siglas sin explicar | Cada pantalla y cada documento se lee sin abrir otro |
| RNF-08 | Compatibilidad | Corre con lo que ya está instalado en la máquina del usuario | Se levanta en una máquina recién formateada |
| RNF-09 | Portabilidad | Puede correr en un servidor sin rehacer la aplicación | Se levanta en otra máquina sin cambiar el código |
| RNF-10 | Compatibilidad hacia atrás | Una versión nueva no rompe lo que servía; si obliga a rehacer algo, lo declara antes | Se corre lo anterior antes de publicar |
| RNF-11 | Crecimiento | Un componente nuevo entra sin obligar a reescribir los anteriores | Agregar uno no cambia archivos de los otros |
| RNF-12 | Trazabilidad | Toda acción registrada dice quién, cuándo y sobre qué | Revisión de lo registrado |

## 5. Las reglas del negocio

> **Una regla del negocio manda sobre el sistema y sobre todo lo demás:** existe aunque el sistema no exista.

| # | Regla | Quién la dicta | Qué pasa si se rompe |
|---|---|---|---|
| RN-1 | Lo que se acuerda se escribe donde no se borra, nunca solo en la conversación | El usuario | La corrección se pierde y hay que darla de nuevo |
| RN-2 | Ningún cambio de estado sin aprobación explícita del usuario | El usuario | Aparecen cambios que nadie autorizó |
| RN-3 | Lo que no se puede deshacer se aprueba una por una | El usuario | Un plan aprobado termina cubriendo lo irreversible |
| RN-4 | No se afirma sobre lo que no se leyó | El usuario | Veredictos falsos, que hacen desconfiar de los verdaderos |
| RN-5 | El estado de una funcionalidad lo fija la prueba corrida, no la lectura | El usuario | Se entrega como terminado lo que nadie comprobó |
| RN-6 | Nada se renumera ni se borra: se deroga | El usuario | Se rompen las citas de documentos y trabajos cerrados |
| RN-7 | La fuente es texto versionado; la base es índice y se puede reconstruir | El usuario | El respaldo deja de ser el repositorio |
| RN-8 | Lo aprobado se congela: si el texto cambia, la aprobación caduca | El usuario | Se da por aprobado algo que nadie leyó así |
| RN-9 | Una credencial no se escribe, no se registra y no se guarda | El usuario | Queda expuesta en algo que se versiona y se publica |

## 6. Los actores y sus permisos

| Actor | Qué hace en el sistema | Qué no puede hacer |
|---|---|---|
| El usuario | Administra, aprueba, corrige, publica versiones | Nada le está vedado: es quien manda |
| El agente | Recibe las reglas, construye, comprueba, escribe documentos y reporta | Cambiar el estado sin aprobación, o declarar terminado lo no probado |
| Un proyecto administrado | Aporta su código, y recibe reglas y avisos | Modificar las reglas que recibe |
| Quien recibe un proyecto | Recibe el expediente generado | Entrar a la plataforma |

## 7. Los casos de uso

> **Un caso de uso cuenta el camino completo, no el feliz.** Los flujos de error son la mitad del trabajo, y la mitad que se omite.

| # | Caso de uso | Actor | Precondición | Qué debe quedar al terminar | Flujos alternos y de error |
|---|---|---|---|---|---|
| CU-01 | Conectar un proyecto | El usuario | El código existe en la máquina | El proyecto registrado y visible | Ruta que no existe: no se registra y se dice · Ruta ya registrada: se avisa cuál es · Carpeta sin control de versiones: se registra y se advierte |
| CU-02 | Ver cómo va un proyecto | El usuario | El proyecto está conectado | Su estado en pantalla | Ruta perdida: se muestra lo guardado y se avisa · Proyecto sin trabajo abierto: se dice que no hay, no se muestra vacío |
| CU-03 | Abrir sesión de trabajo en un proyecto | El agente | El proyecto está conectado | Las reglas cargadas y el aviso de qué versión rige | Plataforma no disponible: se avisa y se trabaja leyendo la fuente · Versión atrasada: se dice qué cambió |
| CU-04 | Escribir o cambiar una regla | El usuario | Ninguna | La regla guardada, con su identificador y pendiente de publicar | Identificador ya usado: no se reutiliza · Regla que contradice a otra: se muestra el choque antes de guardar |
| CU-05 | Publicar una versión | El usuario | Hay cambios sin publicar | La versión publicada, con qué cambió y si obliga a rehacer algo | Rompe algo que servía: no se publica · Sin registro de qué cambió: no se publica |
| CU-06 | Abrir y cerrar una fase | El usuario, con el agente | La historia existe y está aprobada | La fase con sus documentos y su estado | Puerta sin cumplir: no avanza y dice cuál falta · Sin prueba corrida: queda «sin verificar» |
| CU-07 | Aprobar un documento | El usuario | El documento está en borrador | La aprobación registrada, con fecha y sobre qué texto | El texto cambia después: la aprobación caduca y se avisa |
| CU-08 | Pedir el expediente de un proyecto | El usuario | El proyecto tiene documentos | El expediente armado y su entregable generado | Documentos con espacios sin llenar: se avisa antes de generar · Documento faltante: se dice cuál |
| CU-09 | Traer un proyecto que ya existe | El usuario | El proyecto tiene documentación escrita | Lo que tenía, adentro de la plataforma | Lo que no sigue ningún molde: se reporta y no se transforma · Nombres repetidos: se avisa antes de traer |
| CU-10 | Consultar qué se hizo | El usuario | Hay acciones registradas | Lo registrado, filtrado por proyecto, fecha o tipo | Sin coincidencias: se dice que no hay |
| CU-11 | Recuperar lo aprendido en otra sesión | El agente | Hay memoria guardada | Lo aprendido, sin que el usuario lo repita | Nada guardado del tema: se dice, no se inventa · Guardado que dejó de ser cierto: se corrige y queda la corrección |
| CU-12 | Pasarle una credencial al agente | El usuario | Sesión abierta | El trabajo hecho, y la clave tapada en todo lo guardado | Clave sin comillas: se tapa igual · Palabra que solo lo parece: queda intacta |

## 8. La trazabilidad

El camino de cada requisito hasta la funcionalidad que lo ejecuta. El módulo que la implementa y la prueba que la demuestra se escriben en el diseño y en las pruebas: acá no se adivinan.

| Requisito | Funcionalidad | Requisito | Funcionalidad |
|---|---|---|---|
| RF-01 | F-001 | RF-17 | F-017 |
| RF-02 | F-002 | RF-18 | F-018 |
| RF-03 | F-003 | RF-19 | F-019 |
| RF-04 | F-004 | RF-20 | F-020 |
| RF-05 | F-005 | RF-21 | F-021 |
| RF-06 | F-006 | RF-22 | F-022 |
| RF-07 | F-007 | RF-23 | F-023 |
| RF-08 | F-008 | RF-24 | F-024 |
| RF-09 | F-009 | RF-25 | F-025 |
| RF-10 | F-010 | RF-26 | F-026 |
| RF-11 | F-011 | RF-27 | F-027 |
| RF-12 | F-012 | RF-28 | F-028 |
| RF-13 | F-013 | RF-29 | F-029 |
| RF-14 | F-014 | RF-30 | F-030 |
| RF-15 | F-015 | RF-31 | F-031 |
| RF-16 | F-016 | RF-32 | F-032 |

**Ningún requisito quedó sin funcionalidad, y ninguna funcionalidad sin requisito.**

## 9. El glosario del proyecto

Cada palabra del negocio con una sola definición, para que nadie la use de dos formas.

| Término | Qué significa acá | Cómo NO se llama |
|---|---|---|
| Plataforma | Cimiento: lo que administra los proyectos | Sistema, aplicación, herramienta |
| Proyecto administrado | El software que el usuario desarrolla, con su código | Cliente, repositorio |
| Regla | Una exigencia con identificador, que se cita y no se borra | Norma, política, lineamiento |
| Molde | El documento modelo que se copia y se llena | Formato, machote |
| Expediente | El conjunto de documentos de un proyecto, armado para entregar | Paquete, informe |
| Fase | La unidad de trabajo que cabe en una jornada y se revierte | Tarea, sprint |
| Puerta | La condición que hay que cumplir para avanzar de estación | Hito, control |
| Aprobación | El registro de que alguien aceptó un texto exacto, con fecha | Visto bueno |
| Auditoría | Lo registrado sobre qué se hizo, cuándo y sobre qué | Historial, bitácora |
| Memoria | Lo que el agente aprendió y puede recuperar después | Contexto |
| Línea base | Lo aprobado en una fecha, contra lo cual se mide todo cambio | Versión congelada |

> **Los números con que se cita cada cosa.** `RF` requisito funcional · `RNF` requisito no funcional · `RN` regla del negocio · `CU` caso de uso · `F` funcionalidad del inventario · `CA` criterio de aceptación · `DA` decisión de arquitectura. Ninguno se reutiliza.

## 10. Lo que se preguntó y no tiene respuesta

| # | Duda | Quién responde | Se necesita antes de | Estado |
|---|---|---|---|---|
| 1 | ¿Qué entra exactamente en la primera versión? | El autor | Partir el trabajo en versiones | Abierta |
| 2 | ¿Qué se audita de la sesión del agente? «Todo» incluye cada mensaje, y eso pesa | El autor | Construir la auditoría | Abierta |
| 3 | ¿La documentación de todos los proyectos vive en un solo repositorio, o en uno por proyecto? | El autor | Diseñar el modelo de datos | **Resuelta el 2026-08-24:** todo en el repositorio de la plataforma, una carpeta por proyecto |
| 4 | Cuando la plataforma no esté disponible, ¿el agente trabaja leyendo la fuente o se detiene? | El autor | Diseñar la carga de reglas | Abierta, con propuesta: que trabaje y lo diga |
| 5 | ¿El expediente que recibe un cliente incluye la auditoría y la memoria, o solo los entregables? | El autor | Construir el expediente | Abierta, con propuesta: solo los entregables |
| 6 | ¿Sirve para alguien que no sea el autor? | Un usuario ajeno | Declararla como algo más que una herramienta personal | Abierta |

## 11. Cómo se pide un cambio a lo ya acordado

| Quién pide | Por dónde entra | Quién evalúa el impacto | Quién aprueba |
|---|---|---|---|
| El usuario | Como pendiente escrito | El agente, diciendo a qué funcionalidades les pega | El usuario |
| El agente, al toparse con un vacío | Como pendiente, en el momento | El agente, diciendo si es requisito nuevo o interpretación de uno existente | El usuario |

**Desde que este documento se apruebe, lo escrito acá es la línea base de requisitos.** Un cambio no se discute contra lo que alguien recuerde, sino contra esta versión.

## 12. Los entregables de esta etapa, y a quién van

Qué documentos produce la etapa, con qué molde se escriben y quién los recibe.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Inventario de funcionalidades | [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) | Usuario, se aprueba | Aprobado: [inventario-funcionalidades.md](inventario-funcionalidades.md), 32 fichas |
| Épicas | [plantillas/ciclo-vida-proyectos/03-epica.md](../../plantillas/ciclo-vida-proyectos/03-epica.md) | Equipo | Pendiente: la puerta es el inventario aprobado |
| Historias de usuario con criterios | [plantillas/ciclo-vida-proyectos/04-HU.md](../../plantillas/ciclo-vida-proyectos/04-HU.md) | Usuario, una por una | Pendiente |
| Requisitos funcionales | Sección 3 de este documento | Usuario | Listo, treinta y dos |
| Requisitos no funcionales | Sección 4 de este documento | Usuario | Listo, doce con su número |
| Casos de uso | Sección 7 de este documento | Usuario y quien prueba | Listo, doce con sus flujos de error |
| Reglas del negocio | Sección 5 de este documento | Equipo | Listo, nueve |
| Trazabilidad | Sección 8 de este documento | Equipo y quien prueba | Listo, sin huérfanos |
| Glosario | Sección 9 de este documento | Ambos | Listo, once términos |

## 13. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Derivar épicas | el inventario esté aprobado por el usuario | [`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) |
| Pasar a diseño | cada funcionalidad tenga su «Terminada cuando» verificable | Se comprueba al cerrar el inventario |
| Pasar a diseño | ningún requisito quede con palabras sin medida | Cumplido: los doce no funcionales llevan número |
| Diseñar el modelo de datos | esté respondida la duda 3 | Cumplido el 2026-08-24 |

## 14. La decisión de cierre

**Se pasa a diseño**, decidido por el autor el 2026-08-24, con el inventario aprobado ese mismo día y la duda 3 respondida: la documentación vive en el repositorio de la plataforma, una carpeta por proyecto.

**Desde esta fecha lo escrito acá es la línea base de requisitos.**

**Las otras cinco dudas no detienen la etapa.** La 1 y la 2 se responden al partir el trabajo en versiones; la 4 y la 5 tienen propuesta escrita; la 6 solo se responde cuando alguien más lo use.
