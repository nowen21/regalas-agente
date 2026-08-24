# Planificación Proyecto: Estándar de trabajo heredable (`agente`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, **por qué vale la pena hacer el proyecto, por qué camino y con qué**: el problema, los límites del alcance, los recursos, el cronograma, los riesgos, quién responde por cada cosa y cómo se le informa a quién. Es la única etapa que puede terminar en «no se hace», y ese también es un resultado que se escribe acá.

> **Prueba de llenado, retrodocumentada el 2026-08-22 sobre v33.1.0.** El proyecto ya está andando: esto se escribe después, para ver qué contesta el molde y qué deja al descubierto. Lo que nunca se decidió se dice así, no se inventa.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. El problema y el objetivo

| Pregunta | Respuesta |
|---|---|
| **¿Cuál es el problema?** | El usuario delega trabajo de desarrollo a un agente de IA y no puede confiar en lo que recibe. En cada sesión vuelve a explicar lo mismo, porque de la anterior no quedó nada. Le entregan como terminado lo que nunca se probó, le cambian cosas que no pidió y se pierde lo que ya estaba acordado. Al abrir otro proyecto, todo empieza de cero. Y del trabajo hecho no queda documentación: sale código, pero nadie escribe qué se construyó, qué necesidad resolvía ni cómo se instala. Meses después el único que puede responder eso es quien lo escribió, y si fue el agente, ya no existe. Y cuando le pasa una clave para que trabaje con ella, esa clave queda escrita en el registro de la conversación, que se guarda y no se borra. Además, lo que delega no es una tarea suelta: el agente hace de analista, de quien construye, de quien prueba y de quien documenta, y cada tanto le hace falta una pieza nueva. Cada pieza que se agrega se lleva por delante lo que ya funcionaba. |
| **¿A quién le pasa?** | Al autor, que delega el trabajo y responde por lo que se entrega. Y a quien reciba el proyecto después: sin documentación no puede retomarlo ni operarlo sin preguntarle a quien lo hizo. |
| **¿Cada cuánto pasa?** | En cada sesión de trabajo, varias veces al día. No es un incidente aislado: es la forma normal de trabajar con el agente. |
| **¿A qué escala?** | Sobre todo lo que el agente entrega, y de nuevo entero en cada proyecto nuevo. Hoy son siete épicas y unos setenta validadores en este repositorio, más los proyectos que lo hereden. |
| **¿Cómo se resuelve hoy?** | Repitiendo las instrucciones en el chat al abrir cada sesión, y revisando a mano todo lo que el agente entrega. La documentación, cuando se hace, se escribe al final y de memoria. |
| **¿Qué se intentó antes?** | Corregir por chat cada vez que el agente se desviaba. Y guardar las preferencias en el almacén de recuerdos de la herramienta. |
| **¿Por qué no funcionó?** | La corrección por chat se va con la conversación. El almacén de la herramienta queda fuera del repositorio: no viaja con el proyecto, no se versiona y nadie más lo ve. |
| **¿Qué le cuesta hoy?** | El costo no es que el agente se equivoque: es que el usuario tiene que revisarlo todo, y revisar cuesta más que hacer. No está medido en horas; se nota en que la misma corrección se ha dado varias veces y en que hay que releer el trabajo entero para saber si sirve. Sin documentación, leer el código para entender qué hace se repite entero cada vez que se retoma el proyecto, y entregarlo a alguien más no es viable. |
| **¿Qué pasa si no se hace nada?** | El retrabajo se repite en cada sesión y crece con cada proyecto. Y lo construido queda sin poderse entregar ni retomar: el conocimiento vive en la cabeza del autor y en conversaciones que ya se borraron. |
| **¿Qué necesita que pase?** | Que lo acordado una vez siga valiendo en la sesión siguiente y en el proyecto siguiente, y poder saber qué se hizo y qué se comprobó sin releerlo todo. Que sea **un solo sistema y no piezas sueltas**, y que pueda crecer: lo que se agregue tiene que entrar sin romper lo anterior, y poder verse desde algún lado sin abrir archivo por archivo. Y que la documentación del ciclo de vida se vaya generando **a medida que se construye**, no esperando al final a redactarla de memoria: cada documento en su `.md`, con la distribución de las plantillas, y el entregable en `.docx` generado por la interfaz desde esos mismos `.md`, para no mantener dos versiones del mismo texto. |

