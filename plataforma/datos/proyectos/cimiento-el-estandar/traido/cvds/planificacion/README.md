# Planificación Proyecto: Cimiento, plataforma de gestión de proyectos   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, **por qué vale la pena hacer el proyecto, por qué camino y con qué**: el problema, los límites del alcance, los recursos, el cronograma, los riesgos, quién responde por cada cosa y cómo se le informa a quién. Es la única etapa que puede terminar en «no se hace», y ese también es un resultado que se escribe acá.

> **Escrito desde la propuesta, no desde lo que hoy existe.** Lo construido sirve para saber qué se conserva y qué se rehace, nunca para fijar el alcance. Reescrito el 2026-08-24: ver la sección 19.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. El problema y el objetivo

| Pregunta | Respuesta |
|---|---|
| **¿Cuál es el problema?** | El usuario trabaja en varios proyectos a la vez y no tiene desde dónde gobernarlos. Cada proyecto guarda su propia documentación adentro, así que para saber cómo va uno hay que entrar a él, y para compararlos no hay forma. El agente que lo ayuda arranca en blanco cada sesión: repite lo ya corregido, entrega sin comprobar y cambia lo que no se pidió. Lo que se aprueba se dice en una conversación que se borra, así que después nadie puede demostrar qué se autorizó. Y cuando hay que entregar la documentación de un proyecto, hay que armarla documento por documento. |
| **¿A quién le pasa?** | Al usuario, que responde por todos los proyectos. Y a quien reciba cualquiera de ellos: hoy recibiría código sin expediente, o un expediente incompleto |
| **¿Cada cuánto pasa?** | Todos los días, en cada sesión de trabajo, y en cada proyecto |
| **¿A qué escala?** | Sobre todos los proyectos en los que trabaja, y crece con cada proyecto nuevo |
| **¿Cómo se resuelve hoy?** | Entrando proyecto por proyecto, leyendo archivos, y rearmando la documentación a mano cuando alguien la pide |
| **¿Qué se intentó antes?** | Escribir la documentación dentro de cada proyecto. Corregir al agente por chat. Guardar sus preferencias en la herramienta |
| **¿Por qué no funcionó?** | La documentación dentro del proyecto no se puede consultar de conjunto ni auditar. La corrección por chat se va con la conversación. El almacén de la herramienta se queda en esa máquina |
| **¿Qué le cuesta hoy?** | Revisarlo todo, que cuesta más que hacerlo. No está medido en horas; se nota en que la misma corrección se repite, en que entrar a un proyecto es la única forma de saber cómo va, y en que armar un expediente toma un día |
| **¿Qué pasa si no se hace nada?** | El costo crece con cada proyecto. Lo aprobado sigue sin quedar registrado, y el conocimiento sigue viviendo en la cabeza del usuario y en conversaciones borradas |
| **¿Qué necesita que pase?** | Un solo lugar desde donde administrar todos los proyectos: que guarde su documentación, registre lo aprobado, deje auditar lo que se hizo, avise lo que se desvía y **genere el expediente cuando se pida**, sin armarlo documento por documento. Que el agente tome de ahí las reglas con que trabaja, en cualquier proyecto. Y que pueda crecer: lo que se agregue entra sin romper lo anterior |

**Objetivo principal**

Desarrollar una plataforma que administre la documentación, el seguimiento y la auditoría de todos los proyectos del usuario, y de la que el agente tome las reglas con que trabaja, para gobernar el trabajo desde un solo lugar y poder entregar el expediente de cualquier proyecto cuando haga falta.

**Objetivos**

> Cada uno abre con un verbo en infinitivo y sale de lo que el usuario necesita, no del producto.

