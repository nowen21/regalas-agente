# Análisis de requisitos: ¿qué debe hacer el sistema?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué** tiene que hacer el estándar de trabajo heredable, sin decir todavía cómo.

> **Escrito como si no hubiera nada construido**, que es lo que pide la etapa: sale del problema y de los doce objetivos de [cvds/planificacion/README.md](../planificacion/README.md), no del repositorio.

**Estado: BORRADOR** (2026-08-22, sin aprobar).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| El problema, el alcance y los doce objetivos | Planificación | No: el documento de planificación sigue en borrador |
| Las restricciones: sin costo, sin plazo, `.md` como fuente y `.docx` como salida | Planificación | No |
| Los supuestos, con el de que el agente obedece lo que se le carga | Planificación | No, y el 2 sigue sin confirmar |

## 2. Los requisitos funcionales

| # | Qué debe hacer el sistema | Quién lo necesita | ¿De qué objetivo sale? | Prioridad |
|---|---|---|---|---|
| 1 | Cargar las reglas al abrir la sesión, sin que nadie lo pida | El usuario | 1 | Obligatorio |
| 2 | Impedir que se cambie el estado del proyecto sin autorización | El usuario | 6, 7 | Obligatorio |
| 3 | Comprobar por sí solo lo que las reglas exigen | El usuario | 4 | Obligatorio |
| 4 | Declarar como no verificado lo que no tenga prueba corrida | El usuario | 4, 5 | Obligatorio |
| 5 | Instalarse en un proyecto ajeno y decirle qué versión adoptó | El usuario | 2 | Obligatorio |
| 6 | Avisar cuando la versión adoptada quede atrás, y qué cambió | El usuario | 2 | Complementario |
| 7 | Escribir fuera del chat lo que cada sesión dejó | El usuario | 8 | Obligatorio |
| 8 | Tapar toda credencial antes de que quede escrita | El usuario | 9 | Obligatorio |
| 9 | Exigir el documento del ciclo en el momento en que se construye | El usuario | 10, 11 | Obligatorio |
| 10 | Generar el `.docx` de cada documento desde su `.md` | Quien recibe el proyecto | 12 | Complementario |
| 11 | Medir el tiempo que el usuario dedica a revisar | El usuario | 3 | Futuro |

## 3. Los requisitos no funcionales

| Frente | Exigencia | Cómo se comprueba |
|---|---|---|
| Rendimiento | Lo que corre al abrir la sesión no puede demorarla más de dos segundos | Se mide el enganche de apertura sobre un repositorio de mil archivos |
| Disponibilidad | Funciona sin red y sin servicio externo: todo vive en el repositorio | Se corre con la máquina desconectada |
| Seguridad y acceso | Ninguna credencial queda escrita en ningún archivo del repositorio | Comprobación que rechaza el guardado si encuentra una |
| Datos personales y normativa | El estándar no recoge ni almacena datos de personas | Revisión de lo que se escribe en cada documento |
| Usabilidad | Lo entiende quien no conoce el proyecto: sin siglas sin explicar | Cada documento se lee de principio a fin sin abrir otro |
| Compatibilidad | Corre con Python de la biblioteca estándar, sin instalar nada | Se ejecuta en una máquina recién formateada |
| Portabilidad | Se instala en cualquier proyecto sin tocar su código | Instalación de prueba en un proyecto ajeno |

## 4. Las reglas del negocio

| # | Regla | Quién la dicta | Qué pasa si se rompe |
|---|---|---|---|
| 1 | Ningún cambio de estado sin aprobación explícita del usuario | El usuario | Se pierde trabajo que nadie autorizó, y con eso la confianza |
| 2 | Una credencial no se escribe, no se registra y no se guarda | El usuario | Queda expuesta en un archivo que se versiona y se publica |
| 3 | El estado de una funcionalidad lo fija la prueba corrida, no la lectura | El usuario | Se entrega como terminado lo que nadie comprobó |
| 4 | Lo que se acuerda se escribe en el repositorio, no en el chat | El usuario | La corrección se pierde y hay que darla de nuevo |
| 5 | Nada se renumera ni se borra: se deroga | El usuario | Se rompen las citas de documentos y trabajos ya cerrados |

## 5. Los actores y sus permisos

| Actor | Qué hace en el sistema | Qué no puede hacer |
|---|---|---|
| El usuario | Aprueba, corrige, adopta versiones | Nada le está vedado: es quien manda |
| El agente | Escribe, construye, comprueba y reporta | Cambiar el estado del proyecto sin aprobación, o declarar terminado lo no probado |
| El proyecto que hereda | Adopta una versión y recibe avisos | Modificar las reglas heredadas en su copia |

