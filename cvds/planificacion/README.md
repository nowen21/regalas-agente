# Planificación Proyecto: Estándar de trabajo heredable (`agente`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito, antes de comprometer trabajo, **por qué vale la pena hacer el proyecto, por qué camino y con qué**: el problema, los límites del alcance, los recursos, el cronograma, los riesgos, quién responde por cada cosa y cómo se le informa a quién. Es la única etapa que puede terminar en «no se hace», y ese también es un resultado que se escribe acá.

> **Prueba de llenado, retrodocumentada el 2026-08-22 sobre v33.1.0.** El proyecto ya está andando: esto se escribe después, para ver qué contesta el molde y qué deja al descubierto. Lo que nunca se decidió se dice así, no se inventa.

**Estado: BORRADOR** (2026-08-22, sin aprobar).

---

## 1. El problema y el objetivo

**¿Cuál es el problema?**

El usuario delega trabajo de desarrollo a un agente de IA y no puede confiar en lo que recibe. En cada sesión vuelve a explicar lo mismo, porque de la anterior no quedó nada. Le entregan como terminado lo que nunca se probó, le cambian cosas que no pidió y se pierde lo que ya estaba acordado. Al abrir otro proyecto, todo empieza de cero.

Y del trabajo hecho no queda documentación: sale código, pero nadie escribe qué se construyó, qué necesidad resolvía ni cómo se instala. Meses después el único que puede responder eso es quien lo escribió, y si fue el agente, ya no existe.

**¿Qué le cuesta hoy?**

El costo no es que el agente se equivoque: es que el usuario tiene que revisarlo todo, y revisar cuesta más que hacer. No está medido en horas; se nota en que la misma corrección se ha dado varias veces y en que hay que releer el trabajo entero para saber si sirve. Sin documentación, ese trabajo de leer el código para entender qué hace se repite entero cada vez que se retoma el proyecto, y entregarlo a alguien más no es viable.

**¿Qué necesita que pase?**

Que lo acordado una vez siga valiendo en la sesión siguiente y en el proyecto siguiente, y poder saber qué se hizo y qué se comprobó sin releerlo todo.

Y que la documentación del ciclo de vida se vaya generando **a medida que se construye**, no esperando al final a redactarla de memoria: cada documento en su `.md`, con la distribución de las plantillas, y el entregable en `.docx` generado por la interfaz desde esos mismos `.md`, para no mantener dos versiones del mismo texto.

**Objetivo principal**

Desarrollar un estándar de trabajo instalable en cualquier proyecto, que conserve lo acordado con el agente entre sesiones y deje documentado y comprobado lo que se construye, para que el usuario no tenga que revisarlo todo ni volver a leer el código para entenderlo.

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
| 9 | Advertir cuando cambie lo que ya estaba acordado | Se entera de qué cambió sin ir a buscarlo | Los proyectos que heredan |
| 10 | Proteger las credenciales de quedar escritas en claro | Ninguna clave suya queda registrada en el repositorio | El usuario |
| 11 | Documentar lo construido mientras se construye, no después | Cada cosa entregada llega con qué hace y para qué | El usuario |
| 12 | Dejar por escrito cómo se instala y se opera | Otra persona lo levanta sin preguntarle a quien lo hizo | Quien reciba el proyecto |
| 13 | Generar el entregable de ofimática desde lo ya escrito | Recibe el `.docx` sin que nadie lo redigite | El usuario y quien reciba el proyecto |

## 2. El alcance, y sobre todo lo que queda fuera

| Entra | Queda fuera | Por qué queda fuera |
|---|---|---|
| Reglas agnósticas de stack, en `base/` | Reglas de un framework o de un cliente | `M3` y `M13`: lo que sirve a un solo stack no se hereda |
| Moldes de documento, en `plantillas/` | El contenido de los documentos de cada proyecto | El molde viaja; lo llenado se queda en su proyecto |
| Validadores y enganches | Un servidor o un panel de administración | El estándar corre donde ya corre el agente, sin infraestructura propia |
| La interfaz que convierte los `.md` del ciclo en `.docx` | Editar el `.docx` y devolverlo al `.md` | La fuente es el `.md`; el `.docx` es una salida, y una salida no se edita |
| Instalación y aviso de desfase | Actualización automática sin aprobación | `N1`: ningún cambio de estado sin aprobación explícita |