| # | Objetivo | En qué se nota | Para quién |
|---|---|---|---|
| 1 | Administrar todos los proyectos desde un solo lugar | Sabe cómo va cualquiera sin entrar a él | El usuario |
| 2 | Conservar lo acordado entre una sesión y la siguiente | La corrección se da una vez y la siguiente ya la respeta | El usuario |
| 3 | Reducir el tiempo que el usuario gasta revisando | Aprueba leyendo lo entregado, no rehaciéndolo | El usuario |
| 4 | Comprobar antes de entregar, y declarar lo no comprobado | Lo entregado dice qué se probó, y lo que no, también | El usuario |
| 5 | Entregar terminado lo que se declara terminado | No aparece a medias lo que se dio por cerrado | El usuario |
| 6 | Impedir cambios de estado sin autorización del usuario | No aparecen cambios que no pidió | El usuario |
| 7 | Guardar quién aprobó qué, cuándo y sobre qué texto | Puede demostrar lo autorizado meses después | El usuario |
| 8 | Registrar lo que se hizo, para poder auditarlo | Puede rastrear cualquier cambio hasta quién lo hizo | El usuario |
| 9 | Generar el expediente de un proyecto cuando se pida | Lo entrega el mismo día, sin armarlo documento por documento | El usuario y quien reciba el proyecto |
| 10 | Documentar lo construido mientras se construye | Cada cosa entregada llega con qué hace y para qué | El usuario |
| 11 | Dejar por escrito cómo se instala y se opera | Otra persona lo levanta sin preguntarle a quien lo hizo | Quien reciba el proyecto |
| 12 | Proteger las credenciales de quedar escritas en claro | Ninguna clave suya queda registrada | El usuario |
| 13 | Traer un proyecto que ya existe, con lo que tenga escrito | Empieza a gobernarlo sin rehacer su historia | El usuario |
| 14 | Avisar lo que se desvía, sin que haya que ir a mirarlo | Se entera de la ruta perdida o la deuda vencida cuando pasa | El usuario |
| 15 | Agregar componentes nuevos sin romper los que ya servían | Lo que funcionaba ayer sigue funcionando después de cada versión | El usuario |

## 2. El alcance

> **El alcance es la frontera del proyecto: todo lo que el sistema va a hacer, y todo lo que no.** No es la lista de funciones, que va al inventario; es hasta dónde llega el compromiso.

| ¿Qué se incluye? | ¿Qué queda fuera? | ¿Por qué queda fuera? |
|---|---|---|
| La plataforma que administra los proyectos, con su interfaz | Que la plataforma escriba el código del proyecto | Eso lo hace el agente trabajando, no la pantalla |
| La documentación de todos los proyectos, guardada y administrada por la plataforma | Que cada proyecto mantenga su documentación adentro | Es lo que impide consultarlos de conjunto y auditarlos |
| Las reglas con que trabaja el agente, servidas desde la plataforma | Reglas propias de un stack o de un cliente dentro de las comunes | Lo que sirve a uno solo no se hereda |
| El registro de aprobaciones y la auditoría de lo que se hizo | Auditar cada palabra de cada sesión | Pesa más de lo que sirve: se audita la acción, no la conversación |
| La generación del expediente y su entregable de ofimática | Editar el entregable y devolverlo a la fuente | La fuente es el texto, y una salida no se edita |
| Traer proyectos que ya existen, con lo que tengan escrito | Migrar solo lo que no siga ningún molde | Lo que no tiene forma conocida se revisa a mano |
| Que la plataforma crezca con componentes nuevos | Crecer sin comprobar que lo anterior sigue sirviendo | Cada componente nuevo se llevaba por delante lo que ya funcionaba |
| Correr en la máquina del usuario, y poder correr en un servidor después | Un servicio de terceros que aloje la información | Los proyectos son del usuario y de sus clientes |

## 3. Supuestos

> **Un supuesto es un hecho que el plan necesita cierto y nadie comprobó.** Si alguno falla, el plan cambia. Es lo más barato de escribir y lo más caro de omitir.