**Objetivo principal**

Desarrollar un sistema de trabajo instalable en cualquier proyecto, que conserve lo acordado con el agente entre sesiones, no le deje cambiar nada sin autorización, deje documentado, comprobado y entregable lo que se construye, y **pueda crecer con piezas nuevas sin romper las anteriores**, para que el usuario no tenga que revisarlo todo ni volver a leer el código para entenderlo.

**Objetivos**

| # | Objetivo | En qué se nota | Para quién |
|---|---|---|---|
| 1 | Conservar lo acordado entre una sesión y la siguiente | La corrección se da una vez y la siguiente ya la respeta | El usuario |
| 2 | Heredar en cada proyecto nuevo lo ya aprendido | Al abrirlo, ya rige lo aprendido en los anteriores | El usuario, en cada proyecto nuevo |
| 3 | Reducir el tiempo que el usuario gasta revisando | Aprueba leyendo lo entregado, no rehaciéndolo | El usuario |
| 4 | Comprobar antes de entregar, y declarar lo no comprobado | Lo entregado dice qué se probó, y lo que no, también | El usuario |
| 5 | Entregar terminado lo que se declara terminado | No aparece a medias lo que se dio por cerrado | El usuario |
| 6 | Impedir cambios de estado sin autorización del usuario | No aparecen cambios que no pidió | El usuario |
| 7 | Avisar antes de lo que no se puede deshacer | Nada se pierde sin que él lo haya autorizado | El usuario |
| 8 | Registrar fuera del chat lo que la sesión dejó | Se sabe qué pasó sin releer el trabajo entero | El usuario y la sesión siguiente |
| 9 | Proteger las credenciales de quedar escritas en claro | Ninguna clave suya queda registrada en el repositorio | El usuario |
| 10 | Documentar lo construido mientras se construye, no después | Cada cosa entregada llega con qué hace y para qué | El usuario |
| 11 | Dejar por escrito cómo se instala y se opera | Otra persona lo levanta sin preguntarle a quien lo hizo | Quien reciba el proyecto |
| 12 | Generar el entregable de ofimática desde lo ya escrito | Recibe el `.docx` sin que nadie lo redigite | El usuario y quien reciba el proyecto |
| 13 | Agregar piezas nuevas sin romper las que ya servían | Lo que funcionaba ayer sigue funcionando después de cada versión | El usuario y los proyectos que heredan |
| 14 | Ver desde una pantalla lo que el agente hace y guarda | Revisa sin abrir archivo por archivo | El usuario |

## 2. El alcance

> **El alcance es la frontera del proyecto: todo lo que el sistema va a hacer, y todo lo que no.** No es la lista de funciones, que va al inventario; es hasta dónde llega el compromiso.

| ¿Qué se incluye? | ¿Qué queda fuera? | ¿Por qué queda fuera? |
|---|---|---|
| Reglas agnósticas de stack, en `base/` | Reglas de un framework o de un cliente | `M3` y `M13`: lo que sirve a un solo stack no se hereda |
| Moldes de documento, en `plantillas/` | El contenido de los documentos de cada proyecto | El molde viaja; lo llenado se queda en su proyecto |
| Validadores y enganches | Un servicio en línea, o alojado por un tercero | El sistema corre en la máquina de quien trabaja, sin depender de nadie más |
| Una interfaz local para ver los documentos del ciclo y lo que el agente guarda | Editar el `.docx` y devolverlo al `.md` | La fuente es el `.md`; el `.docx` es una salida, y una salida no se edita |
| La memoria de lo aprendido, guardada y consultable | Que la memoria viva en el almacén de la herramienta | Ahí no viaja con el proyecto, no se versiona y nadie más la ve |
| Que el sistema pueda crecer: piezas nuevas que entran sin romper las anteriores | Crecer sin comprobar que lo anterior sigue sirviendo | Cada pieza nueva se lleva por delante lo que ya funcionaba, y eso es parte del problema |
| Instalación y aviso de desfase | Actualización automática sin aprobación | `N1`: ningún cambio de estado sin aprobación explícita |