El alcance ítem por ítem no va acá: va al inventario, [plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md](../../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), y **aprobado por el usuario** es la puerta de las épicas ([`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).

## 3. Supuestos, restricciones y dependencias

**Supuestos.** Se dan por ciertos, y si alguno falla el plan cambia.

| # | Se da por cierto que | Qué pasa si resulta falso | Quién lo confirma |
|---|---|---|---|
| 1 | El agente obedece lo escrito si se le carga al abrir la sesión | El estándar entero pierde sentido: habría que hacerlo cumplir por fuera | El uso diario |
| 2 | Lo que sirve para este usuario sirve para otro | Queda como preferencia personal, no como estándar | Instalarlo en un proyecto ajeno |
| 3 | Las reglas escritas en `.md` bastan; no hace falta código para hacerlas cumplir | Cada regla necesitaría su validador, y el costo se multiplica | Los incumplimientos que aparezcan |
| 4 | La documentación escrita mientras se construye no atrasa el trabajo | Habría que elegir entre documentar y avanzar | Medir el retrabajo evitado |

**Restricciones.** No se negocian: vienen dadas.

| Tipo | Restricción | De dónde viene |
|---|---|---|
| Plazo | Sin fecha de entrega: el estándar se mantiene mientras se use | El propio proyecto |
| Presupuesto | Sin costo monetario; solo tiempo del autor | Decisión del autor |
| Tecnología o plataforma | Python de la biblioteca estándar y los enganches de Claude Code, sin infraestructura propia | Debe correr donde ya corre el agente |
| Formato de los entregables | Se escriben en `.md`, uno por documento del ciclo, con la distribución de las plantillas. El `.docx` no se escribe a mano: lo genera la interfaz desde esos `.md` | Necesidad de entregar al cliente en formato de ofimática sin duplicar la fuente |
| Normativa o licencias | Sin datos personales ni de terceros; las credenciales no se escriben | `N6` |

**Dependencias de terceros.** Lo que el proyecto necesita de alguien que no está en el equipo.

| De quién o de qué | Qué se necesita | Para cuándo | Qué se hace si no llega |
|---|---|---|---|
| Claude Code | Que siga permitiendo enganches al abrir y cerrar sesión | Permanente | Las reglas quedan escritas, pero se cargan a mano |
| Un proyecto ajeno | Alguien que no sea el autor que lo adopte | Sin fecha | Sigue siendo preferencia personal, no estándar |

## 4. Viabilidad, en cuatro frentes

| Frente | Pregunta | Respuesta | ¿Bloquea? |
|---|---|---|---|
| Técnica | ¿Existe la tecnología y el conocimiento para hacerlo? | Sí: archivos `.md`, Python de la biblioteca estándar y los enganches que ya trae Claude Code | No |
| Económica | ¿Los beneficios justifican el costo? | Sí: el costo es tiempo del propio autor; lo que ahorra es la corrección repetida en cada proyecto | No |
| Operativa | ¿La organización y los usuarios lo van a adoptar? | Un solo usuario, que es quien lo escribe. La adopción real se prueba al instalarlo en un proyecto ajeno | No, pero es el frente sin evidencia |
| Legal | ¿Cumple normativas, licencias y protección de datos? | Sin datos personales ni terceros. Las credenciales quedan cubiertas por `N6` y el enmascarado automático | No |

**Recomendación: continuar.** Ningún frente bloquea; el único sin evidencia es el operativo, y se cierra instalándolo fuera de este repositorio.

El análisis largo, con las alternativas descartadas, vive en [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md); acá va solo su conclusión.

## 5. Recursos

**Personas.**

| Perfil | Cuántas | Dedicación | Quién |
|---|---|---|---|
| Autor del estándar, y quien aprueba | 1 | Sin cuota fija | Ing. José Dúmar Jiménez Ruíz |
| Agente que redacta y construye | 1 | Por sesión | Claude Code |

**Infraestructura, herramientas y licencias.**

| Qué | Para qué | Costo | ¿Ya se tiene? |
|---|---|---|---|
| Git y un repositorio remoto | Versionar el estándar y distribuirlo | Sin costo | Sí |
| Python 3 | Correr validadores y enganches | Sin costo | Sí |
| Claude Code | Ejecutar el agente que obedece las reglas | Suscripción ya vigente | Sí |

## 6. Presupuesto

N/A porque no hay costo monetario que asignar: el único recurso es tiempo del autor, y las herramientas ya estaban pagas antes del proyecto.

## 7. Estimación de esfuerzo

**Técnica usada: ninguna.** No se estimó al abrir el proyecto, y se dice en vez de reconstruirlo hacia atrás. Lo que hay es el tamaño alcanzado: 7 épicas, 33 versiones publicadas y unos 70 validadores al 2026-08-22.

**Lo que este hueco deja al descubierto:** sin estimación no hay contra qué comparar el avance, y por eso el proyecto se mide por versiones cerradas y no por esfuerzo consumido.

## 8. Cronograma y desglose del trabajo

**Desglose (WBS/EDT).** Las épicas son el desglose real; no hubo uno previo.

| Código | Paquete de trabajo | Depende de | Duración | Responsable |
|---|---|---|---|---|
| EP-001 | Cuerpo de reglas heredable | — | Abierta | Autor |
| EP-002 | Versionado y adopción | EP-001 | Abierta | Autor |
| EP-003 | Documentos modelo y procedimientos | EP-001 | Abierta | Autor |
| EP-004 | Comprobación automática | EP-001, EP-003 | Abierta | Autor |
| EP-005 | Automatismos que no dependen de la memoria | EP-004 | Abierta | Autor |
| EP-006 | Memoria de lo aprendido | EP-005 | Abierta | Autor |
| EP-007 | Instalación y actualización | EP-002 | Abierta | Autor |

**Hitos y fecha de entrega.**

| Hito | Fecha | Qué tiene que estar listo para darlo por cumplido |
|---|---|---|
| Núcleo blindado que no se sobrescribe | Cumplido | `base/00-nucleo-blindado.md` se carga y gana ante cualquier choque |
| Instalación en un proyecto que hereda | Cumplido | `validadores/instalar.py` lo deja funcionando |
| El aviso de desfase llega al abrir sesión | Cumplido | La sesión dice qué cambió respecto de la versión adoptada |
| Fecha de entrega del proyecto | Sin fecha | El estándar no se entrega: se mantiene mientras se use |

**Ruta crítica: EP-001 → EP-004.** Sin reglas escritas no hay qué validar, y sin validador la regla se incumple sin que nadie se entere.

## 9. Modelo de desarrollo

**Se usa iterativo e incremental**, en fases que caben en una jornada y se revierten desde el control de versiones. Los requisitos aparecen al usar el estándar —cada incumplimiento del agente es un pendiente nuevo—, así que fijarlos por adelantado no era posible.

## 10. Riesgos

| # | Riesgo | Probabilidad | Impacto | Responsable | Mitigación | Qué se hace si ocurre |
|---|---|---|---|---|---|---|
| 1 | El agente escribe el estándar sin haber leído el estándar | Alta | Alto | Autor | El paso 0 del `CLAUDE.md` carga `base/` antes de tocar nada | Se corrige el `CLAUDE.md` y queda como señal |
| 2 | Dos reglas se contradicen entre capítulos | Media | Alto | Autor | El núcleo gana siempre; `M12` obliga a buscar antes de crear | Se deroga la más nueva (`M11`), nunca se borra |
| 3 | Una regla se escribe pero nadie la comprueba | Alta | Medio | Autor | `M9` decide si es validable al escribirla | Entra a `pendientes/` con su validador por hacer |
| 4 | Un proyecto adopta una versión y queda atrás sin saberlo | Media | Medio | Autor | Aviso de desfase al abrir sesión (EP-002) | Se le informa qué cambió desde su versión |
| 5 | El estándar crece hasta que nadie lo lee entero | Media | Alto | Autor | `ID9` y el presupuesto de extensión por regla | Se recorta al molde y el porqué se va a `notas/` |
| 6 | Una credencial queda escrita en claro | Baja | Alto | Autor | `N6` y el enmascarado automático | Se rota la credencial y se limpia el histórico |

## 11. Roles y responsabilidades

| Actividad o entregable | Quién lo hace | Quién responde | A quién se consulta | A quién se informa |
|---|---|---|---|---|
| Escribir y derogar reglas de `base/` | Agente | Autor | Autor | — |
| Aprobar el cambio, y aparte el commit | Autor | Autor | — | — |
| Validadores y enganches | Agente | Autor | Autor | — |
| Versionar (`CHANGELOG` y `VERSION`) | Agente | Autor | — | Proyectos que heredan |

**Quién aprueba las entregas: el autor.** Que apruebe el cambio no es que apruebe el commit: se pregunta aparte.

## 12. Interesados y comunicación

| Interesado | Qué papel tiene | Influencia | Qué recibe | Cada cuánto | En qué formato |
|---|---|---|---|---|---|
| Ing. José Dúmar Jiménez Ruíz | Paga, usa y aprueba, los tres | Alta | El cambio antes de commitear | Por sesión | En el chat, con el enlace al archivo |
| Proyectos que heredan el estándar | Consumen las reglas | Ninguna | Aviso de desfase y `CHANGELOG` | Al abrir sesión | Aviso automático |
| El agente de la sesión siguiente | Ejecuta lo escrito | Ninguna | Histórico, resumen, señales y memoria | Al abrir sesión | Archivos del repositorio |

## 13. Plan de calidad

| Qué se exige | Cómo se mide | Umbral para aceptar |
|---|---|---|
| Toda regla pasa el checklist del estándar | Se aplica el checklist de 20 filas y se sella el resultado | Sin ❌ |
| Toda regla validable tiene su validador | `validadores/reglas-validables.md` frente a `validadores/` | Sin regla validable huérfana |
| Ningún documento se entrega con marcas `«…»` | `13·DOC20`, comprobado por validador | Cero marcas al cerrar |
| Cada cambio de `base/` o `plantillas/` versiona | Entrada en `CHANGELOG.md` y `VERSION` subido | Sin cambio sin versionar |

Los criterios de aceptación por funcionalidad no van acá: viven en [plantillas/ciclo-vida-proyectos/04-HU.md](../../plantillas/ciclo-vida-proyectos/04-HU.md) y su comprobación en [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md).

## 14. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Acta de constitución (*project charter*) | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), sección 1 | Autor — se firma | Pendiente |
| Estudio de viabilidad | [plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md](../../plantillas/ciclo-vida-proyectos/12-estudio-factibilidad.md) | Autor — se firma | Pendiente; la conclusión está en la sección 4 |
| Visión y alcance | [plantillas/ciclo-vida-proyectos/01-planteamiento.md](../../plantillas/ciclo-vida-proyectos/01-planteamiento.md), secciones 1 a 4 | Autor — se firma | Pendiente |
| Plan de proyecto | [plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md](../../plantillas/ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md), secciones 2 a 5 | Autor | Pendiente |
| Cronograma con hitos y fecha | Sección 8 de este documento | Autor | Listo, sin fecha de entrega |
| Presupuesto | Sección 6 de este documento | Autor | N/A |
| Desglose del trabajo (WBS/EDT) | Sección 8 de este documento | Autor | Listo, con las épicas como desglose |
| Registro de riesgos | Sección 10 de este documento | Autor | Listo |
| Roles y matriz de responsabilidades | Sección 11 de este documento | Autor | Listo |
| Estimación de esfuerzo | Sección 7 de este documento | Autor | N/A, nunca se estimó |
| Plan de calidad | Sección 13 de este documento | Autor | Listo |
| Plan de comunicaciones | Sección 12 de este documento | Autor y proyectos que heredan | Listo |

## 15. La decisión de la etapa

**Se hace**, decidido por el autor antes de la v1.0.0 y ratificado al retrodocumentar el 2026-08-22.

El proyecto ya mostró su valor en uso: la corrección que antes se repetía cada sesión hoy está escrita y se comprueba sola. Lo que falta no es decidir si se hace, sino cerrar el frente operativo —instalarlo en un proyecto que no sea del autor— antes de tratarlo como estándar y no como preferencia personal.