| # | Se da por cierto que | Qué pasa si resulta falso | Quién lo confirma |
|---|---|---|---|
| 1 | El agente obedece lo que la plataforma le entrega al abrir | La plataforma administra pero no gobierna: habría que hacerla cumplir por fuera | El uso diario |
| 2 | Guardar la documentación fuera del proyecto no estorba al trabajo diario | Habría que devolver parte al proyecto, y se pierde la vista de conjunto | Las primeras semanas de uso |
| 3 | La fuente cabe en texto, y la base solo hace de índice | El respaldo deja de ser el repositorio y hay que construirle uno propio | Al crecer la memoria |
| 4 | Un solo usuario alcanza para la primera versión | Aparecen permisos, roles y datos de terceros antes de lo previsto | Cuando alguien más la use |
| 5 | Documentar mientras se construye no atrasa el trabajo | Habría que elegir entre documentar y avanzar | Medir el retrabajo evitado |

## 4. Restricciones

> **Una restricción es un límite que el proyecto no puede mover:** viene dado por alguien de afuera o por una decisión ya tomada. La que no se escribe se descubre cuando ya se construyó en contra de ella.

| Tipo | Restricción | ¿De dónde viene? | Cómo se sabe si se rompió |
|---|---|---|---|
| Plazo | Sin fecha de entrega: la plataforma se mantiene mientras se use | El propio proyecto | No aplica: no hay plazo que vencer |
| Presupuesto | Sin costo monetario; solo tiempo del autor | Decisión del autor | Aparecería una dependencia paga o un servicio contratado |
| Dónde corre | En la máquina del usuario. Nada obliga a un servidor, y nada lo impide después | Decisión del autor | Una función que solo sirva con red |
| Dónde vive la información | La fuente es texto versionado; la base es índice y se puede reconstruir | Que el respaldo sea el propio repositorio | Un dato que solo exista en la base |
| Formato de los entregables | Se escriben en `.md`; el `.docx` se genera desde ahí y no se edita | Entregar en ofimática sin duplicar la fuente | Un `.docx` con cambios que no están en su `.md` |
| Normativa y credenciales | Sin datos de personas; ninguna credencial se escribe ni se guarda | `N6` | El enmascarado corre al guardar, y una comprobación rechaza el guardado |

## 5. Dependencias de terceros

> **Una dependencia es algo que el proyecto necesita y no puede producir:** lo entrega alguien que no está en el equipo, y por eso no se le puede exigir la fecha.

| De quién o de qué | Qué se necesita | Para cuándo | Qué se hace si no llega |
|---|---|---|---|
| La herramienta donde corre el agente | Que siga permitiendo enganches al abrir y cerrar sesión | Permanente | Las reglas quedan servidas, pero se cargan a mano |
| El control de versiones | Que siga siendo el respaldo de la fuente | Permanente | Habría que construir un respaldo propio |
| Un proyecto ajeno | Alguien que no sea el autor que la adopte | Sin fecha | Sigue siendo una herramienta personal, y se dice así |

## 6. Viabilidad, en cuatro frentes

> **Viable es lo que se puede hacer con lo que hay: capacidad, dinero, tiempo y permiso legal.** No pregunta si conviene, que es la decisión de la sección 18; pregunta si es posible.

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la capacidad y las herramientas? | Sí: archivos de texto, una base local, una aplicación que corre en la máquina y los enganches de la herramienta del agente | No |
| Económica | ¿El costo cabe en lo que se está dispuesto a invertir? | Sí: no hay gasto, solo tiempo del autor. Lo que ahorra es la revisión repetida y el armado del expediente | No |
| Operativa | ¿Lo van a adoptar? | Es la herramienta de trabajo del propio autor, así que su adopción está asegurada. Fuera de él, sin evidencia | No, pero es el frente sin comprobar |
| Legal | ¿Cumple normativa, licencias y protección de datos? | Sin datos de personas. La documentación de proyectos de clientes queda en la máquina del usuario, no en un servicio ajeno | No |

**Recomendación: continuar.** Ningún frente bloquea. El análisis largo, con las alternativas descartadas, vive en [estudio-factibilidad.md](estudio-factibilidad.md).

## 7. Recursos

