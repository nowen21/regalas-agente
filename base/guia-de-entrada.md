# La guía de entrada: el paso a paso del desarrollo profesional

**Para qué sirve este documento.** Resume, en lenguaje llano, el ciclo que sigue cualquier desarrollo de software profesional (no importa el proyecto ni la tecnología) y las cualidades que un producto debe tener para poder ponerse en producción. Es la puerta de entrada para quien llega sin conocer las reglas: explica por qué se trabaja así, y cada punto enlaza a la regla o al capítulo que lo exige. **La guía explica, no legisla**: la exigencia vive en la regla enlazada, nunca acá.

---

## Primera parte: los 10 pasos del proceso

El orden es el mismo para cualquier software, del más chico al más grande. Cambia la formalidad, no el orden. En el estándar, este ciclo es la cadena que [`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) manda recorrer completa, sin saltar eslabones.

1. **Entender la necesidad.** Qué problema hay que resolver y para quién, en lenguaje de negocio, sin hablar todavía de tecnología. Si esto está mal, todo lo demás queda bien construido sobre el problema equivocado. Es el primer eslabón de la cadena de [`02·F0`](02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md): el planteamiento.

2. **Analizar el contexto.** Qué existe hoy (sistemas, procesos, datos), qué restricciones hay (presupuesto, normas, stack obligatorio) y qué es éxito medible. Aquí nace la decisión de tecnología, no antes: la tecnología es consecuencia del problema. Todo lo que el análisis afirme se verifica contra el proyecto real ([`02·F17`](02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)).

3. **Delimitar el alcance.** Qué entra, qué no entra, y qué se deja explícitamente para después. El "qué no" es tan importante como el "qué sí": los proyectos no mueren por lo que hacen sino por lo que se les fue sumando. El alcance que el usuario no ha dicho se pregunta, no se asume ([`01·C17`](01-conducta.md#c17--ante-un-pedido-que-admite-dos-lecturas-reformula-antes-de-mover-nada)).

4. **Descomponer en unidades.** El alcance se parte en piezas con valor propio (épicas, y estas en historias de usuario), cada una con **criterios de aceptación**: la definición verificable de "esto quedó bien". Sin criterio de aceptación no hay forma objetiva de decir "terminé". Las historias nacen de la plantilla central ([`13·DOC15`](13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md)) y el trabajo se ejecuta en fases, una historia por fase ([`02·F12`](02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)).

5. **Especificar y planificar cada unidad.** Antes de codificar: qué archivos se tocan, qué cambia técnicamente, cómo se prueba, cómo se revierte si sale mal, y quién lo aprueba. Sin especificación acordada no hay código ([`02·F2`](02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md)); todo plan lleva su plan de pruebas y su aprobación explícita ([`02·F4`](02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) y responde las trece preguntas ([`02·F14`](02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md)). El plan se aprueba primero y se ejecuta después; no se renegocia a mitad de camino ([`02·F9`](02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md)).

6. **Implementar.** Escribir el código siguiendo el plan, de corrido ([`02·F3`](02-flujo-de-trabajo/reglas/F3-ejecuta-seguido-el-plan-aprobado.md)) y tocando solo los archivos que el plan declara ([`02·F8`](02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Si aparece algo no previsto, se para y se propone; no se improvisa en silencio ([`02·F20`](02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

7. **Probar contra los criterios.** No "ver si funciona": ejecutar los casos diseñados en el plan de pruebas y registrar qué dio cada uno. Un criterio sin prueba ejecutada no está cumplido, aunque "se haya visto andar". Todo cambio con lógica lleva prueba ([`08·T1`](08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba)) y se implementa literal lo que el criterio pide ([`02·F19`](02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md)).

8. **Documentar y cerrar.** Qué quedó hecho, qué decisiones se tomaron y por qué, qué deuda quedó declarada. Es lo que permite que otra persona (o uno mismo en seis meses) retome sin arqueología. El trabajo y las decisiones se persisten antes de cerrar ([`02·F6`](02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md)) y ninguna fase cierra con trazabilidad incompleta ([`02·F7`](02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md)).

9. **Entregar y desplegar.** Poner la unidad en manos del usuario real, con migración de datos y plan de reversión si aplica. La migración se planifica en vez de postergarse por miedo a producción ([`02·F10`](02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)); el despliegue formal tiene su capítulo opt-in ([`18`](18-despliegue-e-infraestructura.md)).

10. **Mantener y evolucionar.** Lo entregado genera aprendizaje y pedidos nuevos, que vuelven a entrar por el paso 1. El desarrollo no es una línea: es este ciclo repetido por cada unidad. Lo aprendido se registra como señal para no perderlo ([`13·DOC5`](13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)).

La trampa clásica es saltar del paso 1 al 6: "ya sé qué quiero, empecemos a programar". Funciona los primeros días y se paga después con alcance sin control, código sin pruebas y decisiones que nadie recuerda. Estas reglas existen para hacer ese salto imposible.

---

## Segunda parte: las cualidades del producto

Los 10 pasos son la **disciplina del proceso**: garantizan que nada se salte y que todo sea verificable y rastreable. Pero "listo para producción" exige además que el **producto** tenga cualidades técnicas propias. El proceso obliga a preguntarse por ellas en el momento correcto; el trabajo de dárselas es aparte. Cada una tiene su capítulo dueño:

1. **Seguridad.** Entradas validadas, contraseñas y secretos fuera del código, permisos por rol, protección contra los ataques conocidos. Capítulo [`04 · Seguridad`](04-seguridad.md); las credenciales, además, las blinda el núcleo ([`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).