## 3. Supuestos

> **Un supuesto es un hecho que el plan necesita cierto y nadie comprobó.** Si alguno falla, el plan cambia. Es lo más barato de escribir y lo más caro de omitir: un supuesto falso explica la mayoría de los proyectos que se pasan de plazo.

| # | Se da por cierto que | ¿Qué pasa si resulta falso? | ¿Quién lo confirma¿ |
|---|---|---|---|
| 1 | El agente obedece lo escrito si se le carga al abrir la sesión | El estándar entero pierde sentido: habría que hacerlo cumplir por fuera | El uso diario |
| 2 | Lo que sirve para este usuario sirve para otro | Queda como preferencia personal, no como estándar | Instalarlo en un proyecto ajeno |
| 3 | Las reglas escritas en `.md` bastan; no hace falta código para hacerlas cumplir | Cada regla necesitaría su validador, y el costo se multiplica | Los incumplimientos que aparezcan |
| 4 | La documentación escrita mientras se construye no atrasa el trabajo | Habría que elegir entre documentar y avanzar | Medir el retrabajo evitado |

## 4. Restricciones

> **Una restricción es un límite que el proyecto no puede mover:** viene dado por alguien de afuera o por una decisión ya tomada. La que no se escribe se descubre cuando ya se construyó en contra de ella.

| Tipo | Restricción | ¿De dónde viene? | Cómo se sabe si se rompió |
|---|---|---|---|
| Plazo | Sin fecha de entrega: el estándar se mantiene mientras se use | El propio proyecto | No aplica: no hay plazo que vencer |
| Presupuesto | Sin costo monetario; solo tiempo del autor | Decisión del autor | Aparecería una dependencia paga o un servicio contratado |
| Tecnología o plataforma | Python de la biblioteca estándar y los enganches de Claude Code, sin infraestructura propia | Debe correr donde ya corre el agente | Una importación de paquete de terceros en `validadores/`. **Hoy nadie lo comprueba: falta esa comprobación** |
| Formato de los entregables | Se escriben en `.md`, uno por documento del ciclo, con la distribución de las plantillas. El `.docx` no se escribe a mano: lo genera la interfaz desde esos `.md` | Necesidad de entregar al cliente en formato de ofimática sin duplicar la fuente | Un `.docx` con cambios que no están en su `.md`. **Falta esa comprobación, y el generador todavía no existe** |
| Normativa o licencias | Sin datos personales ni de terceros; las credenciales no se escriben | `N6` | El enmascarado corre al guardar, y una comprobación rechaza el guardado si encuentra una clave |

## 5. Dependencias de terceros

> **Una dependencia es algo que el proyecto necesita y no puede producir:** lo entrega alguien que no está en el equipo, y por eso no se le puede exigir la fecha.

| ¿De quién o de qué? | ¿Qué se necesita? | ¿Para cuándo? | ¿Qué se hace si no llega? |
|---|---|---|---|
| Claude Code | Que siga permitiendo enganches al abrir y cerrar sesión | Permanente | Las reglas quedan escritas, pero se cargan a mano |
| Un proyecto ajeno | Alguien que no sea el autor que lo adopte | Sin fecha | Sigue siendo preferencia personal, no estándar |

## 6. Viabilidad, en cuatro frentes