**Personas.**

| Perfil | Cuántas | Dedicación | Quién |
|---|---|---|---|
| Autor, y quien aprueba | 1 | Sin cuota fija | Ing. José Dúmar Jiménez Ruíz |
| Agente que construye | 1 | Por sesión | La herramienta de trabajo |

**Infraestructura, herramientas y licencias.**

| Qué | Para qué | Costo | ¿Ya se tiene? |
|---|---|---|---|
| Git y un repositorio remoto | Versionar la fuente y respaldarla | Sin costo | Sí |
| Python y una base local | Correr la plataforma y su índice | Sin costo | Sí |
| La herramienta donde corre el agente | Trabajar con el agente | Suscripción ya vigente | Sí |

## 8. Presupuesto

N/A porque no hay costo monetario que asignar: el único recurso es tiempo del autor, y las herramientas ya estaban pagas antes del proyecto.

## 9. Estimación de esfuerzo

**Técnica usada: juicio experto, en jornadas de trabajo.** Se estima cada paquete de la sección 10 como si se construyera desde cero.

| Paquete del desglose | Esfuerzo | Supuesto del que depende |
|---|---|---|
| 1 · Plataforma base y proyectos conectados | 15 jornadas | Que baste con guardar la ruta y avisar cuando se pierda |
| 2 · Las reglas, administradas y servidas | 20 jornadas | Que el agente acepte recibirlas al abrir |
| 3 · El ciclo de vida operado desde la interfaz | 25 jornadas | Que los moldes ya escritos sirvan tal como están |
| 4 · Aprobaciones con firma | 8 jornadas | Que baste registrar quién, cuándo y sobre qué texto |
| 5 · Auditoría de lo que se hizo | 12 jornadas | Que se audite la acción y no la conversación |
| 6 · Comprobación automática de lo exigido | 25 jornadas | Que cada regla comprobable admita comprobación mecánica |
| 7 · Memoria administrable | 12 jornadas | Que guardar, consultar y corregir alcancen |
| 8 · Generación del expediente y del entregable | 20 jornadas | Que baste convertir en un sentido |
| 9 · Traer proyectos que ya existen | 15 jornadas | Que lo que ya está escrito siga un molde conocido |
| 10 · Avisos y reportes | 10 jornadas | Que salgan de datos que la plataforma ya tiene |
| 11 · Que lo nuevo no rompa lo anterior | 6 jornadas | Que lo que ya servía tenga prueba que lo demuestre |
| 12 · Enmascarado de credenciales | 3 jornadas | Que las formas de escribir una clave sean pocas y conocidas |
| 13 · Medición del tiempo de revisión | 2 jornadas | Que haya con qué comparar el antes y el después |

**Total: 173 jornadas, con margen de un tercio hacia arriba.** Los paquetes 3 y 6 son los que más pueden correrse: operar el ciclo desde una pantalla tiene más casos raros de los que se ven al planear, y el esfuerzo de comprobar depende de cuántas reglas resulten comprobables, que solo se sabe escribiéndolas.

**Es una estimación de juicio, sin registro de horas contra el cual contrastarla.** Sirve para dimensionar y para partir el trabajo en versiones, no para prometer una fecha.

## 10. Desglose del trabajo (WBS/EDT)

**Desglose (WBS/EDT).** Sale de los quince objetivos, no de lo ya construido: es lo que hay que hacer para resolver el problema, esté hecho o no.

> **El desglose sale de los objetivos.** La columna del medio es el control: un paquete que no atiende a ninguno sobra, y un objetivo que no aparece en ningún paquete no se va a cumplir solo.