2. **Manejo de errores.** El sistema falla con mensajes útiles para el usuario y registros útiles para quien mantiene, sin exponer detalles internos y sin dejar datos a medias (operaciones todo o nada). Capítulo [`05 · Errores y logging`](05-errores-y-logging.md).

3. **Datos protegidos.** Respaldos automáticos y **probados** (un respaldo que nunca se restauró es una esperanza, no un respaldo), migraciones reversibles, datos personales tratados según la norma que aplique. Capítulos [`03 · Datos`](03-datos.md) y [`12 · Privacidad`](12-privacidad-datos.md); los datos reales los protege el núcleo ([`00·N4`](00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

4. **Pruebas automatizadas.** Una suite que cualquiera corre en un comando y que detecta regresiones cuando el cambio de hoy rompe lo de hace tres meses. Capítulo [`08 · Pruebas`](08-pruebas.md).

5. **Reproducibilidad.** El entorno se levanta desde cero con instrucciones escritas; nada depende de "la máquina donde funciona". Capítulos [`11 · Configuración y entornos`](11-configuracion-entornos.md) y [`10 · Dependencias`](10-dependencias.md).

6. **Observabilidad.** Registros, y enterarse de que el sistema se cayó antes de que lo llame el usuario. En producción real: monitoreo y alertas. Capítulo opt-in [`19 · Observabilidad y operación`](19-observabilidad-y-operacion.md).

7. **Rendimiento bajo carga real.** No el dato de prueba de 10 filas, sino el volumen que habrá en un año. Capítulo [`06 · Rendimiento`](06-rendimiento.md).

8. **Despliegue repetible y reversible.** Publicar una versión nueva es un procedimiento aburrido y documentado, no una operación heroica; y si sale mal, se vuelve atrás en minutos. Capítulo opt-in [`18 · Despliegue e infraestructura`](18-despliegue-e-infraestructura.md).

9. **Documentación de operación.** Cómo instalar, configurar, respaldar y recuperar, escrita para quien no estuvo en el desarrollo. Capítulo [`13 · Documentación`](13-documentacion/base.md), en particular [`13·DOC4`](13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md).

Los 10 pasos viven en las reglas de flujo (capítulo [`02`](02-flujo-de-trabajo/base.md), siempre obligatorias). Varias cualidades del producto son **patrones opt-in** que cada proyecto enciende en su `CLAUDE.md` cuando su realidad los exige: registros inmutables ([`15`](15-registros-inmutables.md)), despliegue ([`18`](18-despliegue-e-infraestructura.md)), observabilidad ([`19`](19-observabilidad-y-operacion.md)). Un proyecto local puede tenerlos en "no"; el día que se publique para usuarios reales, encenderlos es parte del paso 9.

---

## La frase que lo resume

**El proceso hace que el desarrollo sea confiable; las cualidades hacen que el producto lo sea.** Un equipo con proceso perfecto puede producir software frágil si nunca prueba un respaldo, y un producto técnicamente sólido construido sin proceso es imposible de mantener porque nadie sabe por qué es como es. Profesional es tener las dos cosas.

> ¿Se atravesó una palabra? Está en el [glosario](glosario.md). ¿De dónde salió esta guía? La escribió el usuario con el agente en un proyecto real y el estándar la adoptó como doctrina; si algo de acá debiera volverse regla, sigue el procedimiento del capítulo [`20`](20-meta-reglas/base.md), no se legisla desde esta página.