> **Viable es lo que se puede hacer con lo que hay: capacidad, dinero, tiempo y permiso legal.** No pregunta si conviene, que es la decisión de la sección 18; pregunta si es posible.

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la tecnología y el conocimiento para hacerlo? | Sí: archivos `.md`, Python de la biblioteca estándar y los enganches que ya trae Claude Code | No |
| Económica | ¿Los beneficios justifican el costo? | Sí: el costo es tiempo del propio autor; lo que ahorra es la corrección repetida en cada proyecto | No |
| Operativa | ¿La organización y los usuarios lo van a adoptar? | Un solo usuario, que es quien lo escribe. La adopción real se prueba al instalarlo en un proyecto ajeno | No, pero es el frente sin evidencia |
| Legal | ¿Cumple normativas, licencias y protección de datos? | Sin datos personales ni terceros. Las credenciales quedan cubiertas por `N6` y el enmascarado automático | No |




## 7. Recursos

**Personas.**

| Perfil | ¿Cuántas? | Dedicación | ¿Quién? |
|---|---|---|---|
| Autor del estándar, y quien aprueba | 1 | Sin cuota fija | Ing. José Dúmar Jiménez Ruíz |
| Agente que redacta y construye | 1 | Por sesión | Claude Code |

**Infraestructura, herramientas y licencias.**

| Qué | Para qué | Costo | ¿Ya se tiene? |
|---|---|---|---|
| Git y un repositorio remoto | Versionar el estándar y distribuirlo | Sin costo | Sí |
| Python 3 | Correr validadores y enganches | Sin costo | Sí |
| Claude Code | Ejecutar el agente que obedece las reglas | Suscripción ya vigente | Sí |

## 8. Presupuesto

N/A porque no hay costo monetario que asignar: el único recurso es tiempo del autor, y las herramientas ya estaban pagas antes del proyecto.

## 9. Estimación de esfuerzo

**Técnica usada: juicio experto, en jornadas de trabajo.** Se estima cada paquete de la sección 10 como si se construyera desde cero.

| Paquete del desglose | Esfuerzo | Supuesto del que depende |
|---|---|---|
| 1 · Cuerpo de reglas que se carga y manda | 20 jornadas | Que la regla se escribe una vez y se corrige con el uso, no de nuevo |
| 2 · Herencia e instalación en otro proyecto | 8 jornadas | Que el proyecto que hereda corre la misma herramienta |
| 3 · Comprobación automática de lo exigido | 25 jornadas | Que cada regla validable admite comprobación mecánica (supuesto 3) |
| 4 · Registro de lo que la sesión deja | 5 jornadas | Que la herramienta permite enganches al abrir y cerrar |
| 5 · Enmascarado de credenciales | 3 jornadas | Que las formas de escribir una clave son pocas y conocidas |
| 6 · Moldes del ciclo de vida | 15 jornadas | Que documentar mientras se construye no atrasa (supuesto 4) |
| 7 · Interfaz local: visor y generador | 20 jornadas | Que basta convertir en un sentido, sin edición de vuelta, y que el visor solo lee |
| 8 · Medición del tiempo de revisión | 2 jornadas | Que hay con qué comparar el antes y el después |
| 9 · Memoria de lo aprendido | 12 jornadas | Que guardar y consultar basta, sin buscar por parecido |
| 10 · Que lo nuevo no rompa lo anterior | 6 jornadas | Que lo que ya servía tiene prueba que lo demuestre |

**Total: 116 jornadas, con margen de un tercio hacia arriba.** El paquete 3 es el que más puede correrse: el esfuerzo de comprobar depende de cuántas reglas resulten validables, y eso solo se sabe escribiéndolas.

**Esta estimación se hizo al retrodocumentar, no al abrir el proyecto.** Sirve para dimensionar lo que falta y para comparar con quien quiera adoptarlo, no para medir desvío: no hay registro de horas contra el cual contrastarla.

## 10. Desglose del trabajo (WBS/EDT)

**Desglose (WBS/EDT).** Sale de los doce objetivos, no de lo ya construido: es lo que hay que hacer para resolver el problema, esté hecho o no.

