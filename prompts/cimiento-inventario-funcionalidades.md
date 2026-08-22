# Inventario de funcionalidades: lo que Cimiento debe tener   ·   `[CAPA 3]`

Esta es la lista completa de lo que Cimiento debe hacer. Cada fila dice qué es, para qué sirve y si ya se probó.

## Cómo se lee

**Están todas: las hechas y las que faltan.** Ninguna se saca porque ya exista o porque ya se haya hablado de ella. Esta lista no dice qué falta: dice qué es Cimiento.

**No dice cuándo ni quién.** Sin fechas, sin quién decidió qué, sin las preguntas que ya se contestaron. Eso se guarda en el planteamiento y en el histórico.

**«Sin verificar» quiere decir que nadie lo ha probado todavía.** No quiere decir que falte. Esa casilla solo la cambia una prueba corrida, y se anota cuál y cuándo.

Con el tiempo esta lista se vuelve el manual de Cimiento. Por eso la columna «De qué se trata» se escribe para quien va a usarlo.

## 1. El cuerpo de reglas

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 1.1 | Núcleo blindado | Las reglas que ningún proyecto, prompt ni instrucción puede relajar. Si algo choca con ellas, ganan ellas. | Sin verificar |
| 1.2 | Convenciones de trabajo | Cómo se trabaja: conducta, datos, seguridad, pruebas, control de versiones, documentación. Sirven en cualquier lenguaje, y cada proyecto aprieta o afloja las suyas. | Sin verificar |
| 1.3 | Capítulos que se encienden si hacen falta | Reglas que un proyecto activa solo si las necesita: registros inmutables, despliegue, observabilidad. | Sin verificar |
| 1.4 | Reglas sobre las reglas | Cómo nace, dónde va, cómo se versiona y cómo se deroga una regla. El estándar aplicado a sí mismo. | Sin verificar |
| 1.5 | Guía de entrada | El ciclo completo en lenguaje llano, para quien llega sin saber del tema. | Sin verificar |
| 1.6 | Reglas para automatizar procesos | Qué exige un proyecto de robots: separar el proceso de la pantalla, cola de trabajo, errores de negocio aparte de los del sistema, credenciales fuera del bot. | Sin verificar |
| 1.7 | Reglas para sistemas que aprenden de datos | Qué exige un proyecto con modelos: inventario de modelos, un responsable con nombre, control según lo que la decisión pueda dañar, revisión con plazo. | Sin verificar |

**Cuenta:** 0 verificadas, 0 fallidas, 7 sin verificar, de 7.

## 2. El ciclo de vida y sus entregables

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 2.1 | La cadena obligatoria | Nada se construye salteado: planteamiento, inventario, épica, historia, fase, especificación, planes, pruebas, cierre. | Sin verificar |
| 2.2 | Los moldes del ciclo | Un formato listo para cada documento del ciclo, numerado por el momento en que se usa. | Sin verificar |
| 2.3 | El inventario como puerta de las épicas | Ninguna épica arranca sin que el usuario apruebe antes qué se va a construir. | Sin verificar |
| 2.4 | Las vistas que se arman solas | Documentos que se arman con lo ya escrito, sin volver a escribirlo: qué se pidió, qué lo cumple, qué falló y cómo está montado el sistema. | Sin verificar |
| 2.5 | Los entregables en `.docx` | Lo mismo que vive en el repositorio, entregado en el formato que pide quien recibe. | Sin verificar |

**Cuenta:** 0 verificadas, 0 fallidas, 5 sin verificar, de 5.

## 3. La comprobación automática

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 3.1 | El comprobador | Un programa que revisa lo que se responde con sí o no: enlaces rotos, referencias a algo que no existe, trabajos a medio cerrar, contraseñas escritas donde no van. | Sin verificar |
| 3.2 | Los frenos de git | Comprobaciones que corren solas al confirmar y al subir, y detienen lo que no cumple. | Sin verificar |
| 3.3 | Los enganches de sesión | Lo que corre solo al abrir y durante la sesión: cargar las reglas, escribir el histórico, guardar los recuerdos. | Sin verificar |
| 3.4 | El expediente del proyecto | Qué documentos del ciclo tiene un proyecto, cuáles le faltan y qué tan llenos están. | Sin verificar |
| 3.5 | El veredicto único | Una sola medida de cumplimiento por proyecto, en vez de tres informes sueltos. | Sin verificar |