## 6. El glosario del proyecto

| Término | Qué significa acá | Cómo NO se llama |
|---|---|---|
| Regla | Una exigencia con identificador, que se cita y no se borra | Norma, política, lineamiento |
| Molde | El documento modelo que alguien copia y llena | Formato, machote |
| Fase | La unidad de trabajo que cabe en una jornada y se revierte | Tarea, sprint |
| Señal | Lo que no se recupera leyendo el código y por eso se escribe | Nota, apunte |
| Desfase | La distancia entre la versión adoptada y la publicada | Actualización pendiente |

## 7. Lo que se preguntó y no tiene respuesta

| # | Duda | Quién responde | Se necesita antes de | Estado |
|---|---|---|---|---|
| 1 | ¿Sirve para alguien que no sea el autor, o es una preferencia personal? | Un usuario ajeno | Declarar el estándar como tal | Abierta |
| 2 | ¿Cuántas reglas admiten comprobación mecánica y cuántas piden criterio? | El autor, escribiéndolas | Estimar el paquete 3 | Abierta |
| 3 | ¿El `.docx` debe conservar la numeración del `.md` o la del cliente? | Quien reciba el entregable | Construir la interfaz | Abierta |

## 8. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Inventario de funcionalidades | [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md) | Usuario, se aprueba | Pendiente |
| Épicas | [plantillas/ciclo-vida-proyectos/03-epica.md](../../plantillas/ciclo-vida-proyectos/03-epica.md) | Equipo | Pendiente |
| Historias de usuario con criterios | [plantillas/ciclo-vida-proyectos/04-HU.md](../../plantillas/ciclo-vida-proyectos/04-HU.md) | Usuario, una por una | Pendiente |
| Requisitos no funcionales | Sección 3 de este documento | Usuario | Listo |
| Glosario | Sección 6 de este documento | Ambos | Listo, con cinco términos |

## 9. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Derivar épicas | el inventario esté aprobado por el usuario | [`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md) |
| Pasar a diseño | cada historia tenga criterios verificables | El criterio se convierte en caso de prueba |
| Cerrar la duda 2 | se escriban las primeras reglas y se vea cuáles se comprueban solas | Sale del análisis, no de la opinión |

## 10. La decisión de cierre

**No se pasa a diseño todavía**, decidido por el autor el 2026-08-22.

Falta el inventario aprobado, que es la puerta. Las tres dudas de la sección 7 siguen abiertas; la 1 es la única que puede cambiar el proyecto entero, porque si no sirve para nadie más, lo que se está construyendo es una preferencia personal y no un estándar.

## 11. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. El resumen de las siete etapas, y lo que este análisis no puede decir, están en [cvds/README.md](../README.md).

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| De dónde salió cada requisito | Lo que el usuario pidió, con sus palabras y sin reescribir | [prompts/](../../prompts/) |
| Las reglas del negocio | Las seis del núcleo blindado, que ninguna otra puede contradecir | [base/00-nucleo-blindado.md](../../base/00-nucleo-blindado.md) |
| Los actores y sus permisos | Qué puede hacer el agente, qué no, y qué cuesta deshacer cada acción | [base/00-identidad-y-rol/acciones-y-riesgo.md](../../base/00-identidad-y-rol/acciones-y-riesgo.md) |
| El glosario del proyecto | Los términos del estándar, con una definición cada uno | [base/glosario.md](../../base/glosario.md) |
| Las dudas abiertas | Las preguntas se escriben y detienen el trabajo en vez de resolverse inventando | Las 42 dudas que detuvieron 26 fases, en [pendientes/hecho/](../../pendientes/hecho/) |
| La trazabilidad | Tabla de cinco columnas obligatoria, y comprobación antes de cerrar | `13·DOC11` y `13·DOC3` |
| Control de cambios sobre lo acordado | Todo cambio versiona, y nada se borra: se deroga | `M10` y `M11`, con [CHANGELOG.md](../../CHANGELOG.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | los requisitos funcionales existen como 102 historias con criterios, pero no hay catálogo con identificador propio ni prioridad |
| 2 | los casos de uso no se escribieron como tales, aunque los criterios de aceptación cumplen parte de esa función |

**No existe**

| # | Qué |
|---|---|
| 1 | requisitos no funcionales, ninguno escrito hasta el llenado de prueba de [cvds/analisis-requisitos/](../analisis-requisitos/README.md) |
| 2 | el inventario de funcionalidades del propio proyecto, que es **la puerta que el estándar le exige a los demás** (`02·F26`) y que él mismo no tiene |
| 3 | la línea base aprobada |