> **Rige desde el 2026-08-24.** No se hizo antes de empezar, y eso no se puede cambiar: lo que sí se hizo fue rehacerlo desde los objetivos, para que el trabajo que queda salga del problema y no de lo que ya estaba construido.

| Código | Paquete de trabajo | Objetivos que atiende | Depende de | Duración | Responsable |
|---|---|---|---|---|---|
| 1 | Cuerpo de reglas que se carga y manda al abrir la sesión | 1, 6, 7 | — | Sin estimar | Autor |
| 2 | Herencia: instalar el estándar en un proyecto ajeno y avisarle cuando cambie | 2 | 1 | Sin estimar | Autor |
| 3 | Comprobación automática de lo que se exige | 4, 5 | 1 | Sin estimar | Autor |
| 4 | Registro de lo que cada sesión deja, fuera del chat | 8 | 1 | Sin estimar | Autor |
| 5 | Enmascarado de credenciales en todo lo que se escribe | 9 | 1 | Sin estimar | Autor |
| 6 | Moldes del ciclo de vida, para documentar mientras se construye | 10, 11 | 1 | Sin estimar | Autor |
| 7 | Interfaz local: ver los documentos del ciclo y la memoria, y generar el `.docx` | 12, 14 | 6, 9 | Sin estimar | Autor |
| 8 | Medición del tiempo de revisión, antes y después | 3 | 3, 4 | Sin estimar | Autor |
| 9 | Memoria de lo aprendido: se guarda, se consulta y sobrevive a la sesión | 8, 14 | 4 | Sin estimar | Autor |
| 10 | Que lo nuevo no rompa lo anterior: comprobación de lo que ya servía | 13 | 3 | Sin estimar | Autor |

## 11. Cronograma

> **El cronograma pone fechas al desglose de la sección 10:** cuándo se alcanza cada hito y qué cadena de tareas no admite atraso. Sin desglose no hay cronograma: son fechas puestas sobre nada.

**Hitos y fecha de entrega.**

| Hito | Fecha | Qué tiene que estar listo para darlo por cumplido |
|---|---|---|
| Las reglas se cargan solas y ganan ante cualquier choque | Cumplido | El núcleo se carga al abrir y nada lo contradice |
| Lo que se exige se comprueba sin que nadie se acuerde | Cumplido | Cada regla validable tiene su comprobación corriendo |
| El ciclo se documenta mientras se construye | En curso | Los moldes del ciclo, con el de planificación en evaluación |
| Instalado en un proyecto que no es del autor | Sin fecha | Alguien ajeno lo adopta y lo usa una semana |
| El entregable sale de lo escrito, sin redigitar | Sin fecha | La interfaz genera el `.docx` desde los `.md` |
| Fecha de entrega del proyecto | Sin fecha | No la hay: el estándar se mantiene mientras se use |

**Ruta crítica: paquetes 1, 3, 6 y 7.** Sin reglas escritas no hay qué comprobar; sin comprobación la regla se incumple sin que nadie se entere; sin moldes no hay documento escrito mientras se construye; y sin documento escrito no hay de dónde generar el entregable.

> La ruta crítica es la cadena de tareas que no admite atraso: si una se corre un día, la entrega se corre un día.

## 12. Modelo de desarrollo

**Se usa iterativo e incremental**, en fases que caben en una jornada y se revierten desde el control de versiones. Los requisitos aparecen al usar el estándar —cada incumplimiento del agente es un pendiente nuevo—, así que fijarlos por adelantado no era posible.

## 13. Riesgos