| Código | Paquete de trabajo | Objetivos que atiende | Depende de | Duración | Responsable |
|---|---|---|---|---|---|
| 1 | Plataforma base: proyectos conectados, con su ruta y su configuración | 1, 14 | — | Sin estimar | Autor |
| 2 | Las reglas: administrarlas, versionarlas y servírselas al agente al abrir | 2, 6 | 1 | Sin estimar | Autor |
| 3 | El ciclo de vida operado: épicas, historias, fases, puertas y estado | 1, 10 | 1 | Sin estimar | Autor |
| 4 | Aprobaciones: qué se aprobó, quién, cuándo y sobre qué texto | 7 | 3 | Sin estimar | Autor |
| 5 | Auditoría: qué se hizo, cuándo y a raíz de qué | 8 | 1 | Sin estimar | Autor |
| 6 | Comprobación automática de lo que las reglas exigen | 4, 5 | 2 | Sin estimar | Autor |
| 7 | Memoria: guardar lo aprendido, consultarlo y corregirlo | 2 | 1 | Sin estimar | Autor |
| 8 | Expediente: armarlo cuando se pida y generar el entregable | 9, 11 | 3 | Sin estimar | Autor |
| 9 | Traer proyectos que ya existen, con lo que tengan escrito | 13 | 1, 3 | Sin estimar | Autor |
| 10 | Avisos y reportes: lo que se desvía y cómo va cada proyecto | 14 | 1, 5 | Sin estimar | Autor |
| 11 | Que un componente nuevo no rompa los que ya servían | 15 | 6 | Sin estimar | Autor |
| 12 | Enmascarado de credenciales en todo lo que se escribe | 12 | 1 | Sin estimar | Autor |
| 13 | Medición del tiempo de revisión, antes y después | 3 | 5, 6 | Sin estimar | Autor |

**Los quince objetivos quedan cubiertos, y ningún paquete sobra.**

## 11. Cronograma

> El cronograma pone fechas al desglose de la sección 10: cuándo se alcanza cada hito y qué cadena de tareas no admite atraso. Sin desglose no hay cronograma: son fechas puestas sobre nada.

**Hitos y fecha de entrega.**

| Hito | Fecha | Qué tiene que estar listo para darlo por cumplido |
|---|---|---|
| Un proyecto conectado y visible desde la plataforma | Sin fecha | Se ve su estado sin entrar a su carpeta |
| El agente recibe las reglas de la plataforma | Sin fecha | Abre sesión en un proyecto y trabaja con lo que la plataforma le entregó |
| El ciclo se opera desde la interfaz | Sin fecha | Se abre una fase y se cierra sin crear archivos a mano |
| Lo aprobado queda registrado | Sin fecha | Se puede mostrar quién aprobó qué, cuándo y sobre qué texto |
| El expediente se genera cuando se pide | Sin fecha | Se entrega el `.docx` de un proyecto el mismo día |
| Un proyecto que ya existía queda gobernado | Sin fecha | Lo que tenía escrito está adentro y se administra desde la plataforma |
| Fecha de entrega del proyecto | Sin fecha | No la hay: la plataforma se mantiene mientras se use |

**Ruta crítica: paquetes 1, 2, 6 y 8.** Sin plataforma no hay dónde conectar nada; sin reglas servidas el agente no cambia su forma de trabajar; sin comprobación lo exigido se incumple en silencio; y sin expediente generado no se resuelve lo que más cuesta hoy.

## 12. Modelo de desarrollo

**Se usa iterativo e incremental**, en fases que caben en una jornada y se revierten desde el control de versiones. El alcance completo está escrito y se entrega por versiones: cada una deja algo utilizable.

## 13. Riesgos

Lo que puede salir mal, con qué tan probable es, cuánto dolería y qué se hace si pasa.