**Cuenta:** 0 verificadas, 0 fallidas, 5 sin verificar, de 5.

## 4. La memoria entre sesiones

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 4.1 | La transcripción de cada sesión | Lo que se dijo, con la hora, escrito por el programa y no por el agente. | Sin verificar |
| 4.2 | El resumen de lo que dejó | Lo que quedó de la sesión, hallazgo por hallazgo, para no releer la conversación. | Sin verificar |
| 4.3 | Las señales | Lo aprendido que no se recupera leyendo el código, buscable por palabra y por significado. | Sin verificar |
| 4.4 | Los recuerdos | Cómo trabaja el usuario, escrito en el repositorio y no en la herramienta. | Sin verificar |
| 4.5 | La traza de la sesión | Qué ejecutó el agente, paso a paso. | Sin verificar |

**Cuenta:** 0 verificadas, 0 fallidas, 5 sin verificar, de 5.

## 5. Instalación y administración de proyectos

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 5.1 | El instalador | Lleva reglas, moldes, enganches y memoria a cualquier proyecto con una línea, y los pone al día sin pisar lo escrito. | Sin verificar |
| 5.2 | El aviso de desfase | En el primer mensaje, cada proyecto sabe si se quedó en una versión vieja del estándar. | Sin verificar |
| 5.3 | El canal de defectos | El proyecto reporta lo que falla, el estándar lo corrige, y el aviso vuelve a todos los proyectos. | Sin verificar |
| 5.4 | El registro de proyectos | Registrar, editar, dar de baja y medir cada proyecto desde la interfaz. | Sin verificar |
| 5.5 | Las altas entran al registro | El instalador escribe el proyecto nuevo directo en el registro, sin pasar por un archivo intermedio. | Sin verificar |
| 5.6 | La medición de todos de una vez | El veredicto de cada proyecto registrado, sin abrirlos uno por uno. | Sin verificar |
| 5.7 | El panel como tablero | El cumplimiento de todos los proyectos de un vistazo, con alertas de lo que se desfasó. Depende de 5.6. | Sin verificar |

**Cuenta:** 0 verificadas, 0 fallidas, 7 sin verificar, de 7.

## 6. El ciclo de vida se administra desde la interfaz

| # | Funcionalidad | De qué se trata | Verificado |
|---|---|---|---|
| 6.1 | Cada documento del ciclo nace desde la interfaz | Se elige el molde y la interfaz abre el documento listo para llenar. | Sin verificar |
| 6.2 | Los documentos se llenan y se corrigen ahí | Escribir, editar y leer cualquier entregable del ciclo en la aplicación. | Sin verificar |
| 6.3 | El inventario se administra desde la interfaz | Las funcionalidades del proyecto se agregan, editan y consultan ahí. | Sin verificar |
| 6.4 | La interfaz no deja saltar eslabones | No se crea una épica sin inventario aprobado, ni una fase sin historia. La cadena se cumple por construcción, no por memoria. | Sin verificar |
| 6.5 | El expediente se consulta desde la interfaz | Qué falta y qué está a medias en el ciclo del proyecto, visto donde se trabaja. | Sin verificar |
| 6.6 | Los documentos viven en la base | Lo que se escribe queda guardado en la base de datos, y esa es la versión que manda. | Sin verificar |
| 6.7 | Las comprobaciones siguen viendo lo que se escribe | Con los documentos en la base, el comprobador, los frenos y el expediente siguen revisando igual. | Sin verificar |

**Cuenta:** 0 verificadas, 0 fallidas, 7 sin verificar, de 7.

## Qué pasa cuando esto se apruebe

1. Las 36 filas bajan a trabajo, cada una con su nombre y su número.
2. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