| # | Riesgo | Probabilidad | Impacto | Responsable | Mitigación | Qué se hace si ocurre |
|---|---|---|---|---|---|---|
| 1 | El agente escribe el estándar sin haber leído el estándar | Alta | Alto | Autor | El paso 0 del `CLAUDE.md` carga `base/` antes de tocar nada | Se corrige el `CLAUDE.md` y queda como señal |
| 2 | Dos reglas se contradicen entre capítulos | Media | Alto | Autor | El núcleo gana siempre; `M12` obliga a buscar antes de crear | Se deroga la más nueva (`M11`), nunca se borra |
| 3 | Una regla se escribe pero nadie la comprueba | Alta | Medio | Autor | `M9` decide si es validable al escribirla | Entra a `pendientes/` con su validador por hacer |
| 4 | Un proyecto adopta una versión y queda atrás sin saberlo | Media | Medio | Autor | Aviso de desfase al abrir sesión (EP-002) | Se le informa qué cambió desde su versión |
| 5 | El estándar crece hasta que nadie lo lee entero | Media | Alto | Autor | `ID9` y el presupuesto de extensión por regla | Se recorta al molde y el porqué se va a `notas/` |
| 6 | Una credencial queda escrita en claro | Baja | Alto | Autor | `N6` y el enmascarado automático | Se rota la credencial y se limpia el histórico |
| 7 | Todo depende de una sola persona | Alta | Alto | Autor | Queda escrito y legible sin su autor | El estándar se congela en su última versión y sigue sirviendo |
| 8 | Nadie ajeno lo adopta, y queda como preferencia personal | Alta | Alto | Autor | Instalarlo en un proyecto que no sea del autor | Se acepta como herramienta personal y se deja de llamar estándar |
| 9 | Las pruebas corren solo cuando alguien se acuerda | Alta | Medio | Autor | Una canalización de integración continua, que hoy no existe | Se construye, y hasta entonces se corre la batería antes de cada publicación |
| 10 | Un respaldo que nunca se restauró resulta inservible | Baja | Alto | Autor | Restaurar de verdad, cada tres meses | Se rehace desde la copia que sí sirva, y se pierde lo que no esté publicado |
| 11 | Historias sin fase, que dejan el inventario detenido | Media | Medio | Autor | La comprobación de historias sin fase, y el pendiente [48](../../pendientes/48-inventario-hu.md) | Se abren las fases que faltan antes de seguir |
| 12 | Ideas del usuario que se pierden por no escribirse | Media | Bajo | Autor | La libreta de ideas, pendiente [10](../../pendientes/10-ideas.md) | Se recogen en la sesión siguiente, que para eso quedan escritas |
| 13 | Una pieza nueva rompe lo que ya funcionaba | Alta | Alto | Autor | El paquete 10: comprobar lo anterior antes de publicar | Se revierte la pieza y se publica una versión de corrección |

> **De dónde salen del 7 al 12.** Los seis primeros se escribieron al planear; estos seis se recogieron de `pendientes/` y del análisis del ciclo el 2026-08-24, que era el hallazgo: los riesgos existían sueltos y sin probabilidad ni impacto.

## 14. Roles y responsabilidades

> **Quién hace, quién responde, a quién se consulta y a quién se informa**, por actividad. Hacer y responder no son lo mismo: si una fila tiene dos responsables, no tiene ninguno.

| Actividad o entregable | Quién lo hace | Quién responde | A quién se consulta | A quién se informa |
|---|---|---|---|---|
| Escribir y derogar reglas de `base/` | Agente | Autor | Autor | — |
| Aprobar el cambio, y aparte el commit | Autor | Autor | — | — |
| Validadores y enganches | Agente | Autor | Autor | — |
| Versionar (`CHANGELOG` y `VERSION`) | Agente | Autor | — | Proyectos que heredan |

**Quién aprueba las entregas: el autor.** Que apruebe el cambio no es que apruebe el commit: se pregunta aparte.

## 15. Interesados y comunicación

| Interesado | Qué papel tiene | Influencia | Qué recibe | Cada cuánto | En qué formato |
|---|---|---|---|---|---|
| Ing. José Dúmar Jiménez Ruíz | Paga, usa y aprueba, los tres | Alta | El cambio antes de commitear | Por sesión | En el chat, con el enlace al archivo |
| Proyectos que heredan el estándar | Consumen las reglas | Ninguna | Aviso de desfase y `CHANGELOG` | Al abrir sesión | Aviso automático |
| El agente de la sesión siguiente | Ejecuta lo escrito | Ninguna | Histórico, resumen, señales y memoria | Al abrir sesión | Archivos del repositorio |