| # | Riesgo | Probabilidad | Impacto | Responsable | Mitigación | Qué se hace si ocurre |
|---|---|---|---|---|---|---|
| 1 | Sin la plataforma no se puede trabajar en ningún proyecto | Alta | Alto | Autor | La fuente es texto y vive en el repositorio: se puede leer sin ella | Se trabaja leyendo los archivos hasta levantarla |
| 2 | Se pierde la máquina, y con ella la información de todos los proyectos | Media | Alto | Autor | El repositorio remoto es el respaldo, y la base se reconstruye | Se clona y se reconstruye el índice |
| 3 | El agente no obedece lo que la plataforma le entrega | Media | Alto | Autor | Comprobar por programa lo que no se puede confiar a su memoria | Se corrige la carga, y queda como señal |
| 4 | El alcance crece más rápido de lo que se construye | Alta | Medio | Autor | El inventario completo está escrito, y cada versión declara qué entra | Se recorta la versión, no el inventario |
| 5 | Auditar todo termina pesando más de lo que sirve | Media | Medio | Autor | Se audita la acción, no la conversación | Se recorta qué se registra, con el criterio escrito |
| 6 | Todo depende de una sola persona | Alta | Alto | Autor | Queda escrito y legible sin su autor | La plataforma se congela y lo escrito sigue sirviendo |
| 7 | Un componente nuevo rompe lo que ya funcionaba | Alta | Alto | Autor | El paquete 11: comprobar lo anterior antes de publicar | Se revierte y se publica una corrección |
| 8 | Una credencial queda escrita en claro | Baja | Alto | Autor | Enmascarado al guardar, y comprobación que lo rechaza | Se rota la credencial y se limpia el rastro |

## 14. Roles y responsabilidades

> **Quién hace, quién responde, a quién se consulta y a quién se informa**, por actividad. Hacer y responder no son lo mismo: si una fila tiene dos responsables, no tiene ninguno.

| Actividad o entregable | Quién lo hace | Quién responde | A quién se consulta | A quién se informa |
|---|---|---|---|---|
| Definir el alcance y aprobarlo | Autor | Autor | — | — |
| Construir la plataforma | Agente | Autor | Autor | — |
| Escribir y derogar reglas | Agente | Autor | Autor | — |
| Aprobar el cambio, y aparte el commit | Autor | Autor | — | — |
| Operar el día a día | Autor, con el agente | Autor | — | — |

## 15. Interesados y comunicación

Quién tiene algo que ganar o perder con el proyecto, y qué recibe de él.

| Interesado | Qué papel tiene | Influencia | Qué recibe | Cada cuánto | En qué formato |
|---|---|---|---|---|---|
| Ing. José Dúmar Jiménez Ruíz | Paga, usa y aprueba, los tres | Alta | El cambio antes de guardarlo | Por sesión | En el chat, con el enlace al archivo |
| Los proyectos que administra | Consumen las reglas y aportan su documentación | Ninguna | Reglas al abrir, y avisos de lo que se desvía | Al abrir sesión | Aviso automático |
| Quien reciba un proyecto | Recibe el expediente | Baja | Los entregables de cada fase | Al entregar | `.docx` generado |
| El agente de la sesión siguiente | Ejecuta lo escrito | Ninguna | Lo que la sesión anterior dejó | Al abrir sesión | Desde la plataforma |

**Lo que nadie recibe, y se dice:** no hay informe periódico de avance. El estado se consulta cuando alguien quiera.

## 16. Plan de calidad

Qué se le exige a lo que se entrega, y con qué se mide.

| Qué se exige | Cómo se mide | Umbral para aceptar |
|---|---|---|
| Toda regla pasa el checklist del estándar | Se aplica el checklist de veinte filas y se sella el resultado | Sin ❌ |
| Toda regla comprobable tiene su comprobación | El catálogo frente a lo que existe | Sin regla comprobable huérfana |
| Ningún documento se entrega con espacios sin llenar | Comprobado por programa | Cero marcas al cerrar |
| Cada cambio de lo que se hereda versiona | Entrada en el registro y número subido | Sin cambio sin versionar |
| Una versión nueva no rompe lo que servía | Se corre lo anterior antes de publicar | Sin falla nueva |

## 17. Los entregables de esta etapa, y a quién van