**Acordado el 2026-08-24 por el autor**, que es quien paga, usa y aprueba, así que el acuerdo es con él mismo y por eso se escribe: cada cambio se le muestra antes de guardarlo, con el enlace al archivo; los proyectos que heredan reciben el aviso de desfase sin pedirlo; y la sesión siguiente recibe lo escrito en el repositorio, nunca lo dicho en el chat.

**Lo que nadie recibe, y se dice:** no hay informe periódico de avance. El estado se lee en el repositorio cuando alguien quiera, y no se reporta aparte.

## 16. Plan de calidad

| Qué se exige | Cómo se mide | Umbral para aceptar |
|---|---|---|
| Toda regla pasa el checklist del estándar | Se aplica el checklist de 20 filas y se sella el resultado | Sin ❌ |
| Toda regla validable tiene su validador | `validadores/reglas-validables.md` frente a `validadores/` | Sin regla validable huérfana |
| Ningún documento se entrega con marcas `«…»` | `13·DOC20`, comprobado por validador | Cero marcas al cerrar |
| Cada cambio de `base/` o `plantillas/` versiona | Entrada en `CHANGELOG.md` y `VERSION` subido | Sin cambio sin versionar |



## 17. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Acta de constitución (*project charter*) | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), sección 1 | Autor — se firma | Escrita en [acta-de-constitucion.md](acta-de-constitucion.md), sin firmar |
| Estudio de viabilidad | [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md) | Autor — se firma | Escrito en [estudio-factibilidad.md](estudio-factibilidad.md), con cinco alternativas; sin aprobar |
| Visión y alcance | [plantillas/ciclo-vida-proyectos/01-planteamiento.md](../../plantillas/ciclo-vida-proyectos/01-planteamiento.md), secciones 1 a 4 | Autor — se firma | Secciones 1 y 2 de este documento, más [planteamiento.md](../../planteamiento.md); sin aprobar |
| Plan de proyecto | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), secciones 2 a 5 | Autor | Escrito en [acta-de-constitucion.md](acta-de-constitucion.md), secciones 2 a 5 |
| Cronograma con hitos y fecha | Sección 11 de este documento | Autor | Listo, sin fecha de entrega |
| Presupuesto | Sección 8 de este documento | Autor | N/A |
| Desglose del trabajo (WBS/EDT) | Sección 10 de este documento | Autor | Listo, con las épicas como desglose |
| Registro de riesgos | Sección 13 de este documento | Autor | Listo |
| Roles y matriz de responsabilidades | Sección 14 de este documento | Autor | Listo |
| Estimación de esfuerzo | Sección 9 de este documento | Autor | Listo, por juicio experto al retrodocumentar |
| Plan de calidad | Sección 16 de este documento | Autor | Listo |
| Plan de comunicaciones | Sección 15 de este documento | Autor y proyectos que heredan | Listo |

## 18. La decisión de la etapa

**Se hace, por la alternativa 1 del [estudio de factibilidad](estudio-factibilidad.md)**, decidido por el autor el 2026-08-24.

Ningún frente de viabilidad bloquea y el costo es tiempo propio, así que la pregunta no es si conviene hacerlo sino si sirve para alguien más. Se construye por los ocho paquetes de la sección 10, empezando por los dos de mayor incertidumbre: la comprobación automática, que decide si el diseño se sostiene, y la instalación en un proyecto ajeno, que confirma el supuesto del que depende todo.

**Sin fecha de entrega, y a propósito:** el estándar no se entrega, se mantiene mientras se use. Lo que sí tiene fecha es la revisión, al cerrar cada versión.

**Lo que queda pendiente de esta etapa no es escribir, es aprobar.** Todo lo de arriba está en borrador; mientras nadie lo firme, no hay línea base contra la cual medir un cambio de alcance.

## 19. Cambios después de la aprobación

> La etapa se aprobó el 2026-08-24. Lo que cambie desde entonces se anota acá, no se corrige en silencio: la línea base solo sirve si se sabe cuándo se movió y por qué.

| Fecha | Qué cambió | Por qué | Quién lo pidió |
|---|---|---|---|
| 2026-08-24 | El problema ahora dice que el agente es **un sistema que crece**, y que cada pieza nueva se llevaba por delante lo anterior | Faltaba en el problema, y por eso el alcance dejaba fuera la interfaz que ya se estaba construyendo | El usuario |
| 2026-08-24 | El alcance: entran la interfaz local y la memoria consultable; lo que queda fuera pasa a ser **un servicio en línea o de terceros**, no «un panel» | Como estaba, excluía lo que sí se quiere | El usuario |
| 2026-08-24 | Dos objetivos más: crecer sin romper lo anterior, y ver desde una pantalla lo que el agente hace y guarda | Salen del problema corregido | El usuario |
| 2026-08-24 | El desglose pasa de 8 a 10 paquetes, y la estimación de 88 a 116 jornadas | Los objetivos nuevos necesitan trabajo, y decirlo sin estimarlo sería prometer gratis | El agente |
| 2026-08-24 | Un riesgo más: una pieza nueva rompe lo que ya funcionaba | Es el riesgo que el problema corregido deja a la vista | El agente |

## 20. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. Los trece hallazgos quedaron escritos y aprobados ese mismo día. El resumen de las siete etapas, y lo que ese análisis no puede decir, están en [cvds/README.md](../README.md).

**Los trece hallazgos de esta etapa, y qué se escribió para cada uno**

| # | Hallazgo del análisis | Qué se hizo | Dónde quedó |
|---|---|---|---|
| 1 | El desglose existía como las 7 épicas, y nunca se hizo antes de empezar | Se rehízo desde los doce objetivos, con la columna que dice a cuál atiende cada paquete | Sección 10 |
| 2 | Los riesgos vivían sueltos en `pendientes/` sin probabilidad ni impacto | Se recogieron seis riesgos más, con probabilidad, impacto, responsable y qué se hace si ocurre | Sección 13, filas 7 a 12 |
| 3 | Los interesados no estaban escritos | Se escribieron los tres, con qué recibe cada uno y cada cuánto, y qué nadie recibe | Sección 15 |
| 4 | Las restricciones se cumplían sin estar declaradas | Se declararon las cinco, y cada una dice cómo se sabría si se rompió. Dos no tienen con qué comprobarse todavía, y se dice | Sección 4 |
| 5 | Los entregables de la etapa no tenían tabla | Se escribió, con el molde de cada uno, a quién va y en qué estado | Sección 17 |
| 6 | No había estudio de viabilidad | Escrito, con cinco alternativas y por qué se descartaron cuatro | [estudio-factibilidad.md](estudio-factibilidad.md) |
| 7 | No había acta de constitución | Escrita, con qué se autoriza y **qué no** | [acta-de-constitucion.md](acta-de-constitucion.md) |
| 8 | No había supuestos | Cuatro, con qué pasa si cada uno resulta falso y quién lo confirma | Sección 3 |
| 9 | No había dependencias de terceros | Dos, con qué se hace si no llegan | Sección 5 |
| 10 | No había estimación de esfuerzo | 88 jornadas por juicio experto, paquete por paquete, con margen declarado | Sección 9 |
| 11 | No había presupuesto | `N/A` con su porqué: no hay costo monetario que asignar | Sección 8 |
| 12 | No había cronograma con hitos | Cinco hitos, con qué los da por cumplidos, y sin fechas dicho a propósito | Sección 11 |
| 13 | No había decisión de cierre | Se hace, por la alternativa 1, con qué se construye primero y por qué | Sección 18 |

**Nada queda abierto en esta etapa.**

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-24.** Desde esta fecha lo escrito acá es la línea base de la etapa: un cambio de alcance se mide contra esto.