Qué documentos produce la etapa, con qué molde se escriben y quién los recibe.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Acta de constitución | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), sección 1 | Autor, se firma | Rehecha y firmada: [acta-de-constitucion.md](acta-de-constitucion.md) |
| Estudio de viabilidad | [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md) | Autor, se firma | Rehecho y aprobado: [estudio-factibilidad.md](estudio-factibilidad.md) |
| Visión y alcance | Secciones 1 y 2 de este documento | Autor, se firma | Listo |
| Plan de proyecto | Secciones 9 a 16 de este documento | Autor | Listo |
| Cronograma con hitos | Sección 11 de este documento | Autor | Listo, sin fechas |
| Presupuesto | Sección 8 de este documento | Autor | N/A |
| Desglose del trabajo | Sección 10 de este documento | Autor | Listo, trece paquetes |
| Registro de riesgos | Sección 13 de este documento | Autor | Listo, ocho |
| Roles y responsabilidades | Sección 14 de este documento | Autor | Listo |
| Estimación de esfuerzo | Sección 9 de este documento | Autor | Listo, 173 jornadas |
| Plan de calidad | Sección 16 de este documento | Autor | Listo |
| Plan de comunicaciones | Sección 15 de este documento | Autor y los proyectos | Listo |

## 18. La decisión de la etapa

**Se hace**, decidido por el autor el 2026-08-24.

Ningún frente de viabilidad bloquea y el costo es tiempo propio. Se construye por los trece paquetes de la sección 10, empezando por la plataforma y las reglas servidas, de los que cuelga todo lo demás.

**Sin fecha de entrega, y a propósito:** la plataforma se mantiene mientras se use. Lo que sí tiene fecha es la revisión, al cerrar cada versión.

**Aprobada el 2026-08-24.** Desde esta fecha lo escrito acá es la línea base de la etapa: un cambio de alcance se mide contra esto, y se anota en la sección 19.

## 19. Cambios después de la aprobación

> La etapa se aprobó el 2026-08-24. Lo que cambie desde entonces se anota acá, no se corrige en silencio: la línea base solo sirve si se sabe cuándo se movió y por qué.

| Fecha | Qué cambió | Por qué | Quién lo pidió |
|---|---|---|---|
| 2026-08-24 | El problema dice que el agente es un sistema que crece | Faltaba, y por eso el alcance dejaba fuera la interfaz que ya se estaba construyendo | El usuario |
| 2026-08-24 | Entraron la interfaz y la memoria al alcance | Como estaba, excluía lo que sí se quiere | El usuario |
| 2026-08-24 | **El producto cambia de naturaleza: de un estándar que viaja dentro de cada proyecto a una plataforma central que los administra.** La documentación deja de vivir en cada proyecto, el agente toma las reglas de la plataforma, y el proyecto queda solo con su código | La documentación dentro de cada proyecto no se puede consultar de conjunto ni auditar, y el expediente había que armarlo documento por documento | El usuario |
| 2026-08-24 | Este documento se reescribió entero desde la propuesta, no desde lo construido | Lo escrito antes partía de lo que hoy existe, que era el error de fondo | El usuario |
| 2026-08-24 | La estimación pasa de 116 a 173 jornadas, en trece paquetes | Administrar, auditar y generar el expediente no cabían en el desglose anterior | El agente |

**Lo que este cambio deja sin efecto:** el acta de constitución y el estudio de factibilidad firmados autorizan otro producto. Hay que rehacerlos antes de volver a aprobar la etapa.

## 20. Qué de esta etapa cumple hoy el proyecto

> El análisis del 2026-08-24 comparaba el ciclo contra lo construido. **Ese contraste queda sin valor con el cambio de la sección 19**: se hizo sobre otro producto. Se vuelve a hacer cuando la etapa esté aprobada, y hasta entonces lo honesto es no arrastrar sus números.

**Lo que sí se conserva de aquel análisis**, porque no depende del producto:

| Qué | Sigue siendo cierto |
|---|---|
| Nadie ajeno al autor ha instalado ni usado nada de esto | Sí |
| Ningún respaldo se ha restaurado nunca | Sí |
| Ninguna comprobación corre sola en cada cambio | Sí |

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-24.**
